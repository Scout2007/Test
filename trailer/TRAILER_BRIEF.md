# Trailer brief

## 1. What it is

A trailer with **its own style**, independent of the nine mini-series episodes and distinct from each of them. It sells *Operation Tidebreak* (the film) and, if the user wants (QUESTIONS B4), opens the series.

The format comes from the user's references, studied in depth. The style is designed new, as the trailer's own style bible.

## 2. Sources it may draw on

- **The world.** The film's world, ships and 3D models: `storyboard/tidebreak_data.py`, the ASSETS list in `miniseries/options/BRIEF.md` §4, and the doctrines for what is physically right.
- **The user's lore:** the departure farewell "Stars above, <ship>." / "Always above, Delta.", Rallypoint Delta, and the rest of `miniseries/PICKS.md`.
- **The episodes.** Not a source. The trailer doesn't reuse their shots, styles or lines unless the user's answers say so. Agents read them only to stay distinct from them.

## 3. Defaults (until the user's answers override them)

- **Spoilers.** No spoilers of the film's outcome: Breakwater's fate, the losses, the surrender. Whether the enemy, the planet or the battle may be shown is the user's call (QUESTIONS B6). Until it's answered: no Maren, Breakwater, Compact, Skerry, Breakers or Anchor by name, and no film ship shown damaged.
- **Speech.** Natural speech only. No line exists to explain lore. A narrator, if the user wants one, speaks like a real trailer voice, sparingly.
- **3D.** The film's 3D models plus small additions and environments. New set or environment work only as far as the user's answer to E19 allows. 2D only as overlays and type. No rigged characters; people are voices.
- **The lore.** The film's look rules: invisible beams; lenses violet only while firing; blue only in the M-1C's bore pulse; heat only on radiator faces.

## 4. Stages and their deliverables

| Stage | Deliverable | Format |
|---|---|---|
| Research | `work/research/ref_NN.md` per reference; `work/research/synthesis.md` | `agents/01`, `agents/03` |
| Style bible | `work/style_bible.md` | `agents/05` |
| Treatments | `work/treatments/treatment_<X>.md`, then `treatment_merged.md` | `agents/06`, `agents/09` |
| Beat sheet | `work/beat_sheet.md` | `agents/10` |
| Storyboard | `work/storyboard.md` (shot by shot, framing and movement) | `agents/11` |
| Motion and timing | `work/motion_timing.md` (camera-move specs and the animatic timing sheet) | `agents/12` |
| Final | `trailer/TRAILER.md` | `agents/14` |
