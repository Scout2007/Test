# Ep 2 · The laser focusing array (T−8)

Every option closes on the 5 s series tag (the film's title card; the clock rolls T−9 to T−8 over [release date]; the card's low tone) and then the platform end card (+5 s, outside the runtime: Ep 3 (T−7), the playlist, "Based on JCB's *Wearing Power Armor to a Magic School*. Ship designs by Sir_Lazz."). Held throughout: no beam is ever seen; the lens is violet only while firing; no stars behind a sunlit hull; vacuum is silent except hull contact-mic ticks and instrument tones; no people on screen. Hours are raw (the plan adds 30 % for re-renders): frames × class at 24 fps. Slow-down labels are captions, not canon.

## Option A: *Unseen*, a luxury brand film (42 s)

### 1. Concept
[maker]'s launch film for its laser focusing array, shot like a luxury-watch ad with every convention honoured (material, movement, complication, spec line, wordmark) except the one that needs a beam. The genre collides with the physics, so the style is the joke, and it pre-teaches the film's *Lenses* look: a violet lens, no beam, a tick through the hull.

### 2. Style bible
- **Frame.** 16:9 full bleed; pure black, no stars behind a sunlit hull.
- **Camera and lens.** Motion control: constant-speed slides and arcs, no handheld, no speed ramps. 100 mm macro, 50 mm rack focus, 28 mm behind the lens plane for the line of fire, 135 mm locked on the glass.
- **Grade and texture.** The film's grade (AgX High Contrast, −0.3 EV, one hard sun at 6 W/m² raking low) minus grain, vignette, dispersion and halation: clean is the luxury. Violet (glow 1–2, via the compositor's emission-exempt path so AgX doesn't turn it lavender) on the lens alone; no streaks or volumetrics, which would draw a beam by accident.
- **Type and graphics.** Hairline extended caps, tracked wide, one line per card, below the subject, cut in on a tick. Mark: a hairline ring (the aperture) with one violet point. A car-ad "closed course" super marks the spark as a test.
- **Sound and voice.** No melody: a sub-bass drone with glass-harmonic overtones, entering after the first pulse. The only rhythm is the yoke servo's tick as a hull contact mic hears it, one per pulse; "tick, tick, rest" is the sonic logo. Voice: close-miked, low, unhurried; 51 words.
- **Edit rhythm.** Cuts land only on ticks; the ticks climb from one every two seconds to two a second, stop dead at the spark, and the next tick is the first pulse.
- **Study.** Swiss watch brand films (constant-speed macro); Apple's materials-first product films; lens-launch films (rack focus to the coating); fragrance films (negative space).

### 3. Storyboard
| # | Time | Shot | On screen | Text | Voice-over | Sound |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:04 | Macro slide, 100 mm, sun from left | Tufted beta cloth into black | none | "Some things are made to be seen." | Faint hull hum |
| 2 | 0:04–0:08 | Locked 50 mm, rack focus to the lens lip | Lip and iris ring sharpen; a glint rolls round the rim | none | "This one isn't." | First tick, on the cut |
| 3 | 0:08–0:12 | 85 mm arc round the barrel sleeve | Quilting turns from sun to shadow | none | "Tufted. Creased. Tied down for a life without air." | Ticks at 0:08, 0:10 |
| 4 | 0:12–0:16 | 100 mm slide along the elevation sector | The pinion walks the sector, tooth by tooth | none | "A joint set low. The optics carried high." | A tick per tooth |
| 5 | 0:16–0:21 | Locked 28 mm behind the lens plane, down the line of fire | Empty black; at 0:20 a far pinprick winks out (FX-PD) | 0:18 "NO BEAM." ; 0:19 "CLOSED RANGE · CALIBRATION TARGET" | none | Ticks 1, then 2 a second; all stop at the spark |
| 6 | 0:21–0:29 | Locked 135 mm, face-on to the lens | Four violet pulses; dark; specs in turn | 0:22 "ONLY THE LENS." ; 0:24 "3.3 M APERTURE" ; 0:25 "350 NM" ; 0:27 "25 MW" | 0:24 "Twenty-five megawatts of ultraviolet, held to a point." | A tick per pulse; the drone enters at 0:24 |
| 7 | 0:29–0:35 | Pull-back, zoom 135 to 50 mm, to `CAM_LookDev_Pair` | The array shrinks into the hull; its black PD laser sharpens | 0:33 "ALSO IN BLACK." | "It won't sink a ship. It takes its eyes, its radiators and its missiles." | Ticks stop; one held chord |
| 8 | 0:35–0:37 | Black card | Ring, violet point, wordmark | "[maker]" ; "UNSEEN." | "[maker]. Unseen." | Sonic logo: tick, tick |
| 9 | 0:37–0:42 | Tag | Title card; the clock rolls | "OPERATION TIDEBREAK" ; "T−9 → T−8" ; [release date] | none | The card's low tone |
| 10 | +5 s | End card | Ep 3, playlist, credit | the series credit line | none | Silence |

