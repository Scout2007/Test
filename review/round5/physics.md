# Round 5 review: physics and orbital mechanics

Read from the frozen checkout of revision 5 (commit bcc0994). The builder was run on a scratch copy; its checks are all clear.

## Verdict
No major issues. The eclipse is built on a sound model, and I reproduced its timings independently:
- Breakwater's umbra lasts 67.5 min, and the penumbra crossing takes 128 s.
- The sunrise falls inside *The wait*.
- The escorts' and the Astrid's shadow times and the waves' shadow entry are right.
- Anchor's lee now has a comfortable margin.
- The numbers the new dialogue states all check out.

One lighting claim needs fixing before World preset E is lit. The "red ring" can only light hulls in the last few hundred kilometres of the umbra. Deeper in, the brightest light is Skerry, which the plan leaves out. Three nits follow.

## Round 4 issues: status

| Round 4 issue | Status | Note |
|---|---|---|
| 1. "One profile" means the killers' 30 g boost (MINOR) | Resolved | In O3, PHASES and KEY_NUMBERS, and on screen: *The pack fires* says "at 30 g", and the decoys "look, boost and fly like" the killers. |
| 2. The kill wave's odds are a floor (NIT) | Resolved | "At least ~33 of the ~40 … a floor". |
| 3. Skerry is a crescent (NIT) | Resolved | "A thin bright crescent on a dark disc". The stated ~6 % is now ~3.5 % (issue 3). |
| 4. Anchor's lee margin (NIT) | Resolved | On the bisector, 4.29 km off each shadow axis, ~4.6 km inside each edge (see *What works*). |

## Issues, ranked

### 1. [MINOR] Deep in Maren's shadow the red ring can't light a hull; Skerry is the key light (*The anvil*, *Umbrella*, *Blind it*, *The spend wave*, *Heat*; LIGHTING; World preset E)
- **Problem:** The lighting rule says that in the shadow "hulls are lit by the thin red ring of Maren's atmosphere (sunlight bent round the limb), the night side's city glow from below, and their own lenses, plumes and flashes." The shots follow it: Breakwater "lit from below by the thin red ring … and the city glow", the Endeavor "a dark hull edged red", the water plume "lit only by the red ring".
- **Evidence:**
  - **Refraction's reach.** An atmosphere bends grazing sunlight by at most ~1.2°, and by ~0.4° through the clearer layer ~10 km up. At Breakwater's ~42,000 km behind Maren, that carries red light only ~290–880 km inside the umbra's edge; at the escorts' ~50,000 km, ~350–1,050 km.
  - **Depths in these shots (km inside the edge).** Measured with the builder's `light()` geometry, every one is beyond that reach:

    | Shot | Body | Depth |
    |---|---|---|
    | *The anvil* | Breakwater | **5,546** |
    | *Umbrella* | the Astrid | 3,849 |
    | *Blind it* | the escorts | 3,293 |
    | *The spend wave* | the Astrid | 1,815 |
    | *Heat* | the escorts | 1,335 |

    Only *The hail* (218 km) and *The wait* (94 km) are close enough, and there the rising red glow is right.
  - **What reaches the hulls deeper in.** The ring is seen only by scattered light: a faint thin arc, on the order of 10⁻³ lux. Earth-like city lights give ~10⁻⁴ lux at synchronous height.
  - **Skerry.** It is in full sun, 76–83° from Breakwater's zenith and well clear of Maren's disc, and 63 % lit (phase 75°). It gives **~0.01 lux**, a quarter-moon night and an order of magnitude more than the ring and the cities together.
- **Fix:**
  - Light preset E with Skerry as a dim, cool key from its bearing, with exposure pushed.
  - Keep the ring as a faint rim from below, the city lights as detail on the disc, and the ports, plumes, tracers and Casaba flashes as the drama.
  - Ramp the red up only within ~5 min of each body's first light: Breakwater from ~T+7:50 (*The hail*, *The wait*), the escorts from ~T+8:01.
  - Reword the LIGHTING rule, *The anvil* ("lit by Skerry's moonlight, its ports, then its plumes"), *Blind it* ("a dark, moonlit hull") and *Heat* ("the plume lit by Skerry").
  - This is a text and rig note; no shot changes.

