# Asset requests

Everything *Operation Tidebreak* (revision 1 · phase 2 draft for review) needs from the modelling session, with the shots that need each item. Generated from `storyboard/tidebreak_data.py`.

- **Status:** *built* exists; *extend* exists but needs additions; *new* must be made.
- **Concept first:** per the user's rule, new weapon and ship designs go through concept sheets and the user picks before modelling. Items without reference art are flagged too.
- **Detail level:** the user asked for everything hero-detailed.

## LREF ships and craft

| ID | Asset | Status | Concept first | Shots | Notes |
|---|---|---|---|---|---|
| AST | L.R.E.F.S. Astrid (Hanuman heavy cruiser) | new |  | 3, 6, 17, 35 | Hero. Spinal cannon along the full hull with muzzle; AVPSA ~100 m articulated dish; 8 stacked fins (retract for warp); ≥25 laser arrays and ≥19 M-1C turrets; dense CIWS and PD lasers; twin hab rings; warp rings; shield launch. Art exists (Sir_Lazz). |
| GI | Garibaldi-Ivanova frigate hull | new |  | 3, 4, 7, 26, 29 | Hero. ~420 m; module bay; warp rings fore and aft; impact shield; spinning hab section; reactor, engines, radiators. Art exists. |
| GI-MAV | Hedgehog (MAV) module | new |  | 3, 7, 29 | ~360 pods (single capital-ship-killer pods fore, multi-silo packs aft); pod-door and ripple-launch rig. Art exists. |
| GI-GUN | Gun module (4 large kinetic batteries) | new | yes | 26 | Concept sheet first (new weapon design). Probably an up-scaled M-1C family. |
| GI-PD | PD module (lasers, CIWS, kill-cloud dispensers) | new | yes | 4 | Concept sheet first. |
| DD | ECW destroyer | new |  | 3, 15, 16, 30 | Hero. ~200 m; parabolic antenna over the aft third; retractable sensor booms; drone/satellite bays; CIWS; stern radiators. Art exists. |
| DD-BRK | Destroyer break-up (Canterbury) | new |  | 16 | Fractured variant: holed stern to bow, reactor scram flash, venting, the hull parting in two. |
| CV | Corvette class | new | yes | 3, 11, 18, 20 | No reference art: concept sheet first. 50–150 m, fast, anti-drone weapons. |
| CV-BRK | Corvette destruction (Normandy) | new |  | 20 | Plasma-bomb hit and break-up variant. |
| TND | Nauvoo, fleet tender | new | yes | 3, 4 | No reference art: concept sheet first. Cargo frames, shield cradles, a crane arm; can stay a distant shape. |
| SHD | Parked impact shields | extend |  | 4 | The Endeavor's gold shield exists; the other ships' shields come with their assets. Needs a parked cluster set-up. |
| DRN-L | LREF drones | new | yes | 11, 18, 30 | Concept sheet first: picket, decoy, PD and EW drones. |
| MSL | Missile asset (26 m, plume, thrust) | built |  | — | Base for every missile variant. |
| MSL-V | Missile variants | new |  | 7, 13, 29 | Hedgehog capital-ship killer (hardened ablative nose, spin), small multi-pack missile, decoy, EW missile, Compact belt-pod missile. |

## Endeavor and M-1C

| ID | Asset | Status | Concept first | Shots | Notes |
|---|---|---|---|---|---|
| EN | L.R.E.F.S. Endeavor (rigged) | built |  | 1, 2, 4, 8, 10, 11, 12, 14, 21, 22, 23, 24, 25, 27, 32, 36, 37 | Hero ship. All rig properties per the README. |
| EN-FIN | Endeavor: per-fin control and damage | extend |  | 24, 36, 37 | Per-fin deploy properties (fin_port, fin_starboard, fin_dorsal, fin_ventral) instead of one radiator_deploy; a shattered port fin, a cut-loose fin drifting away, and the stump state for later shots. |
| EN-MAST | Endeavor: sensor-mast shutters | extend |  | 12 | A `mast_shutter` property: armoured shutters close over the mast windows when a laser paints them. |
| EN-DMG | Endeavor: hull scars | extend |  | 26, 36 | Scorching and spall on the port belt from the Compact frigate's slug (shot 26) carried into shots 27–37. |
| M1C | M-1C twin railcannon | built |  | 25 | On the Endeavor; reused scaled on other ships. |

## The Maren Compact

