# Trailer brief

## 1. What it is

A trailer that **opens** the pre-release mini-series. It is the first thing published, before Ep 1 (T−9), and it promises nine short in-world films counting down to *Operation Tidebreak*. Its tag counter rolls from T−11 to T−10, one step before Ep 1's.

## 2. What it must do

- **Promise the series.** Nine different films in nine different styles, each about one weapon or ship, and a countdown that ends in the film.
- **Build from the episodes.** Its pictures come from the nine locked episodes (`miniseries/PICKS.md`; the shots are in `miniseries/options/epN_*.md` under the picked letter) and from the film's own 3D assets. New shots are allowed if they use the same assets plus small additions.
- **Have a spine.** It must not be just a montage. The format comes from the user's references (`work/format_profile.md`); within that format the trailer needs a through-line, such as the countdown, a voice, or a recurring image.
- **End on the film.** The last frame is the series tag style: a hard cut to OPERATION TIDEBREAK on the still stars, and the counter.

## 3. What it must not do

- **Spoil the film.** Don't use or name Maren, Breakwater, the Compact, Skerry, the Breakers or Anchor. Nothing from the dropped AI plot line. No film ship shown damaged. Systems appear in tests, drills, ceremonies and daily work, never in battle.
- **Explain lore.** No line may exist to inform the viewer. Use voice only where the format has voice, and make it sound like a real trailer (taglines, a few words) or like overheard real people.
- **Leave the 3D models.** No drawn animation, no stock or live action, no rigged characters. People are voices only.
- **Contradict the episodes.** Lines lifted from an episode stay exactly as written there.

## 4. Default format (only if the user gives no references)

- **Length.** 60–90 s, including the 5 s tag.
- **Structure.** A cold open, then three acts that rise in pace, with the cuts quickening:
  1. a quiet open on one image (the Endeavor, or the M-1C's blue pulse);
  2. a run through the nine styles, a beat each, with a short title card per style (TEST FOOTAGE · ADVERT · TRAINING FILM …);
  3. the countdown T−9 … T−1 flashing over the fastest cuts, then silence, and the tag.
- **Sound.** Diegetic sound from each episode's source, with one score cue under the whole.
- **Words.** At most about 25 spoken, all lifted from the episodes.

## 5. Sizes and budget

- **Runtime.** As the references set it, within 45–150 s.
- **Render.** Reuse the episodes' shots wherever possible. New renders should total no more than about 8 h raw, at the film's classes (A 45, A2 90, B 75, C 200, D 15, E 2 s/frame at 24 fps).
- **Spoken words.** State the count. Lines lifted from episodes count, and keep their wording.

## 6. Output format for every trailer file

```
# Trailer · <title> (<runtime> s) — variant <X>
**Logline.** One sentence.
**Spine.** What holds it together, in one sentence.
**Format match.** Which references and which format_profile items it follows, and where it departs and why.
**Storyboard.** | # | s | Picture | Sound and words | Source |   (Source: "Ep N shot k", "film asset", or "new")
**Text cards.** Every card's exact text and timing.
**Words.** N spoken; the lines lifted from episodes, marked.
**New renders.** Each new shot: its class and hours. Total.
**Risks.** Spoilers, lore, assets, timing.
```
