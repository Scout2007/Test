# Agent 16 · Blender preflight (run once, before Phase 2)

**Goal.** Prove the preview pipeline works on this machine with this project, so the preview passes P1–P5 don't fail on setup. This agent removes the riskiest part of the run.

**Inputs from the orchestrator:**
- the Blender path and the `.blend` locations, from the user's answer to Q24;
- `pack/project_docs/README_blender_project.md`.

## Steps

Log each step's command and its result.

1. **Version.** Run `blender --version`. If it fails, escalate to the user (00_common) and stop.
2. **Inventory each project file.** For each `.blend` the trailer needs (at least `LREF_Endeavor.blend`; others the user names), run:
   `blender -b <file> --python trailer/tools/blender_preview.py -- inventory --out trailer/work/previz/preflight/<file>_inventory.json`
3. **Check linking.** Every library in the inventory resolves. Note missing linked assets; don't fix them.
4. **Test a still.** Write a still spec (`preflight/test_still.json`): a new camera 3 km off the hero ship's side, `look_at` the ship, 50 mm, Workbench, 960×402. Render it, look at the image, and confirm the ship is in frame and readable.
5. **Test a move.** Write a 48-frame spec with three keys: a push from 3 km to 1.5 km, `look_at` the ship, with the lens going 35 → 50 mm. Render it at 50 %, then join it with `trailer/tools/animatic.py`, using a timing CSV that points at the frames folder through ffmpeg, or make the mp4 from the frames with ffmpeg directly. Run `prep_reference.py` on the result with `--out trailer/work/previz/preflight --no-beats`, and check that `transitions.csv` and the frames show a push-in (zoom above 1).
6. **Test the engines.** Render one EEVEE still of the same framing and time it. If the style bible will need Cycles, render one Cycles still at low samples and time that too.
7. **Fix the tool if needed.** If `blender_preview.py` fails on this Blender version (an API change, an engine name), fix the tool minimally, and record the diff in the report.

## Write `trailer/work/previz/preflight/REPORT.md`

- the Blender version and GPU;
- per file: the collections and cameras that matter, the hero objects' names and sizes, the rig controls found (custom properties), the world and lighting setup, and any missing links;
- seconds per frame at 960 px for Workbench, EEVEE and Cycles, with the extrapolated hours for P1–P5 at the planned sizes;
- **a cookbook:** the exact JSON specs that worked, with the object names to use for each ship. Every later previz brief includes this file;
- what failed, and how it was fixed or what's needed from the user.

**Reply** (after `CAPABLE`) in at most 6 lines: pass or fail per step, the seconds per frame per engine, and any blocker.