### 2. [NIT] With an atmosphere, the slug lands just before full sun (*Impact*; SUN)
- `light()` uses the solid planet. Eclipse tables enlarge Earth's shadow by ~2 % for the atmosphere, about +75 km of opaque layer. With that, Breakwater's first light moves to T+7:55:37 and full sun to **T+7:57:45**, 16 s after the slug lands at T+7:57:29.
- Setting SUN to **33.1°** with a 6,475 km effective radius restores the board's times: first light T+7:55:13, full sun T+7:57:21. Either make that change or say "in the last seconds of sunrise".

### 3. [NIT] Skerry is ~3.5 % lit, not ~6 % (*Birds away*)
- With the sun now in the ring plane at 33.2°, Skerry's phase angle from the fleet is ~159°. Change the number; the look ("a thin bright crescent on a dark disc") is right.

### 4. [NIT] "Six hours, give or take" (*Skerry throws*)
- The first salvo flies 6 h 36 min, and the Astrid can track it to the minute. "Six and a half hours" is both true and still sounds like a guess.

## What works
- **The shadow model.** Umbra and penumbra are bounded at R ∓ d·tan(0.27°), which is the right cone geometry.
  - Breakwater is eclipsed for 67.5 min (T+6:47:41 → T+7:55:12), close to Earth's ~69 min at synchronous height at equinox. The penumbra crossing takes 128 s at 3.03 km/s across a ~390 km band.
  - The escorts are in the umbra T+7:24:36 → T+8:06:09 and the Astrid until T+8:00:03. The waves enter it at ~T+7:45:20 and T+7:46:40, coasting, which is why *Seeker*, *Wall of fire*, *Casaba* and *Umbrella* are lit by tracers, intercepts and nuclear flashes alone.
  - The red-then-white sunrise at the edge is right. *The wait* holds the whole sunrise from first light to full sun, and the slug lands in the sun.
  - Anchor itself sits ~70,000 km off the shadow axis, so the pack and the rock stay sunlit. Site 1 is on the night side at the end.
- **Anchor's lee.** On the bisector the Endeavor is 4.29 km off both the sun's shadow axis and Site 1's, inside an ~8.9 km umbra. Site 1's line of sight turns ~1° over T+5:09 → T+5:43, moving the Endeavor ~0.3 km relative to it, so it is dark through every lee shot.
- **The ring on the pack.** ~40 m/s of divert moves the clouds ~150 km in their last hour. The pack's 20 km slide on 0.1 g RCS takes ~4.8 min, "a few minutes", and stays inside the overlap of the two ground sites' shadows.
- **The dialogue's numbers.**
  - Fourteen ships; "four-fifty thousand".
  - "One g, thirty-four minutes": 20,387 km.
  - "Eighteen rounds still inbound": six salvos of three thrown by T+0:54, before wave one lands at T+1:02.
  - The first salvo on time at T+6:40 (thrown at ~13.2 km/s); the last, at Anchor, at T+7:07 (~12.7 km/s).
  - "Four hundred klicks": a 16 s flight. "Forty-five klicks": inside the lance's ~50 km field.
  - "Forty Casaba nukes"; "two forty-nine": 169.2 s.
- **The heat readouts.** 94 → 96 % over four minutes is the 1.5 GW hotel load (+1.8 %). Venting from 96 % gives ~31–33 % by T+5:43, within the uncertainty of the fight's heat. After that, 63 % at *Site One*, 88 % at *Blind it* and 97–98 % at *Heat* all follow from the hotel load plus eight minutes of full dazzle.
- **The clocks.** The builder's clock, cue and shadow checks all pass on the scratch copy. *Sixty-four* (T+7:25:40, 14 s) slots between the reveal and *Umbrella*, and the prologue and end cards run off the clock.
