# Open questions

Questions only the user can answer. Phase 1's questions were all answered at sign-off; they are kept below as a decision log, so the reasons stay with the choices.

## Still open

None of these blocks the storyboard; they matter when modelling starts. Each has a recommendation, and the storyboard currently follows it.

| # | Question | Why it comes up | Recommendation (what the board assumes) |
|---|---|---|---|
| Q13 | May the smallest assets be proxies? | "Everything hero-detailed" still stands, but some items are never bigger than a few dozen pixels (the closest-view table in `ASSET_REQUESTS.md`). The inner-ring stations are only points of light 21,800 km apart; the Nauvoo and the Excelsior's PD module are ~40 px behind the parked shields; the Donnager's gun module is only seen far off; drones stay under ~30–40 px. | **Ring stations as lights only; the Nauvoo, the PD module and the gun module as silhouettes; one drone design per side** (LREF and Compact), varied by payload. Everything seen larger stays hero. |
| Q14 | The ECW destroyer's dish: text or art? | The lore post says the antenna is "taking up a near third of the ship’s overall length (at the aft of the ship)", but also that "the stern is literally taken up by the ship's engineering section and radiators". Sir_Lazz's art (`reference_art/destroyer.webp`) puts a forward-facing dish on a truss just behind the shield, and the post's own account of its job ("eyes and ears… once the front impact shield is removed") fits the art. | **Follow the art** (dish forward, fixed on its truss). |
| Q15 | The modelling session's pending picks | The M-1C's wake style (split, ripple, bulk, extend, combined) and the PDC design (PD-1/2/3) were still waiting on you in the modelling session. The Endeavor rebuild, the Astrid's ~19 M-1Cs, the gun module and the PD module all inherit them, and so do the CIWS mounts now on every frigate hull and on the Astrid. | No recommendation from here: they're your design picks. The build order puts them first. |
| Q17 | If the render benchmarks come in high, which fallback do you prefer? | The estimate is 159.2 h against the 160 h gate (with the 30 % re-render allowance), so almost any overrun fires the gate. In the production reviewer's high case, the three render levers (half-resolution FX, cheaper swarm layers, trimming the costliest seconds) don't close the gap on their own, which leaves the fourth step: a smaller re-render allowance or shorter holds. | **A smaller re-render allowance first** (a single full pass still fits the week with ~30 h to spare even in the high case); shorter holds only after that, since the holds carry the film's rhythm. Deciding now means it won't come as a surprise after step 1. |
| Q18 | How much of the AI should the film show? | Both no-lore readers followed the story, but the AI stayed abstract: they couldn't tell where it is, what it wants, which weapons are its, or why humans side with it. The film shows it only through weapons that run themselves ("The rest are AI-run… Can't touch those.") and guns that don't stand down when the Compact asks for terms. | **Leave it offscreen**, as you chose ("Just 'the AI'", no voice): the board now says the Compact crews Breakwater ("COMPACT MONITOR" on its caption), so the last shot's stakes are clear. If you want the film to answer any of the four questions, tell me which, and I'll find a line or a card for it. |

### Changed in phase 2 without a question (say if you disagree)

