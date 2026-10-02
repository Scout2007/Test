# Ep 2 · Laser focusing array (T−8)

Three separate events, all about the same invisible thing. **A** is a luxury brand film in which nothing is ever seen to happen. **B** is two technicians on the night shift, bored, aiming at a mirror. **C** is a friendly range game between two cruisers, with an umpire reading the scores. A has one spoken line, B is a two-hander over a comm loop, and C is a three-way chatter on a training net.

| Option | The event | Who speaks | The one idea | Words | Runtime | Render |
|---|---|---|---|---|---|---|
| A · *Unseen* | A brand film for the array: macro beauty, a violet flush, a far drone going dark | One brand voice, once | The beam is never shown; only its effect | 7 | 41 s | ~6 h |
| B · *Graveyard Shift* | Two techs fire alignment pulses at a reflector satellite and talk about a mug | Dee and Marek (comm loop) | The extraordinary tool is daily work: pulse out, a long wait, a small blip | 30 | 46 s | ~4 h |
| C · *Tag* | Two cruisers duel at training power with hit lights; the umpire calls it | An umpire, Tern's and Gull's helm | You are hit before you know it, so the only defence is hiding the sensor | 32 | 46 s | ~6 h |

Loglines, written first and kept apart. **A:** a luxury ad for a laser lens that blushes violet while a far drone's radiator quietly goes dark, with nothing in between. **B:** at night, two technicians fire pinpricks at a mirror in the dark and argue about a mug. **C:** two cruisers play laser tag in a rock field and learn they have been hit only when the umpire reads the lights.

---

## Option A · *Unseen*: brand film (41 s)

**Logline.** A maker's luxury film for the array shows cloth, polished petals, a gear and a lens, and a far drone's radiator dims, with no beam at any point.

**The idea.** The viewer feels the power by what is missing between cause and effect. The ad is proud of the gap, and the one joke is that the product's best work goes unnoticed.

**Look and sound.**
- Locked 16:9 at 1080p, clean deep black, one hard sun key, shallow depth of field, a slow slide and rack focus. Grade like a watch ad. The violet is saturated but kept low in the glow so AgX does not turn it lavender.
- The array's own camera is a macro on a stage with the mount cut out of the Endeavor; the only far object is a drone, defocused.
- No music. The sound is a low hull hum, as if a hand were on the plate, and the yoke servo's tick, both heard through the hull the camera rides on. The voice is one close-miked, unhurried speaker.
- The lens is violet only while firing. There is never a beam, a flash or a ray.
- The maker's name is [MAKER], one thin, wide-tracked line on the logo card.

**Storyboard.**

| # | s | Picture | Sound and words |
|---|---|---|---|
| 1 | 0–5 | Macro slide over tufted beta cloth. The sun key sweeps and each fibre snaps from black to white. | Hull hum only. |
| 2 | 5–11 | Slide along the array's petals, bright facets. Rack focus from a cloth seam to the lens lip. | Hum. |
| 3 | 11–17 | Macro on the gear sector. The yoke slews a few degrees toward something off-frame and stops. | Tick. Tick. The cut lands on the second tick. |
| 4 | 17–22 | The lens, dead on, black glass. It flushes violet, holds, and fades. Nothing leaves it. | The hum drops out for exactly as long as the glow. |
| 5 | 22–28 | Far behind the soft edge of the lens, a defocused drone. Its radiator panel is a dull red disc. The red dims to black and its tiny steering puffs stop. | Silence, then one tick. |
| 6 | 28–33 | Pull back: the Endeavor, small on black, the sun on one edge. | Voice, unhurried: "Some of our finest work goes unnoticed." |
| 7 | 33–36 | Logo card: [MAKER], one line. | Silence. |
| 8 | 36–41 | Tag. | The card's low tone. |

**Words.** 7 spoken. Numbers spoken: none.

