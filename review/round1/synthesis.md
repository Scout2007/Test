# Round 1 synthesis

Round 1 read **storyboard revision 1** (37 shots, 2:45) and the signed-off doctrines, with five independent reviewers: physics, military doctrine, lore, cinematography, and production. They raised **26 major issues**, 19 minor ones and a handful of nits. **Revision 2** (54 shots, 3:34) answers every major issue. This file records each decision, what else changed while revising, and what round 2 should look at.

The reports are in this folder (`physics.md`, `doctrine.md`, `lore.md`, `cinematography.md`, `production.md`). Shot numbers below are revision 2's unless marked "rev 1".

## The verdicts

- **Physics:** the sublight skeleton holds. Act IV broke: it treated Site 1's zenith as a fixed line, left Maren behind the target, and had the Astrid unable to stop. The heat readouts and Skerry's flight time also didn't add up.
- **Doctrine:** the plan is doctrinal (Skerry first, a slow swept crossing, shelter and vent, cripple then kill). But the Act IV timing broke the LREF's own rules. The anchorage was unswept, and the defender went passive for the last two hours.
- **Lore:** broadly faithful. Two contradictions: the lance as a free-flying ring, and a "kilometre-long" Astrid.
- **Cinematography:** the right shape, but unwatchable as timed: text on screen ~80 % of the time, one tempo, lenses too short to see the kills, no clock or HUD plan, and losses nobody had met.
- **Production:** buildable, but the budget was unmeasured and 75 % class C, detail wasn't tied to what the camera sees, and the Endeavor and M-1C weren't really "built" for this board.

## Major issues and decisions

### Physics (6)

| Issue | Decision | Where |
|---|---|---|
| The Astrid can't stop after its spinal shot | It brakes with the line, stops 10,800 km out and **fires from rest**: no-escape range 11,017 km against a crippled monitor, flight still 184 s | 49–51; KEY_NUMBERS; map E |
| "The line" down Site 1's zenith turns at 15°/h, so nothing can coast down it | **No line to hold.** The fleet flies an inertial path of ~113,000 km from Anchor (turnover T+7:16, stop T+7:51). The waves fly straight from Anchor to where Breakwater will be. The reviewer's "corridor fixed at arrival time" was tried and dropped (see *Beyond the reports*) | 37, 41–42; maps D and E |
| Straight down Site 1's line, Maren is the backstop | The waves arrive **~48° off Breakwater's zenith**; their misses pass ~31,000 km from Maren's centre. The spinal shot comes in **15° off**: a miss, aimed ahead of the moving monitor, clears the surface by ~7,000 km | 37, 46, 49; map E; O9 |
| Heat: the 31 % readout, and fins stowed until T+9:10 | The three surviving fins vent again at Anchor until ~T+5:43 (31 %). The fleet runs dark on the approach. It reaches **98 % at T+8:00 and dumps water**; the fins go out at T+8:24 | 37, 52, 54; KEY_NUMBERS |
| Two hours in Site 1's sky with no effect | Site 1 burns the Extenuating's forward boom (the one visible cost). The fleet holds its arrays for the heat, **rolls and lays smoke**, then dazzles at T+7:50 | 39, 44 |
| Skerry's rounds too slow for the clock | Mass driver raised to **12.5 km/s** (H-14): flight time 6 h 36 m, so T+0:04 → T+6:40 | 7, 38; Defence HO3; WN §2 |

### Doctrine (6)

| Issue | Decision | Where |
|---|---|---|
| The spend wave lands an hour before the kill wave | **90 s apart**: spend T+7:52:00, kill T+7:53:30 (O3 now says 1–2 minutes). The spend wave's arrival has its own shot, and the destroyer steers the kill wave around the revealed batteries | 41–42, 45–46; O3 |
| The Astrid ends up leading into the anvil | It trails, brakes with the line, stops **behind the escorts** (10,800 km against their 8,500 km) and fires from rest | 49; map E |
| An unswept, predictable anchorage | Corvettes and drones sweep Anchor and **trip a mine**; the Donnager shells the rocks nearest-first ("Clear inside three hundred"). The platform sits at **400 km** (16 s flight) and the frigate unmasks at **45 km**; both strike in the same minute | 28, 30–36; map C |
| Nobody hunts the last ECW destroyer | **Breakwater fires all 64 cells at the Extenuating** (T+7:25); the Astrid's umbrella kills them (T+7:31) | 40, 43 |
| Site 1 falls silent in the final approach | As physics issue 5: Site 1 burns and dazzles; the fleet answers with rolls, smoke, then dazzle | 39, 44 |
| The hedgehogs' magazines don't add up | The **Infinity** fires wave one (150) and empties into the spend wave. The **Galactica** fires the kill wave. The **Pillar of Autumn** holds its ~700 in reserve (O11). The pack stays at Anchor as a fire base instead of flying home alone | 9, 37, 41–42; FLEET |

