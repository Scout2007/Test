# Round 3 review: physics and orbital mechanics

## Verdict
No major issues. Both round 2 majors are fixed, and my own integration confirms the fixes. The lane salvos need 13.2–14.9 km/s, inside the new 15.5 km/s cap. The two-part waves close: the multi-packs need at least 44.7 min and get 45. The spinal shot now has ~15 s of margin, and all 62 clocks run continuously. What's left is minor: the new Anchor ring salvo's stated speed, decoys that can't keep pace with the killers, one close-up framed toward the wrong body, and a few rounded numbers.

## Round 2 issues: status

| Round 2 issue | Status | Note |
|---|---|---|
| 1. Skerry's nets can't reach the fleet on time (MAJOR) | Resolved (lane) | Integrated per salvo, the nets at T+6:40, 6:50, 7:00, 7:10 and 7:20 need 13.22, 13.62, 14.03, 14.44 and 14.85 km/s. The new Anchor ring doesn't close at 12.5 km/s (issue 1). |
| 2. Multi-packs can't fly the 25 min waves (MAJOR) | Resolved | 118,759 and 118,936 km in 45.0 min, against a 44.7–44.8 min minimum with the 25 % reserve. They arrive 48.6–49.0° off the zenith, and misses clear the surface by 25,200 km. New: the decoys' speed (issue 2). |
| 3. Site 1 silent for 72 min (MINOR) | Resolved | It fires from the shadow's edge; the rolls, smoke and dazzle start at once. |
| 4. Heat margin after the dump (MINOR) | Resolved | The arrays stand down at T+7:58. With 2.3 TJ of water plus the sink's remaining ~0.4–0.6 TJ, the dump lasts to ~T+8:30 on hotel load. |
| 5. Spinal on the no-escape boundary (MINOR) | Resolved | From 10,000 km the flight is 169 s with 14.5 s of margin; one number to fix (issue 5). |
| 6. The Anchor fire base (MINOR) | Resolved | The slot is hidden from Site 1 and, after T+6:55, the western site; there is no longer a claim to hide from Breakwater. |
| 7. Leaving Anchor (NIT) | Resolved | The burn tilts ~4.5°. |
| 8. The stop's frame (NIT) | Resolved | The escorts now co-move, so 8,500 km holds. The wording needs a tweak (issue 8). |
| 9. Darkness in the lee (NIT) | Resolved | The Endeavor is 15 km from the rock's centre, 7.5 km off the sun-shadow axis: dark. |

## Issues, ranked

### 1. [MINOR] The Anchor ring can't arrive by T+6:52 at 12.5 km/s (shot 44; KEY_NUMBERS; H-14)
- **Problem:** "Skerry's sixth salvo", thrown at T+0:54 at 12.5 km/s, rings Anchor at T+6:52: a 5.97 h flight.
- **Evidence:** I integrated it with Maren's gravity and Skerry's motion. The fastest 12.5 km/s round reaches Anchor at **T+7:10:40**. Arriving at T+6:52 needs **13.2 km/s**, inside the 15.5 km/s cap. (Thrown first, at T+0:04, it would need only ~11.6 km/s.)
- **Fix:** Change "12.5 for the one aimed at Anchor" to "~13.2". Also correct the lane range from "13.5–15.5" to "13.2–14.9 km/s" (nets at T+6:40–7:20). The map label "five nets T+6:40–7:30" should read "…–7:20", matching PHASES' "ten minutes apart".

### 2. [MINOR] The kill wave's decoys fly at half the killers' speed (shots 46, 48; KEY_NUMBERS)
- **Problem:** The ~40 Casaba killers "arrive among the ~300 decoy and EW birds it launched twenty minutes earlier". Those birds are multi-packs.
- **Evidence:**
  - WN §3's multi-pack tops out at 60 km/s even with no reserve, and as flown here it arrives at ~45 km/s. The killers arrive at ~88 km/s (118,524 km in 25 min).
  - Breakwater and Site 1 have tracked both groups for 25–45 min. Two populations with a 2× difference in closing speed and a 20 min gap in launch time sort themselves; no one engages a decoy that can't be a killer. That breaks §5's premise that each decoy costs the defender a retarget.
  - Even with the decoys ignored, the kill still works on WN §8's rough numbers: Breakwater's lasers take ~12, CIWS ~7 in the arrival second and Site 1 up to ~14, which leaves some of the 40 to fire. But it is thin.
- **Fix:** Put the kill wave's decoys on killer airframes launched with the Casabas at T+7:28:30, from the Galactica's ~200 remaining killers. Keep the multi-packs for EW and kill-cloud payloads, where speed doesn't matter. Update the kill-wave mix in KEY_NUMBERS and in shot 48's text.

