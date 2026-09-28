# Round 1 review: physics and orbital mechanics

## Verdict
The sublight skeleton holds. The approach from the warp exit to the Lee closes to the minute, the Lee's orbit and its 12.8°/h drift are right, and most flight times check out. Act IV does not hold. It treats Site 1's zenith as a fixed line when it actually sweeps round at 15°/h. As a result, wave two loses its nose-on geometry, anything that does come straight down the line has Maren behind the target, and the Astrid's spinal shot leaves it unable to stop. The heat readouts and Skerry's flight time also fail to add up. Every beat survives the fixes below.

## Issues, ranked

### 1. [MAJOR] The Astrid can't stop after its spinal shot (shot 35; KEY_NUMBERS; map D)
- **Problem:** "Still coasting bow-on at 14,700 km" means the Astrid skipped the fleet's T+7:05 turnover and is still doing 20 km/s. On the storyboard's own clock the braking line is ~14,500 km out at 8.5 km/s at T+7:26. The Astrid has therefore caught up with it and is about to lead (§13). After firing it cannot brake in time.
- **Evidence:** A flip (58 s, 1,160 km) plus a 1 g brake from 20 km/s (20,387 km) needs 21,550 km, more than the 14,700 km available. The Astrid passes the wreck at 11.6 km/s and stops ~6,800 km beyond it. Stopping short needs 2 g (3,700 km short) or 3 g (7,200 km short).
- **Fix:** Fire from rest. With no closing speed the no-escape range is 11,017 km and the flight is still 184 s (WN §2), so the three-minute beat survives. The Astrid brakes with the line, closes to ≤ 11,000 km for the kill (O10), then cuts thrust, slews, steadies and fires (§10). Change KEY_NUMBERS to "≤ 11,000 km from rest; flight 184 s". The alternative is to keep the coast but at ≤ 10 km/s from ~12,900 km; a 1 g brake then stops ~7,200 km short. Also: in 184 s the crippled monitor can drift up to 830 m on RCS, so the slug hits somewhere on the 1.8 km hull rather than a chosen breach. The spears hit the drive section, not amidships, so write "hits amidships, near the spear damage".

### 2. [MAJOR] "The line" rotates away, and nothing coasts down it (shots 28–30, 33; phases; map D)
- **Problem:** Site 1's zenith turns with Maren at 15°/h, and the Lee drifts off it at 12.8°/h. The storyboard treats the zenith as a fixed line that missiles can be launched along and ships can coast down.
- **Evidence:**
  - At T+5:40 the Lee is 6.6° (17,300 km) off Site 1's zenith; at wave two's launch (T+5:42) it is 7.0° off.
  - A straight flight from there reaches Breakwater at T+6:01 **16° off the zenith**, so Site 1 sees the missiles' flanks, not their noses. A launch at T+5:09 would give 6.6°.
  - Staying on the zenith line needs 3.9–10.9 km/s of sideways velocity (at 54,000–150,000 km) plus 15–80 mg of continuous thrust. That is not a coast.
  - Map D's approach line (96,700 km) is drawn in the rotating frame. The real inertial path from the Lee to the point 54,000 km over Site 1 is **114,000 km**. It turns over at ~T+7:20, arrives at ~T+7:54 (not ~T+7:40), and runs 12–14° off the zenith for most of the way.
- **Fix:**
  - Make "the line" a corridor fixed at arrival time. Shot 28 plots where Site 1's zenith *will be* when the wave arrives, and the missiles steer onto it during boost. Re-aiming 16° at ~110 km/s costs ~30 km/s of their 150 km/s.
  - Redraw map D's approach in the inertial frame, and retime the turnover and arrival (or leave the Lee ~15 min earlier).
  - In the phase table, change "coast down Site 1's line" to "coast toward Site 1's zenith".

### 3. [MAJOR] Straight down Site 1's line, Maren is the backstop (shots 33–35; map D)
- **Problem:** Seen from Breakwater, Maren fills ±8.7° around the zenith. Map D puts the Astrid, Breakwater and Site 1 on one line, so the spinal's line of fire ends on Site 1. So does the line of any wave that arrives exactly down the zenith. Misses, over-penetration and PD-killed wreckage keep going, into the planet that Q6 and §13 forbid striking.
- **Evidence:**
  - A 500 kg slug at 60–80 km/s carries 0.2–0.4 kt. A ~3 t missile, or its wreckage, at 110 km/s carries 4.3 kt.
  - The doctrine expects ~100 PD kills per wave. That is ~0.4 Mt of fragments hitting Maren's atmosphere over Site 1 about 5 min later (35,800 km at 110 km/s).
  - At the no-escape boundary a spinal miss is possible by definition.
