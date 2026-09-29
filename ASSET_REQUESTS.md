# Asset requests

Everything *Operation Tidebreak* (revision 2 · after review round 1) needs from the modelling session, with the shots that need each item. Generated from `storyboard/tidebreak_data.py`.

- **Status:** *built* exists; *extend* exists but needs additions; *new* must be made.
- **Concept first:** per the user's rule, new weapon and ship designs go through concept sheets and the user picks before modelling. Items without reference art are flagged too.
- **Detail level:** the user asked for everything hero-detailed. The closest view says how much of that detail the camera can ever see; proxies for the smallest items are open question Q13.
- **Set-ups:** 8 set-ups cover the film: the Endeavor (1–2, 4, 12, 14, 16–17, 26, 29–31, 33, 35, 44, 52, 54); the Astrid (6, 21, 43, 49); the destroyers (5, 19–20, 38–39); the Breakers (13, 15, 18, 22–23, 25); the pack and Anchor (9, 28, 32, 34, 36, 41–42); Breakwater over Maren (40, 45–48, 50–51, 53); long-lens plates (3, 10–11); 2D (7–8, 24, 27, 37).

## LREF ships and craft

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| AST | L.R.E.F.S. Astrid (Hanuman heavy cruiser) | new |  | shot 49: EWS 200 mm, end-on at ~2 km, fills the frame | 3, 6, 10, 12, 21, 43, 49 | Hero, ~1,650 m. Build from lref_kit: M-1Cs, arrays, CIWS, fins, rings and shield are instances, so the new hero work is the hull, the AVPSA dish and the spinal. Concept sheet for the spinal muzzle and its FX look. Controls: `avpsa_az`, `avpsa_el`, `fins_deploy` (8), `spinal_charge`, `spinal_shot`, plus the Endeavor's `ciws_phase` and `ciws_fire` on its instanced CIWS. Art exists. |
| GI | Garibaldi-Ivanova frigate hull | new |  | shot 9: hull camera on the Infinity, fills the frame | 3, 9–10, 28, 41–42 | Hero, ~420 m. One hull for all five frigates; module bay; warp rings; shield; spinning hab section. Art exists. |
| GI-MAV | Hedgehog (MAV) module | new |  |  | 3, 9, 41–42 | ~360 pods; `pod_ripple` launch control. Art exists. |
| GI-GUN | Gun module (4 large kinetic batteries) | new | yes |  | 28 | Four scaled M-1C twins; the concept sheet only settles the layout. |
| GI-PD | PD module | new | yes | shot 4: behind the parked shields, ~40 px | 4 | Build after the PDC pick. Seen only far off in shot 4: a silhouette is enough if the user agrees (Q13). |
| DD | ECW destroyer | new |  | shot 5: MS 40 mm at ~600 m, fills the frame | 3, 5, 10, 19–20, 38–39 | Hero, ~200 m. Dish placement follows the art (forward, behind the shield) unless the user decides otherwise (Q14). Controls: `dish_deploy`, `booms_deploy`, `drone_bay`. Art exists. |
| DD-BRK | Destroyer break-up (Canterbury) | new |  |  | 20 | Section-break rig: holed bow to stern, venting, the hull parting in two. |
| CV | Corvette class | new | yes | shot 25: 300 mm at ~20 km, ~150 px | 3, 10, 13, 23, 25, 28 | No reference art: concept sheet first. Brief: 50–150 m; two warp rings at the ends; a jettisonable forward shield; radiators and booms that stow for warp; no spin section; anti-drone weapons 'far more powerful and varied' than a big ship's PD. |
| CV-BRK | Corvette destruction (Normandy) | new |  |  | 25 | Section-break rig variant. |
| TND | Nauvoo, fleet tender | new | yes | shot 4: behind the parked shields, ~40 px | 3–4 | No reference art: concept sheet first. Brief: two warp rings, forward shield, stowable radiators; cradles for spare shields; a rig for swapping frigate modules. Seen only far off: a silhouette if the user agrees (Q13). |
| SHD | Parked impact shields | extend |  |  | 4 | Scaled instances of the gold shield for the park cluster. |
| DRN-L | LREF drone | new | yes | shot 5: MS 40 mm, ~40 px | 5, 13, 23, 28, 38 | One design (picket/PD/EW variants by payload only), concept first. |
| MSL | Missile asset (26 m, plume, thrust) | built |  |  | — | Base for every variant. |
| MSL-V | Missile variants | new | yes |  | 9, 15, 40–43, 46 | Concept sheet first (five new weapon designs): the Casaba killer (hardened ablative nose, spin), the small multi-pack missile with MIRV bus, decoy, EW missile, Compact belt-pod missile. Three LODs each for the swarm system. |