### 4. Lore facts shown
- Lasers are one of four families, "the namestays" with kinetics [P1 §3–4]; "various DEW Laser Focusing Arrays" on the Ryland class [P1 §6]; 8 arrays, 8 half-scale black PD lasers, the mount and the lens [Model].
- Invisible beam, violet lens only while firing [User]; no stars behind a sunlit hull [LIGHTING]; one hull tick per pulse [*Lenses*].
- 3.3 m, 350 nm, 25 MW [A-22], canon once shown; lasers "strip; they don't sink" [LREF §4.2].

### 5. Assets and render
- **Reused:** the Endeavor's array (`laser_power`, `laser_traverse`, `laser_elevation`) and black PD laser; `CAM_LookDev_Yoke`, `_Front`, `_Pair`; `LREF_Compositor`; FX-PD's flash; the HUD kit.
- **New:** the plan's one-mount laser stage (series-only); 2D cards. No concept sheet.
- **Render:** shots 1–6, 696 frames × 15 s = 2.9 h; pull-back 144 × 45 s = 1.8 h; cards 288 × 2 s = 0.2 h: **~4.9 h**. Locked shots 5–6 with a lens light group would save ~1.3 h.

### 6. Risks
- Glow past ~2 turns lavender under AgX.
- A beam by accident: keep spokes, streaks and volumetrics off the line of fire (the thin red-edged strut in `lookpair_final.jpg` runs at beam angle).
- The spark must read as a test: the super, a calibration target, no missile.
- Quilted macros may run ~18 s a frame (+0.6 h); the stage isn't built.

## Option B: *Nothing to See*, a visitor-centre exhibit film (44 s)

### 1. Concept
The wall film in [visitor centre]'s Ryland-class gallery: a docent's audio-guide walk past a cut-away array model, a life-size lens ring on the floor, three discs of light painted to scale, and a glass case labelled THE BEAM with nothing in it. Museums exhibit what can't be shown, so floor decals and an empty case teach diffraction and invisibility faster than a diagram.

### 2. Style bible
- **Frame.** 16:9 for a wall screen; the voice captioned along the bottom tenth.
- **Camera and lens.** A visitor's-eye gimbal walk at 1.6 m, 28 mm, planted 1.5 s at each stop; 50–85 mm orbits of the model at walking pace; no whips, no handheld.
- **Grade and texture.** A dark gallery: black walls, a glossy floor mirroring the guide line, warm (~3,000 K) spots on the model, cool label lightboxes, soft halation, no grain; violet only on the lit lens.
- **Type and graphics.** Museum wall text: humanist sans, sentence case, on pale lightbox plates in the scene; round stop badges; a floor-plan pip whose dot jumps to each stop; numbered pins on the cutaway.
- **Sound and voice.** A large quiet room: room tone, soft reverb, footsteps that stop when we plant, a two-note chime before each stop, stepper motors in the gallery's air, a quiet pad; a sine tone climbs with the meter (an instrument channel). Docent: warm, patient, close to the ear, imperatives, dry at the empty case; about 100 words; not an announcer (Ep 7) or a historian (Ep 8).
- **Edit rhythm.** Walk, plant, tell: stops of 3–7 s joined by continuous glides; hard cuts only on the chime; labels carry the numbers.
- **Study.** Science Museum London and Smithsonian Air and Space audio tours; sectioned models at Space Center Houston; Exploratorium exhibits.

