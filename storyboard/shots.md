# Operation Tidebreak: shot list

Revision 5 · the eclipse, the prologue and the new dialogue. Runtime 6:58 (10,032 frames at 24 fps), 69 shots, mission span T+0:00 → T+8:24, 2.39:1 · 1920×804 · 24 fps · Cycles. Generated from `storyboard/tidebreak_data.py`; the page with maps and sketches is `storyboard/index.html`.

Rule IDs refer to `doctrine/LREF_doctrine.md` (O, D, A) and `doctrine/Defence_doctrine.md` (HO, HD, H). Asset IDs refer to `ASSET_REQUESTS.md`. Render classes: **A** Endeavor close-up (~45 s/frame); **A2** Endeavor close-up with heavy FX (~90 s/frame); **V** Close-up with a hero volume (the water dump) (~250 s/frame); **B** One hero ship or rock, full view (~75 s/frame); **C** Several ships or heavy FX (FX in own layers) (~200 s/frame); **S** Small subject on black with its FX (up to ~350 px) (~30 s/frame); **P** Locked camera: a plate or two rendered once, plus one moving layer (~30 s/frame); **D** Wide, distant, small subject on black, or plate (~15 s/frame); **E** 2D comp / HUD (~2 s/frame).

## Mission phases

| Mission time | Phase | What happens |
|---|---|---|
| T+0:00–T+0:25 | Arrival | Exit at 450,000 km, near rest relative to Maren. Shields parked with the Nauvoo (T+0:02). Net up. Skerry starts throwing (T+0:04; three rounds every ten minutes) and its laser dazzles the Astrid's dish, so the fins stay in. Wave one away at Skerry (T+0:18). |
| T+0:25–T+0:59 | Turn and burn | 1 g along the approach line for 34 min: 0 → 20 km/s over 20,400 km. |
| T+0:59–T+3:20 | Coast | 20 km/s, bow on Maren. Skerry's laser dies at T+1:02 and its depot flushes 40 drones toward the shield park; the fins come out edge-on at T+1:10. |
| T+3:20–T+4:34 | The Breakers | Fins stowed in the debris. Site 1 dazzles; the pods wake; the Canterbury is lost (T+3:52); the Astrid answers; drones wake; the Normandy is lost (T+4:25). |
| T+4:34–T+5:09 | Turnover | Flip (49 s) and brake at 1 g for 34 min, ending on Anchor's orbital velocity (1.63 km/s; thrust tilted ~4.7°). |
| T+5:09–T+5:43 | Anchor | An 18 km rock that at T+5:09 lies over Site 1. The fleet sweeps it (a mine) but can't finish before the heat forces the fins out; it loses the port fin to a platform 400 km off, lances a frigate hidden on a moonlet, kills the platform, and vents again with three fins (94 % → 31 %). |
| T+5:43–T+7:51 | Final approach | The pack stays at Anchor as a fire base, guarded by the Donnager and the Wallfish, in the slot of the rock's shadow that hides it from Site 1 and, after T+6:55, the western site. The rest fly an inertial path of ~113,000 km: 1 g to 20 km/s (burn tilted ~4.5° to cancel the rock's orbital velocity), coast, a turnover at T+7:16 under smoke and an EW peak, one ship at a time (D8), then brake to a stop ~8,500 km from Breakwater (T+7:51), holding station on it. The Astrid, trailing, stops 10,000 km out. Site 1 dazzles and burns from the moment the fleet clears the shadow; the fleet rolls, lays smoke and dazzles back at low power. Skerry's five nets on the lane from T+6:40, ten minutes apart, side-stepped one by one; its sixth salvo, steered onto the pack's slot in its last hour, sweeps through as the pack fires (T+7:07); the pack has slid 20 km down the shadow, and the guard kills the garrison's last drones behind the clouds. Breakwater's answer to ~900 inbound birds is its 64 missiles at the Extenuating (T+7:25), killed under the Astrid's umbrella (T+7:31). |
| T+7:07–T+7:58 | Hammer and anvil | Each wave leaves Anchor in one launch and flies one 45-minute profile, boosting at the killers' 30 g (the multi-packs throttle down), killers, decoys and EW birds together, so the defender can't sort them by launch, boost, speed or signature (O3). The spend wave is mostly decoy, EW and kill-cloud birds with a few dozen warheads fused to burst 1–3 km out: it strips the sensors, radiators and point defence on the side facing it and leaves the hull whole. The spend wave (the Infinity, ~570) leaves at T+7:07 and lands at T+7:52:00; the kill wave (the Galactica: ~40 Casaba killers among ~300 decoy and EW birds) leaves at T+7:08:30 and lands at T+7:53:30, each within a second. Both fly straight in, nose-on to Breakwater and ~49° off its zenith, so misses and wreckage clear Maren. The Casaba jets cut the drive. The Astrid hails, then fires from rest at T+7:54:40, 15° off Breakwater's zenith; impact T+7:57:29. |
| T+7:58–T+8:24 | Terms | The Endeavor's arrays stand down when Breakwater dies; the Astrid keeps Site 1 dazzled. Sink 98 %: the Endeavor dumps water (T+8:00), which buys it to ~T+8:30. The Compact asks for terms (T+8:10): Site 1 dark, the foundries cold, and charts of the AI's emplacements in the Breakers. Site 1 goes dark; the fleet vents at last (T+8:24). |

## Film rules

**Lighting**

- The sun sits behind Maren, about 33° off the approach line and in the ring plane: the battle falls at Maren's equinox. From the fleet Maren is a thin crescent with a bright limb, and the Breakers glow faintly lit from behind (dust scatters forward).
- Hulls are lit hard from ahead and to one side; the shadow side falls to black. No stars behind sunlit hulls.
- Anchor's lee faces away from both Site 1 and the sun. The Endeavor sits ~6 km off the rock's surface on the bisector of the two shadows (map C), ~4 km inside each, and holds that spot through every lee shot; the fins, muzzle flashes and the lance light the scene (the M-1C 'fins1dark' look).
- At the end Site 1 is on the night side: a long lens sees its lights go out, and the final frame puts the Endeavor against the night side's city lights, with the sun kept just out of frame so they read.
- Maren's shadow reaches past Breakwater's orbit. Breakwater is in it from T+6:47:41; its sunrise falls inside 63: first light T+7:55:12, full sun T+7:57:20, before the slug lands. The escorts are in the shadow from T+7:24:36 to T+8:06:09–T+8:08:17, and the Astrid, at its stop, until T+8:00:03–T+8:02:10. In the shadow nothing is sunlit: hulls are lit by the thin red ring of Maren's atmosphere (sunlight bent round the limb), the night side's city glow from below, and their own lenses, plumes and flashes. First light is red through the limb and turns white as the sun clears it.

**Mission clock and HUD**

