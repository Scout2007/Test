#!/usr/bin/env python3
"""Prepare one trailer reference for the analyst agents: download, frames, cut list, transcript, loudness map.

    pip install yt-dlp imageio-ffmpeg        (or have ffmpeg and yt-dlp on PATH)
    python trailer/tools/prep_reference.py ref_01 "https://www.youtube.com/watch?v=..." [--ranges 0:12-0:40,1:05-1:20]
    python trailer/tools/prep_reference.py ref_02 path/to/video.mp4 [--cut-window 0.5] [--no-beats] [--out DIR]

Optional extras: pip install numpy pillow (transition motion and strips), librosa (beats and tempo).

Writes trailer/refs/ref_NN/:
  video.*          the media (git-ignored)
  info.json        yt-dlp metadata, when downloaded
  subs.*.vtt       captions or auto-captions, when available; transcript.txt is the plain text
  cuts.csv         every detected cut: index, time (s), kind (hard / soft: a possible dissolve or soft cut / flash)
  frames/cut_*.jpg one frame per detected cut (the first frame of each shot)
  frames/ts_*.jpg  one frame per second inside each --ranges window
  sheets/sheet_*.jpg contact sheets, one frame every 2 s, 6x5 per sheet, timecode printed on each
  loudness.csv     RMS level every 0.5 s (dB), for the music and silence map
  silences.csv     silent stretches (below -40 dB for at least 0.4 s)
  transitions/cut_NNN.jpg  a strip per cut: every native frame from --cut-window s before to after the cut
  transitions.csv  per cut: picture motion out of and into the cut (dx, dy in px/frame at 320 px wide, by phase
                   correlation, ±1 px; negative dx = the picture moves left, i.e. the camera pans right),
                   luma and mean colour either side, whether motion carries across, and a flash hint
  beats.csv        beat times and tempo (librosa if installed, else an onset-energy estimate); cuts.csv then
                   gains each cut's offset from the nearest beat
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


def cuts(ff, video, frames, hard=0.3, soft=0.12):
    """Hard cuts above `hard`; changes between `soft` and `hard` are kept as possible soft cuts or dissolves."""
    r = run([ff, "-hide_banner", "-i", str(video), "-vf",
             f"select='gt(scene,{soft})',metadata=print:key=lavfi.scene_score,showinfo,scale=640:-2",
             "-vsync", "vfr", "-q:v", "3", str(frames / "cut_%04d.jpg")])
    times = [float(t) for t in re.findall(r"Parsed_showinfo[^\n]*?pts_time:([\d.]+)", r.stderr)]
    scores = [float(x) for x in re.findall(r"lavfi\.scene_score=([\d.]+)", r.stderr)]
    scores += [hard] * (len(times) - len(scores))
    out = []
    for i, (t, sc) in enumerate(zip(times, scores)):
        kind = "hard" if sc >= hard else "soft"
        # a cut followed by another within 3 frames and a return is treated as a flash candidate
        if i + 1 < len(times) and times[i + 1] - t < 0.13:
            kind = "flash?"
        out.append((t, round(sc, 3), kind))
    return out


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


def transitions(ff, video, out, cut_list, fps, window):
    """Native-rate frames around every cut, a strip image per cut, and global motion either side of it."""
    try:
        import numpy as np
        from PIL import Image
    except ImportError:
        return "skipped (pip install numpy pillow)"
    tdir = out / "transitions"
    tdir.mkdir(exist_ok=True)
    rows = []
    for n, (t, sc, kind) in enumerate(cut_list, 1):
        a = max(0.0, t - window)
        tmp = tdir / f"_c{n:03d}"
        tmp.mkdir(exist_ok=True)
        run([ff, "-hide_banner", "-ss", f"{a:.3f}", "-t", f"{2 * window:.3f}", "-i", str(video),
             "-vf", "scale=320:-2", "-q:v", "4", str(tmp / "f_%03d.jpg")])
        files = sorted(tmp.glob("f_*.jpg"))
        if len(files) < 4:
            continue
        imgs = [Image.open(f).convert("RGB") for f in files]
        k = min(range(len(files)), key=lambda i: abs(a + i / (fps or 24) - t))   # first frame of the new shot
        w, h = imgs[0].size
        per_row = max(k, len(imgs) - k)
        strip = Image.new("RGB", (w * per_row, h * 2 + 6), (255, 0, 0))
        for i, im in enumerate(imgs[:k]):
            strip.paste(im, (w * (per_row - k + i), 0))                       # row 1: outgoing shot, ending at right
        for i, im in enumerate(imgs[k:]):
            strip.paste(im, (w * i, h + 6))                                    # row 2: incoming shot, from left
        strip.save(tdir / f"cut_{n:03d}.jpg", quality=80)
        g = [np.asarray(im.convert("L"), dtype=np.float32) for im in imgs]

        def motion(x, y):
            fx, fy = np.fft.fft2(x - x.mean()), np.fft.fft2(y - y.mean())
            r = fx * np.conj(fy)
            c = np.abs(np.fft.ifft2(r / (np.abs(r) + 1e-6)))
            dy, dx = np.unravel_index(np.argmax(c), c.shape)
            dy = dy - c.shape[0] if dy > c.shape[0] // 2 else dy
            dx = dx - c.shape[1] if dx > c.shape[1] // 2 else dx
            return -dx, -dy

        def mean_motion(seq):
            if len(seq) < 2:
                return (0.0, 0.0)
            v = [motion(seq[i], seq[i + 1]) for i in range(len(seq) - 1)]
            return (round(float(np.median([p[0] for p in v])), 2), round(float(np.median([p[1] for p in v])), 2))

        out_m, in_m = mean_motion(g[:k]), mean_motion(g[k:])
        lo, li = float(g[k - 1].mean()), float(g[k].mean())
        co = [round(float(c), 1) for c in np.asarray(imgs[k - 1]).reshape(-1, 3).mean(0)]
        ci = [round(float(c), 1) for c in np.asarray(imgs[k]).reshape(-1, 3).mean(0)]
        same_dir = (out_m[0] * in_m[0] > 0) or (out_m[1] * in_m[1] > 0)
        flash = max(float(x.mean()) for x in g[max(0, k - 2):k + 2]) > max(lo, li) + 60
        rows.append([n, round(t, 3), kind, out_m[0], out_m[1], in_m[0], in_m[1], round(lo, 1), round(li, 1),
                     "/".join(map(str, co)), "/".join(map(str, ci)), "yes" if same_dir else "", "yes" if flash else ""])
        for f in files:
            f.unlink()
        tmp.rmdir()
    with open(out / "transitions.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cut", "time_s", "kind", "out_dx", "out_dy", "in_dx", "in_dy", "luma_out", "luma_in",
                    "rgb_out", "rgb_in", "motion_carries", "flash"])
        w.writerows(rows)
    return f"{len(rows)} cuts, ±{window} s at native rate"


def beats(ff, video, out):
    """Beat times and tempo. librosa if available; otherwise an onset-energy estimate."""
    wav = out / "_audio.wav"
    run([ff, "-hide_banner", "-y", "-i", str(video), "-vn", "-ac", "1", "-ar", "22050", str(wav)])
    if not wav.exists():
        return None, []
    try:
        import librosa
        y, sr = librosa.load(str(wav), sr=22050)
        tempo, frames = librosa.beat.beat_track(y=y, sr=sr)
        times = librosa.frames_to_time(frames, sr=sr).tolist()
        tempo, method = float(tempo if not hasattr(tempo, "__len__") else tempo[0]), "librosa"
    except Exception:
        try:
            import numpy as np
            import wave
            with wave.open(str(wav)) as w:
                y = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)
            hop = 512
            env = np.array([np.sqrt(np.mean(y[i:i + 1024] ** 2)) for i in range(0, len(y) - 1024, hop)])
            flux = np.maximum(np.diff(env), 0)
            thr = flux.mean() + 1.5 * flux.std()
            times = [i * hop / 22050 for i in range(1, len(flux) - 1)
                     if flux[i] > thr and flux[i] >= flux[i - 1] and flux[i] >= flux[i + 1]]
            iv = np.diff(times) if len(times) > 2 else []
            tempo = float(60 / np.median(iv)) if len(iv) else 0.0
            method = "onset-energy estimate"
        except Exception:
            wav.unlink(missing_ok=True)
            return None, []
    wav.unlink(missing_ok=True)
    with open(out / "beats.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["beat", "time_s"])
        w.writerows([(i + 1, round(t, 3)) for i, t in enumerate(times)])
    return f"{tempo:.1f} BPM ({method})", times


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
    out = (Path(sys.argv[sys.argv.index("--out") + 1]) if "--out" in sys.argv else ROOT) / ref
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
    tempo, beat_times = (None, []) if "--no-beats" in sys.argv else beats(ff, video, out)
    with open(out / "cuts.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["cut", "time_s", "timecode", "scene_score", "kind", "nearest_beat_offset_s"])
        for i, (t, sc, kind) in enumerate(cut_list, 1):
            off = min((t - b for b in beat_times), key=abs) if beat_times else ""
            w.writerow([i, round(t, 3), tc(t), sc, kind, round(off, 3) if off != "" else ""])
    window = float(sys.argv[sys.argv.index("--cut-window") + 1]) if "--cut-window" in sys.argv else 0.5
    trans = transitions(ff, video, out, cut_list, info["fps"], window)
    if ranges:
        ranges_frames(ff, video, frames, ranges)
    sheets(ff, video, out / "sheets")
    n_loud, n_sil = loudness(ff, video, out)
    has_subs = transcript(out)
    title = ""
    if (out / "info.json").exists():
        meta = json.loads((out / "info.json").read_text())
        title = f"{meta.get('title', '')} ({meta.get('uploader', '')})"
    hard = [c for c in cut_list if c[2] == "hard"]
    shots = len(hard) + 1
    asl = info["duration"] / shots if shots else 0
    (out / "manifest.md").write_text(
        f"# {ref}\n\n- Source: {src}\n- Title: {title or 'n/a'}\n- Duration: {tc(info['duration'])} ({info['duration']} s)\n"
        f"- Resolution: {info['width']}x{info['height']} · {info['fps']} fps\n"
        f"- Detected cuts: {len(hard)} hard (score ≥ 0.3) → {shots} shots, average shot length {asl:.2f} s; "
        f"{len(cut_list) - len(hard)} soft or flash candidates to confirm by eye\n"
        f"- Transitions: {trans} (transitions/cut_NNN.jpg: top row = outgoing shot ending at the right; "
        f"bottom row = incoming shot from the left; transitions.csv)\n"
        f"- Beats: {tempo or 'none (pip install librosa, or no audio)'}; cuts.csv gives each cut's offset from the nearest beat\n"
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