### 3. Storyboard
| # | Time | Shot | On screen | Text | Voice-over | Sound |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Gimbal glide through a doorway, 28 mm | Lit sign; guide line on a black floor | "GALLERY 4 · THE RYLAND CLASS" | "Gallery four. Please follow the line." | Footsteps; room tone; chime |
| 2 | 0:03–0:07 | Plant, 28 mm, push in 1 m | Cut-away array on a plinth under a warm spot; the pip jumps to 7 | "STOP 7 · LASER FOCUSING ARRAY · Model, cut away" | "Stop seven: a laser focusing array. The Endeavor carries eight." | Chime; a stepper turns the plinth |
| 3 | 0:07–0:12 | 85 mm arc of 60° | Blanket sliced to show its layers; yoke, sector, pinion beneath; a black box for the optics | "1 BLANKET · 2 SECTOR · 3 PINION" ; "BEAM TRAIN · NOT ON DISPLAY" | "The blanket is cut away to show the mount. The optics are not on display." | Steppers whir; a soft thunk |
| 4 | 0:12–0:17 | Tilt down, 28 mm; glide into a floor ring | A white ring at the lens's true size | "THE LENS, LIFE-SIZE · 3.3 M" | "Step into the ring. That is the lens, life-size: three point three metres." | Footsteps, hollow on the ring |
| 5 | 0:17–0:24 | Lateral track along a wall, 35 mm | Three to-scale discs of light: a table-tennis ball, a steering wheel, wider than the ring | "A FOCUSED BEAM STILL SPREADS" ; "100 KM · 4 CM" ; "1,000 KM · 39 CM" ; "10,000 KM · 3.9 M" | "Focused, it still spreads: a table-tennis ball at a hundred kilometres, wider than its own lens at ten thousand." | A soft note per disc |
| 6 | 0:24–0:31 | Plant, 50 mm, slow push along an empty case in the lens's line | The model's lens at left; beyond it an empty spot-lit case; a meter at zero | "THE BEAM · 25 MW · 350 NM · Not visible in space. Not emitted here." | "Stop eight: the beam. Nothing in space scatters it, and at three hundred and fifty nanometres it is ultraviolet anyway." | Chime; room tone only |
| 7 | 0:31–0:34 | Locked 85 mm, lens and meter | A button lights; three violet pulses; the bar climbs to 25 MW | "DEMONSTRATION: LENS LIGHT ONLY · NO BEAM IS EMITTED" | "Press the button. Only the lens lights." | A click; the tone climbs with the bar |
| 8 | 0:34–0:39 | Locked 35 mm, then a turn to an exit sign | Two-column wall panel; a green exit sign beyond | "DOES: BLINDS SENSORS PAST 1,000,000 KM · BURNS A RADIATOR, 11 S AT 10,000 KM · KILLS A MISSILE SIDE-ON, 0.2 S AT 1,000 KM" ; "DOES NOT: SINK AN ARMOURED SHIP" | "It blinds sensors at a million kilometres, burns radiators, and cannot sink a ship." | Footsteps recede; the pad fades |
| 9 | 0:39–0:44 | Tag | Title card; the clock rolls | "OPERATION TIDEBREAK" ; "T−9 → T−8" ; [release date] | none | The card's low tone |
| 10 | +5 s | End card | Ep 3, playlist, credit | the series credit line | none | Silence |

### 4. Lore facts shown
- 8 arrays on the Endeavor; the mount, blanket layers and materials [Model]; the Ryland class [P1 §6].
- 3.3 m, 350 nm, 25 MW [A-22]; spots of 4 cm, 39 cm and 3.9 m at 100, 1,000 and 10,000 km, with A-22's 1.5× jitter [WN §1]: both canon once shown.
- Dazzle past 10⁶ km [WN §1]; a fin in ~11 s at 10,000 km; a missile side-on in 0.2 s at 1,000 km; "strip; they don't sink" [LREF §4.2]. Invisible beam, violet lens [User].

### 5. Assets and render
- **Reused:** the array with its blanket as separate geometry; beta-cloth, foil and ceramic materials; `laser_power`; the HUD kit and star plate.
- **New (series-only):** a gallery of primitives (room, floor, plinth, cases, lightbox plates); a sectioned array (blanket sliced to a layered strip, mount cut at the yoke, optics a labelled black box); decals; the 2D pip, button and meter.
- **Render:** model close-ups (shots 2, 3, 7: 288 frames) × 45 s = 3.6 h; gallery shots (1, 4, 5, 6: 528) × 15 s = 2.2 h; panel and cards (360) × 2 s = 0.2 h: **~6.0 h**.

