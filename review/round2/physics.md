# Round 2 review: physics and orbital mechanics

## Verdict
Revision 2 fixes most of what round 1 found, and the fixes check out: the inertial approach, the ~48° wave geometry, the backstop clearances, the spinal shot from rest, the heat thread to T+8:00, the Anchor sequence and every shot's clock. Two new problems break the doctrine's own numbers. With the rev 2 geometry, Skerry's 12.5 km/s rounds can't reach any of the six nets on time. And most of the missiles in "hundreds of plumes" are multi-packs that can't fly 118,000 km in 25 minutes. Both have fixes that keep the beats.

## Round 1 issues: status

| Round 1 issue | Status | Note |
|---|---|---|
| 1. The Astrid can't stop after its spinal shot | Resolved | Fires from rest 10,800 km out. The margin is only ~1 s (issue 5). |
| 2. "The line" rotates away | Resolved | Inertial path of 112,915 km, turnover T+7:16:17, stop T+7:51:05 (confirmed). The waves fly straight. |
| 3. Maren is the backstop | Resolved | The waves arrive 47.7–48.1° off Breakwater's zenith, and their misses pass 24,800 km above the surface. The spinal line comes in 18.6° off and clears the surface by 7,063 km. |
| 4. Heat readouts | Resolved | 31 % at T+5:43 and 98 % at T+8:00 both check out. The margin after the dump depends on the arrays (issue 4). |
| 5. Two hours in Site 1's sky | Partly | Site 1 now fires, but only from T+6:55; the fleet is exposed from T+5:43 (issue 3). |
| 6. Skerry's rounds too slow | Not resolved | The new path puts the lane 320,000–365,000 km from Skerry (issue 1). |
| 7. The shadow is narrower than stated | Partly | The Astrid sits within ~300 km. The pack at Anchor now faces a second ground site (issue 6). |
| 8. The fins retract faster than the slugs arrive | Resolved | 400 km at 25 km/s is 16 s, which leaves the fins about half in. |
| 9. The Endeavor is far from the wreck at the terms | Partly | Now a 2,000 mm view from the standoff, but the standoff drifts (issue 8). |
| 10. Small numbers | Resolved | All applied. |

## Issues, ranked

### 1. [MAJOR] Skerry's nets can't reach the fleet on time (shots 7, 38; map A; H-14)
- **Problem:** The six nets are timed for T+6:40–T+7:30. Rev 2 mirrors the map (fleet from −x, Skerry at 140°) but keeps Maren's rotation, so the final approach now swings *away* from Skerry.
- **Evidence:** I integrated each salvo with Maren's gravity, Skerry's orbital motion, and 12.5 km/s at launch, aimed at `final_at` on the planned arrival time.
  - Salvo 1 (T+0:04 → T+6:40) must cover 319,700 km. Its fastest flight is 6.98 h, so it arrives no earlier than **T+7:03**.
  - The later salvos must cover 328,800–364,600 km. Their earliest arrivals are T+7:25, 7:48, 8:10, 8:33 and 8:53.
  - While coasting, the fleet recedes from Skerry at ~15 km/s, faster than the rounds, so they only catch it after it stops (~T+8:10).
  - Moving Skerry to 220° (the other side of the axis) is not enough: salvo 1 still arrives at T+6:47 and salvo 6 at T+8:09.
- **Fix:**
  - Preferred: raise H-14 (unstarred) to **~15 km/s**. Integrated, 13.8 km/s already lands salvo 1 early (6.33 h against the 6.60 h available) and 15.6 km/s lands salvo 6 early (6.42 h), so salvo 1 needs ~13.5 km/s and salvo 6 ~15.2 km/s. The mass driver throws the earlier salvos slower. Energy is ~1.1 TJ per round.
  - Or keep 12.5 km/s and give the nets one beat: a single net, met during the braking burn, from rounds aimed at the lane's end.
  - Either way, update the HUD's "ARRIVE T+6:40".

