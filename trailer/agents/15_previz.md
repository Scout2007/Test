# Agent 15 · Previz (preview passes P1–P5)

**Goal.** Make the current stage visible, so you and the reviewers judge pictures and motion, not prose. Each pass builds on the last, moving from stills to light animation to block-outs.

**Tools.** These run on the user's machine:
- Blender 5.2, run headless: `blender -b <file.blend> --python <script.py> -- <args>`;
- the project's `.blend` files and helper scripts (`pack/project_docs/README_blender_project.md`: `LREF_Endeavor.blend`, `LREF_Railcannon_M1C.blend`, `render_previews.py` and friends);
- `trailer/tools/animatic.py` and `trailer/tools/prep_reference.py`.

Start with `blender --version`. If Blender or the files are missing, escalate to the user (see 00_common), and don't fake renders.

**Engines.**
- Workbench (solid or flat) for block-outs.
- EEVEE for style frames and boards, at around 960–1280 px wide, 2.39:1.
- Cycles only if the style bible depends on it, and only for P1.

Put every script you write in `trailer/work/previz/scripts/`, so the passes can be repeated.

## The passes

The orchestrator names which one to run.

| Pass | When | Make | Output in `trailer/work/previz/` |
|---|---|---|---|
| **P1 · Style frames** (static) | After the style bible | 4–6 hero stills that prove the look: lens, colour script, grain, light, type on one frame | `p1/frame_NN.png`, `p1/sheet.png` (all frames on one sheet), `p1/notes.md` |
| **P2 · Key images** (static) | After the merged treatment | One still per key image in the treatment, framed as described | `p2/key_NN.png`, `p2/sheet.png`, `p2/notes.md` |
| **P3 · Boards** (static) | After the storyboard | Per shot, its first frame, plus its last frame if it moves. Per cut, a **transition pair**: the outgoing last frame beside the incoming first frame, side by side and at the same size | `p3/shot_NNN_a.png`, `_b.png`, `p3/cut_NNN_pair.png`, `p3/board_sheet_*.png` |
| **P4 · Animatic** (light animation) | After the storyboard is clean | P3's boards cut to the timing sheet with `animatic.py`, using light 2D moves (push, pull, pan, tilt) to stand in for each camera move, and the storyboard's transitions (dissolve, flash, whip, smash). Use the temp audio if the user supplied it, or a click track at the music map's tempo | `p4/timing.csv`, `p4/animatic.mp4`, `p4/analysis/` (run `prep_reference.py` on the animatic with `--out`) |
| **P5 · Block-out** (blocked animation) | After the motion and timing sheet | The real camera moves from `motion_timing.md`, as Workbench renders of the actual models and keyframes: shot bodies at 12 fps, and **every transition window at full 24 fps for 12 frames each side of the cut**. Joined with `animatic.py` | `p5/shots/shot_NNN.mp4`, `p5/blockout.mp4`, `p5/analysis/` |

## For every pass

- **`notes.md`.** List each image or shot, what it shows, and where it departs from its stage document and why (an impossible framing, a scale problem). Never quietly "fix" the design. Report the problem, so the fixer changes the document.
- **Transitions (P3–P5).** For each cut, compare against the storyboard's transition fields:
  - the outgoing and incoming screen positions of the subject;
  - the motion direction and speed across the cut (`analysis/transitions.csv` gives the measured motion);
  - the brightness and colour jump;
  - the sound bridge.

  List every cut that doesn't do what the storyboard says.
- **Render log.** Report the hours spent per pass. Keep P1–P3 under about 1 h each and P5 under about 3 h, unless the user allows more.

**Reply** (after `CAPABLE`) in at most 6 lines: the pass, the files made, the render time, and the count of departures and failed transitions.
