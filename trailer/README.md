# Trailer package: an orchestrated pipeline

This package makes a trailer for *Operation Tidebreak*, **in its own style**, independent of the mini-series episodes. One orchestrator session oversees the work: it asks the questions, delegates every task to agents one at a time, and stops at checkpoints for the user.

## Running it

**Run this locally,** in Claude Code on your own machine. Cloud sessions can't reach YouTube, and the overseer needs to download the references and extract their frames.

1. Get the repo: clone the `claude/confident-ramanujan-b53a9q` branch of `Scout2007/Test`, or unzip the handoff zip.
2. Install Python 3.9 or newer, then run `python -m pip install yt-dlp imageio-ffmpeg numpy pillow librosa`. That gives the downloader, a bundled ffmpeg, the cut-motion analysis and beat detection; librosa is optional. For the preview passes you also need Blender 5.2 and the project's `.blend` files.
3. Open Claude Code in the repo folder.

To test the reference prep on its own:

```
python trailer/tools/prep_reference.py ref_01 "https://www.youtube.com/watch?v=..." --ranges 0:10-0:45
```

Then look in `trailer/refs/ref_01/`. Downloaded videos stay local (they're git-ignored); they're for personal study only.

## How to start

1. Open a new Claude Code session in this repo.
2. Paste the part of `ORCHESTRATOR_PROMPT.md` below its line.
3. The orchestrator sends you the questionnaire (`QUESTIONS.md`) and asks for your references. Have them ready:
   - **Video files are best.** The agents extract and study the frames, the cut points and the audio structure.
   - **Links** need timestamps of the moments you mean. Some sites can't be fetched, so attach the files or screenshots if you can.
   - **Images and stills.** Say what you like about each.

## Pipeline

```
Phase 0  questionnaire + references; the overseer downloads and prepares each one
         (cuts, frames, ±0.5 s native-rate transition strips, motion across cuts, beats, loudness)
Phase 1  one deep analyst per reference ─▶ audit (depth + 10-claim accuracy spot-check, redo loop)
         ─▶ synthesis ─▶ CHECKPOINT (round-2 questions) ─▶ world digest ─▶ BLENDER PREFLIGHT
Phase 2  style bible ─▶ review ─▶ P1 STYLE FRAMES (stills) ─▶ review ─▶ lock
Phase 3  treatments ─▶ round-robin reviews ─▶ revise ─▶ CHECKPOINT ─▶ best-parts synthesizer
         ─▶ review ─▶ P2 KEY IMAGES (stills) ─▶ review ─▶ lock
Phase 4  beat sheet (with the transition intent) ─▶ review
Phase 5  storyboard (framing, lens, movement, transition-out fields) ─▶ review (8 lenses incl. L9 transitions)
         ─▶ P3 BOARDS + TRANSITION PAIRS (stills) ─▶ review
         ─▶ P4 ANIMATIC (light animation, real transitions, temp track) ─▶ review
         ─▶ P4b KEY MOVES IN 3D (10–15 shots, real camera moves, cheap engine) ─▶ review ─▶ CHECKPOINT ─▶ lock
Phase 6  motion & timing (keyframes, 12-frame transition windows) ─▶ review
         ─▶ P5 BLOCK-OUT (Workbench renders; transition windows at full 24 fps) ─▶ review ─▶ CHECKPOINT
Phase 7  final check ─▶ TRAILER.md ─▶ FINAL CHECKPOINT
```

**Every agent checks its own capability first.** It answers `CAPABLE`, or `ESCALATE` to a stronger model, the user or a tool (`agents/00_common.md`). Film-craft roles start on the stronger model.

**Nine review lenses** (`RUBRIC.md`):
- L1: reference fidelity
- L2: distinctness
- L3: story
- L4: lore and spoilers
- L5: speech and text
- L6: cinematography
- L7: movement and editing
- L8: production
- **L9: transitions**

Lean mode trims the run to 3 treatments, second rounds only where needed, and previews P1, P3, P4 and P4b.

## Files

| File | Purpose |
|---|---|
| `ORCHESTRATOR_PROMPT.md` | The prompt to paste |
| `QUESTIONS.md` | The round-1 questionnaire, asked before any work |
| `TRAILER_BRIEF.md` | What the trailer is, its defaults, and each stage's deliverable |
| `RUBRIC.md` | The eight lenses, which run at each stage, the findings format and the stopping rule |
| `STATE.md` | The orchestrator's log and the user's answers, verbatim; it lets a session resume |
| `agents/00_common.md` | The preamble in every brief: the capability check and escalation, the shared rules |
| `agents/01–16_*.md` | The agent templates, ending with 15, previz, and 16, the Blender preflight: reference analyst, research auditor, research synthesis, world digest, style bible, treatment writer, reviewer, tally, synthesizer, beat sheet, storyboard artist, motion and timing, fixer, final check |
| `tools/blender_preview.py` | Runs inside Blender: `inventory` lists a .blend's scene facts; `render --spec shot.json` renders a still or keyed move (Workbench, EEVEE or Cycles) without saving the file |
| `tools/animatic.py` | Builds the P4 animatic and the P5 block-out from stills or clips and a timing sheet (cuts, dissolves, flashes, whips, light 2D moves) |
| `tools/prep_reference.py` | Downloads a reference and extracts its cuts, frames, contact sheets, transcript and loudness map for the agents |
| `refs/` | Your references (`REFERENCES.md`, plus one prepared folder per reference) |
| `work/` | All agent outputs: `research/`, `treatments/`, `reviews/`, the style bible, beat sheet, storyboard and motion sheet |
| `TRAILER.md` | The finished trailer package (written at phase 7) |

## Cost and pace

- **Lean run:** about 50–65 agent runs.
- **Full run:** about 85–115.
- **Preview renders:** a few hours, which the preflight measures on your machine first.
- **Time:** 2–5 days of wall time, with checkpoints and usage limits.

The run is linear, and phase summaries let it resume or move to a fresh session at any phase end.

## How the known risks are handled

| Risk | Answer | Tested |
|---|---|---|
| Blender automation fails mid-run | **Preflight (agent 16)** before any preview: an inventory of the real files, a test still, a test move, timings per engine, and a cookbook of working specs. Previews use the same tested helper (`blender_preview.py`), not ad-hoc scripts | The helper was tested here with Blender's `bpy` 5.0.1: inventory, a Cycles still, a 24-frame keyed push with a look-at camera. Workbench and EEVEE need a GPU, which this container lacks, so the preflight checks them on your machine |
| Agents claim depth but get facts wrong | The audit adds a **10-claim accuracy spot-check** per reference against the frames and data. Too many wrong or unverifiable claims means a redo | — |
| Motion only seen as frames | Every native frame for ±0.5 s around each cut, as strips. Measured **pan, zoom and rotation** across each cut. A `low_texture` flag where black space makes numbers unreliable | Tested: pans, a 1 %/frame push-in (measured 1.0108), a 2°/frame roll (2.0), static shots (1.0), and black frames (flagged) |
| No music structure | `music_sections.csv` marks silence, quiet, build, hit and sustain from loudness, plus beats and each cut's beat offset. Q8 asks for a temp track before the animatic | Tested on a synthetic quiet-to-loud click track |
| Flat 2D animatic hides 3D problems | **P4b**: the 10–15 key shots as real 3D moves, cheaply, before the motion sheet and the full block-out | — |
| Questionnaire overload | **12 must-answer questions**; the rest have stated defaults | — |
| Scene detection errors | Hard and soft thresholds, flash candidates, and confirmation by eye against the strips | Tested |
| One model's blind spots | Capability checks with escalation; film-craft roles and the L6, L7 and L9 reviewers on the stronger model; your checkpoints | — |
| Long runs and the overseer's context | Phase summaries, fresh sessions at phase ends, linear runs, lean mode | — |
| Fix loops ping-pong | Locked decisions; a loop that flips twice goes to you | — |
| Copying references | Technique, not content; local-only downloads; the L2 lens | — |
