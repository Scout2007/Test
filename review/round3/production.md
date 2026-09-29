# Round 3 review: production feasibility

## Verdict
Revision 3 closes six of my seven round 2 issues. Every shot is in an honest class, and nothing is unbuildable. The user's eight new shots are cheap: 7.2 h, about 6 % of the budget. One issue is left, and it is about the margin. The arithmetic behind 159 h is honest, but the slack after the 30 % allowance has shrunk to 8.7 h. The go/no-go gate now lets through costs that already blow the week. It also doesn't reach the modelling session, which does the rendering. My risk case clears the week only if the gate fires. The fix is small.

## Round 2 issues: status

| Round 2 issue | Status | Note |
|---|---|---|
| 1. B and C unmeasured; benchmarks test the wrong classes | partly | Step 1 now has method benchmarks with stand-ins, and a gate with agreed levers. But the gate's thresholds (mine, sized for 119 h) now sit above break-even. Class B has no benchmark, and the gate isn't in the handoff file (#1). |
| 2. Classes don't follow the pixels | resolved | Every move is applied. The water dump has FX-DUMP and class V; the last shot is class P. |
| 3. Build-order inversions | resolved | The swarm is built on the MSL with LOD slots; MSL-V goes first in the concept round; sections are in the hull briefs; PROXY is in step 1; *Umbrella* renders last. One small new inversion (#3). |
| 4. Sets are asset groups | resolved | ENVS and STATES are in, the builder checks the state assets, and batches follow the World preset. |
| 5. Rig and closest-view gaps | resolved | The Astrid, Breakwater and destroyer controls are added; CLOSEST is fixed and extended; GI-GUN is in Q13. One new gap: `seeker_shutter` (#2). |
| 6. Hidden costs | resolved | All five are in the methods row, which still has to reach the handoff (#1). |
| 7. Haze glow, disk | resolved | Sun-direction gradient added; disk plan is ~150 GB. |

## Issues, ranked

### 1. [MAJOR] The gate can't protect the week as written (all shots; most exposed: 9, 30, 46, 49, 53 and the dark lee, 31–40)
- **Problem:**
  - **Thin slack.** The estimate is 122.6 h raw, 159.3 h with the allowance, which leaves 8.7 h (13 h in revision 2). Break-even is now 224 s/frame for class C and 92 s for class B. The gate only fires above 230 s and 100 s: my round 2 numbers, sized for revision 2's 119 h. At either threshold alone the total is 170–172 h with the allowance, and 183 h at both, yet no lever fires.
  - **No B benchmark.** Class B (16 shots, 30 h) is named in the gate, but no step 1 benchmark measures it.
  - **Not in the handoff.** The gate, the levers, the build order, the methods row (fin area lights, the defocused-foreground layer, the rock tile) and the render pipeline live only in `tidebreak_data.py` and the page. `ASSET_REQUESTS.md` has none of them. That is the file the user carries to the modelling session (01_PROJECT_CONTEXT, 00_PROMPT), and the modelling session is the one that renders.
- **Evidence:**
  - Builder output: 122.6 h / 159.3 h, C 56 h, B 30 h.
  - My risk case is the same one as in round 2, and also unmeasured: the heavy C swarm shots at 260–300 s, and the dark-lee A and A2 shots at +50 %. It comes to 136.7 h raw and 178 h with the allowance, 10 h over. A single full pass still fits, with 31 h spare.
  - The agreed levers bring the risk case to ~124 h raw (~161 h with the allowance): trims worth ~5.7 h, plus 16 spp swarm layers, which I estimate at ~6–7 h. But that only happens if the gate triggers them.
- **Fix:**
  1. **Gate on the total, not per class.** Put the measured s/frame into `render_budget()`, and apply levers until the total with the allowance is ≤ 160 h. After step 3 below, that is roughly C ≤ 220 s or B ≤ 93 s on their own.
  2. **Add a B stand-in to the step 1 benchmarks:** one linked Endeavor in full view, sunlit, with its drive lit.
  3. **Bank ~5 h now.**
     - *Holed* and *Normandy* are subjects of ~320 and ~200 px on black; class them at ~30 s/frame.
     - *The wait* shares the Casaba angle; if its camera is locked, make it class P (a monitor plate plus a turrets-and-vents layer).
     - Result: 117.8 h, 153 h with the allowance, 15 h of slack. With the levers, my risk case then lands at ~155 h.
  4. **Put the plan in the handoff.** Have `write_assets()` append the render budget table, RENDER_NOTE and PRODUCTION_PLAN to `ASSET_REQUESTS.md`.

### 2. [MINOR] The hero missile is under-specified (10, 52)
- **Problem:**
  - Shot 10 lists the built MSL as its hero, at CU 85 mm, about 1.4 cm per pixel. But wave one flies killers (FLEET), and 52 shows that same design at ECU as MSL-V.
  - The MSL was built early; nothing in the pack says it had the later SAVAGES detail pass.
  - 52's `seeker_shutter` is requested nowhere, and nothing drives the ablative cap's glow.
- **Evidence:**
  - ASSETS: the MSL note says "the hero LOD flies alongside the camera in *Birds away*"; the MSL-V note describes the Casaba killer's "seeker window behind a shutter".
  - My cross-check of every rig item against ASSETS and the README finds only `seeker_shutter` unrequested. The builder doesn't check "(new)" rig items at all.
- **Fix:**
  - Make one hero missile, the MSL-V Casaba killer, with LOD0 built for 52's ECU, and use it in 10 too. Shot 10 then becomes concept-gated, unless the user confirms that the killer keeps the MSL body.
  - Request `seeker_shutter` and `cap_glow`.
  - Add a builder check that every "(new)" rig item is named in ASSETS.

### 3. [MINOR] Step 1's benchmarks need step 3's effects (all C and volume shots)
- **Problem:** The C benchmark needs an FX-PD layer and a rock tile, and the volume benchmark needs FX-SMOKE and FX-DUMP. The order builds the FX library and Anchor in step 3, so "nothing waits on new assets" isn't quite true.
- **Evidence:** PRODUCTION_PLAN, "Order", steps 1 and 3; RENDER_NOTE.
- **Fix:** Build benchmark-grade first versions in step 1: stock tracer streaks and flashes, a Quick Smoke cache at both scales, a point-cloud plume and a displaced rock tile. The finished effects still arrive in step 3.

### 4. [NIT] The dark cluster in *Site One goes dark* (61)
- **Problem:** The World-shader planet was built for low orbit. At 2,000 mm from ~36,000 km, one pixel is ~340 m.
- **Evidence:** README, Environment; MAREN note ("about 10 px at 2,000 mm").
- **Fix:** Make the ~10 px cluster a masked texture, or a comp element over a plate rendered once, rather than a controllable feature of the World shader.

## Asset list corrections
- **ASSET_REQUESTS.md:** append the render budget table, RENDER_NOTE (the benchmarks and the gate) and PRODUCTION_PLAN (order, methods, rendering), so the modelling session gets them.
- **MSL-V:** the Casaba killer is the hero missile in 10 and 52, with LOD0 at ECU detail. Add the controls `seeker_shutter` and `cap_glow`, with spin as a per-instance attribute in the swarm.
- **MSL:** mark it as the swarm's stand-in and base. If 10 keeps it as the hero, it needs a hero detail pass.
- **EN-FIN:** add the dark-lee fin area lights (strength from `heat`, emission sampling off on the fin meshes). They are in the methods row today, not in the asset.
- **PROXY / step 1:** add benchmark-grade FX-PD, FX-SMOKE and FX-DUMP, plus one rock tile.
- **MAREN:** make Site 1's cluster a mask or comp element (61).

## What works
- Every round 2 issue has an answer in the data, and the builder now checks states, closest views and sets.
- The classes follow the pixels: small subjects on black at D or B, the volumes at C and V, and a plate for the locked-off end.
- The eight new shots cost 7.2 h and are classed right or conservatively:
  - 18 is the existing yoke look-dev set-up.
  - 39 and 40 are the M-1C's own wake and firing cycle. Its measured night render scales to ~18 s/frame at full size, well inside A and A2.
  - 10 and 52 are single objects on black, at class B.
  - 32, 44 and 61 are nearly free.
- Nothing is unbuildable. The Endeavor set (19 shots, 30 h, a quarter of the budget) can start as soon as the Q15 picks are made.
- The render pipeline is complete: EXR sequences with placeholders, the grade as its own pass, ~150 GB of disk.
