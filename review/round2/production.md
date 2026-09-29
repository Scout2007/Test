# Round 2 review: production feasibility

## Verdict
On paper, revision 2 answers every production issue from round 1. The methods, closest views, rig lists, crash-safe EXR pipeline and build order are all in the data, and every shot can be built. What remains is a question of numbers. The 119 h estimate leaves only 13 h of slack after the 30 % re-render allowance. The benchmarks measure none of the classes that carry 77 % of the hours. Several shots are also in the wrong class: the new volume shots are too cheap, and the small-subject tracker shots too dear. Both are fixable before modelling starts.

## Round 1 issues: status

| Round 1 issue | Status | Note |
|---|---|---|
| 1. Budget unmeasured, rests on class C | partly | The classes are re-costed per shot, with a named benchmark gate. But the benchmarks test only A, A2 and D, and the slack is 13 h (#1, #2). |
| 2. Detail not tied to what the camera sees | resolved | There is now a CLOSEST table and Q13. It has small gaps: the Astrid's densest view, GI-GUN, GI-MAV and MSL-V (#5). |
| 3. Endeavor and M-1C not "built" | resolved | Both are now "extend: rebuild after the Q15 picks", first in the order. |
| 4. Rig gaps | partly | Every Endeavor item and shot 25's per-gun keys are fixed. The Astrid, Breakwater and destroyer controls are still short (#5). |
| 5. Break-ups and volumes | partly | The methods are adopted, but the new plume and smoke shots outgrow "one small cached VDB" (#2). |
| 6. Swarms | resolved | FX-SWARM spec written. It is still unbenchmarked, and its missile meshes come late (#1, #3). |
| 7. World presets | resolved | Handled by WORLD. Its Shots column should read "every 3D shot". |
| 8. Crash-safe renders | resolved | Now in PRODUCTION_PLAN. |
| 9. Build order and shared set-ups | partly | Both now exist. The order has three dependency inversions, and the sets are asset groups rather than scenes (#3, #4). |

## Issues, ranked

### 1. [MAJOR] The week rests on unmeasured B and C costs, and the benchmarks don't measure them (all 13 C and 15 B shots)
- **Problem:** The raw estimate is 119.2 h, or 155 h with the 30 % allowance, which leaves 13 h of slack. The break-even raw total is 129 h. Class C alone (64 h) has to come in within +16 %, at 231 s/frame or less.
  - The four benchmark shots are A (2), D (10), A2 (17) and A2 (35). Together they cover 23 % of the hours. B and C, 92 h and 77 % of the total, stay unmeasured until their assets exist, which is at the end.
  - The class-B benchmark was lost by accident. In revision 1, "Turn and burn" was a B-class Endeavor orbit (I named it in round 1). In revision 2 it is a D-class 400 mm group shot that needs five unbuilt ships (AST, GI, DD, CV plus FX-FAR). It cannot run in step 1, and it measures only 0.6 h of the budget.
- **Evidence:**
  - Builder output: 119 h / 155 h; C 64 h, B 28 h.
  - My own risk case, also unmeasured: move the classes as in #2, then allow a plausible overrun on the heavy C and dark-lee shots (9, 28 at 260 s; 41, 43, 46 at 300 s; 29–31, 33, 35 at +50 %). That gives ~131 h raw and ~171 h with the allowance, over the week.
- **Fix:**
  1. **Step 1 method benchmarks, using stand-ins so nothing waits on new assets:**
     - **C:** two or three linked Endeavors, plus 600 instances of the built MSL through the swarm system, plus an FX-PD layer at 16–32 spp. Record s/frame and VRAM.
     - **Volume:** the smoke VDB at fleet scale (39), and a water-dump plume in an MS frame (52).
     - **Dark lee:** the Endeavor lit only by its fins, plus one M-1C shot in the dark (29, 35).
     - **Keep:** shots 2 and 35.
  2. Put the measured numbers into `SEC_PER_FRAME`.
  3. **Gate:** if C comes in above ~230 s or B above ~100 s, apply levers agreed in advance before the full pass:
     - half-resolution volume and FX layers;
     - swarm layers at 16 spp, with earlier LOD switches;
     - 1 s trimmed from 9, 41 and 46 (each second of C costs 1.3 h).

### 2. [MAJOR] Classes don't follow the pixels: volume shots under-costed, small-subject tracker shots over-costed (19, 20, 25, 26, 34, 36, 39, 52, 54)
- **Problem:**
  - **Under-costed volumes:**
    - **52 (Heat):** puts a 1,000 t water plume across an MS close-up at A2 (90 s). FX-VENT's method for it is "one small cached VDB reused", which won't read as that plume. A dense, sunlit scattering volume at close range is the costliest element Cycles renders, and at ~8 min/frame this one shot would eat the whole 13 h slack.
    - **39 (Site One):** blooms a smoke screen across a WS at class B.
    - **26 (Turnover):** has smoke plus the main plume behind a hull camera at class A.
  - **Over-costed small subjects:**
    - **20 (Holed):** the Canterbury at 40 km through 600 mm is ~160 px on black, yet class C (6.7 h).
    - **25 (Normandy):** the corvette is ~150 px, class C.
    - **34 (Lance):** the frigate is ~470 px on black, class C.
    - **19 and 36:** subjects of a few hundred px, class B.
    - **54 (Hold):** 9 s of class B (4.5 h) for a locked-off EWS that is mostly night side.
- **Evidence:** The pixel sizes come from the lens and distance in each shot, the same method as the CLOSEST table. The FX-VENT note in `ASSET_REQUESTS.md` gives the plume method quoted above.
- **Fix:**
  - **Move down:** 20, 25 and 34 to B; 19 and 36 to D; 54 to a planet plate rendered once plus a ship layer (~30 s). This saves 12.6 h.
  - **Move up:** 39 to C and 26 to A2. Give the water dump its own asset, FX-DUMP: a Geometry Nodes ice point cloud with a thin low-res VDB core, in its own layer at half resolution with one volume bounce, costed at ~250 s. Put it in the volume benchmark.
  - **Result:** ~116 h raw, ~151 h with the allowance. That is about the same total, but the hours now sit where the risk is, and #1's gate protects the rest.

### 3. [MINOR] Build order: three dependency inversions (5, 9, 20, 25, 34, 38, 40–43, 46, 51)
- **Problem:**
  - The swarm system is in step 3 and carries 42.5 h across nine shots (36 %). The meshes it needs, the MSL-V variants, are concept-gated in step 4, and they gate 32 h on their own.
  - The section-break rig (17.3 h) needs each breakable hull (DD, CV, CF, BW) to be modelled in sections at bulkhead frames. Nothing in the hull briefs says so, which invites a re-cut later.
  - The step 1 timing animatic needs true-scale blocking proxies for every ship, but the plan only makes proxies in step 5.
- **Evidence:** PRODUCTION_PLAN. 67 % of the render hours (80 h) depend on at least one concept-gated asset. Shot 43 (Umbrella) waits on three gates: the AST build, MSL-V, and the PDC pick for the Astrid's CIWS.
- **Fix:**
  - Build the swarm system on the built MSL as a stand-in, with LOD slots that the MSL-V meshes drop into later. Put MSL-V first in the concept batch.
  - Add the section spec to the DD, CV, CF and BW briefs.
  - Make crude true-scale proxies in step 1.
  - Schedule 43 last.

### 4. [MINOR] The eight sets are asset groups, not scene set-ups
- **Problem:**
  - "The pack and Anchor" includes 9, which happens in sunlight at the arrival point, not at Anchor.
  - "The Endeavor" set spans five lighting environments (arrival, coast, Breakers haze, Anchor's dark lee, the night side) and several state presets (shield on or off, the fin states, the belt damage).
  - "The destroyers" mixes two ships in two places, and the Extenuating's boom damage from 39 onward has no state.
- **Evidence:** The builder checks that every shot is in exactly one set, but not that the set is one scene. Shots 35 and 52 omit the port-fin stump (EN-FIN), and 52 omits `dmg_belt` (EN-DMG) even though its note says the damage "must read" there.
- **Fix:** Give each shot an `env` field (a World preset) and a `state` field (Endeavor: shield, fins, belt; DD: boom; BW: intact, breached, broken). Have the builder check state continuity, and batch renders by `env`. A continuity miss on a hero shot is a re-render, which comes straight out of the 30 %.

### 5. [MINOR] Rig and closest-view gaps (10, 19, 21, 28, 39, 43, 45, 46, 49)
- **Problem:**
  - **AST:** no `engine_throttle` (43's braking plume, 10), no RCS (21, 49) and no `laser_power` (43's violet lenses).
  - **BW:** its 40 CIWS and 24 PD lasers have no `ciws_fire` muzzle empties or lens glow, which 45 and 46 need. It was in my round 1 corrections but isn't in its controls.
  - **DD:** needs `rcs` (19) and a `dmg_boom` state (39 onward).
  - **CLOSEST:**
    - The Astrid's densest view is 6 (MS 50 mm along the dorsal hull), not 49.
    - GI-MAV and MSL-V are missing; both are hero-close in 9.
    - GI-GUN appears only in 28, "far off", so it belongs in Q13 beside GI-PD.
    - The CV's closest view depends on 23's unstated distance (the sketch draws ~230 px, larger than 25's ~150 px).
- **Evidence:** ASSETS controls lists; shots.md rig and action lines.
- **Fix:** See the asset list corrections below.

### 6. [MINOR] Hidden costs in the new shots (9, 28, 29–36, 41, 42)
- **Problem:**
  - **42:** a 300 mm tracker mounted on the Pillar puts its pods in a heavily defocused foreground, which is slow to converge in Cycles.
  - **41 and 28:** each puts a hero rock tile (displacement plus boulder scatter) at 24 mm beside hundreds of plumes or many craft, which is a VRAM risk.
  - **Swarm lights:** the "nearest ~5 lights" rule can pop as the set of nearest missiles changes, flickering the hull lighting in 9, 41 and 42.
  - **Dark lee:** 29–36 are lit only by emissive fins, flashes and the lance, which is noisy.
- **Evidence:** Cycles converges slowly on strong defocus and on scenes lit only by small emitters. The M-1C already needed point lights for its fins to read.
- **Fix:**
  - **42:** render the foreground as its own layer and defocus it in comp.
  - **41 and 28:** instance everything, and include a rock tile in the C benchmark.
  - **Swarm lights:** fade them in and out over ~6 frames.
  - **Timing:** drive `pod_ripple` and `cells_open` from the same per-pod launch-time attribute as the swarm, so doors and launches can't drift apart.
  - **Dark lee:** light the hull from explicit area lights on each fin, with strength driven by `heat`, and turn emission sampling off on the fin meshes.

### 7. [NIT] Haze glow and disk space
- **Problem:** The Mist pass gives depth haze, but not the forward-scatter glow toward the sun that the lighting rule asks for. The ~100 GB disk estimate was set for the shorter film.
- **Evidence:** LIGHTING ("lit from behind"). The film is now 5,136 frames, plus the FX layers.
- **Fix:** Add a sun-direction gradient to the haze in comp, and plan for ~150 GB.

## Asset list corrections
- **EN-FIN:** add shots 35 and 52 (the port stump is in view).
- **EN-DMG:** add shot 52.
- **AST:** add `engine_throttle`, `rcs_bow/stern` and `laser_power/traverse`. Set the closest view to shot 6 for the hull and shot 49 for the muzzle.
- **BW:** add `ciws_phase`/`ciws_fire` with muzzle empties, and PD `laser_power`.
- **DD:** add `rcs` and `dmg_boom`.
- **New FX-DUMP:** the water-dump plume, split out of FX-VENT (#2).
- **FX-SMOKE:** make two cache resolutions (MS in 17, fleet scale in 39), or add procedural detail in the volume shader. Render it in a half-resolution layer.
- **GI-GUN:** closest view shot 28, far off. Add it to Q13 as a silhouette.
- **GI-MAV, MSL-V:** closest view shot 9. Add MSL-V to shot 47 (the Casaba carriers at 2 km, ~26 px).
- **CF:** add simple instanced escape pods for shot 34.
- **CV:** state shot 23's distance and recompute its closest view.
- **WORLD:** set its Shots column to "every 3D shot".
- **New PROXY:** true-scale blocking proxies of every ship, built in step 1 for the animatic.

## What works
- Every round 1 production issue has a concrete answer. The builder now enforces the bookkeeping: sets, closest views, clock continuity and subtitle rates.
- The class costs are more conservative (A 45, C 200). Costing is per shot, the budget is regenerated from the data, and measured numbers drop straight in.
- The adopted methods are sound: the section-break rig, ice-glint venting, the Mist pass, one swarm system, EXR sequences with placeholders, and text added in the edit.
- The tracker framings put small subjects on black, so many of the new cuts (19, 20, 25, 34, 36, 45, 53) are cheap once they are classed honestly.
- The 16 Endeavor-set shots (26.7 h, 22 %) need only the rebuilt ship plus FX, so production can start as soon as the Q15 picks are made.
