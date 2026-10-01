# Asset requests

Everything *Operation Tidebreak* (revision 8 · the dialogue review: orders and reports as a fleet net gives them, one name for each thing) needs from the modelling session, with the shots that need each item. Generated from `storyboard/tidebreak_data.py`.

- **Status:** *built* exists; *extend* exists but needs additions; *new* must be made.
- **Concept first:** per the user's rule, new weapon and ship designs go through concept sheets and the user picks before modelling. Items without reference art are flagged too.
- **Detail level:** the user asked for everything hero-detailed. The closest view says how much of that detail the camera can ever see; proxies for the smallest items are open question Q13.
- **Set-ups:** 9 set-ups cover the film: the Endeavor (2–3, 5, 14, 16, 18–20, 29, 32, 34–35, 37, 39–41, 51, 60, 63); the Astrid (7, 24, 50, 57); the destroyers (6, 22–23, 44–45); the Breakers (15, 17, 21, 25–26, 28); the pack and Anchor (10, 31, 33, 36, 38, 42, 46–47); missile close-ups (11, 53); Breakwater over Maren (48, 52, 54–56, 58–59, 61–62); long-lens plates (4, 12–13); 2D (1, 8–9, 27, 30, 43, 49, 64).

## LREF ships and craft

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| AST | L.R.E.F.S. Astrid (Hanuman heavy cruiser) | new |  | shot 7: MS 50 mm along the dorsal hull (the muzzle: 57), fills the frame | 4, 7, 12, 14, 24, 50, 57 | Hero, ~1,650 m. Build from lref_kit: M-1Cs, arrays, CIWS, fins, rings and shield are instances, so the new hero work is the hull, the AVPSA dish and the spinal. Concept sheet for the spinal muzzle and its FX look. Controls: `avpsa_az`, `avpsa_el`, `fins_deploy` (8), `spinal_charge`, `spinal_shot`, `engine_throttle`, `rcs_bow`/`rcs_stern`, `laser_power`/`laser_traverse`, plus the Endeavor's `ciws_phase` and `ciws_fire` on its instanced CIWS. Art exists. |
| GI | Garibaldi-Ivanova frigate hull | new |  | shot 10: hull camera on the Infinity, fills the frame | 4, 10, 12, 31, 46–47 | Hero, ~420 m. One hull for all five frigates; module bay; warp rings; shield; spinning hab section; 4 CIWS mounts on the hull whatever the module, instanced from the Endeavor's, with their `ciws_phase` and `ciws_fire` (the Donnager's in 46). Art exists. |
| GI-MAV | Hedgehog (MAV) module | new |  | shot 10: hull camera beside the pods, fills the frame | 4, 10, 46–47 | ~360 pods; `pod_ripple` launch control, driven from the swarm system's per-pod launch-time attribute so doors and launches can't drift apart. Art exists. |
| GI-GUN | Gun module (4 large kinetic batteries) | new | yes | shot 31: far off, shelling rocks, a few px | 31, 46 | Four scaled M-1C twins; the concept sheet only settles the layout. Seen only far off in 31: a silhouette is enough if the user agrees (Q13). |
| GI-PD | PD module | new | yes | shot 5: behind the parked shields, ~40 px | 5 | Build after the PDC pick. Seen only far off in shot 5: a silhouette is enough if the user agrees (Q13). |
| DD | ECW destroyer | new |  | shot 6: MS 40 mm at ~600 m, fills the frame | 4, 6, 12, 22–23, 44–45 | Hero, ~200 m. The dish sits fixed, forward, behind the shield, as in the art (Q14); it is unmasked when the shield leaves. Controls: `booms_deploy`, `drone_bay`, `rcs`, `dmg_boom` (the Extenuating's scorched boom from 45). Model it in sections at its bulkhead frames for the section-break rig. Art exists. |
| DD-BRK | Destroyer break-up (Canterbury) | new |  |  | 23 | Section-break rig: holed bow to stern, venting, the hull parting in two. |
| CV | Corvette class | new | yes | shot 28: 800 mm at ~20 km, ~200 px | 4, 12, 15, 26, 28, 31, 46 | No reference art: concept sheet first. Brief: 50–150 m; two warp rings at the ends; a jettisonable forward shield; radiators and booms that stow for warp; no spin section; anti-drone weapons 'far more powerful and varied' than a big ship's PD. Model it in sections at its bulkhead frames. |
| CV-BRK | Corvette destruction (Normandy) | new |  |  | 28 | Section-break rig variant. |
| TND | Nauvoo, fleet tender | new | yes | shot 5: behind the parked shields, ~40 px | 4–5 | No reference art: concept sheet first. Brief: two warp rings, forward shield, stowable radiators; cradles for spare shields; a rig for swapping frigate modules. Seen only far off: a silhouette if the user agrees (Q13). |
| SHD | Parked impact shields | extend |  |  | 5 | Scaled instances of the gold shield for the park cluster. |
| DRN-L | LREF drone | new | yes | shot 6: MS 40 mm, ~40 px | 6, 15, 26, 31, 44 | One design (picket/PD/EW variants by payload only), concept first. |
| MSL | Missile asset (26 m, plume, thrust) | built |  |  | inside FX-SWARM (10, 26, 28, 44, 46–48, 50, 54) | The swarm system's stand-in and base mesh, not a hero: the variants (MSL-V) scale it down to fit the pods. |
| MSL-V | Missile variants | new | yes | shot 53: ECU 100 mm on a Casaba killer's nose (and CU 85 mm alongside one in 11), fills the frame | 10–11, 17, 46–48, 50, 53–55 | Concept sheet first (five new weapon designs). The capital-ship killer, sized to fit the hedgehog's pods (no more than ~20 m; the art's pods are ~6–7 m boxes in an array 32–49 m across), in a conventional (teller-device) version and a Casaba version, both nuclear, with a hardened ablative nose, a seeker window behind a shutter and a slow spin: the hero missile, LOD0 built for the extreme close-up of 53 and flown in 11 too. The small multi-pack missile with MIRV bus. The decoy, which fits a multi-silo cell, opens a shroud to a killer's size and signature after launch, and carries a motor sized (or dead mass) so its plume and acceleration match a killer's through the 30 g boost. The EW missile; the Compact belt-pod missile. Controls: `seeker_shutter`, `cap_glow` (the ablative cap under laser fire), with spin as a per-instance attribute in the swarm. Three LODs each, dropped into the swarm system's slots. |

## Endeavor and M-1C

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| EN | L.R.E.F.S. Endeavor (rigged) | extend |  |  | 2–3, 5, 12, 14–16, 18–20, 29, 31–32, 34–37, 39–41, 51, 60, 63 | Hero ship. Rebuild after the M-1C wake-style and PDC picks that are still pending in the modelling session (Q15), then link it into shot files with a library override on the rig empty. Its states (STATES) are presets the shot files load. Add `dump_light`: a work light at the water-dump valve that rakes the port belt in 60, which plays in Maren's shadow. |
| EN-FIN | Endeavor: per-fin control and damage | extend |  |  | 32, 34–37, 39–41, 51, 60, 63 | Per-fin deploy properties `fin_port`, `fin_starboard`, `fin_dorsal`, `fin_ventral` (the ship-wide `radiator_deploy` stays as a master). Port fin states via `fin_port_state`: intact, pre-fractured (shot 35), stump (every Endeavor shot after it). For the dark lee, an area light on each fin with its strength driven by `heat`, and emission sampling off on the fin meshes. |
| EN-PD | Endeavor: defence, countermeasure and emergency controls | extend |  |  | 18, 20, 29, 60 | `ciws_phase` (a keyed angle, with a spin-blur swap above ~600 rpm, because `ciws_rpm` changes jump and strobe), `ciws_fire` (muzzle empties), `cm_chaff`, `cm_flare`, `cm_smoke`, `ew_active`, `water_dump` (valve and emitter for FX-DUMP). |
| EN-MAST | Endeavor: sensor-mast shutters | extend |  |  | 16 | `mast_shutter`: armoured shutters close over the mast windows. |
| EN-DMG | Endeavor: hull damage | extend |  |  | 36–37, 39–41, 51, 60, 63 | `dmg_belt`: spall and scorching on the port belt from shot 36 on; it must read in shot 60, which runs along the port flank in the dark, under the dump valve's work light (`dump_light` on EN). |
| M1C | M-1C twin railcannon | extend |  | shot 41: CU 85 mm on the barrels and the crest vent, fills the frame | 39–41 | Fleet gun. Wake style still to be picked (split, ripple, bulk, extend, combined: Q15). The ship's `rail_wake`, `rail_lock` and `rail_arm` play the wake in 40 in the README's order (power up, unclamp, lay, open the shell); per-gun `charge_a/b`, `shot_a/b`, `fins_a/b`, `heat_a/b` play 41, where only the gun that fired vents. |

## The Maren Compact

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| BW | Breakwater, Compact monitor | new | yes | shot 56: drone camera near the monitor, fills the frame | 48, 52–56, 58–59, 61 | Concept sheet first. ~1,800 m warpless monitor: no rings or shield, ~2 m belt, 6 twin heavy turrets, 24 PD lasers, 40 CIWS, 64 cells, armoured louvred radiators, rows of small lit ports (it is crewed): emissive, with emission sampling off and any light pools painted into the texture. Controls: `turret_traverse`, `turret_elevation`, `cells_open`, `drive_glow`, `vent`, `ciws_phase`/`ciws_fire` with muzzle empties, PD `laser_power`. Model it in sections at its bulkhead frames. |
| BW-BRK | Breakwater break-up | new |  |  | 55–56, 58–59, 61 | Section-break rig: spear wounds on the drive bells, the spinal entry amidships, secondaries, the back breaking. |
| CF | Compact frigate | new | yes | shot 38: 1,000 mm at 45 km, ~420 px | 36, 38 | Concept sheet first. ~350 m; coilgun and missiles; simple instanced escape pods; modelled in sections for its break-up. Seen at ~420 px in shot 38 (1,000 mm at 45 km), so it needs real detail. |
| DRN-C | Compact drone and its hide | new | yes | shot 26: 28 mm, nearest drones ~1 km off, ~30 px | 26, 28, 46 | One design (plasma-bomb payload) plus the cold hide on a rock; concept first. |
| EMP-POD | Cold missile pod on a rock | new | yes | shot 17: drone near the rock, ~300 px | 17 | Concept first. Controls: `heave`, `petals`. |
| EMP-RG | Breakers railgun platform | new | yes | shot 21: drone over the platform, fills the frame | 21, 25, 33, 42 | Concept first. Buried twin railgun. Controls: `unmask`, `shot`. |
| RING | Inner-ring station | new | yes | shot 48: far along the orbit, points of light | 48, 61 | Only ever a point of light at ~21,800 km spacing: lights only, if the user agrees (Q13). |
| SKR | Skerry | new |  | shot 13: 1,200 mm at ~262,000 km, a quarter-frame thin crescent on a dark disc | 8, 11, 13 | One still plate of an airless moon; the battery, tracks and depot are flash and light positions only. |

## Environment

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| WORLD | World presets and sun | extend |  |  | every 3D shot | Used by every 3D shot. One preset per environment (ENVS), with planet-shine scaled to each (Maren is 1.6° across from the exit, ~17.5° from Breakwater's orbit); a Sun object that drives the World (today `TO_SUN` needs a rebuild), set ~33° off the approach line in the ring plane (LIGHTING); for Maren's shadow (World E), Skerry as a dim, cool key light from its bearing (~0.01 lux: push the exposure), the red ring of the atmosphere as a faint rim round the limb, and the night side's city lights as detail on the disc, with the red raised only within ~5 min of each sunrise; the sunrise in 58 as the Sun's strength and colour keyed through the ~2 min penumbra, deep red to white, raking from near the frame edge; a still star plate for the title and end cards, graded apart from the film's black crush; Skerry as a second body at the right angular size; a sun-direction gradient on the Breakers haze in comp; each set-up's camera kept near the world origin. |
| MAREN | Maren: planet re-dress | extend |  |  | 4, 48, 52, 56, 61–63 | New continents and weather, night-side cities. Site 1's light cluster in 62 (about 10 px at 2,000 mm, where one pixel is ~340 m) is a masked texture or a comp element over a plate rendered once, not a feature of the World shader, centred on an otherwise dark plateau with enough relief to read as ground. |
| BRK | The Breakers environment | new |  |  | 4, 15, 17, 21, 25–26, 31, 33, 42 | The dust haze as the Mist pass plus a sparse glitter layer; a generic rock kit; large rocks at realistic spacing. |
| ANCHOR | Anchor: hero rock | new |  | shot 31: low over the surface, fills the frame | 31, 36, 46–47 | ~18 km rubble pile: a Geometry Nodes boulder scatter from the BRK kit, with hero surface tiles only where the camera goes close (31; in 46 the rock is a black disc 150 km off); the moonlet with the frigate's cleft. |

## Blocking

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| PROXY | Blocking proxies and first-version effects | new |  |  | every 3D shot | True-scale stand-ins for every ship and rock, built in step 1 for the timing animatic and the benchmarks, with benchmark-grade first versions of the effects the benchmarks need: stock tracer streaks and flashes (FX-PD), a Quick Smoke cache at both scales (FX-SMOKE), a point-cloud plume (FX-DUMP) and one displaced rock tile. The finished effects still come in step 3. |

## Effects

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| FX-WARP | Warp-exit flash | new |  |  | 2, 4 | Bubble collapse bloom (comp plus a light). |
| FX-SWARM | Swarm system | new |  |  | 10, 26, 28, 44, 46–48, 50, 54 | One Geometry Nodes system for missiles, drones and canister pellets: per-instance launch time, three LODs (hero mesh only for the nearest ~10), each plume a single emissive mesh with emission sampling off, real lights only on the ~5 nearest plumes or flashes (faded in and out over ~6 frames so the hull lighting doesn't pop), pellets as emissive points whose brightness follows the lamp angle, rendered in its own view layer. Built first on the existing missile (MSL); the variants drop into its LOD slots later. |
| FX-FAR | Distant drive plumes | new |  |  | 4, 12 | Cheap far plumes for long-lens fleet shots. |
| FX-NUKE | Nuclear flashes | new |  |  | 13, 31 | Point flashes: Skerry's surface, the mine at Anchor. |
| FX-PD | Point-defence fire | new |  |  | 19–20, 46, 50, 52–54 | CIWS tracers and kill clouds, chaff, flares, intercept flashes, laser lens pulses, in their own view layer at low samples. |
| FX-SMOKE | Smoke screen | new |  |  | 20, 29, 45 | A cached VDB in two resolutions (medium shot in 20 and 29, fleet scale in 45), rendered in a half-resolution layer. |
| FX-SLUG | Slug streaks and impacts | new |  |  | 21, 25, 33, 35–36, 41–42 | Glints, impact flash, spall cone, shock ring. |
| FX-BREAK | Section-break rig and debris kit | new |  |  | 23, 28, 38, 59 | No cell fracture (the plated kit hulls defeat it): each breakable hull is modelled in 3–8 sections at its bulkhead frames, the torn edges capped with kit parts, the pieces driven apart with a procedural `break` 0→1, and an instanced debris kit scattered. |
| FX-VENT | Venting in vacuum | new |  |  | 23, 35, 38, 55–56 | Short-lived sprays of glinting ice (what gas and coolant do in vacuum); one small cached VDB reused. |
| FX-DUMP | Water-dump plume | new |  |  | 60 | A Geometry Nodes ice point cloud with a thin low-resolution VDB core, in its own layer at half resolution with one volume bounce. Costed at ~250 s/frame and part of the volume benchmark. |
| FX-FIN | Fin shatter | new |  |  | 35 | The pre-fractured port fin's shards and glow. |
| FX-LANCE | Plasma lance | new |  |  | 38 | A field-held violet-white jet from the nose channels to the target inside a faint field sheath; it fizzles back when `lance_power` cuts. |
| FX-CASABA | Casaba jets | new |  |  | 55 | Narrow nuclear spears from 2 km standoff. |
| FX-SPINAL | Spinal fire and impact | new |  |  | 24, 57, 59 | Muzzle bloom down the Astrid's kilometre barrel; impact flash and spall. |
| FX-DAZZLE | Dazzle and whiteout | new |  |  | 8, 16, 45 | Comp: bloom on optics, POV whiteout. |
| FX-EW | EW overlay | new |  |  | 27, 51 | Comp: glitch bands on HUD inserts. |

## 2D compositing

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| HUD | Tactical HUD and mission clock | new |  |  | 1–2, 8–9, 27, 30, 43, 49, 61, 64 | 2D comp, built by the storyboard session: it generates the title and end cards and plot inserts from the same geometry as the maps (the SVG code in build_storyboard.py). The user approves a style frame in step 1; the sequences come in step 3, and the edit composites them. |
| SUB | Comm subtitles | new |  |  | 3–6, 8–17, 20–21, 23–32, 34–37, 39, 42–47, 49–52, 54–58, 60–63 | 2D comp, added in the edit; short dim speaker tags. |

## Render budget and the gate

| Class | Kind | Cost | Shots | Frames | Time |
|---|---|---|---|---|---|
| A | Endeavor close-up | ~45 s/frame | 3, 5, 14, 16, 18–19, 32, 34, 37, 39–40, 51 | 1,008 | 12.6 h |
| A2 | Endeavor close-up with heavy FX | ~90 s/frame | 20, 29, 35–36, 41 | 456 | 11.4 h |
| V | Close-up with a hero volume (the water dump) | ~250 s/frame | 60 | 96 | 6.7 h |
| B | One hero ship or rock, full view | ~75 s/frame | 6–7, 11, 15, 17, 21, 24–25, 38, 53, 56–57 | 912 | 19.0 h |
| C | Several ships or heavy FX (FX in own layers) | ~200 s/frame | 10, 26, 31, 45–48, 50, 54–55, 59 | 936 | 52.0 h |
| S | Small subject on black with its FX (up to ~350 px) | ~30 s/frame | 23, 28 | 192 | 1.6 h |
| P | Locked camera: a plate or two rendered once, plus one moving layer | ~30 s/frame | 58, 63 | 240 | 2.0 h |
| D | Wide, distant, small subject on black, or plate | ~15 s/frame | 2, 4, 12–13, 22, 33, 42, 44, 52, 61–62 | 1,320 | 5.5 h |
| E | 2D comp / HUD | ~2 s/frame | 1, 8–9, 27, 30, 43, 49, 64 | 1,992 | 1.1 h |
| | **Total** | | 64 shots | 7,152 | **111.9 h** |
| | With 30% for re-renders | | | | **145.4 h** |

These costs are estimates, not measurements. Step 1 runs the benchmarks in the worksheet with stand-ins and first-version effects (PROXY), so nothing waits on new assets; record s/frame and VRAM for each. It also renders the C stand-in twice more, once with half-resolution FX layers and once with 16 spp swarm layers, to size levers 1 and 2. Gate before the full pass: fill in the worksheet (the arithmetic is in ASSET_REQUESTS.md). If the total with the re-render allowance is over the gate, apply the levers agreed in advance, in order, until it isn't: 1) half-resolution FX layers (the volumes already render at half resolution); 2) swarm layers at 16 spp with earlier LOD switches; 3) seconds trimmed where they cost most: 60 (~1.7 h raw a second), then class C holds such as 10, 46 and 54 (~1.3 h a second each), since trimming cards and plots saves nothing (~0.01 h a second); 4) if it is still over, the storyboard session and the user choose between a smaller re-render allowance (MARGIN; one full pass still fits the week) and shorter holds. OPEN_QUESTIONS Q17 asks which the user prefers. The ceiling is a week (168 h) per full pass.

The gate: 145.4 h with the allowance (estimated), against 160 h, so 14.6 h to spare. Break-even for one class on its own, the others as they stand: C 243 s/frame (estimate 200), B 119 s/frame (estimate 75), A 85 s/frame (estimate 45), A2 178 s/frame (estimate 90), V 670 s/frame (estimate 250), D 46 s/frame (estimate 15).

### The benchmark worksheet

Each benchmark stands for the shots listed. Fill in the measured column; each row's hours are frames × s/frame ÷ 3,600. Add the rows, multiply by 1.3 for re-renders, and compare with the gate (160 h). Then send the measured numbers back to the storyboard session, which enters them in `MEASURED` and rebuilds the board with them.

| Entry | Benchmark | Stands for (shots) | Frames | Estimate, s/frame | Measured, s/frame | Hours at the estimate |
|---|---|---|---|---|---|---|
| `A` | 3: the Endeavor close up, sunlit | 3, 5, 14, 16, 18–19 | 504 | 45 |  | 6.3 h |
| `A@C` | 32 and 39: the Endeavor in the dark lee, lit by its fins | 32, 34, 37, 39–40, 51 | 504 | 45 |  | 6.3 h |
| `A2@C` | 41: one M-1C shot in the dark lee | 35–36, 41 | 240 | 90 |  | 6.0 h |
| `B` | stand-in: one linked Endeavor in full view, sunlit, its drive lit | 6–7, 11, 15, 17, 21, 24–25, 38 | 648 | 75 |  | 13.5 h |
| `C` | stand-in: two or three linked Endeavors, 600 missiles through the swarm system, an FX-PD layer at 16–32 spp | 10, 26, 31, 46–47, 59 | 552 | 200 |  | 30.7 h |
| `B@E` | the B stand-in relit for Maren's shadow: Skerry's moonlight as the key, the running lights and ports, the faint red rim | 53, 56–57 | 264 | 75 |  | 5.5 h |
| `C@E` | the C stand-in relit for Maren's shadow: Skerry's moonlight and the faint red rim, with the swarm and FX-PD as the main light | 48, 50, 54–55 | 312 | 200 |  | 17.3 h |
| `Countermeasures` | 20: the Endeavor close up in the medium-scale smoke cache, with chaff, flares and tracers | 20, 29 | 216 | 90 |  | 5.4 h |
| `Site One` | 45: the fleet-scale smoke | 45 | 72 | 200 |  | 4.0 h |
| `V` | 60: the water dump | 60 | 96 | 250 |  | 6.7 h |
| — | not benchmarked: their class estimates stand | 1–2, 4, 8–9, 12–13, 22–23, 27–28, 30, 33, 42–44, 49, 52, 58, 61–64 | 3,744 | — | — | 10.2 h |

## Production plan

- **Sets:** 9 set-ups cover the film: the Endeavor (2–3, 5, 14, 16, 18–20, 29, 32, 34–35, 37, 39–41, 51, 60, 63); the Astrid (7, 24, 50, 57); the destroyers (6, 22–23, 44–45); the Breakers (15, 17, 21, 25–26, 28); the pack and Anchor (10, 31, 33, 36, 38, 42, 46–47); missile close-ups (11, 53); Breakwater over Maren (48, 52, 54–56, 58–59, 61–62); long-lens plates (4, 12–13); 2D (1, 8–9, 27, 30, 43, 49, 64).
- **Batches:** Render in batches by World preset: arrival and coast (sunlit crescent, Maren 1.6°): 2–7, 10–14; the Breakers (backlit haze): 15–26, 28–29; Anchor's dark lee: 31–42; the final approach (Maren growing, night side): 44–47; Maren's shadow (keyed by Skerry's dim, cool moonlight, with the red ring of Maren's air as a faint rim, the night side's city lights, and the scene's own lights): 48, 50–57, 60; after Breakwater's sunrise (a low sun just past Maren's limb, the night side below): 58–59, 61–63.
- **Order:** 1) Step 1: the user's pending picks (Q15); the HUD style frame; the Endeavor rebuild and its new rig items; the World presets; blocking proxies and first-version effects (PROXY) and a timing animatic; the method benchmarks and the gate (see the render note); the swarm system, built on the existing missile with LOD slots for the variants. 2) One batched concept round, missile variants first, since it waits on the user. 3) Meanwhile the assets with art: the FX library, the Breakers then Anchor, the frigate with its hedgehog module, the destroyer, the Astrid; and the 2D sequences (the title and end cards and plot inserts), generated by the storyboard session. 4) The concept-gated assets: the missile variants into the swarm's slots, the corvette and drones, the emplacements, Breakwater, the gun module. Every breakable hull (DD, CV, CF, BW) is modelled in sections at its bulkhead frames. 5) The long-lens plates last; 50 renders last of all, since it waits on three gates (the Astrid, the missile variants, the PDC pick).
- **Methods:** The foreground pods of 47 in their own layer, defocused in comp; 53's rack focus likewise, the nose and the far field as separate layers. Every rock and plume instanced, with a rock tile in the class C benchmark (31). In Maren's shadow (World E) Skerry is one dim, distant key light and the red ring a faint rim; the scene's own emitters do the rest. In the dark lee, area lights on each fin driven by `heat`, with emission sampling off on the fin meshes (EN-FIN). 58 and 63 are locked off: a plate rendered once plus one moving layer (the turrets and vents; the ship). 58 renders one plate with Cycles light groups (the Sun; Skerry and the rim; the emitters) and keys the Sun group's colour and strength in comp through the sunrise, which is exact because light adds; its moving layer renders with the hull as holdout and shadow catcher, so the turrets' shadows move. Site 1's lights in 62 are a comp element over a plate.
- **Rendering:** One job per shot to multilayer EXR sequences (DWAA), Placeholders on and Overwrite off so a crashed render resumes; the grade (`LREF_Compositor`) as a separate pass; emissive FX in their own view layers at 16–32 spp with 1–3 proxy lights in the beauty layer; Persistent Data; adaptive sampling with denoising; vector blur in comp; plan ~150 GB of disk.
