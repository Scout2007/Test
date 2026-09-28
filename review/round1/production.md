# Round 1 review: production feasibility

## Verdict
Every shot can be built from the existing kit plus the requested assets, and 14 Endeavor shots (66 s, 40 % of the film) need little beyond the rebuilt ship. But the ~100 h budget is unmeasured and 75 % of it is class C. Made as written (volumes, fracture sims, hundreds of lit plumes), a pass could reach ~185 h, past the week. Asset scope is the critical path: 43 new or extended items and 11 concept rounds, some for things never larger than 15 px on screen.

## Issues, ranked

### 1. [MAJOR] The render budget is unmeasured and rests on class C (all shots)
- **Problem:** Class A is labelled "measured hero cost", but the context calls 30–40 s "the draft's estimate". Only the one-turret M-1C patch has been measured. Class C (17 shots, 1,800 frames) is 75 of the 100 h at a guessed 150 s/frame. The total covers one clean pass, and shots 6, 12, 17 and 35 each hide two set-ups.
- **Evidence:**
  - The measured patch (3–3.5 s at 60 %, 64 spp) scales to ~18 s at full size and 128 spp. So 35 s suits plain close-ups, but not 14 (smoke, tracers), 24 (shatter, vapour) or 25 (the whole ship; plasma needing 64 transparent bounces; a moving 3 MW light per shot).
  - Classed too high: 15 (the destroyer, 600 km off, is ~1 px), 31 (ring stations are only lights), 36 (hull plus instanced debris), 1 and 37 (mostly dark EWS), 9 (a still moon).
  - With class C at 300 s and 14/24/25 at 120 s, a pass takes ~184 h.
- **Fix:**
  1. Benchmark shots 2, 8, 14 and 25 on the rebuilt ship, plus one volume test, and put the results in `SEC_PER_FRAME`.
  2. Reclassify: 14, 24, 25 to ~90 s; 15, 31, 36 to B; 9 to E. Cost 6, 17 and 35 per set-up.
  3. Methods:
     - Emissive FX in their own view layers at 16–32 spp, with 1–3 proxy lights left in the beauty layer.
     - Persistent Data, and adaptive sampling with albedo/normal denoising.
     - Plates rendered once for the locked-off shots 1, 3 and 37.
     - Vector blur in comp.

  My re-estimate with these changes is ~90 h, or ~117 h with 30 % for re-renders: ~50 h inside the week.

