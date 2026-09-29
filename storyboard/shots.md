# Operation Tidebreak: shot list

Revision 3 · after review round 2. Runtime 4:11 (6,024 frames at 24 fps), 62 shots, mission span T+0:00 → T+8:24, 2.39:1 · 1920×804 · 24 fps · Cycles. Generated from `storyboard/tidebreak_data.py`; the page with maps and sketches is `storyboard/index.html`.

Rule IDs refer to `doctrine/LREF_doctrine.md` (O, D, A) and `doctrine/Defence_doctrine.md` (HO, HD, H). Asset IDs refer to `ASSET_REQUESTS.md`. Render classes: **A** Endeavor close-up (~45 s/frame); **A2** Endeavor close-up with heavy FX (~90 s/frame); **V** Close-up with a hero volume (the water dump) (~250 s/frame); **B** One hero ship or rock, full view (~75 s/frame); **C** Several ships or heavy FX (FX in own layers) (~200 s/frame); **P** Planet plate rendered once, plus one ship layer (~30 s/frame); **D** Wide, distant, small subject on black, or plate (~15 s/frame); **E** 2D comp / HUD (~2 s/frame).

## Mission phases

| Mission time | Phase | What happens |
|---|---|---|
| T+0:00–T+0:25 | Arrival | Exit at 450,000 km, near rest relative to Maren. Shields parked with the Nauvoo (T+0:02). Net up. Skerry starts throwing (T+0:04; three rounds every ten minutes) and its laser dazzles the Astrid's dish, so the fins stay in. Wave one away at Skerry (T+0:18). |
| T+0:25–T+0:59 | Turn and burn | 1 g along the approach line for 34 min: 0 → 20 km/s over 20,400 km. |
| T+0:59–T+3:20 | Coast | 20 km/s, bow on Maren. Skerry's laser dies at T+1:02 and its depot flushes 40 drones toward the shield park; the fins come out edge-on at T+1:10. |
| T+3:20–T+4:34 | The Breakers | Fins stowed in the debris. Site 1 dazzles; the pods wake; the Canterbury is lost (T+3:52); the Astrid answers; drones wake; the Normandy is lost (T+4:25). |
| T+4:34–T+5:09 | Turnover | Flip (49 s) and brake at 1 g for 34 min, ending on Anchor's orbital velocity (1.63 km/s; thrust tilted ~4.7°). |
| T+5:09–T+5:43 | Anchor | An 18 km rock that at T+5:09 lies over Site 1. The fleet sweeps it (a mine) but can't finish before the heat forces the fins out; it loses the port fin to a platform 400 km off, lances a frigate hidden on a moonlet, kills the platform, and vents again with three fins (94 % → 31 %). |
| T+5:43–T+7:51 | Final approach | The pack stays at Anchor as a fire base, guarded by the Donnager and the Wallfish, in the slot of the rock's shadow that hides it from Site 1 and, after T+6:55, the western site. The rest fly an inertial path of ~113,000 km: 1 g to 20 km/s (burn tilted ~4.5° to cancel the rock's orbital velocity), coast, a turnover at T+7:16 under smoke and an EW peak, one ship at a time (D8), then brake to a stop ~8,500 km from Breakwater (T+7:51), matching its orbit. The Astrid, trailing, stops 10,000 km out. Site 1 dazzles and burns from the moment the fleet clears the shadow; the fleet rolls, lays smoke and dazzles back at low power. Skerry's five nets on the lane from T+6:40, ten minutes apart, side-stepped one by one; its sixth salvo rings Anchor at T+6:52. Breakwater's 64 missiles at the Extenuating (T+7:25), killed under the Astrid's umbrella (T+7:31). |
| T+7:07–T+7:58 | Hammer and anvil | The waves leave Anchor in two parts so each lands within a second. The slow multi-packs go first (T+7:07 and T+7:08:30; 45 min flights), then the killers (T+7:27 and T+7:28:30; 25 min). The spend wave (the Infinity, ~570) lands at T+7:52:00; the kill wave (the Galactica: ~40 Casaba killers among ~300 decoy and EW birds) at T+7:53:30. Both fly straight in, nose-on to Breakwater and ~48° off its zenith, so misses and wreckage clear Maren. The Casaba jets cut the drive. The Astrid hails, then fires from rest at T+7:54:40, 15° off Breakwater's zenith; impact T+7:57:27. |
| T+7:58–T+8:24 | Terms | The Endeavor's arrays stand down when Breakwater dies; the Astrid keeps Site 1 dazzled. Sink 98 %: the Endeavor dumps water (T+8:00), which buys it to ~T+8:30. Maren asks for terms (T+8:10). Site 1 goes dark; the fleet vents at last (T+8:24). |

## Film rules

**Lighting**

- The sun sits behind Maren, about 30° off the approach line. From the fleet Maren is a thin crescent with a bright limb, and the Breakers glow faintly lit from behind (dust scatters forward).
- Hulls are lit hard from ahead and to one side; the shadow side falls to black. No stars behind sunlit hulls.
- Anchor's lee faces away from both Site 1 and the sun. The Endeavor sits within ~9 km of the rock's surface, where the two shadows overlap, so the fins, muzzle flashes and the lance light the scene (the M-1C 'fins1dark' look).
- At the end Site 1 is on the night side: a long lens sees its lights go out, and the final frame puts the Endeavor against the night side's city lights.

**Mission clock and HUD**

- The mission clock is small, persistent and clear of the subtitles. It starts on the flash in shot 1 (T+0:00:00).
- It runs at the shot's rate: spinning seconds mean compressed time, crawling ones slowed. Every jump of 30 minutes or more rolls the digits.
- One master tactical plot, always with Maren screen right. Geography inserts hold for at least 5 s, and their labels count toward the reading-speed ceiling like subtitles.
- The SINK readout appears only on HUD inserts and on hull-camera shots where the heat matters, with values that build to the dump: 94 % (31), 31 % (42), 62 % (44), 88 % (50), 98 % (59).
- Subtitles and the clock go in during the edit, after the grade, so a changed line never forces a re-render.

**Screen direction**

