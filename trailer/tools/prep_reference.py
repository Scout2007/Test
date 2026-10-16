#!/usr/bin/env python3
"""Prepare one trailer reference for the analyst agents: download, frames, cut list, transcript, loudness map.

    pip install yt-dlp imageio-ffmpeg        (or have ffmpeg and yt-dlp on PATH)
    python trailer/tools/prep_reference.py ref_01 "https://www.youtube.com/watch?v=..." [--ranges 0:12-0:40,1:05-1:20]
    python trailer/tools/prep_reference.py ref_02 path/to/video.mp4

Writes trailer/refs/ref_NN/:
  video.*          the media (git-ignored)
  info.json        yt-dlp metadata, when downloaded
  subs.*.vtt       captions or auto-captions, when available; transcript.txt is the plain text
  cuts.csv         every detected cut: index, time (s), scene score
  frames/cut_*.jpg one frame per detected cut (the first frame of each shot)
  frames/ts_*.jpg  one frame per second inside each --ranges window
  sheets/sheet_*.jpg contact sheets, one frame every 2 s, 6x5 per sheet, timecode printed on each
  loudness.csv     RMS level every 0.5 s (dB), for the music and silence map
  silences.csv     silent stretches (below -40 dB for at least 0.4 s)
  manifest.md      a summary for the agents: duration, resolution, fps, cut count, average shot length, files

Personal study use only: keep downloaded media out of the repository (see trailer/.gitignore).
"""
import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "refs"


def ffmpeg_bin():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg not found: install it, or run  pip install imageio-ffmpeg")


def run(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, errors="replace", **kw)


def download(url, out):
    ytdlp = shutil.which("yt-dlp")
    base = [ytdlp] if ytdlp else [sys.executable, "-m", "yt_dlp"]
    cmd = base + ["-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/b[height<=1080]/b", "--merge-output-format", "mp4",
                  "--ffmpeg-location", ffmpeg_bin(), "--write-info-json", "--write-subs", "--write-auto-subs",
                  "--sub-langs", "en.*", "--sub-format", "vtt", "-o", str(out / "video.%(ext)s"), url]
    r = run(cmd)
    if r.returncode:
        sys.exit("yt-dlp failed:\n" + r.stderr[-2000:])
    for f in out.glob("video.info.json"):
        f.rename(out / "info.json")
    for f in out.glob("video.*.vtt"):
        f.rename(out / ("subs." + f.name.split(".", 1)[1]))
    vids = [f for f in out.glob("video.*") if f.suffix in (".mp4", ".mkv", ".webm")]
    if not vids:
        sys.exit("no video file after download")
    return vids[0]


def probe(ff, video):
    err = run([ff, "-hide_banner", "-i", str(video)]).stderr
    dur = re.search(r"Duration: (\d+):(\d+):([\d.]+)", err)
    seconds = int(dur.group(1)) * 3600 + int(dur.group(2)) * 60 + float(dur.group(3)) if dur else 0.0
    res = re.search(r"Video:.*?(\d{2,5})x(\d{2,5})", err)
    fps = re.search(r"([\d.]+) fps", err)
    return {"duration": round(seconds, 2), "width": int(res.group(1)) if res else None,
            "height": int(res.group(2)) if res else None, "fps": float(fps.group(1)) if fps else None}


def tc(s):
    return f"{int(s // 60)}:{s % 60:05.2f}"


def cuts(ff, video, frames, threshold=0.3):
    r = run([ff, "-hide_banner", "-i", str(video), "-vf", f"select='gt(scene,{threshold})',showinfo,scale=640:-2",
             "-vsync", "vfr", "-q:v", "3", str(frames / "cut_%04d.jpg")])
    times = [float(t) for t in re.findall(r"pts_time:([\d.]+)", r.stderr)]
    scores = re.findall(r"scene_score=([\d.]+)", r.stderr) or [""] * len(times)
    return list(zip(times, scores + [""] * (len(times) - len(scores))))


def ranges_frames(ff, video, frames, ranges):
    for i, rng in enumerate(ranges, 1):
        a, b = [parse_time(x) for x in rng.split("-")]
        run([ff, "-hide_banner", "-ss", str(a), "-to", str(b), "-i", str(video), "-vf", "fps=1,scale=960:-2",
             "-q:v", "3", str(frames / f"ts_r{i}_%03d.jpg")])


def parse_time(s):
    parts = [float(p) for p in s.strip().split(":")]
    return sum(p * 60 ** i for i, p in enumerate(reversed(parts)))


