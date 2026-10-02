# Round 1 review: lore fidelity

Lens: JCB's posts and Sir_Lazz's art. The user's decisions are taken as given.

## Verdict

Revision 1 is broadly faithful to the posts: every class does its canonical job, the warp, shield and radiator rules hold, and the destroyers' ECW is told in the posts' own terms. Two details contradict canon: the plasma lance is drawn as a free-flying, self-confined ring, and the Astrid is called "kilometre-long". Six more strain it. All are text, brief or VFX fixes; no shot needs cutting.

## Issues, ranked

### 1. [MAJOR] The lance is a free-flying ring, not a lance (shot 27; FX-LANCE; A-23)

- **Problem:** Shot 27 fires "a violet-white plasma ring" that "crosses the gap". FX-LANCE is a "compact toroid", and LREF §4.3 says the toroids "hold their own field" in flight.
  - Once the ring leaves the nose, no field from the ship holds the plasma. The posts allow two ways to hold it; this is neither, just a torpedo without the generator.
  - It reads as a bolt, not a lance.
- **Evidence:** Part 1, item 4: plasma needs "an active electromagnetic field to maintain its form lest it just fizzles out; hence the need for a self-contained ‘topredo’ [sic] with an EMF generator, or a ‘lance’ where the ship itself generates the EMF to deliver plasma straight to a target".
- **Fix:** Keep the shot and change the effect.
  - Make it a violet-white spear from the nose channels to the frigate, inside a faint field sheath that the ship projects. The spear fizzles back from the target when `lance_power` cuts.
  - Reword A-23: the ~50 km limit is how far the ship can project its field. That is the posts' mechanism, and it explains the range.
  - Change FX-LANCE to "field-held plasma jet, nose to target".

### 2. [MAJOR] The Astrid is not kilometre-long (shot 17)

- **Problem:** "it swings its whole kilometre-long hull to bear". The kilometre is the gun, not the hull. AST and the doctrine have the length right.
- **Evidence:**
  - Part 2: the Hanuman "clocks in at 1600 meters".
  - Part 3: "roughly 1200 and 1700 meters long respectively".
  - Part 1: "The spinal cannon taking up a good kilometer or so of that".
- **Fix:** "swings its 1.6-kilometre hull to bear". The fix is trivial, but the number is canon.

### 3. [MINOR] One destroyer "holds the net alone" (shots 16, 19, 28, 32; FLEET)

- **Problem:** After the Canterbury dies, the Extenuating Circumstances keeps the whole screen at full strength and nobody remarks on it. The posts make the screen a matter of numbers. Its offensive ECW alone (shots 19, 32) is fine: the posts give one destroyer that reach.
- **Evidence:** Part 1: "Capable of silencing the radio-emissions of an entire fleet if present in large enough numbers".
- **Fix:**
  - Shot 16: "Extenuating, you have the net. What's left of it."
  - Shots 19 and 28: a HUD tag, "NET DEGRADED · DIRECT LINKS" (the backup in LREF §3).
  - Or ask the user about a third destroyer.

### 4. [MINOR] The Infinity is "dry" after 150 missiles (shots 7, 29; FLEET)

- **Problem:** The Infinity fires 150 missiles in wave one and nothing else, yet it is "empty" in shot 29. The posts allow mission loads, but the doctrine assumes the typical one (A-26: about 700 missiles).
- **Evidence:** Part 2: "just about 360 missile pods in this current pattern", with the back third as "multi-silo launch packs", and "many of these missiles feature Multiple Independently Targetable Vehicles".
- **Fix:** Pick one:
  - Wave one empties the module (several hundred missiles; the swarm is instanced).
  - Or keep 150, keep the Infinity as the pack's reserve (O11), and move "dry, heading home" to after wave three.

  Either way, add MIRV buses to MSL-V.

### 5. [MINOR] The destroyer brief puts the dish aft (DD; LREF §2 "Kit"; shots 3, 15, 16, 30)

- **Problem:** DD reads "parabolic antenna over the aft third", following one parenthesis in Part 3. Sir_Lazz's art (`reference_art/destroyer.webp`) puts a forward-facing dish on a truss just behind the shield, at roughly 10–60 m of the 200 m hull. The post's account of the dish's job fits the art.
- **Evidence:** Part 3: the dish is the "‘eyes and ears’ of the ship once the front impact shield is removed", and "the stern is literally taken up by the ship's engineering section and radiators".
- **Fix:** Rewrite DD and §2 to follow the art. Log the conflict between text and art in `OPEN_QUESTIONS.md` for the user.

### 6. [MINOR] The corvette and tender briefs drop the design rules (CV, TND; shots 3, 4, 11, 18, 20)

- **Problem:** Both go to concept sheets without reference art, and their briefs omit what every GUN ship needs. A sheet could come back with no warp rings or shield, or with a hab ring.
- **Evidence:**
  - Part 1: the rules hold "for FTL capable ships, and STL ships in general".
  - Part 1: every ship can "independently warp, without relying on any big tender".
  - Part 1: below 1,000 m, "‘rings-on-stick’ configurations, or no rings visible at all".
  - Part 2: modules are swapped "at your nearest fleet tender".
- **Fix:** Add to both briefs:
  - two warp rings at the ends;
  - a jettisonable forward shield (both belong in the shot 4 park);
  - radiators and booms that stow for warp.

  CV also needs no spin section and weapons "far more powerful and varied" than a big ship's PD. TND also needs spare shields and a rig to swap frigate modules.