- Maren and the enemy stay screen right. The LREF travels and fires left to right.
- Until the turnover (shot 28) bows point right. After it bows point left while travel stays left to right, so the drives burn toward screen right.
- The final approach repeats the pattern: bows right from Anchor to the second turnover (T+7:16), bows left while braking, and the Astrid swings its bow back to screen right for the spinal shot.
- At Anchor the Endeavor's bow points at the frigate's moonlet. The frigate, off the port bow, is the one enemy on screen left; the platform, off the port quarter, stays screen right. Shots 32–41 share that axis: the platform's slugs and the broadside cross from and toward the right, the lance from right to left.
- The kill wave, the Casaba jets and the spinal slug come in from screen left, the side the waves and the Astrid are on, and Breakwater faces them from screen right (52–58).
- Enemy reverses only over an enemy foreground.

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
| 3 | 0:10.0–0:15.0 | 241–360 | T+0:00:10 | compressed 7× (13 exits over ~36 s) | The task group | EWS · 85 mm · locked off, far out on the group's flank (drone camera) | O1 D2 |
| 4 | 0:15.0–0:20.0 | 361–480 | T+0:02:00 | compressed 8× (~40 s) | Shields to the park | MS · 35 mm · riding the shield's backplate, looking back at the bow (hull camera) | O1 D9 D11 |
| 5 | 0:20.0–0:23.0 | 481–552 | T+0:02:40 | compressed 10× (the booms run out over ~30 s) | Net up | MS · 40 mm · off the Canterbury's bow (drone camera) | O2 D10 |
| 6 | 0:23.0–0:26.0 | 553–624 | T+0:03:20 | compressed 10× (the slew takes ~30 s) | The Astrid looks | MS · 50 mm · along the Astrid's dorsal hull (drone camera) | O2 D3 |
| 7 | 0:26.0–0:32.0 | 625–768 | T+0:04:10 | 1:1 | Skerry throws | HUD insert · the Astrid's telescope feed, 2,000 mm equivalent (HUD insert) | HO3 HO5 O2 |
| 8 | 0:32.0–0:39.0 | 769–936 | T+0:09:00 | compressed ~43× (the picture builds over ~5 min) | The picture | HUD insert · the master plot (HUD insert) | O2 D3 |
| 9 | 0:39.0–0:44.0 | 937–1056 | T+0:18:00 | 1:1 | Wave one | WS · 24 mm · on the Infinity's hull, shaking with each launch (hull camera) | O3 O9 D3 |
| 10 | 0:44.0–0:47.0 | 1057–1128 | T+0:19:00 | 1:1 | Birds away | CU · 85 mm · a drone camera pacing one missile (cinematic licence: it keeps up with a 30 g boost) (drone camera) | O3 O9 |
| 11 | 0:47.0–0:53.0 | 1129–1272 | T+0:25:00 | compressed 8× (the turn takes ~49 s) | Turn and burn | EWS · 400 mm · the whole group (tracker) | O1 D2 |
| 12 | 0:53.0–0:57.0 | 1273–1368 | T+1:02:00 | compressed 5× (~20 s of hits); the digits roll 36 min into it | Skerry burns | EWS · 1,200 mm · Skerry a quarter-frame disc (tracker) | O3 O9 HO8 |
| 13 | 0:57.0–1:03.0 | 1369–1512 | T+1:10:00 | compressed; the digits roll through a 2 h 10 min coast | Fins edge-on | MS · 40 mm · arcing round to dead ahead (drone camera) | D3 |
| 14 | 1:03.0–1:07.0 | 1513–1608 | T+3:20:00 | 1:1 | The Breakers | WS · 24 mm · tracking alongside (drone camera) | O8 D3 D5 D6 |
| 15 | 1:07.0–1:10.0 | 1609–1680 | T+3:30:00 | 1:1 | Blind | CU · 85 mm · the sensor mast, with its POV feed inset (hull camera) | HO5 |
| 16 | 1:10.0–1:13.0 | 1681–1752 | T+3:40:00 | compressed 10× (~30 s) | The belt wakes | WS · 40 mm · beside a rock ahead of the fleet (drone camera) | HO2 HD3 |
| 17 | 1:13.0–1:14.0 | 1753–1776 | T+3:45:00 | 1:1 | Spin-up | ECU · 100 mm · a CIWS (hull camera) | D1 |
| 18 | 1:14.0–1:17.0 | 1777–1848 | T+3:45:01 | 1:1 | Lenses | ECU · 135 mm · a laser focusing array on its yoke (hull camera) | D1 O5 |
| 19 | 1:17.0–1:21.0 | 1849–1944 | T+3:45:04 | 1:1 | Countermeasures | MS · 35 mm · along the port flank (drone camera) | D1 |
| 20 | 1:21.0–1:23.0 | 1945–1992 | T+3:52:00 | 1:1 | The platform | WS · 50 mm · over the platform's shoulder (drone camera) | HO1 HO2 HO9 |
| 21 | 1:23.0–1:25.0 | 1993–2040 | T+3:52:05 | compressed 4× (13 s flight) | Canterbury | Tracker · 1,500 mm · from the Extenuating Circumstances (tracker) | D4 |
| 22 | 1:25.0–1:30.0 | 2041–2160 | T+3:52:13 | 1:1 | Holed | Tracker · 1,500 mm · holding on the Canterbury (tracker) | HO9 |
| 23 | 1:30.0–1:34.0 | 2161–2256 | T+3:52:38 | 1:1 (the last degrees of the slew; it fires two seconds in) | Answer | EWS · 135 mm · the Astrid in profile, bow screen right (drone camera) | O4 |
| 24 | 1:34.0–1:37.0 | 2257–2328 | T+3:54:28 | the clock jumps 108 s from the shot | Payback | WS · 50 mm · the platform shot's framing (drone camera) | O4 |
| 25 | 1:37.0–1:41.0 | 2329–2424 | T+4:10:00 | compressed ~30× (2 min) | Screens out | WS · 28 mm · behind the corvettes (drone camera) | HO4 D6 O7 |
| 26 | 1:41.0–1:46.0 | 2425–2544 | T+4:14:00 | 1:1 | Return to sender | HUD insert · the Extenuating Circumstances' plot (HUD insert) | O5 HD9 D10 |
| 27 | 1:46.0–1:51.0 | 2545–2664 | T+4:25:00 | 1:1 | Normandy | Tracker · 800 mm · from the Wallfish (tracker) | HO4 |
| 28 | 1:51.0–1:57.0 | 2665–2808 | T+4:34:10 | rotation at ~4×, the middle of the 49 s flip cut out | Turnover | WS · 24 mm · on the dorsal hull looking aft (hull camera) | D8 O8 |
| 29 | 1:57.0–2:02.0 | 2809–2928 | T+5:08:00 | 1:1; the digits roll 33 min into it | Anchor | HUD insert · the master plot, zoomed (HUD insert) | D5 D2 |
| 30 | 2:02.0–2:06.0 | 2929–3024 | T+5:09:00 | compressed ~20× (minutes) | The sweep | WS · 24 mm · low over Anchor's surface (drone camera) | O8 D6 O4 |
| 31 | 2:06.0–2:10.0 | 3025–3120 | T+5:12:00 | compressed 5× (the fins take ~20 s) | Too hot | MS · 35 mm · on the stern shoulder (hull camera) | D3 D5 |
| 32 | 2:10.0–2:11.0 | 3121–3144 | T+5:13:00 | 1:1 | The flash | Tracker · 1,200 mm · on a rock 400 km off the port quarter (tracker) | HO7 HO1 |
| 33 | 2:11.0–2:14.0 | 3145–3216 | T+5:13:01 | compressed 5× (the fins crawl in against a 16 s flight) | Fins in | MS · 35 mm · the same shoulder, the clock large (hull camera) | HO7 HO1 D3 |
| 34 | 2:14.0–2:17.0 | 3217–3288 | T+5:13:16 | 1:1 | Fin hit | CU · 50 mm · on the port fin (hull camera) | HO7 D7 |
| 35 | 2:17.0–2:21.0 | 3289–3384 | T+5:13:30 | 1:1 | Off the port bow | Hull camera · 600 mm · on the Endeavor's port side (hull camera) | HO6 O6 |
| 36 | 2:21.0–2:23.0 | 3385–3432 | T+5:13:53 | 1:1 | Lance channels | CU · 28 mm · the Endeavor's nose (hull camera) | O12 |
| 37 | 2:23.0–2:25.0 | 3433–3480 | T+5:13:55 | 1:1 | Lance | Tracker · 1,000 mm · on the frigate, 45 km out (tracker) | O12 O6 |
| 38 | 2:25.0–2:28.0 | 3481–3552 | T+5:14:00 | compressed 5× (the roll) | Broadside | MS · 35 mm · the port batteries, the rock beyond (hull camera) | O6 O4 D3 |
| 39 | 2:28.0–2:32.0 | 3553–3648 | T+5:14:15 | compressed 2× (the 6–9 s wake) | Rails wake | CU · 50 mm · on one M-1C turret (hull camera) | O4 O6 |
| 40 | 2:32.0–2:34.0 | 3649–3696 | T+5:14:23 | 1:1 | Fire | ECU · 85 mm · on the muzzles (hull camera) | O4 O6 |
| 41 | 2:34.0–2:36.0 | 3697–3744 | T+5:14:40 | the clock jumps 16 s of flight from the shot | The platform dies | Tracker · 1,200 mm · the flash's framing (tracker) | O4 |
| 42 | 2:36.0–2:44.0 | 3745–3936 | T+5:40:00 | 1:1 | The fire plan | HUD insert · the master plot (HUD insert) | O9 O3 O10 O11 D11 |
| 43 | 2:44.0–2:49.0 | 3937–4056 | T+6:40:00 | compressed ~24× (2 min); the digits roll 60 min into it | The net | WS · 50 mm · over the Extenuating Circumstances (drone camera) | HO3 D4 O8 |
| 44 | 2:49.0–2:55.0 | 4057–4200 | T+6:52:00 | 1:1 | Anchor ringed | HUD insert · the Donnager's plot at Anchor (HUD insert) | HO3 HO4 HD6 D11 D6 |
| 45 | 2:55.0–2:59.0 | 4201–4296 | T+6:55:00 | compressed ~15× (a minute) | Site One | WS · 40 mm · ahead of the Extenuating Circumstances (drone camera) | HO5 D1 D3 O5 |
| 46 | 2:59.0–3:03.0 | 4297–4392 | T+7:07:00 | 1:1 | The pack fires | WS · 24 mm · low over Anchor, looking toward Breakwater (drone camera) | O3 O11 |
| 47 | 3:03.0–3:07.0 | 4393–4488 | T+7:25:00 | compressed 10× (the ripple takes ~40 s) | The anvil | WS · 40 mm · above Breakwater, Maren's night side below (drone camera) | HD7 HO9 HD1 HO1 D1 |
| 48 | 3:07.0–3:10.0 | 4489–4560 | T+7:28:30 | 1:1 | Kill wave away | Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow (tracker) | O3 O10 O11 |
| 49 | 3:10.0–3:13.0 | 4561–4632 | T+7:31:00 | 1:1 | Umbrella | Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 50 km above (tracker) | D1 D2 D10 HO9 O13 |
| 50 | 3:13.0–3:17.0 | 4633–4728 | T+7:50:00 | 1:1 | Blind it | MS · 35 mm · the Endeavor's laser arrays (hull camera) | O5 HD9 |
| 51 | 3:17.0–3:21.0 | 4729–4824 | T+7:52:00 | 1:1 | The spend wave | Tracker · 250 mm · from the Astrid, Maren's limb in frame (tracker) | O3 O5 HD5 |
| 52 | 3:21.0–3:25.0 | 4825–4920 | T+7:53:14 | compressed ~3.5× (the last 14 s of flight) | Seeker | ECU · 100 mm · riding a Casaba killer's nose (drone camera) | O3 O10 HD5 |
| 53 | 3:25.0–3:29.0 | 4921–5016 | T+7:53:28 | slowed 5× (the wave arrives within ~1 s) | Wall of fire | WS · 40 mm · above Breakwater (drone camera) | O3 HD5 O9 |
| 54 | 3:29.0–3:33.0 | 5017–5112 | T+7:53:30 | slowed 3× | Casaba | WS · 35 mm · off Breakwater's quarter (drone camera) | O10 |
| 55 | 3:33.0–3:38.0 | 5113–5232 | T+7:54:00 | 1:1 | The hail | MS · 50 mm · slow push on Breakwater over the night side (drone camera) | O10 |
| 56 | 3:38.0–3:41.0 | 5233–5304 | T+7:54:38 | 1:1 (the last degree of the slew; it fires two seconds in, at T+7:54:40) | Spinal | MS · 200 mm · the Astrid end-on (drone camera) | O4 O10 HD7 O9 |
| 57 | 3:41.0–3:47.0 | 5305–5448 | T+7:54:41 | compressed ~27× (163 of the slug's 167 s; the clock races) | The wait | WS · 35 mm · the Casaba shot's angle (drone camera) | O10 |
| 58 | 3:47.0–3:50.0 | 5449–5520 | T+7:57:27 | 1:1 | Impact | WS · 35 mm · the Casaba shot's angle (drone camera) | O4 |
| 59 | 3:50.0–3:54.0 | 5521–5616 | T+8:00:00 | 1:1 | Heat | MS · 35 mm · along the Endeavor's scorched port flank (hull camera) | D3 D7 |
| 60 | 3:54.0–4:02.0 | 5617–5808 | T+8:10:00 | 1:1 | Terms | Tracker · 2,000 mm · from the Endeavor's standoff (tracker) | O4 D7 |
| 61 | 4:02.0–4:04.0 | 5809–5856 | T+8:24:00 | 1:1 | Site One goes dark | Tracker · 2,000 mm · on Site 1's plateau, night side (tracker) | O9 |
| 62 | 4:04.0–4:11.0 | 5857–6024 | T+8:24:02 | 1:1 | Hold | EWS · 35 mm · locked off, the Endeavor end-on (drone camera) | D3 |

## Act I: Arrival

The fleet arrives slow, parks its shields, reads the system, and strikes Skerry first because Skerry's laser can burn its fins.

### 1. Black, then a star

- **Film:** 0:00.0–0:06.0 (6 s), frames 1–144
- **Mission:** T+0:00:00 · 1:1
- **Camera:** EWS · 35 mm · locked off (drone camera)
- **Action:** Starfield. A point of light swells into a blue-white bloom as the bubble collapses (~5 s). The Endeavor resolves out of it, bow screen right, shield forward, both warp rings glowing, fins stowed as they must be in warp. The mission clock starts on the flash.
- **State:** EN: shield on, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
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
- **State:** EN: shield on, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O1
- **VFX:** Emitter glow fade, RCS puffs
- **Rig:** warp_charge 0.3→0; rcs_bow pulse
- **Assets:** EN (extend)
- **Sound:** Ticking metal and RCS thumps through the truss.
- **Render class:** A · **Map:** A · **Reference frame:** `img/bow_v4b_combat.jpg`

### 3. The task group

- **Film:** 0:10.0–0:15.0 (5 s), frames 241–360
- **Mission:** T+0:00:10 · compressed 7× (13 exits over ~36 s)
- **Camera:** EWS · 85 mm · locked off, far out on the group's flank (drone camera)
- **Action:** Staggered warp flashes, seconds and 50+ km apart: the Astrid, the hedgehog pack, the Donnager, the Excelsior, both destroyers, four corvettes, the Nauvoo. Screen right, Maren is a thin crescent with the sun behind it, ringed by the faint backlit glow of the Breakers.
- **Comms:** ACTUAL · ASTRID: “All fourteen. All home.”
- **State:** DD: intact
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
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
- **State:** EN: shield parked, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O1, D9, D11
- **VFX:** Shield separation, thruster plumes
- **Rig:** shield_thrusters 1; shield_separation 0→400
- **Assets:** EN (extend), SHD (extend), TND (new), GI-PD (new), SUB (new)
- **Sound:** Clamp bangs through the backplate, then silence.
- **Render class:** A · **Map:** A · **Reference frame:** `img/endeavor_combat_demo_f060.jpg`

### 5. Net up

- **Film:** 0:20.0–0:23.0 (3 s), frames 481–552
- **Mission:** T+0:02:40 · compressed 10× (the booms run out over ~30 s)
- **Camera:** MS · 40 mm · off the Canterbury's bow (drone camera)
- **Action:** With its shield gone, the Canterbury's forward dish is clear on its truss. Its sensor booms run out and its drones scatter ahead. From here the fleet talks only by laser.
- **Comms:** CANTERBURY: “Net's up. Going quiet.”
- **State:** DD: intact
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O2, D10
- **VFX:** Drone launch
- **Rig:** booms_deploy (new); drone_bay (new)
- **Assets:** DD (new), DRN-L (new), SUB (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** A

### 6. The Astrid looks

- **Film:** 0:23.0–0:26.0 (3 s), frames 553–624
- **Mission:** T+0:03:20 · compressed 10× (the slew takes ~30 s)
- **Camera:** MS · 50 mm · along the Astrid's dorsal hull (drone camera)
- **Action:** The Astrid's 100 m AVPSA dish slews toward Maren. Its eight stacked fins stay stowed: Skerry's laser can see them.
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O2, D3
- **VFX:** 
- **Rig:** avpsa_az / avpsa_el (new)
- **Assets:** AST (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** A

### 7. Skerry throws

- **Film:** 0:26.0–0:32.0 (6 s), frames 625–768
- **Mission:** T+0:04:10 · 1:1
- **Camera:** HUD insert · the Astrid's telescope feed, 2,000 mm equivalent (HUD insert)
- **Action:** A thread of light runs along Skerry's dark limb: the mass driver throwing. Three rounds leave; the plot tags their arrival. Then a glare blooms across the feed: Skerry's laser has found the dish.
- **Comms:** ASTRID: “Skerry's throwing down our lane.” / ACTUAL: “They'll be hours.”
- **On screen:** `ARRIVE T+6:40`
- **Doctrine:** HO3, HO5, O2
- **VFX:** HUD, telescope grain, dazzle glare
- **Rig:** none
- **Assets:** HUD (new), SKR (new), FX-DAZZLE (new), SUB (new)
- **Sound:** Soft sensor tones.
- **Render class:** E · **Map:** A

### 8. The picture

- **Film:** 0:32.0–0:39.0 (7 s), frames 769–936
- **Mission:** T+0:09:00 · compressed ~43× (the picture builds over ~5 min)
- **Camera:** HUD insert · the master plot (HUD insert)
- **Action:** The master plot, Maren screen right: Breakwater parked over Site 1; Skerry, with its laser and mass driver; the Breakers; the approach line. The fins stay in while Skerry's laser can see them.
- **Comms:** ACTUAL: “Picture's up. Breakwater's right where the brief said.”
- **On screen:** `BREAKWATER` · `SKERRY` · `THE BREAKERS`
- **Doctrine:** O2, D3
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones.
- **Render class:** E · **Map:** A

### 9. Wave one

- **Film:** 0:39.0–0:44.0 (5 s), frames 937–1056
- **Mission:** T+0:18:00 · 1:1
- **Camera:** WS · 24 mm · on the Infinity's hull, shaking with each launch (hull camera)
- **Action:** The Infinity ripple-fires 150 capital-ship killers at Skerry's laser, mass driver and depot in fifteen seconds. Pod doors open in waves down the hull and the plumes curve away screen right. Skerry goes first because its laser can burn the fleet's fins all the way in.
- **Comms:** ACTUAL: “Infinity, wave one. Skerry.” / INFINITY: “Wave one away.”
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O3, O9, D3
- **VFX:** 150 missiles (swarm system), pod doors
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), SUB (new)
- **Sound:** Launch cracks through the hull; the camera shakes with each.
- **Render class:** C · **Map:** A

### 10. Birds away

- **Film:** 0:44.0–0:47.0 (3 s), frames 1057–1128
- **Mission:** T+0:19:00 · 1:1
- **Camera:** CU · 85 mm · a drone camera pacing one missile (cinematic licence: it keeps up with a 30 g boost) (drone camera)
- **Action:** Alongside one of the 150, a minute into its boost: the 26 m body in a slow spin, its plume a white-hot needle, the Infinity already a spark far behind. Ahead, screen right, Maren's thin crescent.
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O3, O9
- **VFX:** Hero missile and plume, far launch sparks
- **Rig:** thrust 1 (MSL); spin
- **Assets:** MSL (built), MSL-V (new), MAREN (extend)
- **Sound:** Silence; the score lifts.
- **Render class:** B · **Map:** A

### 11. Turn and burn

- **Film:** 0:47.0–0:53.0 (6 s), frames 1129–1272
- **Mission:** T+0:25:00 · compressed 8× (the turn takes ~49 s)
- **Camera:** EWS · 400 mm · the whole group (tracker)
- **Action:** Through a long lens, eleven drives light one after another as the group turns onto the approach line, bows toward Maren and plumes streaming screen left; the three ships at the park stay dark behind them. One g for 34 minutes.
- **Comms:** ACTUAL: “All ships, execute. One g.”
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

### 12. Skerry burns

- **Film:** 0:53.0–0:57.0 (4 s), frames 1273–1368
- **Mission:** T+1:02:00 · compressed 5× (~20 s of hits); the digits roll 36 min into it
- **Camera:** EWS · 1,200 mm · Skerry a quarter-frame disc (tracker)
- **Action:** Pinpricks of white on Skerry's limb: wave one arriving, nose-on to the battery. The light left Skerry 0.9 s ago. Just before the hits, a faint spray of points leaves the depot: its drones, flushed toward the shield park. Its eighteen rounds are already on their way.
- **Comms:** ASTRID: “Splash on Skerry. Their laser's gone.”
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** O3, O9, HO8
- **VFX:** Distant nuclear flashes, flushed drones
- **Rig:** none
- **Assets:** SKR (new), FX-NUKE (new), SUB (new)
- **Sound:** Nothing; a swell of score.
- **Render class:** D · **Map:** A

### 13. Fins edge-on

- **Film:** 0:57.0–1:03.0 (6 s), frames 1369–1512
- **Mission:** T+1:10:00 · compressed; the digits roll through a 2 h 10 min coast
- **Camera:** MS · 40 mm · arcing round to dead ahead (drone camera)
- **Action:** With Skerry's laser gone, the four fins run out, glowing a dull red. The camera arcs to dead ahead as they extend, until they collapse to slivers: edge-on to Site 1 and Breakwater, dead ahead. Far behind, the Astrid's eight fins glow like a lantern. The clock rolls on.
- **Comms:** ENDEAVOR: “Fins out. Keep them edge-on.”
- **State:** EN: shield parked, four fins
- **World:** arrival and coast (sunlit crescent, Maren 1.6°)
- **Doctrine:** D3
- **VFX:** Fin glow
- **Rig:** radiator_deploy 0.12→1; heat 0.6; radiator_glow
- **Assets:** EN (extend), AST (new), SUB (new)
- **Sound:** Silence; the score carries the coast.
- **Render class:** A · **Map:** A · **Reference frame:** `img/orbit_v8d.jpg`

### 14. The Breakers

- **Film:** 1:03.0–1:07.0 (4 s), frames 1513–1608
- **Mission:** T+3:20:00 · 1:1
- **Camera:** WS · 24 mm · tracking alongside (drone camera)
- **Action:** The fins retract before the debris. A faint haze thickens, lit from behind. A single large rock slides past twenty kilometres off, gone across the frame in under two seconds at 20 km/s. The corvettes spread ahead, screen right.
- **Comms:** ACTUAL: “No shields from here. Corvettes, sweep the lane.”
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** O8, D3, D5, D6
- **VFX:** Dust haze (Mist pass), one rock fly-by
- **Rig:** radiator_deploy 1→0.12
- **Assets:** EN (extend), BRK (new), CV (new), DRN-L (new), SUB (new)
- **Sound:** Silence; a low drone in the score.
- **Render class:** B · **Map:** B

### 15. Blind

- **Film:** 1:07.0–1:10.0 (3 s), frames 1609–1680
- **Mission:** T+3:30:00 · 1:1
- **Camera:** CU · 85 mm · the sensor mast, with its POV feed inset (hull camera)
- **Action:** Site 1's beam finds the Endeavor through the haze. The mast's optics flare, the inset feed whites out, and armoured shutters slam shut.
- **Comms:** ENDEAVOR: “Site One's painting us. Shutters.”
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO5
- **VFX:** Dazzle bloom, POV whiteout
- **Rig:** mast_shutter 0→1 (new)
- **Assets:** EN (extend), EN-MAST (extend), FX-DAZZLE (new), SUB (new)
- **Sound:** A static howl on the feed; the shutter slam through the hull.
- **Render class:** A · **Map:** B · **Reference frame:** `img/lookmast_v8d.jpg`

### 16. The belt wakes

- **Film:** 1:10.0–1:13.0 (3 s), frames 1681–1752
- **Mission:** T+3:40:00 · compressed 10× (~30 s)
- **Camera:** WS · 40 mm · beside a rock ahead of the fleet (drone camera)
- **Action:** Regolith heaves and petal doors open. Missiles tumble out cold, then light two kilometres clear and turn screen left, toward the fleet. Until now the pods were the temperature of the rock.
- **Comms:** ROCINANTE: “Launch! Cold birds off the rocks!”
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO2, HD3
- **VFX:** Pod doors, late motor ignition
- **Rig:** heave / petals (new)
- **Assets:** EMP-POD (new), MSL-V (new), BRK (new), SUB (new)
- **Sound:** Silence; a sting in the score.
- **Render class:** B · **Map:** B

### 17. Spin-up

- **Film:** 1:13.0–1:14.0 (1 s), frames 1753–1776
- **Mission:** T+3:45:00 · 1:1
- **Camera:** ECU · 100 mm · a CIWS (hull camera)
- **Action:** Seven barrels blur into motion inside the perforated jacket.
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D1
- **VFX:** 
- **Rig:** ciws_phase (new); ciws_fire (new)
- **Assets:** EN (extend), EN-PD (extend)
- **Sound:** A rising whine through the hull.
- **Render class:** A · **Map:** B

### 18. Lenses

- **Film:** 1:14.0–1:17.0 (3 s), frames 1777–1848
- **Mission:** T+3:45:01 · 1:1
- **Camera:** ECU · 135 mm · a laser focusing array on its yoke (hull camera)
- **Action:** The array's lens assembly slews onto an incoming pod missile, steadies, and flashes violet in rapid pulses, each one a shot; the beams themselves are invisible in vacuum. Far off, a spark as the missile dies, and the yoke is already swinging to the next.
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D1, O5
- **VFX:** Lens glow pulses, a distant intercept flash
- **Rig:** laser_power pulses; laser_traverse; laser_elevation
- **Assets:** EN (extend), FX-PD (new)
- **Sound:** Capacitor whine and the yoke's servo through the hull, one tick per pulse.
- **Render class:** A · **Map:** B

### 19. Countermeasures

- **Film:** 1:17.0–1:21.0 (4 s), frames 1849–1944
- **Mission:** T+3:45:04 · 1:1
- **Camera:** MS · 35 mm · along the port flank (drone camera)
- **Action:** Chaff and flares bloom and a smoke screen unfurls, thinning as it spreads. The CIWS lay kill clouds in the missiles' paths; the laser lenses glow violet, beams invisible. Missiles pop one by one.
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D1
- **VFX:** Tracers, kill clouds, chaff, smoke, intercept flashes
- **Rig:** ciws_fire (new); cm_chaff / cm_flare / cm_smoke (new); laser_power 0→1; laser_traverse
- **Assets:** EN (extend), EN-PD (extend), FX-PD (new), FX-SMOKE (new)
- **Sound:** Silence (drone camera); the score's pulse.
- **Render class:** A2 · **Map:** B · **Reference frame:** `img/lookpair_final.jpg`

### 20. The platform

- **Film:** 1:21.0–1:23.0 (2 s), frames 1945–1992
- **Mission:** T+3:52:00 · 1:1
- **Camera:** WS · 50 mm · over the platform's shoulder (drone camera)
- **Action:** A buried twin railgun heaves out of a rock 600 km ahead of the fleet and fires a ten-slug pattern screen left, straight down the fleet's path.
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO1, HO2, HO9
- **VFX:** Muzzle flashes, slug glints
- **Rig:** unmask / shot (new)
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new)
- **Sound:** Silence.
- **Render class:** B · **Map:** B

### 21. Canterbury

- **Film:** 1:23.0–1:25.0 (2 s), frames 1993–2040
- **Mission:** T+3:52:05 · compressed 4× (13 s flight)
- **Camera:** Tracker · 1,500 mm · from the Extenuating Circumstances (tracker)
- **Action:** The Canterbury, fifty kilometres off, jinks hard on RCS, its dish forward.
- **Comms:** EXTENUATING: “Canterbury, jink!”
- **State:** DD: intact
- **World:** the Breakers (backlit haze)
- **Doctrine:** D4
- **VFX:** RCS puffs
- **Rig:** rcs (new)
- **Assets:** DD (new), SUB (new)
- **Sound:** Silence.
- **Render class:** D · **Map:** B

### 22. Holed

- **Film:** 1:25.0–1:30.0 (5 s), frames 2041–2160
- **Mission:** T+3:52:13 · 1:1
- **Camera:** Tracker · 1,500 mm · holding on the Canterbury (tracker)
- **Action:** The slugs arrive from ahead. The Canterbury is holed bow to stern in three white flashes; it vents glittering ice, the hull parts in two and tumbles. Hold on it as its channel dies to hiss.
- **Comms:** EXTENUATING: “Canterbury's gone.”
- **State:** DD: intact
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO9
- **VFX:** Impact flashes, venting, section break
- **Rig:** break 0→1 (new)
- **Assets:** DD (new), DD-BRK (new), FX-BREAK (new), FX-VENT (new), SUB (new)
- **Sound:** The dying channel's hiss, then silence.
- **Render class:** B · **Map:** B

### 23. Answer

- **Film:** 1:30.0–1:34.0 (4 s), frames 2161–2256
- **Mission:** T+3:52:38 · 1:1 (the last degrees of the slew; it fires two seconds in)
- **Camera:** EWS · 135 mm · the Astrid in profile, bow screen right (drone camera)
- **Action:** The Astrid's 1.6-kilometre hull swings its last few degrees onto the platform, steadies on RCS, and two seconds in fires down the spinal: a blue-white bloom at the bow that holds to the cut.
- **Comms:** ACTUAL: “Astrid, spinal on the platform.” / ASTRID: “Firing.”
- **World:** the Breakers (backlit haze)
- **Doctrine:** O4
- **VFX:** Spinal muzzle bloom
- **Rig:** rcs_bow / rcs_stern (new); spinal_charge / spinal_shot (new)
- **Assets:** AST (new), FX-SPINAL (new), SUB (new)
- **Sound:** A sub-bass punch.
- **Render class:** B · **Map:** B

### 24. Payback

- **Film:** 1:34.0–1:37.0 (3 s), frames 2257–2328
- **Mission:** T+3:54:28 · the clock jumps 108 s from the shot
- **Camera:** WS · 50 mm · the platform shot's framing (drone camera)
- **Action:** 8,600 km away and 108 seconds later, the platform's rock erupts. The platform could not move.
- **Comms:** ASTRID GUNS: “Remember the Cant.”
- **World:** the Breakers (backlit haze)
- **Doctrine:** O4
- **VFX:** Impact eruption on the rock
- **Rig:** none
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new), SUB (new)
- **Sound:** A delayed boom in the score.
- **Render class:** B · **Map:** B

