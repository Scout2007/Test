# Operation Tidebreak: shot list

Revision 2 · after review round 1. Runtime 3:34 (5,136 frames at 24 fps), 54 shots, mission span T+0:00 → T+8:24, 2.39:1 · 1920×804 · 24 fps · Cycles. Generated from `storyboard/tidebreak_data.py`; the page with maps and sketches is `storyboard/index.html`.

Rule IDs refer to `doctrine/LREF_doctrine.md` (O, D, A) and `doctrine/Defence_doctrine.md` (HO, HD, H). Asset IDs refer to `ASSET_REQUESTS.md`. Render classes: **A** Endeavor close-up (~45 s/frame); **A2** Endeavor close-up with heavy FX (~90 s/frame); **B** One hero ship or rock, full view (~75 s/frame); **C** Several ships or heavy FX (FX in own layers) (~200 s/frame); **D** Wide, distant or plate (~15 s/frame); **E** 2D comp / HUD (~2 s/frame).

## Mission phases

| Mission time | Phase | What happens |
|---|---|---|
| T+0:00–T+0:25 | Arrival | Exit at 450,000 km, near rest relative to Maren. Shields parked with the Nauvoo (T+0:02). Net up. Skerry throws three rounds (T+0:04) and its laser dazzles the Astrid's dish, so the fins stay in. Wave one away at Skerry (T+0:18). |
| T+0:25–T+0:59 | Turn and burn | 1 g along the approach line for 34 min: 0 → 20 km/s over 20,400 km. |
| T+0:59–T+3:20 | Coast | 20 km/s, bow on Maren. Skerry's laser dies at T+1:02 and its depot flushes 40 drones toward the shield park; the fins come out edge-on at T+1:10. |
| T+3:20–T+4:34 | The Breakers | Fins stowed in the debris. Site 1 dazzles; the pods wake; the Canterbury is lost (T+3:52); the Astrid answers; drones wake; the Normandy is lost (T+4:25). |
| T+4:34–T+5:09 | Turnover | Flip (49 s) and brake at 1 g for 34 min, ending on Anchor's orbital velocity (1.63 km/s; thrust tilted ~4.7°). |
| T+5:09–T+5:43 | Anchor | An 18 km rock that at T+5:09 lies over Site 1. The fleet sweeps it (a mine), vents, loses the port fin to a platform 400 km off, lances a frigate, kills the platform, and vents again with three fins (94 % → 31 %). |
| T+5:43–T+7:51 | Final approach | An inertial path of ~113,000 km: 1 g to 20 km/s (to T+6:17), coast, turnover at T+7:16, then brake to a stop ~8,500 km from Breakwater (T+7:51). The Astrid, trailing, stops 10,800 km out. Skerry's net at T+6:40; Site 1's fire from T+6:55; Breakwater's 64 missiles at the Extenuating (T+7:25), killed under the Astrid's umbrella (T+7:31). The pack stays at Anchor as a fire base. |
| T+7:27–T+7:58 | Hammer and anvil | From Anchor, 118,000 km out, the spend wave (Infinity) arrives at T+7:52:00 and the kill wave (Galactica) at T+7:53:30. Both fly straight in, nose-on to Breakwater and ~48° off its zenith, so misses and wreckage clear Maren. Casaba jets cut the drive. The Astrid hails, then fires from rest at T+7:54:40, 15° off Breakwater's zenith; impact T+7:57:44. |
| T+7:58–T+8:24 | Terms | Sink 98 %: the Endeavor dumps water (T+8:00). Maren asks for terms (T+8:10). Site 1 goes dark; the fleet vents at last (T+8:24). |

## Film rules

**Lighting**

- The sun sits behind Maren, about 30° off the approach line. From the fleet Maren is a thin crescent with a bright limb, and the Breakers glow faintly lit from behind (dust scatters forward).
- Hulls are lit hard from ahead and to one side; the shadow side falls to black. No stars behind sunlit hulls.
- Anchor's lee faces away from both Site 1 and the sun: the fleet shelters in darkness, so the fins, muzzle flashes and the lance light the scene (the M-1C 'fins1dark' look).
- At the end Site 1 is on the night side: its lights can be seen going out, and the final frame puts the Endeavor against the night side's city lights.

**Mission clock and HUD**

- The mission clock is small, persistent and clear of the subtitles. It starts on the flash in shot 1 (T+0:00:00).
- It runs at the shot's rate: spinning seconds mean compressed time, crawling ones slowed. On jumps over 30 minutes the digits roll or the shot dissolves.
- One master tactical plot, always with Maren screen right. Inserts hold for at least 5 s where they carry geography, with no more than about four labels.
- A fixed corner readout carries ENDEAVOR SINK nn % and FINS n/4 from Act III, so the heat builds visibly toward the dump.
- Subtitles and the clock go in during the edit, after the grade, so a changed line never forces a re-render.

**Screen direction**

- Maren and the enemy stay screen right. The LREF travels and fires left to right.
- Until the turnover (shot 26) bows point right. After it bows point left while travel stays left to right, so the drives burn toward screen right.
- The final approach repeats the pattern: bows right from Anchor to the second turnover (T+7:16), bows left while braking, and the Astrid swings its bow back to screen right for the spinal shot.
- Enemy reverses only over an enemy foreground. At Anchor the Endeavor's bow points at the frigate's moonlet: the frigate is off the port bow, the platform off the port quarter, and shots 30–36 share that axis.

**Camera bodies**

- Hull camera: bolted to a ship, shakes with it, and is the only body that hears (sound through structure).
- Drone camera: free-flying, silent; score and sub-bass only.
- Tracker: a long lens (300–2,000 mm) on a ship or drone; heavy slow pans, sensor noise; silent.
- HUD insert: 2D compositing, UI tones only.

## Overview

