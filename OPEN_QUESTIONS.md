# Open questions

Questions only the user can answer. Phase 1's questions were all answered at sign-off; they are kept below as a decision log, so the reasons stay with the choices.

## Still open

None of these blocks the storyboard; they matter when modelling starts. Each has a recommendation, and the storyboard currently follows it.

| # | Question | Why it comes up | Recommendation (what the board assumes) |
|---|---|---|---|
| Q13 | May the smallest assets be proxies? | "Everything hero-detailed" still stands, but some items are never bigger than a few dozen pixels (the closest-view table in `ASSET_REQUESTS.md`). The inner-ring stations are only points of light 21,800 km apart; the Nauvoo and the Excelsior's PD module are ~40 px behind the parked shields; the Donnager's gun module is only seen far off; drones stay under ~30–40 px. | **Ring stations as lights only; the Nauvoo, the PD module and the gun module as silhouettes; one drone design per side** (LREF and Compact), varied by payload. Everything seen larger stays hero. |
| Q14 | The ECW destroyer's dish: text or art? | The lore post says the antenna is "taking up a near third of the ship’s overall length (at the aft of the ship)", but also that "the stern is literally taken up by the ship's engineering section and radiators". Sir_Lazz's art (`reference_art/destroyer.webp`) puts a forward-facing dish on a truss just behind the shield, and the post's own account of its job ("eyes and ears… once the front impact shield is removed") fits the art. | **Follow the art** (dish forward, fixed on its truss). |
| Q15 | The modelling session's pending picks | The M-1C's wake style (split, ripple, bulk, extend, combined) and the PDC design (PD-1/2/3) were still waiting on you in the modelling session. The Endeavor rebuild, the Astrid's ~19 M-1Cs, the gun module and the PD module all inherit them. | No recommendation from here: they're your design picks. The build order puts them first. |

### Changed in phase 2 without a question (say if you disagree)

- **The rock is now called "Anchor"**, a placeholder in the sea-and-storm theme. "The lee of the Lee" read badly at speed. A better name is welcome.
- **A one-way hail before the spinal shot.** *"Breakwater, you can't move. Strike, or we fire."* No answer comes, so the defender stays unheard. The lore review asked for it; it fits the GUN's values.
- **The film is 4:11** (revision 1 was 2:45) with **62 shots** (was 37). Internal cuts became shots; new beats set up the losses and pay off the threats; your five weapon close-ups and the reviewers' holds added the rest. Runtime was left flexible.
- **The Endeavor keeps its 16 VLS cells** as the fast reserve (~4 min to Breakwater from the stop) rather than joining the kill wave. It could fire them in shot 50 if you'd like the moment.
- **The hedgehog pack keeps a guard at Anchor**, the Donnager and the Wallfish, and the defender now makes one try for it (Skerry's clouds ring the rock, drones follow); the guard beats it off.
- **The kill wave is ~40 Casaba killers among ~300 decoy and EW birds**, sized to cripple Breakwater's drive and leave the kill to the spinal shot; ~1,100 missiles stay in reserve.

## Decided at phase 1 sign-off

### The world and its rules

| # | Question | Decision | Where it lands |
|---|---|---|---|
| Q1 | Who defends the system? | **The Maren Compact**: a human polity that broke away from the GUN, with no warp fleet at Maren and **no relief coming** | Defence §1, H-01 |
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
| Close-ups of the other weapons: missiles in flight, the nose sensors, railcannons waking and firing, laser arrays flashing and tracking | Revision 3: *Birds away* (a missile in flight), *Lenses* (a laser array tracking and pulsing), *Rails wake* and *Fire* (an M-1C waking and firing), *Seeker* (a Casaba killer's nose sensor in its last seconds). "Nose sensors" was read as the missiles' seeker heads; say if you meant the Endeavor's own nose sensors. |

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
