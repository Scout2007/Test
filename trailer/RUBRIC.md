# Review rubric

Reviews come in rounds. Lenses L6, L7 and L9 run on the stronger model by default (see ORCHESTRATOR_PROMPT, model policy). Each round runs a set of lenses, and each lens is a separate reviewer agent who reviews **every** item under review, in a rotated order. Each criterion is scored 1–5, then the reviewer lists majors, minors and the best part.

## Lenses

| # | Lens | Criteria (score each 1–5) | A major is… |
|---|---|---|---|
| L1 | Reference fidelity | Length, structure, rhythm, devices and sound match what the research found and what the user marked essential | It ignores an essential reference or a user answer |
| L2 | Distinctness | Its own style, distinct from all nine episodes and from the references themselves (inspired by them, never copied) | It reads as one of the episodes' styles, or copies a reference's shots, lines or titles |
| L3 | Story and hook | Spine, a hook in the first 5 s, the build, the turn, the payoff, rewatch value | A plain montage with no spine, or no hook |
| L4 | Lore and spoilers | Faithful to the world, its physics and look rules, and the user's spoiler answers | A spoiler beyond the user's limit, or a breach of physics or lore |
| L5 | Speech and text | Natural lines, real trailer copy, no exposition, type that works at speed | A line that exists to explain lore |
| L6 | Cinematography | Each shot's size, lens, angle, composition and lighting serve its beat; variety; scale; screen direction | A shot that can't read (scale, axis or exposure), or a broken screen direction or axis |
| L7 | Movement and editing | Camera moves are motivated and physically plausible for their camera (hull-mounted, drone, long lens), with eases, speeds and holds; cuts land on rhythm; transitions | A move with no motivation or with impossible physics, or cut rhythm far from the format profile |
| L8 | Production | Built from the film's assets plus allowed additions; render hours within budget; feasible in Blender | It needs a new hero model or rigged character, or goes over budget |
| L9 | Transitions | Every cut is designed. The outgoing and incoming frames relate by position, shape, motion direction and speed, light and colour, or by a deliberate clash. The sound bridges (J- and L-cuts, hits, silences) are specified. The transition type suits the beat. Within each act the transitions vary without becoming a showcase. On the previews, the measured motion and luma across each cut match the design | A cut with no designed relation, an unintended jump (axis, direction, scale, brightness) that reads as an error, a transition that contradicts its beat, or a preview cut that doesn't do what the storyboard says |

## Which lenses run at each stage

| Stage | Lenses |
|---|---|
| Research audit | (agent 02's checklist, not lenses) |
| Style bible | L1, L2, L4, L8 |
| Treatments (rounds 1 and 2) | L1, L2, L3, L4, L5, L8 |
| Merged treatment | L1, L2, L3, L4, L5 |
| Beat sheet | L1, L3, L5, L7, L9 (for the transition intent between beats) |
| Storyboard (rounds until clean) | L1, L3, L4, L5, L6, L7, L8, **L9** |
| Motion and timing | L1, L6, L7, L8, **L9** |
| P1 style frames, P2 key images | L1, L2, L6 |
| P3 boards | L6, **L9** |
| P4 animatic | L1 (rhythm against the references), L7, **L9** |
| P5 block-out | L6, L7, L8, **L9** |

## Findings format

```
## <Item>
| Criterion | Score | Why (one line) |
**Majors.** Numbered; each with its location (shot or beat #), the problem and a concrete fix.
**Minors.** The same, briefer.
**Best part.** The single thing most worth keeping, and why.
```

## Stopping rule

A stage is done when a review round finds no majors in any lens, or after 3 rounds. After 3 rounds, report what's left to the user, who decides.