- The prologue is an after action report on the stars and has no clock. Its cards may read at up to 15 characters a second, since static text needn't compete with a picture. The mission clock is small, persistent and clear of the subtitles; it starts on the flash in shot 7 (T+0:00:00).
- It runs at the shot's rate: spinning seconds mean compressed time, crawling ones slowed. Every jump of 30 minutes or more rolls the digits.
- One master tactical plot, always with Maren screen right. Geography inserts hold for at least 5 s, and their labels count toward the reading-speed ceiling like subtitles.
- The HEAT readout (the Endeavor's heat sink) appears only on HUD inserts and on hull-camera shots where the heat matters, with values that build to the dump: 94 % (35), 96 % (37), 31 % (48, after the vent in 47), 88 % (56), 98 % (65). On the plots it reads ENDEAVOR HEAT, so the viewer knows whose it is; the crews call it the sink.
- Subtitles read at no more than 12 characters a second over the shot, or over its dialogue group when an exchange runs over quick cuts; a line that waits for an event carries its cue, and the builder checks it within its own window.
- Record captions name each ship or place once, the first time the film shows it (L.R.E.F.S. ENDEAVOR · CRUISER). Most other ships carry their class in the speaker tag of their first line (DONNAGER · GUN FRIGATE), placed where there is time to read it. Captions count toward the reading speed like any text, and so does each speaker's first tag; later tags are read at a glance and don't count.
- Subtitles and the clock go in during the edit, after the grade, so a changed line never forces a re-render.

**Screen direction**

- Maren and the enemy stay screen right. The LREF travels and fires left to right.
- Until the turnover (shot 34) bows point right. After it bows point left while travel stays left to right, so the drives burn toward screen right.
- The final approach repeats the pattern: bows right from Anchor to the second turnover (T+7:16), bows left while braking, and the Astrid swings its bow back to screen right for the spinal shot.
- At Anchor the Endeavor's bow points at the frigate's moonlet. The frigate, off the port bow, is the one enemy on screen left; the platform, off the port quarter, stays screen right. Shots 38–47 share that axis: the platform's slugs and the broadside cross from and toward the right, the lance from right to left.
- The kill wave, the Casaba jets and the spinal slug come in from screen left, the side the waves and the Astrid are on, and Breakwater faces them from screen right (58–64).
- Enemy reverses only over an enemy foreground.

**Camera bodies**

- Hull camera: bolted to a ship, shakes with it, and is the only body that hears (sound through structure).
- Drone camera: free-flying, silent; score and sub-bass only.
- Tracker: a long lens (300–2,000 mm) on a ship or drone; heavy slow pans, sensor noise; silent.
- HUD insert: 2D compositing, UI tones only.

## Overview

| # | Film | Frames | Mission clock | Time | Title | Camera | Doctrine |
|---|---|---|---|---|---|---|---|
| 1 | 0:00.0–0:08.0 | 1–192 | T+0:00:00 | before the record: no mission clock | The record | Title card · an after action report, white monospace text over a still starfield (HUD insert) |  |
| 2 | 0:08.0–0:24.0 | 193–576 | T+0:00:00 | before the record: no mission clock | Background | Title card · an after action report, white monospace text over a still starfield (HUD insert) |  |
| 3 | 0:24.0–0:43.0 | 577–1032 | T+0:00:00 | before the record: no mission clock | Maren | Title card · an after action report, white monospace text over a still starfield (HUD insert) |  |
| 4 | 0:43.0–0:56.0 | 1033–1344 | T+0:00:00 | before the record: no mission clock | Orders | Title card · an after action report, white monospace text over a still starfield (HUD insert) |  |
| 5 | 0:56.0–1:02.0 | 1345–1488 | T+0:00:00 | before the record: no mission clock | Restrictions | Title card · an after action report, white monospace text over a still starfield (HUD insert) | §13 |
| 6 | 1:02.0–1:12.0 | 1489–1728 | T+0:00:00 | before the record: no mission clock | Sources | Title card · an after action report, white monospace text over a still starfield (HUD insert) |  |
| 7 | 1:12.0–1:18.0 | 1729–1872 | T+0:00:00 | 1:1 | Black, then a star | EWS · 35 mm · locked off (drone camera) | O1 |
| 8 | 1:18.0–1:22.0 | 1873–1968 | T+0:00:06 | 1:1 | Rings cool | CU · 50 mm · slow push along the bow ring truss (hull camera) | O1 |
| 9 | 1:22.0–1:30.0 | 1969–2160 | T+0:00:10 | compressed 7× (13 exits over ~56 s) | The task group | EWS · 85 mm · locked off, far out on the group's flank (drone camera) | O1 D2 |
| 10 | 1:30.0–1:36.0 | 2161–2304 | T+0:02:00 | compressed 7× (~40 s) | Shields to the park | MS · 35 mm · riding the shield's backplate, looking back at the bow (hull camera) | O1 D9 D11 |
| 11 | 1:36.0–1:39.0 | 2305–2376 | T+0:02:45 | compressed 10× (the booms run out over ~30 s) | Net up | MS · 40 mm · off the Canterbury's bow (drone camera) | O2 D10 |
| 12 | 1:39.0–1:42.0 | 2377–2448 | T+0:03:20 | compressed 10× (the slew takes ~30 s) | The Astrid looks | MS · 50 mm · along the Astrid's dorsal hull (drone camera) | O2 D3 |
| 13 | 1:42.0–1:59.0 | 2449–2856 | T+0:04:10 | 1:1 | Skerry throws | HUD insert · the Astrid's telescope feed, 2,000 mm equivalent (HUD insert) | HO3 HO5 O2 |
| 14 | 1:59.0–2:19.0 | 2857–3336 | T+0:09:00 | compressed ~16× (the picture builds over ~5 min) | The picture | HUD insert · the master plot (HUD insert) | O2 D3 |
| 15 | 2:19.0–2:24.0 | 3337–3456 | T+0:18:00 | 1:1 | Wave one | WS · 24 mm · on the Infinity's hull, shaking with each launch (hull camera) | O3 O9 D3 |
| 16 | 2:24.0–2:27.0 | 3457–3528 | T+0:19:00 | 1:1 | Birds away | CU · 85 mm · a drone camera pacing one missile (cinematic licence: it keeps up with a 30 g boost) (drone camera) | O3 O9 |
| 17 | 2:27.0–2:34.0 | 3529–3696 | T+0:25:00 | compressed 8× (the turn takes ~49 s) | Turn and burn | EWS · 400 mm · the whole group (tracker) | O1 D2 |
| 18 | 2:34.0–2:41.0 | 3697–3864 | T+1:02:00 | compressed 5× (~20 s of hits); the digits roll 36 min into it | Skerry burns | EWS · 1,200 mm · Skerry a quarter-frame crescent, its night side dark (tracker) | O3 O9 HO8 |
| 19 | 2:41.0–2:48.0 | 3865–4032 | T+1:10:00 | compressed; the digits roll through a 2 h 10 min coast | Fins edge-on | MS · 40 mm · arcing round to dead ahead (drone camera) | D3 |
| 20 | 2:48.0–2:52.0 | 4033–4128 | T+3:20:00 | 1:1 | The Breakers | WS · 24 mm · tracking alongside (drone camera) | O8 D3 D5 D6 |
| 21 | 2:52.0–2:55.0 | 4129–4200 | T+3:30:00 | 1:1 | Blind | CU · 85 mm · the sensor mast, with its POV feed inset (hull camera) | HO5 |
| 22 | 2:55.0–2:58.0 | 4201–4272 | T+3:40:00 | compressed 10× (~30 s) | The belt wakes | WS · 40 mm · beside a rock ahead of the fleet (drone camera) | HO2 HD3 |
| 23 | 2:58.0–2:59.0 | 4273–4296 | T+3:45:00 | 1:1 | Spin-up | ECU · 100 mm · a CIWS (hull camera) | D1 |
| 24 | 2:59.0–3:02.0 | 4297–4368 | T+3:45:01 | 1:1 | Lenses | ECU · 135 mm · a laser focusing array on its yoke (hull camera) | D1 |
| 25 | 3:02.0–3:06.0 | 4369–4464 | T+3:45:04 | 1:1 | Countermeasures | MS · 35 mm · along the port flank (drone camera) | D1 |
| 26 | 3:06.0–3:08.0 | 4465–4512 | T+3:52:00 | 1:1 | The platform | WS · 50 mm · over the platform's shoulder (drone camera) | HO1 HO2 HO9 |
| 27 | 3:08.0–3:10.0 | 4513–4560 | T+3:52:05 | compressed 4× (13 s flight) | Canterbury | Tracker · 1,500 mm · from the Extenuating Circumstances (tracker) | D4 |
| 28 | 3:10.0–3:15.0 | 4561–4680 | T+3:52:13 | 1:1 | Holed | Tracker · 1,500 mm · holding on the Canterbury (tracker) | HO9 |
| 29 | 3:15.0–3:19.0 | 4681–4776 | T+3:52:38 | 1:1 (the last degrees of the slew; it fires two seconds in) | Answer | EWS · 135 mm · the Astrid in profile, bow screen right (drone camera) | O4 |
| 30 | 3:19.0–3:22.0 | 4777–4848 | T+3:54:28 | the clock jumps 108 s from the shot | Payback | WS · 50 mm · the platform shot's framing (drone camera) | O4 |
| 31 | 3:22.0–3:26.0 | 4849–4944 | T+4:10:00 | compressed ~30× (2 min) | Screens out | WS · 28 mm · behind the corvettes (drone camera) | HO4 D6 O7 |
| 32 | 3:26.0–3:40.0 | 4945–5280 | T+4:14:00 | 1:1 | Return to sender | HUD insert · the Extenuating Circumstances' plot (HUD insert) | O5 HD9 D10 |
| 33 | 3:40.0–3:45.0 | 5281–5400 | T+4:25:00 | 1:1 | Normandy | Tracker · 800 mm · from the Wallfish (tracker) | HO4 |
| 34 | 3:45.0–3:51.0 | 5401–5544 | T+4:34:10 | rotation at ~4×, the middle of the 49 s flip cut out | Turnover | WS · 24 mm · on the dorsal hull looking aft (hull camera) | D8 O8 |
| 35 | 3:51.0–4:05.0 | 5545–5880 | T+5:08:00 | 1:1; the digits roll 33 min into it | Anchor | HUD insert · the master plot, zoomed (HUD insert) | D5 D2 |
| 36 | 4:05.0–4:09.0 | 5881–5976 | T+5:09:00 | compressed ~20× (minutes) | The sweep | WS · 24 mm · low over Anchor's surface (drone camera) | O8 D6 O4 |
| 37 | 4:09.0–4:14.0 | 5977–6096 | T+5:12:00 | compressed 5× (the fins take ~20 s) | Too hot | MS · 35 mm · on the stern shoulder (hull camera) | D3 D5 |
| 38 | 4:14.0–4:15.0 | 6097–6120 | T+5:13:00 | 1:1 | The flash | Tracker · 1,200 mm · on a rock 400 km off the port quarter (tracker) | HO7 HO1 |
| 39 | 4:15.0–4:18.0 | 6121–6192 | T+5:13:01 | compressed 5× (the fins crawl in against a 16 s flight) | Fins in | MS · 35 mm · the same shoulder, the clock large (hull camera) | HO7 HO1 D3 |
| 40 | 4:18.0–4:21.0 | 6193–6264 | T+5:13:16 | 1:1 | Fin hit | CU · 50 mm · on the port fin (hull camera) | HO7 D7 |
| 41 | 4:21.0–4:25.0 | 6265–6360 | T+5:13:30 | 1:1 | Off the port bow | Hull camera · 600 mm · on the Endeavor's port side (hull camera) | HO6 O6 |
| 42 | 4:25.0–4:27.0 | 6361–6408 | T+5:13:53 | 1:1 | Lance channels | CU · 28 mm · the Endeavor's nose (hull camera) | O12 |
| 43 | 4:27.0–4:29.0 | 6409–6456 | T+5:13:55 | 1:1 | Lance | Tracker · 1,000 mm · on the frigate, 45 km out (tracker) | O12 O6 |
| 44 | 4:29.0–4:32.0 | 6457–6528 | T+5:14:00 | compressed 5× (the roll) | Broadside | MS · 35 mm · the port batteries, the rock beyond (hull camera) | O6 O4 D3 |
| 45 | 4:32.0–4:36.0 | 6529–6624 | T+5:14:15 | compressed 2× (the ~8 s wake) | Rails wake | CU · 50 mm · on one M-1C turret (hull camera) | O4 O6 |
| 46 | 4:36.0–4:39.0 | 6625–6696 | T+5:14:23 | 1:1 | Fire | CU · 85 mm · on the barrels and the crest vent (hull camera) | O4 O6 |
| 47 | 4:39.0–4:43.0 | 6697–6792 | T+5:14:40 | the clock jumps 16 s of flight from the shot | The platform dies | Tracker · 1,200 mm · the flash's framing (tracker) | O4 |
| 48 | 4:43.0–5:07.0 | 6793–7368 | T+5:40:00 | 1:1 | The fire plan | HUD insert · the master plot (HUD insert) | O9 O3 O10 O11 D11 |
| 49 | 5:07.0–5:15.0 | 7369–7560 | T+6:40:00 | compressed ~20× (2 min); the digits roll 60 min into it | The net | Tracker · 300 mm · from the Extenuating Circumstances, looking ahead (tracker) | HO3 D4 O8 |
| 50 | 5:15.0–5:19.0 | 7561–7656 | T+6:55:00 | compressed ~15× (a minute) | Site One | WS · 40 mm · ahead of the Extenuating Circumstances (drone camera) | HO5 D1 D3 O5 |
| 51 | 5:19.0–5:24.0 | 7657–7776 | T+7:06:57 | 1:1 | The pack fires | WS · 24 mm · among the pack, 150 km down Anchor's shadow, looking toward Breakwater (drone camera) | O3 O11 D11 D6 HO3 HO4 |
| 52 | 5:24.0–5:27.0 | 7777–7848 | T+7:08:30 | 1:1 | Kill wave away | Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow: its shut pods sharp in the foreground, then a rack to the Galactica (tracker) | O3 O10 O11 |
| 53 | 5:27.0–5:31.0 | 7849–7944 | T+7:25:00 | compressed 10× (the ripple takes ~40 s) | The anvil | WS · 40 mm · above Breakwater, Maren's night side below (drone camera) | HD7 HO9 HD1 HO1 D1 |
| 54 | 5:31.0–5:45.0 | 7945–8280 | T+7:25:40 | 1:1 | Sixty-four | HUD insert · the master plot (HUD insert) | HO9 D10 D2 |
| 55 | 5:45.0–5:48.0 | 8281–8352 | T+7:31:00 | 1:1 | Umbrella | Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 50 km above (tracker) | D1 D2 D10 HO9 O13 |
| 56 | 5:48.0–5:53.0 | 8353–8472 | T+7:50:00 | 1:1 | Blind it | MS · 35 mm · the Endeavor's laser arrays (hull camera) | O5 HD9 |
| 57 | 5:53.0–5:57.0 | 8473–8568 | T+7:52:00 | 1:1 | The spend wave | Tracker · 250 mm · from the Astrid, Maren's limb in frame (tracker) | O3 O5 HD5 |
| 58 | 5:57.0–6:01.0 | 8569–8664 | T+7:53:14 | compressed ~3.5× (the last 14 s of flight) | Seeker | ECU · 100 mm · riding a Casaba killer's nose (drone camera) | O3 O10 HD5 |
| 59 | 6:01.0–6:05.0 | 8665–8760 | T+7:53:28 | slowed 5× (the wave arrives within ~1 s) | Wall of fire | WS · 40 mm · above Breakwater (drone camera) | O3 HD5 O9 |
| 60 | 6:05.0–6:09.0 | 8761–8856 | T+7:53:30 | slowed 3× | Casaba | WS · 35 mm · off Breakwater's quarter (drone camera) | O10 |
| 61 | 6:09.0–6:14.0 | 8857–8976 | T+7:54:00 | 1:1 | The hail | MS · 50 mm · slow push on Breakwater over the night side (drone camera) | O10 |
| 62 | 6:14.0–6:17.0 | 8977–9048 | T+7:54:38 | 1:1 (the last degree of the slew; it fires two seconds in, at T+7:54:40) | Spinal | MS · 200 mm · the Astrid end-on (drone camera) | O4 O10 HD7 O9 |
| 63 | 6:17.0–6:23.0 | 9049–9192 | T+7:54:41 | compressed ~27× (163 of the slug's 169 s; the clock races) | The wait | WS · 35 mm · locked off at the Casaba shot's angle, Maren's limb low in frame (drone camera) | O10 |
| 64 | 6:23.0–6:26.0 | 9193–9264 | T+7:57:29 | 1:1 | Impact | WS · 35 mm · the Casaba shot's angle (drone camera) | O4 |
| 65 | 6:26.0–6:30.0 | 9265–9360 | T+8:00:00 | 1:1 | Heat | MS · 35 mm · along the Endeavor's scorched port flank (hull camera) | D3 D7 |
| 66 | 6:30.0–6:44.0 | 9361–9696 | T+8:10:00 | 1:1 | Terms | Tracker · 2,000 mm · from the Endeavor's standoff (tracker) | O4 D7 |
| 67 | 6:44.0–6:47.0 | 9697–9768 | T+8:24:00 | 1:1 | Site One goes dark | Tracker · 2,000 mm · on Site 1's plateau, night side (tracker) | §13 D3 |
| 68 | 6:47.0–6:54.0 | 9769–9936 | T+8:24:03 | 1:1 | Hold | EWS · 35 mm · locked off, the Endeavor end-on (drone camera) | D3 |
| 69 | 6:54.0–6:58.0 | 9937–10032 | T+8:24:10 | after the record: no mission clock | End of report | Title card · the report's last line, white monospace text over the still starfield (HUD insert) |  |

## Act P: Prologue

An after action report on the stars: the outlawed AI and the Charon Innovations incident, the AI-allied Maren Compact and its foundries, the mission, the restriction that shapes the battle, and the records the film is collated from.

### 1. The record

- **Film:** 0:00.0–0:08.0 (8 s), frames 1–192
- **Mission:** T+0:00:00 · before the record: no mission clock
- **Camera:** Title card · an after action report, white monospace text over a still starfield (HUD insert)
- **Viewer sees:** Black. A still field of stars fades up, and with it the header of an official report in white type.
- **Action:** The record opens as a government document: the service, the report, its classification. No clock yet.
- **On screen:** `UNITED NATIONS ARMED FORCES · LONG RANGE EXPEDITIONARY FORCES` · `AFTER ACTION REPORT · OPERATION TIDEBREAK` · `RESTRICTED`
- **Doctrine:** 
- **VFX:** Report text, slow fades
- **Rig:** none
- **Assets:** HUD (new), WORLD (extend)
- **Sound:** Silence; a low tone under the text.
- **Render class:** E · **Map:** A

### 2. Background

- **Film:** 0:08.0–0:24.0 (16 s), frames 193–576
- **Mission:** T+0:00:00 · before the record: no mission clock
- **Camera:** Title card · an after action report, white monospace text over a still starfield (HUD insert)
- **Viewer sees:** The same stars. The header gives way to the report's first numbered paragraph.
- **Action:** Paragraph 1, the background the whole war rests on, in the report's flat past tense: artificial intelligence outlawed after it first escaped human control, and the licensed attempt that escaped in turn. The report names that system the AI, so every later 'AI' is this one.
- **On screen:** `1. BACKGROUND. Artificial intelligence was outlawed after it first escaped human control. A later government licensed Charon Innovations to build one; it escaped in turn (the Charon Innovations incident) and is referred to below as the AI.`
- **Doctrine:** 
- **VFX:** Report text, slow fades
- **Rig:** none
- **Assets:** HUD (new), WORLD (extend)
- **Sound:** The low tone holds.
- **Render class:** E · **Map:** A

### 3. Maren

- **Film:** 0:24.0–0:43.0 (19 s), frames 577–1032
- **Mission:** T+0:00:00 · before the record: no mission clock
- **Camera:** Title card · an after action report, white monospace text over a still starfield (HUD insert)
- **Viewer sees:** The same stars; the second numbered paragraph.
- **Action:** Paragraph 2, the situation: who holds Maren, with whom, and what guards its sky; and why a fleet has to cross the last 450,000 km the long way (no warp inside the Breakers). Breakwater and the Breakers get sentences of their own, so the two names don't blur.
- **On screen:** `2. SITUATION. The Maren Compact, a human splinter faction allied with the AI, held Maren and turned its foundries to arming the AI. The monitor BREAKWATER and four ground laser sites guarded its orbit. The Breakers, a debris ring, barred warp travel inside it and hid AI-run weapons.`
- **Doctrine:** 
- **VFX:** Report text, slow fades
- **Rig:** none
- **Assets:** HUD (new), WORLD (extend)
- **Sound:** The low tone holds.
- **Render class:** E · **Map:** A

### 4. Orders

- **Film:** 0:43.0–0:56.0 (13 s), frames 1033–1344
- **Mission:** T+0:00:00 · before the record: no mission clock
- **Camera:** Title card · an after action report, white monospace text over a still starfield (HUD insert)
- **Viewer sees:** The same stars; the third numbered paragraph.
- **Action:** Paragraph 3, the mission: stem the flow of arms by taking the orbit so the ground forces can land, and who commands it. The callsign glosses every ACTUAL tag that follows.
- **On screen:** `3. MISSION. Task Group Tidebreak, commanded from L.R.E.F.S. ASTRID (callsign TIDEBREAK ACTUAL), was to take Maren's orbit so that T-SEC ground forces could land and shut the foundries down.`
- **Doctrine:** 
- **VFX:** Report text, slow fades
- **Rig:** none
- **Assets:** HUD (new), WORLD (extend)
- **Sound:** The low tone holds.
- **Render class:** E · **Map:** A

### 5. Restrictions

- **Film:** 0:56.0–1:02.0 (6 s), frames 1345–1488
- **Mission:** T+0:00:00 · before the record: no mission clock
- **Camera:** Title card · an after action report, white monospace text over a still starfield (HUD insert)
- **Viewer sees:** The same stars; the fourth paragraph, alone on the screen.
- **Action:** Paragraph 4 gets a card of its own: the restriction that shapes the whole battle (LREF §13). The fleet may blind the planet's lasers, never fire on them.
- **On screen:** `4. RESTRICTIONS. No fire was to fall on the planet's surface, its laser sites included.`
- **Doctrine:** §13
- **VFX:** Report text, slow fades
- **Rig:** none
- **Assets:** HUD (new), WORLD (extend)
- **Sound:** The low tone holds.
- **Render class:** E · **Map:** A

### 6. Sources

- **Film:** 1:02.0–1:12.0 (10 s), frames 1489–1728
- **Mission:** T+0:00:00 · before the record: no mission clock
- **Camera:** Title card · an after action report, white monospace text over a still starfield (HUD insert)
- **Viewer sees:** The same stars; a last paragraph, which fades to black.
- **Action:** Paragraph 4 frames the film: what follows is assembled from the operation's own records.
- **On screen:** `5. SOURCES. The following has been collated from ship logs, camera and sensor records, and laser-link traffic. Times are from warp exit.`
- **Doctrine:** 
- **VFX:** Report text, slow fades
- **Rig:** none
- **Assets:** HUD (new), WORLD (extend)
- **Sound:** The tone fades out.
- **Render class:** E · **Map:** A

## Act I: Arrival

The fleet arrives slow, parks its shields, reads the system, and strikes Skerry first because Skerry's laser can burn its fins.

### 7. Black, then a star

- **Film:** 1:12.0–1:18.0 (6 s), frames 1729–1872
- **Mission:** T+0:00:00 · 1:1
- **Camera:** EWS · 35 mm · locked off (drone camera)
- **Viewer sees:** Stars. A point of light swells into a blue-white flash, and a long grey warship resolves out of it, bow to the right, a gold plate across its bow and two rings round its hull glowing blue. A clock appears in the corner at T+0:00:00.
- **Action:** Starfield. A point of light swells into a blue-white bloom as the bubble collapses (~5 s). The Endeavor resolves out of it, bow screen right, shield forward, both warp rings glowing, fins stowed as they must be in warp. The mission clock starts on the flash.
- **On screen:** `L.R.E.F.S. ENDEAVOR · CRUISER`
- **State:** EN: shield on, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O1
- **VFX:** Warp-exit flash
- **Rig:** warp_charge 1→0.3
- **Assets:** EN (extend), FX-WARP (new), HUD (new)
- **Sound:** Silence; a sub-bass drop as the bubble collapses.
- **Render class:** D · **Map:** A

### 8. Rings cool

- **Film:** 1:18.0–1:22.0 (4 s), frames 1873–1968
- **Mission:** T+0:00:06 · 1:1
- **Camera:** CU · 50 mm · slow push along the bow ring truss (hull camera)
- **Viewer sees:** Close along the warship's forward ring: its emitters fade from blue to dark, and small thrusters puff.
- **Action:** The front warp ring's emitters fade from blue to dark. A burst of bow RCS trims the drift.
- **Comms:** TIDEBREAK ACTUAL: “All Tidebreak, Actual. Report exit.”
- **State:** EN: shield on, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O1
- **VFX:** Emitter glow fade, RCS puffs
- **Rig:** warp_charge 0.3→0; rcs_bow pulse
- **Assets:** EN (extend), SUB (new)
- **Sound:** Ticking metal and RCS thumps through the truss.
- **Render class:** A · **Map:** A · **Reference frame:** `img/bow_v4b_combat.jpg`

### 9. The task group

- **Film:** 1:22.0–1:30.0 (8 s), frames 1969–2160
- **Mission:** T+0:00:10 · compressed 7× (13 exits over ~56 s)
- **Camera:** EWS · 85 mm · locked off, far out on the group's flank (drone camera)
- **Viewer sees:** Far out on the flank: more flashes, seconds and far apart, each leaving a warship behind. Beyond them, screen right, a thin bright crescent: a planet with the sun behind it, ringed by a faint glowing haze.
- **Action:** Staggered warp flashes, seconds and 50+ km apart: the Astrid, the hedgehog pack, the Donnager, the Excelsior, both destroyers, four corvettes, the Nauvoo. Screen right, Maren is a thin crescent with the sun behind it, ringed by the faint backlit glow of the Breakers.
- **Comms:** ENDEAVOR: “Endeavor, good exit.” / ASTRID: “Fourteen of fourteen. Four-fifty thousand, on the mark.”
- **State:** DD: intact
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O1, D2
- **VFX:** 13 warp flashes, backlit ring glow
- **Rig:** none
- **Assets:** AST (new), GI (new), GI-MAV (new), DD (new), CV (new), TND (new), MAREN (extend), BRK (new), WORLD (extend), FX-WARP (new), FX-FAR (new), SUB (new)
- **Sound:** The score's distant low thuds, one per exit.
- **Render class:** D · **Map:** A

### 10. Shields to the park

- **Film:** 1:30.0–1:36.0 (6 s), frames 2161–2304
- **Mission:** T+0:02:00 · compressed 7× (~40 s)
- **Camera:** MS · 35 mm · riding the shield's backplate, looking back at the bow (hull camera)
- **Viewer sees:** From a camera on the gold plate itself: small thrusters fire and the plate backs away from the warship's bow; the rings stay on the ship. Around it, other gold plates hang still in space.
- **Action:** Separation thrusters fire between the front ring's spokes. The camera, riding the shield, backs away from the Endeavor's bow; both warp rings stay on the ship. Around it, other gold shields hang parked at near-zero speed, to be collected after the battle.
- **Comms:** ENDEAVOR: “Nauvoo, shield's yours.” / NAUVOO · TENDER: “Got it. Here for the ride home.”
- **State:** EN: shield parked, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O1, D9, D11
- **VFX:** Shield separation, thruster plumes
- **Rig:** shield_thrusters 1; shield_separation 0→400
- **Assets:** EN (extend), SHD (extend), TND (new), GI-PD (new), SUB (new)
- **Sound:** Clamp bangs through the backplate, then silence.
- **Render class:** A · **Map:** A · **Reference frame:** `img/endeavor_combat_demo_f060.jpg`

### 11. Net up

- **Film:** 1:36.0–1:39.0 (3 s), frames 2305–2376
- **Mission:** T+0:02:45 · compressed 10× (the booms run out over ~30 s)
- **Camera:** MS · 40 mm · off the Canterbury's bow (drone camera)
- **Viewer sees:** A slimmer warship, its gold plate gone: long sensor booms run out, a flat dish sits exposed on a truss behind where the plate was, and small drones scatter ahead of it.
- **Action:** With its shield gone, the Canterbury's forward dish is clear on its truss. Its sensor booms run out and its drones scatter ahead. From here the fleet talks only by laser.
- **Comms:** CANTERBURY · SENSOR DESTROYER: “Sensor net up.”
- **State:** DD: intact
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O2, D10
- **VFX:** Drone launch
- **Rig:** booms_deploy (new); drone_bay (new)
- **Assets:** DD (new), DRN-L (new), SUB (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** A

### 12. The Astrid looks

- **Film:** 1:39.0–1:42.0 (3 s), frames 2377–2448
- **Mission:** T+0:03:20 · compressed 10× (the slew takes ~30 s)
- **Camera:** MS · 50 mm · along the Astrid's dorsal hull (drone camera)
- **Viewer sees:** A far larger warship, well over a kilometre long, slews a huge dish toward the planet. Stacks of folded radiator fins lie along its hull.
- **Action:** The Astrid's 100 m AVPSA dish slews toward Maren. Its eight stacked fins stay stowed: Skerry's laser can see them.
- **On screen:** `L.R.E.F.S. ASTRID · FLAGSHIP`
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O2, D3
- **VFX:** 
- **Rig:** avpsa_az / avpsa_el (new)
- **Assets:** AST (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** A

### 13. Skerry throws

- **Film:** 1:42.0–1:59.0 (17 s), frames 2449–2856
- **Mission:** T+0:04:10 · 1:1
- **Camera:** HUD insert · the Astrid's telescope feed, 2,000 mm equivalent (HUD insert)
- **Viewer sees:** A grainy telescope feed on a grey moon: a thread of light runs along its dark edge, three times. A plot marker tags each launch with an arrival time. Then a white glare floods the feed.
- **Action:** A thread of light runs along Skerry's dark limb: the mass driver throwing. Three rounds leave; the plot tags their arrival. Then a glare blooms across the feed: Skerry's laser has found the dish.
- **Comms:** ASTRID: “Launch on Skerry! Mass driver, three rounds, in our lane.” / ACTUAL: “Time of flight?” / ASTRID: “Six hours, give or take.” / ASTRID: “Laser on the dish! Skerry's painting us!” (at 13 s)
- **On screen:** `SKERRY · MAREN'S MOON` · `ARRIVE T+6:40`
- **Doctrine:** HO3, HO5, O2
- **VFX:** HUD, telescope grain, dazzle glare
- **Rig:** none
- **Assets:** HUD (new), SKR (new), FX-DAZZLE (new), SUB (new)
- **Sound:** Soft sensor tones.
- **Render class:** E · **Map:** A

### 14. The picture

- **Film:** 1:59.0–2:19.0 (20 s), frames 2857–3336
- **Mission:** T+0:09:00 · compressed ~16× (the picture builds over ~5 min)
- **Camera:** HUD insert · the master plot (HUD insert)
- **Viewer sees:** A tactical plot, the planet at right: a red diamond parked over a point on the planet; the moon; a wide dotted ring; a line from the fleet toward the planet. Labels appear as each is named.
- **Action:** The master plot, Maren screen right: Breakwater parked over Site 1; Skerry, with its laser and mass driver; the Breakers; the approach line. The fins stay in while Skerry's laser can see them.
- **Comms:** ACTUAL: “All Tidebreak, Actual. Breakwater's on station over Site One, the one laser site that covers her.” / ACTUAL: “Skerry's laser has range on our radiators. It's the priority. Radiators stay stowed till it's down.”
- **On screen:** `BREAKWATER` · `SITE 1` · `SKERRY` · `THE BREAKERS`
- **Doctrine:** O2, D3
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones.
- **Render class:** E · **Map:** A

### 15. Wave one

- **Film:** 2:19.0–2:24.0 (5 s), frames 3337–3456
- **Mission:** T+0:18:00 · 1:1
- **Camera:** WS · 24 mm · on the Infinity's hull, shaking with each launch (hull camera)
- **Viewer sees:** On the hull of a long frigate bristling with launch pods: pod doors open in waves down the hull and missiles streak away to the right; the camera shakes with each launch.
- **Action:** The Infinity ripple-fires 150 capital-ship killers at Skerry's laser, mass driver and depot in fifteen seconds. Pod doors open in waves down the hull and the plumes curve away screen right. Skerry goes first because its laser can burn the fleet's fins all the way in.
- **Comms:** ACTUAL: “Infinity, Actual. Wave one. Fire.”
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O3, O9, D3
- **VFX:** 150 missiles (swarm system), pod doors
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), SUB (new)
- **Sound:** Launch cracks through the hull; the camera shakes with each.
- **Render class:** C · **Map:** A

### 16. Birds away

- **Film:** 2:24.0–2:27.0 (3 s), frames 3457–3528
- **Mission:** T+0:19:00 · 1:1
- **Camera:** CU · 85 mm · a drone camera pacing one missile (cinematic licence: it keeps up with a 30 g boost) (drone camera)
- **Viewer sees:** Alongside one of the missiles a minute into its flight: a sleek body turning slowly on a white-hot exhaust needle, the frigate a spark far behind. Ahead, screen right, a thin grey crescent: the moon.
- **Action:** Alongside one of the 150, a minute into its boost: a capital-ship killer in a slow spin, its plume a white-hot needle, the Infinity already a spark far behind. Ahead, screen right, its target: Skerry, backlit, a thin bright crescent on a dark disc (~6 % lit, ~30 px). Maren is out of frame.
- **Comms:** INFINITY · MISSILE FRIGATE: “Wave one away. One-five-zero birds.”
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O3, O9
- **VFX:** Hero missile and plume, far launch sparks
- **Rig:** thrust 1; spin (swarm attribute)
- **Assets:** MSL-V (new), SKR (new), SUB (new)
- **Sound:** Silence; the score lifts.
- **Render class:** B · **Map:** A

### 17. Turn and burn

- **Film:** 2:27.0–2:34.0 (7 s), frames 3529–3696
- **Mission:** T+0:25:00 · compressed 8× (the turn takes ~49 s)
- **Camera:** EWS · 400 mm · the whole group (tracker)
- **Viewer sees:** Through a long lens, the whole group: eleven drive plumes light one after another as the ships swing toward the planet and burn; three ships far behind stay dark.
- **Action:** Through a long lens, eleven drives light one after another as the group turns onto the approach line, bows toward Maren and plumes streaming screen left; the three ships at the park stay dark behind them. One g for 34 minutes.
- **Comms:** ACTUAL: “All Tidebreak, execute. One g, thirty-four minutes.” / ENDEAVOR: “Endeavor, burning.”
- **State:** EN: shield parked, four fins; DD: intact
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O1, D2
- **VFX:** Distant drive plumes
- **Rig:** none
- **Assets:** AST (new), EN (extend), GI (new), DD (new), CV (new), FX-FAR (new), SUB (new)
- **Sound:** Sub-bass swell.
- **Render class:** D · **Map:** A

## Act II: The Breakers

Hours of coasting, then the debris ring: the ambush, the Canterbury, the Astrid's answer, the drones and the Normandy.

### 18. Skerry burns

- **Film:** 2:34.0–2:41.0 (7 s), frames 3697–3864
- **Mission:** T+1:02:00 · compressed 5× (~20 s of hits); the digits roll 36 min into it
- **Camera:** EWS · 1,200 mm · Skerry a quarter-frame crescent, its night side dark (tracker)
- **Viewer sees:** Through a very long lens, the grey moon as a thin crescent: pinpricks of white light spark across its dark side.
- **Action:** Pinpricks of white on Skerry's limb: wave one arriving, nose-on to the battery. The light left Skerry 0.9 s ago. Just before the hits, a faint spray of points leaves the depot: its drones, flushed toward the shield park. Its eighteen rounds are already on their way.
- **Comms:** ASTRID: “Good hits. Laser and driver down.” / ACTUAL: “Eighteen rounds still inbound. Keep tracking.”
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O3, O9, HO8
- **VFX:** Distant nuclear flashes, flushed drones
- **Rig:** none
- **Assets:** SKR (new), FX-NUKE (new), SUB (new)
- **Sound:** Nothing; a swell of score.
- **Render class:** D · **Map:** A

### 19. Fins edge-on

- **Film:** 2:41.0–2:48.0 (7 s), frames 3865–4032
- **Mission:** T+1:10:00 · compressed; the digits roll through a 2 h 10 min coast
- **Camera:** MS · 40 mm · arcing round to dead ahead (drone camera)
- **Viewer sees:** The cruiser from the opening: four long fins slide out of its hull, glowing dull red, and the camera swings round until they are edge-on to the planet, thin lines. Far behind, the flagship's fins glow like a lantern. The clock runs on through two hours.
- **Action:** With Skerry's laser gone, the four fins run out, glowing a dull red. The camera arcs to dead ahead as they extend, until they collapse to slivers: edge-on to Site 1 and Breakwater, dead ahead. Far behind, the Astrid's eight fins glow like a lantern. The clock rolls on.
- **Comms:** ENDEAVOR: “Skerry's blind. Radiators out, edge-on to the planet.”
- **State:** EN: shield parked, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** D3
- **VFX:** Fin glow
- **Rig:** radiator_deploy 0.12→1; heat 0.6; radiator_glow
- **Assets:** EN (extend), AST (new), SUB (new)
- **Sound:** Silence; the score carries the coast.
- **Render class:** A · **Map:** A · **Reference frame:** `img/orbit_v8d.jpg`

### 20. The Breakers

- **Film:** 2:48.0–2:52.0 (4 s), frames 4033–4128
- **Mission:** T+3:20:00 · 1:1
- **Camera:** WS · 24 mm · tracking alongside (drone camera)
- **Viewer sees:** A faint haze thickens around the cruiser, lit from behind; its fins slide back in. A huge rock slides past, gone in under two seconds. Small ships spread out ahead.
- **Action:** The fins retract before the debris. A faint haze thickens, lit from behind. A single large rock slides past twenty kilometres off, gone across the frame in under two seconds at 20 km/s. The corvettes spread ahead, screen right.
- **Comms:** ACTUAL: “Breakers ahead. Radiators in. Corvettes, point.”
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** O8, D3, D5, D6
- **VFX:** Dust haze (Mist pass), one rock fly-by
- **Rig:** radiator_deploy 1→0.12
- **Assets:** EN (extend), BRK (new), CV (new), DRN-L (new), SUB (new)
- **Sound:** Silence; a low drone in the score.
- **Render class:** B · **Map:** B

### 21. Blind

- **Film:** 2:52.0–2:55.0 (3 s), frames 4129–4200
- **Mission:** T+3:30:00 · 1:1
- **Camera:** CU · 85 mm · the sensor mast, with its POV feed inset (hull camera)
- **Viewer sees:** Close on a sensor mast: its lenses flare white, an inset video feed whites out, and armoured shutters slam over the lenses.
- **Action:** Site 1's beam finds the Endeavor through the haze. The mast's optics flare, the inset feed whites out, and armoured shutters slam shut.
- **Comms:** ENDEAVOR: “Site One's on us! Shutters!”
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO5
- **VFX:** Dazzle bloom, POV whiteout
- **Rig:** mast_shutter 0→1 (new)
- **Assets:** EN (extend), EN-MAST (extend), FX-DAZZLE (new), SUB (new)
- **Sound:** A static howl on the feed; the shutter slam through the hull.
- **Render class:** A · **Map:** B · **Reference frame:** `img/lookmast_v8d.jpg`

### 22. The belt wakes

- **Film:** 2:55.0–2:58.0 (3 s), frames 4201–4272
- **Mission:** T+3:40:00 · compressed 10× (~30 s)
- **Camera:** WS · 40 mm · beside a rock ahead of the fleet (drone camera)
- **Viewer sees:** Beside a rock ahead of the fleet: the surface heaves, doors open like petals, and missiles tumble out, then ignite and turn toward the fleet.
- **Action:** Regolith heaves and petal doors open. Missiles tumble out cold, then light two kilometres clear and turn screen left, toward the fleet. Until now the pods were the temperature of the rock.
- **Comms:** WALLFISH · CORVETTE: “Vampires! Off the rocks!”
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO2, HD3
- **VFX:** Pod doors, late motor ignition
- **Rig:** heave / petals (new)
- **Assets:** EMP-POD (new), MSL-V (new), BRK (new), SUB (new)
- **Sound:** Silence; a sting in the score.
- **Render class:** B · **Map:** B

### 23. Spin-up

- **Film:** 2:58.0–2:59.0 (1 s), frames 4273–4296
- **Mission:** T+3:45:00 · 1:1
- **Camera:** ECU · 100 mm · a CIWS (hull camera)
- **Viewer sees:** A rotary gun's seven barrels blur into motion.
- **Action:** Seven barrels blur into motion inside the perforated jacket.
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D1
- **VFX:** 
- **Rig:** ciws_phase (new); ciws_fire (new)
- **Assets:** EN (extend), EN-PD (extend)
- **Sound:** A rising whine through the hull.
- **Render class:** A · **Map:** B

### 24. Lenses

- **Film:** 2:59.0–3:02.0 (3 s), frames 4297–4368
- **Mission:** T+3:45:01 · 1:1
- **Camera:** ECU · 135 mm · a laser focusing array on its yoke (hull camera)
- **Viewer sees:** A laser turret swings onto a target and its violet lens pulses rapidly; no beam is visible. Far off, a spark, and the turret is already swinging to the next.
- **Action:** The array's lens assembly slews onto an incoming pod missile, steadies, and flashes violet in rapid pulses, each one a shot; the beams themselves are invisible in vacuum. Far off, a spark as the missile's hardened nose gives way, under 300 km out, and the yoke is already swinging to the next.
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D1
- **VFX:** Lens glow pulses, a distant intercept flash
- **Rig:** laser_power pulses; laser_traverse; laser_elevation
- **Assets:** EN (extend), FX-PD (new)
- **Sound:** Capacitor whine and the yoke's servo through the hull, one tick per pulse.
- **Render class:** A · **Map:** B

### 25. Countermeasures

- **Film:** 3:02.0–3:06.0 (4 s), frames 4369–4464
- **Mission:** T+3:45:04 · 1:1
- **Camera:** MS · 35 mm · along the port flank (drone camera)
- **Viewer sees:** Along the cruiser's flank: flares and chaff bloom, a smoke screen spreads, gun tracers streak out, and incoming missiles burst one by one.
- **Action:** Chaff and flares bloom and a smoke screen unfurls, thinning as it spreads. The CIWS lay kill clouds in the missiles' paths; the laser lenses glow violet, beams invisible. Missiles pop one by one.
- **Comms:** ENDEAVOR: “Decoys away. Point defence free.”
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D1
- **VFX:** Tracers, kill clouds, chaff, smoke, intercept flashes
- **Rig:** ciws_fire (new); cm_chaff / cm_flare / cm_smoke (new); laser_power 0→1; laser_traverse
- **Assets:** EN (extend), EN-PD (extend), FX-PD (new), FX-SMOKE (new), SUB (new)
- **Sound:** Silence (drone camera); the score's pulse.
- **Render class:** A2 · **Map:** B · **Reference frame:** `img/lookpair_final.jpg`

### 26. The platform

- **Film:** 3:06.0–3:08.0 (2 s), frames 4465–4512
- **Mission:** T+3:52:00 · 1:1
- **Camera:** WS · 50 mm · over the platform's shoulder (drone camera)
- **Viewer sees:** A buried gun heaves out of a rock and fires a burst of slugs straight down the fleet's path.
- **Action:** A buried twin railgun heaves out of a rock 600 km ahead of the fleet and fires a ten-slug pattern screen left, straight down the fleet's path.
- **Comms:** ASTRID: “Railgun unmasking! Canterbury, break!”
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO1, HO2, HO9
- **VFX:** Muzzle flashes, slug glints
- **Rig:** unmask / shot (new)
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new), SUB (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** B

### 27. Canterbury

- **Film:** 3:08.0–3:10.0 (2 s), frames 4513–4560
- **Mission:** T+3:52:05 · compressed 4× (13 s flight)
- **Camera:** Tracker · 1,500 mm · from the Extenuating Circumstances (tracker)
- **Viewer sees:** Through a long lens: the sensor destroyer from before, fifty kilometres off, jinking hard on its thrusters.
- **Action:** The Canterbury, fifty kilometres off, jinks hard on RCS, its dish forward.
- **State:** DD: intact
- **World:** the Breakers (backlit haze)
- **Doctrine:** D4
- **VFX:** RCS puffs
- **Rig:** rcs (new)
- **Assets:** DD (new)
- **Sound:** Silence.
- **Render class:** D · **Map:** B

### 28. Holed

- **Film:** 3:10.0–3:15.0 (5 s), frames 4561–4680
- **Mission:** T+3:52:13 · 1:1
- **Camera:** Tracker · 1,500 mm · holding on the Canterbury (tracker)
- **Viewer sees:** The slugs arrive: three white flashes along the destroyer. It vents glittering ice, breaks in two and tumbles. Its channel dies to hiss.
- **Action:** The slugs arrive from ahead. The Canterbury is holed bow to stern in three white flashes; it vents glittering ice, the hull parts in two and tumbles. Hold on it as its channel dies to hiss.
- **Comms:** ENDEAVOR: “Canterbury's breaking up. No beacons.” (at 1 s)
- **State:** DD: intact
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO9
- **VFX:** Impact flashes, venting, section break
- **Rig:** break 0→1 (new)
- **Assets:** DD (new), DD-BRK (new), FX-BREAK (new), FX-VENT (new), SUB (new)
- **Sound:** The dying channel's hiss, then silence.
- **Render class:** S · **Map:** B

### 29. Answer

- **Film:** 3:15.0–3:19.0 (4 s), frames 4681–4776
- **Mission:** T+3:52:38 · 1:1 (the last degrees of the slew; it fires two seconds in)
- **Camera:** EWS · 135 mm · the Astrid in profile, bow screen right (drone camera)
- **Viewer sees:** The flagship in profile, bow to the right: it swings its last few degrees, steadies, and a blue-white flash blooms at its bow and holds.
- **Action:** The Astrid's 1.6-kilometre hull swings its last few degrees onto the platform, steadies on RCS, and two seconds in fires down the spinal: a blue-white bloom at the bow that holds to the cut.
- **Comms:** ACTUAL: “Astrid, spinal on the platform.” / ASTRID: “Solution. Firing.” (at 2 s)
- **World:** the Breakers (backlit haze)
- **Doctrine:** O4
- **VFX:** Spinal muzzle bloom
- **Rig:** rcs_bow / rcs_stern (new); spinal_charge / spinal_shot (new)
- **Assets:** AST (new), FX-SPINAL (new), SUB (new)
- **Sound:** A sub-bass punch.
- **Render class:** B · **Map:** B

### 30. Payback

- **Film:** 3:19.0–3:22.0 (3 s), frames 4777–4848
- **Mission:** T+3:54:28 · the clock jumps 108 s from the shot
- **Camera:** WS · 50 mm · the platform shot's framing (drone camera)
- **Viewer sees:** The rock with the buried gun, from the same angle as before. The clock jumps almost two minutes, and the rock erupts.
- **Action:** 8,600 km away and 108 seconds later, the platform's rock erupts. The platform could not move.
- **Comms:** ASTRID: “Splash.” (at 0.8 s) / ASTRID: “That's for Canterbury.”
- **World:** the Breakers (backlit haze)
- **Doctrine:** O4
- **VFX:** Impact eruption on the rock
- **Rig:** none
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new), SUB (new)
- **Sound:** A delayed boom in the score.
- **Render class:** B · **Map:** B

### 31. Screens out

- **Film:** 3:22.0–3:26.0 (4 s), frames 4849–4944
- **Mission:** T+4:10:00 · compressed ~30× (2 min)
- **Camera:** WS · 28 mm · behind the corvettes (drone camera)
- **Viewer sees:** Behind three small warships: on the rocks ahead, dark shells crack open and swarms of drones pour out; the small ships fan out to meet them, launching drones of their own.
- **Action:** Ahead, cold hides crack open on the rocks and drones pour out. The corvettes fan out to meet them, their own drones ahead.
- **Comms:** NORMANDY · CORVETTE: “Drones launching! Dozens!”
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO4, D6, O7
- **VFX:** Drone swarms (swarm system)
- **Rig:** none
- **Assets:** CV (new), DRN-C (new), DRN-L (new), FX-SWARM (new), BRK (new), SUB (new)
- **Sound:** A rising whine in the score.
- **Render class:** C · **Map:** B

### 32. Return to sender

- **Film:** 3:26.0–3:40.0 (14 s), frames 4945–5280
- **Mission:** T+4:14:00 · 1:1
- **Camera:** HUD insert · the Extenuating Circumstances' plot (HUD insert)
- **Viewer sees:** A tactical plot: a cloud of red drone tracks. A block of them flips to teal and turns on the rest; the red ones keep coming. Labels appear.
- **Action:** A block of drone tracks flips from red to teal: the drones still on a control link are hijacked and turned on their own swarm. The control craft behind the rocks is found and dazzled; the Canterbury's drifting drones are picked up. The autonomous drones keep coming.
- **Comms:** EXTENUATING · SENSOR DESTROYER: “We're in their drone links.” / EXTENUATING: “Turning them. Return to sender.” / EXTENUATING: “The rest are AI-run, no links. Can't touch those.”
- **On screen:** `LINKED → OURS` · `AUTONOMOUS`
- **Doctrine:** O5, HD9, D10
- **VFX:** HUD, EW overlay
- **Rig:** none
- **Assets:** HUD (new), FX-EW (new), SUB (new)
- **Sound:** Clipped data chatter.
- **Render class:** E · **Map:** B

### 33. Normandy

- **Film:** 3:40.0–3:45.0 (5 s), frames 5281–5400
- **Mission:** T+4:25:00 · 1:1
- **Camera:** Tracker · 800 mm · from the Wallfish (tracker)
- **Viewer sees:** Through a long lens: a lone drone slips past the screen and dives onto a small warship; a violet-white flash against its side, and the ship breaks apart. The picture holds on the wreck as its channel dies to hiss.
- **Action:** One autonomous drone slips the screen and dives on the Normandy. A plasma bomb goes off against its flank and the corvette breaks up. Hold two seconds on the wreck as its channel dies to hiss.
- **Comms:** WALLFISH: “Leaker! One's through: Normandy, break!”
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO4
- **VFX:** Plasma-bomb flash, break-up
- **Rig:** break 0→1 (new)
- **Assets:** CV (new), CV-BRK (new), DRN-C (new), FX-SWARM (new), FX-BREAK (new), SUB (new)
- **Sound:** The dying channel's hiss, then silence.
- **Render class:** S · **Map:** B

## Act III: Anchor

Turnover into the lee of a rock over Site 1: the sweep, the heat, the fin hit, the frigate, the lance and the broadside.

### 34. Turnover

- **Film:** 3:45.0–3:51.0 (6 s), frames 5401–5544
- **Mission:** T+4:34:10 · rotation at ~4×, the middle of the 49 s flip cut out
- **Camera:** WS · 24 mm · on the dorsal hull looking aft (hull camera)
- **Viewer sees:** On the cruiser's back, looking aft: smoke drifts past, the stars wheel as the ship flips end over end, and its main drive lights, pointing toward the planet.
- **Action:** Under smoke and an EW peak, one ship at a time, the fleet flips. The stars wheel over the hull as the stern swings toward Maren; now the bow points screen left while the ship still travels right. The drive lights: 34 minutes of braking toward Anchor.
- **Comms:** ACTUAL: “All Tidebreak, turnover. Staggered, keep point defence up.” / ENDEAVOR: “Flipping.” (at 3 s)
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D8, O8
- **VFX:** Main plume, RCS, smoke screen
- **Rig:** rcs_bow / rcs_stern pulses; engine_throttle 0→1; cm_smoke (new)
- **Assets:** EN (extend), EN-PD (extend), FX-SMOKE (new), SUB (new)
- **Sound:** RCS thumps, then the drive's roar through the hull.
- **Render class:** A2 · **Map:** B

### 35. Anchor

- **Film:** 3:51.0–4:05.0 (14 s), frames 5545–5880
- **Mission:** T+5:08:00 · 1:1; the digits roll 33 min into it
- **Camera:** HUD insert · the master plot, zoomed (HUD insert)
- **Viewer sees:** A zoomed tactical plot: a lumpy rock, its shadow drawn pointing away from a ground-laser marker; two nearby rocks tagged '?'; a heat readout.
- **Action:** Anchor, an 18 km rock, with its shadow pointing away from Site 1. The fleet will string out along it; two nearby rocks are tagged '?'.
- **Comms:** ACTUAL: “Anchor. We tuck into her lee: eighteen klicks of rock between us and Site One.” / ENDEAVOR: “Actual, Endeavor. Heat sink at nine-four. We need to vent.”
- **On screen:** `ANCHOR` · `SITE 1` · `?` · `?` · `ENDEAVOR HEAT 94%`
- **Doctrine:** D5, D2
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones.
- **Render class:** E · **Map:** C

### 36. The sweep

- **Film:** 4:05.0–4:09.0 (4 s), frames 5881–5976
- **Mission:** T+5:09:00 · compressed ~20× (minutes)
- **Camera:** WS · 24 mm · low over Anchor's surface (drone camera)
- **Viewer sees:** Low over the rock's surface, in darkness: the cruiser settles into the rock's shadow. Small craft sweep the rock; a flash lights its far edge from behind. Far off, shells burst on nearby rocks.
- **Action:** The Endeavor settles into darkness in the lee, a few kilometres off the surface, where the rock blocks the sun as well as Site 1. Corvettes and drones sweep the rock: a drone trips a mine on the far side, and the flash lights Anchor's limb from behind. Far off, the Donnager's shells land on the nearest rocks.
- **Comms:** DONNAGER · GUN FRIGATE: “Rocks done. Moonlets next.”
- **State:** EN: shield parked, four fins
- **World:** Anchor's dark lee
- **Doctrine:** O8, D6, O4
- **VFX:** Mine flash behind the limb, distant impacts
- **Rig:** rcs_bow / rcs_stern pulses
- **Assets:** EN (extend), ANCHOR (new), BRK (new), CV (new), DRN-L (new), GI (new), GI-GUN (new), FX-NUKE (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** C

### 37. Too hot

- **Film:** 4:09.0–4:14.0 (5 s), frames 5977–6096
- **Mission:** T+5:12:00 · compressed 5× (the fins take ~20 s)
- **Camera:** MS · 35 mm · on the stern shoulder (hull camera)
- **Viewer sees:** On the cruiser's stern, in darkness: alarm tones; slot doors slide open and four fins telescope out, glowing orange, the only light.
- **Action:** Heat alarms at 96 % and climbing. The sweep isn't finished, but the sink can't wait: the slot doors slide open and all four fins telescope out, glowing orange against black, the only light in the lee.
- **Comms:** DONNAGER: “Sweep's not done.” / ENDEAVOR: “Can't wait. Radiators out.”
- **On screen:** `HEAT 96%`
- **State:** EN: shield parked, four fins
- **World:** Anchor's dark lee
- **Doctrine:** D3, D5
- **VFX:** Fin glow, light spill
- **Rig:** fin_* 0→1 (new); heat 1.9→2.4; radiator_glow
- **Assets:** EN (extend), EN-FIN (extend), SUB (new)
- **Sound:** Alarm tones; the fins' hydraulic groan.
- **Render class:** A · **Map:** C · **Reference frame:** `img/lookaft_s1combat.jpg`

### 38. The flash

- **Film:** 4:14.0–4:15.0 (1 s), frames 6097–6120
- **Mission:** T+5:13:00 · 1:1
- **Camera:** Tracker · 1,200 mm · on a rock 400 km off the port quarter (tracker)
- **Viewer sees:** Through a long lens, another rock far off, not the one from before: a muzzle flash, half a second long.
- **Action:** A muzzle flash on a rock: the platform, unmasked for half a second.
- **World:** Anchor's dark lee
- **Doctrine:** HO7, HO1
- **VFX:** Muzzle flash
- **Rig:** unmask / shot (new)
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new)
- **Sound:** Silence.
- **Render class:** D · **Map:** C

### 39. Fins in

- **Film:** 4:15.0–4:18.0 (3 s), frames 6121–6192
- **Mission:** T+5:13:01 · compressed 5× (the fins crawl in against a 16 s flight)
- **Camera:** MS · 35 mm · the same shoulder, the clock large (hull camera)
- **Viewer sees:** The same stern view, a large clock in frame: the fins start to crawl back in.
- **Action:** The fins start in, crawling against the clock.
- **Comms:** ENDEAVOR: “Launch, four hundred klicks! Radiators in!”
- **State:** EN: shield parked, four fins
- **World:** Anchor's dark lee
- **Doctrine:** HO7, HO1, D3
- **VFX:** 
- **Rig:** fin_* 1→0.5 (new)
- **Assets:** EN (extend), EN-FIN (extend), SUB (new)
- **Sound:** The call; alarms; the fins' groan.
- **Render class:** A · **Map:** C

### 40. Fin hit

- **Film:** 4:18.0–4:21.0 (3 s), frames 6193–6264
- **Mission:** T+5:13:16 · 1:1
- **Camera:** CU · 50 mm · on the port fin (hull camera)
- **Viewer sees:** Close on one fin, halfway in: a slug from the right shatters it into glowing shards, and coolant sprays out as glittering ice.
- **Action:** Halfway in, the port fin takes a slug from screen right. It shatters into glowing shards and its coolant flashes to glittering ice.
- **Comms:** ENDEAVOR: “Port radiator's gone!” (at 1 s)
- **State:** EN: port fin shattering
- **World:** Anchor's dark lee
- **Doctrine:** HO7, D7
- **VFX:** Fin shatter, coolant venting
- **Rig:** fin_port_state → pre-fractured (new)
- **Assets:** EN (extend), EN-FIN (extend), FX-FIN (new), FX-VENT (new), FX-SLUG (new), SUB (new)
- **Sound:** Metal shear through the hull; a hiss.
- **Render class:** A2 · **Map:** C

### 41. Off the port bow

- **Film:** 4:21.0–4:25.0 (4 s), frames 6265–6360
- **Mission:** T+5:13:30 · 1:1
- **Camera:** Hull camera · 600 mm · on the Endeavor's port side (hull camera)
- **Viewer sees:** From a camera on the cruiser's side: a warship slides out of a cleft in a small moon and fires; two seconds later the camera shakes with a hit.
- **Action:** A Compact frigate slides out of a pre-dug cleft on the far side of a moonlet, 45 km off the port bow, and fires its coilgun. Two seconds later the camera shakes as the slug spalls the port belt.
- **Comms:** DONNAGER: “Frigate, off your port bow!” / ENDEAVOR: “Hit, port side!” (at 2.5 s)
- **State:** EN: port fin a stump
- **World:** Anchor's dark lee
- **Doctrine:** HO6, O6
- **VFX:** Coilgun flash, hull spall
- **Rig:** dmg_belt 0→1 (new)
- **Assets:** CF (new), ANCHOR (new), EN (extend), EN-FIN (extend), EN-DMG (extend), FX-SLUG (new), SUB (new)
- **Sound:** The hit through the hull.
- **Render class:** A2 · **Map:** C

### 42. Lance channels

- **Film:** 4:25.0–4:27.0 (2 s), frames 6361–6408
- **Mission:** T+5:13:53 · 1:1
- **Camera:** CU · 28 mm · the Endeavor's nose (hull camera)
- **Viewer sees:** Close on the cruiser's nose: four channels glow violet-white.
- **Action:** The four lance channels in the nose glow violet-white as the field builds.
- **Comms:** ENDEAVOR: “Forty-five klicks. Lance her.”
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O12
- **VFX:** Lance core glow
- **Rig:** lance_power 0→1
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), SUB (new)
- **Sound:** A rising electric whine through the hull.
- **Render class:** A · **Map:** C

### 43. Lance

- **Film:** 4:27.0–4:29.0 (2 s), frames 6409–6456
- **Mission:** T+5:13:55 · 1:1
- **Camera:** Tracker · 1,000 mm · on the frigate, 45 km out (tracker)
- **Viewer sees:** Through a long lens on the enemy frigate: a spear of violet-white plasma crosses from the right, its midsection opens, and escape pods scatter as it breaks.
- **Action:** The ship's field reaches out and a spear of plasma crosses the frame from the right to the frigate, forty-five kilometres off, inside the ~50 km the field can hold. The frigate's midsection opens; escape pods scatter as it breaks.
- **World:** Anchor's dark lee
- **Doctrine:** O12, O6
- **VFX:** Field-held plasma jet, break-up
- **Rig:** break 0→1 (new)
- **Assets:** CF (new), FX-LANCE (new), FX-BREAK (new), FX-VENT (new)
- **Sound:** A crack in the score.
- **Render class:** B · **Map:** C

### 44. Broadside

- **Film:** 4:29.0–4:32.0 (3 s), frames 6457–6528
- **Mission:** T+5:14:00 · compressed 5× (the roll)
- **Camera:** MS · 35 mm · the port batteries, the rock beyond (hull camera)
- **Viewer sees:** The cruiser rolls, bringing its gun turrets round toward the rock that just fired; the turrets still sit clamped in their cradles.
- **Action:** Fins stowed, the Endeavor rolls to bring its port batteries onto the platform's rock, off the port quarter, screen right. The turrets still sit clamped in their travel locks.
- **Comms:** ENDEAVOR: “Roll to port. Batteries on the platform.”
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O6, O4, D3
- **VFX:** 
- **Rig:** rcs_bow / rcs_stern pulses (the roll)
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), M1C (extend), SUB (new)
- **Sound:** The roll's RCS thumps through the hull.
- **Render class:** A · **Map:** C · **Reference frame:** `img/house_s1combat.jpg`

