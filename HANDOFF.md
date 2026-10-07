# Operation Tidebreak: handoff

**Stopped at the user's request on 2026-10-07.** The branch is `claude/confident-ramanujan-b53a9q` on `Scout2007/Test`, and everything below is committed and pushed. This file is the starting point for the next session.

## 1. What this project is

*Operation Tidebreak* is a short Blender animation of a fleet battle: realism first, faithful to the lore, in the style of *The Expanse*.
- **Ships:** the LREF fleet from JCB's *Wearing Power Armor to a Magic School*, with ship designs by Sir_Lazz.
- **Original brief:** `00_PROMPT.md`.
- **Input material:** `pack/` and `LREF_Storyboard_Pack.zip`.

The work has three parts:
1. **Doctrines (phase 1).** How each side fights, with worked numbers. Signed off.
2. **The film's storyboard (phase 2).** At revision 8. The reviews have met their stopping rule.
3. **A nine-episode pre-release mini-series** that counts down to the film. Episodes 1–8 are locked; episode 9 is in progress.

## 2. Where things stand

| Area | State |
|---|---|
| Doctrines | Signed off: `doctrine/LREF_doctrine.md`, `doctrine/Defence_doctrine.md`, `doctrine/working_numbers.md`. Reading edition in `doctrine/reading/`. |
| Film storyboard | **Revision 8:** 64 shots, 4:58 (298 s, 7,152 frames). Render estimate 111.9 h raw, 145.4 h with the 30 % allowance, against a 160 h gate (14.6 h spare). Builder checks are all clear. |
| Reviews | Five-lens rounds 1–5 are in `review/round1`–`round5`. Rounds 4 and 5 found no major issues, which meets the stopping rule. Cold reads by agents with no lore knowledge scored 7, 8, 7 and 7 out of 10 (`review/coldread/`). The dialogue and military-usage review (`review/dialogue/round1.md`, 18 fixes) is applied as revision 8. |
| Mini-series | Plan in `miniseries/SERIES_PLAN.md`; round 2 options in `miniseries/options/`; picks in `miniseries/PICKS.md`. Eps 1–8 are locked. Ep 9 has a draft, *Take Five*, and the user's notes for its rewrite (§6). |

## 3. Repo map

- `storyboard/tidebreak_data.py` is the single source for the film: shots, fleet, clocks, reviews and the revision line. `storyboard/build_storyboard.py` builds and checks it. It generates `index.html`, `shots.md`, `shots.csv` and `audience_script.md`, and updates `ASSET_REQUESTS.md`. Never edit the generated files by hand; patch the data, finding shots by title, and rebuild.
- `doctrine/` holds the two doctrines, the working numbers and `build_reading.py`, which builds the reading edition.
- `review/` holds every review report and synthesis, the cold reads and the dialogue review.
- `miniseries/` holds:
  - `SERIES_PLAN.md`: the plan, whose series rules were updated for round 2;
  - `PICKS.md`: the user's picks and the lore they supplied;
  - `options/BRIEF.md`: the rules every episode writer follows;
  - `options/README.md`: an at-a-glance table;
  - `options/ep1…ep9_*.md`: three options per episode;
  - `build_plan_page.py`, `build_options_page.py` and `build_picker.py`: the page builders;
  - `speech_check.py`: lists every spoken line with word and number counts, and flags lines repeated between options.
- `OPEN_QUESTIONS.md` holds the decisions made and the questions still open. `ASSET_REQUESTS.md` lists everything the Blender modelling session must build.

## 4. Building and checking

You need Python 3 with `pip install markdown-it-py beautifulsoup4`. Node is optional; the storyboard builder uses it to syntax-check the page script.

```
python3 storyboard/build_storyboard.py --fragment OUT.html --doc-base https://claude.ai/artifact/Fs71RuXXWxCKUkXpcNSYHe
python3 doctrine/build_reading.py --fragment OUT.html
python3 miniseries/build_plan_page.py --fragment OUT.html
python3 miniseries/build_options_page.py --fragment OUT.html
python3 miniseries/build_picker.py --fragment OUT.html
python3 miniseries/speech_check.py            # every episode, or name the files
```

The storyboard builder enforces these rules; it must end on "checks: all clear":
- Reading speed: at most 12 characters a second for lines plus HUD text per shot or `group`, and 15 on the title cards.
- Each speaker's first tag counts toward that.
- Cued lines must fit their windows, and `hold` keeps seconds clear at a shot's end.
- Sketches must not contain an apostrophe in a quote.
- Clocks must run continuously.
- The render budget must stay under the gate.

## 5. Published pages

These are claude.ai artifacts, private to the owner. To update one, read it first, then publish with its URL.

| Page | URL | State |
|---|---|---|
| Storyboard | https://claude.ai/artifact/DWowJbriJqam8wg2KQ9upa | v9 = revision 8 |
| Doctrines | https://claude.ai/artifact/Fs71RuXXWxCKUkXpcNSYHe | v7 |
| Mini-series plan | https://claude.ai/artifact/DsGL8ptk8CSGn6xSgsGev5 | v1, which predates round 2; republish once the plan is rewritten |
| Episode options picker | https://claude.ai/artifact/QV5uo9g4PYFW28NeEv7Drm | v5, with the `db` and `user` capabilities |