### 6. Risks
- The most new work (a set, a sectioned model); glass and gloss push past 15 s unless the glass is a flat shader.
- [visitor centre] must stay a placeholder, not the LREF.
- A real optics cutaway would be a new design needing a concept sheet [User]; the sealed box is the answer, and the joke.
- The press demo mustn't read as a lamp causing the glow.

## Option C: *Dwell Time*, a popular-science segment (42 s)

### 1. Concept
A segment from [show] with footage from [institute]: a presenter's voice-over and high-speed photography ask how you film a weapon that gives off no visible light, and answer that you time it. The laser's identity is time (light-speed delivery, milliseconds to blind, seconds to burn a fin, two minutes for a hull belt), which is what slow motion and a stopwatch make visible.

### 2. Style bible
- **Frame.** 16:9 clean broadcast; no lower thirds, bug or ticker (Eps 8–9): callouts pinned to the picture and one stopwatch.
- **Camera and lens.** High-speed windows: locked 85–135 mm on a black stage with a strip light and a kicker, motion blur off, a SLOWED badge; real time at a 180° shutter; speed ramps in and out; coupons seen square-on from a chase camera.
- **Grade and texture.** Punchy and clean: neutral-cool blacks, hard speculars, no grain, brighter than the film's crush. Accents: violet (lens), heat orange (radiator coupons only), measurement green (graphics).
- **Type and graphics.** A bold condensed title sting; mono numerals; a green oscilloscope trace under every slowed shot; a stopwatch that resets per experiment; leader-line callouts; scale silhouettes (table-tennis ball, steering wheel, the 3.3 m ring).
- **Sound and voice.** A low pulsing synth bed, a riser into each slow-down, a sub-drop on each reveal, UI blips; slowed hull ticks time-stretched down; a pure scope tone as the instrument channel; coupons otherwise silent. Presenter voice-over: quick, curious, wry, second person; question, demonstration, payoff; about 100 words; [presenter] is a voice only.
- **Edit rhythm.** Shots of 2–6 s; hard cuts on riser peaks; each experiment ends on a number held for a full second.
- **Study.** BBC Horizon and PBS NOVA experiments; Mythbusters and Slow Mo Guys high-speed work; Veritasium-style numeric explainers.

### 3. Storyboard
| # | Time | Shot | On screen | Text | Voice-over | Sound |
|---|---|---|---|---|---|---|
| 1 | 0:00–0:03 | Locked 135 mm, face-on to the lens | The glass flashes violet twice | none | "This weapon is firing at twenty-five megawatts." | Two hull ticks; low pulsing bed |
| 2 | 0:03–0:05 | Locked 28 mm behind the lens plane | Empty black; nothing happens | none | "Can you see it?" | Silence |
| 3 | 0:05–0:08 | Title sting on black | The stopwatch starts at 0.000 s | "DWELL TIME" ; "HOW LONG A BEAM YOU CAN'T SEE HAS TO STAY" | "No? Then we'll time it." | Riser, sub-drop, UI blip |
| 4 | 0:08–0:13 | Locked 100 mm on the lens, high speed | One pulse blooms across the glass and fades; the green trace follows | "SLOWED ×50" ; "THE GLOW IS THE LENS" ; "BEAM: 350 NM, ULTRAVIOLET" | "That violet is the glass. The beam is ultraviolet, and nothing in space scatters it." | Hull tick time-stretched; scope tone |
| 5 | 0:13–0:17 | 2D: frame bar over a 10,000 km ruler | A photon dot stops inside the first frame | "10,000 KM · 33 MS" ; "ONE FRAME · 42 MS" | "Light covers ten thousand kilometres in thirty-three milliseconds. Less than one frame." | A blip as the dot lands |
| 6 | 0:17–0:22 | 2D: silhouettes against the 3.3 m ring | A table-tennis ball, a steering wheel, a disc wider than the ring | "100 KM · 4 CM" ; "1,000 KM · 39 CM" ; "10,000 KM · 3.9 M" | "Focused: a table-tennis ball at a hundred kilometres; wider than its own lens at ten thousand." | A blip per object |
| 7 | 0:22–0:28 | Locked 85 mm on a radiator coupon, high speed | A 39 cm white spot brightens, the panel glows, a hole opens | "RADIATOR PANEL · 1,000 KM" ; stopwatch to "0.113 S" ; "SLOWED ×40" | "A radiator panel, a thousand kilometres out. A tenth of a second. Slowed down, watch the hole open." | Scope tone climbs; sub-drop at the hole |
| 8 | 0:28–0:32 | Same camera, time-lapse | The panel reddens slowly and fails late | stopwatch to "11.3 S" ; "10,000 KM" ; "×10 RANGE = ×100 TIME" | "Ten times further, a hundred times longer: eleven seconds." | The tone crawls |
| 9 | 0:32–0:37 | Locked 50 mm, two coupons side by side | The fin coupon opens at 0.113 s; the belt coupon, time-lapsed, at 112.7 s | "FIN: 0.113 S" ; "HULL BELT: 112.7 S" ; "×1,000" ; "IF THE TARGET HOLDS STILL" | "A hull belt takes a thousand times longer. Lasers strip ships. They don't sink them." | The bed resolves to a held note |
| 10 | 0:37–0:42 | Tag | Title card; the clock rolls | "OPERATION TIDEBREAK" ; "T−9 → T−8" ; [release date] | none | The card's low tone |
| 11 | +5 s | End card | Ep 3, playlist, credit | the series credit line | none | Silence |