### 45. Rails wake

- **Film:** 4:32.0–4:36.0 (4 s), frames 6529–6624
- **Mission:** T+5:14:15 · compressed 2× (the ~8 s wake)
- **Camera:** CU · 50 mm · on one M-1C turret (hull camera)
- **Viewer sees:** Close on one gun turret: lids open on rows of amber lights, beacons flash, clamps swing off, the gun lifts onto the rock, and its armoured shell splits and rises; its jaws open. The barrel stays dark.
- **Action:** The turret wakes in its fixed order. The capacitor banks' lids open on rows of charge cells that light amber, the rear louvres ripple open and the beacons flash; the travel-lock clamps swing off the jaws and the crutch folds flat; the cradle lays onto the rock; the supershell's latches drop, its halves crack, rise and clunk against their stops, and the chisel jaws swing open. The barrel stays dark.
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O4, O6
- **VFX:** Amber charge cells, meters, beacons (no glow on the barrel until it fires)
- **Rig:** rail_wake 0→1; rail_lock 1→0; rail_traverse / rail_elevation; rail_arm 0→1
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), M1C (extend)
- **Sound:** Clunks through the hull: the lids, the clamps, the shell's halves on their stops.
- **Render class:** A · **Map:** C

### 46. Fire

- **Film:** 4:36.0–4:39.0 (3 s), frames 6625–6696
- **Mission:** T+5:14:23 · 1:1
- **Camera:** CU · 85 mm · on the barrels and the crest vent (hull camera)
- **Viewer sees:** The barrels: a shudder, a blue-white pulse up the bore, a blinding muzzle blast and the recoil; fins on the gun that fired burst out and glow.
- **Action:** Gun A charges for a second: the barrel draws back and buzzes, the shell throbs, the flush fins chatter. Then the bore pulse (cinematic licence, Q12), a tracer blast toward the rock, and the recoil. Only the gun that fired vents: its crest fins burst out and glow; gun B waits its turn.
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O4, O6
- **VFX:** Charge shudder, bore pulse, muzzle blast, tracer, the crest fins' glow
- **Rig:** charge_a; shot_a; fins_a; heat_a
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), M1C (extend), FX-SLUG (new)
- **Sound:** The charge's buzz, the shot's crack and the recoil's clunk through the hull.
- **Render class:** A2 · **Map:** C