## Endeavor and M-1C

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| EN | L.R.E.F.S. Endeavor (rigged) | extend |  |  | 1–2, 4, 10, 12–14, 16–17, 26, 28–33, 35, 44, 52, 54 | Hero ship. Rebuild after the M-1C wake-style and PDC picks that are still pending in the modelling session (Q15), then link it into shot files with a library override on the rig empty. |
| EN-FIN | Endeavor: per-fin control and damage | extend |  |  | 29–31, 54 | Per-fin deploy properties `fin_port`, `fin_starboard`, `fin_dorsal`, `fin_ventral` (the ship-wide `radiator_deploy` stays as a master). Port fin states via `fin_port_state`: intact, pre-fractured (shot 31), stump (shots 32–54). |
| EN-PD | Endeavor: defence, countermeasure and emergency controls | extend |  |  | 16–17, 52 | `ciws_phase` (a keyed angle, with a spin-blur swap above ~600 rpm, because `ciws_rpm` changes jump and strobe), `ciws_fire` (muzzle empties), `cm_chaff`, `cm_flare`, `cm_smoke`, `ew_active`, `water_dump` (valve and plume emitter). |
| EN-MAST | Endeavor: sensor-mast shutters | extend |  |  | 14 | `mast_shutter`: armoured shutters close over the mast windows. |
| EN-DMG | Endeavor: hull damage | extend |  |  | 32 | `dmg_belt`: spall and scorching on the port belt from shot 32 on; it must read in shot 52, which runs along the port flank. |
| M1C | M-1C twin railcannon | extend |  |  | 35 | Fleet gun. Wake style still to be picked (split, ripple, bulk, extend, combined: Q15); per-gun `charge_a/b`, `shot_a/b`, `fins_a/b`, `heat_a/b` for shot 35 (only the gun that fired vents). |

## The Maren Compact

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| BW | Breakwater, Compact monitor | new | yes | shot 48: drone camera near the monitor, fills the frame | 40, 45–48, 50–51 | Concept sheet first. ~1,800 m warpless monitor: no rings or shield, ~2 m belt, 6 twin heavy turrets, 24 PD lasers, 40 CIWS, 64 cells, armoured louvred radiators. Controls: `turret_traverse`, `turret_elevation`, `cells_open`, `drive_glow`, `vent`. |
| BW-BRK | Breakwater break-up | new |  |  | 47–48, 50–51, 53 | Section-break rig: spear wounds on the drive bells, the spinal entry amidships, secondaries, the back breaking. |
| CF | Compact frigate | new | yes | shot 34: 1,000 mm at 40 km, ~470 px | 32, 34 | Concept sheet first. ~350 m; coilgun and missiles; section-break variant. Seen at ~470 px in shot 34 (1,000 mm at 40 km), so it needs real detail. |
| DRN-C | Compact drone and its hide | new | yes | shot 23: 28 mm, nearest drones, ~30 px | 23, 25 | One design (plasma-bomb payload) plus the cold hide on a rock; concept first. |
| EMP-POD | Cold missile pod on a rock | new | yes | shot 15: drone near the rock, ~300 px | 15 | Concept first. Controls: `heave`, `petals`. |
| EMP-RG | Breakers railgun platform | new | yes | shot 18: drone over the platform, fills the frame | 18, 22, 30, 36 | Concept first. Buried twin railgun. Controls: `unmask`, `shot`. |
| RING | Inner-ring station | new | yes | shot 40: far along the orbit, points of light | 40 | Only ever a point of light at ~21,800 km spacing: lights only, if the user agrees (Q13). |
| SKR | Skerry | new |  | shot 11: 1,200 mm at ~262,000 km, a quarter-frame disc | 7, 11 | One still plate of an airless moon; the battery, tracks and depot are flash and light positions only. |