### 4. Lore facts shown
- DEWs, 3.3 m, 350 nm, 25 MW [P1 §4, A-22]; invisible beam, violet lens [User]; light crosses 10,000 km in 33 ms (light-lag is the film's own rule, WN §5).
- Spot sizes [WN §1]; a fin burns in 113 ms at 1,000 km and 11.3 s at 10,000 km: ×10 range costs ×100 time [WN §1, LREF §4.2].
- A hull belt (0.72 m [Model]) melts in 112.7 s at 1,000 km "if the target doesn't roll"; a fin is a 20 MJ/m² target, a hull 20 GJ/m² [WN §1]; "strip; they don't sink" [LREF §4.2]. A-22 and these thresholds become canon once shown.

### 5. Assets and render
- **Reused:** the array's lens close-up (`laser_power`; the lens as a light group, so a locked shot renders once and the pulse is a comp curve); Ep 1's witness plate (from `plating.py`) as the belt coupon; the fin-face material; FX-DAZZLE's bloom; the HUD kit.
- **New:** a 2D stopwatch, scope and callout kit; a flat fin coupon (series-only); a burn-through comp (emission mask, hole matte).
- **Render:** 600 frames × 15 s = 2.5 h; 528 frames of 2D × 2 s = 0.3 h: **~2.8 h**.

### 6. Risks
- Smoke lighting the beam, the genre's staple, is off-limits: the film won't give viewers a beam image.
- The most numeric option: every figure is canon, and the belt burn is the first hull shown to melt (a test coupon, "if the target holds still").
- Neighbours: Ep 1's high-speed replay (this is colour, crisp, graphic-led, and measures time) and Ep 3's explainer voice (a curious presenter, not a trainer).

## Comparison and recommendation

| | A · Unseen | B · Nothing to See | C · Dwell Time |
|---|---|---|---|
| The idea | The ad genre collides with the physics | An empty case and a ring on the floor | Time is the only way to see it |
| New work | One-mount stage | Gallery, sectioned model | Two coupons, graphics kit |
| Render | ~4.9 h | ~6.0 h | ~2.8 h |
| Main risk | An accidental beam | The most new work | Most numbers become canon |

**Recommendation: A.** It is the only option where the style is the joke: an ad exists to show the product, and this one can't be shown. It gives the series its sparsest voice between narrator-heavy slots, keeps the raw-glossy-vintage alternation, and shows the film's *Lenses* look first, on one reusable stage for ~4.9 h. B suits a calmer break and has the best single image (the empty case); C teaches the heat-and-time rules early but canonises most of its numbers. If A feels thin, C's "a hull belt takes a thousand times longer" can close shot 7 at no render cost.