| ID | Asset | Status | Concept first | Shots | Notes |
|---|---|---|---|---|---|
| BW | Breakwater, Compact monitor | new | yes | 31, 33, 34, 35 | Concept sheet first. ~1,800 m warpless monitor: no warp rings or shield, ~2 m armour belt, 6 twin heavy turrets, 24 PD lasers, 40 CIWS, 64 missile cells, armoured louvred radiators. |
| BW-BRK | Breakwater break-up | new |  | 34, 35 | Casaba breach on the drive section, spinal entry wound amidships, secondaries, the back breaking. |
| CF | Compact frigate | new | yes | 26, 27 | Concept sheet first. ~350 m, coilgun and missiles; break-up variant. |
| DRN-C | Compact drones | new | yes | 18, 20 | Concept sheet first: plasma-bomb drone and kill-cloud drone; a cold 'hide' on a rock. |
| EMP-POD | Cold missile pod on a rock | new | yes | 13 | Concept sheet first. Buried in regolith; petal doors; cold launch. |
| EMP-RG | Breakers railgun platform | new | yes | 15 | Concept sheet first. Buried twin railgun that unmasks, fires a 10-slug salvo, and dies. |
| RING | Inner-ring emplacement | new | yes | 31 | Concept sheet first. Orbital railgun/PD station. |
| SKR | Skerry (moon) and complex | new |  | 3, 5, 9 | Airless moon ~900 km radius; three mass-driver tracks (~40 km), laser battery, drone depot. Seen from far away: detail can stay modest. |

## Environment

| ID | Asset | Status | Concept first | Shots | Notes |
|---|---|---|---|---|---|
| MAREN | Maren: planet re-dress | extend |  | 3, 31, 37 | Re-dress the World-shader planet: new continents and weather, night-side cities, the Site 1 plateau, and the limb for shots 31–37. |
| BRK | The Breakers: debris-torus environment | new |  | 3, 11, 13, 17, 18 | Faint dust haze and glitter (volumetric or particles), a generic rock set, sparse large rocks at realistic spacing. |
| LEE | The Lee: hero rock | new |  | 22, 26, 29 | ~18 km rubble-pile asteroid with boulders and a few small moonlets; must hold up at close range. |

## Effects

| ID | Asset | Status | Concept first | Shots | Notes |
|---|---|---|---|---|---|
| FX-WARP | Warp-exit flash | new |  | 1, 3 | Bubble collapse bloom (comp plus light). |
| FX-SWARM | Missile swarm | new |  | 7, 29, 33 | Instanced missiles with plumes; ripple launch; staggered burns. |
| FX-NUKE | Distant nuclear flashes | new |  | 9 | Point flashes on Skerry's surface, seen from far away. |
| FX-PD | Point-defence fire | new |  | 14, 21, 33 | CIWS tracer streams and kill clouds, chaff, flares, smoke screens, intercept flashes. |
| FX-SLUG | Slug streaks and impacts | new |  | 15, 24 | Glints, impact flash, spall cone, shock ring. |
| FX-BREAK | Ship break-up | new |  | 16, 20, 27, 35, 36 | Cell fracture, venting, debris (shared by DD-BRK, CV-BRK, CF, BW-BRK). |
| FX-DRN | Drone swarm | new |  | 18, 20 | Instanced drones, plasma-bomb flashes. |
| FX-FIN | Fin shatter and coolant vapour | new |  | 24 | Glowing shards, coolant flashing to vapour. |
| FX-LANCE | Plasma lance bolt | new |  | 27 | Compact toroid: violet-white ring, near-instant. |
| FX-CAN | Canister cloud | new |  | 30 | Skerry's canister round bursting into a pellet cloud, seen as glints in drone lights. |
| FX-CASABA | Casaba jets | new |  | 34 | Narrow nuclear plasma spears from 2–4 km standoff. |
| FX-SPINAL | Spinal cannon fire and impact | new |  | 17, 35 | Muzzle bloom down the Astrid's kilometre barrel; impact flash and spall. |
| FX-DAZZLE | Dazzle and sensor whiteout | new |  | 12 | Comp: bloom on optics, POV whiteout. |
| FX-EW | EW overlay | new |  | 19, 32 | Comp: glitch bands on HUD inserts. |

## 2D compositing

| ID | Asset | Status | Concept first | Shots | Notes |
|---|---|---|---|---|---|
| HUD | Tactical HUD and mission clock | new |  | 5, 6, 19, 28 | 2D comp: plots, tracks, mission clock, heat readouts; one design reused. |
| SUB | Comm subtitles | new |  | 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37 | 2D comp: speaker tag + line; voice acting may replace them later. |

Not used by any shot yet: MSL.