### 2. [MAJOR] Asset scope is the critical path, and detail isn't tied to what the camera sees (3, 4, 11, 18, 20, 26, 27, 30, 31)
- **Problem:** 43 of 46 items are new or extended, and 11 need concept rounds (the M-1C took five). Everything is specified at hero detail, yet:
  - the RING stations are ~21,800 km apart (30° on Breakwater's orbit), so each is under 0.1 px in 31;
  - CF is ~13 px in 26 (60 km, 40 mm) and ~15 px in 27 (40 km, 28 mm), and its escape pods are invisible;
  - TND and GI-PD appear only behind shot 4;
  - drones stay under ~30 px;
  - shot 3 needs every ship class, at 5–150 px.
- **Evidence:** The user: "some of the final details for the final animation can be locked to the bits shown in the final animation" (user_messages 2026-09-27; project_notes v4).
- **Fix:**
  - Add a "closest view (shot, distance, px)" column to the asset list.
  - Ask the user to confirm: RING as lights only; CF as a silhouette proxy with a comp break-up (or a closer shot, if cinematography wants one); TND and GI-PD as silhouettes; one drone design per side.
  - Batch the remaining concept sheets into one round.
  - Build AST, GI, DD and CV from `lref_kit` ("reuse the kit for new classes"). The M-1Cs, arrays, CIWS, fins, rings and shields are instances, so the Astrid's new hero work is its hull, the dish and the spinal.
  - Link and instance, so shots 26 and 29 fit in GPU memory. Shot 3 uses LODs and renders last.

### 3. [MAJOR] The Endeavor and M-1C are not "built" for this board (14, 25, 36, and every reuse)
- **Problem:** `rail_wake` and `charge_a/b` exist in code only. The wake style and the PDC design (PD-1/2/3) are both still waiting on the user's picks. Shot 25 needs `rail_wake`; 14 and 36 show the CIWS; AST (≥19 M-1C), GI-GUN and GI-PD inherit both picks.
- **Evidence:** project_notes v9–v11: "ship NOT rebuilt", "AWAITING USER'S PICK", "PDC concept pick still pending".
- **Fix:**
  - Mark EN and M1C as "extend: rebuild after the picks", and do them first.
  - Shot files link `LREF_Endeavor` with a library override on the rig empty, and keep their keys in headless per-shot scripts. Rebuilds then propagate, as long as object names stay stable.

### 4. [MAJOR] Rig: shot 25 breaks a user decision, and controls are missing (14, 21, 25, 33, 36, 37, new assets)
- **Problem:**
  - Shot 25 keys the ship-wide `rail_scales`/`rail_heat` and omits `charge_a/b` and `battery_traverse/elevation`.
  - Shots 14 and 36 ramp `ciws_rpm`.
  - Nothing fires the CIWS, the countermeasure launchers or the jammers (14, 21, 33).
  - Shot 37 drives three fins with `radiator_deploy`.
  - Fifteen shots say "Rig: none" while animating new assets (6, 7, 13, 15–18, 20, 26, 29–31, 33–35).
  - The sun is fixed at build time.
- **Evidence:**
  - Only the gun that fired vents, using per-gun `fins_a/b` and `heat_a/b` (project_notes, stage 2).
  - README: CIWS rpm changes "jump rather than easing"; at 2,400 rpm the barrels turn 1.7 times per frame and strobe.
  - The README has no fire or countermeasure properties, and `TO_SUN` needs a "rebuild after changing it".
- **Fix:**
  - **Endeavor:** `ciws_phase` (a keyed angle) with a spin-blur swap, `ciws_fire` with muzzle empties, `cm_chaff/flare/smoke`, `ew_active`, per-fin `fin_*`, `fin_port_state` and `dmg_belt`.
  - **Sun:** a Sun object that drives the World.
  - **New assets:** a controls table for each, like the README's, using simple-expression drivers that can be overridden. For example:
    - AST: `avpsa_az/el`, `spinal_charge/shot`;
    - GI-MAV: `pod_ripple`;
    - BW: turret traverse/elevation, `cells_open`, `drive_glow`;
    - EMP-POD: `heave`, `petals`;
    - EMP-RG: `unmask`, `shot`;
    - every break-up: `break`.

### 5. [MAJOR] Break-ups and volumes, as written, will eat the schedule (11, 13, 14, 16, 20–22, 24, 34–36)
- **Problem:** FX-BREAK specifies cell fracture, which needs simple closed meshes. The kit hulls are assemblies of separate plates, quilts and frames, so at hero detail it will fail or the piece count explodes. Done as volumes, the haze (11), smoke screens (14, 21), venting (16, 34), coolant vapour (24) and dust (13, 22) mean kilometre-scale Mantaflow domains, long bakes and noisy renders.
- **Evidence:** README: plating and quilting are real geometry. The board has six break-ups and about eight volume uses.
- **Fix:**
  - **Break-ups:** one section-break rig for DD, CV, CF and BW, with no rigid-body sims:
    - split each hull along its bulkhead frames into 3–8 sections;
    - cap the torn edges with kit parts (exposed decks, frames and pipes, not interiors or greebles);
    - drive the pieces apart from the hit point with a procedural `break` 0→1;
    - scatter an instanced debris kit, reused in 36.
  - **Venting and vapour:** short-lived sprays of glinting ice, which is what gas does in vacuum, plus one small cached VDB reused in 16, 20 and 34.
  - **Smoke screen:** one low-res cached VDB in its own layer, reused in 14 and 21.
  - **Haze:** the Mist pass.

### 6. [MAJOR] Swarms with hundreds of plumes (7, 18, 29, 30, 33)
- **Problem:** Shot 7 has 150 missiles, 29 and 33 have ~400–600 plus decoys each, 18 has dozens of drones and 30 has a pellet cloud. Plumes built like the M-1C gas (layered transparent shells), or carrying lights, mean minutes per frame. Specular pellets under lamps make fireflies.
- **Evidence:** LREF doctrine [A-26]: "two waves of about 400–600 missiles plus decoys each". README: the M-1C plasma needs 64 transparent bounces.
- **Fix:** One Geometry Nodes swarm system serves FX-SWARM, FX-DRN and FX-CAN:
  - a launch time for each instance;
  - three LODs, with the hero missile only for the nearest ~10;
  - each plume a single emissive mesh with emission sampling off (as the burst materials already are);
  - lights only on the ~5 nearest plumes or flashes;
  - pellets as emissive points whose brightness follows the lamp angle;
  - the swarm in its own layer.

### 7. [MINOR] The World is in every shot but set for low orbit (all shots)
- **Problem:** MAREN lists only 3, 31 and 37, but the World-shader planet is in every frame. It is placed for low orbit and lights the ship's underside, while the board runs from 450,000 km out (Maren 1.6° across) to Breakwater's orbit (17.5°). Far bodies at real scale also break float precision.
- **Evidence:** README, Environment.
- **Fix:**
  - World presets for arrival, the Breakers, the Lee and Breakwater, with the planet-shine scaled to each.
  - Skerry as a second World body or a proxy at the right angular size.
  - Each set-up's camera near the world origin.
  - The Site 1 plateau never resolves, so a light that goes out is enough.

### 8. [MINOR] Final renders must survive a week on one machine (all shots)
- **Problem:** `render_anim.py` writes H.264 with the grade baked in. A crash loses the clip, and any grade tweak means a re-render.
- **Evidence:** README; project_notes. The user has already had to restart the machine mid-task (user_messages 2026-09-28).
- **Fix:**
  - One job per shot, rendered to multilayer EXR sequences (DWAA).
  - Placeholders on and Overwrite off, so a crashed render resumes.
  - Grade with `LREF_Compositor` in a separate pass.
  - Plan for ~100 GB of disk.

### 9. [MINOR] No build order or shared set-ups (all shots)
- **Problem:** Assets are grouped by faction, not by dependency, and the 37 shots are treated as 37 scenes.
- **Evidence:** The shots reduce to eight sets, and most Endeavor shots match existing cameras.
- **Fix:**
  - **Sets:**
    - **Endeavor:** 1, 2, 4, 8, 10, 12, 14, 21, 23–25, 27, 32, 36, 37. Start from `CAM_Nose`, `CAM_LookDev_Pair/Yoke`, `CAM_Radiator_Slot`, `CAM_Railgun_House`, `CAM_Engines_Burn` and `CAM_Hero`. Shots 8 and 21 share the orbit move and the flip; 10, 23 and 37 share the fins-out action.
    - **Astrid:** 6, 17a, 35a.
    - **Hedgehog:** 7, 29.
    - **Breakers:** 11, 13, 15, 16, 18, 20, 17b.
    - **Lee:** 22, 26, 29, plus plates for 23–27.
    - **Breakwater:** 31, 33, 34, 35b, plus 36's debris.
    - **Plates:** 3, 5, 9, 37.
    - **2D:** 5, 6b, 12's POV insert, 19, 28.
  - **Order:**
    1. The picks, the EN rebuild and rig items, the World presets, the benchmarks, and an EEVEE timing animatic (preview only).
    2. Send the batched concept round now, since it waits on the user.
    3. Meanwhile, build what already has art: the FX library, BRK then LEE, GI with GI-MAV, DD, AST.
    4. The concept-gated items: MSL-V, CV and drones, EMP-POD/RG, BW with BW-BRK, GI-GUN.
    5. The proxies, and shot 3, last.

## Asset list corrections
- **EN, M1C:** change "built" to "extend: rebuild after the wake-style and PDC picks".
- **EN-FIN:** three states: intact, a pre-fractured port fin (24), and a stump (28–37). Add per-fin properties (24, 36, 37). Drop the "cut-loose fin": no shot shows it.
- **EN-DMG:** a `dmg_belt` toggle from shot 26 on. It only reads on screen in 36.
- **New EN-PD and WORLD (extend):** the items from #4 and #7.
- **MSL-V:** concept first = yes, since these are five new weapon designs. Name the Casaba killer, add shots 33 and 34, and ask for LODs.
- **AST:** a concept sheet for the spinal muzzle and its FX look.
- **GI-GUN:** four scaled RC_M1C twins, so the concept sheet only settles the layout.
- **GI-PD:** build after the PDC pick; a silhouette is enough in shot 4.
- **CF, TND, RING:** a proxy, a silhouette and lights respectively, if the user agrees.
- **DRN-L, DRN-C:** one design each, plus the hide. Add DRN-L to shot 16 ("its drones drift").
- **DD:** drop it from shot 15, where it is ~1 px.
- **SHD:** fill the distant park with scaled instances of the gold shield.
- **LEE:** a Geometry Nodes boulder scatter from the BRK kit. Hero surface tiles only for 22 and 29.
- **SKR:** one still plate; the battery and depot are flash positions only.
- **FX-BREAK:** the section-break rig and a debris kit instead of cell fracture.
- **FX-SWARM, FX-DRN, FX-CAN:** merge into one system.
- **New FX-VENT** (16, 20, 24, 34) and **New FX-FAR**, distant drive plumes (3, 8, 22, 30).
- **HUD, SUB:**
  - The user approves a style frame first.
  - The mission clock appears on every time-jump shot.
  - Subtitles and the clock go in during the edit, after the grade, so a changed line never forces a re-render.
  - HUD plots can reuse the SVG map code in `build_storyboard.py`.

## What works
- Twelve shots (55 s) need only the Endeavor plus FX and rig extensions, and two more (27, 37) need just a CF proxy and the planet re-dress. Production can start there.
- Most heavy shots are 3–5 s, and 5, 19 and 28 are already 2D.
- The reuse instincts are right: one frigate hull with three modules, a shared break-up asset, and the M-1C as the fleet gun.
- The concept-first flags are correct for every design without reference art, and `render_budget()` takes measured numbers straight in.