On the picker, the user chooses a base option per episode, taps cells to borrow or cut, and adds notes. Picks are saved in the `picks` collection, one document per episode (`ep1`–`ep9`), each with a plain-text `readable` field. Read them with ArtifactData `list` on that collection. If the page can't save, the user pastes the summary text instead.

## 6. Mini-series status

| Ep | Subject | Pick |
|---|---|---|
| 1 | M-1C railcannon | B · *Jink*, with shot 2's **picture** cut (about 50 s). Fold the cut in when the plan is rewritten. |
| 2 | Laser array | A · *Unseen* |
| 3 | Point defence | C · *Seeker* |
| 4 | Plasma lance | B · *Sinkex* |
| 5 | Frigate and tender | B · *Shift Change* |
| 6 | Warheads | A · *Family Resemblance*, from the product-advert takes the user asked for |
| 7 | ECW destroyer | B · *Who's Transmitting?*; shot 6's line is now EW: "Three now." |
| 8 | Heavy cruiser, spinal | C · *Bore Survey* |
| 9 | Endeavor, the finale | **Open.** A · *Take Five* is the current draft; B and C are kept for reference. |

**Ep 9: the user's latest notes, verbatim, not yet applied.** "flesh out her voicelines, dont say the stars above for each, if a not so important ships name is seen in the background dont say it. I want her basicaly talking throughout the whole thing, with short pauses after each cut where the name of a ship and stars above is said."

The rewrite brief was drafted, but the user stopped the session before it was applied. Rewrite Option A only, keeping B and C exactly:
- **Her takes.** She talks almost the whole time. Each take is a real 10–25 s attempt at a message home: home news, questions, a joke, avoidance. Each one falls apart for a human reason: she nearly says where she's going, gets emotional, says something she won't send, or runs on too long. Then she deletes it. She never states the mission, the destination or any danger.
- **The pauses.** After each delete comes a 2–3 s pause with one farewell on the departure net: "Stars above, <ship>." / "Always above, Delta." Only the important ships are named, in this order: Astrid, Canterbury, Extenuating, Nauvoo, Endeavor (last). Other ships can be seen leaving but are never named.
- **The ending.** The final take is the plain one ("Hi Mum. Did the tomatoes come up? Tell Dad he was right. Love you."), then SEND. Then "Stars above, Endeavor." / "Always above, Delta.", the ring spins up, and a hard cut goes to the finale tag (T−1 → T−0 → COLLATED FROM THE AFTER ACTION REPORT).
- **Keep:**
  - the faint, audio-only *Safe Travels* hold call under one take;
  - RALLYPOINT DELTA · DEPARTURE on screen once;
  - no warp blooms, which leaves the film's arrival order free.
- **Size.** About 130–180 words for her and about 30 for the ritual lines; 95–115 s including the tag.

**After Ep 9 is approved:**
1. Rewrite `SERIES_PLAN.md` from the final nine: the episode table, the episode sections pointing at the chosen options, the runtime and render totals, and Ep 1's cut.
2. Republish the plan page.

## 7. The user's standing preferences

- **Dialogue:**
  - military-correct and natural;
  - people talk to each other, never to the audience;
  - no lines that exist only to explain lore;
  - show, don't tell.
- **The film:**
  - five minutes at most;
  - the intro is one title card, OPERATION TIDEBREAK / COLLATED FROM THE AFTER ACTION REPORT;
  - no AI plot line (Charon Innovations went with it).
- **The mini-series:**
  - each episode in its own style;
  - options must be different events, not re-skins;
  - every shot is buildable from the film's 3D models, plus small additions and environments;
  - specs may appear on screen where the medium really shows them (Ep 6's adverts).
- **Lore the user supplied:**
  - Each departing ship's last words are "Stars above, <ship>." with the reply "Always above, <place>."
  - The departure station is **Rallypoint Delta** (a nod to Risk of Rain 2), spoken as "Delta".
  - Ep 9 carries one quiet nod to the UES *Safe Travels*.
- **Workflow:**
  - Use subagents, on a cheaper model, wherever they save usage, with self-contained briefs.
  - The user picks through the picker page.

## 8. Open questions for the user

- **From `OPEN_QUESTIONS.md`:**
  - **Q13:** may the smallest assets be proxies? This also decides how the tender appears in Ep 9.
  - **Q14:** the ECW destroyer's dish: text or art?
  - **Q15:** the modelling session's picks: the M-1C's wake style and the point-defence gun design.
  - **Q17:** the render fallback order if benchmarks come in high.
- **From the plan:**
  - the series title (recommended: *Spin-Up*);
  - names for the in-world makers (still [placeholders]);
  - whether Sir_Lazz's art may appear on screen;
  - cadence (two episodes a week, the finale on release day).

## 9. Notes for the next session

- **Git:**
  - Commit to this branch with the session's co-author trailers.
  - Don't open a PR unless asked.
  - The stop hook requires a clean, pushed tree.
- **Usage limits.** Ten agents in parallel hit the session limit. Run about three at a time. After a limit resets, an agent sometimes stalls with no activity; stop it and relaunch, or do a small job directly.
- **Subagent writes.** Subagents can't write to the scratchpad, so have them write in the repo and commit their work yourself.
- **Harmless messages:**
  - Artifact watch subscriptions always fail with `mint_failed`.
  - Google Fonts don't load in local headless Chromium.
- **Blocked site.** `riskofrain2.wiki.gg` is blocked by the network proxy.
