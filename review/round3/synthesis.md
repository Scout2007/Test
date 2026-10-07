# Round 3 synthesis

Round 3 read **storyboard revision 3** (62 shots, 4:11) with the same five reviewers. Each first checked how its round 2 issues were handled, then reviewed revision 3 fresh, including the user's five weapon close-ups. They raised **2 major issues** (7 in round 2, 26 in round 1), 14 minor ones and a handful of nits. Physics, lore and cinematography had no major issue left.

**Revision 4** (61 shots, 4:08) answers both major issues and every minor one. This file records the decisions. The reports are in this folder. Shot numbers below are revision 4's unless marked "rev 3".

## The verdicts

- **Physics:** both round 2 majors are fixed, and the reviewer's own integration confirms them: the lane salvos need 13.2–14.9 km/s, inside the new 15.5 km/s cap, and the multi-packs need 44.7 min and get 45. All 62 clocks run continuously. **No major issues.** What was left: the Anchor ring salvo's stated speed, decoys that couldn't keep pace with the killers, one close-up framed toward the wrong body, and a few rounded numbers.
- **Doctrine:** four of five round 2 issues are resolved and the fifth in part. The pack's guard, the defender's try for it, Site 1's duel and the anchorage's risk all read as competent forces. One new major: the two-part launch handed the defender the Casabas.
- **Lore:** every round 2 issue is resolved, and nothing on screen contradicts the posts. **No major issues.** Three details to fix before modelling: the M-1C's wake, the missile's length, and which guns kill drones.
- **Cinematography:** every round 2 issue is fixed; the close-ups cut in well, and the M-1C run (38–41) is the film's best mechanical beat. **No major issues.** Act IV's run-up sagged, Breakwater's reveal fell inside Maren's shadow, and three beats were a second short.
- **Production:** six of seven round 2 issues are resolved, and the user's new shots cost 7.2 h. One major: the go/no-go gate could no longer protect the week.

## Major issues and decisions

| Lens | Issue | Decision | Where |
|---|---|---|---|
| Doctrine | The kill wave's ~300 decoy and EW birds left at T+7:08:30 on a 45-minute flight and arrived at ~45 km/s; its ~40 Casaba killers left twenty minutes later and arrived at ~88 km/s. Launch time and speed marked every Casaba, so the decoys never drew a shot (LREF §5, §6), and the cripple went from robust to marginal. The physics reviewer raised the same problem as a minor | The reviewer's option (a): **each wave leaves in one launch and flies one profile**, killers, decoys and EW birds together. The spend wave leaves at T+7:07, the kill wave at T+7:08:30, both on the 45-minute profile, arriving at ~45 km/s. The decoys mimic a killer's signature and size (MSL-V). *Kill wave away* (46) now plays before *The anvil* (47), which becomes Breakwater's answer to ~900 inbound birds. O3 now says it in the doctrine. At ~45 km/s the defence gets ~56 kills per wave (lasers ~21, CIWS ~7, Site 1 ~28), spread over ~340 look-alike tracks, so ~33 of the 40 Casabas reach the standoff | 45–47; PHASES, KEY_NUMBERS, FLEET; LREF O3; WN §8 |
| Production | The gate fired only above ~230 s/frame (C) or ~100 s/frame (B), the round 2 numbers, which now sat above break-even; no benchmark measured class B; and the gate, levers and plan never reached `ASSET_REQUESTS.md`, the file the modelling session (which renders) works from | **The gate works on the total.** Measured costs go into a new `MEASURED` table and replace the estimates; if the total with the allowance is over **160 h**, the levers apply in order until it isn't. The builder prints each class's break-even (C 213, B 88, A 58, A2 118, V 391 s/frame). A **class B benchmark** is added (one Endeavor in full view, sunlit, drive lit). **~5 h banked:** *Holed* and *Normandy* move to a new class S (small subject on black, ~30 s/frame), and *The wait* is locked off as class P. The **budget table, the render note, the gate and the production plan** are now written into `ASSET_REQUESTS.md` | RENDER_CLASSES, MEASURED, RENDER_NOTE; 22, 27, 56; builder |

The render estimate is now **119 h, or 155 h with the 30 % margin**: 5 h under the gate and 13 h under the week.

## Minor issues and nits

All applied.