### 25. Screens out

- **Film:** 1:37.0–1:41.0 (4 s), frames 2329–2424
- **Mission:** T+4:10:00 · compressed ~30× (2 min)
- **Camera:** WS · 28 mm · behind the corvettes (drone camera)
- **Action:** Ahead, cold hides crack open on the rocks and drones pour out. The corvettes fan out to meet them, their own drones ahead.
- **Comms:** NORMANDY: “Drones waking on the rocks. Dozens.”
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO4, D6, O7
- **VFX:** Drone swarms (swarm system)
- **Rig:** none
- **Assets:** CV (new), DRN-C (new), DRN-L (new), FX-SWARM (new), BRK (new), SUB (new)
- **Sound:** A rising whine in the score.
- **Render class:** C · **Map:** B

### 26. Return to sender

- **Film:** 1:41.0–1:46.0 (5 s), frames 2425–2544
- **Mission:** T+4:14:00 · 1:1
- **Camera:** HUD insert · the Extenuating Circumstances' plot (HUD insert)
- **Action:** A block of drone tracks flips from red to teal: the drones still on a control link are hijacked and turned on their own swarm. The control craft behind the rocks is found and dazzled; the Canterbury's drifting drones are picked up. The autonomous drones keep coming.
- **Comms:** EXTENUATING: “Return to sender.”
- **On screen:** `LINKED → OURS` · `AUTONOMOUS` · `NET DEGRADED`
- **Doctrine:** O5, HD9, D10
- **VFX:** HUD, EW overlay
- **Rig:** none
- **Assets:** HUD (new), FX-EW (new), SUB (new)
- **Sound:** Clipped data chatter.
- **Render class:** E · **Map:** B

