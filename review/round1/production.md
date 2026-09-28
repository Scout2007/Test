# Round 1 review: production feasibility

## Verdict
Every shot can be built from the existing kit plus the requested assets, and 14 Endeavor shots (66 s, 40 % of the film) could start as soon as the ship is rebuilt. But the ~100 h budget is unmeasured and 75 % of it sits in class C: made as written (volumetric haze and smoke, fracture sims, hundreds of lit plumes), a full pass could reach ~185 h, past the week. Asset scope is the real critical path: 43 new or extended items and 11 concept rounds, some for things never seen larger than 15 px.

## Issues, ranked

### 1. [MAJOR] The render budget is unmeasured, mislabelled and rests on class C (all shots)
- **Problem:** Class A is labelled "measured hero cost", but the project context calls the 30–40 s figure "the draft's estimate"; only the one-turret M-1C patch has been measured. Class C (17 shots, 1,800 frames) accounts for 75 of the 100 h, at a guessed 150 s/frame that has to cover volumes, sims and swarms. The total is one clean pass: no re-renders, bakes or animatic. Shots 6, 12, 17 and 35 each hide two set-ups.
- **Evidence:**
  - Scaled up from the measured patch (3–3.5 s at 60 % and 64 spp), full size at 128 spp is ~18 s, so ~35 s for a plain close-up is plausible.
  - The FX close-ups will not hold 35 s: 14 (smoke, tracers, chaff, flashes), 24 (shatter, vapour) and 25 (the whole ship, several guns whose plasma needs 64 transparent bounces, plus a moving 3 MW light per shot).
  - Shots classed too high: 15 (the destroyer is 600 km off, ~1 px), 31 (the ring stations show only as lights, see #2), 36 (hull plus instanced debris), 1 and 37 (mostly-dark EWS), 9 (a still moon plus flashes).
  - With class C at 300 s/frame and 14/24/25 at 120 s, a pass is ~184 h.
- **Fix:**
  1. Benchmark before building new assets. Render one frame each of 2, 8, 14 and 25 on the rebuilt ship, plus one volume test, then put the measured numbers into `SEC_PER_FRAME` and relabel.
  2. Reclassify: 14, 24 and 25 at ~90 s/frame; 15, 31 and 36 as B; 9 as E. Cost 6, 17 and 35 per set-up (the Astrid EWS halves are cheap).
  3. Change methods:
     - Put emissive FX in their own view layers at 16–32 spp, keeping 1–3 proxy lights in the beauty layer for the light the FX throw on hulls.
     - Turn on Persistent Data, adaptive sampling, and denoising with albedo/normal passes (the grade's grain and black crush hide what's left).
     - Render static plates once for the locked-off shots 1, 3 and 37.
     - Blur rocks and slugs with vector blur in comp.

  My per-shot re-estimate with these changes is ~90 h. Adding 30 % for fix re-renders gives ~117 h, which is inside the week with ~50 h of margin.

### 2. [MAJOR] Asset scope is the critical path, and detail isn't tied to what the camera sees (3, 4, 11, 18, 20, 26, 27, 30, 31)
- **Problem:** 43 of 46 items are new or extended and 11 need concept rounds (the M-1C alone took five). Everything is marked hero-detailed, yet:
  - **RING:** 12 stations sit 30° apart on Breakwater's orbit, ~21,800 km apart, so in 31 any station is under 0.1 px. Only its lights read.
  - **CF:** ~13 px at 60 km on 40 mm (26) and ~15 px at 40 km on 28 mm (27). Its escape pods are invisible.
  - **TND and GI-PD:** seen only in the background of 4.
  - **Drones:** under ~30 px in 11, 18, 20 and 30, so four LREF drone types can't be told apart.
  - **Shot 3:** needs every ship class at 5–150 px, for a 5 s class-D shot.
- **Evidence:** The user said "some of the final details for the final animation can be locked to the bits shown in the final animation" (user_messages, 2026-09-27; project_notes v4). Taken together with "everything hero-detailed", that means hero detail where the camera goes.
- **Fix:**
  - Add a "closest view (shot, distance, px)" column to `ASSET_REQUESTS.md`.
  - Ask the user to confirm the cuts: RING as lights only; CF as a silhouette proxy with a comp break-up, or a closer shot if cinematography wants one; TND and GI-PD as silhouettes; one drone design per side.
  - Send the remaining concept sheets as one batched round.
  - Build AST, GI, DD and CV from `lref_kit` (per the notes: "reuse the kit for new classes"). The M-1Cs, arrays, CIWS, fins, rings and shields are instances, so the Astrid's new hero work is its hull, the AVPSA dish and the spinal. Link and instance so 26 and 29 fit in GPU memory.
  - Give shot 3 LODs and render it last.

### 3. [MAJOR] The Endeavor and M-1C are not "built" for this board (14, 25, 36, and every reuse)
- **Problem:** `rail_wake` and `charge_a/b` exist in code only. The M-1C wake style and the PDC design (PD-1/2/3) are both still waiting on the user's pick. Shot 25 needs `rail_wake`, 14 and 36 show the CIWS, and AST (≥19 M-1C), GI-GUN and GI-PD inherit both picks.
- **Evidence:** project_notes v9–v11: "ship NOT rebuilt"; "AWAITING USER'S PICK"; "PDC concept pick still pending".
- **Fix:**
  - Mark EN and M1C as "extend: rebuild after the picks", and schedule the two picks and the rebuild first.
  - Shot files link `LREF_Endeavor` with a library override on the rig empty only, and keep their keys in headless per-shot scripts (the project's workflow). Rebuilds then propagate without redoing shots, as long as object names stay stable.

### 4. [MAJOR] Rig: shot 25 breaks a user decision, and controls are missing (14, 21, 25, 33, 36, 37, all new assets)
- **Problem:**
  - Shot 25 keys the ship-wide `rail_scales`/`rail_heat` and omits `charge_a/b` and `battery_traverse/elevation`.
  - Shots 14 and 36 ramp `ciws_rpm`.
  - No property fires the CIWS, the chaff, flare and smoke launchers, or the jammers, which 14, 21 and 33 need.
  - Shot 37 drives three fins with the single `radiator_deploy`.
  - Fifteen shots with new assets say "Rig: none" but animate dishes, pod doors, turrets, cells and break-ups (6, 7, 13, 15–18, 20, 26, 29–31, 33–35).
- **Evidence:**
  - The user's decision is that only the gun that fired vents: per-gun `fins_a/b` and `heat_a/b` (project_notes, stage 2; README).
  - README: CIWS rpm changes mid-shot "jump rather than easing". At 2,400 rpm the barrels turn 1.7 times a frame, so they strobe.
  - The README has no fire or countermeasure properties.
  - The sun is `TO_SUN` ("rebuild after changing it").
- **Fix:**
  - **Endeavor (EN-PD):** `ciws_phase` (a keyed angle) plus a spin-blur swap; `ciws_fire` with muzzle empties; `cm_chaff`, `cm_flare` and `cm_smoke` with emitter locators; `ew_active`.
  - **Endeavor (EN-FIN):** per-fin `fin_*`, a `fin_port_state` (intact/shattered/stump) and a `dmg_belt` toggle.
  - **Sun:** a sun rig, a Sun object that drives the World.
  - **New assets:** a controls table for each, like the README's, with simple-expression drivers that can be library-overridden. Examples: AST `avpsa_az/el` and `spinal_charge/shot`; GI-MAV a single `pod_ripple`; BW turret traverse/elevation, `cells_open` and `drive_glow`; EMP-POD `heave` and `petals`; EMP-RG `unmask` and `shot`; and `break` on every break-up.

### 5. [MAJOR] Break-ups and volumes, as written, will eat the schedule (11, 13, 14, 16, 20–22, 24, 34–36)
- **Problem:** FX-BREAK specifies cell fracture, which needs simple, closed meshes. The kit hulls are assemblies of separate plates, quilts and frames, so at hero detail it will fail or produce unmanageable piece counts. The volumetric haze (11), smoke screens (14, 21), venting (16, 34), coolant vapour (24) and dust (13, 22) would need kilometre-scale Mantaflow domains, long bakes and slow, noisy volume renders.
- **Evidence:** The README describes real-geometry plating and quilting. The board has six break-up events and about eight volume uses, most of them in class C.
- **Fix:**
  - **Break-ups:** one section-break rig for DD, CV, CF and BW:
    - split each hull along its bulkhead frames into 3–8 sections;
    - cap the torn edges with kit parts (exposed decks, frames and pipes, which are neither interiors nor greebles);
    - drive separation and tumble from the hit point with a procedural `break` 0→1;
    - add an instanced debris kit, reused in 36.

    No rigid-body sims.
  - **Venting and vapour:** short-lived sprays of glinting ice particles, which is also what gas does in vacuum, plus one small cached VDB reused in 16, 20 and 34.
  - **Smoke screen:** one low-res VDB cached once, rendered in its own layer and reused in 14 and 21.
  - **Breakers haze:** the Mist pass, done in comp.

### 6. [MAJOR] Swarms with hundreds of plumes (7, 18, 29, 30, 33)
- **Problem:** Shot 7 has 150 missiles, and 29 and 33 carry ~400–600 plus decoys each. Shot 18 has dozens of drones and 30 a pellet cloud. If the plumes are layered transparent shells like the M-1C gas, or each carries a light, frames will take many minutes. Specular pellets under drone lamps make fireflies.
- **Evidence:** LREF doctrine, "Pack arithmetic" [A-26]: "two waves of about 400–600 missiles plus decoys each". README: the M-1C plasma needs 64 transparent bounces.
- **Fix:** One Geometry Nodes swarm system serves FX-SWARM, FX-DRN and FX-CAN:
  - points with a per-instance launch time and three LODs; the hero missile only for the nearest ~10;
  - each plume a single emissive mesh with emission sampling off (as the burst materials already are), and low transparent bounces;
  - real lights only on the ~5 nearest plumes or flashes;
  - the pellets as emissive points whose brightness follows the angle to the lamp;
  - the swarm rendered as its own layer.

### 7. [MINOR] The World is in every shot but is set for low orbit (all shots)
- **Problem:** MAREN is listed for 3, 31 and 37 only. The World-shader planet is in every frame, set up for low orbit and lighting the ship's underside, while the board runs from 450,000 km out (Maren 1.6° across) to Breakwater's orbit (17.5°). Far bodies at real scale also break float precision.
- **Evidence:** README, Environment: the planet "lights the ship's underside".
- **Fix:**
  - Build World presets for arrival/coast, the Breakers, the Lee and Breakwater, with the planet-shine scaled to each.
  - Make Skerry a second World body, or a proxy at the right angular size.
  - Keep each set-up's camera near the origin.
  - The Site 1 plateau is never resolvable; a light that goes out is enough.

### 8. [MINOR] Final renders must survive a week on one machine (all shots)
- **Problem:** `render_anim.py` writes H.264 MP4 with the grade baked in. A crash loses the whole clip, and any grade tweak means a re-render.
- **Evidence:** README (render_anim.py); project_notes ("writes MP4 via Blender's built-in FFmpeg"). The user has already had to restart the machine mid-task (user_messages, 2026-09-28).
- **Fix:**
  - Render one job per shot to multilayer EXR sequences (DWAA): beauty, mist, vector, cryptomatte and the FX layers.
  - Turn Placeholders on and Overwrite off, so a crashed render resumes where it stopped.
  - Grade with `LREF_Compositor` in a separate pass, then encode.
  - Plan for ~100 GB of disk.

### 9. [MINOR] No build order or shared set-ups (all shots)
- **Problem:** The list is grouped by faction rather than by dependency, and the 37 shots are treated as 37 scenes.
- **Evidence:** They reduce to about eight sets, and most Endeavor shots match existing cameras.
- **Fix:**
  - **Sets:**
    - **Endeavor:** 1, 2, 4, 8, 10, 12, 14, 21, 23–25, 27, 32, 36, 37. Start from the existing cameras: `CAM_Nose` (2, 27), `CAM_LookDev_Pair` (14), `CAM_Radiator_Slot` (24), `CAM_Railgun_House`/`CAM_Battery` (25), `CAM_LookDev_Yoke` (32), `CAM_Engines_Burn` (8, 21), `CAM_Hero` (37). 8 and 21 share the orbit move and the flip action; 10, 23 and 37 share the fins-out action.
    - **Astrid:** 6, 17a, 35a, with one spinal-fire action.
    - **Hedgehog:** 7, 29.
    - **Breakers:** 11, 13, 15, 16, 18, 20, 17b.
    - **Lee:** 22, 26, 29, plus background plates for 23–27.
    - **Breakwater:** 31, 33, 34, 35b, plus the debris for 36.
    - **Plates:** 3, 5, 9, 37.
    - **2D:** 5, 6b, the POV insert in 12, 19, 28.
  - **Order:**
    1. The two picks, the EN rebuild and its rig items, the World presets, the benchmarks, and an EEVEE timing animatic (preview only; the finals stay in Cycles).
    2. Send the batched concept round now, because it waits on the user.
    3. Meanwhile, build what already has art: the FX library, the BRK kit then the Lee, GI with GI-MAV, DD, and AST.
    4. Then the concept-gated items: MSL-V, CV and drones, EMP-POD and EMP-RG, BW with BW-BRK, GI-GUN.
    5. Proxies, and shot 3, last.

### 10. [NIT] Keep text out of the renders (all shots)
- **Problem:** SUB and the clock are listed as comp.
- **Evidence:** Voice acting "may replace them later" (OPEN_QUESTIONS).
- **Fix:** Add the subtitles and clock in the edit, after the grade. Generate the HUD plots from the geometry `build_storyboard.py` already draws as SVG maps, rendered to PNG sequences.

## Asset list corrections
- **EN, M1C:** change "built" to "extend (rebuild after the wake-style and PDC picks)".
- **EN-FIN:** three states: intact, a pre-fractured port fin (24), and a stump (28–37), plus per-fin properties (24, 36, 37). Drop "cut-loose fin drifting away": no shot shows it.
- **EN-DMG:** a `dmg_belt` toggle from shot 26 on. It only reads on screen in 36.
- **New, EN-PD (extend):** `ciws_phase`, `ciws_fire`, and the countermeasure and EW triggers (14, 21, 36). Put the same hooks on BW's CIWS (33).
- **New, WORLD (extend):** the location presets and the sun rig; all shots.
- **MSL-V:** set concept first to yes (five new weapon designs). Name the Casaba killer explicitly, add shots 33 and 34, and ask for LODs.
- **AST:** concept first for the spinal muzzle and its FX look; build the rest from the kit.
- **GI-GUN:** four scaled RC_M1C twins on a module frame, so the concept sheet only has to settle the layout.
- **GI-PD:** wait for the PDC pick; a silhouette is enough in shot 4.
- **CF, TND, RING:** a proxy, a silhouette, and lights only, in that order (see #2); the user decides.
- **DRN-L, DRN-C:** one design each, plus the hide. Add DRN-L to shot 16 ("its drones drift").
- **DD:** remove from shot 15 (~1 px; a glint will do).
- **SHD:** for the distant park, instance scaled copies of the gold shield rather than waiting for every ship to be built.
- **LEE:** a base mesh with a Geometry Nodes boulder scatter from the BRK kit. Hero surface tiles only for 22 and 29; background plates for 23–27.
- **BRK:** haze via the Mist pass. The rock kit also feeds the Lee, the emplacement host rocks and the drone hides.
- **SKR:** render it once as a still plate. The battery and depot are sub-pixel, so they need only flash positions.
- **FX-BREAK:** replace "cell fracture" with the section-break rig, torn-edge caps and a debris kit.
- **FX-SWARM, FX-DRN, FX-CAN:** merge into one swarm system.
- **New, FX-VENT:** vacuum venting spray (16, 20, 24, 34).
- **New, FX-FAR:** distant drive plumes and glints (3, 8, 22, 30).
- **HUD:** a style frame for the user to approve first. Add the clock to every time-jump shot.

## What works
- Fourteen shots (66 s, 40 % of the film) need only the built Endeavor plus FX and rig extensions. That work can start now.
- Most heavy shots are 3–5 s long, and 5, 19 and 28 are already 2D.
- The reuse instincts are right: one frigate hull with three modules, one shared break-up asset, and the M-1C as the fleet gun.
- Concept-first flags are set correctly for every design that has no reference art.
- The budget is generated from the data (`render_budget()`), so measured numbers drop straight in.
- Nine Endeavor shots cite current renders as reference, and most match existing cameras.