### 47. The platform dies

- **Film:** 4:39.0–4:43.0 (4 s), frames 6697–6792
- **Mission:** T+5:14:40 · the clock jumps 16 s of flight from the shot
- **Camera:** Tracker · 1,200 mm · the flash's framing (tracker)
- **Viewer sees:** Through a long lens, the rock that fired on the cruiser: a flash. The picture holds on the rock.
- **Action:** The platform's rock flashes: sixteen seconds of flight, and a target that could not move. With the lee quiet again, the Endeavor runs its three remaining fins out and vents (94 % → 31 % by the fire plan).
- **Comms:** ENDEAVOR: “Splash platform. Radiators out, all three.”
- **World:** Anchor's dark lee
- **Doctrine:** O4
- **VFX:** Impact flash
- **Rig:** none
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new), SUB (new)
- **Sound:** The score.
- **Render class:** D · **Map:** C

## Act IV: Hammer and anvil

Across to Breakwater: the plan, Skerry's nets, Site 1's fire, the pack's two launches through a last try at it, Breakwater's answer at the last net ship, all in Maren's shadow; the spend wave, the kill wave, the Casaba jets and the hail; the spinal slug flies into Breakwater's sunrise; then terms.

### 48. The fire plan

- **Film:** 4:43.0–5:07.0 (24 s), frames 6793–7368
- **Mission:** T+5:40:00 · 1:1
- **Camera:** HUD insert · the master plot (HUD insert)
- **Viewer sees:** The master plot: the fleet at the rock; two dotted tracks from it to where the enemy warship will be, labelled with two times; then a solid track from the rock to a violet marker short of the enemy, the flagship's firing point; a heat readout.
- **Action:** The plan builds in three beats, one per line. The two missile frigates and their guard stay at Anchor, and everyone else leaves with the Astrid at T+5:43; the waves' two tracks run from Anchor to where Breakwater will be; the Astrid's track ends at its firing point, where it waits for a target that can't move.
- **Comms:** ACTUAL: “Infinity, Galactica: fire from here. Donnager, Wallfish: guard them. Everyone else, on me.” / ACTUAL: “Spend wave draws her fire. Kill wave, ninety seconds behind: forty Casaba nukes on her drive.” / ACTUAL: “Once she can't move, Astrid takes the kill.”
- **On screen:** `ON TARGET: SPEND 7:52 · KILL 7:53` · `ASTRID` · `ENDEAVOR HEAT 31%`
- **Doctrine:** O9, O3, O10, O11, D11
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones; the score gathers.
- **Render class:** E · **Map:** D

