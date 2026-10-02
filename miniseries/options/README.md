# Style options, round 2: the picks at a glance

Round 1 was rejected for three reasons: lore-dumping dialogue, three options that rehashed each other, and work beyond the film's 3D models. Round 2 follows a new brief (`BRIEF.md`):
- **Speech:** only what a real person would say, with picture and sound carrying the idea.
- **Events:** each option is a different event with one idea.
- **Production:** every shot is a render of the film's assets plus small additions and environments.

Every spoken line was checked by script: word counts, spoken numbers, and lines repeated between options.

## At a glance

The user's picks are in `../PICKS.md`. Eps 1–5 and 7 are locked; Eps 6, 8 and 9 have new options to choose from.

Each cell gives the title, what happens, spoken words · runtime · render hours (raw, ±30 %).

| Ep | Subject | A | B | C | Agent's pick |
|---|---|---|---|---|---|
| 1 | M-1C railcannon | *Run 4*: a factory shot at a plate 100 km out on locked range cameras; four seconds of nothing, then the hit · 26 w · 60 s · ~7.8 h | *Jink*: live fire at a drone that sidesteps until it's too close to dodge; the gun crew's loop · 30 w · 60 s · ~6.8 h | *Eight Milliseconds*: one shot in high-speed playback, the blue pulse crawling down the bore · 0 w · 50 s · ~6.4 h | **A** |
| 2 | Laser array | *Unseen*: a luxury brand film; a far drone's radiator dims to black, no beam ever · 7 w · 41 s · ~6 h | *Graveyard Shift*: two night-shift techs ping a reflector satellite while arguing about a mug · 30 w · 46 s · ~4 h | *Tag*: two cruisers play laser tag among rocks; an umpire reads the hit lights · 32 w · 46 s · ~6 h | **B** |
| 3 | Point defence | *Six Layers*: a vintage training film; each layer strikes a dot off a chalk counter; four dry narrator lines · 28 w · 65 s · ~8 h | *The Leaker*: a chief scrubs the replay of the one round that reached 8 km until someone owns up · 31 w · 55 s · ~6 h | *Seeker*: a target missile's own feed from lock to cut · 0 w · 42 s · ~3 h | **B** |
| 4 | Plasma lance | *Field Reach*: a clay-and-line publication plate; the field sleeve builds and a point of light is released · 0 w · 45 s · ~4.9 h | *Sinkex*: a retired frigate hull is cut in two while a veteran remembers the coat he slept in aboard her · 49 w · 60 s · ~10 h | *The Edge*: one chase shot beside a single pulse until it frays and goes out; "Lost." · 1 w · 43 s · ~9.5 h | **C** |
| 5 | Frigate and tender | *The Multitool*: a late-night infomercial; "in seconds!" over a caption reading ACTUAL TIME: 6 HOURS · 65 w · 50 s · ~7.2 h | *Shift Change*: a time-lapse module swap on the tender's arm camera, with a night crew heard in radio fragments · 13 w · 55 s · ~3.5 h | *Sisters*: three frigates with three modules tease each other, then part for three jobs · 34 w · 55 s · ~11.9 h | **A** |
| 6 | Warheads (rewritten to the user's note: a product advert with specs) | *Family Resemblance*: a range-launch line-up, every missile on its plinth with a spec card · 27 w · 61 s · ~7.6 h | *Build Your Salvo*: an online configurator, a flight preview for each pick · 11 w · 58 s · ~4.4 h | *Contactless*: a catalogue spin, one page per missile · 0 w · 52 s · ~2.9 h | — |
| 7 | ECW destroyer | *Quiet Hours*: a go-dark drill; a search plume crawls past and the bridge whispers out of habit · 16 w · 50 s · ~2.2 h | *Who's Transmitting?*: the EW picture catches a frigate's galley radio playing the match · 18 w · 55 s · ~2.5 h | *Shepherd*: drones come home after a long sortie; the last one is talked in · 9 w · 70 s · ~5.1 h | **B** |
| 8 | Heavy cruiser, spinal (B kept; A and C new) | *Clear of the Glass*: the Astrid undocks after refit, watched from the yard gallery by the families who built her · 39 w · 60 s · ~6.6 h | *Pass in Review*: kept as written · 13 w · 50 s · ~3.1 h | *Bore Survey*: an inspection crawler drives the kilometre of the spinal's bore to daylight · 20 w · 56 s · ~4.1 h | — |
| 9 | Endeavor, finale (A is the user's B+C merge) | *Delivered*: traffic control clears all fourteen ships out while her message home plays over it · 60 w · 88 s · ~6 h | *Cleared to Depart*: as before · 37 w · 60 s · ~7 h | *Voice Note*: as before · 14 w · 55 s · ~5 h | — |

Taking every agent's pick comes to 7:43 and ~50 h raw, against round 1's 9:30 and ~48 h.

## Decisions that come with some options

- **Ep 2 C:** the duel needs two Endeavor hulls in different liveries.
- **Ep 4 C:** whether the drone feed keeps its range counter.
- **Ep 8 A:** shows a two-minute turn and a ~2 min 48 s flight to 10,000 km.
- **Ep 8 C:** implies about half a minute of fin time per shot.
- **Ep 8, A and C:** both make their numbers canon.
- **Ep 9:** the film defines only the warp *arrival* flash, so the departure's look is yours to set. A and B show a bloom; C cuts to the tag before it.
- **Ep 7 A:** needs the destroyer rig to pose its fins edge-on.
- **Placeholders:** makers, callsigns and hull numbers stay in [brackets] until you name them.

## How to pick

Use the picker: the published options page, built by `miniseries/build_picker.py` into `miniseries/picker.html`.

1. For each episode, choose a **base**: the option whose event you want to make.
2. Tap a **picture** or a **sound and words** cell, or a **look** note, in another option to borrow it. Tap one in your base to cut it.
3. Add a **note** for anything the taps can't say.

The page keeps a live estimate of runtime and spoken words. Picks save to the page as you go; tell Claude "picks are in".

Claude then reads them and briefs one writer per episode with:
- the base;
- the borrowed and cut pieces;
- your note;
- this brief.

Each merged episode comes back as a single storyboard for a final yes or no.
