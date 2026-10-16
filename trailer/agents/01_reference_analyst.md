# Agent 01 · Reference analyst (one reference per run)

**Goal.** An in-depth, evidence-backed breakdown of **one** reference. Not a summary: a technical study someone could rebuild the format from.

**Input from the orchestrator:**
- the reference's row in `trailer/refs/REFERENCES.md`;
- its files;
- the user's verbatim notes on it;
- the output path `trailer/work/research/ref_NN.md`.

## Getting at the material

The orchestrator has already prepared `trailer/refs/ref_NN/` with `trailer/tools/prep_reference.py`:
- `manifest.md`;
- `cuts.csv`, the detected cuts;
- `frames/cut_*.jpg`, the first frame of each shot;
- `frames/ts_*.jpg`, one frame per second in the user's ranges;
- `sheets/sheet_*.jpg`, a frame every 2 s with timecodes;
- `loudness.csv` and `silences.csv`;
- `transcript.txt`, when captions exist;
- `info.json`;
- the video itself, local only.

**Start there.**
- Read the manifest.
- Look at every contact sheet and every cut frame.
- Look at all the range frames.
- Use `cuts.csv` for timings. Confirm each cut against the frames, because scene detection misses dissolves and splits flashes into extra cuts.
- Use `loudness.csv` for the music map.

When you need a closer look, extract more frames from the local video with ffmpeg: around a fast sequence, or at a specific timestamp.

If the folder is missing anything, use the fallbacks below:

- **A video file:**
  1. Check for `ffmpeg` and `ffprobe`. If they're missing, try `pip install imageio-ffmpeg` and use its binary. Run downloaded media tools in their own folder, and pass paths as arguments.
  2. Probe its length, resolution, frame rate and aspect.
  3. Extract frames with scene-change detection (`select='gt(scene,0.3)'`), plus one frame every second through the user's timestamps. Write the frames to `trailer/work/research/frames/ref_NN/`.
  4. **Look at the frames** (read the images).
  5. Build the cut list from the scene-change times.
  6. Extract the audio, and use `ffmpeg`'s `silencedetect` and `astats` to map loud and quiet sections, so the music and silence structure is measured, not guessed.
- **A link:**
  - Fetch the page with your fetch tool, or with the `web-fetch` agent type.
  - Get the title, length, description, chapters and any transcript or captions.
  - If downloading is possible (try `yt-dlp` if present), treat the download as a video file, above.
  - If you can neither download nor see it, say so plainly. Ask (through your reply) for the file or for screenshots, and analyse only what you can verify.
- **Images:** read every one. Describe composition, framing, type, colour and grain in detail.

## The breakdown

Write it to `ref_NN.md`. Cite evidence for every claim: a timestamp, a frame file or a transcript line. Where something is inferred, label it **INFERRED** and give the reason.

1. **Identity.** What it is, its length, its aspect ratio and frame rate, and what the user wants from it, verbatim.
2. **Structure.**
   - acts and sections with timecodes;
   - where the hook is, the turn, the climax and the button;
   - how it opens and how it ends.
3. **Shot list.** For every shot you can see, or for the user's timestamped range if the reference is long:
   - timecode in and out;
   - duration;
   - shot size;
   - lens feel (wide, normal or long; depth of field);
   - angle;
   - composition (subject placement, negative space, leading lines);
   - camera movement: type, direction, speed, easing, motivation;
   - lighting and colour;
   - transition into the next shot.
4. **Rhythm.**
   - the average and median shot length per section;
   - a chart of cut timings (a table is enough);
   - how the rhythm accelerates, and where it holds.
5. **Sound.**
   - the music's structure (intro, build, drop, silence), mapped to timecodes;
   - sound design, voice, and how sound and cuts sync (cuts on beats or off them);
   - J-cuts and L-cuts.
6. **Text and type.**
   - every card: its words, typeface feel, size and placement, timing and animation;
   - the copy's voice.
7. **Signature devices.** What makes this reference itself, the things a viewer would remember.
8. **What transfers.** What we can use in our trailer, translated into our world and our 3D-only means. Mark each as a technique to borrow, never content to copy.
9. **What doesn't transfer, and why:** live action, actors, budget, and so on.
10. **Open questions for the user** that this reference raises.

**Depth bar.**
- A video reference gets a shot list covering all of it, or at least the user's ranges, with every column filled.
- A one-paragraph summary fails, and the research audit will send it back.

**Reply** in at most 8 lines: the path, what you could and couldn't access, the shot count analysed, three signature devices, and your questions for the user.