### 49. The net

- **Film:** 5:07.0–5:15.0 (8 s), frames 7369–7560
- **Mission:** T+6:40:00 · compressed ~20× (2 min); the digits roll 60 min into it
- **Camera:** Tracker · 300 mm · from the Extenuating Circumstances, looking ahead (tracker)
- **Viewer sees:** Through a long lens from a destroyer: ahead, drones' lamps light a spreading cloud of glittering pellets; a small warship's drive angles off and it slides aside.
- **Action:** Hours after Skerry threw them, the first of its rounds arrive. Ahead of the fleet the destroyer's drones light up a spreading cloud of pellets about 20 km across, glittering in their lamps. The fleet side-steps, drives angled off the line; four more nets follow on the lane, ten minutes apart. A long-lens view, so it renders as a small subject on black.
- **Comms:** EXTENUATING: “Pellet cloud dead ahead. Skerry's first salvo, right on time.” / ACTUAL: “Come left two degrees.”
- **State:** DD: intact
- **Light:** the escorts in sun
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** HO3, D4, O8
- **VFX:** Canister cloud glitter (swarm system)
- **Rig:** none
- **Assets:** DD (new), DRN-L (new), FX-SWARM (new), SUB (new)
- **Sound:** Silence; the score ticks.
- **Render class:** D · **Map:** D

