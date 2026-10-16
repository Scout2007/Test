#!/usr/bin/env python3
"""Build a preview animatic from stills or block-out clips and a timing sheet.

    pip install imageio-ffmpeg          (or have ffmpeg on PATH)
    python trailer/tools/animatic.py trailer/work/previz/p4_timing.csv trailer/work/previz/p4_animatic.mp4 [--audio temp.wav] [--width 1280]

The timing sheet is a CSV with a header row:
    shot,source,duration_s,move,transition,transition_frames
- source: an image (a still: style frame, board frame) or a video clip (a block-out render). Relative paths
  resolve from the CSV's folder.
- move (stills only): none | push | pull | pan_l | pan_r | tilt_u | tilt_d. It is a light 2D move standing in
  for the planned camera move (P4); block-out clips carry their own movement (P5).
- transition INTO the next shot: cut | dissolve | fade_black | flash_white | whip_l | whip_r | smash. For a
  cut or a smash, transition_frames is ignored.
- duration_s includes the transition overlap: a 24-frame dissolve takes its frames from both neighbours.

Output: the animatic at 24 fps and 2.39:1 (letterboxed sources are fitted), plus <output>.cuts.csv with every
cut or transition centre time. To study its transitions the same way as the references:
    python trailer/tools/prep_reference.py anim_p4 trailer/work/previz/p4_animatic.mp4 --no-beats --out trailer/work/previz/analysis
"""
import csv
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

FPS = 24
XFADE = {"dissolve": "fade", "fade_black": "fadeblack", "flash_white": "fadewhite", "whip_l": "slideleft",
         "whip_r": "slideright"}


def ffmpeg_bin():
    exe = shutil.which("ffmpeg")
    if exe:
        return exe
    try:
        import imageio_ffmpeg
        return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("ffmpeg not found: install it, or run  pip install imageio-ffmpeg")


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, errors="replace")
    if r.returncode:
        sys.exit("ffmpeg failed:\n" + " ".join(cmd) + "\n" + r.stderr[-1500:])
    return r


def zoompan(move, frames, w, h):
    n = max(frames - 1, 1)
    z = {"push": f"1+0.08*on/{n}", "pull": f"1.08-0.08*on/{n}"}.get(move, "1.08" if move.startswith(("pan", "tilt")) else "1")
    x = {"pan_l": f"(iw-iw/zoom)*(1-on/{n})", "pan_r": f"(iw-iw/zoom)*on/{n}"}.get(move, "(iw-iw/zoom)/2")
    y = {"tilt_u": f"(ih-ih/zoom)*(1-on/{n})", "tilt_d": f"(ih-ih/zoom)*on/{n}"}.get(move, "(ih-ih/zoom)/2")
    return f"zoompan=z='{z}':x='{x}':y='{y}':d={frames}:s={w}x{h}:fps={FPS}"


def clip(ff, src, dur, move, w, h, out):
    frames = max(1, round(dur * FPS))
    fit = f"scale={w * 2}:{h * 2}:force_original_aspect_ratio=decrease,pad={w * 2}:{h * 2}:(ow-iw)/2:(oh-ih)/2"
    if src.suffix.lower() in (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff"):
        vf = f"{fit},{zoompan(move, frames, w, h)},format=yuv420p"
        run([ff, "-hide_banner", "-y", "-loop", "1", "-i", str(src), "-vf", vf, "-frames:v", str(frames),
             "-c:v", "libx264", "-crf", "20", "-r", str(FPS), str(out)])
    else:
        vf = f"fps={FPS},scale={w}:{h}:force_original_aspect_ratio=decrease,pad={w}:{h}:(ow-iw)/2:(oh-ih)/2,format=yuv420p"
        run([ff, "-hide_banner", "-y", "-i", str(src), "-vf", vf, "-frames:v", str(frames), "-an",
             "-c:v", "libx264", "-crf", "20", str(out)])
    return frames / FPS


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    sheet, out = Path(sys.argv[1]), Path(sys.argv[2])
    w = int(sys.argv[sys.argv.index("--width") + 1]) if "--width" in sys.argv else 1280
    w -= w % 2
    h = round(w / 2.39 / 2) * 2
    ff = ffmpeg_bin()
    rows = list(csv.DictReader(open(sheet, newline="")))
    tmp = Path(tempfile.mkdtemp(prefix="animatic_"))
    clips = []
    for i, r in enumerate(rows):
        src = Path(r["source"])
        src = src if src.is_absolute() else sheet.parent / src
        if not src.exists():
            sys.exit(f"shot {r['shot']}: missing source {src}")
        d = clip(ff, src, float(r["duration_s"]), (r.get("move") or "none").strip(), w, h, tmp / f"c{i:03d}.mp4")
        clips.append((tmp / f"c{i:03d}.mp4", d, (r.get("transition") or "cut").strip(),
                      int(r.get("transition_frames") or 0)))
    # join one clip at a time: concat for cuts, xfade for everything else
    acc, acc_len, marks = clips[0][0], clips[0][1], []
    for i in range(1, len(clips)):
        nxt, d, _, _ = clips[i]
        kind, tf = clips[i - 1][2], clips[i - 1][3]
        joined = tmp / f"j{i:03d}.mp4"
        if kind in XFADE and tf > 0:
            dur = tf / FPS
            off = acc_len - dur
            run([ff, "-hide_banner", "-y", "-i", str(acc), "-i", str(nxt), "-filter_complex",
                 f"[0:v][1:v]xfade=transition={XFADE[kind]}:duration={dur:.4f}:offset={off:.4f},format=yuv420p",
                 "-c:v", "libx264", "-crf", "20", str(joined)])
            marks.append((rows[i - 1]["shot"], rows[i]["shot"], round(off + dur / 2, 3), kind))
            acc_len = acc_len + d - dur
        else:
            lst = tmp / f"l{i:03d}.txt"
            lst.write_text(f"file '{acc.as_posix()}'\nfile '{nxt.as_posix()}'\n")
            run([ff, "-hide_banner", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(joined)])
            marks.append((rows[i - 1]["shot"], rows[i]["shot"], round(acc_len, 3), kind if kind == "smash" else "cut"))
            acc_len += d
        acc = joined
    out.parent.mkdir(parents=True, exist_ok=True)
    if "--audio" in sys.argv:
        audio = sys.argv[sys.argv.index("--audio") + 1]
        run([ff, "-hide_banner", "-y", "-i", str(acc), "-i", audio, "-map", "0:v", "-map", "1:a", "-c:v", "copy",
             "-c:a", "aac", "-shortest", str(out)])
    else:
        shutil.copy(acc, out)
    with open(str(out) + ".cuts.csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["from_shot", "to_shot", "time_s", "transition"])
        wr.writerows(marks)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"wrote {out}: {len(rows)} shots, {acc_len:.2f} s, {w}x{h} at {FPS} fps; transitions in {out}.cuts.csv")


if __name__ == "__main__":
    main()
