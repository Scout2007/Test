# Asset requests

Everything *Operation Tidebreak* (revision 3 · after review round 2) needs from the modelling session, with the shots that need each item. Generated from `storyboard/tidebreak_data.py`.

- **Status:** *built* exists; *extend* exists but needs additions; *new* must be made.
- **Concept first:** per the user's rule, new weapon and ship designs go through concept sheets and the user picks before modelling. Items without reference art are flagged too.
- **Detail level:** the user asked for everything hero-detailed. The closest view says how much of that detail the camera can ever see; proxies for the smallest items are open question Q13.
- **Set-ups:** 9 set-ups cover the film: the Endeavor (1–2, 4, 13, 15, 17–19, 28, 31, 33–34, 36, 38–40, 50, 59, 62); the Astrid (6, 23, 49, 56); the destroyers (5, 21–22, 43, 45); the Breakers (14, 16, 20, 24–25, 27); the pack and Anchor (9, 30, 32, 35, 37, 41, 46, 48); missile close-ups (10, 52); Breakwater over Maren (47, 51, 53–55, 57–58, 60–61); long-lens plates (3, 11–12); 2D (7–8, 26, 29, 42, 44).

## LREF ships and craft

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| AST | L.R.E.F.S. Astrid (Hanuman heavy cruiser) | new |  | shot 6: MS 50 mm along the dorsal hull (the muzzle: 56), fills the frame | 3, 6, 11, 13, 23, 49, 56 | Hero, ~1,650 m. Build from lref_kit: M-1Cs, arrays, CIWS, fins, rings and shield are instances, so the new hero work is the hull, the AVPSA dish and the spinal. Concept sheet for the spinal muzzle and its FX look. Controls: `avpsa_az`, `avpsa_el`, `fins_deploy` (8), `spinal_charge`, `spinal_shot`, `engine_throttle`, `rcs_bow`/`rcs_stern`, `laser_power`/`laser_traverse`, plus the Endeavor's `ciws_phase` and `ciws_fire` on its instanced CIWS. Art exists. |
| GI | Garibaldi-Ivanova frigate hull | new |  | shot 9: hull camera on the Infinity, fills the frame | 3, 9, 11, 30, 46, 48 | Hero, ~420 m. One hull for all five frigates; module bay; warp rings; shield; spinning hab section. Art exists. |
| GI-MAV | Hedgehog (MAV) module | new |  | shot 9: hull camera beside the pods, fills the frame | 3, 9, 46, 48 | ~360 pods; `pod_ripple` launch control, driven from the swarm system's per-pod launch-time attribute so doors and launches can't drift apart. Art exists. |
| GI-GUN | Gun module (4 large kinetic batteries) | new | yes | shot 30: far off, shelling rocks, a few px | 30 | Four scaled M-1C twins; the concept sheet only settles the layout. Seen only far off in 30: a silhouette is enough if the user agrees (Q13). |
| GI-PD | PD module | new | yes | shot 4: behind the parked shields, ~40 px | 4 | Build after the PDC pick. Seen only far off in shot 4: a silhouette is enough if the user agrees (Q13). |
| DD | ECW destroyer | new |  | shot 5: MS 40 mm at ~600 m, fills the frame | 3, 5, 11, 21–22, 43, 45 | Hero, ~200 m. The dish sits fixed, forward, behind the shield, as in the art (Q14); it is unmasked when the shield leaves. Controls: `booms_deploy`, `drone_bay`, `rcs`, `dmg_boom` (the Extenuating's scorched boom from 45). Model it in sections at its bulkhead frames for the section-break rig. Art exists. |
| DD-BRK | Destroyer break-up (Canterbury) | new |  |  | 22 | Section-break rig: holed bow to stern, venting, the hull parting in two. |
| CV | Corvette class | new | yes | shot 27: 800 mm at ~20 km, ~200 px | 3, 11, 14, 25, 27, 30 | No reference art: concept sheet first. Brief: 50–150 m; two warp rings at the ends; a jettisonable forward shield; radiators and booms that stow for warp; no spin section; anti-drone weapons 'far more powerful and varied' than a big ship's PD. Model it in sections at its bulkhead frames. |
| CV-BRK | Corvette destruction (Normandy) | new |  |  | 27 | Section-break rig variant. |
| TND | Nauvoo, fleet tender | new | yes | shot 4: behind the parked shields, ~40 px | 3–4 | No reference art: concept sheet first. Brief: two warp rings, forward shield, stowable radiators; cradles for spare shields; a rig for swapping frigate modules. Seen only far off: a silhouette if the user agrees (Q13). |
| SHD | Parked impact shields | extend |  |  | 4 | Scaled instances of the gold shield for the park cluster. |
| DRN-L | LREF drone | new | yes | shot 5: MS 40 mm, ~40 px | 5, 14, 25, 30, 43 | One design (picket/PD/EW variants by payload only), concept first. |
| MSL | Missile asset (26 m, plume, thrust) | built |  | shot 10: CU 85 mm alongside one missile, fills the frame | 10 | Base for every variant; the hero LOD flies alongside the camera in 10. |
| MSL-V | Missile variants | new | yes | shot 52: ECU 100 mm on a Casaba killer's nose, fills the frame | 9–10, 16, 46–49, 52–54 | Concept sheet first (five new weapon designs): the Casaba killer (hardened ablative nose, a seeker window behind a shutter, spin; seen in extreme close-up in 52), the small multi-pack missile with MIRV bus, decoy, EW missile, Compact belt-pod missile. Three LODs each, dropped into the swarm system's slots. |

## Endeavor and M-1C

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| EN | L.R.E.F.S. Endeavor (rigged) | extend |  |  | 1–2, 4, 11, 13–15, 17–19, 28, 30–31, 33–36, 38–40, 50, 59, 62 | Hero ship. Rebuild after the M-1C wake-style and PDC picks that are still pending in the modelling session (Q15), then link it into shot files with a library override on the rig empty. Its states (STATES) are presets the shot files load. |
| EN-FIN | Endeavor: per-fin control and damage | extend |  |  | 31, 33–36, 38–40, 50, 59, 62 | Per-fin deploy properties `fin_port`, `fin_starboard`, `fin_dorsal`, `fin_ventral` (the ship-wide `radiator_deploy` stays as a master). Port fin states via `fin_port_state`: intact, pre-fractured (shot 34), stump (every Endeavor shot after it). |
| EN-PD | Endeavor: defence, countermeasure and emergency controls | extend |  |  | 17, 19, 28, 59 | `ciws_phase` (a keyed angle, with a spin-blur swap above ~600 rpm, because `ciws_rpm` changes jump and strobe), `ciws_fire` (muzzle empties), `cm_chaff`, `cm_flare`, `cm_smoke`, `ew_active`, `water_dump` (valve and emitter for FX-DUMP). |
| EN-MAST | Endeavor: sensor-mast shutters | extend |  |  | 15 | `mast_shutter`: armoured shutters close over the mast windows. |
| EN-DMG | Endeavor: hull damage | extend |  |  | 35–36, 38–40, 50, 59, 62 | `dmg_belt`: spall and scorching on the port belt from shot 35 on; it must read in shot 59, which runs along the port flank. |
| M1C | M-1C twin railcannon | extend |  | shot 40: ECU 85 mm on the muzzles, fills the frame | 38–40 | Fleet gun. Wake style still to be picked (split, ripple, bulk, extend, combined: Q15). Per-gun `charge_a/b`, `shot_a/b`, `fins_a/b`, `heat_a/b` for 39 and 40, where only the gun that fired vents. |

## The Maren Compact

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| BW | Breakwater, Compact monitor | new | yes | shot 55: drone camera near the monitor, fills the frame | 47, 51–55, 57–58, 60 | Concept sheet first. ~1,800 m warpless monitor: no rings or shield, ~2 m belt, 6 twin heavy turrets, 24 PD lasers, 40 CIWS, 64 cells, armoured louvred radiators. Controls: `turret_traverse`, `turret_elevation`, `cells_open`, `drive_glow`, `vent`, `ciws_phase`/`ciws_fire` with muzzle empties, PD `laser_power`. Model it in sections at its bulkhead frames. |
| BW-BRK | Breakwater break-up | new |  |  | 54–55, 57–58, 60 | Section-break rig: spear wounds on the drive bells, the spinal entry amidships, secondaries, the back breaking. |
| CF | Compact frigate | new | yes | shot 37: 1,000 mm at 45 km, ~420 px | 35, 37 | Concept sheet first. ~350 m; coilgun and missiles; simple instanced escape pods; modelled in sections for its break-up. Seen at ~420 px in shot 37 (1,000 mm at 45 km), so it needs real detail. |
| DRN-C | Compact drone and its hide | new | yes | shot 25: 28 mm, nearest drones ~1 km off, ~30 px | 25, 27 | One design (plasma-bomb payload) plus the cold hide on a rock; concept first. |
| EMP-POD | Cold missile pod on a rock | new | yes | shot 16: drone near the rock, ~300 px | 16 | Concept first. Controls: `heave`, `petals`. |
| EMP-RG | Breakers railgun platform | new | yes | shot 20: drone over the platform, fills the frame | 20, 24, 32, 41 | Concept first. Buried twin railgun. Controls: `unmask`, `shot`. |
| RING | Inner-ring station | new | yes | shot 47: far along the orbit, points of light | 47, 60 | Only ever a point of light at ~21,800 km spacing: lights only, if the user agrees (Q13). |
| SKR | Skerry | new |  | shot 12: 1,200 mm at ~262,000 km, a quarter-frame disc | 7, 12 | One still plate of an airless moon; the battery, tracks and depot are flash and light positions only. |

## Environment

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| WORLD | World presets and sun | extend |  |  | every 3D shot | Used by every 3D shot. One preset per environment (ENVS), with planet-shine scaled to each (Maren is 1.6° across from the exit, ~17.5° from Breakwater's orbit); a Sun object that drives the World (today `TO_SUN` needs a rebuild); Skerry as a second body at the right angular size; a sun-direction gradient on the Breakers haze in comp; each set-up's camera kept near the world origin. |
| MAREN | Maren: planet re-dress | extend |  |  | 3, 10, 47, 51, 55, 60–62 | New continents and weather, night-side cities, the Site 1 plateau as a light cluster that goes out (shot 61), about 10 px at 2,000 mm. |
| BRK | The Breakers environment | new |  |  | 3, 14, 16, 20, 24–25, 30, 32, 41 | The dust haze as the Mist pass plus a sparse glitter layer; a generic rock kit; large rocks at realistic spacing. |
| ANCHOR | Anchor: hero rock | new |  | shot 30: low over the surface, fills the frame | 30, 35, 46, 48 | ~18 km rubble pile: a Geometry Nodes boulder scatter from the BRK kit, with hero surface tiles only where the camera goes close (shots 30, 46); the moonlet with the frigate's cleft. |

## Blocking

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| PROXY | Blocking proxies | new |  |  | every 3D shot | True-scale stand-ins for every ship and rock, built in step 1 for the timing animatic and the benchmarks. |

## Effects

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| FX-WARP | Warp-exit flash | new |  |  | 1, 3 | Bubble collapse bloom (comp plus a light). |
| FX-SWARM | Swarm system | new |  |  | 9, 25, 27, 43, 46–49, 53 | One Geometry Nodes system for missiles, drones and canister pellets: per-instance launch time, three LODs (hero mesh only for the nearest ~10), each plume a single emissive mesh with emission sampling off, real lights only on the ~5 nearest plumes or flashes (faded in and out over ~6 frames so the hull lighting doesn't pop), pellets as emissive points whose brightness follows the lamp angle, rendered in its own view layer. Built first on the existing missile (MSL); the variants drop into its LOD slots later. |
| FX-FAR | Distant drive plumes | new |  |  | 3, 11 | Cheap far plumes for long-lens fleet shots. |
| FX-NUKE | Nuclear flashes | new |  |  | 12, 30 | Point flashes: Skerry's surface, the mine at Anchor. |
| FX-PD | Point-defence fire | new |  |  | 18–19, 49, 51–53 | CIWS tracers and kill clouds, chaff, flares, intercept flashes, laser lens pulses, in their own view layer at low samples. |
| FX-SMOKE | Smoke screen | new |  |  | 19, 28, 45 | A cached VDB in two resolutions (medium shot in 19 and 28, fleet scale in 45), rendered in a half-resolution layer. |
| FX-SLUG | Slug streaks and impacts | new |  |  | 20, 24, 32, 34–35, 40–41 | Glints, impact flash, spall cone, shock ring. |
| FX-BREAK | Section-break rig and debris kit | new |  |  | 22, 27, 37, 58 | No cell fracture (the plated kit hulls defeat it): each breakable hull is modelled in 3–8 sections at its bulkhead frames, the torn edges capped with kit parts, the pieces driven apart with a procedural `break` 0→1, and an instanced debris kit scattered. |
| FX-VENT | Venting in vacuum | new |  |  | 22, 34, 37, 54–55 | Short-lived sprays of glinting ice (what gas and coolant do in vacuum); one small cached VDB reused. |
| FX-DUMP | Water-dump plume | new |  |  | 59 | A Geometry Nodes ice point cloud with a thin low-resolution VDB core, in its own layer at half resolution with one volume bounce. Costed at ~250 s/frame and part of the volume benchmark. |
| FX-FIN | Fin shatter | new |  |  | 34 | The pre-fractured port fin's shards and glow. |
| FX-LANCE | Plasma lance | new |  |  | 37 | A field-held violet-white jet from the nose channels to the target inside a faint field sheath; it fizzles back when `lance_power` cuts. |
| FX-CASABA | Casaba jets | new |  |  | 54 | Narrow nuclear spears from 2 km standoff. |
| FX-SPINAL | Spinal fire and impact | new |  |  | 23, 56, 58 | Muzzle bloom down the Astrid's kilometre barrel; impact flash and spall. |
| FX-DAZZLE | Dazzle and whiteout | new |  |  | 7, 15, 45 | Comp: bloom on optics, POV whiteout. |
| FX-EW | EW overlay | new |  |  | 26, 50 | Comp: glitch bands on HUD inserts. |

## 2D compositing

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| HUD | Tactical HUD and mission clock | new |  |  | 1, 7–8, 26, 29, 42, 44, 60 | 2D comp. The user approves a style frame first; the plots can reuse the SVG map code in build_storyboard.py. |
| SUB | Comm subtitles | new |  |  | 3–5, 7–9, 11–16, 21–31, 33–36, 42–51, 53–57, 59–62 | 2D comp, added in the edit; short dim speaker tags. |