- **The rock is now called "Anchor"**, a placeholder in the sea-and-storm theme. "The lee of the Lee" read badly at speed. A better name is welcome.
- **A one-way hail before the spinal shot.** *"Breakwater, Tidebreak. Surrender or abandon ship."* No answer comes, so the defender stays unheard. The lore review asked for it; it fits the GUN's values.
- **The film is 6:49** (revision 1 was 2:45) with **69 shots** (was 37). Internal cuts became shots; new beats set up the losses and pay off the threats; your weapon close-ups, the reviewers' holds, the report's cards and the room the new dialogue needs added the rest. Runtime was left flexible.
- **The Endeavor keeps its 16 VLS cells** as the fast reserve (~4 min to Breakwater from the stop) rather than joining the kill wave. It could fire them in *Blind it* if you'd like the moment.
- **The hedgehog pack keeps a guard at Anchor**, the Donnager and the Wallfish, and the defender makes one try for it: Skerry's last salvo sweeps past the rock with the garrison's last drones behind it, just as the pack fires, and the guard beats it off.
- **The kill wave is ~40 Casaba killers among ~300 decoy and EW birds**, sized to cripple Breakwater's drive and leave the kill to the spinal shot; ~1,100 missiles stay in reserve. Since revision 4 each wave leaves in one launch and flies one profile, so the defender can't pick the Casabas out by launch time or speed.
- **The hero missile is the capital-ship killer**, sized to fit the hedgehog's pods (no more than ~20 m). The built 26 m missile becomes the swarm system's stand-in, so *Birds away* now waits on the missile concept sheet like *Seeker*.
- **The terms ask for charts of the AI's weapons in the Breakers**, because the Compact says they don't answer to it (*"Says the AI's guns don't answer to them." "Then they map them."*), and the last line is "T-SEC, you're next." rather than "the sky's yours": Sites 2–4, the ring and the garrison are still live.
- **Record captions and first tags** name each ship once. Captions go on the first sight of the flagship, the Endeavor and Breakwater ("L.R.E.F.S. ENDEAVOR · CRUISER", "BREAKWATER · COMPACT MONITOR · NO WARP DRIVE"); most other ships carry their class in their first speaker tag ("DONNAGER · GUN FRIGATE"), placed where there is time to read it. Both fit the "collated from the records" framing.
- **"The AI" is the Charon system.** The report's first paragraph ends "…and is referred to below as the AI", so every later "AI" in the film (the drones, the guns, the terms) means the system from the Charon Innovations incident. Say if the Compact's AI should be a different one.
- **The report closes the film**: after the last line and a second of black, the report's RESULT paragraph and "END OF REPORT" fade up on the opening's still stars (10 s).
- **The eclipse's light (round 5).** Deep in Maren's shadow the red ring can't light a hull: bent sunlight only reaches the shadow's outer few hundred kilometres. So Breakwater's reveal, the umbrella, *Blind it* and *Heat* are keyed by Skerry's dim moonlight, with the red ring as a faint rim, the city lights, the ports and the weapons' own light. The red glow now rises in the last minutes before sunrise (*The hail*, *The wait*), which makes the sunrise a bigger change. The reveal reads as a silhouette against the city-lit night side.
- **The report is shorter (72 s → 68 s).** Breakwater and the laser sites now first appear in *The picture*, which also keeps "Breakwater" and "the Breakers" apart. The cinematography review asked for 45–50 s; going below ~68 s would cut the AI's history or the warp bar, which the cold readers relied on. Say if you'd rather have it shorter still.
- **Full laser power on Breakwater only.** In *Blind it* the arrays go to full on Breakwater's optics while Site One stays at the dazzle it has had since Anchor ("Arrays full on Breakwater. Site One, dazzle only."). Full power on Site One would have been a burn on a populated surface, against the report's own restriction, which now reads "…laser sites included; they could be dazzled, not struck."
- **The destroyers are "E-WAR DESTROYER"s** in their first tags, short for the lore post's "e-warfare" (the full word didn't fit the reading time), rather than "sensor destroyers".
- **The report gives the no-fire rule's reason (cold read 5).** The restrictions card now starts "Maren is populated: no fire was to fall on its surface…", from LREF §13: a slug or warhead fired at a populated world is a weapon of mass destruction. Cold read 5 found no reason given for the rule.
- **The report closes with a RESULT paragraph.** "6. RESULT. Maren's orbit was opened to T-SEC at T+8:24. Lost: L.R.E.F.S. CANTERBURY and L.R.E.F.S. NORMANDY." now comes before END OF REPORT (the last card is 10 s, was 4 s), because two cold readers found the film stopped rather than ended.
- **The shield handover is answered.** The Nauvoo now says "Got it. See you after." and the Endeavor says "Guns clear." when it hands over its shield. The last line, "Bring the shields in", no longer suggests the fleet is leaving, and the reason the shields come off is spoken.
- **Breakwater is introduced as the target in *The picture*** ("Target is Breakwater, their warship, under Site One's cover."), since cold read 5 couldn't tell it was a ship until its reveal.

## Decided at phase 1 sign-off

### The world and its rules

| # | Question | Decision | Where it lands |
|---|---|---|---|
| Q1 | Who defends the system? | **The Maren Compact**: a human polity that broke away from the GUN, with no warp fleet at Maren and **no relief coming**. *Phase 2 (the user):* a splinter faction allied with **the AI**, outlawed after it went rogue (a later licence to Charon Innovations ended in the Charon Innovations incident), holding the manufacturing world of Maren. Humans crew *Breakwater* and the laser sites; the AI runs the drones, the emplacements and the foundries. The AI has no name | Defence §1, HD9, H-01 |
| Q2 | The asteroid belt | **A debris ring around the planet** (the wreck of a former moon), realistic spacing; close-rock shots are deliberate passes of chosen rocks | Defence §4.1, H-05 |
| Q4 | The arrival | **Slow warp exit ~450,000 km out; shields parked with the tender**; the flip-and-burn moves to mid-film as the turnover | LREF §9, O1 |
| Q5 | Heat clock | **~24 min (Endeavor) and ~40 min (Astrid)** of full combat with fins stowed | LREF §8, A-31 |
| Q6 | May the LREF strike the planet's laser sites? | **No.** Beat them with geometry, weather, smoke and EW | LREF §13 |
| Q7 | Objective | **Orbital control for a T-SEC landing, not shown** in the film | LREF A-13 |
| Q8 | Warp rules | **Both confirmed**: velocity is conserved through warp; no bubble inside dense debris | LREF A-01, A-02 |
| Q9 | Hab rings in battle | **Keep spinning, depopulated** | LREF §10, A-34 |

### The fleet and the names