### 27. Normandy

- **Film:** 1:46.0–1:51.0 (5 s), frames 2545–2664
- **Mission:** T+4:25:00 · 1:1
- **Camera:** Tracker · 800 mm · from the Wallfish (tracker)
- **Action:** One autonomous drone slips the screen and dives on the Normandy. A plasma bomb goes off against its flank and the corvette breaks up. Hold two seconds on the wreck as its channel dies to hiss.
- **Comms:** WALLFISH: “One's through—on Normandy!”
- **World:** the Breakers (backlit haze)
- **Doctrine:** HO4
- **VFX:** Plasma-bomb flash, break-up
- **Rig:** break 0→1 (new)
- **Assets:** CV (new), CV-BRK (new), DRN-C (new), FX-SWARM (new), FX-BREAK (new), SUB (new)
- **Sound:** The dying channel's hiss, then silence.
- **Render class:** B · **Map:** B

## Act III: Anchor

Turnover into the lee of a rock over Site 1: the sweep, the heat, the fin hit, the frigate, the lance and the broadside.

### 28. Turnover

- **Film:** 1:51.0–1:57.0 (6 s), frames 2665–2808
- **Mission:** T+4:34:10 · rotation at ~4×, the middle of the 49 s flip cut out
- **Camera:** WS · 24 mm · on the dorsal hull looking aft (hull camera)
- **Action:** Under smoke and an EW peak, one ship at a time, the fleet flips. The stars wheel over the hull as the stern swings toward Maren; now the bow points screen left while the ship still travels right. The drive lights: 34 minutes of braking toward Anchor.
- **Comms:** ACTUAL: “Turnover, one at a time.”
- **State:** EN: shield parked, four fins
- **World:** the Breakers (backlit haze)
- **Doctrine:** D8, O8
- **VFX:** Main plume, RCS, smoke screen
- **Rig:** rcs_bow / rcs_stern pulses; engine_throttle 0→1; cm_smoke (new)
- **Assets:** EN (extend), EN-PD (extend), FX-SMOKE (new), SUB (new)
- **Sound:** RCS thumps, then the drive's roar through the hull.
- **Render class:** A2 · **Map:** B