- **Fix:**
  - Fly a corridor 10–12° off the zenith; the inertial path in issue 2 already gives about that. Misses then clear Maren's limb by 900–2,400 km.
  - The cost is modest. Site 1 sees the missiles' flanks at 78–80° incidence, and by WN §8's method it kills ~45 missiles per wave instead of ~14 nose-on (or ~99 side-on).
  - Missiles that miss divert away: their 25 % Δv reserve turns them ~19°.
  - Put the Astrid ≥ 10° off the axis for the spinal shot; a crippled monitor can be hit from any bearing.
  - One comm line sells the choice: "Offset twelve. Nothing goes down Site One's throat."

### 4. [MAJOR] Heat: the 31 % readout, and fins stowed until T+9:10 (shots 23–28, 36, 37)
- **Problem:** The fins are stowed at the fin hit (T+5:21) and stay stowed until T+9:10. Yet the sink reads 31 % at T+5:40, and the heat is only dumped at T+9:10.
- **Evidence (WN §4):**
  - Inputs: 4 fins at 1,200 K reject 12.2 GW, and 3 fins 9.1 GW. The hotel load is 1.5 GW, eight LFAs dazzling add ~1.8 GW, and each M-1C slug adds 12.5 GJ.
  - The sink goes from 94 % to 67 % after 8 min of venting, then to 73 % after the broadside, frigate and lance (~1.2 TJ). With the fins in, it stands at **80 % at T+5:40**.
  - Even with 3 fins out again from T+5:25 it reaches only 39 %. Getting to 31 % needs them out for ~18 min.
  - Starting from 31 % at T+5:45 and running dark, with the dazzle and PD, the sink is full at ~T+7:24, before the spinal hit. By T+9:10 it would need 25 TJ, against a 20 TJ capacity.
- **Fix:**
  - (a) In shots 27–28, the three surviving fins run out again behind the rock until ~T+5:43 (D5). That makes 31 % true.
  - (b) Add a heat beat in Act IV: "Sink ninety-eight percent" at ~T+7:20. Follow it with an emergency water dump (A-32: 1,000 t covers ~26 min of hotel load and leaves a white plume), or with fins edge-on down the approach axis as in shot 10 (D3).
  - (c) Bring "Hold" forward to ≤ T+8:00. "The fleet vents at last" at T+9:10 is ~1.5 h too late.

### 5. [MAJOR] Two hours in Site 1's sky with no effect (shots 29–36)
- **Problem:** From T+5:45 the fleet leaves the shadow and spends about two hours within ~15° of Site 1's zenith (elevation ~75°), closing from 145,000 km to 56,000 km. The storyboard shows neither Site 1's fire nor the fleet's counter.
- **Evidence (WN §1, a 2 GW site):** At 100,000 km a fin burns in 20 s, a sensor window in 1 s, and a non-rolling belt in 5.6 h. At 56,000 km (T+7:26) these become 6 s, 0.3 s and 1.8 h. Act III's rock shadow loses its point if the fleet can then sit in that beam unharmed.
- **Fix:** Show the counters Q6 allows (EW, smoke, geometry): ships roll to spread the beam, and smoke is laid ahead (it travels with the fleet). Shot 32's order becomes "All arrays, dazzle Breakwater and Site One." Show one cost, for example a scorched mast on the Extenuating in shot 30.

### 6. [MAJOR] Skerry's rounds are too slow for the clock (shots 5, 30; map A)
- **Problem:** Rounds launched at T+0:04 at 10 km/s (H-14) meet the fleet at T+6:40, a 6.6 h flight. The action text says "about seven hours" and the HUD sketch "TOF 6 h 40 m".
- **Evidence:** Skerry (380,000 km out, 40° off the axis) is ~293,000 km from the fleet's T+6:40 position, which is ~100,000 km from Maren. Integrating with Maren's gravity and Skerry's 1.02 km/s orbital motion, the fastest 10 km/s round takes **8.3 h** and arrives at ~T+8:25. No point on Skerry's orbit is closer than ~273,000 km.
- **Fix:** Raise H-14 (an unstarred assumption) to ~12.5 km/s. That gives a 6.6 h flight at 0.8 TJ per round. The HUD then reads "TOF 6 h 36 m".