### 2. [MAJOR] The multi-pack missiles can't fly the 25-minute waves (shots 41–42, 45; A-26, WN §3)
- **Problem:** The spend wave is "everything [the Infinity] has left … hundreds of plumes". The kill wave carries "EW missiles and decoys" alongside the Casabas. Both fly Anchor → Breakwater in 25 min.
- **Evidence:**
  - The flights are 118,349 km and 118,524 km, an average of 79 km/s.
  - Wave one's 150 had to be capital-ship killers: only those reach Skerry by T+1:02 (43.9 min).
  - By A-26, the Infinity is therefore left with ~90 killers and **~480 multi-pack missiles**.
  - WN §3's multi-pack (50 g, 60 km/s) needs 44.6 min with its 25 % reserve, or 33.9 min spending all its Δv. Its missiles would land at T+8:02–8:12, after the kill wave and the spinal shot.
  - The capital-ship killers are fine: they fly the 25 min by cruising at ~88 km/s and keep 42 % in reserve. (WN §8's 80 km/s case matches.)
- **Fix:** Launch the multi-pack share from Anchor at **~T+7:07** (44.6 min flight). "The pack fires" can open on it, or it can be mentioned in shot 37. The capital-ship killers still go at T+7:27 and T+7:28:30, and all arrive on the same seconds. Alternatively, say the waves' decoys and EW missiles ride capital-ship-killer airframes.

### 3. [MINOR] Site 1 holds fire for 72 minutes after the fleet leaves the shadow (shots 37–39; phases)
- **Problem/Evidence:** From T+5:43 the whole approach is 74–86° up in Site 1's sky, at 144,000 km at T+5:43, 98,000 km at T+6:40 and 44,000 km at the stop. At 144,000 km a 2 GW site kills a sensor window in ~2 s and a fin in ~42 s (WN §1). Nothing physical (range, horizon, haze) stops it firing from ~T+5:45.
- **Fix:** Start the rolls, the smoke and Site 1's dazzle at departure. Keep shot 39 at T+6:55 as the moment it finally burns a boom: "Site One's on our booms" after an hour of trying.

### 4. [MINOR] After the dump, the heat margin depends on the arrays (shots 44, 52–54)
- **Problem/Evidence:**
  - Recomputing with WN §4 gives 95 % after the Anchor fight and 31 % after 28 min of three fins. Running dark gives 92 % at T+8:00, and **the ten minutes of dazzle from T+7:50 make it 98 %**, so the dazzle is accounted for.
  - The dump plus the 2 % headroom (2.7 TJ) lasts 30 min on hotel load alone (to T+8:30), so fins out at T+8:24 works.
  - But shot 44 also dazzles Site 1, which stays live until T+8:24. If the Endeavor's arrays stay on to the terms (T+8:10), the sink is full at **~T+8:18**; if they stay on to T+8:24, at ~T+8:14.
- **Fix:** Say the Endeavor's arrays stand down when Breakwater dies (T+7:58), and the Astrid (60 TJ) keeps Site 1 dazzled. Or bring the fins out at ~T+8:12.

### 5. [MINOR] The spinal shot sits on the no-escape boundary (shots 49–51; KEY_NUMBERS)
- **Problem/Evidence:**
  - With the Astrid at inertial rest, Breakwater moves 565 km during the flight (a 2.8° lead) and opens the range at 0.94 km/s. The slug's path is therefore 10,964 km: **182.7 s**, not 184.
  - WN §2 gives the crippled monitor 183.6 s to clear 800 m, so the margin is under 1 s. The no-escape range at that opening speed is 10,844 km, against a 10,800 km standoff.
  - (A miss clears the surface by 7,063 km, as the board says.)
- **Fix:** Stop at ~10,000 km. The flight is then ~167 s, with ~17 s of margin, and the miss geometry is unchanged. Set the flight to "~2.8 min" and shot 50 to compressed ~42×.

### 6. [MINOR] Anchor as a fire base: a second site, and Breakwater (shots 37, 41–42)
- **Problem/Evidence:**
  - Following Site 1's shadow is cheap: the line turns 8.5×10⁻⁶ rad/s, which is 1.5 m/s sideways at 180 km behind the rock.
  - But Anchor drifts west toward the next site. It rises above that site's 20° lethal elevation at **~T+6:55** and reaches 27.5° by T+7:28.
  - From Anchor, that site's shadow lies 3.4° from Site 1's. Both can be hidden only in their overlap: ~7 km wide at 180 km behind the rock, and gone beyond ~300 km.
  - Breakwater's sight line is 9° off by T+7:27, so it sees the pack. That is harmless at 110,000 km: its heavy railgun needs ~1 h to get there.
- **Fix:** "The pack holds Anchor's lee from Site 1 and, after T+6:55, the western site too: a slot a few kilometres wide within ~200 km of the rock." Drop any claim that it is hidden from Breakwater.

### 7. [NIT] Leaving Anchor (phases; map D)
- The fleet starts with Anchor's 1.63 km/s. Of that, 1.58 km/s lies across the path, which would drift the fleet 12,100 km if uncorrected. Maren's gravity alone moves the stop by ~1,100 km, with 0.5 km/s left over. Mirror the arrival note: "the burn tilts ~4.5° to cancel the rock's orbital velocity" (and trim the brake).

### 8. [NIT] "Stop" means inertial rest, so Breakwater walks away (shots 50–53)
- Stopped inertially at T+7:51, the escorts are 8,698 km from Breakwater at the kill, 10,487 km at the terms and 12,404 km at T+8:24. The terms shot says 8,500 km. Either write ~10,500 km, or have the escorts co-move with Breakwater (3.65 km/s tangential plus 11 mg of inward thrust).

### 9. [NIT] Darkness in the lee (map C; shot 28)
- The sun lies 30° off Site 1's direction as seen from Anchor, so the two shadow columns overlap only within ~18 km of the rock's centre. Map C's Endeavor, 30 km from the centre, sits 15 km off the sun-shadow axis and is sunlit. Put it within ~9 km of the lee surface.

## What works
- **The final approach:** 112,915 km, turnover at T+7:16:17 and stop at T+7:51:05 all reproduce. The fleet is 4–15° from Site 1's zenith as seen from Maren's centre, and the escorts' stop is 2,357 km clear of the spinal line and 2,954 km from the kill wave's track.
- **The waves:** 48° off the zenith, with misses 31,200 km from Maren's centre. Site 1's closest approach to any missile is 35,764 km (at Breakwater), so WN §8's ~15 kills per wave follows. The capital-ship killers fly the 25 min on 58 % of their Δv.
- **Breakwater's 64 missiles:** the fleet is 17,264 km out at T+7:25 and braking (15.3 → 11.8 km/s), and the six-minute intercept needs ~36 km/s average, fine for a pod-class missile. The Astrid's ≥ 25 arrays can kill 64 nose-on missiles (WN §8 scaled).
- **The Anchor sequence:** 400 km at 25 km/s is 16 s; the coilgun at 45 km takes 2.25 s; a 2 g frigate closes 45 → 40 km in ~23 s; the broadside at T+5:14:15 lands at T+5:14:31. I walked every shot's clock by hand and all 54 are continuous.
- **The side-step while braking is feasible:** moving 15 km in 2 min takes a ~12° tilt of the 1 g thrust (≈ 2 % of the braking), with drones ahead giving the warning. It is moot until issue 1 is fixed.
- **Lighting:** Site 1 is on the night side from T+5:09 to the end (150–199° from the sub-solar point).