### 29. Anchor

- **Film:** 1:57.0–2:02.0 (5 s), frames 2809–2928
- **Mission:** T+5:08:00 · 1:1; the digits roll 33 min into it
- **Camera:** HUD insert · the master plot, zoomed (HUD insert)
- **Action:** Anchor, an 18 km rock, with its shadow pointing away from Site 1. The fleet will string out along it; two nearby rocks are tagged '?'.
- **Comms:** ACTUAL: “Into Anchor's lee.”
- **On screen:** `ANCHOR` · `SITE 1` · `?` · `?` · `SINK 94%`
- **Doctrine:** D5, D2
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones.
- **Render class:** E · **Map:** C

### 30. The sweep

- **Film:** 2:02.0–2:06.0 (4 s), frames 2929–3024
- **Mission:** T+5:09:00 · compressed ~20× (minutes)
- **Camera:** WS · 24 mm · low over Anchor's surface (drone camera)
- **Action:** The Endeavor settles into darkness in the lee, a few kilometres off the surface, where the rock blocks the sun as well as Site 1. Corvettes and drones sweep the rock: a drone trips a mine on the far side, and the flash lights Anchor's limb from behind. Far off, the Donnager's shells land on the nearest rocks.
- **Comms:** DONNAGER: “Rocks inside three hundred done. Moonlets next.”
- **State:** EN: shield parked, four fins
- **World:** Anchor's dark lee
- **Doctrine:** O8, D6, O4
- **VFX:** Mine flash behind the limb, distant impacts
- **Rig:** rcs_bow / rcs_stern pulses
- **Assets:** EN (extend), ANCHOR (new), BRK (new), CV (new), DRN-L (new), GI (new), GI-GUN (new), FX-NUKE (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** C

### 31. Too hot

- **Film:** 2:06.0–2:10.0 (4 s), frames 3025–3120
- **Mission:** T+5:12:00 · compressed 5× (the fins take ~20 s)
- **Camera:** MS · 35 mm · on the stern shoulder (hull camera)
- **Action:** Heat alarms. The sweep isn't finished, but the sink can't wait: the slot doors slide open and all four fins telescope out, glowing orange against black, the only light in the lee.
- **Comms:** DONNAGER: “Sweep's not done.” / ENDEAVOR: “Can't wait. Fins out.”
- **On screen:** `SINK 94%`
- **State:** EN: shield parked, four fins
- **World:** Anchor's dark lee
- **Doctrine:** D3, D5
- **VFX:** Fin glow, light spill
- **Rig:** fin_* 0→1 (new); heat 1.9→2.4; radiator_glow
- **Assets:** EN (extend), EN-FIN (extend), SUB (new)
- **Sound:** Alarm tones; the fins' hydraulic groan.
- **Render class:** A · **Map:** C · **Reference frame:** `img/lookaft_s1combat.jpg`

### 32. The flash

- **Film:** 2:10.0–2:11.0 (1 s), frames 3121–3144
- **Mission:** T+5:13:00 · 1:1
- **Camera:** Tracker · 1,200 mm · on a rock 400 km off the port quarter (tracker)
- **Action:** A muzzle flash on a rock: the platform, unmasked for half a second.
- **World:** Anchor's dark lee
- **Doctrine:** HO7, HO1
- **VFX:** Muzzle flash
- **Rig:** unmask / shot (new)
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new)
- **Sound:** Silence.
- **Render class:** D · **Map:** C