- **Physics.**
  - **The Anchor ring salvo.** It now sweeps past Anchor as the pack fires (~T+7:07), thrown at T+0:54 at **~12.7 km/s**, checked with our own integration (which reproduces the reviewer's lane numbers to within 0.05 km/s). The lane salvos read 13.2–14.9 km/s, and map A reads "five nets on the lane T+6:40–7:20".
  - **The decoys' speed:** answered by the major fix above.
  - ***Birds away* (10):** Skerry, a small grey disc, is ahead; Maren is out of frame.
  - **The ring's pellets.** The pack is safe by distance, 150 km down the shadow, not behind the rock (45).
  - **Nits:**
    - the spinal flight is 169 s, impact **T+7:57:29**, "Impact in two forty-nine"; the builder now computes the impact from the geometry and checks the shot clock and Breakwater's state against it;
    - *Seeker*'s tracers converge far ahead on the monitor instead of streaking past;
    - *Lenses*' kill is under 300 km out;
    - "holding station on Breakwater"; Site 1 against the slow waves ~28 kills (WN §8 now has a 45 km/s column); the heat at T+8:00 reads 97–98 %.
- **Doctrine.**
  - **Nits:**
    - *Lenses* (18) cites D1;
    - *Site One goes dark* (60) cites §13 and D3 (the builder now accepts section citations);
    - *Seeker*'s shutter opens as the laser swings off to another bird;
    - the Astrid confirms Site 1's power and heat are gone;
    - the Endeavor keeps its nose on Site 1 until the terms are signed;
    - the terms ask for the Breakers charts, and the last line is "T-SEC, you're next.";
    - the Wallfish and the Donnager's CIWS kill the drones;
    - map E shows the computed impact time.
- **Lore.**
  - ***Rails wake* (39)** follows the README's wake in order: lids open on amber charge cells, the louvres ripple and the beacons flash; the clamps swing off and the crutch folds; the cradle lays; the supershell splits and lifts and the jaws open. The barrel stays dark until the bore pulse in *Fire*. The laying moved out of *Broadside* (38), since the locks must fold first.
  - **The missile's length.** The hero missile is the capital-ship killer, sized to fit the pods (no more than ~20 m), used in both 10 and 51. The built 26 m missile becomes the swarm's stand-in and base.
  - **The drones** die to the Wallfish and the Donnager's CIWS; the Donnager's batteries are there for the two Compact frigates behind the limb.
- **Cinematography.**
  - **Act IV's run-up.** *Anchor ringed* (rev 3) is folded into *The pack fires* (45): the try at the pack now has a picture, and the insert is gone. *The net* (43) runs 4 s with "Skerry's rounds. On time." / "Left two degrees."
  - **Breakwater in Maren's shadow.** The sun now sits ~12° off the ring plane (a month from Maren's equinox), so nothing at Breakwater's height is eclipsed. The eclipse look is offered to the user as Q16. In *Hold* (61) the sun is kept out of frame.
  - **Beats a second short.** *Fire* (40) is a CU and runs 3 s with the charge, shot and vent. *Terms* (59) runs 9 s, with the callback held alone for 3 s. *Site One goes dark* (60) runs 3 s, the cluster centred on a dark plateau with relief.
  - **Lines at the ceiling.** Trimmed in *The picture* (8), *The Breakers* (14), *The sweep* (30), *Fin hit* (34), *The fire plan* (42), *The net* (43) and *Blind it* (49); the film rules now ask for ~10 cps where a line waits for an event.
  - **Nits:** the sound check now works per clause, knows hiss, crack, rumble, pop, hum and thud, and ignores "no bangs"; geography inserts are checked for 5 s; *Seeker* racks focus from the cap to Breakwater as the shutter opens.
- **Production.**
  - **The hero missile:** as in lore above. `seeker_shutter` and `cap_glow` are requested on MSL-V, with spin as a swarm attribute. The builder now checks that every rig control marked new is requested by an asset.
  - **Step 1's benchmarks needed step 3's effects.** PROXY now includes benchmark-grade first versions: stock tracers and flashes, a Quick Smoke cache at both scales, a point-cloud plume and one rock tile.
  - **Nit:** Site 1's cluster is a comp element over a plate (MAREN, 60). EN-FIN carries the dark-lee fin lights.

## Doctrine and working-number changes

- **LREF O3:** "Each wave leaves in one launch and flies one profile, so its decoys can't be told from its killers by launch time or speed (§5, §6)."
- **WN §8:** Site 1's kills against an orbital target, now at 80 and 45 km/s (49°: 16 and 28).

## Left to the user

- **Q16 (new):** keep the sun tilted, which the board assumes, or light Breakwater's reveal for an eclipse.
- **Q13–Q15** stand as before.

## Round 4

Round 4 reads revision 4 with the same five reviewers, who check how their round 3 issues were handled and look for anything the changes broke: the one-launch waves and their arrival speed, the folded *The pack fires*, the moved *Kill wave away*, the gate, and the tilted sun.