### 7. [MINOR] The rock's shadow is narrower, in space and in time, than the text says (shots 22, 24; map C)
- **Problem/Evidence:**
  - After T+5:09 the sight lines from Site 1 and from Breakwater through the Lee swing apart at 2.15×10⁻⁵ rad/s. Behind an 18 km rock, a ship 700 km back (the Astrid) is hidden from both for only ±19 min; one 440 km back for ±30 min; one 110 km back for ±2 h.
  - By T+5:45 the Astrid is 32 km outside Breakwater's shadow, and it has to slide sideways at 5.7 m/s to stay in Site 1's.
  - The platform 800 km off, ~60° off the shadow axis, is not blocked by the Lee at all: it sees the whole ship.
  - The braking burn must also end with the Lee's 1.63 km/s orbital velocity (thrust tilted ~4.7°). Otherwise the fleet slides off the rock at ~100 km/min.
- **Fix:** Write "the rock hides the fleet from Site 1" (and from Breakwater, for the near ships). Pull the Astrid in to ≤ 300 km. For the fin hit: "a platform 800 km off to the side has a clear line of sight."

### 8. [MINOR] The fins retract faster than the slugs arrive (shots 10, 23, 24)
- **Problem/Evidence:** 800 km at 25 km/s is 32 s. The fins move in ~20 s, so with a 3 s reaction they are stowed ~9 s before impact, not "halfway in".
- **Fix:** Make the fin motion take ~60 s, so shots 10 and 23 become "compressed 15×". Or put the platform at ~400 km, for a 16 s flight in shots 24–25.

### 9. [MINOR] At the terms, the Endeavor is 11,800 km from the wreck (shot 36)
- **Problem/Evidence:** The stand-off is 11,836 km above Breakwater. Break-up debris moving at ≤ 1 km/s is still within ~1,000 km of the wreck at T+7:45, and the Endeavor needs ~37 min at 1 g to reach it.
- **Fix:** Put the camera in the debris at the wreck, with the Endeavor arriving at ~T+8:15. Or drop the debris and keep the damage close-up.

### 10. [NIT] Small numbers
- **Shot 17:** the platform is ~4.6° off the Astrid's bow, which needs a ~5 s slew, not ~30 s. The flight is 8,600 km at 80 km/s, or 108 s.
- **Shot 27:** a 2 g frigate needs ~45 s to close from 60 km to 40 km, so the lance fires at ~T+5:24:50.
- **Shot 34:** a 100 kt spear breaches a 2 m belt only inside ~2.5 km (H-10). Say "two kilometres", or aim the spears at the unbelted drive bells.
- **Shot 16:** the slugs came from ahead, so the hull is "holed bow to stern". A scram makes no flash; the flash is the impact itself (10 kg at 45 km/s ≈ 2.4 t TNT).
- **Shot 30, map D:** 10⁵ pellets are lethal only in a cloud of ≲ 20 km radius, not the ~1,500 km spread drawn. At that size, "come left two degrees" (0.7 km/s, 71 s at 1 g) works with ~2 min of warning.
- **KEY_NUMBERS:** the light-lag to Skerry at T+1:04 is 0.87 s (262,000 km), not 1.0 s.
- **Shot 4:** a shield park "at rest" 450,000 km out falls ~1,000 km toward Maren in 9 h unless the Nauvoo station-keeps (2 mm/s²).

## What works
- **The approach closes to the minute.** The burn is 34.0 min over 20,387 km, and the coast puts the fleet at 260,800 km at T+3:20. The Breakers crossing covers 89,000 km to T+4:34:10, and the flip and brake end at T+5:08:58, ~150,000 km out. Maren's gravity adds only ~90 m/s, so ignoring it is correct.
- **The orbits are right.** The Lee moves at 1.63 km/s on a 6.7-day orbit and drifts 12.80°/h relative to Site 1; map D's T+5:45 position (7.7° along) matches. 42,164 km is synchronous for a 23.93 h sidereal day. At alignment the Lee is 2.4° below the horizon of Sites 2 and 4, and Breakwater 8.6° below, so hiding from Site 1 alone is the right idea.
- **The weapon timings check out:**
  - the Canterbury salvo: 600 km at 45 km/s, 13.3 s;
  - the broadside: 32 s;
  - the frigate's coilgun: 3 s;
  - the lance: 0.04 s;
  - wave one: ~44 min, arriving at T+1:02 (the storyboard says T+1:04);
  - wave two: 19.3 min, arriving at T+6:01;
  - the spinal: 184 s;
  - light-lag from the Lee to Site 1: 0.48 s.
- **The heat budget is right up to the Lee.** 94 % at T+5:09 matches the hotel load plus ~70 min of laser fire over the crossing. At T+1:10 all four ground sites lie within 0.9° of the bow and Breakwater within ~6°, so the fins really are edge-on. Skerry, 40° off the axis, is exactly why it had to die first.
- **The visuals scale.** A rock 20 km off crosses a 24 mm frame in ~1.5 s at 20 km/s. Skerry at 262,000 km is a 0.39° disc, about a quarter of the width of a 1,200 mm frame.