### 33. Fins in

- **Film:** 2:11.0–2:14.0 (3 s), frames 3145–3216
- **Mission:** T+5:13:01 · compressed 5× (the fins crawl in against a 16 s flight)
- **Camera:** MS · 35 mm · the same shoulder, the clock large (hull camera)
- **Action:** The fins start in, crawling against the clock.
- **Comms:** ENDEAVOR: “Launch, four hundred! Fins in!”
- **State:** EN: shield parked, four fins
- **World:** Anchor's dark lee
- **Doctrine:** HO7, HO1, D3
- **VFX:** 
- **Rig:** fin_* 1→0.5 (new)
- **Assets:** EN (extend), EN-FIN (extend), SUB (new)
- **Sound:** The call; alarms; the fins' groan.
- **Render class:** A · **Map:** C

### 34. Fin hit

- **Film:** 2:14.0–2:17.0 (3 s), frames 3217–3288
- **Mission:** T+5:13:16 · 1:1
- **Camera:** CU · 50 mm · on the port fin (hull camera)
- **Action:** Halfway in, the port fin takes a slug from screen right. It shatters into glowing shards and its coolant flashes to glittering ice.
- **Comms:** ENDEAVOR: “Port fin's gone. Cut it loose.”
- **State:** EN: port fin shattering
- **World:** Anchor's dark lee
- **Doctrine:** HO7, D7
- **VFX:** Fin shatter, coolant venting
- **Rig:** fin_port_state → pre-fractured (new)
- **Assets:** EN (extend), EN-FIN (extend), FX-FIN (new), FX-VENT (new), FX-SLUG (new), SUB (new)
- **Sound:** Metal shear through the hull; a hiss.
- **Render class:** A2 · **Map:** C

### 35. Off the port bow

- **Film:** 2:17.0–2:21.0 (4 s), frames 3289–3384
- **Mission:** T+5:13:30 · 1:1
- **Camera:** Hull camera · 600 mm · on the Endeavor's port side (hull camera)
- **Action:** A Compact frigate slides out of a pre-dug cleft on the far side of a moonlet, 45 km off the port bow, and fires its coilgun. Two seconds later the camera shakes as the slug spalls the port belt.
- **Comms:** DONNAGER: “Frigate, off your port bow!”
- **State:** EN: port fin a stump
- **World:** Anchor's dark lee
- **Doctrine:** HO6, O6
- **VFX:** Coilgun flash, hull spall
- **Rig:** dmg_belt 0→1 (new)
- **Assets:** CF (new), ANCHOR (new), EN (extend), EN-FIN (extend), EN-DMG (extend), FX-SLUG (new), SUB (new)
- **Sound:** The hit through the hull.
- **Render class:** A2 · **Map:** C

### 36. Lance channels

- **Film:** 2:21.0–2:23.0 (2 s), frames 3385–3432
- **Mission:** T+5:13:53 · 1:1
- **Camera:** CU · 28 mm · the Endeavor's nose (hull camera)
- **Action:** The four lance channels in the nose glow violet-white as the field builds.
- **Comms:** ENDEAVOR: “Lance. Now.”
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O12
- **VFX:** Lance core glow
- **Rig:** lance_power 0→1
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), SUB (new)
- **Sound:** A rising electric whine through the hull.
- **Render class:** A · **Map:** C

### 37. Lance

- **Film:** 2:23.0–2:25.0 (2 s), frames 3433–3480
- **Mission:** T+5:13:55 · 1:1
- **Camera:** Tracker · 1,000 mm · on the frigate, 45 km out (tracker)
- **Action:** The ship's field reaches out and a spear of plasma crosses the frame from the right to the frigate, forty-five kilometres off, inside the ~50 km the field can hold. The frigate's midsection opens; escape pods scatter as it breaks.
- **World:** Anchor's dark lee
- **Doctrine:** O12, O6
- **VFX:** Field-held plasma jet, break-up
- **Rig:** break 0→1 (new)
- **Assets:** CF (new), FX-LANCE (new), FX-BREAK (new), FX-VENT (new)
- **Sound:** A crack in the score.
- **Render class:** B · **Map:** C

### 38. Broadside

- **Film:** 2:25.0–2:28.0 (3 s), frames 3481–3552
- **Mission:** T+5:14:00 · compressed 5× (the roll)
- **Camera:** MS · 35 mm · the port batteries, the rock beyond (hull camera)
- **Action:** Fins stowed, the Endeavor rolls to bring its port batteries onto the platform's rock, off the port quarter, screen right. The dorsal well battery rises.
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O6, O4, D3
- **VFX:** 
- **Rig:** rail_traverse; rail_elevation; battery_raise 0→1; battery_traverse; battery_elevation
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), M1C (extend)
- **Sound:** The roll's RCS thumps and the battery's rise through the hull.
- **Render class:** A · **Map:** C · **Reference frame:** `img/house_s1combat.jpg`

### 39. Rails wake

- **Film:** 2:28.0–2:32.0 (4 s), frames 3553–3648
- **Mission:** T+5:14:15 · compressed 2× (the 6–9 s wake)
- **Camera:** CU · 50 mm · on one M-1C turret (hull camera)
- **Action:** The rails unlock, the twin barrels rise onto the rock, and the charge builds: the capacitor bank's glow creeps up the housing until the turret locks.
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O4, O6
- **VFX:** Rail glow, capacitor glow
- **Rig:** rail_wake; rail_lock; rail_arm; charge_a/b
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), M1C (extend)
- **Sound:** A rising whine through the hull, then the lock's clunk.
- **Render class:** A · **Map:** C

### 40. Fire

- **Film:** 2:32.0–2:34.0 (2 s), frames 3649–3696
- **Mission:** T+5:14:23 · 1:1
- **Camera:** ECU · 85 mm · on the muzzles (hull camera)
- **Action:** Gun A fires: the bore pulse (cinematic licence, Q12) and a tracer blast toward the rock. Only the gun that fired vents; gun B waits its turn.
- **State:** EN: port fin a stump, port belt scorched
- **World:** Anchor's dark lee
- **Doctrine:** O4, O6
- **VFX:** Muzzle blast, tracer, venting
- **Rig:** shot_a; fins_a; heat_a
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), M1C (extend), FX-SLUG (new)
- **Sound:** The shot's crack and the recoil's clunk through the hull.
- **Render class:** A2 · **Map:** C

### 41. The platform dies

- **Film:** 2:34.0–2:36.0 (2 s), frames 3697–3744
- **Mission:** T+5:14:40 · the clock jumps 16 s of flight from the shot
- **Camera:** Tracker · 1,200 mm · the flash's framing (tracker)
- **Action:** The platform's rock flashes: sixteen seconds of flight, and a target that could not move.
- **World:** Anchor's dark lee
- **Doctrine:** O4
- **VFX:** Impact flash
- **Rig:** none
- **Assets:** EMP-RG (new), BRK (new), FX-SLUG (new)
- **Sound:** The score.
- **Render class:** D · **Map:** C

## Act IV: Hammer and anvil

Across to Breakwater: Skerry's nets, the try at the pack, Site 1's fire, Breakwater's missiles at the last net ship, the spend wave, the kill wave, the Casaba jets, the hail and the spinal shot, then terms.

### 42. The fire plan

- **Film:** 2:36.0–2:44.0 (8 s), frames 3745–3936
- **Mission:** T+5:40:00 · 1:1
- **Camera:** HUD insert · the master plot (HUD insert)
- **Action:** The plan builds in two beats, each tied to a clause of the line. First the waves' two tracks from Anchor to where Breakwater will be; then the Astrid's firing point. The pack stays at Anchor with its guard.
- **Comms:** ACTUAL: “Pack, Donnager and Wallfish hold Anchor. The rest, with me.”
- **On screen:** `SPEND 7:52 · KILL 7:53` · `ASTRID` · `SINK 31%`
- **Doctrine:** O9, O3, O10, O11, D11
- **VFX:** HUD
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones; the score gathers.
- **Render class:** E · **Map:** D

### 43. The net

- **Film:** 2:44.0–2:49.0 (5 s), frames 3937–4056
- **Mission:** T+6:40:00 · compressed ~24× (2 min); the digits roll 60 min into it
- **Camera:** WS · 50 mm · over the Extenuating Circumstances (drone camera)
- **Action:** Hours after Skerry threw them, the first of its rounds arrive. Ahead of the fleet the destroyer's drones light up a spreading cloud of pellets about 20 km across, glittering in their lamps. The fleet side-steps, drives angled off the line; four more nets follow on the lane, ten minutes apart.
- **Comms:** EXTENUATING: “Skerry's rounds. Right on time.” / ACTUAL: “All ships, left two degrees.”
- **State:** DD: intact
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** HO3, D4, O8
- **VFX:** Canister cloud glitter (swarm system)
- **Rig:** none
- **Assets:** DD (new), DRN-L (new), FX-SWARM (new), SUB (new)
- **Sound:** Silence; the score ticks.
- **Render class:** B · **Map:** D

