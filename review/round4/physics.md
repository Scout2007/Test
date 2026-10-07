# Round 4 review: physics and orbital mechanics

## Verdict
No major issues. Every round 3 issue is fixed, and the rev 4 changes hold up under my own integration:
- the ring salvo needs 12.68 km/s to reach Anchor at T+7:07;
- both waves fly 45 min and arrive 48.6° and 49.0° off Breakwater's zenith, with misses clearing Maren's surface by ~25,000 km;
- the builder's spinal numbers match mine: 10,150 km, 169.2 s, impact T+7:57:29, a miss 7,006 km above Maren;
- the tilted sun keeps Anchor's lee dark and Breakwater out of Maren's shadow.

What's left is one wording gap in the new "one profile" rule, which matters for the decoys, plus three nits.

## Round 3 issues: status

| Round 3 issue | Status | Note |
|---|---|---|
| 1. Anchor ring can't arrive at 12.5 km/s (MINOR) | Resolved | Thrown at T+0:54, it needs 12.68 km/s for T+7:07:00; at 12.7 it passes at ~T+7:06:40. The lane salvos read 13.2–14.9 km/s, and map A reads T+6:40–7:20. |
| 2. Decoys at half the killers' speed (MINOR) | Resolved | One launch per wave, one flight time, ~45 km/s arrival. One caveat on the boost (issue 1). |
| 3. *Birds away* aimed at Maren (MINOR) | Resolved | Skerry is ahead and Maren out of frame. Skerry's phase is a nit (issue 3). |
| 4. The ring's pellets vs the rock (MINOR) | Resolved | The pack is safe by distance, 150 km down the shadow, and the clouds pass wide. |
| 5. Spinal numbers (NIT) | Resolved | Computed by the builder: 169.2 s, "two forty-nine", ~15 s of margin. |
| 6. *Seeker*'s tracers (NIT) | Resolved | They converge far ahead. At 45 km/s the missile crosses the 30 → 5 km kill-cloud zone in its last 0.66–0.11 s, after the shot ends. |
| 7. *Lenses*' kill range (NIT) | Resolved | Under 300 km. |
| 8. Wording (NIT) | Resolved | Station-keeping (3.65 km/s plus ~11 mg), ~28 Site 1 kills at 45 km/s, 97–98 % heat. |

## Issues, ranked

### 1. [MINOR] "One profile" has to mean the killers' 30 g boost (PHASES, KEY_NUMBERS, LREF O3; shots 45–46)
- **Problem:** KEY_NUMBERS says each wave flies "the multi-packs' 45-minute profile". The multi-packs' WN §3 profile boosts at 50 g, but the killers are 30 g missiles and can't follow it.
- **Evidence:**
  - At 50 g the decoys reach cruise in 91 s; at 30 g the killers need 154 s.
  - For the first two and a half minutes, the acceleration and the length of the plumes would mark every killer. That is the same sorting the round 3 fix set out to remove, just earlier.
  - With the whole wave boosting at 30 g, the flights still close: 45.0 min needs a 45.3 km/s cruise (118,759 km and 118,936 km).
  - That leaves the multi-packs 24.4 % of their 60 km/s, a hair under A-25's quarter, which is fine.
- **Fix:** Write "one 45-minute profile, boosting at the killers' 30 g (the multi-packs throttle down)" in O3, PHASES and KEY_NUMBERS. Nothing on screen changes.

### 2. [NIT] The kill wave's odds are a floor, not an estimate (KEY_NUMBERS)
- The "~56 kills" row counts Site 1's ~28 and Breakwater's lasers' ~21 as if each wave had them to itself. But both waves are in flight together (T+7:08:30–7:52:00), and the run-ins from 10,000 km overlap for ~130 s.
- Site 1 also has one beam, and it is dazzled at full power from T+7:50, just as the waves come closest.
- So the defence's share per wave is lower, and "~33 of the 40 Casabas" is a minimum. Say "at least ~33".

### 3. [NIT] Skerry is a crescent, not a grey disc (shots 10, 12)
- With the sun ~30° off the approach line and ~12° up, Skerry seen from the fleet near the exit has a phase angle of ~153°: only ~6 % of its disc is lit.
- In *Birds away* it is 0.38° across (~30 px at 85 mm). Call it "a thin bright crescent on a dark disc".
- The same holds for *Skerry burns*' quarter-frame disc. "Pinpricks on the limb" and the "dark limb" in *Skerry throws* already fit.

### 4. [NIT] Anchor's lee is dark, but only just (LIGHTING; map C)
- With the sun 12° above the ring plane, the sun's shadow axis and Site 1's are 32.1° apart (30.0° before).
- The Endeavor, 15 km out on Site 1's axis, sits 7.97 km off the sun's axis, where the umbra's radius is 8.94 km. It is dark, with ~1 km of margin.
- Keep the lee shots (29–41) on the Endeavor's marked position, or nudge it a few km toward the bisector of the two axes (the overlap runs out ~33 km along it). Otherwise a camera move could put the hull in sunlight.

## What works
- **The waves.** Each flies 45.0 min from Anchor (the multi-packs' minimum is 44.7 min) and arrives ~45 km/s, 48.6° and 49.0° off the zenith. Misses pass 25,244 km and 25,435 km above the surface. The decoys now share the killers' launch time and speed, and with the fix above their acceleration too. The spend wave lands 90 s ahead, and a 90 s steer around the lit batteries costs the killers almost nothing.
- **The ring.** 12.68 km/s puts three clouds past Anchor at T+7:07, "six hours" after the throw. The pellets arrive at ~12 km/s from 120° off Site 1's direction, and each cloud crosses in ~1.6 s. Aimed at the rock, they pass ~150 km from the pack's slot. The spend wave's missiles reach the rock's distance ~30 s after launch, long after the clouds have gone.
- ***Seeker* at 45 km/s.**
  - The shot opens 728 km out, where Breakwater is ~13 px wide at 100 mm, and ends 93 km out at ~104 px: a point to a sliver.
  - Breakwater's PD laser puts ~2×10⁷ W/m² on the cap at that range, so it glows but would take ~230 s to burn through; the glow fading as the beam moves on is right.
  - Shot 45's view from the pack's slot works too: the rock is a 6.9° black disc, and Breakwater sits just past its limb, so the missiles clear it.
- **The sun.** At ~12° above the plane (the declination a month from equinox with an Earth-like tilt), Breakwater's orbit never comes closer than 8,766 km to Maren's shadow axis, against a ~6,200 km umbra, so no eclipse. Site 1 stays on the night side for the ending.
- **The spinal.** It is built from the geometry now: from rest at 10,000 km and 15° off the zenith, the slug leads a 3.07 km/s target. It flies 10,150 km in 169.2 s, ~15 s inside the no-escape time, and a miss clears the surface by 7,006 km.
- **The clocks.**
  - *The pack fires* (T+7:06:57) holds both the clouds and the T+7:07:00 launch.
  - *Kill wave away* (T+7:08:30) now comes before *The anvil* (T+7:25), and the order and ~900 birds inbound are consistent.
  - *Seeker* 14 s, *Wall of fire* 0.8 s and *Casaba* 1.3 s chain to the jets at T+7:53:30.
  - *The wait*'s 6 s at ~27× leaves the 169 s flight landing on *Impact* at T+7:57:29.
  - The last shots run on to T+8:24:03.
