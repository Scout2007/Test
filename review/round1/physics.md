# Round 1 review: physics and orbital mechanics

## Verdict
The sublight skeleton holds: the approach from the exit to the Lee closes to the minute, the Lee's orbit and drift are right, and most flight times check out. Act IV breaks because it treats Site 1's zenith as a fixed line when it sweeps round at 15°/h, so wave two loses its nose-on geometry and whatever comes straight down the line has Maren behind the target. The Astrid also cannot stop after its spinal shot, and the heat readouts and Skerry's flight time don't add up, but every beat survives the fixes below.

## Issues, ranked

### 1. [MAJOR] The Astrid can't stop after its spinal shot (shot 35; KEY_NUMBERS; map D)
- **Problem:** "Still coasting bow-on at 14,700 km" means the Astrid skipped the fleet's T+7:05 turnover and is still at 20 km/s. On the storyboard's own clock the braking line is ~14,500 km out at 8.5 km/s at T+7:26, so the Astrid has caught up and is about to lead (§13).
- **Evidence:** A flip (58 s, 1,160 km) plus a 1 g brake from 20 km/s (20,387 km) needs 21,550 km, and only 14,700 km is left. The Astrid passes the wreck at 11.6 km/s and stops ~6,800 km beyond it. Stopping short would take 2 g (stops 3,700 km short) or 3 g (7,200 km short).
- **Fix:** Fire from rest. With zero closing speed the no-escape range is 11,017 km and the flight is still 184 s (WN §2), so the three-minute beat is unchanged.
  - The Astrid brakes with the line, then closes to ≤ 11,000 km for the kill (O10).
  - It cuts thrust, slews, steadies and fires (§10).
  - KEY_NUMBERS becomes "≤ 11,000 km from rest; flight 184 s".
  - Alternative: keep the coast but at ≤ 10 km/s, firing from ~12,900 km; a 1 g brake then stops ~7,200 km short.

  One more fix: on RCS the crippled monitor can drift 830 m in 184 s, so the slug hits the 1.8 km hull, not a chosen breach. The spears hit the drive section, not amidships, so write "hits amidships, near the spear damage".

### 2. [MAJOR] "The line" rotates away, and nothing coasts down it (shots 28–30, 33; phases; map D)
- **Problem:** Site 1's zenith turns with Maren at 15°/h, and the Lee drifts off it at 12.8°/h. The storyboard treats the zenith as a fixed line to launch along and to coast down.
- **Evidence:**
  - The Lee is 6.6° (17,300 km) off Site 1's zenith at T+5:40, and 7.0° off at wave two's launch.
  - Flown straight from there, the wave reaches Breakwater at T+6:01 **16° off the zenith**. Site 1 therefore sees the missiles' flanks, not their noses. A launch at T+5:09 would arrive 6.6° off.
  - Holding station on the zenith line would take 3.9–10.9 km/s of sideways velocity plus 15–80 mg of continuous thrust. That is not a coast.
  - The inertial path from the Lee to the point 54,000 km over Site 1 is **114,000 km**, not map D's 96,700 km, which is a rotating-frame line. Turnover moves to ~T+7:20 and arrival to ~T+7:54, and the fleet runs 12–14° off the zenith for most of the way.
- **Fix:**
  - Make "the line" a corridor fixed at arrival time. Shot 28 plots where Site 1's zenith *will be* when the wave arrives, and the missiles steer onto it during boost. A 16° re-aim at ~110 km/s costs ~30 km/s of their 150 km/s.
  - Redraw map D's approach in the inertial frame, and retime the turnover and arrival, or leave the Lee ~15 min earlier.
  - Phases: "coast toward Site 1's zenith", not "down Site 1's line".

### 3. [MAJOR] Straight down Site 1's line, Maren is the backstop (shots 33–35; map D)
- **Problem:** Seen from Breakwater, Maren fills ±8.7° around the zenith. Map D puts the Astrid, Breakwater and Site 1 on one line, so the spinal's line of fire ends on Site 1. So does the line of any wave that arrives exactly down the zenith. Misses, over-penetration and PD-killed wreckage keep going, into the planet that Q6 and §13 forbid striking.
- **Evidence:**
  - A 500 kg slug at 60–80 km/s carries 0.2–0.4 kt.
  - A ~3 t missile, or its wreckage, at 110 km/s carries 4.3 kt.
  - The doctrine expects ~100 PD kills per wave. That puts ~0.4 Mt of fragments into Maren's air over Site 1, about 5 min later.
  - At the no-escape boundary, a spinal miss is possible by definition.