### Lore (2)

| Issue | Decision | Where |
|---|---|---|
| The lance is a free-flying ring | A **field-held jet** from the nose channels to the target inside a faint sheath; it fizzles back when `lance_power` cuts. ~50 km is how far the ship can project its field (A-23 reworded) | 33–34; FX-LANCE; LREF §4.3 |
| The Astrid isn't kilometre-long | "Its **1.6-kilometre** hull": the kilometre is the gun | 21 |

### Cinematography (6)

| Issue | Decision | Where |
|---|---|---|
| Subtitles bury the picture | Lines cut and rewritten; short tags (ACTUAL, EXTENUATING…). Every shot now reads at **≤ 12 characters a second**, and the builder checks it | all |
| One tempo throughout | Re-timed to 3:34 with holds: the 2 h coast plays on the clock (12), the hiss after each loss (20, 25), and three minutes on the crippled monitor (50), the film's suspense beat | 12, 20, 25, 50, 54 |
| Lenses too short to see the far end | A **tracker** body (300–2,000 mm) and matched framings: the platform's rock (18 → 22), the glimpse (30 → 36), the Casaba angle (47 → 50–51) | 19–22, 30–36, 43, 45, 53 |
| No clock or HUD plan | A persistent clock that runs at the shot's rate and rolls on big jumps; one master plot with Maren screen right; at most ~4 labels; a fixed SINK/FINS readout | CLOCK_HUD; 7, 8, 24, 27, 37 |
| The losses and the antagonist aren't set up | The Canterbury speaks first ("Net's up. Going quiet."), the Normandy calls the drones, Breakwater gets a reveal (40), and the last plot names both lost ships | 5, 23, 40, 53 |
| Time compression turns big hulls into models | Rotations at ≤ 4× with the middle cut out; every internal cut is now its own shot with its own clock | 21, 26, 49; the a/b splits below |

### Production (6)

| Issue | Decision | Where |
|---|---|---|
| The render budget is unmeasured | Classes re-costed (A 45, A2 90, B 75, C 200, D 15, E 2 s/frame) and computed per shot: **119 h, 155 h with 30 % margin**, inside the week. Shots 2, 10, 17 and 35 plus one volume test are the benchmarks | RENDER_CLASSES, RENDER_NOTE |
| Detail isn't tied to what the camera sees | A **closest-view** table for every main asset; proxies proposed for the ring stations, the tender and the PD module (**Q13**) | CLOSEST; ASSET_REQUESTS |
| The Endeavor and M-1C aren't built for this board | EN and M1C are "extend: rebuild after the pending picks" (**Q15**) and come first in the build order | ASSETS; PRODUCTION_PLAN |
| Rig gaps | Per-fin `fin_*` and `fin_port_state`, `ciws_phase` with a spin-blur swap, `ciws_fire`, `cm_chaff/flare/smoke`, `ew_active`, `water_dump`, `dmg_belt`, plus a controls list for every new asset | EN-FIN, EN-PD, EN-DMG, AST, BW… |
| Break-ups and volumes | A **section-break rig** (hulls split at bulkhead frames, `break` 0→1) instead of cell fracture; venting as ice glints; one cached smoke VDB; the Mist pass for haze | FX-BREAK, FX-VENT, FX-SMOKE, BRK |
| Swarms with hundreds of plumes | One Geometry Nodes swarm system with LODs, single emissive plume meshes, lights on the ~5 nearest only, its own view layer | FX-SWARM |

## Minor issues and nits

Applied unless marked otherwise.

- **Physics.**
  - **The shadow is narrower than the text says.** Anchor hides the fleet from Site 1, and from Breakwater only near the rock. The Astrid stays within ~300 km, the platform has a clear line of sight, and the braking burn ends on Anchor's orbital velocity.
  - **The fins retract faster than the slugs arrive.** Fixed by putting the platform at 400 km.
  - **The terms shot's distance.** It becomes a 2,000 mm tracker from 8,500 km.
  - **Nits:**
    - the slew is "the last degrees";
    - the spinal flight to the platform is 108 s;
    - "holed bow to stern";
    - Casaba jets from 2 km;
    - pellet clouds ~20 km across;
    - light-lag 0.87 s.