### 44. Anchor ringed

- **Film:** 2:49.0–2:55.0 (6 s), frames 4057–4200
- **Mission:** T+6:52:00 · 1:1
- **Camera:** HUD insert · the Donnager's plot at Anchor (HUD insert)
- **Action:** Skerry's sixth salvo was never meant for the lane: three canister clouds ring Anchor, and drones wake on the nearby rocks behind them. The pack has tucked in behind the rock, away from the clouds; the Donnager's batteries and the Wallfish pick the drones off as they come round.
- **Comms:** DONNAGER: “Clouds on Anchor. Drones behind. Pack's tucked in.”
- **On screen:** `ANCHOR` · `3 CLOUDS` · `SINK 62%`
- **Doctrine:** HO3, HO4, HD6, D11, D6
- **VFX:** HUD, drone tracks dying
- **Rig:** none
- **Assets:** HUD (new), SUB (new)
- **Sound:** Sensor tones; clipped chatter.
- **Render class:** E · **Map:** D

### 45. Site One

- **Film:** 2:55.0–2:59.0 (4 s), frames 4201–4296
- **Mission:** T+6:55:00 · compressed ~15× (a minute)
- **Camera:** WS · 40 mm · ahead of the Extenuating Circumstances (drone camera)
- **Action:** Site 1 has been firing since the fleet cleared Anchor's shadow, against rolling hulls, smoke and the fleet's low-power dazzle. Now its invisible beam holds long enough on the destroyer's forward sensor boom: it scorches and smokes, the one visible cost. The ships roll on, and a fresh smoke screen blooms ahead, travelling with the fleet.
- **Comms:** EXTENUATING: “Site One's on our booms. Smoke forward.”
- **State:** DD: Extenuating: forward boom scorched
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** HO5, D1, D3, O5
- **VFX:** Scorching, fleet-scale smoke screen
- **Rig:** dmg_boom 0→1 (new)
- **Assets:** DD (new), FX-SMOKE (new), FX-DAZZLE (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** D

### 46. The pack fires

- **Film:** 2:59.0–3:03.0 (4 s), frames 4297–4392
- **Mission:** T+7:07:00 · 1:1
- **Camera:** WS · 24 mm · low over Anchor, looking toward Breakwater (drone camera)
- **Action:** From Anchor's shadow the Infinity ripple-fires its multi-pack missiles: hundreds of small plumes on a 45-minute flight, the slow part of the spend wave. Its last killers will follow at T+7:27 so everything lands together.
- **Comms:** ACTUAL: “Spend wave, go.” / INFINITY: “Slow birds away.”
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** O3, O11
- **VFX:** Ripple launch (swarm system)
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), ANCHOR (new), SUB (new)
- **Sound:** Silence; the score drops out.
- **Render class:** C · **Map:** D

### 47. The anvil

- **Film:** 3:03.0–3:07.0 (4 s), frames 4393–4488
- **Mission:** T+7:25:00 · compressed 10× (the ripple takes ~40 s)
- **Camera:** WS · 40 mm · above Breakwater, Maren's night side below (drone camera)
- **Action:** Breakwater's reveal. Its turrets track the fleet but stay silent: the fleet never comes within the range they could hit. Its 64 cells open and ripple-fire, every missile at the Extenuating Circumstances, 17,000 km off, into the fleet's braking burn. Far along the orbit, ring stations wake as points of light.
- **Comms:** ASTRID: “Sixty-four inbound. All on Extenuating.”
- **State:** BW: intact
- **World:** Breakwater over Maren's night side
- **Doctrine:** HD7, HO9, HD1, HO1, D1
- **VFX:** Cell doors, missile launch (swarm system)
- **Rig:** turret_traverse / cells_open (new)
- **Assets:** BW (new), RING (new), MAREN (extend), MSL-V (new), FX-SWARM (new), SUB (new)
- **Sound:** A low brass sting.
- **Render class:** C · **Map:** E

### 48. Kill wave away

- **Film:** 3:07.0–3:10.0 (3 s), frames 4489–4560
- **Mission:** T+7:28:30 · 1:1
- **Camera:** Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow (tracker)
- **Action:** Ninety seconds behind the spend wave's killers, pod doors open down the Galactica's hull and ~40 Casaba killers leave, to arrive among the ~300 decoy and EW birds it launched twenty minutes earlier. In the foreground the Pillar of Autumn's pods stay shut: the reserve.
- **Comms:** GALACTICA: “Kill wave away.”
- **World:** the final approach (Maren growing, night side)
- **Doctrine:** O3, O10, O11
- **VFX:** Ripple launch (swarm system), defocused foreground
- **Rig:** pod_ripple (new)
- **Assets:** GI (new), GI-MAV (new), MSL-V (new), FX-SWARM (new), ANCHOR (new), SUB (new)
- **Sound:** Silence.
- **Render class:** C · **Map:** D

### 49. Umbrella

- **Film:** 3:10.0–3:13.0 (3 s), frames 4561–4632
- **Mission:** T+7:31:00 · 1:1
- **Camera:** Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 50 km above (tracker)
- **Action:** Breakwater's missiles arrive up the fleet's drive axis. The Astrid has cut its drive for the minute so its plume won't blind its own point defence: its lenses glow violet and its CIWS lay kill clouds across the missiles' path. The flashes walk in toward the Extenuating and stop short.
- **Comms:** EXTENUATING: “Sixty-four down. Thanks, Actual.”
- **World:** Breakwater over Maren's night side
- **Doctrine:** D1, D2, D10, HO9, O13
- **VFX:** Kill clouds, intercept flashes, lens glow, the drive's dying glow
- **Rig:** engine_throttle 1→0 (new); laser_power (new); ciws_phase / ciws_fire (new, on the Astrid)
- **Assets:** AST (new), MSL-V (new), FX-PD (new), FX-SWARM (new), SUB (new)
- **Sound:** Silence; the score's pulse.
- **Render class:** C · **Map:** E

### 50. Blind it

- **Film:** 3:13.0–3:17.0 (4 s), frames 4633–4728
- **Mission:** T+7:50:00 · 1:1
- **Camera:** MS · 35 mm · the Endeavor's laser arrays (hull camera)
- **Action:** The Extenuating Circumstances floods the ring's links. The arrays go from low power to full on Breakwater's optics and Site 1's trackers: lenses violet, beams invisible.
- **Comms:** EXTENUATING: “Their net's down.” / ENDEAVOR: “All arrays, full power.”
- **On screen:** `SINK 88%`
- **State:** EN: port fin a stump, port belt scorched
- **World:** Breakwater over Maren's night side
- **Doctrine:** O5, HD9
- **VFX:** Lens glow, EW overlay on inserts
- **Rig:** laser_power 0.2→1; laser_traverse; laser_elevation
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), FX-EW (new), SUB (new)
- **Sound:** The lenses' capacitor whine through the hull.
- **Render class:** A · **Map:** E · **Reference frame:** `img/lookyoke_final.jpg`

### 51. The spend wave

- **Film:** 3:17.0–3:21.0 (4 s), frames 4729–4824
- **Mission:** T+7:52:00 · 1:1
- **Camera:** Tracker · 250 mm · from the Astrid, Maren's limb in frame (tracker)
- **Action:** Five degrees off Maren's limb, a sparkle: the spend wave dying against Breakwater's point defence, which lights up and gives away every battery. The destroyer steers the kill wave around them.
- **Comms:** EXTENUATING: “Their batteries are lit. Steering round.”
- **State:** BW: intact
- **World:** Breakwater over Maren's night side
- **Doctrine:** O3, O5, HD5
- **VFX:** Distant PD sparkle
- **Rig:** none
- **Assets:** BW (new), FX-PD (new), MAREN (extend), SUB (new)
- **Sound:** The score.
- **Render class:** D · **Map:** E

### 52. Seeker

- **Film:** 3:21.0–3:25.0 (4 s), frames 4825–4920
- **Mission:** T+7:53:14 · compressed ~3.5× (the last 14 s of flight)
- **Camera:** ECU · 100 mm · riding a Casaba killer's nose (drone camera)
- **Action:** The hardened nose of a Casaba killer through its last seconds. The ablative cap glows where Breakwater's lasers are burning it, and tracers streak past; then the seeker shutter opens, and ahead, screen right, Breakwater grows from a point to a sliver.
- **State:** BW: intact
- **World:** Breakwater over Maren's night side
- **Doctrine:** O3, O10, HD5
- **VFX:** Glowing ablative cap, tracers, the seeker window
- **Rig:** spin; seeker_shutter (new)
- **Assets:** MSL-V (new), FX-PD (new), BW (new)
- **Sound:** Silence; the score climbs.
- **Render class:** B · **Map:** E

### 53. Wall of fire