| # | Question | Decision |
|---|---|---|
| Q3 | Task group | **Expanded**: a hedgehog pack of three, a PD frigate and a tender added to the draft's fleet |
| Q10 | Ship names | Sci-fi references (the user's choice). **Hedgehogs:** *Infinity*, *Pillar of Autumn*, *Galactica*. **Gun frigate:** *Donnager*. **PD frigate:** *Excelsior*. **Destroyers:** *Canterbury* (lost early, as in *Leviathan Wakes*), *Extenuating Circumstances* (survives, kept as a destroyer). **Corvettes:** *Rocinante*, *Tantive IV*, *Wallfish*, *Normandy* (lost to the drones). **Tender:** *Nauvoo*. The Astrid and the Endeavor keep their lore names. |
| Q10 | Place names | New originals: the planet **Maren**, the moon **Skerry**, the debris ring **the Breakers**, the monitor ***Breakwater***, the faction **the Maren Compact** |
| — | Operation name | **Operation Tidebreak** (kept) |
| — | LREF losses | **The destroyer *Canterbury* and the corvette *Normandy***; the Endeavor loses a radiator fin |
| — | Ending | **A costly victory** |

### Phase 2 requests

| Request | Where it landed |
|---|---|
| Q16: Breakwater's reveal, sunlit or in eclipse ("The alt sounds fire.") | Revision 5 keeps the eclipse. The sun sits in the ring plane (the battle falls at Maren's equinox), so Breakwater is revealed in Maren's shadow, lit only by the red ring of the atmosphere, the city glow and its own missiles. The umbrella, the kill wave, the Casaba jets and the hail play in the dark, the spinal slug flies into Breakwater's sunrise during *The wait*, and the impact lands in the first full sun. The builder computes who is in shadow when; see the Light row on each card and maps D–E. |
| The AI alliance: the enemy as a human splinter faction allied with the AI, on a manufacturing world, with Tidebreak there to stem the tide | Revision 5: the report's Background and Situation paragraphs carry it (the Charon Innovations incident; the foundries); the mission ends "and shut the foundries down"; the destroyer finds the drones it can't hijack are "AI-run, no links"; the terms add the foundries and charts of the AI's emplacements, which answer to no one, the Compact included. The operation keeps its name ("Tidebreak"). |
| The script "dumbed down": realistic fleet chatter instead, and the intro as an official after action report | Revision 5: the lines are fleet traffic (callsigns, reports, orders, acknowledgments) that react to events and never explain what the crew already knows; the prologue is an after action report in six cards (header; background; situation; mission; restrictions; sources: "The following has been collated…"), and "END OF REPORT" closes the film. |
| Richer dialogue that carries the story; a text intro ("collated from the operation" plus an overview); an agent with no lore reading the film to see if the story holds | Revision 5: the report prologue on the stars; record captions on first sightings; lines that carry what the viewer needs as the crews would say it. Each cold reader sees only a generated audience script (`storyboard/audience_script.md`); their reports are in `review/coldread/`. Cold read 3 (on the chatter script) scored it 7/10 and led to: who stays at Anchor and who leaves with the Astrid ("Everyone else, on me"); Skerry's "first" and "last" salvos; the AI's guns that don't answer to the Compact; "Once she can't move, Astrid takes the kill"; a HEAT readout instead of SINK; fewer new names at once, with first tags only where there is time to read them. |
| Close-ups of the other weapons: missiles in flight, the nose sensors, railcannons waking and firing, laser arrays flashing and tracking | Revision 3: *Birds away* (a missile in flight), *Lenses* (a laser array tracking and pulsing), *Rails wake* and *Fire* (an M-1C waking and firing), *Seeker* (a Casaba killer's nose sensor in its last seconds). Revision 4 makes *Rails wake* follow the M-1C's own wake step by step (lids and amber cells, clamps off, lay, the supershell splitting and lifting, the jaws opening) and *Fire* its firing cycle (charge, bore pulse, recoil, the crest fins venting). "Nose sensors" was read as the missiles' seeker heads; say if you meant the Endeavor's own nose sensors. |

### The film

| Question | Decision |
|---|---|
| Runtime | **Flexible**: the story sets the length, and the storyboard reports it |
| Time and tactical picture | **A burned-in mission clock at each time jump, plus 2D tactical HUD inserts** |
| Cameras | **Cinematic free cameras**, with real lens behaviour |
| Interiors | **None**: exteriors only, with the HUD inserts as the "inside" view |
| Dialogue | **GUN-side comm lines throughout**, as subtitles first (voice acting maybe later). They ride the fleet's laser links, so they don't break its radio silence (LREF §7). The defender is never heard. |
| Sound | **Expanse-style**: near silence outside, sound through structure when the camera rides a hull, and big events as sub-bass |
| New asset scope | **Everything hero-detailed** |
| Render budget | **Up to a week per full pass** of the film |
| Q12: the M-1C's 0.33 s bore pulse (a real shot takes ~8 ms) | **Kept as cinematic licence**, labelled in the physics notes |