| # | Film | Frames | Mission clock | Time | Title | Camera | Doctrine |
|---|---|---|---|---|---|---|---|
| 1 | 0:00.0–0:06.0 | 1–144 | T+0:00:00 | 1:1 | Black, then a star | EWS · 35 mm · locked off (drone camera) | O1 |
| 2 | 0:06.0–0:10.0 | 145–240 | T+0:00:06 | 1:1 | Rings cool | CU · 50 mm · slow push along the bow ring truss (hull camera) | O1 |
| 3 | 0:10.0–0:15.0 | 241–360 | T+0:00:10 | compressed 7× (13 exits over ~36 s) | The task group | EWS · 85 mm · long lens, locked off (tracker) | O1 D2 |
| 4 | 0:15.0–0:20.0 | 361–480 | T+0:02:00 | compressed 8× (~40 s) | Shields to the park | MS · 35 mm · riding the shield's backplate, looking back at the bow (hull camera) | O1 D9 D11 |
| 5 | 0:20.0–0:23.0 | 481–552 | T+0:02:40 | compressed 10× (the dish unfolds over ~30 s) | Net up | MS · 40 mm · off the Canterbury's bow (drone camera) | O2 D10 |
| 6 | 0:23.0–0:26.0 | 553–624 | T+0:03:20 | compressed 10× (the slew takes ~30 s) | The Astrid looks | MS · 50 mm · along the Astrid's dorsal hull (drone camera) | O2 D3 |
| 7 | 0:26.0–0:31.0 | 625–744 | T+0:04:10 | 1:1 | Skerry throws | HUD insert · the Astrid's telescope feed, 2,000 mm equivalent (HUD insert) | HO3 HO5 O2 |
| 8 | 0:31.0–0:36.0 | 745–864 | T+0:09:00 | compressed 60× (the picture builds over ~5 min) | The picture | HUD insert · the master plot (HUD insert) | O2 D3 |
| 9 | 0:36.0–0:41.0 | 865–984 | T+0:18:00 | 1:1 | Wave one | WS · 24 mm · on the Infinity's hull, shaking with each launch (hull camera) | O3 O9 D3 |
| 10 | 0:41.0–0:47.0 | 985–1128 | T+0:25:00 | compressed 8× (the turn takes ~49 s) | Turn and burn | EWS · 400 mm · the whole group (tracker) | O1 D2 |
| 11 | 0:47.0–0:51.0 | 1129–1224 | T+1:02:00 | compressed 5× (~20 s of hits) | Skerry burns | EWS · 1,200 mm · Skerry a quarter-frame disc (tracker) | O3 O9 HO8 |
| 12 | 0:51.0–0:57.0 | 1225–1368 | T+1:10:00 | compressed; the clock rolls through a 2 h 10 min coast | Fins edge-on | MS · 40 mm · arcing round to dead ahead (drone camera) | D3 |
| 13 | 0:57.0–1:01.0 | 1369–1464 | T+3:20:00 | 1:1 | The Breakers | WS · 24 mm · tracking alongside (drone camera) | O8 D3 D5 D6 |
| 14 | 1:01.0–1:04.0 | 1465–1536 | T+3:30:00 | 1:1 | Blind | CU · 85 mm · the sensor mast, with its POV feed inset (hull camera) | HO5 |
| 15 | 1:04.0–1:07.0 | 1537–1608 | T+3:40:00 | compressed 10× (~30 s) | The belt wakes | WS · 40 mm · beside a rock ahead of the fleet (drone camera) | HO2 HD3 |
| 16 | 1:07.0–1:08.0 | 1609–1632 | T+3:45:00 | 1:1 | Spin-up | ECU · 100 mm · a CIWS (hull camera) | D1 |
| 17 | 1:08.0–1:12.0 | 1633–1728 | T+3:45:01 | 1:1 | Countermeasures | MS · 35 mm · along the port flank (drone camera) | D1 |
| 18 | 1:12.0–1:14.0 | 1729–1776 | T+3:52:00 | 1:1 | The platform | WS · 50 mm · over the platform's shoulder (drone camera) | HO1 HO2 HO9 |
| 19 | 1:14.0–1:16.0 | 1777–1824 | T+3:52:05 | compressed 4× (13 s flight) | Canterbury | Tracker · 600 mm · from the Extenuating Circumstances (tracker) | D4 |
| 20 | 1:16.0–1:21.0 | 1825–1944 | T+3:52:13 | 1:1 | Holed | Tracker · 600 mm · holding on the Canterbury (tracker) | HO9 |
| 21 | 1:21.0–1:25.0 | 1945–2040 | T+3:52:36 | 1:1 (the last degrees of the slew) | Answer | EWS · 135 mm · the Astrid in profile, bow screen right (drone camera) | O4 |
| 22 | 1:25.0–1:28.0 | 2041–2112 | T+3:54:28 | the clock jumps 108 s | Payback | WS · 50 mm · the platform shot's framing (drone camera) | O4 |
| 23 | 1:28.0–1:32.0 | 2113–2208 | T+4:10:00 | compressed ~30× (2 min) | Screens out | WS · 28 mm · behind the corvettes (drone camera) | HO4 D6 O7 |
| 24 | 1:32.0–1:36.0 | 2209–2304 | T+4:14:00 | 1:1 | Return to sender | HUD insert · the Extenuating Circumstances' plot (HUD insert) | O5 HD9 D10 |
| 25 | 1:36.0–1:39.0 | 2305–2376 | T+4:25:00 | 1:1 | Normandy | Tracker · 300 mm · from the Wallfish (tracker) | HO4 |
| 26 | 1:39.0–1:45.0 | 2377–2520 | T+4:34:10 | rotation at ~4×, the middle of the 49 s flip cut out | Turnover | WS · 24 mm · on the dorsal hull looking aft (hull camera) | D8 O8 |
| 27 | 1:45.0–1:48.0 | 2521–2592 | T+5:08:00 | 1:1 | Anchor | HUD insert · the master plot, zoomed (HUD insert) | D5 D2 |
| 28 | 1:48.0–1:52.0 | 2593–2688 | T+5:09:00 | compressed ~20× (minutes) | The sweep | WS · 24 mm · low over Anchor's surface (drone camera) | O8 D6 O4 |
| 29 | 1:52.0–1:56.0 | 2689–2784 | T+5:12:00 | compressed 5× (the fins take ~20 s) | Too hot | MS · 35 mm · on the stern shoulder (hull camera) | D3 D5 |
| 30 | 1:56.0–2:00.0 | 2785–2880 | T+5:13:00 | compressed ~4× (the fins crawl in against a 16 s flight) | Fins in | MS · 35 mm · the same shoulder, the clock large (hull camera) | HO7 HO1 D3 |
| 31 | 2:00.0–2:03.0 | 2881–2952 | T+5:13:16 | 1:1 | Fin hit | CU · 50 mm · on the port fin (hull camera) | HO7 D7 |
| 32 | 2:03.0–2:07.0 | 2953–3048 | T+5:13:30 | 1:1 | Off the port bow | Hull camera · 600 mm · on the Endeavor's port side (hull camera) | HO6 O6 |
| 33 | 2:07.0–2:09.0 | 3049–3096 | T+5:13:53 | 1:1 | Lance channels | CU · 28 mm · the Endeavor's nose (hull camera) | O12 |
| 34 | 2:09.0–2:11.0 | 3097–3144 | T+5:13:55 | 1:1 | Lance | Tracker · 1,000 mm · on the frigate, 40 km out (tracker) | O12 O6 |
| 35 | 2:11.0–2:17.0 | 3145–3288 | T+5:14:00 | the roll at 5× (3 s), then 1:1 (3 s) | Broadside | MS · 35 mm · the port batteries, the rock beyond (hull camera) | O6 O4 D3 |
| 36 | 2:17.0–2:19.0 | 3289–3336 | T+5:14:31 | the clock jumps 13 s (16 s of flight) | The platform dies | Tracker · 1,200 mm · the glimpse's framing (tracker) | O4 |
| 37 | 2:19.0–2:24.0 | 3337–3456 | T+5:40:00 | 1:1 | The fire plan | HUD insert · the master plot (HUD insert) | O9 O3 O10 O11 HO6 HO8 D11 |
| 38 | 2:24.0–2:29.0 | 3457–3576 | T+6:40:00 | compressed ~24× (2 min) | The net | WS · 50 mm · over the Extenuating Circumstances (drone camera) | HO3 D4 O8 |
| 39 | 2:29.0–2:33.0 | 3577–3672 | T+6:55:00 | compressed ~15× (a minute) | Site One | WS · 40 mm · ahead of the Extenuating Circumstances (drone camera) | HO5 D1 D3 |
| 40 | 2:33.0–2:37.0 | 3673–3768 | T+7:25:00 | compressed 10× (the ripple takes ~40 s) | The anvil | WS · 40 mm · above Breakwater, Maren's night side below (drone camera) | HD7 HO9 HD1 HO1 D1 |
| 41 | 2:37.0–2:41.0 | 3769–3864 | T+7:27:00 | 1:1 | The pack fires | WS · 24 mm · low over Anchor, looking toward Breakwater (drone camera) | O3 O11 |
| 42 | 2:41.0–2:44.0 | 3865–3936 | T+7:28:30 | 1:1 | Kill wave away | Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow (tracker) | O3 O10 O11 |
| 43 | 2:44.0–2:47.0 | 3937–4008 | T+7:31:00 | 1:1 | Umbrella | Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 20 km above (tracker) | D1 D2 D10 HO9 |
| 44 | 2:47.0–2:50.0 | 4009–4080 | T+7:50:00 | 1:1 | Blind it | MS · 35 mm · the Endeavor's laser arrays (hull camera) | O5 HD9 |
| 45 | 2:50.0–2:53.0 | 4081–4152 | T+7:52:00 | 1:1 | The spend wave | Tracker · 800 mm · from the Astrid, over Maren's limb (tracker) | O3 O5 HD5 |
| 46 | 2:53.0–2:57.0 | 4153–4248 | T+7:53:28 | slowed 5× (the wave arrives within ~1 s) | Wall of fire | WS · 40 mm · above Breakwater (drone camera) | O3 HD5 O9 |
| 47 | 2:57.0–3:01.0 | 4249–4344 | T+7:53:30 | slowed 3× | Casaba | WS · 35 mm · off Breakwater's quarter (drone camera) | O10 |
| 48 | 3:01.0–3:06.0 | 4345–4464 | T+7:54:00 | 1:1 | The hail | MS · 50 mm · slow push on Breakwater over the night side (drone camera) | O10 |
| 49 | 3:06.0–3:09.0 | 4465–4536 | T+7:54:37 | 1:1 (the last degree of the slew; it fires at T+7:54:40) | Spinal | EWS · 200 mm · the Astrid end-on (drone camera) | O4 O10 HD7 O9 |
| 50 | 3:09.0–3:13.0 | 4537–4632 | T+7:54:40 | compressed 45× (180 of the slug's 184 s; the clock races) | Three minutes | WS · 35 mm · the Casaba shot's angle (drone camera) | O10 |
| 51 | 3:13.0–3:16.0 | 4633–4704 | T+7:57:44 | 1:1 | Impact | WS · 35 mm · the Casaba shot's angle (drone camera) | O4 |
| 52 | 3:16.0–3:20.0 | 4705–4800 | T+8:00:00 | 1:1 | Heat | MS · 35 mm · along the Endeavor's scorched port flank (hull camera) | D3 D7 |
| 53 | 3:20.0–3:25.0 | 4801–4920 | T+8:10:00 | 1:1 | Terms | Tracker · 2,000 mm · from the Endeavor's standoff (tracker) |  |
| 54 | 3:25.0–3:34.0 | 4921–5136 | T+8:24:00 | 1:1 | Hold | EWS · 35 mm · locked off, the Endeavor end-on (drone camera) | D3 |

## Act I: Arrival

The fleet arrives slow, parks its shields, reads the system, and strikes Skerry first because Skerry's laser can burn its fins.

### 1. Black, then a star

- **Film:** 0:00.0–0:06.0 (6 s), frames 1–144
- **Mission:** T+0:00:00 · 1:1
- **Camera:** EWS · 35 mm · locked off (drone camera)
- **Action:** Starfield. A point of light swells into a blue-white bloom as the bubble collapses (~5 s). The Endeavor resolves out of it, bow screen right, shield forward, both warp rings glowing, fins stowed as they must be in warp. The mission clock starts on the flash.
- **Doctrine:** O1
- **VFX:** Warp-exit flash
- **Rig:** warp_charge 1→0.3
- **Assets:** EN (extend), FX-WARP (new), HUD (new)
- **Sound:** Silence; a sub-bass drop as the bubble collapses.
- **Render class:** D · **Map:** A

### 2. Rings cool

- **Film:** 0:06.0–0:10.0 (4 s), frames 145–240
- **Mission:** T+0:00:06 · 1:1
- **Camera:** CU · 50 mm · slow push along the bow ring truss (hull camera)
- **Action:** The front warp ring's emitters fade from blue to dark. A burst of bow RCS trims the drift.
- **Doctrine:** O1
- **VFX:** Emitter glow fade, RCS puffs
- **Rig:** warp_charge 0.3→0; rcs_bow pulse
- **Assets:** EN (extend)
- **Sound:** Ticking metal and RCS thumps through the truss.
- **Render class:** A · **Map:** A · **Reference frame:** `img/bow_v4b_combat.jpg`

### 3. The task group

- **Film:** 0:10.0–0:15.0 (5 s), frames 241–360
- **Mission:** T+0:00:10 · compressed 7× (13 exits over ~36 s)
- **Camera:** EWS · 85 mm · long lens, locked off (tracker)
- **Action:** Staggered warp flashes, seconds and 50+ km apart: the Astrid, the hedgehog pack, the Donnager, the Excelsior, both destroyers, four corvettes, the Nauvoo. Screen right, Maren is a thin crescent with the sun behind it, ringed by the faint backlit glow of the Breakers.
- **Comms:** ACTUAL: “All fourteen. All home.”
- **Doctrine:** O1, D2
- **VFX:** 13 warp flashes, backlit ring glow
- **Rig:** none
- **Assets:** AST (new), GI (new), GI-MAV (new), DD (new), CV (new), TND (new), MAREN (extend), BRK (new), WORLD (extend), FX-WARP (new), FX-FAR (new), SUB (new)
- **Sound:** Distant low thuds, one per exit (score, not diegetic).
- **Render class:** D · **Map:** A

### 4. Shields to the park

- **Film:** 0:15.0–0:20.0 (5 s), frames 361–480
- **Mission:** T+0:02:00 · compressed 8× (~40 s)
- **Camera:** MS · 35 mm · riding the shield's backplate, looking back at the bow (hull camera)
- **Action:** Separation thrusters fire between the front ring's spokes. The camera, riding the shield, backs away from the Endeavor's bow; both warp rings stay on the ship. Around it, other gold shields hang parked at near-zero speed, to be collected after the battle.
- **Comms:** ENDEAVOR: “Nauvoo, Endeavor. The shield's yours.” / NAUVOO: “Porch light's off.”
- **Doctrine:** O1, D9, D11
- **VFX:** Shield separation, thruster plumes
- **Rig:** shield_thrusters 1; shield_separation 0→400
- **Assets:** EN (extend), SHD (extend), TND (new), GI-PD (new), SUB (new)
- **Sound:** Clamp bangs through the backplate, then silence.
- **Render class:** A · **Map:** A · **Reference frame:** `img/endeavor_combat_demo_f060.jpg`

### 5. Net up

- **Film:** 0:20.0–0:23.0 (3 s), frames 481–552
- **Mission:** T+0:02:40 · compressed 10× (the dish unfolds over ~30 s)
- **Camera:** MS · 40 mm · off the Canterbury's bow (drone camera)
- **Action:** The Canterbury swings its big dish out behind where its shield sat and runs out its sensor booms; its drones scatter ahead. From here the fleet talks only by laser.
- **Comms:** CANTERBURY: “Net's up. Going quiet.”
- **Doctrine:** O2, D10
- **VFX:** Drone launch
- **Rig:** dish_deploy (new); booms_deploy (new); drone_bay (new)
- **Assets:** DD (new), DRN-L (new), SUB (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** A

### 6. The Astrid looks

- **Film:** 0:23.0–0:26.0 (3 s), frames 553–624
- **Mission:** T+0:03:20 · compressed 10× (the slew takes ~30 s)
- **Camera:** MS · 50 mm · along the Astrid's dorsal hull (drone camera)
- **Action:** The Astrid's 100 m AVPSA dish slews toward Maren. Its eight stacked fins stay stowed: Skerry's laser can see them.
- **Doctrine:** O2, D3
- **VFX:** 
- **Rig:** avpsa_az / avpsa_el (new)
- **Assets:** AST (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** A

### 7. Skerry throws

- **Film:** 0:26.0–0:31.0 (5 s), frames 625–744
- **Mission:** T+0:04:10 · 1:1
- **Camera:** HUD insert · the Astrid's telescope feed, 2,000 mm equivalent (HUD insert)
- **Action:** A thread of light runs along Skerry's dark limb: the mass driver throwing. Three rounds leave; the plot tags them ARRIVE T+6:40 · OUR LANE. Then a glare blooms across the feed: Skerry's laser has found the dish.
- **Comms:** ASTRID: “Skerry's thrown three rounds down our lane.” / ACTUAL: “They'll be hours.”
- **Doctrine:** HO3, HO5, O2
- **VFX:** HUD, telescope grain, dazzle glare
- **Rig:** none
- **Assets:** HUD (new), SKR (new), FX-DAZZLE (new), SUB (new)
- **Sound:** Soft sensor tones.
- **Render class:** E · **Map:** A

### 8. The picture

- **Film:** 0:31.0–0:36.0 (5 s), frames 745–864
- **Mission:** T+0:09:00 · compressed 60× (the picture builds over ~5 min)
- **Camera:** HUD insert · the master plot (HUD insert)
- **Action:** The master plot, Maren screen right: Breakwater parked over Site 1; Skerry with its laser and mass driver; the Breakers; the approach line. The fins stay in while Skerry's laser can see them.
- **Comms:** ACTUAL: “Picture's up. Breakwater's right where the brief said.”
- **Doctrine:** O2, D3
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones.
- **Render class:** E · **Map:** A

### 9. Wave one

- **Film:** 0:36.0–0:41.0 (5 s), frames 865–984
- **Mission:** T+0:18:00 · 1:1
- **Camera:** WS · 24 mm · on the Infinity's hull, shaking with each launch (hull camera)
- **Action:** The Infinity ripple-fires 150 missiles at Skerry's laser, mass driver and depot in fifteen seconds. Pod doors open in waves down the hull and the plumes curve away screen right. Skerry goes first because its laser can burn the fleet's fins all the way in.
- **Comms:** ACTUAL: “Infinity, wave one. Skerry.” / INFINITY: “Wave one away.”
- **Doctrine:** O3, O9, D3
- **VFX:** 150 missiles (swarm system), pod doors
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), SUB (new)
- **Sound:** Launch cracks through the hull; the camera shakes with each.
- **Render class:** C · **Map:** A

### 10. Turn and burn

- **Film:** 0:41.0–0:47.0 (6 s), frames 985–1128
- **Mission:** T+0:25:00 · compressed 8× (the turn takes ~49 s)
- **Camera:** EWS · 400 mm · the whole group (tracker)
- **Action:** Through a long lens, fourteen drives light one after another as the group turns onto the approach line: bows toward Maren, plumes streaming screen left. One g for 34 minutes.
- **Comms:** ACTUAL: “All ships, execute. One g.”
- **Doctrine:** O1, D2
- **VFX:** Distant drive plumes
- **Rig:** none
- **Assets:** AST (new), EN (extend), GI (new), DD (new), CV (new), FX-FAR (new), SUB (new)
- **Sound:** Sub-bass swell.
- **Render class:** D · **Map:** A

## Act II: The Breakers

Hours of coasting, then the debris ring: the ambush, the Canterbury, the Astrid's answer, the drones and the Normandy.

### 11. Skerry burns

- **Film:** 0:47.0–0:51.0 (4 s), frames 1129–1224
- **Mission:** T+1:02:00 · compressed 5× (~20 s of hits)
- **Camera:** EWS · 1,200 mm · Skerry a quarter-frame disc (tracker)
- **Action:** Pinpricks of white on Skerry's limb: wave one arriving, nose-on to the battery. The light left Skerry 0.9 s ago. Just before the hits, a faint spray of points leaves the depot: its drones, flushed toward the shield park.
- **Comms:** ASTRID: “Splash on Skerry. Their laser's gone.”
- **Doctrine:** O3, O9, HO8
- **VFX:** Distant nuclear flashes, flushed drones
- **Rig:** none
- **Assets:** SKR (new), FX-NUKE (new), SUB (new)
- **Sound:** Nothing; a swell of score.
- **Render class:** D · **Map:** A

### 12. Fins edge-on

- **Film:** 0:51.0–0:57.0 (6 s), frames 1225–1368
- **Mission:** T+1:10:00 · compressed; the clock rolls through a 2 h 10 min coast
- **Camera:** MS · 40 mm · arcing round to dead ahead (drone camera)
- **Action:** With Skerry's laser gone, the four fins run out, glowing a dull red. The camera arcs to dead ahead as they extend, until they collapse to slivers: edge-on to Site 1 and Breakwater, dead ahead. Far behind, the Astrid's eight fins glow like a lantern. The clock rolls on.
- **Comms:** ENDEAVOR: “Fins out. Keep them edge-on.”
- **Doctrine:** D3
- **VFX:** Fin glow
- **Rig:** radiator_deploy 0.12→1; heat 0.6; radiator_glow
- **Assets:** EN (extend), AST (new), SUB (new)
- **Sound:** Silence; the score carries the coast.
- **Render class:** A · **Map:** A · **Reference frame:** `img/orbit_v8d.jpg`

### 13. The Breakers

- **Film:** 0:57.0–1:01.0 (4 s), frames 1369–1464
- **Mission:** T+3:20:00 · 1:1
- **Camera:** WS · 24 mm · tracking alongside (drone camera)
- **Action:** The fins retract before the debris. A faint haze thickens, lit from behind. A single large rock slides past twenty kilometres off, gone across the frame in under two seconds at 20 km/s. The corvettes spread ahead, screen right.
- **Comms:** ACTUAL: “No shields from here. Corvettes, sweep the lane.”
- **Doctrine:** O8, D3, D5, D6
- **VFX:** Dust haze (Mist pass), one rock fly-by
- **Rig:** radiator_deploy 1→0.12
- **Assets:** EN (extend), BRK (new), CV (new), DRN-L (new), SUB (new)
- **Sound:** Silence; a low drone in the score.
- **Render class:** B · **Map:** B

### 14. Blind

- **Film:** 1:01.0–1:04.0 (3 s), frames 1465–1536
- **Mission:** T+3:30:00 · 1:1
- **Camera:** CU · 85 mm · the sensor mast, with its POV feed inset (hull camera)
- **Action:** Site 1's beam finds the Endeavor through the haze. The mast's optics flare, the inset feed whites out, and armoured shutters slam shut.
- **Comms:** ENDEAVOR: “Site One's painting us. Shutters.”
- **Doctrine:** HO5
- **VFX:** Dazzle bloom, POV whiteout
- **Rig:** mast_shutter 0→1 (new)
- **Assets:** EN (extend), EN-MAST (extend), FX-DAZZLE (new), SUB (new)
- **Sound:** A static howl on the feed; the shutter slam through the hull.
- **Render class:** A · **Map:** B · **Reference frame:** `img/lookmast_v8d.jpg`

### 15. The belt wakes

- **Film:** 1:04.0–1:07.0 (3 s), frames 1537–1608
- **Mission:** T+3:40:00 · compressed 10× (~30 s)
- **Camera:** WS · 40 mm · beside a rock ahead of the fleet (drone camera)
- **Action:** Regolith heaves and petal doors open. Missiles tumble out cold, then light two kilometres clear and turn screen left, toward the fleet. Until now the pods were the temperature of the rock.
- **Comms:** ROCINANTE: “Launch! Cold birds off the rocks!”
- **Doctrine:** HO2, HD3
- **VFX:** Pod doors, late motor ignition
- **Rig:** heave / petals (new)
- **Assets:** EMP-POD (new), MSL-V (new), BRK (new), SUB (new)
- **Sound:** Silence; a sting in the score.
- **Render class:** B · **Map:** B

### 16. Spin-up

- **Film:** 1:07.0–1:08.0 (1 s), frames 1609–1632
- **Mission:** T+3:45:00 · 1:1
- **Camera:** ECU · 100 mm · a CIWS (hull camera)
- **Action:** Seven barrels blur into motion inside the perforated jacket.
- **Doctrine:** D1
- **VFX:** 
- **Rig:** ciws_phase (new); ciws_fire (new)
- **Assets:** EN (extend), EN-PD (extend)
- **Sound:** A rising whine through the hull.
- **Render class:** A · **Map:** B

### 17. Countermeasures

- **Film:** 1:08.0–1:12.0 (4 s), frames 1633–1728
- **Mission:** T+3:45:01 · 1:1
- **Camera:** MS · 35 mm · along the port flank (drone camera)
- **Action:** Chaff and flares bloom and a smoke screen unfurls, thinning as it spreads. The CIWS lay kill clouds in the missiles' paths; the laser lenses glow violet, beams invisible. Missiles pop one by one.
- **Comms:** ENDEAVOR: “PD free. Chaff, smoke.”
- **Doctrine:** D1
- **VFX:** Tracers, kill clouds, chaff, smoke, intercept flashes
- **Rig:** ciws_fire (new); cm_chaff / cm_flare / cm_smoke (new); laser_power 0→1; laser_traverse
- **Assets:** EN (extend), EN-PD (extend), FX-PD (new), FX-SMOKE (new), SUB (new)
- **Sound:** Silence (drone camera); the score's pulse.
- **Render class:** A2 · **Map:** B · **Reference frame:** `img/lookpair_final.jpg`

### 18. The platform

- **Film:** 1:12.0–1:14.0 (2 s), frames 1729–1776
- **Mission:** T+3:52:00 · 1:1
- **Camera:** WS · 50 mm · over the platform's shoulder (drone camera)
- **Action:** A buried twin railgun heaves out of a rock 600 km ahead of the fleet and fires a ten-slug pattern screen left, straight down the fleet's path.
- **Doctrine:** HO1, HO2, HO9
- **VFX:** Muzzle flashes, slug glints
- **Rig:** unmask / shot (new)
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** B

### 19. Canterbury

- **Film:** 1:14.0–1:16.0 (2 s), frames 1777–1824
- **Mission:** T+3:52:05 · compressed 4× (13 s flight)
- **Camera:** Tracker · 600 mm · from the Extenuating Circumstances (tracker)
- **Action:** The Canterbury, forty kilometres off, jinks hard on RCS, its dish forward.
- **Comms:** EXTENUATING: “Canterbury, jink!”
- **Doctrine:** D4
- **VFX:** RCS puffs
- **Rig:** none
- **Assets:** DD (new), SUB (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** B

### 20. Holed

- **Film:** 1:16.0–1:21.0 (5 s), frames 1825–1944
- **Mission:** T+3:52:13 · 1:1
- **Camera:** Tracker · 600 mm · holding on the Canterbury (tracker)
- **Action:** The slugs arrive from ahead. The Canterbury is holed bow to stern in three white flashes; it vents glittering ice, the hull parts in two and tumbles. Hold on it as its channel dies to hiss.
- **Comms:** EXTENUATING: “Canterbury's gone.” / ACTUAL: “Extenuating, the net's yours.”
- **Doctrine:** HO9
- **VFX:** Impact flashes, venting, section break
- **Rig:** break 0→1 (new)
- **Assets:** DD (new), DD-BRK (new), FX-BREAK (new), FX-VENT (new), SUB (new)
- **Sound:** The dying channel's hiss, then silence.
- **Render class:** C · **Map:** B

### 21. Answer

- **Film:** 1:21.0–1:25.0 (4 s), frames 1945–2040
- **Mission:** T+3:52:36 · 1:1 (the last degrees of the slew)
- **Camera:** EWS · 135 mm · the Astrid in profile, bow screen right (drone camera)
- **Action:** The Astrid's 1.6-kilometre hull swings its last few degrees onto the platform, steadies on RCS, and fires down the spinal: a blue-white bloom at the bow.
- **Comms:** ACTUAL: “Astrid, spinal on the platform.” / ASTRID: “Firing.”
- **Doctrine:** O4
- **VFX:** Spinal muzzle bloom
- **Rig:** spinal_charge / spinal_shot (new)
- **Assets:** AST (new), FX-SPINAL (new), SUB (new)
- **Sound:** A sub-bass punch.
- **Render class:** B · **Map:** B

### 22. Payback

- **Film:** 1:25.0–1:28.0 (3 s), frames 2041–2112
- **Mission:** T+3:54:28 · the clock jumps 108 s
- **Camera:** WS · 50 mm · the platform shot's framing (drone camera)
- **Action:** 8,600 km away and 108 seconds later, the platform's rock erupts. The platform could not move.
- **Comms:** ASTRID GUNS: “Remember the Cant.”
- **Doctrine:** O4
- **VFX:** Impact eruption on the rock
- **Rig:** none
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new), SUB (new)
- **Sound:** A delayed boom in the score.
- **Render class:** B · **Map:** B

### 23. Screens out

- **Film:** 1:28.0–1:32.0 (4 s), frames 2113–2208
- **Mission:** T+4:10:00 · compressed ~30× (2 min)
- **Camera:** WS · 28 mm · behind the corvettes (drone camera)
- **Action:** Ahead, cold hides crack open on the rocks and drones pour out. The corvettes fan out to meet them, their own drones ahead.
- **Comms:** NORMANDY: “Drones waking on the rocks. Dozens.”
- **Doctrine:** HO4, D6, O7
- **VFX:** Drone swarms (swarm system)
- **Rig:** none
- **Assets:** CV (new), DRN-C (new), DRN-L (new), FX-SWARM (new), BRK (new), SUB (new)
- **Sound:** A rising whine in the score.
- **Render class:** C · **Map:** B

### 24. Return to sender

- **Film:** 1:32.0–1:36.0 (4 s), frames 2209–2304
- **Mission:** T+4:14:00 · 1:1
- **Camera:** HUD insert · the Extenuating Circumstances' plot (HUD insert)
- **Action:** A block of drone tracks flips from red to teal: the drones still on a control link are hijacked and turned on their own swarm. The control craft behind the rocks is found and dazzled; the Canterbury's drifting drones are picked up. The autonomous drones keep coming. Tag: NET DEGRADED · DIRECT LINKS.
- **Comms:** EXTENUATING: “Return to sender.”
- **Doctrine:** O5, HD9, D10
- **VFX:** HUD, EW overlay
- **Rig:** none
- **Assets:** HUD (new), FX-EW (new), SUB (new)
- **Sound:** Clipped data chatter.
- **Render class:** E · **Map:** B

### 25. Normandy

- **Film:** 1:36.0–1:39.0 (3 s), frames 2305–2376
- **Mission:** T+4:25:00 · 1:1
- **Camera:** Tracker · 300 mm · from the Wallfish (tracker)
- **Action:** One autonomous drone slips the screen and dives on the Normandy. A plasma bomb goes off against its flank and the corvette breaks up. Its channel dies to hiss.
- **Comms:** WALLFISH: “One's through—on Normandy!”
- **Doctrine:** HO4
- **VFX:** Plasma-bomb flash, break-up
- **Rig:** break 0→1 (new)
- **Assets:** CV (new), CV-BRK (new), DRN-C (new), FX-SWARM (new), FX-BREAK (new), SUB (new)
- **Sound:** The dying channel.
- **Render class:** C · **Map:** B

## Act III: Anchor

Turnover into the lee of a rock over Site 1: the sweep, the heat, the fin hit, the frigate, the lance and the broadside.

### 26. Turnover

- **Film:** 1:39.0–1:45.0 (6 s), frames 2377–2520
- **Mission:** T+4:34:10 · rotation at ~4×, the middle of the 49 s flip cut out
- **Camera:** WS · 24 mm · on the dorsal hull looking aft (hull camera)
- **Action:** Under smoke and an EW peak, one ship at a time, the fleet flips. The stars wheel over the hull as the stern swings toward Maren; now the bow points screen left while the ship still travels right. The drive lights: 34 minutes of braking toward Anchor.
- **Comms:** ACTUAL: “Normandy's gone. Turnover, one at a time.”
- **Doctrine:** D8, O8
- **VFX:** Main plume, RCS, smoke screen
- **Rig:** rcs_bow / rcs_stern pulses; engine_throttle 0→1
- **Assets:** EN (extend), FX-SMOKE (new), SUB (new)
- **Sound:** RCS thumps, then the drive's roar through the hull.
- **Render class:** A · **Map:** B

### 27. Anchor

- **Film:** 1:45.0–1:48.0 (3 s), frames 2521–2592
- **Mission:** T+5:08:00 · 1:1
- **Camera:** HUD insert · the master plot, zoomed (HUD insert)
- **Action:** Anchor, an 18 km rock, with its shadow cone pointing away from Site 1. The fleet will string out along it; two nearby rocks are tagged '?'. Corner readout: ENDEAVOR SINK 94 %.
- **Comms:** ACTUAL: “Into Anchor's lee.”
- **Doctrine:** D5, D2
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones.
- **Render class:** E · **Map:** C

### 28. The sweep

- **Film:** 1:48.0–1:52.0 (4 s), frames 2593–2688
- **Mission:** T+5:09:00 · compressed ~20× (minutes)
- **Camera:** WS · 24 mm · low over Anchor's surface (drone camera)
- **Action:** The Endeavor settles into darkness in the lee; the rock blocks the sun as well as Site 1. Corvettes and drones sweep the rock: a drone trips a mine on the far side, and the flash lights Anchor's limb from behind. Far off, the Donnager's shells land on the nearest rocks.
- **Comms:** DONNAGER: “Clear inside three hundred. Working outward.”
- **Doctrine:** O8, D6, O4
- **VFX:** Mine flash behind the limb, distant impacts
- **Rig:** rcs_bow / rcs_stern pulses
- **Assets:** EN (extend), ANCHOR (new), BRK (new), CV (new), DRN-L (new), GI (new), GI-GUN (new), FX-NUKE (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** C

### 29. Too hot

- **Film:** 1:52.0–1:56.0 (4 s), frames 2689–2784
- **Mission:** T+5:12:00 · compressed 5× (the fins take ~20 s)
- **Camera:** MS · 35 mm · on the stern shoulder (hull camera)
- **Action:** Heat alarms. The slot doors slide open and all four fins telescope out, glowing orange against black: the only light in the lee.
- **Comms:** ENDEAVOR: “Sink ninety-four. Dumping heat.”
- **Doctrine:** D3, D5
- **VFX:** Fin glow, light spill
- **Rig:** fin_* 0→1 (new); heat 1.9→2.4; radiator_glow
- **Assets:** EN (extend), EN-FIN (extend), SUB (new)
- **Sound:** Alarm tones; the fins' hydraulic groan.
- **Render class:** A · **Map:** C · **Reference frame:** `img/lookaft_s1combat.jpg`

### 30. Fins in

- **Film:** 1:56.0–2:00.0 (4 s), frames 2785–2880
- **Mission:** T+5:13:00 · compressed ~4× (the fins crawl in against a 16 s flight)
- **Camera:** MS · 35 mm · the same shoulder, the clock large (hull camera)
- **Action:** A flash on a rock 400 km off the port quarter, a half-second glimpse of the platform. The fins start in, crawling against the clock.
- **Comms:** ENDEAVOR: “Launch, four hundred! Fins in!”
- **Doctrine:** HO7, HO1, D3
- **VFX:** Distant muzzle flash
- **Rig:** fin_* 1→0.5 (new)
- **Assets:** EN (extend), EN-FIN (extend), EMP-RG (new), SUB (new)
- **Sound:** The call; alarms; the fins' groan.
- **Render class:** A · **Map:** C

### 31. Fin hit

- **Film:** 2:00.0–2:03.0 (3 s), frames 2881–2952
- **Mission:** T+5:13:16 · 1:1
- **Camera:** CU · 50 mm · on the port fin (hull camera)
- **Action:** Halfway in, the port fin takes a slug. It shatters into glowing shards and its coolant flashes to glittering ice.
- **Comms:** ENDEAVOR: “Port fin's gone. Cut it loose.”
- **Doctrine:** HO7, D7
- **VFX:** Fin shatter, coolant venting
- **Rig:** fin_port_state → pre-fractured (new)
- **Assets:** EN (extend), EN-FIN (extend), FX-FIN (new), FX-VENT (new), FX-SLUG (new), SUB (new)
- **Sound:** Metal shear through the hull; a hiss.
- **Render class:** A2 · **Map:** C

### 32. Off the port bow

- **Film:** 2:03.0–2:07.0 (4 s), frames 2953–3048
- **Mission:** T+5:13:30 · 1:1
- **Camera:** Hull camera · 600 mm · on the Endeavor's port side (hull camera)
- **Action:** A Compact frigate clears a moonlet 45 km off the port bow and fires its coilgun. Two seconds later the camera shakes as the slug spalls the port belt.
- **Comms:** DONNAGER: “Frigate, off your port bow!”
- **Doctrine:** HO6, O6
- **VFX:** Coilgun flash, hull spall
- **Rig:** dmg_belt 0→1 (new)
- **Assets:** CF (new), ANCHOR (new), EN (extend), EN-DMG (extend), FX-SLUG (new), SUB (new)
- **Sound:** The hit through the hull.
- **Render class:** A2 · **Map:** C

### 33. Lance channels

- **Film:** 2:07.0–2:09.0 (2 s), frames 3049–3096
- **Mission:** T+5:13:53 · 1:1
- **Camera:** CU · 28 mm · the Endeavor's nose (hull camera)
- **Action:** The four lance channels in the nose glow violet-white as the field builds.
- **Comms:** ENDEAVOR: “Lance. Now.”
- **Doctrine:** O12
- **VFX:** Lance core glow
- **Rig:** lance_power 0→1
- **Assets:** EN (extend), SUB (new)
- **Sound:** A rising electric whine through the hull.
- **Render class:** A · **Map:** C

### 34. Lance

- **Film:** 2:09.0–2:11.0 (2 s), frames 3097–3144
- **Mission:** T+5:13:55 · 1:1
- **Camera:** Tracker · 1,000 mm · on the frigate, 40 km out (tracker)
- **Action:** The ship's field reaches out and a spear of plasma runs from the nose to the frigate, forty kilometres off, well inside the ~50 km the field can hold. The frigate's midsection opens; escape pods scatter as it breaks.
- **Doctrine:** O12, O6
- **VFX:** Field-held plasma jet, break-up
- **Rig:** break 0→1 (new)
- **Assets:** CF (new), FX-LANCE (new), FX-BREAK (new), FX-VENT (new)
- **Sound:** A crack in the score.
- **Render class:** C · **Map:** C

### 35. Broadside

- **Film:** 2:11.0–2:17.0 (6 s), frames 3145–3288
- **Mission:** T+5:14:00 · the roll at 5× (3 s), then 1:1 (3 s)
- **Camera:** MS · 35 mm · the port batteries, the rock beyond (hull camera)
- **Action:** Fins stowed, the Endeavor rolls to bring its port batteries onto the platform's rock off the port quarter. The dorsal well battery rises; the M-1Cs wake, charge and fire in sequence, and only the gun that fired vents.
- **Comms:** ENDEAVOR: “Batteries up. Fire.”
- **Doctrine:** O6, O4, D3
- **VFX:** M-1C tracer blasts
- **Rig:** rail_traverse; rail_elevation; battery_raise 0→1; battery_traverse; battery_elevation; rail_wake; rail_lock; rail_arm; charge_a/b; shot_a/b; fins_a/b; heat_a/b
- **Assets:** EN (extend), M1C (extend), SUB (new)
- **Sound:** Each shot's crack and recoil clunk through the hull.
- **Render class:** A2 · **Map:** C · **Reference frame:** `img/house_s1combat.jpg`

### 36. The platform dies

- **Film:** 2:17.0–2:19.0 (2 s), frames 3289–3336
- **Mission:** T+5:14:31 · the clock jumps 13 s (16 s of flight)
- **Camera:** Tracker · 1,200 mm · the glimpse's framing (tracker)
- **Action:** The platform's rock flashes: sixteen seconds of flight, and a target that could not move.
- **Doctrine:** O4
- **VFX:** Impact flash
- **Rig:** none
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new)
- **Sound:** The score.
- **Render class:** B · **Map:** C

## Act IV: Hammer and anvil

Across to Breakwater: Skerry's net, Site 1's fire, Breakwater's missiles at the last net ship, the spend wave, the kill wave, the Casaba jets, the hail and the spinal shot, then terms.

### 37. The fire plan

- **Film:** 2:19.0–2:24.0 (5 s), frames 3337–3456
- **Mission:** T+5:40:00 · 1:1
- **Camera:** HUD insert · the master plot (HUD insert)
- **Action:** The plan on the plot: where Breakwater will be at T+7:52, the waves' straight tracks from Anchor, and the Astrid's firing point 10,800 km out, 15° off Breakwater's zenith. Every line of fire clears Maren. The pack stays at Anchor as a fire base. Four labels: SPEND 7:52 · KILL 7:53; RESERVE ~700; FIRING LINE 15°; 2 FRIGATES · LIMB. The corner readout adds PARK HOLDING under SINK 31 % · FINS 3/4.
- **Comms:** ACTUAL: “That's the plan. Pack holds Anchor. The rest, with me.”
- **Doctrine:** O9, O3, O10, O11, HO6, HO8, D11
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones; the score gathers.
- **Render class:** E · **Map:** D

### 38. The net

- **Film:** 2:24.0–2:29.0 (5 s), frames 3457–3576
- **Mission:** T+6:40:00 · compressed ~24× (2 min)
- **Camera:** WS · 50 mm · over the Extenuating Circumstances (drone camera)
- **Action:** Hours after Skerry threw them, its rounds arrive. Ahead of the fleet the destroyer's drones light up a spreading cloud of pellets about 20 km across, glittering in their lamps. The fleet side-steps, drives angled off the line.
- **Comms:** EXTENUATING: “Skerry's rounds. Right on time.” / ACTUAL: “All ships, left two degrees.”
- **Doctrine:** HO3, D4, O8
- **VFX:** Canister cloud glitter (swarm system)
- **Rig:** none
- **Assets:** DD (new), DRN-L (new), FX-SWARM (new), SUB (new)
- **Sound:** Silence; the score ticks.
- **Render class:** B · **Map:** D

### 39. Site One

- **Film:** 2:29.0–2:33.0 (4 s), frames 3577–3672
- **Mission:** T+6:55:00 · compressed ~15× (a minute)
- **Camera:** WS · 40 mm · ahead of the Extenuating Circumstances (drone camera)
- **Action:** Site 1's beam, invisible, finds the fleet. The destroyer's forward sensor boom scorches and smokes: the one visible cost. The fleet doesn't fire back, since every laser shot would heat the sinks. The ships begin a slow roll to spread the heat, and a grey smoke screen blooms ahead of the fleet, travelling with it.
- **Comms:** EXTENUATING: “Site One's on our booms. Smoke forward.”
- **Doctrine:** HO5, D1, D3
- **VFX:** Scorching, smoke screen
- **Rig:** none
- **Assets:** DD (new), FX-SMOKE (new), FX-DAZZLE (new), SUB (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** D

### 40. The anvil

- **Film:** 2:33.0–2:37.0 (4 s), frames 3673–3768
- **Mission:** T+7:25:00 · compressed 10× (the ripple takes ~40 s)
- **Camera:** WS · 40 mm · above Breakwater, Maren's night side below (drone camera)
- **Action:** Breakwater's reveal. Its turrets track the fleet but stay silent: the fleet never comes within the range they could hit. Its 64 cells open and ripple-fire, every missile at the Extenuating Circumstances, 17,000 km off. Far along the orbit, ring stations wake as points of light.
- **Comms:** ASTRID: “Sixty-four inbound. All on Extenuating.”
- **Doctrine:** HD7, HO9, HD1, HO1, D1
- **VFX:** Cell doors, missile launch (swarm system)
- **Rig:** turret_traverse / cells_open (new)
- **Assets:** BW (new), RING (new), MAREN (extend), MSL-V (new), FX-SWARM (new), SUB (new)
- **Sound:** A low brass sting.
- **Render class:** C · **Map:** E

### 41. The pack fires

- **Film:** 2:37.0–2:41.0 (4 s), frames 3769–3864
- **Mission:** T+7:27:00 · 1:1
- **Camera:** WS · 24 mm · low over Anchor, looking toward Breakwater (drone camera)
- **Action:** From Anchor's shadow the Infinity ripple-fires everything it has left: the spend wave, hundreds of plumes streaming away toward Breakwater, 118,000 km off.
- **Comms:** ACTUAL: “Spend wave, go.” / INFINITY: “Spend wave away. We're dry.”
- **Doctrine:** O3, O11
- **VFX:** Ripple launch (swarm system)
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), ANCHOR (new), SUB (new)
- **Sound:** Silence; the score drops out.
- **Render class:** C · **Map:** D

### 42. Kill wave away

- **Film:** 2:41.0–2:44.0 (3 s), frames 3865–3936
- **Mission:** T+7:28:30 · 1:1
- **Camera:** Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow (tracker)
- **Action:** Ninety seconds behind the spend wave, pod doors open down the Galactica's hull and the kill wave leaves: Casaba killers, EW missiles and decoys. In the foreground the Pillar of Autumn's pods stay shut: the reserve.
- **Comms:** GALACTICA: “Kill wave away.”
- **Doctrine:** O3, O10, O11
- **VFX:** Ripple launch (swarm system)
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), ANCHOR (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** D

### 43. Umbrella

- **Film:** 2:44.0–2:47.0 (3 s), frames 3937–4008
- **Mission:** T+7:31:00 · 1:1
- **Camera:** Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 20 km above (tracker)
- **Action:** Breakwater's missiles arrive. Above the destroyer the braking Astrid's lenses glow violet and its CIWS lay kill clouds across the missiles' path. The flashes walk in toward the Extenuating and stop short.
- **Comms:** EXTENUATING: “Sixty-four down. Thanks, Actual.”
- **Doctrine:** D1, D2, D10, HO9
- **VFX:** Kill clouds, intercept flashes, lens glow, the Astrid's drive plume
- **Rig:** ciws_phase / ciws_fire (new, on the Astrid)
- **Assets:** AST (new), MSL-V (new), FX-PD (new), FX-SWARM (new), FX-FAR (new), SUB (new)
- **Sound:** Silence; the score's pulse.
- **Render class:** C · **Map:** E

### 44. Blind it

- **Film:** 2:47.0–2:50.0 (3 s), frames 4009–4080
- **Mission:** T+7:50:00 · 1:1
- **Camera:** MS · 35 mm · the Endeavor's laser arrays (hull camera)
- **Action:** The Extenuating Circumstances floods the ring's links. Every array in the fleet turns on Breakwater's optics and Site 1's trackers: lenses violet, beams invisible.
- **Comms:** EXTENUATING: “Their net's down.” / ENDEAVOR: “All arrays, dazzle.”
- **Doctrine:** O5, HD9
- **VFX:** Lens glow, EW overlay on inserts
- **Rig:** laser_power 1; laser_traverse; laser_elevation
- **Assets:** EN (extend), FX-EW (new), SUB (new)
- **Sound:** The lenses' capacitor whine through the hull.
- **Render class:** A · **Map:** E · **Reference frame:** `img/lookyoke_final.jpg`

### 45. The spend wave

- **Film:** 2:50.0–2:53.0 (3 s), frames 4081–4152
- **Mission:** T+7:52:00 · 1:1
- **Camera:** Tracker · 800 mm · from the Astrid, over Maren's limb (tracker)
- **Action:** Over the limb, a sparkle: the spend wave dying against Breakwater's point defence, which lights up and gives away every battery. On the plot, the destroyer steers the kill wave around them.
- **Doctrine:** O3, O5, HD5
- **VFX:** Distant PD sparkle
- **Rig:** none
- **Assets:** BW (new), FX-PD (new), MAREN (extend)
- **Sound:** The score.
- **Render class:** D · **Map:** E

### 46. Wall of fire

- **Film:** 2:53.0–2:57.0 (4 s), frames 4153–4248
- **Mission:** T+7:53:28 · slowed 5× (the wave arrives within ~1 s)
- **Camera:** WS · 40 mm · above Breakwater (drone camera)
- **Action:** The kill wave arrives in the same second, nose-on to Breakwater, from the rock's side. Tracers and dying decoys fill the sky; the hardened noses keep coming.
- **Comms:** GALACTICA: “Kill wave. Three, two—”
- **Doctrine:** O3, HD5, O9
- **VFX:** Tracer streams, intercept flashes, swarm
- **Rig:** none
- **Assets:** BW (new), FX-PD (new), FX-SWARM (new), MSL-V (new), SUB (new)
- **Sound:** A dense crackle in the score; no air, no bangs.
- **Render class:** C · **Map:** E

### 47. Casaba

- **Film:** 2:57.0–3:01.0 (4 s), frames 4249–4344
- **Mission:** T+7:53:30 · slowed 3×
- **Camera:** WS · 35 mm · off Breakwater's quarter (drone camera)
- **Action:** Two kilometres out, the surviving Casaba charges fire: nuclear jets lance into Breakwater's drive bells and its engines go dark. The monitor is whole, but it can no longer move.
- **Comms:** ASTRID: “Spears in. Her drive's dark.”
- **Doctrine:** O10
- **VFX:** Casaba jets, drive breach, venting
- **Rig:** drive_glow 1→0 (new); vent (new)
- **Assets:** BW (new), BW-BRK (new), FX-CASABA (new), FX-VENT (new), SUB (new)
- **Sound:** White noise, then silence.
- **Render class:** C · **Map:** E

### 48. The hail

- **Film:** 3:01.0–3:06.0 (5 s), frames 4345–4464
- **Mission:** T+7:54:00 · 1:1
- **Camera:** MS · 50 mm · slow push on Breakwater over the night side (drone camera)
- **Action:** Breakwater hangs dead-engined over Maren's night side, venting from the spear wounds, its turrets still tracking. On an open channel the Astrid hails it. No answer comes.
- **Comms:** ACTUAL: “Breakwater, you can't move. Strike, or we fire.”
- **Doctrine:** O10
- **VFX:** Venting
- **Rig:** vent (new)
- **Assets:** BW (new), BW-BRK (new), MAREN (extend), FX-VENT (new), SUB (new)
- **Sound:** Silence where the answer should be.
- **Render class:** B · **Map:** E

### 49. Spinal

- **Film:** 3:06.0–3:09.0 (3 s), frames 4465–4536
- **Mission:** T+7:54:37 · 1:1 (the last degree of the slew; it fires at T+7:54:40)
- **Camera:** EWS · 200 mm · the Astrid end-on (drone camera)
- **Action:** The Astrid, stopped 10,800 km out and 15° off Breakwater's zenith so a miss would clear Maren, settles its last degree and fires.
- **Comms:** ACTUAL: “Fire.”
- **Doctrine:** O4, O10, HD7, O9
- **VFX:** Spinal muzzle bloom
- **Rig:** spinal_shot (new)
- **Assets:** AST (new), FX-SPINAL (new), SUB (new)
- **Sound:** Everything drops out.
- **Render class:** B · **Map:** E

### 50. Three minutes

- **Film:** 3:09.0–3:13.0 (4 s), frames 4537–4632
- **Mission:** T+7:54:40 · compressed 45× (180 of the slug's 184 s; the clock races)
- **Camera:** WS · 35 mm · the Casaba shot's angle (drone camera)
- **Action:** Hold on the crippled monitor, turrets swinging uselessly, while the clock races through the slug's three minutes.
- **Comms:** ASTRID: “Impact in three minutes.”
- **Doctrine:** O10
- **VFX:** Venting
- **Rig:** turret_traverse (new)
- **Assets:** BW (new), BW-BRK (new), SUB (new)
- **Sound:** Silence; one held note.
- **Render class:** B · **Map:** E

### 51. Impact

- **Film:** 3:13.0–3:16.0 (3 s), frames 4633–4704
- **Mission:** T+7:57:44 · 1:1
- **Camera:** WS · 35 mm · the Casaba shot's angle (drone camera)
- **Action:** The slug arrives amidships, near the spear damage: a white flash, a spall cone, and Breakwater's back breaks in a chain of secondary flashes.
- **Doctrine:** O4
- **VFX:** Impact, spall, section break
- **Rig:** break 0→1 (new)
- **Assets:** BW (new), BW-BRK (new), FX-SPINAL (new), FX-BREAK (new)
- **Sound:** One deep boom on the cut.
- **Render class:** C · **Map:** E

### 52. Heat

- **Film:** 3:16.0–3:20.0 (4 s), frames 4705–4800
- **Mission:** T+8:00:00 · 1:1
- **Camera:** MS · 35 mm · along the Endeavor's scorched port flank (hull camera)
- **Action:** The Endeavor's sink reads 98 %. A valve opens and a thousand tonnes of water boil out in a white plume streaming off the ship: twenty-five minutes of margin.
- **Comms:** ENDEAVOR: “Sink ninety-eight. Dump the water.”
- **Doctrine:** D3, D7
- **VFX:** Water-dump plume
- **Rig:** water_dump 0→1 (new)
- **Assets:** EN (extend), EN-PD (extend), FX-VENT (new), SUB (new)
- **Sound:** A roar through the hull, then a long hiss.
- **Render class:** A2 · **Map:** E

### 53. Terms

- **Film:** 3:20.0–3:25.0 (5 s), frames 4801–4920
- **Mission:** T+8:10:00 · 1:1
- **Camera:** Tracker · 2,000 mm · from the Endeavor's standoff (tracker)
- **Action:** Far off, 8,500 km away, Breakwater's wreck is a glittering smear venting over the night side. On the last plot two channels stay dark: Canterbury, Normandy.
- **Comms:** EXTENUATING: “Actual, Maren's asking for terms.” / ACTUAL: “Site One goes dark first.”
- **Doctrine:** 
- **VFX:** Distant wreck, HUD tag
- **Rig:** none
- **Assets:** BW-BRK (new), MAREN (extend), HUD (new), SUB (new)
- **Sound:** The score, low.
- **Render class:** D · **Map:** E

### 54. Hold

- **Film:** 3:25.0–3:34.0 (9 s), frames 4921–5136
- **Mission:** T+8:24:00 · 1:1
- **Camera:** EWS · 35 mm · locked off, the Endeavor end-on (drone camera)
- **Action:** On Maren's night side a cluster of lights goes dark: Site 1. The Endeavor, end-on, runs out its three fins (already part-way out) into a broken cross glowing orange against the night side, the stump where the fourth was. Cut to black.
- **Comms:** ENDEAVOR: “Site One's dark.” / ACTUAL: “Nauvoo, bring the shields in. T-SEC, the sky's yours.”
- **Doctrine:** D3
- **VFX:** Fin glow, city lights going out
- **Rig:** fin_starboard / fin_dorsal / fin_ventral 0.5→1 (new); heat 2.4; radiator_glow
- **Assets:** EN (extend), EN-FIN (extend), MAREN (extend), WORLD (extend), SUB (new)
- **Sound:** The score resolves; then silence.
- **Render class:** B · **Map:** E · **Reference frame:** `img/hero_s1combat.jpg`
