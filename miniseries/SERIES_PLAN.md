# *Operation Tidebreak*: the pre-release mini-series

**Status:** a draft plan for the user. **Sources:** the lore posts, `doctrine/`, `storyboard/tidebreak_data.py`, `ASSET_REQUESTS.md`, `OPEN_QUESTIONS.md`, `pack/project_docs/`.
**Tags:** [P1 §n] is JCB's Part 1 post, point n, and [P1 classes] its class list; [P2] and [P3] are the frigate and destroyer posts; [Model] is the Blender README; A-nn, [LREF §n] and [WN §n] are the doctrine's assumptions, sections and working numbers; [User] is a decision already made.

## 1. Concept

### Title options
1. ***Spin-Up*** (recommended). Everything in the film spins up before it acts (warp rings, CIWS barrels, the M-1C), and the series is the film's spin-up.
2. ***Before Tidebreak***. Plain: a stranger knows what it is.
3. ***Hard Coat***. From JCB's "a soft sci fi setting wearing a hard sci fi coat".
4. ***Shields Off***. The order that opens every LREF battle [P1 §10].

### In-world framing
Each episode is in-world media from the months before the operation, made by whoever really would make it: the LREF and its fleet units, GUN-EWCC [P3], two contractors, a shipyard and two broadcasters. Eight are peacetime pieces that can't know Tidebreak is coming, which is the spoiler guard. The ninth is the news of the task group leaving.

### Series rules
- **Sound.** Narration, music and graphics belong to the medium. Footage of vacuum is silent unless the camera rides a hull or the sound comes on an instrument channel: comms, telemetry, a contact mic.
- **Numbers.** Only the lore's and the doctrine's, with their limits. Assumptions shown on screen (A-20, A-22 to A-25) become canon, so each episode lists them.
- **Look [User].** Invisible beams; lenses violet only while firing; blue only in the M-1C's bore pulse; heat only on the fins' radiator faces; fins stowed and shields on in warp.
- **No spoilers.** No Maren, Breakwater, Compact, Skerry, Breakers or Anchor, and nothing from the dropped AI plot line. No task-group names but the Astrid and the Endeavor, nothing damaged, no film framing copied. Systems appear in tests, drills and diagrams, never in battle. The series does teach the film's rules (time of flight, invisible beams, kill clouds, field reach, standoff, heat), so the film has less to explain.
- **No people on screen.** There are no character assets, so presenters are voices.
- **Assets.** New 3D work is film assets pulled forward, plus four cheap series-only set-ups: a witness plate, a one-mount laser and CIWS stage, clay and line overrides, and the missile's exploded split. The rest is 2D, all at 24 fps.

### What counts as "main"

| Subject | Decision | Why |
|---|---|---|
| M-1C; laser focusing arrays | Own episodes | Kinetics and DEWs are "the namestays" [P1 §4]; both built |
| CIWS, PD lasers, countermeasures | One episode | Your suggestion; layers of one defence [LREF §6] |
| Plasma lance | Own episode | One of the four families [P1 §3]; the torpedo appears as a drawing |
| Nuclear warheads, with their missiles | One episode | Missiles are "a warhead delivery platform rather than a distinct weapon 'system'" [P1 §5] |
| Spinal cannon | In the heavy cruiser's | SCCs "are effectively just built AROUND a big gun" [P1 classes] |
| Cruiser, heavy cruiser, frigate, ECW destroyer | Own episodes | The task group's classes with art and a lore post |
| Tender | In the frigate's | Its job is that episode's punchline [P2]; it has no art |
| EW and drones | In Eps 3 and 7 | Not systems of their own in the lore |
| Corvette | Dropped; a bonus later | No art and no picked concept: an episode now would fix its look before you choose it |
| Light cruiser, battleship, carrier, dreadnought, chem-rails | Dropped | Not in the task group; chem-rails are "near to obsolete" [P1 §3] |