def sheets(ff, video, out):
    out.mkdir(exist_ok=True)
    vf = ("fps=1/2,scale=320:-2,drawtext=text='%{pts\\:hms}':x=6:y=6:fontsize=18:fontcolor=white:box=1:boxcolor=black@0.6,"
          "tile=6x5")
    r = run([ff, "-hide_banner", "-i", str(video), "-vf", vf, "-q:v", "4", str(out / "sheet_%02d.jpg")])
    if not list(out.glob("sheet_*.jpg")):            # some ffmpeg builds lack drawtext: retry without timecodes
        run([ff, "-hide_banner", "-i", str(video), "-vf", "fps=1/2,scale=320:-2,tile=6x5", "-q:v", "4",
             str(out / "sheet_%02d.jpg")])
    return r


def loudness(ff, video, out):
    r = run([ff, "-hide_banner", "-i", str(video), "-vn", "-af",
             "aresample=16000,asetnsamples=8000,astats=metadata=1:reset=1,"
             "ametadata=print:key=lavfi.astats.Overall.RMS_level", "-f", "null", "-"])
    t = re.findall(r"pts_time:([\d.]+)", r.stderr)
    v = re.findall(r"RMS_level=(-?[\d.]+|-inf)", r.stderr)
    with open(out / "loudness.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time_s", "rms_db"])
        w.writerows(zip(t, v))
    s = run([ff, "-hide_banner", "-i", str(video), "-vn", "-af", "silencedetect=noise=-40dB:d=0.4", "-f", "null", "-"])
    starts = re.findall(r"silence_start: ([\d.]+)", s.stderr)
    ends = re.findall(r"silence_end: ([\d.]+) \| silence_duration: ([\d.]+)", s.stderr)
    with open(out / "silences.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["start_s", "end_s", "duration_s"])
        for a, (b, d) in zip(starts, ends):
            w.writerow([a, b, d])
    return len(t), len(ends)


def transcript(out):
    vtts = sorted(out.glob("subs.*.vtt"))
    if not vtts:
        return False
    lines, last = [], None
    for line in vtts[0].read_text(errors="replace").splitlines():
        if "-->" in line:
            stamp = line.split("-->")[0].strip()
            continue
        text = re.sub(r"<[^>]+>", "", line).strip()
        if text and not text.startswith(("WEBVTT", "Kind:", "Language:")) and text != last:
            lines.append(f"[{stamp}] {text}")
            last = text
    (out / "transcript.txt").write_text("\n".join(lines))
    return True


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    ref, src = sys.argv[1], sys.argv[2]
    ranges = sys.argv[sys.argv.index("--ranges") + 1].split(",") if "--ranges" in sys.argv else []
    out = ROOT / ref
    frames = out / "frames"
    frames.mkdir(parents=True, exist_ok=True)
    ff = ffmpeg_bin()
    if re.match(r"https?://", src):
        video = download(src, out)
    else:
        video = out / ("video" + Path(src).suffix)
        shutil.copy(src, video)
    info = probe(ff, video)
    cut_list = cuts(ff, video, frames)
    with open(out / "cuts.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cut", "time_s", "timecode", "scene_score"])
        for i, (t, s) in enumerate(cut_list, 1):
            w.writerow([i, round(t, 3), tc(t), s])
    if ranges:
        ranges_frames(ff, video, frames, ranges)
    sheets(ff, video, out / "sheets")
    n_loud, n_sil = loudness(ff, video, out)
    has_subs = transcript(out)
    title = ""
    if (out / "info.json").exists():
        meta = json.loads((out / "info.json").read_text())
        title = f"{meta.get('title', '')} ({meta.get('uploader', '')})"
    shots = len(cut_list) + 1
    asl = info["duration"] / shots if shots else 0
    (out / "manifest.md").write_text(
        f"# {ref}\n\n- Source: {src}\n- Title: {title or 'n/a'}\n- Duration: {tc(info['duration'])} ({info['duration']} s)\n"
        f"- Resolution: {info['width']}x{info['height']} · {info['fps']} fps\n"
        f"- Detected cuts: {len(cut_list)} (scene threshold 0.3) → {shots} shots, average shot length {asl:.2f} s\n"
        f"- Frames: {len(list(frames.glob('cut_*.jpg')))} cut frames, {len(list(frames.glob('ts_*.jpg')))} range frames "
        f"({', '.join(ranges) or 'no ranges given'})\n"
        f"- Contact sheets: {len(list((out / 'sheets').glob('*.jpg')))} (one frame every 2 s)\n"
        f"- Loudness samples: {n_loud} (every 0.5 s) · silences: {n_sil}\n"
        f"- Transcript: {'transcript.txt' if has_subs else 'none available'}\n\n"
        "Scene detection misses dissolves and fast flashes and may split camera flashes into extra cuts: "
        "the analyst confirms cuts against the frames and contact sheets.\n")
    print((out / "manifest.md").read_text())


if __name__ == "__main__":
    main()