**Built from.** EN (the array mount and hull, with the Endeavor's `laser_power` and `laser_traverse` rigs) · DRN-L (the drone, with its radiator face glowing dull red). Additions: a one-mount macro stage cut from EN (small: the same mesh, isolated); a cloth displacement shader on the existing blanket material (a material, not a model); a thin-type logo card (2D). Environments: black, a sun.

**Render.** Macro stage 22 s at ~18 s/frame, 2.6 h; class A defocused drone shot 1.8 h; class A pull-back 1.5 h; E cards and tag 0.1 h: **~6 h**.

---

## Option B · *Graveyard Shift*: night-shift CCTV (46 s)

**Logline.** On the night shift, two technicians fire alignment pulses at a mirror satellite and talk about a missing mug, and the one return blip is a small thing that arrives late.

**The idea.** Wonder is somebody's routine. The same tool that elsewhere takes a ship's eyes is, tonight, a pin pointed at a mirror, and the interesting event is the wait for the answer.

**Look and sound.**
- Berth CCTV at 720p: fixed cameras on gantry rails, soft, slightly green, a timestamp in the corner, a little compression. No camera moves except a slow lens drift on one.
- The scope is a 2D overlay: a trace sweeps left to right, a tick marks each pulse, and a bump is the return. The delay is shown as distance along the trace and is never explained.
- Sound is the comm loop only: hiss, a chair, a console chirp, two voices that overlap a little. No tick, no hull hum; everything outside the cabin is silent.
- The reflector satellite's own star-tracker camera is the only close view of the pulse: a violet pinprick far off in the dark.

**Storyboard.**

| # | s | Picture | Sound and words |
|---|---|---|---|
| 1 | 0–7 | CCTV wide: the Endeavor in a fitting-out berth at night, a few work lamps, a gantry. Nothing moves. | Hiss. DEE: "Anything?" Long pause. MAREK: "Not yet." |
| 2 | 7–16 | The reflector satellite's star-tracker view: stars drifting, a corner of its mirror tile catching the sun. At the end, five frames of a violet pinprick far down in the dark, then nothing. | DEE: "Did you take my mug?" MAREK: "Which one's yours?" DEE: "The one that's mine." |
| 3 | 16–25 | The scope. A tick; the trace sweeps to the end, flat. A second tick; the trace runs, and about two-thirds along a small bump rises. | MAREK: "Again." Then, after the bump: "...There." |
| 4 | 25–33 | CCTV close on the Endeavor's flank, the array slewed a few degrees and still. On the gantry module a window light comes on. | DEE: "That's it?" MAREK: "That's it. Your mug's on your desk." DEE: "...Oh." |
| 5 | 33–41 | The first CCTV wide. The work lamps go out one by one; one stays on. | MAREK: "Logged. Go home." Hiss, a click. |
| 6 | 41–46 | Tag. | The card's low tone. |

**Words.** 30 spoken (Dee 13, Marek 17). Numbers spoken: none.

**Built from.** EN (the array, hull, `laser_traverse`) · HUD (the scope's overlay style). Additions, each small: a reflector satellite (a flat mirror tile on a short spar, one mesh); a few gantry girders, work lamps and a lit-window box; a star-tracker "camera" (just a camera with a lens-hood prop). Environments: a bare berth against stars. The violet pinprick is the lens glow seen from far off.

**Render.** Class A at 720p, 23 s of berth shots, 3.1 h; class D star-field and scope plates at 720p, 18 s, 0.8 h; E timestamps, scope and tag 0.3 h: **~4 h**.

---

## Option C · *Tag*: range-control feed (46 s)

**Logline.** Two cruisers play laser tag at training power among rocks, and the umpire's hit lights go on before either crew knows it.

**The idea.** You are hit before you can know, so a ship's whole defence is turning its sensors away. The comedy is two proud crews rolling in circles.

**Look and sound.**
- A spotter-buoy camera on a rock at 720p, long lens, a little soft; a plain scoreboard overlay: TERN 1 – 1 GULL and a clock. The score is shown, not said.
- The ships are two Endeavor-class hulls with different stripes in white and amber (never blue) and different [hull numbers]. Their lenses are never shown.
- Small hit pads on each hull are cold green and chime on the range net when they light. They are green, not amber, so they cannot be mistaken for fin heat.
- Sound is the range net only: the umpire, two bridges, scoring chimes, open mikes. Everything else is silent.

**Storyboard.**

| # | s | Picture | Sound and words |
|---|---|---|---|
| 1 | 0–7 | Spotter cam: two cruisers hang apart among rocks, each in a lazy roll. Scoreboard 0 – 0. | UMPIRE: "Clock's running. Play nice." |
| 2 | 7–13 | Long-lens close on Tern's flank. One green pad on its back blinks twice and the scoreboard ticks. Nothing else happens for two seconds. | Chime. Silence. UMPIRE: "Tern, you're lit." TERN: "When?" |
| 3 | 13–19 | Tern starts to roll, and its sensor-mast shutters snap shut on the exposed side in turn. Gull begins to roll as well. | UMPIRE: "Just now. Dorsal, aft." TERN: "Rolling." GULL: "Match him." |
| 4 | 19–29 | Wide: both hulls turn together, slowly, like two people on one dance floor. A rock drifts through frame. Ten seconds is a long time. | UMPIRE: "Gentlemen, you're both just spinning." TERN: "That's the plan." |
| 5 | 29–35 | Gull's roll lags a beat. Its underside comes round and a pad under its hull blinks. The scoreboard goes to 1 – 1. | Chime. UMPIRE: "Gull's lit. Level." GULL: "...Where?" UMPIRE: "Underneath." TERN: "Nobody checks underneath." |
| 6 | 35–41 | Both ships stop rolling. One pad on each, blinking in step like indicators. | UMPIRE: "Time." A long tone. |
| 7 | 41–46 | Tag. | The card's low tone. |

**Words.** 32 spoken (umpire 21, Tern 8, Gull 3). Numbers spoken: none.

**Built from.** EN twice (a second livery on the same rig, with sensor-mast shutters and per-fin control) · HUD (the scoreboard style). Additions, each small: ~10 emissive green hit pads per hull (a material and a light each); a spotter buoy prop on a rock (a stick and a lens); two stripe textures. Environments: a generic rock field (drifting rocks, a star sky). No hero models are new.

**Render.** Class A at 720p, 41 s, 5.5 h; E scoreboard and tag 0.3 h: **~6 h**.

---

## Recommendation

**B** is my pick: it is the cheapest, it is the most human of the three, it shows the wait on the page instead of saying it, and its last line is the kind a night shift would actually say. **C** is the funnier and the only one with a real third voice; choose it if the series wants a laugh in its second week. **A** is the most beautiful but it is the series' third advert (Eps 5 and 6 are also adverts), so pick it only if you accept that. Decisions for you: whether two Endeavor hulls in different liveries are acceptable for C, and whether A's no-music, hull-borne sound is what you want from a brand film.
