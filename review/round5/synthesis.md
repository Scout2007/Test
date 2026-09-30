# Round 5 synthesis

Round 5 read **storyboard revision 5** (commit bcc0994: 69 shots, 6:58), with the same five reviewers. It was the first round on four things the user asked for after revision 4:
- the eclipse;
- the after action report;
- the fleet-traffic script;
- the Compact's alliance with the AI.

**No reviewer raised a major issue.** With round 4 that makes two rounds in a row with none, which meets the brief's stopping rule.

A session limit stopped all five reviewers once. Cinematography and production were stopped twice. Every report was finished from the frozen checkout of revision 5.

**Revision 6** (commit 489d24c and after) applies the round's minor issues and nits, except where noted below. It is 69 shots, 6:40. The render estimate is 122.4 h raw and 159.1 h with the 30 % allowance: 0.9 h under the 160 h gate.

No sixth round was run. Revision 6's changes are the reviewers' own fixes, and cold read 5 checks that the story still reads after the trims. The page says a sixth round is available if the user wants one.

Shot titles are used throughout, because the numbers shifted.

## The verdicts

- **Physics: no major issues.** The reviewer reproduced the eclipse independently:
  - a 67.5-minute umbra, and a 128 s penumbra crossing inside *The wait*;
  - the escorts', the Astrid's and the waves' shadow times;
  - ~4.6 km of lee on both of Anchor's shadows;
  - every number the dialogue states.

  Left over: a lighting claim (the red ring can't light a hull deep in the shadow), the atmosphere's effect on the shadow, Skerry's phase, and "six hours".
- **Doctrine: no major issues.** It found the traffic reads as a fleet net, and the AI lore and the eclipse both hold tactically. Left over:
  - *Blind it*'s full power on Site 1 would be a burn;
  - the fire plan sent the reserve hedgehog along;
  - four wording and procedure nits;
  - make the eclipse the planners' choice.
- **Lore: no major issues.** The header, the L.R.E.F.S. prefix and the report's voice fit the GUN's LREF. The AI lore conflicts with nothing in the posts. Left over:
  - "SENSOR DESTROYER" mislabels the e-warfare ships;
  - the reason the shields come off had left the screen;
  - the thinned net isn't shown;
  - four nits.
- **Cinematography: no major issues.** The eclipse, the report frame and the traffic work, and the climax reads in the dark. Left over:
  - the film had tipped into a reading film;
  - four dark shots lacked a key light;
  - held beats were filled with text;
  - three nits.
- **Production: no major issues.** The gate machinery works, the eclipse is costed sensibly and the cards are nearly free. Left over:
  - the budget sits on the gate, and the gate's report broke when it fired;
  - three benchmarks don't match their shots;
  - *The wait*'s sunrise can't come from a cross-fade;
  - the 2D work had no owner;
  - small asset and builder nits.

## The cold reads

Each cold read is a fresh agent with no lore. It reads only the builder's audience script (`storyboard/audience_script.md`) and retells the story. Its reports are in `review/coldread/`.

| Read | Version | Score | Its biggest gaps, and what changed |
|---|---|---|---|
| 1 | Revision 5's first, explanatory script | 7/10 | The user then asked for fleet chatter instead ("dumbed down"). |
| 2 | The first chatter script | — | Cut off by a session limit; it never reported. |
| 3 | Chatter, the report, the AI lore (19f7e24) | 7/10 | The climax's layout, Skerry's rounds seeming to arrive twice, the AI staying abstract, jargon. Fixed in bcc0994: "Everyone else, on me" and the Astrid's track, Skerry's "first" and "last" salvos, "the AI's guns don't answer to them", HEAT for SINK, first tags placed where they can be read. |
| 4 | bcc0994 (round 5's version) | **8/10** | The AI still abstract; look-alike names; unstated steps in the endgame. Revision 6 names who crews Breakwater ("COMPACT MONITOR"), puts "you're the whole net now" on screen, gives the exact on-target times, and resolves the two "she"s in *Sixty-four*. What the AI wants and where it is are left to the user (Q18). |
| 5 | Revision 6 | pending | Checks that the trims below kept the story readable. |

## Minor issues and nits: what revision 6 did

### Physics
- **Moonlight is the key light in the shadow.**
  - Bent sunlight reaches only the outer few hundred kilometres of the shadow. So deeper in, Skerry's moonlight (~0.01 lux) is the key, and the red ring is a faint rim.
  - This is changed in LIGHTING (the builder's eclipse text), World E, WORLD, the Methods row, *The anvil*, *Blind it*, *The spend wave* and *Heat*.
  - The red now rises only in the last ~5 minutes before each sunrise (*The hail*, *The wait*).
  - Recorded in `OPEN_QUESTIONS.md`, since it adjusts the look the user picked.
- **The atmosphere.** The shadow now includes ~75 km of air (`R_SHADOW`), and SUN is 33.1°. First light is T+7:55:13, full sun T+7:57:21, and the slug lands at 7:57:29, still in the first full sun. Breakwater enters the shadow at T+6:46:52.
- **Skerry is ~3.5 % lit** in *Birds away*.
- **"Six and a half, give or take."**

### Doctrine
- ***Blind it*.** The arrays go to full on Breakwater's optics only. Site 1 stays at the under-1 % dazzle it has had since T+5:43: "Arrays full on Breakwater. Site One, dazzle only." The rig is split to match. The restriction card now ends "…laser sites included; they could be dazzled, not struck."
- **The fire plan.** "Missile frigates hold here with Donnager and Wallfish. Everyone else, on me." The Pillar stays at Anchor.
- **Nits.**
  - Actual's first call now comes after the Astrid is out of warp. The Endeavor reports its own exit first.
  - The turn order is "Everyone on me, come left two degrees." The reviewer suggested "All Tidebreak", but that would include the pack at Anchor, which cold read 3 took for a contradiction.
  - "Point defence lit. Kill wave steering clear."
  - The spend wave carries ~90 warheads everywhere.
  - The inner ring is AI-run: it doesn't stand down with the Compact, the charts in the terms cover it, and the Endeavor risks its fins anyway.
- **The eclipse as the planners' choice.** The fire plan's plot draws Maren's shadow over Breakwater. The action notes the kill is timed into the dark (O9). The reviewer's text label was left out for reading time.

### Lore
- **"E-WAR DESTROYER"** in both first tags. The full "E-WARFARE" didn't fit the net's reading window.
- **The shields.** *Shields to the park* now shows the plate backing away to uncover the bow turrets and sensors, which is why it comes off. *The Breakers* says "Corvettes, sweep." There was no reading time for "No shields".
- **"Extenuating, you're the whole net now."** opens *Return to sender*. "Return to sender" itself goes, to make room.
- **The Background card** now says "a later licensed system … escaped too", so "it" can't be read as the company.
- **Who flies which drones.** The AI runs the unlinked drones and the emplacements; crewed control craft fly the linked drones. This is in DEFENDERS, Defence §1, HD9 and H-01.
- **Declined, for reading time:**
  - spelling out T-SEC (the card already says "T-SEC ground forces");
  - "HEAVY CRUISER" on the Astrid's caption. FLAGSHIP carries the Actual–Astrid link the cold readers needed.
  - "NO WARP RINGS". The film never names the rings, so "NO WARP DRIVE" reads better cold.

### Cinematography
- **Less to read.** The film is 18 s shorter, and every reading window is at or under the ceiling with first tags counted.
  - The report: 72 s → 68 s. Breakwater and the laser sites now first appear in *The picture*, which also separates "Breakwater" from "the Breakers".
  - *The picture*: 20 s → 14 s.
  - *Anchor*: 14 s → 11 s.
  - *The fire plan*: 24 s → 21 s.
  - *Sixty-four*: 14 s → 13 s.
  - *Skerry burns*: 7 s → 5 s.
  - *Terms*: 14 s → 13 s.
  - **Not done:**
    - The 45–50 s report the reviewer asked for would cut the AI's history or the warp bar, which the cold readers relied on; `OPEN_QUESTIONS.md` offers it to the user.
    - The new long-lens shot of the fleet leaving Anchor would cost ~0.65 h, more than the 0.9 h margin can spare. The line and the plot track carry it.
- **Key lights for the dark shots:**
  - ***Heat***: a work light at the dump valve rakes the port belt. `dump_light` is requested on EN before the rebuild.
  - ***The anvil***: reads as a silhouette against the city-lit night side, edged by moonlight, with lit ports.
  - ***Spinal***: running lights and RCS puffs light the settle.
  - ***The wait***: the sunrise point sits near the frame edge, so the light rakes across the hull.
- **Held beats.**
  - *The hail*'s line ends early ("…Surrender.", with a 0.8 s held silence), and *Spinal* waits 1.2 s before "Astrid, fire." "No response." is gone.
  - *Terms* has a 3 s hold for NO CARRIER, which the builder now checks.
  - Declined: lengthening *The hail* (class B) and *Umbrella* (class C). They cost 1–3 h of render each, and only the 2D shots were shortened.
- **Nits.**
  - "ENDEAVOR HEAT 77%" on *Sixty-four* bridges 31 → 88 %.
  - The first shot holds the resolved Endeavor 2 s longer (class D, cheap) for its caption.
  - The cue check now counts uncued lines that follow a cue. *Payback*'s "Splash." now comes at 0.5 s.
  - END OF REPORT gets a second of black before it.

### Production
- **The gate's report.**
  - It prints "N h over" and "can't close the gap alone" instead of negative numbers.
  - It shows one decimal, so 0.5 h is no longer rounded up to "1 h".
  - `MARGIN` now sits beside `GATE_HOURS` in the data.
  - Lever 3 points at the costliest seconds: *Heat*, then the class C holds.
  - Q17 asks the user now which fallback they prefer.
- **Benchmarks.**
  - A new `B@E` entry covers the dark class B shots.
  - A new *Countermeasures* smoke run also covers *Turnover* (`BENCH_ALIAS`).
  - *Blind it* moves under `A@C`.
- ***The wait***: one plate with Cycles light groups, the Sun group keyed in comp.
- **The 2D work.** The storyboard session generates the report cards and plot inserts from the maps' geometry. The style frame is in step 1 and the sequences in step 3. The cards' star plate is graded separately.
- **Nits.**
  - BW's ports are emissive, with emission sampling off.
  - Q15 now covers the CIWS mounts.
  - The builder says when node isn't there to parse the page script.

## Also fixed

- The page's sketches had stopped drawing: an apostrophe in one sketch broke the whole script. The builder now checks each sketch's quotes and, where node is installed, parses the script.
- Act IV's timeline band and links had lost their styles when the prologue was added. The styles are now keyed to act names.
- The round 4 synthesis's revision 5 numbers (121 h, 157 h, 5:55) and its "SINK 63%" on *Site One* describe revision 5 as it stood then. The figures above supersede them.