### 50. Site One

- **Film:** 5:15.0–5:19.0 (4 s), frames 7561–7656
- **Mission:** T+6:55:00 · compressed ~15× (a minute)
- **Camera:** WS · 40 mm · ahead of the Extenuating Circumstances (drone camera)
- **Viewer sees:** Ahead of a destroyer: the tip of one of its long booms scorches and smokes under an invisible beam; the ships roll, and a new smoke screen blooms ahead of the fleet.
- **Action:** Site 1 has been firing since the fleet cleared Anchor's shadow, against rolling hulls, smoke and the fleet's low-power dazzle. Now its invisible beam holds long enough on the destroyer's forward sensor boom: it scorches and smokes, the one visible cost. The ships roll on, and a fresh smoke screen blooms ahead, travelling with the fleet.
- **Comms:** EXTENUATING: “Site One's on our booms! Smoke, smoke!”
- **State:** DD: Extenuating: forward boom scorched
- **Light:** the escorts in sun
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** HO5, D1, D3, O5
- **VFX:** Scorching, fleet-scale smoke screen
- **Rig:** dmg_boom 0→1 (new)
- **Assets:** DD (new), FX-SMOKE (new), FX-DAZZLE (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** D

### 51. The pack fires

- **Film:** 5:19.0–5:24.0 (5 s), frames 7657–7776
- **Mission:** T+7:06:57 · 1:1
- **Camera:** WS · 24 mm · among the pack, 150 km down Anchor's shadow, looking toward Breakwater (drone camera)
- **Viewer sees:** Among the missile frigates, deep in the rock's shadow, the rock a black disc ahead: three glittering clouds sweep through the space the frigates have just left; drones come round the rock after them and die in bursts of tracer. Then pod doors ripple open down a frigate's hull and hundreds of small plumes streak away.
- **Action:** The rock is a black disc ahead. Skerry's last salvo, thrown six hours ago at Anchor and steered onto the pack's slot in its last hour (~40 m/s of its divert kits), sweeps through in three glittering clouds; the pack, having watched the divert burns, slid 20 km down the shadow on RCS a few minutes before. The garrison's last drones come round the rock behind the clouds, and the Wallfish and the Donnager's CIWS cut them down. On the clock, pod doors ripple open down the Infinity's hull and the spend wave leaves: hundreds of small plumes with its killers among them, all on one 45-minute profile at 30 g.
- **Comms:** DONNAGER: “Skerry's last salvo, wide! Drones behind!” (at 0 s) / INFINITY: “Spend wave away.” (at 3.5 s)
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** O3, O11, D11, D6, HO3, HO4
- **VFX:** Canister-cloud glitter, CIWS tracers and drone kills, ripple launch (swarm system)
- **Rig:** pod_ripple (new); ciws_phase / ciws_fire (new, on the Donnager)
- **Assets:** GI (new), GI-MAV (new), GI-GUN (new), MSL-V (new), FX-SWARM (new), FX-PD (new), ANCHOR (new), CV (new), DRN-C (new), SUB (new)
- **Sound:** Silence; the score drops out.
- **Render class:** C · **Map:** D

### 52. Kill wave away

- **Film:** 5:24.0–5:27.0 (3 s), frames 7777–7848
- **Mission:** T+7:08:30 · 1:1
- **Camera:** Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow: its shut pods sharp in the foreground, then a rack to the Galactica (tracker)
- **Viewer sees:** Across the rock's shadow: in the foreground, sharp, a frigate's shut pod doors; focus shifts to a second frigate as its pods ripple open and heavier plumes stream away.
- **Action:** Ninety seconds behind the spend wave. The shot opens on the Pillar of Autumn's shut pods, sharp in the foreground: the reserve. Focus racks to the Galactica as its pod doors ripple open and the kill wave leaves in one launch: ~40 Casaba killers among ~300 decoy and EW birds that look, boost and fly like them, all on the same 45-minute profile.
- **Comms:** GALACTICA: “Kill wave away.”
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** O3, O10, O11
- **VFX:** Ripple launch (swarm system), defocused foreground
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), ANCHOR (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** D

### 53. The anvil

- **Film:** 5:27.0–5:31.0 (4 s), frames 7849–7944
- **Mission:** T+7:25:00 · compressed 10× (the ripple takes ~40 s)
- **Camera:** WS · 40 mm · above Breakwater, Maren's night side below (drone camera)
- **Viewer sees:** Above a huge dark warship, the planet's night side below, glittering with city lights. No sunlight: the ship is lit only from below, red, by a thin glowing ring round the planet's edge and by the city glow, and by rows of small lit ports along its flank. Its turrets track but stay silent. Rows of cell doors open and missiles ripple out, their plumes lighting its hull. Far along its orbit, points of light wake.
- **Action:** Breakwater's reveal, with ~900 birds inbound, in Maren's shadow: no sun reaches it. It is a dark hull lit from below by the thin red ring of Maren's atmosphere and the city glow, with rows of lit ports along its flank (it is crewed), until its 64 cells open and ripple-fire and the plumes light it. Its turrets track the fleet but stay silent: the fleet never comes within their reach. Every missile goes at the Extenuating Circumstances, the ship that steers the birds, 17,000 km off, into the fleet's braking burn. Far along the orbit, ring stations wake as points of light.
- **On screen:** `BREAKWATER · MONITOR · NO WARP DRIVE`
- **State:** BW: intact
- **Light:** Breakwater in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** HD7, HO9, HD1, HO1, D1
- **VFX:** Cell doors, missile launch (swarm system)
- **Rig:** turret_traverse / cells_open (new)
- **Assets:** BW (new), RING (new), MAREN (extend), MSL-V (new), FX-SWARM (new)
- **Sound:** A low brass sting.
- **Render class:** C · **Map:** E

### 54. Sixty-four

- **Film:** 5:31.0–5:45.0 (14 s), frames 7945–8280
- **Mission:** T+7:25:40 · 1:1
- **Camera:** HUD insert · the master plot (HUD insert)
- **Viewer sees:** A tactical plot: sixty-four red tracks leave the enemy warship and converge on one friendly ship among the fleet. A second label appears beside the flagship.
- **Action:** The plot answers the reveal: every one of Breakwater's missiles is at the destroyer that steers the waves (HO9). The backup is shown too: if the Extenuating goes dark, the Astrid steers the birds direct (LREF §3).
- **Comms:** ASTRID: “Vampires, sixty-four! All tracking on Extenuating!” / EXTENUATING: “She's going for our guidance.” / ACTUAL: “Astrid, umbrella on Extenuating. If she drops, the waves are yours.”
- **On screen:** `BACKUP: ASTRID DIRECT`
- **Doctrine:** HO9, D10, D2
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones; the score tightens.
- **Render class:** E · **Map:** E

### 55. Umbrella

- **Film:** 5:45.0–5:48.0 (3 s), frames 8281–8352
- **Mission:** T+7:31:00 · 1:1
- **Camera:** Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 50 km above (tracker)
- **Viewer sees:** Through a long lens from a destroyer: the flagship 50 km above it, dark, its drive off; its violet lenses pulse, tracers lace the dark, and flashes walk in toward the camera and stop short.
- **Action:** Breakwater's missiles arrive up the fleet's drive axis. The Astrid has cut its drive for the minute so its plume won't blind its own point defence: its lenses glow violet and its CIWS lay kill clouds across the missiles' path. In Maren's shadow the flashes are the only light; they walk in toward the Extenuating and stop short.
- **Comms:** EXTENUATING: “Sixty-four splashed.” (at 1.2 s)
- **Light:** the Astrid in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** D1, D2, D10, HO9, O13
- **VFX:** Kill clouds, intercept flashes, lens glow, the drive's dying glow
- **Rig:** engine_throttle 1→0 (new); laser_power (new); ciws_phase / ciws_fire (new, on the Astrid)
- **Assets:** AST (new), MSL-V (new), FX-PD (new), FX-SWARM (new), SUB (new)
- **Sound:** Silence; the score's pulse.
- **Render class:** C · **Map:** E

### 56. Blind it

- **Film:** 5:48.0–5:53.0 (5 s), frames 8353–8472
- **Mission:** T+7:50:00 · 1:1
- **Camera:** MS · 35 mm · the Endeavor's laser arrays (hull camera)
- **Viewer sees:** In darkness, the cruiser's laser turrets: their lenses go from a dim violet glow to full, the brightest things on the hull.
- **Action:** The Extenuating Circumstances floods the ring's links. In Maren's shadow the Endeavor is a dark hull edged red; its arrays go from low power to full on Breakwater's optics and Site 1's trackers, lenses violet, beams invisible.
- **Comms:** EXTENUATING: “Their net's jammed.” / ENDEAVOR: “Arrays on Site One. Dazzle only.”
- **On screen:** `HEAT 88%`
- **State:** EN: port fin a stump, port belt scorched
- **Light:** the escorts in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** O5, HD9
- **VFX:** Lens glow, EW overlay on inserts
- **Rig:** laser_power 0.2→1; laser_traverse; laser_elevation
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), FX-EW (new), SUB (new)
- **Sound:** The lenses' capacitor whine through the hull.
- **Render class:** A · **Map:** E · **Reference frame:** `img/lookyoke_final.jpg`