- **Fix:** Fly a corridor 10–12° off the zenith; issue 2's inertial path already gives about that. Misses then clear Maren's limb by 900–2,400 km.
  - Site 1 sees the missiles' flanks at 78–80° incidence. By WN §8's method it kills ~45 per wave, against ~14 nose-on and ~99 side-on: an affordable cost.
  - Missiles that miss divert away; the 25 % Δv reserve turns them ~19°.
  - Put the Astrid ≥ 10° off the axis. A crippled monitor can be shot from any bearing.

### 4. [MAJOR] Heat: the 31 % readout, and fins stowed until T+9:10 (shots 23–28, 36, 37)
- **Problem:** The fins go in at the fin hit (T+5:21) and stay stowed until T+9:10. Yet the sink reads 31 % at T+5:40, and the heat is dumped only at T+9:10.
- **Evidence (WN §4):**
  - Inputs: 4 fins at 1,200 K reject 12.2 GW; 3 fins reject 9.1 GW. The hotel load is 1.5 GW. The dazzling LFAs add ~1.8 GW. Each M-1C slug adds 12.5 GJ.
  - The sink runs from 94 % to 67 % after 8 min of venting. The broadside, frigate and lance (~1.2 TJ) take it to 73 %, and it reaches **80 % at T+5:40** with the fins in.
  - Even with 3 fins out again from T+5:25 it only gets to 39 %; 31 % needs them out ~18 min.
  - Starting from 31 % at T+5:45 and running dark, it is full at ~T+7:24, before the spinal hit.
  - Holding until T+9:10 would take 25 TJ of a 20 TJ sink.
- **Fix:**
  - (a) Shots 27–28: the three surviving fins run out again behind the rock until ~T+5:43 (D5), which makes 31 % true.
  - (b) Act IV: "Sink ninety-eight percent" at ~T+7:20, then an emergency water dump (A-32: ~26 min of hotel load, with a white plume), or fins edge-on down the approach axis as in shot 10.
  - (c) Move "Hold" to ≤ T+8:00. At T+9:10 the vent comes ~1.5 h too late.

### 5. [MAJOR] Two hours in Site 1's sky with no effect (shots 29–36)
- **Problem:** From T+5:45 the fleet spends ~2 h within ~15° of Site 1's zenith (elevation ~75°), closing from 145,000 km to 56,000 km. Neither Site 1's fire nor the fleet's counter is shown.
- **Evidence (WN §1, 2 GW site):** At 100,000 km a fin burns in 20 s, a sensor window in 1 s, and a non-rolling belt in 5.6 h. At 56,000 km those become 6 s, 0.3 s and 1.8 h. If the fleet can sit in that beam unharmed, Act III's rock shadow loses its point.
- **Fix:** Show the counters Q6 allows:
  - ships roll to spread the beam;
  - smoke is laid ahead (it travels with the fleet);
  - shot 32's order becomes "All arrays, dazzle Breakwater and Site One."

  Show one cost, for example a scorched mast on the Extenuating in shot 30.

### 6. [MAJOR] Skerry's rounds are too slow for the clock (shots 5, 30; map A)
- **Problem:** Rounds launched at T+0:04 at 10 km/s (H-14) meet the fleet at T+6:40. The text says "about seven hours", the HUD sketch "TOF 6 h 40 m".
- **Evidence:** Skerry (380,000 km out, 40° off the axis) is ~293,000 km from the fleet's T+6:40 position. With Maren's gravity and Skerry's 1.02 km/s orbital motion integrated, the fastest 10 km/s round takes **8.3 h** and arrives ~T+8:25. No point on Skerry's orbit is closer than ~273,000 km.
- **Fix:** Raise H-14 (unstarred) to ~12.5 km/s. That gives a 6.6 h flight at 0.8 TJ per round; the HUD then reads "TOF 6 h 36 m".