- **Doctrine.**
  - **Skerry is under-used.** Its laser dazzles the Astrid's dish (7). It now throws three rounds every ten minutes until wave one kills it: 18 rounds, arriving as six nets from T+6:40 that the fleet side-steps one by one (38). Its depot flushes 40 drones at the park (11, 37).
  - **The park guard.** It is the Excelsior and the Tantive IV (D11). The Tantive's old line went to the Rocinante (15).
  - **Loose ends:**
    - the Canterbury's drones are picked up (24);
    - the control craft is found and dazzled (24);
    - two frigates wait behind the limb (37);
    - the ring is reworded (40);
    - the head count is fourteen (3).
  - **Nits:**
    - the rule citations are corrected;
    - at the terms, the Astrid's firing line has already swung onto the next ring station (53).
- **Lore.**
  - **The net is degraded:** "Extenuating, the net's yours", plus a NET DEGRADED tag.
  - **The Infinity's load:** it now empties into the spend wave.
  - **The destroyer's dish:** it follows the art, forward (**Q14**).
  - **The corvette and tender briefs:** they now carry the design rules.
  - **The shieldless crossing:** acknowledged ("No shields from here").
  - **Labels:** re-tagged ([A-29], [Model]).
  - **Nits:**
    - the Astrid glows like a lantern (12);
    - "Casaba jets", not plasma;
    - "Remember the Cant." moves to a gun-deck voice, and a one-way hail is added before the spinal shot (48);
    - the final line closes the shields and T-SEC loop (54).
  - **Not applied: the Endeavor's 16 VLS.** It keeps its cells for self-defence. A capital ship this deep in the anvil holds its own missiles, and the kill wave's 700 don't need 16 more. It can be added to shot 44 if the user wants the moment.