### Tag and end card
- **Tag (5 s, every episode).** A hard cut to the film's still star plate. OPERATION TIDEBREAK types on in the report's white monospace, over a mission-clock counter rolling from T−[n+1] to T−[n] (the film's "digits roll" rule) and the release date. The only sound is the film's prologue tone.
- **Finale.** The counter reaches T−0 and the card becomes the film's first card, *The record* (UNITED NATIONS ARMED FORCES · LONG RANGE EXPEDITIONARY FORCES / AFTER ACTION REPORT · OPERATION TIDEBREAK / RESTRICTED).
- **End card** (the platform's end screen, outside the runtime): the next episode, the playlist, and "Based on JCB's *Wearing Power Armor to a Magic School*. Ship designs by Sir_Lazz."

### Order and cadence
- **Order:** the guns, then the defences and missiles, then the ships up to the flagship, then the departure, with the tone alternating: raw, glossy, vintage, silent, comic, loud, uncanny, grave, live. It follows the film's build order: Eps 1–4 need built assets, the Q15 picks and step 1's first-version effects; Eps 5–9 need step 3–4 assets.
- **Cadence:** two a week, with the finale on release day as the film's pre-show. Finish Eps 1–4 before Ep 1 airs; if the series must run alongside the film's production, go weekly.

### Runtime and render
- **Runtime:** 9:26 over nine episodes of 41–90 s (13,584 frames).
- **Method:** the film's classes (A 45, A2 90, B 75, C 200, S 30, D 15, E 2 s/frame at 1920×804), scaled by each style's pixel count. A one-mount stage ("ST") is costed from the measured M-1C stage (3–3.5 s/frame at 60 % and 64 spp): ~9 s/frame at full size, ~18 s as a 128 spp macro.
- **Total: ~51 h raw, ~66 h with the film's 30 % re-render allowance**, about 40 % of a film pass. Keep it out of the film's pass week: the film's gate has under an hour to spare (Q17).

## 2. Episode table

| # | Tag | Subject | Style | Runtime | In-world maker | Hook |
|---|---|---|---|---|---|---|
| 1 | T−9 | M-1C twin railcannon | Weapons-test footage | 60 s | The LREF (a declassified trial) | It fires in under a frame, hits a plate 100 km off four seconds later, then waits for its fins. |
| 2 | T−8 | Laser focusing array | Promotional advertisement | 42 s | The array's maker | A luxury ad for a beam no one will ever see. |
| 3 | T−7 | Point defence: CIWS, PD lasers, countermeasures | Vintage training film | 75 s | Fleet training (a re-issue) | Six layers between a ship and a missile, and the one rule they serve. |
| 4 | T−6 | Plasma lance | Technical-manual animation | 41 s | LREF technical publications | A lance ends where the ship's field does: about 50 km. |
| 5 | T−5 | Garibaldi-Ivanova frigate, with the tender | Infomercial | 90 s | The frigate's builder | One hull, three modules, swapped at your nearest fleet tender. Sold in packs. |
| 6 | T−4 | Nuclear warheads and their missiles | Defence-contractor trade-show reel | 55 s | A missile maker | A Casaba breaches a hull from 2–4 km away. |
| 7 | T−3 | ECW destroyer | Crew safety briefing | 60 s | GUN-EWCC | Why the fleet never uses radio, and who keeps it quiet. |
| 8 | T−2 | Hanuman heavy cruiser and its spinal cannon | Documentary | 68 s | A public documentary series | How the glass cannon became a pocket battleship. |
| 9 | T−1 | Ryland cruiser L.R.E.F.S. Endeavor | News segment, handing over to the film | 75 s | A news network | A task group leaves for somewhere the LREF won't name. |

The contractors, the shipyard and the broadcasters are placeholders to name (question 7).

## 3. Episodes

### Ep 1 · *Acceptance Trial, Run 4* (M-1C, weapons-test footage, 60 s)
**Premise.** Declassified footage: an M-1C on a test stand wakes, fires at a witness plate 100 km downrange, and is held for heat.

**Style**
- *Frame:* 4:3; a 2×2 split of locked cameras with IDs and timecode.
- *Grain, colour:* sensor noise, flat and clipped; sunlit; the high-speed window in monochrome.
- *Type:* a monospace data block (SLUG 10.0 KG · V₀ 25.0 KM/S · RANGE 100 KM · TOF), a slate, a red HOLD.
- *Camera:* locked cameras, a long-lens tracker, a replay marked HS 1,000 FPS.
- *Sound:* no music; range comms, countdown tones, a contact mic on the mount.
- *Voice:* range control: "Mount, you're hot."

**Beats**
1. 0–4 s: The slate.
2. 4–16 s: In 2×2: amber cells light, the clamps swing off, the cradle lays, and the shell opens in your wake style.
3. 16–21 s: "Gun A, on the tone." The 1.2 s charge, one white frame (the bore transit takes ~8 ms), the blast and the 7 m recoil; A's fins burst out, glowing.
4. 21–27 s: The replay: the blue pulse runs up the bore in the rig's 8 frames, 8 ms at 1,000 fps. Freeze at muzzle exit.
5. 27–33 s: The tracker: TOF counts to 4.0 s, then a white flash (3.1 GJ).
6. 33–38 s: Gun B fires; only B vents.
7. 38–50 s: HOLD. "Hold for heat." The fins cool as the timecode jumps. SUSTAINED: 1 RD/GUN/~15 S.
8. 50–60 s: END OF RUN; the tag.

**Lore.** Kinetics [P1 §3]; two guns of two rails per turret [User]; 10 kg at 25 km/s, 3.1 GJ (A-20); 4.0 s to 100 km [WN §2]; one shot per gun every ~15 s sustained, because of heat [LREF §4.1]. The lore's "nearly 100 meter" length [P1 §6] stays off screen, so nobody measures the model against it.

**Assets.** Reused: `LREF_Railcannon_M1C.blend` (`RC_M1C`, `RC_FireCycle`, the Stage and its `CAM_RC_*` cameras, the `tracer` blast, the per-gun controls). New: a witness plate (series-only, from `plating.py`); a comp flash until FX-SLUG exists; 2D overlays.

**Render.** ST windows 0.7 h, ST full frame 1.5 h, D 0.6 h, E 0.2 h: **~3 h**.

**Risks.** It needs the wake-style pick (Q15). The real-time window keys `shot_a` 0→0.33 in one frame, and the replay plays the rig unchanged and stops at muzzle exit. That makes Q12's 0.33 s licence honest.

### Ep 2 · *Unseen* (laser focusing array, promotional advertisement, 42 s)
**Premise.** The array maker's brand film, shot like a luxury-watch ad: beta cloth, a polished lens, a violet pulse, and nothing else to see.

**Style**
- *Frame:* 16:9, full bleed.
- *Grain, colour:* clean, deep black, a hard sun key; saturated violet (glow ~1–2 under AgX).
- *Type:* a thin, wide-tracked sans, one line per card.
- *Camera:* motion-control macro slides, rack focus, a slow orbit.
- *Sound:* a sparse pulse on the yoke servo's tick, heard through the hull as in the film's *Lenses*.
- *Voice:* close-miked and unhurried.

**Beats**
1. 0–6 s: Macro over tufted beta cloth. "Some things are made to be seen."
2. 6–12 s: Rack focus to the lens lip. "This one isn't."
3. 12–18 s: The gear sector turns as the yoke slews. Tick. Tick.
4. 18–25 s: The lens pulses violet; far behind, defocused, a spark winks out. NO BEAM. ONLY THE LENS.
5. 25–30 s: 3.3 m · 350 nm · 25 MW.
6. 30–35 s: Pull back to the Endeavor's hull, a black PD laser beside the array. "It won't sink a ship. It takes its eyes, its radiators and its missiles."
7. 35–42 s: The logo; the tag.

**Lore.** DEWs are "the namestays" [P1 §4]; the Endeavor's 8 arrays and 8 PD lasers [Model]; the invisible beam and violet lens [User]; 3.3 m, 350 nm, 25 MW (A-22); lasers "strip; they don't sink" [LREF §4.2].

**Assets.** Reused: the Endeavor's arrays (`laser_power`, `laser_traverse`) and `CAM_LookDev_*` cameras. New: a one-mount laser stage (series-only); FX-PD's flash as the spark; 2D cards.

**Render.** Macro stage at 1080p 4.8 h, class A pull-back 2.0 h, E 0.1 h: **~7 h**.

**Risks.** Push the glow and AgX turns it lavender. An ad wants a visible beam, and it mustn't get one.

### Ep 3 · *Six Layers* (point defence, vintage training film, 75 s)
**Premise.** An old fleet training film, "revised edition: current fleet footage": a cheerful narrator walks new crews through the six layers between a ship and a missile.

**Style**
- *Frame:* 1.37:1, pillarboxed; a leader countdown and splice flashes.
- *Grain, colour:* black and white, with heavy 16 mm grain and scratches that also hide first-version effects.
- *Type:* hand-lettered intertitles, cel-animated diagrams.
- *Camera:* locked tripod shots, slow zooms.
- *Sound:* mono with optical hiss and a library orchestra. Hull shots carry the CIWS whine; drone shots stay silent.
- *Voice:* a warm mid-century narrator.

**Beats**
1. 0–6 s: The leader; SIX LAYERS · A FLEET TRAINING FILM.
2. 6–14 s: Six rings round a ship. "Each layer gets what the last one missed."
3. 14–22 s: Layers 1–3: a jammer, a drawn decoy, the arrays' ring at 30,000 km. "Blind it. Fool it. Burn it."
4. 22–30 s: Layer 4, a PD laser, "from 5,000 kilometres in."
5. 30–40 s: Layer 5: chaff, flares and smoke bloom and thin. "No air holds a screen up. Fire it just in time."
6. 40–54 s: Layer 6: a CIWS side-on, barrels blurring, and a cloud laid 5–30 km out. "The missile's own speed does the killing."
7. 54–66 s: A Casaba's jet reaching a hull from 2–4 km, and a red line at 10 km. "Anything that might be a Casaba dies before ten kilometres."
8. 66–75 s: THE END; the tag.

**Lore.** "Lasers, classic bulletstorm CIWS', kinetic kill clouds" [P2]; the Endeavor's 16 CIWS, 8 PD lasers, 6 launchers and 2 jammers [Model]; the layers and the Casaba rule [LREF §6]; ~280 rounds/s and clouds at 5–30 km [WN §8]; powered flares and thinning screens (A-27, A-28).

**Assets.** Reused: the Endeavor after the PDC pick, with `ciws_phase`, `ciws_fire`, `cm_chaff/flare/smoke` and `ew_active`; Ep 2's stage plus a CIWS mount; FX-PD and FX-SMOKE, whose step 1 versions pass under the grain. New: a vintage 2D kit.

**Render.** A2 smoke shot 3.7 h, A jammer 0.9 h, stage 0.7 h, E 0.7 h: **~6 h**.

**Risks.** The CIWS waits on the PDC pick (Q15); if that slips, swap Eps 3 and 4. The Casaba rule sets up the film's climax, which is fine if no target looks like a monitor.

### Ep 4 · *Field Reach* (plasma lance, technical-manual animation, 41 s)
**Premise.** An animated page of the Ryland-class manual: how a lance works, and why it stops where the ship's field stops.

**Style**
- *Frame:* 16:9, a manual page with FIG. numbers.
- *Grain, colour:* none: white paper, black lines, white clay, one violet-white accent.
- *Type:* a condensed technical sans, callouts, a CAUTION box.
- *Camera:* orthographic and exploded views.
- *Sound:* a click per step; no music.
- *Voice:* none; the captions narrate.

**Beats**
1. 0–4 s: FIG. 1: the bow in clay ortho, its four lance slots ringed.
2. 4–10 s: A block diagram of a field projector and a plasma source: boxes, not a design.
3. 10–17 s: STEP 1, FIELD: a dashed sheath runs from the nose to the target. STEP 2, PLASMA: a jet runs down it. ~1,000 KM/S · ~1 GJ A PULSE.
4. 17–24 s: FIELD REACH ~50 KM: the sheath ends, and the jet blooms and fizzles.
5. 24–30 s: AIMING: the lances fire along the bow, so the hull turns to bear.
6. 30–34 s: FIG. 2: a torpedo that carries its own field generator.
7. 34–41 s: CAUTION: NOT FOR USE BEYOND FIELD REACH; the tag.

**Lore.** Plasma needs "an active electromagnetic field to maintain its form lest it just fizzles out" and is "finicky and specialized" [P1 §4]. Four nose lances [Model]; ~1,000 km/s, ~1 GJ, ~50 km (A-23); a knife weapon [LREF §4.3].

**Assets.** Reused: the Endeavor's nose and `lance_power`. New: a clay and Freestyle set-up (series-only); a stylised jet, which keeps FX-LANCE for the film; 2D diagrams.

**Render.** Clay ortho at 1080p (class D) 2.3 h, E 0.3 h: **~2.6 h**.

**Risks.** A detailed cutaway would be a new design needing concept sheets [User], so it stays boxes. The manual states A-23, the doctrine's reading of a soft-SF weapon, as fact.

### Ep 5 · *The Multitool* (Garibaldi-Ivanova frigate, infomercial, 90 s)
**Premise.** The shipyard's late-night infomercial: the pitch is JCB's frigate post nearly word for word, and its caveats become the fine print.

**Style**
- *Frame:* 4:3 SD video (rendered at 960×720), star wipes, an offer bar.
- *Grain, colour:* soft, over-saturated video with chroma bleed and loud floodlight colours.
- *Type:* chrome bevelled words, starbursts, a tiny crawl.
- *Camera:* fast zooms, whip pans, before-and-after splits.
- *Sound:* a cheesy synth, studio-audience "ooh"s and a BUT WAIT stinger; the launches silent (a drone camera).
- *Voice:* a loud pitchman, and a co-host feeding him problems.

**Beats**
1. 0–6 s: TIRED OF ONE-TRICK WARSHIPS? "Bought a battleship for a drone war?"
2. 6–18 s: The frigate turns. "One hull. Every job." Callouts: the shield, the warp rings, the hab section, the radiators that retract for warp.
3. 18–28 s: The stripped hull ("like a fluffy cat out of a bath") beside the hedgehog. "Just shove in the hot-swappable missile pod module!"
4. 28–33 s: A drone along the hull as the pod doors ripple open. "About 360 pods!"
5. 33–53 s: "Need help at medium range?" Four kinetic batteries. "They've specced everything into drones?" Lasers, bulletstorm CIWS, kill clouds. Both modules appear as concept-sheet cards.
6. 53–61 s: "Just swap it out at your nearest fleet tender!" A tender cartoon.
7. 61–74 s: BUT WAIT: "the biggest, baddest, meanest dreadnought" against 5, 10 and 20 packs. "Does it really add up?"
8. 74–85 s: The crawl: "A sole MAV frigate is more than likely insufficient… Once expended, 4 CIWS mounts remain."
9. 85–90 s: The tag.

**Lore.** All [P2]: "the premier generalist platform"; ~400 m; ~360 pods; the gun module for "that awkward middle-range gap"; the PD fit; the tender; packs and "the economics of war"; the 4-CIWS limit; the cat. Plus ~700 missiles a hedgehog (A-26).

**Assets.** Reused: GI and GI-MAV with `pod_ripple` (film step 3); FX-SWARM, with MSL-V or, at SD, the scaled MSL. New: the 2D kit; module and tender cards from their concept sheets (silhouettes in the film, Q13); a dreadnought silhouette.

**Render.** B at SD 4.9 h, the C launch 3.0 h, E 0.8 h: **~9 h**.

**Risks.** Comedy against a grim film, but it's JCB's own voice. Use a hull number, not the pack's names.

### Ep 6 · *Standoff* (nuclear warheads, trade-show reel, 55 s)
**Premise.** The loop a missile maker plays on its expo stand: the capital-ship killer and its Casaba warhead.

**Style**
- *Frame:* 16:9 for a video wall, with centre-safe type.
- *Grain, colour:* clean CG in navy and cyan; the missile photoreal on black; SIMULATION on engagement graphics.
- *Type:* a bold geometric sans, kinetic type.
- *Camera:* CG orbits, smash zooms, speed ramps.
- *Sound:* driving electronic music with a hit on each word; it loops.
- *Voice:* none, since the expo floor would drown it.

**Beats**
1. 0–4 s: The logo; the nose turns out of black.
2. 4–14 s: Exploded turntable: ablative nose, seeker shutter, warhead, MIRV bus, motor. HARDENED NOSE · SPIN · THREE GUIDANCE PATHS.
3. 14–20 s: 30 G · Δv 150 KM/S · 100,000 KM IN 18 MIN.
4. 20–28 s: NO BLAST WAVE IN VACUUM: a bare burst strips fins out to 1–3 km, but breaches a hull only within ~30–110 m.
5. 28–38 s: SIMULATION, on a box hull: a Casaba jet breaches the belt from 2–4 km. STANDOFF 2–4 KM.
6. 38–44 s: The missile slides into a hedgehog pod.
7. 44–55 s: The logo, a stand number, the loop point; the tag.

**Lore.** Nuclear means "Casaba howitzers, conventional, etc", "much more commonplace and reliable than even plasma" [P1 §3–4]; missiles are platforms [P1 §5]; capital-ship killers and MIRVs [P2]; vacuum effects [LREF §4.4]; the Casaba jet (A-24); the missile's numbers (A-25).

**Assets.** Reused: MSL-V's capital-ship killer, whose LOD0 is built for the film's *Seeker*; a GI-MAV pod. New: the exploded split, with sections set by the concept sheet; 2D graphics.

**Render.** The missile as a one-object stage at 1080p 1.6 h, E 0.5 h: **~2 h**.

**Risks.** It waits on the missile concept and MSL-V (film steps 2 and 4); if they're late, swap Eps 6 and 7. The real Casaba jets stay in the film.

### Ep 7 · *Through Glass* (ECW destroyer, crew safety briefing, 60 s)
**Premise.** The GUN-EWCC briefing every crew sees on joining a task group: why the fleet never uses radio, and who keeps it quiet.

**Style**
- *Frame:* a 16:9 safety-card layout, with the destroyer in a rounded inset.
- *Grain, colour:* flat pastel pictograms; the inset in the film's grade.
- *Type:* a rounded sans, numbered rules, ISO-style pictograms.
- *Camera:* static centred cards; a slow orbit in the inset.
- *Sound:* soft muzak with a chime per rule; the destroyer is silent.
- *Voice:* a calm airline-safety announcer, faintly uncanny.

**Beats**
1. 0–5 s: GUN-EWCC · CREW BRIEFING · EMISSIONS CONTROL.
2. 5–13 s: Rule 1: "For your safety, this fleet does not use radio. Every transmission tells someone where you are."
3. 13–21 s: Rule 2: "Talk by laser. Only someone standing in the beam can hear it."
4. 21–37 s: From the stern quarter, a ~200 m destroyer, its dish forward on the truss, runs out its booms and scatters drones. "Your destroyer is your relay, your sensor net, and the screen that hides your chatter."
5. 37–49 s: Rule 3: "Two sensors, or it isn't real." Rule 4: "Every drone of ours has a kill switch, so no one can return it to sender."
6. 49–55 s: The motto: WARS FOUGHT THROUGH GLASS, AND ENDED WITH MATH.
7. 55–60 s: The tag.

**Lore.** From [P3]: ~200 m; no main weapons; banks of supercomputers; GUN-EWCC crews; drones; the dish as the "eyes and ears" once the shield is off; "return to sender"; the motto, JCB's own line. It can silence "the radio-emissions of an entire fleet" [P1 classes]. EMCON (A-29); D10.

**Assets.** Reused: DD (film step 3) with `booms_deploy` and `drone_bay`; an SHD shield; DRN-L as specks. New: a pictogram kit.

**Render.** B at 720p 4.8 h, E 0.6 h: **~5.4 h**.

**Risks.** The dish fills the inset, so Q14 must hold (dish forward, as in the art). Don't name the destroyer: the Canterbury is lost in the film.

### Ep 8 · *The Pocket Battleship* (Hanuman heavy cruiser and spinal cannon, documentary, 68 s)
**Premise.** A public documentary segment: how the heavy cruiser went from glass cannon to pocket battleship, told through the Astrid.

**Style**
- *Frame:* 16:9, with present-day footage letterboxed at 2.39:1 and drawings at 4:3.
- *Grain, colour:* a warm documentary grade; cyanotype and sepia drawings; a false-colour thermal insert.
- *Type:* an elegant serif, chapter cards, lower thirds.
- *Camera:* slow dollies, pans across drawings, a long-lens archive shot.
- *Sound:* strings and piano over silent footage, dropping out for the spinal flash.
- *Voice:* an older historian, measured and dry.

**Beats**
1. 0–6 s: "Every ship in the fleet is classed by one rule of thumb: length."
2. 6–15 s: Line drawings, MULTI-ROLE beside SPINAL CANNON CAPABLE. "Like designing a ship for a gun."
3. 15–24 s: I. THE GLASS CANNON: "a spinal cannon at the expense of everything", and a battlecruiser stamped NEVER WENT ANYWHERE.
4. 24–34 s: II. THE POCKET BATTLESHIP: a dolly along the Astrid's aft hull as its eight stacked fins run out and glow. ASTRID · HANUMAN CLASS · 1,600 M.
5. 34–40 s: THERMAL: "She glows in thermals. Fins out, she can be seen fifteen AU away."
6. 40–45 s: The AVPSA tilts: "just over a hundred metres across."
7. 45–55 s: Archive, long lens: a distant heavy cruiser turns (compressed, and labelled so), steadies, and a small flash sparks at its bow. "A kilometre of her is gun. To aim it, she turns."
8. 55–63 s: A push on a still. "She turns slowly, her armour is thin, and she can't hide."
9. 63–68 s: The tag.

**Lore.** From [P1 classes]: classing by length; MRVs and SCCs; glass cannons and pocket battleships; a spinal of "a good kilometer or so"; the battlecruiser that "never went anywhere". From [P1 §7]: 8 fins past the warp-ring boundary; "GLOWS in thermals"; the AVPSA; weak manoeuvrability, armour and stealth. [P2]: 1,600 m. ~15 AU [WN §5]; aiming by turning [LREF §10].

**Assets.** Reused: AST (film step 3) with `fins_deploy`, `avpsa_az/el` and `rcs_bow/stern`; FX-SPINAL as a far flash only. New: line renders of EN and AST; 2D drawings and graphics.

**Render.** B 7.5 h, D 1.0 h, E 0.6 h: **~9 h**.

**Risks.** The Astrid's ~19 M-1Cs and its CIWS inherit Q15. Never show the bloom down the barrel, which is the film's climax. Sir_Lazz's art itself needs permission (question 8).

### Ep 9 · *Undisclosed* (Ryland cruiser Endeavor, news segment, 75 s)
**Premise.** Evening news: a task group, the Endeavor nearest the camera, leaves on a deployment the LREF won't describe. The live picture ends as the warp rings light, and the segment hands over to the film.

**Style**
- *Frame:* 16:9 broadcast, with a bug, a LIVE tag, a ticker and FILE tags.
- *Grain, colour:* sharpened, compressed video with pumping exposure; no heat shimmer, since there's no air.
- *Type:* the network's lower thirds and ticker.
- *Camera:* a station's operator-driven long lens, the ship under a third of the frame; closer FILE clips.
- *Sound:* the news theme and studio voices over silent pictures.
- *Voice:* a neutral anchor and a live, slightly breathless reporter.

**Beats**
1. 0–6 s: "An LREF task group is leaving tonight on a deployment the service won't describe."
2. 6–16 s: LIVE: the Endeavor over the planet, shield on, fins stowed, rings turning. L.R.E.F.S. ENDEAVOR · RYLAND-CLASS CRUISER.
3. 16–26 s: FILE: turrets on their travel locks, a laser array, the missile cells. "Every weapon family the fleet has, on one hull."
4. 26–34 s: LIVE: fourteen sets of running lights. "Behind her, the flagship Astrid."
5. 34–42 s: FILE: the gold shield. "It rides ahead of her in warp. Before a fight, they leave it with the tender."
6. 42–52 s: LIVE: the rings brighten as the clock jumps three minutes. "There's no sound out here. Just the light."
7. 52–58 s: A blue-white bloom whites out the camera, which recovers on empty stars. "And she's gone."
8. 58–64 s: "The LREF will release details when it can." Freeze; the signal drops.
9. 64–75 s: Black; the counter rolls to T−0; the film's first card and the release date.

**Lore.** [P1 §6]: the Ryland class, an exploratory variant of the Grace class, with railguns, arrays, lances and missiles but no spinal cannon. [P1 classes]: 950–1,400 m, "the workhorse of both the LREF and EAF". [P1 §10]: the shield, left before battle and collected after. [Model]: 1,194 m; rings at 2.4 rpm. A 3–5 min spool (A-05).

**Assets.** Reused: the Endeavor rebuilt after Q15 (`warp_charge`, `ring_rpm`); the World shader's Earth-like planet; FX-WARP; FX-FAR; the film's first card and star plate. New: the news 2D kit.

**Render.** S at 720p 3.1 h, A at 720p 3.2 h, D 0.5 h, E 0.3 h: **~7 h**.

**Risks.** The film defines only the arrival flash (A-04), so the departure's look is your call (question 6). The other ships stay as lights, since the corvette and tender have no design yet.

## 4. Open questions

| # | Question | Recommendation |
|---|---|---|
| 1 | The series title | *Spin-Up*; *Before Tidebreak* if you want it plain. |
| 2 | Which classes count as main | The nine above, with the corvette as a bonus recruitment ad between Eps 7 and 8 once its concept is picked. |
| 3 | Style swaps | Keep them: only the news can end live into the film, and the lasers suit an ad about what you can't see. Possible swaps: the Astrid as the ad (but only the heavy cruiser has a lore history), or PD as gun-camera footage of a drill (rawer, but it explains less). |
| 4 | Episode length and cadence | Keep 41–90 s (9:26) and two a week. A 60 s cap saves about a minute, mostly cards, so under an hour of render. |
| 5 | Q15: the wake style and the PDC design | Your picks; nothing here favours one. They gate Eps 1 and 3 and reach Eps 5, 8 and 9. Pick both before rendering, or swap Eps 3 and 4 if the PDC waits. |
| 6 | Ep 9's warp departure | Mirror the arrival: FX-WARP's bloom, seen as a broadcast whiteout. |
| 7 | Names for the in-world makers | Use lore names where they exist; ask JCB to name the shipyard, the contractors and the broadcasters, or use logos alone. |
| 8 | Sir_Lazz's art on screen (Ep 8) | Use line renders of the models; show the art itself only with JCB's and the artist's OK. |
