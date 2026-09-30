# Asset requests

Everything *Operation Tidebreak* (revision 4 · after review round 3) needs from the modelling session, with the shots that need each item. Generated from `storyboard/tidebreak_data.py`.

- **Status:** *built* exists; *extend* exists but needs additions; *new* must be made.
- **Concept first:** per the user's rule, new weapon and ship designs go through concept sheets and the user picks before modelling. Items without reference art are flagged too.
- **Detail level:** the user asked for everything hero-detailed. The closest view says how much of that detail the camera can ever see; proxies for the smallest items are open question Q13.
- **Set-ups:** 9 set-ups cover the film: the Endeavor (1–2, 4, 13, 15, 17–19, 28, 31, 33–34, 36, 38–40, 49, 58, 61); the Astrid (6, 23, 48, 55); the destroyers (5, 21–22, 43–44); the Breakers (14, 16, 20, 24–25, 27); the pack and Anchor (9, 30, 32, 35, 37, 41, 45–46); missile close-ups (10, 51); Breakwater over Maren (47, 50, 52–54, 56–57, 59–60); long-lens plates (3, 11–12); 2D (7–8, 26, 29, 42).

## LREF ships and craft

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| AST | L.R.E.F.S. Astrid (Hanuman heavy cruiser) | new |  | shot 6: MS 50 mm along the dorsal hull (the muzzle: 55), fills the frame | 3, 6, 11, 13, 23, 48, 55 | Hero, ~1,650 m. Build from lref_kit: M-1Cs, arrays, CIWS, fins, rings and shield are instances, so the new hero work is the hull, the AVPSA dish and the spinal. Concept sheet for the spinal muzzle and its FX look. Controls: `avpsa_az`, `avpsa_el`, `fins_deploy` (8), `spinal_charge`, `spinal_shot`, `engine_throttle`, `rcs_bow`/`rcs_stern`, `laser_power`/`laser_traverse`, plus the Endeavor's `ciws_phase` and `ciws_fire` on its instanced CIWS. Art exists. |
| GI | Garibaldi-Ivanova frigate hull | new |  | shot 9: hull camera on the Infinity, fills the frame | 3, 9, 11, 30, 45–46 | Hero, ~420 m. One hull for all five frigates; module bay; warp rings; shield; spinning hab section; CIWS instanced from the Endeavor's, with its `ciws_phase` and `ciws_fire` (the Donnager's in 45). Art exists. |
| GI-MAV | Hedgehog (MAV) module | new |  | shot 9: hull camera beside the pods, fills the frame | 3, 9, 45–46 | ~360 pods; `pod_ripple` launch control, driven from the swarm system's per-pod launch-time attribute so doors and launches can't drift apart. Art exists. |
| GI-GUN | Gun module (4 large kinetic batteries) | new | yes | shot 30: far off, shelling rocks, a few px | 30 | Four scaled M-1C twins; the concept sheet only settles the layout. Seen only far off in 30: a silhouette is enough if the user agrees (Q13). |
| GI-PD | PD module | new | yes | shot 4: behind the parked shields, ~40 px | 4 | Build after the PDC pick. Seen only far off in shot 4: a silhouette is enough if the user agrees (Q13). |
| DD | ECW destroyer | new |  | shot 5: MS 40 mm at ~600 m, fills the frame | 3, 5, 11, 21–22, 43–44 | Hero, ~200 m. The dish sits fixed, forward, behind the shield, as in the art (Q14); it is unmasked when the shield leaves. Controls: `booms_deploy`, `drone_bay`, `rcs`, `dmg_boom` (the Extenuating's scorched boom from 44). Model it in sections at its bulkhead frames for the section-break rig. Art exists. |
| DD-BRK | Destroyer break-up (Canterbury) | new |  |  | 22 | Section-break rig: holed bow to stern, venting, the hull parting in two. |
| CV | Corvette class | new | yes | shot 27: 800 mm at ~20 km, ~200 px | 3, 11, 14, 25, 27, 30, 45 | No reference art: concept sheet first. Brief: 50–150 m; two warp rings at the ends; a jettisonable forward shield; radiators and booms that stow for warp; no spin section; anti-drone weapons 'far more powerful and varied' than a big ship's PD. Model it in sections at its bulkhead frames. |
| CV-BRK | Corvette destruction (Normandy) | new |  |  | 27 | Section-break rig variant. |
| TND | Nauvoo, fleet tender | new | yes | shot 4: behind the parked shields, ~40 px | 3–4 | No reference art: concept sheet first. Brief: two warp rings, forward shield, stowable radiators; cradles for spare shields; a rig for swapping frigate modules. Seen only far off: a silhouette if the user agrees (Q13). |
| SHD | Parked impact shields | extend |  |  | 4 | Scaled instances of the gold shield for the park cluster. |
| DRN-L | LREF drone | new | yes | shot 5: MS 40 mm, ~40 px | 5, 14, 25, 30, 43 | One design (picket/PD/EW variants by payload only), concept first. |
| MSL | Missile asset (26 m, plume, thrust) | built |  |  | inside FX-SWARM (9, 25, 27, 43, 45–48, 52) | The swarm system's stand-in and base mesh, not a hero: the variants (MSL-V) scale it down to fit the pods. |
| MSL-V | Missile variants | new | yes | shot 51: ECU 100 mm on a Casaba killer's nose (and CU 85 mm alongside one in 10), fills the frame | 9–10, 16, 45–48, 51–53 | Concept sheet first (five new weapon designs). The capital-ship killer, sized to fit the hedgehog's pods (no more than ~20 m; the art's pods are ~6–7 m boxes in an array 32–49 m across), in a nuclear and a Casaba version with a hardened ablative nose, a seeker window behind a shutter and a slow spin: the hero missile, LOD0 built for the extreme close-up of 51 and flown in 10 too. The small multi-pack missile with MIRV bus; the decoy, which mimics a killer's signature and size with a deployable shroud; the EW missile; the Compact belt-pod missile. Controls: `seeker_shutter`, `cap_glow` (the ablative cap under laser fire), with spin as a per-instance attribute in the swarm. Three LODs each, dropped into the swarm system's slots. |

## Endeavor and M-1C

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| EN | L.R.E.F.S. Endeavor (rigged) | extend |  |  | 1–2, 4, 11, 13–15, 17–19, 28, 30–31, 33–36, 38–40, 49, 58, 61 | Hero ship. Rebuild after the M-1C wake-style and PDC picks that are still pending in the modelling session (Q15), then link it into shot files with a library override on the rig empty. Its states (STATES) are presets the shot files load. |
| EN-FIN | Endeavor: per-fin control and damage | extend |  |  | 31, 33–36, 38–40, 49, 58, 61 | Per-fin deploy properties `fin_port`, `fin_starboard`, `fin_dorsal`, `fin_ventral` (the ship-wide `radiator_deploy` stays as a master). Port fin states via `fin_port_state`: intact, pre-fractured (shot 34), stump (every Endeavor shot after it). For the dark lee, an area light on each fin with its strength driven by `heat`, and emission sampling off on the fin meshes. |
| EN-PD | Endeavor: defence, countermeasure and emergency controls | extend |  |  | 17, 19, 28, 58 | `ciws_phase` (a keyed angle, with a spin-blur swap above ~600 rpm, because `ciws_rpm` changes jump and strobe), `ciws_fire` (muzzle empties), `cm_chaff`, `cm_flare`, `cm_smoke`, `ew_active`, `water_dump` (valve and emitter for FX-DUMP). |
| EN-MAST | Endeavor: sensor-mast shutters | extend |  |  | 15 | `mast_shutter`: armoured shutters close over the mast windows. |
| EN-DMG | Endeavor: hull damage | extend |  |  | 35–36, 38–40, 49, 58, 61 | `dmg_belt`: spall and scorching on the port belt from shot 35 on; it must read in shot 58, which runs along the port flank. |
| M1C | M-1C twin railcannon | extend |  | shot 40: CU 85 mm on the barrels and the crest vent, fills the frame | 38–40 | Fleet gun. Wake style still to be picked (split, ripple, bulk, extend, combined: Q15). The ship's `rail_wake`, `rail_lock` and `rail_arm` play the wake in 39 in the README's order (power up, unclamp, lay, open the shell); per-gun `charge_a/b`, `shot_a/b`, `fins_a/b`, `heat_a/b` play 40, where only the gun that fired vents. |

## The Maren Compact

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| BW | Breakwater, Compact monitor | new | yes | shot 54: drone camera near the monitor, fills the frame | 47, 50–54, 56–57, 59 | Concept sheet first. ~1,800 m warpless monitor: no rings or shield, ~2 m belt, 6 twin heavy turrets, 24 PD lasers, 40 CIWS, 64 cells, armoured louvred radiators. Controls: `turret_traverse`, `turret_elevation`, `cells_open`, `drive_glow`, `vent`, `ciws_phase`/`ciws_fire` with muzzle empties, PD `laser_power`. Model it in sections at its bulkhead frames. |
| BW-BRK | Breakwater break-up | new |  |  | 53–54, 56–57, 59 | Section-break rig: spear wounds on the drive bells, the spinal entry amidships, secondaries, the back breaking. |
| CF | Compact frigate | new | yes | shot 37: 1,000 mm at 45 km, ~420 px | 35, 37 | Concept sheet first. ~350 m; coilgun and missiles; simple instanced escape pods; modelled in sections for its break-up. Seen at ~420 px in shot 37 (1,000 mm at 45 km), so it needs real detail. |
| DRN-C | Compact drone and its hide | new | yes | shot 25: 28 mm, nearest drones ~1 km off, ~30 px | 25, 27, 45 | One design (plasma-bomb payload) plus the cold hide on a rock; concept first. |
| EMP-POD | Cold missile pod on a rock | new | yes | shot 16: drone near the rock, ~300 px | 16 | Concept first. Controls: `heave`, `petals`. |
| EMP-RG | Breakers railgun platform | new | yes | shot 20: drone over the platform, fills the frame | 20, 24, 32, 41 | Concept first. Buried twin railgun. Controls: `unmask`, `shot`. |
| RING | Inner-ring station | new | yes | shot 47: far along the orbit, points of light | 47, 59 | Only ever a point of light at ~21,800 km spacing: lights only, if the user agrees (Q13). |
| SKR | Skerry | new |  | shot 12: 1,200 mm at ~262,000 km, a quarter-frame disc | 7, 10, 12 | One still plate of an airless moon; the battery, tracks and depot are flash and light positions only. |

## Environment

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| WORLD | World presets and sun | extend |  |  | every 3D shot | Used by every 3D shot. One preset per environment (ENVS), with planet-shine scaled to each (Maren is 1.6° across from the exit, ~17.5° from Breakwater's orbit); a Sun object that drives the World (today `TO_SUN` needs a rebuild), set 30° off the approach line and ~12° above the ring plane (LIGHTING); Skerry as a second body at the right angular size; a sun-direction gradient on the Breakers haze in comp; each set-up's camera kept near the world origin. |
| MAREN | Maren: planet re-dress | extend |  |  | 3, 47, 50, 54, 59–61 | New continents and weather, night-side cities. Site 1's light cluster in 60 (about 10 px at 2,000 mm, where one pixel is ~340 m) is a masked texture or a comp element over a plate rendered once, not a feature of the World shader, centred on an otherwise dark plateau with enough relief to read as ground. |
| BRK | The Breakers environment | new |  |  | 3, 14, 16, 20, 24–25, 30, 32, 41 | The dust haze as the Mist pass plus a sparse glitter layer; a generic rock kit; large rocks at realistic spacing. |
| ANCHOR | Anchor: hero rock | new |  | shot 30: low over the surface, fills the frame | 30, 35, 45–46 | ~18 km rubble pile: a Geometry Nodes boulder scatter from the BRK kit, with hero surface tiles only where the camera goes close (shots 30, 45); the moonlet with the frigate's cleft. |

## Blocking

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| PROXY | Blocking proxies and first-version effects | new |  |  | every 3D shot | True-scale stand-ins for every ship and rock, built in step 1 for the timing animatic and the benchmarks, with benchmark-grade first versions of the effects the benchmarks need: stock tracer streaks and flashes (FX-PD), a Quick Smoke cache at both scales (FX-SMOKE), a point-cloud plume (FX-DUMP) and one displaced rock tile. The finished effects still come in step 3. |

## Effects

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| FX-WARP | Warp-exit flash | new |  |  | 1, 3 | Bubble collapse bloom (comp plus a light). |
| FX-SWARM | Swarm system | new |  |  | 9, 25, 27, 43, 45–48, 52 | One Geometry Nodes system for missiles, drones and canister pellets: per-instance launch time, three LODs (hero mesh only for the nearest ~10), each plume a single emissive mesh with emission sampling off, real lights only on the ~5 nearest plumes or flashes (faded in and out over ~6 frames so the hull lighting doesn't pop), pellets as emissive points whose brightness follows the lamp angle, rendered in its own view layer. Built first on the existing missile (MSL); the variants drop into its LOD slots later. |
| FX-FAR | Distant drive plumes | new |  |  | 3, 11 | Cheap far plumes for long-lens fleet shots. |
| FX-NUKE | Nuclear flashes | new |  |  | 12, 30 | Point flashes: Skerry's surface, the mine at Anchor. |
| FX-PD | Point-defence fire | new |  |  | 18–19, 45, 48, 50–52 | CIWS tracers and kill clouds, chaff, flares, intercept flashes, laser lens pulses, in their own view layer at low samples. |
| FX-SMOKE | Smoke screen | new |  |  | 19, 28, 44 | A cached VDB in two resolutions (medium shot in 19 and 28, fleet scale in 44), rendered in a half-resolution layer. |
| FX-SLUG | Slug streaks and impacts | new |  |  | 20, 24, 32, 34–35, 40–41 | Glints, impact flash, spall cone, shock ring. |
| FX-BREAK | Section-break rig and debris kit | new |  |  | 22, 27, 37, 57 | No cell fracture (the plated kit hulls defeat it): each breakable hull is modelled in 3–8 sections at its bulkhead frames, the torn edges capped with kit parts, the pieces driven apart with a procedural `break` 0→1, and an instanced debris kit scattered. |
| FX-VENT | Venting in vacuum | new |  |  | 22, 34, 37, 53–54 | Short-lived sprays of glinting ice (what gas and coolant do in vacuum); one small cached VDB reused. |
| FX-DUMP | Water-dump plume | new |  |  | 58 | A Geometry Nodes ice point cloud with a thin low-resolution VDB core, in its own layer at half resolution with one volume bounce. Costed at ~250 s/frame and part of the volume benchmark. |
| FX-FIN | Fin shatter | new |  |  | 34 | The pre-fractured port fin's shards and glow. |
| FX-LANCE | Plasma lance | new |  |  | 37 | A field-held violet-white jet from the nose channels to the target inside a faint field sheath; it fizzles back when `lance_power` cuts. |
| FX-CASABA | Casaba jets | new |  |  | 53 | Narrow nuclear spears from 2 km standoff. |
| FX-SPINAL | Spinal fire and impact | new |  |  | 23, 55, 57 | Muzzle bloom down the Astrid's kilometre barrel; impact flash and spall. |
| FX-DAZZLE | Dazzle and whiteout | new |  |  | 7, 15, 44 | Comp: bloom on optics, POV whiteout. |
| FX-EW | EW overlay | new |  |  | 26, 49 | Comp: glitch bands on HUD inserts. |

## 2D compositing

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| HUD | Tactical HUD and mission clock | new |  |  | 1, 7–8, 26, 29, 42, 59 | 2D comp. The user approves a style frame first; the plots can reuse the SVG map code in build_storyboard.py. |
| SUB | Comm subtitles | new |  |  | 3–5, 7–9, 11–16, 21–31, 33–36, 42–50, 52–56, 58–61 | 2D comp, added in the edit; short dim speaker tags. |

## Render budget and the gate

| Class | Kind | Cost | Shots | Frames | Time |
|---|---|---|---|---|---|
| A | Endeavor close-up | ~45 s/frame | 2, 4, 13, 15, 17–18, 31, 33, 36, 38–39, 49 | 1,008 | 12.6 h |
| A2 | Endeavor close-up with heavy FX | ~90 s/frame | 19, 28, 34–35, 40 | 480 | 12.0 h |
| V | Close-up with a hero volume (the water dump) | ~250 s/frame | 58 | 96 | 6.7 h |
| B | One hero ship or rock, full view | ~75 s/frame | 5–6, 10, 14, 16, 20, 23–24, 37, 43, 51, 54–55 | 1,032 | 21.5 h |
| C | Several ships or heavy FX (FX in own layers) | ~200 s/frame | 9, 25, 30, 44–48, 52–53, 57 | 1,032 | 57.3 h |
| S | Small subject on black with its FX (up to ~350 px) | ~30 s/frame | 22, 27 | 240 | 2.0 h |
| P | Locked camera: a plate rendered once, plus one moving layer | ~30 s/frame | 56, 61 | 312 | 2.6 h |
| D | Wide, distant, small subject on black, or plate | ~15 s/frame | 1, 3, 11–12, 21, 32, 41, 50, 59–60 | 1,008 | 4.2 h |
| E | 2D comp / HUD | ~2 s/frame | 7–8, 26, 29, 42 | 744 | 0.4 h |
| | **Total** | | 61 shots | 5,952 | **119.3 h** |
| | With 30% for re-renders | | | | **155.1 h** |

These costs are estimates, not measurements. Step 1 benchmarks the methods with stand-ins and first-version effects (PROXY), so nothing waits on new assets: class C (two or three linked Endeavors, 600 instances of the existing missile through the swarm system and an FX-PD layer at 16–32 spp; record s/frame and VRAM), class B (one linked Endeavor in full view, sunlit, its drive lit), the volumes (the fleet-scale smoke of 44 and the water dump of 58), the dark lee (the Endeavor lit only by its fins, and one M-1C shot, as in 31 and 40), plus shots 2 and 38. Gate before the full pass: enter each measured s/frame in MEASURED (storyboard/tidebreak_data.py) and rebuild, so the budget uses it. If the total with the re-render allowance is over the gate, apply the levers agreed in advance, in this order, until it isn't: 1) half-resolution volume and FX layers; 2) swarm layers at 16 spp with earlier LOD switches; 3) a second trimmed from each of 9, 45 and 52. The ceiling is a week (168 h) per full pass.

The gate: 155 h with the allowance (estimated), against 160 h, so 5 h to spare. Break-even for one class on its own, the others as they stand: C 213 s/frame (estimate 200), B 88 s/frame (estimate 75), A 58 s/frame (estimate 45), A2 118 s/frame (estimate 90), V 391 s/frame (estimate 250).

## Production plan

- **Sets:** 9 set-ups cover the film: the Endeavor (1–2, 4, 13, 15, 17–19, 28, 31, 33–34, 36, 38–40, 49, 58, 61); the Astrid (6, 23, 48, 55); the destroyers (5, 21–22, 43–44); the Breakers (14, 16, 20, 24–25, 27); the pack and Anchor (9, 30, 32, 35, 37, 41, 45–46); missile close-ups (10, 51); Breakwater over Maren (47, 50, 52–54, 56–57, 59–60); long-lens plates (3, 11–12); 2D (7–8, 26, 29, 42).
- **Batches:** Render in batches by World preset: arrival and coast (sunlit crescent, Maren 1.6°): 1–6, 9–13; the Breakers (backlit haze): 14–25, 27–28; Anchor's dark lee: 30–41; the final approach (Maren growing, night side): 43–46; Breakwater over Maren's night side: 47–61.
- **Order:** 1) Step 1: the user's pending picks (Q15); the Endeavor rebuild and its new rig items; the World presets; blocking proxies and first-version effects (PROXY) and a timing animatic; the method benchmarks and the gate (see the render note); the swarm system, built on the existing missile with LOD slots for the variants. 2) One batched concept round, missile variants first, since it waits on the user. 3) Meanwhile the assets with art: the FX library, the Breakers then Anchor, the frigate with its hedgehog module, the destroyer, the Astrid. 4) The concept-gated assets: the missile variants into the swarm's slots, the corvette and drones, the emplacements, Breakwater, the gun module. Every breakable hull (DD, CV, CF, BW) is modelled in sections at its bulkhead frames. 5) The long-lens plates last; 48 renders last of all, since it waits on three gates (the Astrid, the missile variants, the PDC pick).
- **Methods:** The foreground pods of 46 in their own layer, defocused in comp. Every rock and plume instanced, with a rock tile in the class C benchmark (30, 45). In the dark lee, area lights on each fin driven by `heat`, with emission sampling off on the fin meshes (EN-FIN). 56 and 61 are locked off: a plate rendered once plus one moving layer (the turrets and vents; the ship). Site 1's lights in 60 are a comp element over a plate.
- **Rendering:** One job per shot to multilayer EXR sequences (DWAA), Placeholders on and Overwrite off so a crashed render resumes; the grade (`LREF_Compositor`) as a separate pass; emissive FX in their own view layers at 16–32 spp with 1–3 proxy lights in the beauty layer; Persistent Data; adaptive sampling with denoising; vector blur in comp; plan ~150 GB of disk.