- **Film:** 3:25.0–3:29.0 (4 s), frames 4921–5016
- **Mission:** T+7:53:28 · slowed 5× (the wave arrives within ~1 s)
- **Camera:** WS · 40 mm · above Breakwater (drone camera)
- **Action:** The kill wave arrives in the same second, nose-on to Breakwater, from screen left. Tracers and dying decoys fill the sky; the hardened noses keep coming.
- **Comms:** GALACTICA: “Kill wave. Three, two—”
- **State:** BW: intact
- **World:** Breakwater over Maren's night side
- **Doctrine:** O3, HD5, O9
- **VFX:** Tracer streams, intercept flashes, swarm
- **Rig:** ciws_fire (new, on Breakwater)
- **Assets:** BW (new), FX-PD (new), FX-SWARM (new), MSL-V (new), SUB (new)
- **Sound:** A dense crackle in the score; no air, no bangs.
- **Render class:** C · **Map:** E

### 54. Casaba

- **Film:** 3:29.0–3:33.0 (4 s), frames 5017–5112
- **Mission:** T+7:53:30 · slowed 3×
- **Camera:** WS · 35 mm · off Breakwater's quarter (drone camera)
- **Action:** Two kilometres out, the surviving Casaba charges fire from screen left: nuclear jets lance into Breakwater's drive bells and its engines go dark. The monitor is whole, but it can no longer move.
- **Comms:** ASTRID: “Spears in. Her drive's dark.”
- **State:** BW: drive breached, venting
- **World:** Breakwater over Maren's night side
- **Doctrine:** O10
- **VFX:** Casaba jets, drive breach, venting
- **Rig:** drive_glow 1→0 (new); vent (new)
- **Assets:** BW (new), BW-BRK (new), MSL-V (new), FX-CASABA (new), FX-VENT (new), SUB (new)
- **Sound:** The comm channels white out, then silence.
- **Render class:** C · **Map:** E

### 55. The hail

- **Film:** 3:33.0–3:38.0 (5 s), frames 5113–5232
- **Mission:** T+7:54:00 · 1:1
- **Camera:** MS · 50 mm · slow push on Breakwater over the night side (drone camera)
- **Action:** Breakwater hangs dead-engined over Maren's night side, venting from the spear wounds, its turrets still tracking. On an open channel the Astrid hails it. No answer comes.
- **Comms:** ACTUAL: “Breakwater, you can't move. Strike, or we fire.”
- **State:** BW: drive breached, venting
- **World:** Breakwater over Maren's night side
- **Doctrine:** O10
- **VFX:** Venting
- **Rig:** vent (new)
- **Assets:** BW (new), BW-BRK (new), MAREN (extend), FX-VENT (new), SUB (new)
- **Sound:** Silence where the answer should be.
- **Render class:** B · **Map:** E

### 56. Spinal

- **Film:** 3:38.0–3:41.0 (3 s), frames 5233–5304
- **Mission:** T+7:54:38 · 1:1 (the last degree of the slew; it fires two seconds in, at T+7:54:40)
- **Camera:** MS · 200 mm · the Astrid end-on (drone camera)
- **Action:** The Astrid, stopped 10,000 km out and 15° off Breakwater's zenith so a miss would clear Maren, settles its last degree and fires. The bloom fills the last second.
- **Comms:** ACTUAL: “Fire.”
- **World:** Breakwater over Maren's night side
- **Doctrine:** O4, O10, HD7, O9
- **VFX:** Spinal muzzle bloom
- **Rig:** rcs_bow / rcs_stern (new); spinal_shot (new)
- **Assets:** AST (new), FX-SPINAL (new), SUB (new)
- **Sound:** Everything drops out.
- **Render class:** B · **Map:** E

### 57. The wait

- **Film:** 3:41.0–3:47.0 (6 s), frames 5305–5448
- **Mission:** T+7:54:41 · compressed ~27× (163 of the slug's 167 s; the clock races)
- **Camera:** WS · 35 mm · the Casaba shot's angle (drone camera)
- **Action:** Hold on the crippled monitor, turrets swinging uselessly, while the clock races through the slug's flight.
- **Comms:** ASTRID: “Impact in two forty-seven.”
- **State:** BW: drive breached, venting
- **World:** Breakwater over Maren's night side
- **Doctrine:** O10
- **VFX:** Venting
- **Rig:** turret_traverse (new)
- **Assets:** BW (new), BW-BRK (new), SUB (new)
- **Sound:** Silence; one held note.
- **Render class:** B · **Map:** E

### 58. Impact

- **Film:** 3:47.0–3:50.0 (3 s), frames 5449–5520
- **Mission:** T+7:57:27 · 1:1
- **Camera:** WS · 35 mm · the Casaba shot's angle (drone camera)
- **Action:** The slug arrives amidships, near the spear damage: a white flash, a spall cone, and Breakwater's back breaks in a chain of secondary flashes.
- **State:** BW: back broken
- **World:** Breakwater over Maren's night side
- **Doctrine:** O4
- **VFX:** Impact, spall, section break
- **Rig:** break 0→1 (new)
- **Assets:** BW (new), BW-BRK (new), FX-SPINAL (new), FX-BREAK (new)
- **Sound:** One deep boom in the score, on the cut.
- **Render class:** C · **Map:** E

### 59. Heat

- **Film:** 3:50.0–3:54.0 (4 s), frames 5521–5616
- **Mission:** T+8:00:00 · 1:1
- **Camera:** MS · 35 mm · along the Endeavor's scorched port flank (hull camera)
- **Action:** Its arrays stood down when Breakwater died, but the Endeavor's sink still reads 98 %. A valve opens and a thousand tonnes of water boil out in a white plume streaming off the ship: half an hour of margin.
- **Comms:** ENDEAVOR: “Dump the water.”
- **On screen:** `SINK 98%`
- **State:** EN: port fin a stump, port belt scorched
- **World:** Breakwater over Maren's night side
- **Doctrine:** D3, D7
- **VFX:** Water-dump plume
- **Rig:** water_dump 0→1 (new)
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), EN-PD (extend), FX-DUMP (new), SUB (new)
- **Sound:** A roar through the hull, then a long hiss.
- **Render class:** V · **Map:** E

### 60. Terms

- **Film:** 3:54.0–4:02.0 (8 s), frames 5617–5808
- **Mission:** T+8:10:00 · 1:1
- **Camera:** Tracker · 2,000 mm · from the Endeavor's standoff (tracker)
- **Action:** Far off, 8,500 km away, Breakwater's wreck is a glittering smear venting over the night side; the Astrid's firing line has already swung onto the next ring station. The exchange plays first; then the last plot holds alone for two seconds on the two dark channels.
- **Comms:** EXTENUATING: “Actual, Maren's asking for terms.” / ACTUAL: “Site One goes dark first.”
- **On screen:** `CANTERBURY · NORMANDY: NO CARRIER`
- **State:** BW: back broken
- **World:** Breakwater over Maren's night side
- **Doctrine:** O4, D7
- **VFX:** Distant wreck, HUD tag
- **Rig:** none
- **Assets:** BW (new), BW-BRK (new), MAREN (extend), RING (new), HUD (new), SUB (new)
- **Sound:** The score, low.
- **Render class:** D · **Map:** E

### 61. Site One goes dark

- **Film:** 4:02.0–4:04.0 (2 s), frames 5809–5856
- **Mission:** T+8:24:00 · 1:1
- **Camera:** Tracker · 2,000 mm · on Site 1's plateau, night side (tracker)
- **Action:** A cluster of lights on Maren's night side, about ten pixels wide: Site 1. They go out, block by block.
- **Comms:** ENDEAVOR: “Site One's dark.”
- **World:** Breakwater over Maren's night side
- **Doctrine:** O9
- **VFX:** City lights going out
- **Rig:** none
- **Assets:** MAREN (extend), WORLD (extend), SUB (new)
- **Sound:** The score falls away.
- **Render class:** D · **Map:** E

### 62. Hold

- **Film:** 4:04.0–4:11.0 (7 s), frames 5857–6024
- **Mission:** T+8:24:02 · 1:1
- **Camera:** EWS · 35 mm · locked off, the Endeavor end-on (drone camera)
- **Action:** The Endeavor, end-on, runs out its three fins (already part-way out) in silence, into a broken cross glowing orange against the night side, the stump where the fourth was. Cut to black under the last line.
- **Comms:** ACTUAL: “Nauvoo, bring the shields in. T-SEC, the sky's yours.”
- **State:** EN: port fin a stump, port belt scorched
- **World:** Breakwater over Maren's night side
- **Doctrine:** D3
- **VFX:** Fin glow
- **Rig:** fin_starboard / fin_dorsal / fin_ventral 0.5→1 (new); heat 2.4; radiator_glow
- **Assets:** EN (extend), EN-FIN (extend), EN-DMG (extend), MAREN (extend), WORLD (extend), SUB (new)
- **Sound:** The score resolves; then silence.
- **Render class:** P · **Map:** E · **Reference frame:** `img/hero_s1combat.jpg`