### 7. [MINOR] The rock's shadow is narrower than the text says (shots 22, 24; map C)
- **Problem/Evidence:**
  - After T+5:09 the sight lines from Site 1 and from Breakwater through the Lee swing apart at 2.15×10⁻⁵ rad/s. With an 18 km shadow, a ship is hidden from both for ±19 min at 700 km back (the Astrid), ±30 min at 440 km and ±2 h at 110 km.
  - To stay in Site 1's shadow the Astrid must slide sideways at 5.7 m/s.
  - The platform 800 km off, ~60° off the axis, isn't blocked by the Lee at all; it sees the whole ship.
  - The braking burn must also end with the Lee's 1.63 km/s orbital velocity (thrust tilted ~4.7°), or the fleet slides off the rock at ~100 km/min.
- **Fix:**
  - Say "hides the fleet from Site 1", and from Breakwater only for the near ships.
  - Keep the Astrid within ~300 km.
  - Shot 24: "a platform 800 km off to the side has a clear line of sight".

### 8. [MINOR] The fins retract faster than the slugs arrive (shots 10, 23, 24)
- **Problem/Evidence:** 800 km at 25 km/s takes 32 s. The fins move in ~20 s, so after a 3 s reaction they are stowed ~9 s before impact, not "halfway in".
- **Fix:** Make the fin motion ~60 s, which turns shots 10 and 23 into "compressed 15×". Or put the platform at ~400 km, for a 16 s flight.

### 9. [MINOR] At the terms, the Endeavor is 11,800 km from the wreck (shot 36)
- **Problem/Evidence:** The stand-off is 11,836 km above Breakwater. Debris at ≤ 1 km/s is still within ~1,000 km of the wreck at T+7:45, and the Endeavor needs ~37 min at 1 g to get there.
- **Fix:** Set the shot in the debris at the wreck with the Endeavor arriving (~T+8:15), or drop the debris.

### 10. [NIT] Small numbers
- **Shot 17:** the platform is ~4.6° off the Astrid's bow, so the slew takes ~5 s, not ~30 s. The flight is 8,600 km at 80 km/s, which is 108 s.
- **Shot 27:** a 2 g frigate needs ~45 s to close from 60 km to 40 km, so the lance fires at ~T+5:24:50.
- **Shot 34:** a 100 kt spear breaches a 2 m belt only inside ~2.5 km (H-10). Say "two kilometres", or aim at the unbelted drive bells.
- **Shot 16:** the slugs came from ahead, so "holed bow to stern". The flash is the 2.4 t TNT impact; a scram makes none.
- **Shot 30 and map D:** 10⁵ pellets are lethal only within a ≲ 20 km radius, not the ~1,500 km spread drawn. At that size, "left two degrees" (0.7 km/s, 71 s at 1 g) works with ~2 min of warning.
- **KEY_NUMBERS:** the light-lag to Skerry at T+1:04 is 0.87 s.

## What works
- **The approach timeline:** 34.0 min of burn over 20,387 km, 260,800 km out at T+3:20, and the flip and brake done at T+5:08:58, ~150,000 km out. Maren's gravity adds only ~90 m/s, so ignoring it is correct.
- **The orbits:** the Lee's orbit (1.63 km/s, 6.7 d), its 12.80°/h drift and map D's T+5:45 position are right, and 42,164 km is synchronous for a 23.93 h sidereal day. At alignment the Lee is 2.4° below the horizons of Sites 2 and 4, so hiding from Site 1 alone is the right call.
- **The flight times:** Canterbury 13.3 s, broadside 32 s, coilgun 3 s, lance 0.04 s, wave one ~44 min (T+1:02 against T+1:04), wave two 19.3 min (T+6:01), spinal 184 s, and 0.48 s of light-lag from the Lee to Site 1.
- **The heat up to the Lee.** 94 % at T+5:09 matches the hotel load plus ~70 min of laser fire. At T+1:10 all four ground sites lie within 0.9° of the bow and Breakwater within ~6°, so the fins really are edge-on.
- **The visual scales.** A rock 20 km off crosses a 24 mm frame in ~1.5 s. Skerry at 262,000 km is a 0.39° disc, a quarter of a 1,200 mm frame.