### 3. [MINOR] *Birds away* puts Maren ahead of a missile flying at Skerry (shot 10)
- **Problem/Evidence:** Seen from the exit, wave one heads 54.7° and Maren lies at −2.5°, so they are **57° apart**. An 85 mm frame is 23.9° wide, so "ahead, screen right, Maren's thin crescent" can't share the frame with the direction of flight. The rest of the shot checks: a minute into a 30 g boost the missile is 530 km out at 17.7 km/s, still boosting (the boost runs 382 s), and the Infinity at 530 km is a spark.
- **Fix:** "Ahead, screen right, Skerry: a grey dot" (it spans ~0.37°, ~30 px at 85 mm). Leave Maren out of frame, or look back past the plume toward it.

### 4. [MINOR] The ring's pellets don't come from behind the rock (shot 44)
- **Problem/Evidence:**
  - The ring's pellets reach Anchor at 12.2 km/s from a bearing **120° away from Site 1's direction**, and each ~20 km cloud sweeps past in 1.6 s.
  - The rock blocks both directions only for a ship within ~1 km of its surface: at 1 km the rock covers a 64° half-angle, and 60° is needed. At 2 km (55°) it no longer does.
  - "Tucked in behind the rock, away from the clouds" therefore can't mean the rock shields the pack.
  - The pack's real protection is distance: clouds aimed at the rock pass ~150–200 km from its slot down Site 1's shadow.
- **Fix:** "Three clouds sweep past Anchor in a second or two; the pack, 150 km down the shadow, is clear of them." Or, if it hides behind the rock, it must sit within ~1 km of the surface for the pass.

### 5. [NIT] Spinal numbers (shots 56–58; KEY_NUMBERS)
- With the lead on a monitor moving at 3.07 km/s, the slug's path from 10,000 km is 10,148 km, which is **169 s**. Impact is therefore T+7:57:29, and the line should be "Impact in two forty-nine". The margin is ~15 s, not ~17 s. A miss still clears the surface by 6,975 km, and the line comes in 18.5° off the zenith.

### 6. [NIT] *Seeker*'s tracers (shot 52)
- The point-to-sliver growth checks. At ~88 km/s the missile is 1,230 km out when the shot opens, where Breakwater is ~8 px wide at 100 mm, and 178 km out when it ends, ~54 px. The glowing cap is right too: Breakwater's PD laser puts ~10 MW/m² on it at 1,000 km, which heats the cap but can't burn through.
- But kill clouds sit 5–30 km out, and the missile crosses them only in its last 0.06–0.34 s, after this shot ends. Drop "tracers streak past", or show them far ahead, converging on the monitor.

### 7. [NIT] *Lenses*: keep the kill close (shot 18)
- A pod missile coming at the Endeavor shows its hardened nose. Burning through it takes ~28 s at 1,000 km and ~0.3 s at 100 km (WN §1). For a kill inside the shot's 3 s, the spark should be ≲ 300 km off (~2.5 s). A seeker kill works at any range but doesn't make a spark.

### 8. [NIT] Small wording
- "Matching its orbit": at ~50,000 km the escorts can't share Breakwater's synchronous orbit. Holding station over it takes 3.65 km/s plus ~11 mg of thrust. Say "holding station on Breakwater".
- Site 1 against the slow birds: WN §8 at 45 km/s gives ~27 kills at 48°, against 15 at 80 km/s. Say "~15–30 per wave". It is still ~3 % of the waves.
- *Heat* reads 98 % at T+8:00. Hotel load plus 8 min of full dazzle gives 97 %. Either figure is fine if the low-power dazzle stays under ~1 % power: 10 W/m² at 100,000 km needs only ~15 kW of beam.

## What works
- **Skerry's lane.** All five salvos close within the cap, the defender throws each at its own speed (H-14), and 18 rounds match 3 tracks × 6 salvos.
- **The two-part waves.** Timings, angles (47.7–49.0°) and misses (24,800–25,400 km above the surface) all check. The magazine arithmetic adds up: 3 × ~720 missiles, with ~1,100 in reserve.
- **The Anchor sequence and the close-ups.** *The flash* → 16 s → hit at T+5:13:16. The broadside runs roll 15 s → wake 8 s → gun A at ~T+5:14:24 → the platform dies at T+5:14:40. The lance at 45 km is inside the ~50 km field. From the standoff, *Site One goes dark*'s ~10 px at 2,000 mm is a ~4 km light cluster at ~43,800 km, and Site 1 is on the night side.
- **Heat.** The readouts 94 → 31 → 62 (T+6:52) → 88 (T+7:50) → 97–98 % match hotel load plus the eight minutes of full dazzle.
- **Clocks.** I walked all 62 by hand: every start and jump is continuous, and every compressed rate multiplies out.