### 7. [MINOR] The shieldless crossing at speed is never acknowledged (shots 4, 11)

- **Problem:** The fleet crosses 89,600 km of debris at 20 km/s with its shields parked. The park fits "jettisoned prior to a battle" and is the user's call (Q4), but the posts also give the shield a sublight job, and the film never admits the trade.
- **Evidence:** Part 2: "a kinetic impact shield at the very front for impacts at speed and in warp". Part 1 calls jettisoning "a big trade-off".
- **Fix:** Shot 11: "Entering the Breakers. No shields from here. Corvettes, you're the shield: sweep the lane."

### 8. [MINOR] Assumptions presented as canon (LREF §2, §3, §10; shot 27)

- **Problem:**
  - §3 tags the "laser-link mesh" [Lore], but it is A-29.
  - §10 has "counter-rotating twin rings [Lore; Model]", but the posts say only "dual ring configuration"; counter-rotation is [Model], as A-34 already says.
  - §2 tags the aft dish [Lore] (see issue 5).
  - Shot 27's "the one range where a lance works" treats A-23's ~50 km as a law. The posts give no range.
- **Evidence:** The doctrine's own "How to read the labels".
- **Fix:** Re-tag the first two. Shot 27: "at 40 km, well inside the ~50 km its field can hold".

### 9. [NIT] The Endeavor never fires a missile (shots 29, 33)

- **Problem:** Its 16 VLS cells stay shut (`vls_open` and MSL are built and unused), so the fleet's generalist never fields its missiles.
- **Evidence:** Part 1: "a healthy complement of missiles as its primary offensive systems"; "it's only with the cruiser that all of these systems are presented in their full generalist potential".
- **Fix:** In shot 29 or 33, the Endeavor adds its 16 VLS Casaba shots to wave three.

### 10. [NIT] The Astrid never glows (shots 6, 10)

- **Problem:** Its 8 stacked fins and its heat never appear.
- **Evidence:** Part 1: "8 stacked radiator fins which are capable of extending further than the warp ring boundary"; "the thing GLOWS in thermals".
- **Fix:** Give it one thermal beat: fins out during the coast after T+1:04 (alongside shot 10), or outshining the fleet on a thermal insert in shot 6.

### 11. [NIT] "Nuclear plasma spears" blurs the families (shot 34)

- **Problem:** In the posts, "plasma" names the field-held family, not a Casaba jet.
- **Evidence:** Part 1: "C. Plasma (in the form of torpedoes and lances), D. Nuclear (Casaba howitzers, conventional, etc)".
- **Fix:** "Casaba jets" or "nuclear spears".

### 12. [NIT] Tone against the GUN's stated values (shots 17, 35)

- **Problem:** The flag officer's "Remember the Cant" is a revenge slogan. Shot 35 then kills a crippled, immobile human warship without a word.
- **Evidence:** T-SEC post: "professionalism, integrity, and above all else — accountability to the people"; the dove and raven "act as symbols of caution". Part 1: "an attempt to fully shift towards an air of peace and reconciliation".
- **Fix:** Give the easter egg to a gun-deck voice, or cut it. Before the spinal shot, add a one-way hail: "Breakwater, Tidebreak Actual. You can't move. Strike, or we fire." Silence keeps the defender unheard.

### 13. [NIT] Close the canon loops at the end (shot 37)

- **Problem:** The shields' recovery and T-SEC, the trip home and the reason for the operation, are never named.
- **Evidence:** Part 1: the shields are "collected and re-attached". T-SEC post: "Along with the LREF and the EAF, T-SEC tends to be the first boots on the ground".
- **Fix:** Add a line to shot 37. TIDEBREAK ACTUAL: "Nauvoo, bring the shields in. T-SEC, the sky's yours." The landing stays unshown (Q7).

## What works

- **Shields and warp:**
  - The shields are jettisoned and parked for recovery, and both rings stay on.
  - The drone raid on the park (shot 28) is the posts' "enemy sorties targeting the detached shields".
  - Each ship, the tender included, warps independently.
  - The fins are stowed in warp, and "Cut it loose" (shot 24) follows from the rule that radiators must retract for warp.
- **Roles:**
  - The corvettes screen the drones.
  - The destroyers are nearly unarmed and still feared:
    - "return to sender" is the crews' own phrase;
    - autonomous drones resist it, and there is no self-destruct (the posts call it "nigh impossible");
    - the net comes up once the shields are off.
  - The hedgehogs work as a pack.
  - The Donnager has "4 large kinetic batteries", and the Excelsior has the PD fit.
  - The Astrid is the backline eye, the gun and the PD anchor.
  - The Endeavor fights with railguns, lasers and lances, and has no spinal.
- **Weapon families:** kinetics and lasers are the mainstays, plasma is the finicky knife, nuclear is commonplace, and missiles are only the delivery platform.
- **The Endeavor matches the README:** five engines, M-1C turrets and well batteries, violet lenses with invisible beams, nose lances, shield thrusters.
- **GUN values:** the rules of engagement spare the populated world; the escape pods and city lights fit a GUN accountable "to the people".
- **The Maren Compact:** its warpless monitor, with no rings or shield, is consistent with the posts' design rules.