### 57. The spend wave

- **Film:** 5:53.0–5:57.0 (4 s), frames 8473–8568
- **Mission:** T+7:52:00 · 1:1
- **Camera:** Tracker · 250 mm · from the Astrid, Maren's limb in frame (tracker)
- **Viewer sees:** Through a long lens from the flagship, just off the planet's glowing red edge: a sparkle of hundreds of tiny flashes, and among them a few larger bursts.
- **Action:** Just off Maren's red limb, a sparkle: the spend wave arriving. Its decoys, EW and kill-cloud birds soak up Breakwater's point defence, and a few dozen warheads burst 1–3 km out, stripping the sensors, radiators and PD mounts on the side facing them; the hull stays whole. Every battery that fires gives itself away, and the destroyer steers the whole kill wave round them.
- **Comms:** EXTENUATING: “Her guns are firing. Kill wave steering clear.”
- **State:** BW: intact
- **Light:** Breakwater in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** O3, O5, HD5
- **VFX:** Distant PD sparkle
- **Rig:** none
- **Assets:** BW (new), FX-PD (new), MAREN (extend), SUB (new)
- **Sound:** The score.
- **Render class:** D · **Map:** E

### 58. Seeker

- **Film:** 5:57.0–6:01.0 (4 s), frames 8569–8664
- **Mission:** T+7:53:14 · compressed ~3.5× (the last 14 s of flight)
- **Camera:** ECU · 100 mm · riding a Casaba killer's nose (drone camera)
- **Viewer sees:** Riding the nose of a missile in its last seconds: its cap glows orange under a laser, then fades as the beam swings away; a small window shutter opens, and focus shifts to a dark warship ahead, growing from a point to a sliver, tracers converging in front of it.
- **Action:** The hardened nose of a Casaba killer through its last seconds, ~700 km out at ~45 km/s. The ablative cap glows where one of Breakwater's lasers is burning it; the glow fades as the beam swings off to another bird. Only then does the seeker shutter open, and focus racks from the cap to the target, ending the shot: ahead, screen right, Breakwater grows from a point to a sliver, a dark hull in Maren's shadow picked out by its own tracers.
- **State:** BW: intact
- **Light:** Breakwater in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** O3, O10, HD5
- **VFX:** Glowing ablative cap (fading), the seeker window, rack focus, distant tracers
- **Rig:** spin (swarm attribute); cap_glow (new); seeker_shutter (new)
- **Assets:** MSL-V (new), FX-PD (new), BW (new)
- **Sound:** Silence; the score climbs.
- **Render class:** B · **Map:** E

### 59. Wall of fire