## Environment

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| WORLD | World presets and sun | extend |  |  | 3, 54 | World presets for arrival, the Breakers, Anchor and Breakwater, with planet-shine scaled to each (Maren is 1.6° across from the exit, ~17.5° from Breakwater's orbit); a Sun object that drives the World (today `TO_SUN` needs a rebuild); Skerry as a second body at the right angular size; each set-up's camera kept near the world origin. |
| MAREN | Maren: planet re-dress | extend |  |  | 3, 40, 45, 48, 53–54 | New continents and weather, night-side cities, the Site 1 plateau as a light cluster that can go out (shot 53). |
| BRK | The Breakers environment | new |  |  | 3, 13, 15, 18, 22–23, 28, 36 | The dust haze as the Mist pass plus a sparse glitter layer; a generic rock kit; large rocks at realistic spacing. |
| ANCHOR | Anchor: hero rock | new |  | shot 28: low over the surface, fills the frame | 28, 32, 41–42 | ~18 km rubble pile: a Geometry Nodes boulder scatter from the BRK kit, with hero surface tiles only where the camera goes close (shots 28, 41). |

## Effects

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| FX-WARP | Warp-exit flash | new |  |  | 1, 3 | Bubble collapse bloom (comp plus a light). |
| FX-SWARM | Swarm system | new |  |  | 9, 23, 25, 38, 40–43, 46 | One Geometry Nodes system for missiles, drones and canister pellets: per-instance launch time, three LODs (hero mesh only for the nearest ~10), each plume a single emissive mesh with emission sampling off, real lights only on the ~5 nearest plumes or flashes, pellets as emissive points whose brightness follows the lamp angle, rendered in its own view layer. |
| FX-FAR | Distant drive plumes | new |  |  | 3, 10, 43 | Cheap far plumes for long-lens fleet shots. |
| FX-NUKE | Nuclear flashes | new |  |  | 11, 28 | Point flashes: Skerry's surface, the mine at Anchor. |
| FX-PD | Point-defence fire | new |  |  | 17, 43, 45–46 | CIWS tracers and kill clouds, chaff, flares, intercept flashes, in their own view layer at low samples. |
| FX-SMOKE | Smoke screen | new |  |  | 17, 26, 39 | One low-resolution cached VDB in its own layer, reused in shots 17, 26 and 39. |
| FX-SLUG | Slug streaks and impacts | new |  |  | 18, 22, 31–32, 36 | Glints, impact flash, spall cone, shock ring. |
| FX-BREAK | Section-break rig and debris kit | new |  |  | 20, 25, 34, 51 | No cell fracture (the plated kit hulls defeat it): split each hull along its bulkhead frames into 3–8 sections, cap the torn edges with kit parts, drive the pieces apart with a procedural `break` 0→1, scatter an instanced debris kit. |
| FX-VENT | Venting in vacuum | new |  |  | 20, 31, 34, 47–48, 52 | Short-lived sprays of glinting ice (what gas and coolant do in vacuum), plus the Endeavor's water-dump plume; one small cached VDB reused. |
| FX-FIN | Fin shatter | new |  |  | 31 | The pre-fractured port fin's shards and glow. |
| FX-LANCE | Plasma lance | new |  |  | 34 | A field-held violet-white jet from the nose channels to the target inside a faint field sheath; it fizzles back when `lance_power` cuts. |
| FX-CASABA | Casaba jets | new |  |  | 47 | Narrow nuclear spears from 2 km standoff. |
| FX-SPINAL | Spinal fire and impact | new |  |  | 21, 49, 51 | Muzzle bloom down the Astrid's kilometre barrel; impact flash and spall. |
| FX-DAZZLE | Dazzle and whiteout | new |  |  | 7, 14, 39 | Comp: bloom on optics, POV whiteout. |
| FX-EW | EW overlay | new |  |  | 24, 44 | Comp: glitch bands on HUD inserts. |

## 2D compositing

| ID | Asset | Status | Concept first | Closest view | Shots | Notes |
|---|---|---|---|---|---|---|
| HUD | Tactical HUD and mission clock | new |  |  | 1, 7–8, 24, 27, 37, 53 | 2D comp. The user approves a style frame first; the plots can reuse the SVG map code in build_storyboard.py. |
| SUB | Comm subtitles | new |  |  | 3–5, 7–15, 17, 19–33, 35, 37–44, 46–50, 52–54 | 2D comp, added in the edit; short dim speaker tags. |

Not used by any shot yet: MSL.
