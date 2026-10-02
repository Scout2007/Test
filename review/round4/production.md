# Round 4 review: production feasibility

## Verdict
No major issues. Revision 4 closes all four of my round 3 issues:
- the gate now works on the total;
- class B is benchmarked;
- ~5 h is banked;
- the handoff carries the budget, the gate and the plan.

My risk case lands 15 h over the gate before the levers, and at about the gate after them. A single full pass fits the week in every case I modelled. Two minor issues remain. The gate can't tell which benchmark feeds which cost, and the levers have no measured size and no last step. Nothing is unbuildable.

## Round 3 issues: status

| Round 3 issue | Status | Note |
|---|---|---|
| 1. [MAJOR] The gate can't protect the week | resolved | The gate is total-based at 160 h, fed from MEASURED. The builder prints each class's break-even. There is a class B benchmark, and ~5 h is banked (S: *Holed*, *Normandy*; P: *The wait*). The budget, render note, gate and plan are now in `ASSET_REQUESTS.md`. Two refinements follow (#1, #2). |
| 2. The hero missile | resolved | There is one hero missile: the ≤20 m capital-ship killer (MSL-V), with LOD0 for *Seeker*'s ECU, also flown in *Birds away*. `seeker_shutter` and `cap_glow` are requested, spin is a swarm attribute, and MSL is the stand-in. The builder checks controls marked "(new)". |
| 3. Step 1's benchmarks need step 3's effects | resolved | PROXY carries first versions of FX-PD, FX-SMOKE, FX-DUMP and one rock tile. |
| 4. Site 1's cluster | resolved | It is a comp element over a plate. *Site One goes dark* is 3 s of class D. |

## Issues, ranked

### 1. [MINOR] MEASURED can't hold the benchmarks that feed it, and the modelling session can't run the gate as written (all shots)
- **Problem:** MEASURED has one slot per class, but eight benchmarks feed it:
  - **A:** three benchmarks. *Rings cool* is sunlit; *Too hot* and *Broadside* are in the dark lee.
  - **C:** two benchmarks, the swarm stand-in and *Site One*'s smoke.
  - **A2:** one benchmark, *Fire*, which is in the dark lee.
  - **B and V:** one each.

  The note doesn't say which number fills which slot, and both obvious choices mislead:
  - A sunlit A number hides the lee's 16 s of class A. Under my risk case that is ~3.5 h with the allowance, against 4.9 h of slack under the gate.
  - A dark-lee number applied to all of A or A2 adds ~8–9 h and fires the levers for nothing.

  Separately, the note tells whoever measures to "enter each measured s/frame in MEASURED (storyboard/tidebreak_data.py) and rebuild". The benchmarks run in the modelling session, which works from `ASSET_REQUESTS.md`, the file the user carries across, not from the storyboard repo.
- **Evidence:** RENDER_NOTE; `build_storyboard.py` builds `SEC_PER_FRAME` from class keys only; 01_PROJECT_CONTEXT.
- **Fix:**
  - Let MEASURED take a shot title, a class within one World preset (the dark lee is preset C), or a class, with the most specific entry winning.
  - Have the note name the entry each benchmark fills: *Rings cool* goes to A; *Too hot* and *Broadside* to A in the lee; *Fire* to A2 in the lee; *Site One* to itself; the stand-ins to C and B; *Heat* to V.
  - In the handoff, give the gate as arithmetic the modelling session can do itself: the frames column × measured s/frame ÷ 3,600 × 1.3, against 160 h.
  - Say that the numbers then go back to the storyboard session for the rebuild.

### 2. [MINOR] The levers have no measured size and no last step (9, 45, 52 and the swarm shots)
- **Problem:** Only lever 3 has a known size: a second off *Wave one*, *The pack fires* and *Wall of fire* saves ~4 h raw (~5 h with the allowance) at the estimates. Levers 1 and 2 are unmeasured, and lever 1 partly repeats the plan's own methods, since the smoke and the water dump already render at half resolution. If all three aren't enough, the note has no next step.
- **Evidence:**
  - My risk case is unchanged from round 3: the heavy class C swarm shots at 260–300 s/frame, and the dark lee at +50 %. It comes to 134.4 h raw and 174.7 h with the allowance: 14.7 h over the gate and 6.7 h over the week.
  - Levers 2 and 3 bring it to ~158–161 h, if 16 spp swarm layers save 10–15 % on the swarm shots, which is my guess.
  - A single pass still has 34 h to spare.
- **Fix:**
  - Measure the levers in step 1 as well: render the C stand-in again with half-resolution FX layers, and again with 16 spp swarm layers, and record each saving next to MEASURED.
  - Add a fourth step: if the total is still over, the storyboard session and the user choose between a smaller re-render allowance (one pass still fits) and shorter holds.

### 3. [NIT] A stale hero rock tile for *The pack fires* (45)
- **Problem:** Shot 45 now sits 150 km down Anchor's shadow, where the rock is "a black disc ahead", about 180 px at 24 mm. ANCHOR still asks for a hero surface tile there, and the Methods row lists 45 with the C benchmark's rock tile.
- **Evidence:** the ANCHOR note; PRODUCTION_PLAN, Methods; 45's action line.
- **Fix:** Keep the hero tile for *The sweep* (30) only.

### 4. [NIT] Two method details for the new classes (51, 56)
- **Problem:**
  - In *The wait* (56), the turrets swing over a hull plate rendered once, so their shadows stay where the plate froze them.
  - In *Seeker* (51), focus racks from a glowing cap at ECU to Breakwater. A bright, defocused emitter is slow to converge in Cycles.
- **Evidence:** class P ("a plate rendered once, plus one moving layer"); 51's action line. The Methods row already handles 46's defocused foreground in comp.
- **Fix:**
  - For 56, render the moving layer with the hull as holdout and shadow catcher.
  - For 51, render the nose and the far field as separate layers and rack the focus in comp, as for 46.

## Asset list corrections
- **ANCHOR:** hero surface tiles for *The sweep* (30) only; drop 45 there and in the Methods row.
- **The pack fires (45):** add GI-GUN if the Donnager is in frame (a silhouette under Q13), since the Donnager's CIWS fire is shown there.
- **Render note:** say which MEASURED entry each benchmark fills (#1), and add the lever measurements and a fourth step (#2).

## What works
- The gate is a real control now. It runs on the total, prints every class's break-even (C 213, B 88, A 58, A2 118, V 391 s/frame against the 160 h gate), and reaches the modelling session together with the sets, batches, order, methods and render pipeline.
- The new classes are honest:
  - S puts the Canterbury (~320 px) and the Normandy (~200 px) at 30 s/frame.
  - P renders the locked hull and planet once.
  - The budget is 119.3 h, 155.1 h with the allowance: 4.9 h under the gate, 12.9 h under the week.
- The changed shots are costed right. *The pack fires* folds the ring salvo, the guard's CIWS and the launch into one 5 s class C shot (+1.3 h) and drops an insert. *Fire*, *The net*, *Terms* and *Site One goes dark* sit in sensible classes.
- The new rig check works. My own scan of every rig item in the board against the README and the requested controls finds nothing missing; the swarm's `spin` is described in MSL-V.
- Nothing is unbuildable, and the hero missile is now one asset for both close-ups.