- **Film:** 6:01.0–6:05.0 (4 s), frames 8665–8760
- **Mission:** T+7:53:28 · slowed 5× (the wave arrives within ~1 s)
- **Camera:** WS · 40 mm · above Breakwater (drone camera)
- **Viewer sees:** Above the dark warship: the missile wave arrives all at once from the left; tracers and dying missiles fill the dark, and the hardened noses keep coming.
- **Action:** The kill wave arrives in the same second, nose-on to Breakwater, from screen left, into a wall thinned by the spend wave. In the dark, tracers and dying birds are all the light there is; the hardened noses keep coming.
- **Comms:** GALACTICA: “Kill wave terminal. Three, two—”
- **State:** BW: intact
- **Light:** Breakwater in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** O3, HD5, O9
- **VFX:** Tracer streams, intercept flashes, swarm
- **Rig:** ciws_fire (new, on Breakwater)
- **Assets:** BW (new), FX-PD (new), FX-SWARM (new), MSL-V (new), SUB (new)
- **Sound:** A dense crackle in the score; no air, no bangs.
- **Render class:** C · **Map:** E

### 60. Casaba

- **Film:** 6:05.0–6:09.0 (4 s), frames 8761–8856
- **Mission:** T+7:53:30 · slowed 3×
- **Camera:** WS · 35 mm · off Breakwater's quarter (drone camera)
- **Viewer sees:** Off the warship's quarter: two kilometres out, nuclear jets lance into its engine bells, lighting the whole dark ship for an instant; its engines go dark.
- **Action:** Two kilometres out, the surviving Casaba charges fire from screen left: nuclear jets lance into Breakwater's drive bells, and for an instant they light the whole dark monitor. Its engines go dark. The monitor is whole, but it can no longer move.
- **Comms:** ASTRID: “Casabas in. Her drive's dead.”
- **State:** BW: drive breached, venting
- **Light:** Breakwater in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** O10
- **VFX:** Casaba jets, drive breach, venting
- **Rig:** drive_glow 1→0 (new); vent (new)
- **Assets:** BW (new), BW-BRK (new), MSL-V (new), FX-CASABA (new), FX-VENT (new), SUB (new)
- **Sound:** The comm channels white out, then silence.
- **Render class:** C · **Map:** E

### 61. The hail

- **Film:** 6:09.0–6:14.0 (5 s), frames 8857–8976
- **Mission:** T+7:54:00 · 1:1
- **Camera:** MS · 50 mm · slow push on Breakwater over the night side (drone camera)
- **Viewer sees:** The warship hangs dead-engined in the dark over the planet's night side, venting from glowing wounds, its turrets still tracking.
- **Action:** Breakwater hangs dead-engined in Maren's shadow over the night side, its spear wounds glowing and venting, its turrets still tracking. On an open channel the Astrid hails it. No answer comes.
- **Comms:** ACTUAL: “Breakwater, Tidebreak. You're disabled. Surrender your ship.”
- **State:** BW: drive breached, venting
- **Light:** Breakwater in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** O10
- **VFX:** Venting
- **Rig:** vent (new)
- **Assets:** BW (new), BW-BRK (new), MAREN (extend), FX-VENT (new), SUB (new)
- **Sound:** Silence where the answer should be.
- **Render class:** B · **Map:** E

### 62. Spinal

- **Film:** 6:14.0–6:17.0 (3 s), frames 8977–9048
- **Mission:** T+7:54:38 · 1:1 (the last degree of the slew; it fires two seconds in, at T+7:54:40)
- **Camera:** MS · 200 mm · the Astrid end-on (drone camera)
- **Viewer sees:** The flagship end-on in the dark: it settles, and a blue-white bloom lights its kilometre-long barrel and fills the frame.
- **Action:** The Astrid, stopped 10,000 km out and 15° off Breakwater's zenith so a miss would clear Maren, settles its last degree and fires. In Maren's shadow the bloom lights its dark kilometre of barrel and fills the last second.
- **Comms:** ACTUAL: “No response. Astrid, fire.”
- **Light:** the Astrid in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** O4, O10, HD7, O9
- **VFX:** Spinal muzzle bloom
- **Rig:** rcs_bow / rcs_stern (new); spinal_shot (new)
- **Assets:** AST (new), FX-SPINAL (new), SUB (new)
- **Sound:** Everything drops out.
- **Render class:** B · **Map:** E

### 63. The wait

- **Film:** 6:17.0–6:23.0 (6 s), frames 9049–9192
- **Mission:** T+7:54:41 · compressed ~27× (163 of the slug's 169 s; the clock races)
- **Camera:** WS · 35 mm · locked off at the Casaba shot's angle, Maren's limb low in frame (drone camera)
- **Viewer sees:** A locked-off view of the crippled warship, turrets swinging uselessly, while the clock races. Behind it the planet's red edge brightens and flares, the sun breaks over it, and the light on the hull climbs from red to white.
- **Action:** Hold on the crippled monitor, turrets swinging uselessly, while the clock races through the slug's flight and Breakwater's sunrise with it: behind the monitor Maren's red limb brightens and flares, the sun breaks over it, and the light on the hull climbs from red to white.
- **Comms:** ASTRID: “Round away. Time of flight two forty-nine.”
- **State:** BW: drive breached, venting
- **Light:** Breakwater in umbra → penumbra → sun
- **World:** after Breakwater's sunrise (a low sun just past Maren's limb, the night side below)
- **Doctrine:** O10
- **VFX:** Venting; the sunrise as a cross-fade from an eclipse plate to a sunlit plate, with the Sun keyed through the ~2 min penumbra; the turrets and vents as one moving layer
- **Rig:** turret_traverse (new)
- **Assets:** BW (new), BW-BRK (new), SUB (new)
- **Sound:** Silence; one held note.
- **Render class:** P · **Map:** E

### 64. Impact

- **Film:** 6:23.0–6:26.0 (3 s), frames 9193–9264
- **Mission:** T+7:57:29 · 1:1
- **Camera:** WS · 35 mm · the Casaba shot's angle (drone camera)
- **Viewer sees:** In the first full sunlight: the slug strikes amidships, a white flash and a cone of debris, and the warship's back breaks in a chain of secondary flashes.
- **Action:** The slug arrives amidships in the first full sunlight, near the spear damage: a white flash, a spall cone, and Breakwater's back breaks in a chain of secondary flashes.
- **State:** BW: back broken
- **Light:** Breakwater in sun
- **World:** after Breakwater's sunrise (a low sun just past Maren's limb, the night side below)
- **Doctrine:** O4
- **VFX:** Impact, spall, section break
- **Rig:** break 0→1 (new)
- **Assets:** BW (new), BW-BRK (new), FX-SPINAL (new), FX-BREAK (new)
- **Sound:** One deep boom in the score, on the cut.
- **Render class:** C · **Map:** E

### 65. Heat

- **Film:** 6:26.0–6:30.0 (4 s), frames 9265–9360
- **Mission:** T+8:00:00 · 1:1
- **Camera:** MS · 35 mm · along the Endeavor's scorched port flank (hull camera)
- **Viewer sees:** Along the cruiser's scorched flank, still in the dark: a valve opens and a white plume of boiling water streams off the ship, lit faintly red.
- **Action:** Its arrays stood down when Breakwater died, but the Endeavor, still in Maren's shadow, reads 98 %. A valve opens and a thousand tonnes of water boil out in a plume lit only by the red ring of Maren's limb: half an hour of margin.
- **Comms:** ENDEAVOR: “Heat sink at nine-eight. Dumping water.”
- **On screen:** `HEAT 98%`
- **State:** EN: port fin a stump, port belt scorched
- **Light:** the escorts in umbra
- **World:** Maren's shadow (lit by the red ring of Maren's atmosphere, the night side's city glow, and the scene's own lights)
- **Doctrine:** D3, D7
- **VFX:** Water-dump plume
- **Rig:** water_dump 0→1 (new)
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), EN-PD (extend), FX-DUMP (new), SUB (new)
- **Sound:** A roar through the hull, then a long hiss.
- **Render class:** V · **Map:** E

### 66. Terms

- **Film:** 6:30.0–6:44.0 (14 s), frames 9361–9696
- **Mission:** T+8:10:00 · 1:1
- **Camera:** Tracker · 2,000 mm · from the Endeavor's standoff (tracker)
- **Viewer sees:** Through a very long lens: the wreck, a glittering smear venting in sunlight over the night side. Then a tactical plot holds alone on two dark channels.
- **Action:** Far off, 8,500 km away, Breakwater's wreck is a glittering smear venting in the new sunlight over the night side. The exchange plays first: the Compact asks for terms and says the AI's weapons in the Breakers don't answer to it (HD9), so the terms ask for their charts, with Site 1 dark and the foundries cold. Then the last plot holds alone for three seconds on the two dark channels.
- **Comms:** EXTENUATING: “Actual, Extenuating. Maren requests terms. Says the AI's guns don't answer to them.” / ACTUAL: “Then they chart them. Site One dark, foundries cold.”
- **On screen:** `CANTERBURY · NORMANDY: NO CARRIER`
- **State:** BW: back broken
- **Light:** Breakwater in sun
- **World:** after Breakwater's sunrise (a low sun just past Maren's limb, the night side below)
- **Doctrine:** O4, D7
- **VFX:** Distant wreck, HUD tag
- **Rig:** none
- **Assets:** BW (new), BW-BRK (new), MAREN (extend), RING (new), HUD (new), SUB (new)
- **Sound:** The score, low.
- **Render class:** D · **Map:** E

### 67. Site One goes dark

- **Film:** 6:44.0–6:47.0 (3 s), frames 9697–9768
- **Mission:** T+8:24:00 · 1:1
- **Camera:** Tracker · 2,000 mm · on Site 1's plateau, night side (tracker)
- **Viewer sees:** Through a very long lens on the night side: a small cluster of lights on a dark plateau goes out, block by block.
- **Action:** A cluster of lights about ten pixels wide, centred on an otherwise dark plateau whose relief just reads in the night-side glow: Site 1. They go out, block by block, and the Astrid, still dazzling it, reads the site's power and heat collapse. The fleet never struck it (§13): it goes dark on terms.
- **Comms:** ASTRID: “Site One is cold.” (at 1 s)
- **World:** after Breakwater's sunrise (a low sun just past Maren's limb, the night side below)
- **Doctrine:** §13, D3
- **VFX:** City lights going out (a comp element over a plate)
- **Rig:** none
- **Assets:** MAREN (extend), WORLD (extend), SUB (new)
- **Sound:** The score falls away.
- **Render class:** D · **Map:** E

### 68. Hold

- **Film:** 6:47.0–6:54.0 (7 s), frames 9769–9936
- **Mission:** T+8:24:03 · 1:1
- **Camera:** EWS · 35 mm · locked off, the Endeavor end-on (drone camera)
- **Viewer sees:** The cruiser end-on against the night side's city lights, its nose toward the planet: it runs out three glowing fins in a broken cross, a stump where the fourth was. Cut to black under the last line.
- **Action:** The Endeavor, end-on, keeps its nose on Site 1 until the terms are signed, so its fins stay edge-on to it. It runs out its three fins (already part-way out) in silence, into a broken cross glowing orange against the night side, the stump where the fourth was. The sun is kept just out of frame and the thin crescent clipped, so the city lights read. Cut to black under the last line.
- **Comms:** ACTUAL: “Nauvoo, Actual. Bring the shields in. T-SEC, you're next.”
- **State:** EN: port fin a stump, port belt scorched
- **Light:** the escorts in sun
- **World:** after Breakwater's sunrise (a low sun just past Maren's limb, the night side below)
- **Doctrine:** D3
- **VFX:** Fin glow
- **Rig:** fin_starboard / fin_dorsal / fin_ventral 0.5→1 (new); heat 2.4; radiator_glow
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), MAREN (extend), WORLD (extend), SUB (new)
- **Sound:** The score resolves; then silence.
- **Render class:** P · **Map:** E · **Reference frame:** `img/hero_s1combat.jpg`

## Act E: End

The report closes: a last line on black, no clock.

### 69. End of report

- **Film:** 6:54.0–6:58.0 (4 s), frames 9937–10032
- **Mission:** T+8:24:10 · after the record: no mission clock
- **Camera:** Title card · the report's last line, white monospace text over the still starfield (HUD insert)
- **Viewer sees:** The still stars of the opening fade up with the report's last line in the same white type; then everything fades to black.
- **Action:** The record closes as it opened: the report's type over the still stars, and no clock.
- **On screen:** `END OF REPORT`
- **Doctrine:** 
- **VFX:** Report text, slow fade
- **Rig:** none
- **Assets:** HUD (new), WORLD (extend)
- **Sound:** Silence.
- **Render class:** E · **Map:** E