- **Cinematography.**
  - **Film rules:** a screen-direction rule, camera bodies with the sound rule (the builder checks that only hull cameras hear), and a lighting plan (the sun behind Maren; darkness in Anchor's lee; Site 1 on the night side).
  - **Coverage:** ECUs (16), a long-lens group shot (10), and a hull-camera flip (26).
  - **Housekeeping:** the act break is moved to the turnover.
- **Production.**
  - **Environment:** World presets and a Sun object (WORLD).
  - **Rendering:** crash-safe EXR rendering and the grade as a separate pass.
  - **Planning:** eight set-ups, which the builder checks cover every shot once, and a build order.
  - **The asset list:** all of its corrections are applied. The one exception is the Compact frigate. It stays real detail rather than a proxy, because the new 1,000 mm lance shot (34) shows it at ~470 px.

## Beyond the reports

Things found while revising, not raised by any reviewer:

1. **The "corridor fixed at arrival time" doesn't pay.** By T+7:53 Breakwater's zenith has turned ~41°, and Anchor lies ~48° off it. Bending the waves onto a 15° line would cost a ~33° turn at speed, most of their Δv reserve. A new WN §8 case shows why it doesn't matter. A wave aimed at an orbital target never comes within ~36,000 km of Site 1, so the site kills ~15 per wave at 48° and ~5 at 15°. The angle only has to keep misses off Maren (O9), which ~48° does. The 15° line is kept for the spinal shot, the one weapon that can't divert.
2. **The clock ran backwards** in three places: Act I (4 → 5 → 6), the Broadside → The platform dies pair, and Spinal → Three minutes. All are fixed, and the builder now checks clock continuity for every shot with a stated rate.
3. **"The pack fires" claimed two launches 90 s apart in a 4 s shot at 1:1.** Split into 41 and 42 (*Kill wave away*).
4. **Breakwater's 64 missiles had no payoff.** Added 43 (*Umbrella*).
5. **The escorts would have sat 740 km from the Astrid's line of fire.** They now stop at 8,500 km, 25° off Breakwater's zenith, ~1,500 km clear of it.
6. **Sketches still drew gold shields after the park.** They now drop them automatically after T+0:02.
7. **Hand-typed shot numbers had already drifted.** Text now refers to shots by title, and the builder numbers them and checks every reference.

## Doctrine refinements (made before revision 2)

- **LREF:**
  - O3: the spend wave lands 1–2 min before the kill wave.
  - O9: never with an inhabited world behind the target; final legs ≥ 10° off the target's local vertical.
  - §4.3 and A-23: the lance is a field-held jet with ~50 km of field reach.
  - §13: a ROE sub-bullet on firing past a target.
  - The destroyer's dish follows the art.
  - The laser-link mesh is tagged [A-29], and the counter-rotating hab rings [Model].
  - §3: the net thins with fewer destroyers.
- **Defence:**
  - The mass driver is 12.5 km/s (H-14, HO3: "100,000 km ≈ 2.2 h"; "can shatter small rocks… a large rock it can only ring with canister clouds").
  - The inner-ring rows are reworded (21,800 km apart, sector defence).
- **Working numbers:**
  - §2: the mass driver entry.
  - §8: the new case of a ground site against a wave aimed at an orbital target.
- **Draft corrections:** the mass driver's flight time.

## Revision 1 → revision 2

| Rev 1 | Rev 2 | Note |
|---|---|---|
| 1 Black, then a star | 1 | |
| 2 Rings cool | 2 | line dropped (the picture shows it) |
| 3 The task group | 3 | long lens; fourteen ships |
| 4 Shields to the park | 4 | camera rides the shield |
| 5 The moon speaks | 7 Skerry throws | the laser's glare added |
| 6 The Astrid looks | 5 Net up, 6 The Astrid looks, 8 The picture | split; the Canterbury introduced |
| 7 Wave one | 9 | hull camera on the Infinity |
| 8 Turn and burn | 10 | 400 mm, the whole group |
| 9 Skerry burns | 11 | the depot flushes its drones |
| 10 Fins edge-on | 12 | the coast plays on the clock |
| 11 The Breakers | 13 | "No shields from here" |
| 12 Blind | 14 | |
| 13 The belt wakes | 15 | |
| 14 Countermeasures | 16 Spin-up, 17 Countermeasures | ECU added |
| 15 Railguns in the rocks | 18 The platform, 19 Canterbury | split |
| 16 Canterbury | 20 Holed | bow to stern; the hiss |
| 17 Answer | 21 Answer, 22 Payback | split; matched framing |
| 18 Screens out | 23 | the Normandy calls it |
| 19 Return to sender | 24 | NET DEGRADED; the control craft |
| 20 Normandy | 25 | |
| 21 Turnover | 26 | hull camera; act break moved here |
| 22 Into the lee | 27 Anchor, 28 The sweep | the rock renamed; sweep and mine |
| 23 Too hot | 29 | |
| 24 Fin hit | 30 Fins in, 31 Fin hit | the platform at 400 km |
| 26 The frigate | 32 Off the port bow | 45 km, same minute |
| 27 Lance | 33 Lance channels, 34 Lance | field-held jet; 1,000 mm |
| 25 Broadside | 35 Broadside, 36 The platform dies | now after the lance |
| 28 The line | 37 The fire plan | no line; the fire plan |
| 30 The net | 38 | first of six nets |
| — | 39 Site One | new: Site 1's cost |
| 31 The anvil | 40 | the 64 cells fire |
| 29 Wave two | 41 The pack fires, 42 Kill wave away | now 90 s apart, from Anchor |
| — | 43 Umbrella | new: the 64 die |
| 32 Blind it | 44 | |
| — | 45 The spend wave | new: the spend wave dies over the limb |
| 33 Wall of fire | 46 | |
| 34 Casaba | 47 | 2 km, the drive section |
| — | 48 The hail | new |
| 35 Spinal | 49 Spinal, 50 Three minutes, 51 Impact | from rest; the three-minute hold |
| — | 52 Heat | new: the water dump |
| 36 Terms | 53 | 2,000 mm; the next ring station |
| 37 Hold | 54 | end-on; Site 1's lights go out |

## For round 2

The areas that changed most, and deserve the hardest look:
- **Act IV geometry** (maps D and E): the inertial approach, the waves from Anchor at ~48°, the Astrid's firing point, the escorts' stop.
- **The heat thread:** 94 % → 31 % → 98 % and the water dump.
- **The new shots:** 5, 16, 28, 39, 42, 43, 45, 48 and 52.
- **Anchor as a fire base:** whether the pack can stay hidden there for two hours while the rock drifts 29° off Site 1.
- **Skerry's six nets,** side-stepped during the coast and the braking burn.
- **The render budget** (155 h with margin) and the new closest-view table.
