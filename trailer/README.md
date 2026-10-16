# Trailer package: an orchestrated pipeline

This package makes a trailer that opens the *Operation Tidebreak* mini-series. One **orchestrator** session oversees the work and only delegates, running one agent at a time.

## How to start

1. Open a new Claude Code session in this repo.
2. Paste the part of `ORCHESTRATOR_PROMPT.md` below its line.
3. The orchestrator first asks you for references to the trailer format you want: links (with timestamps), images, videos and screenshots. Have them ready. Agents can't watch video, so screenshots of key moments plus a line on what you like about each help most.

## Pipeline

```
0  references from you ─▶ 1 reference analyst ─▶ 2 project digest
   ─▶ 3 four variants (A countdown · B one voice · C the styles · D wild card), written one after another
   ─▶ 4 round-robin review: 5 lenses, each reviewing every variant in a rotated order
   ─▶ 5 tally ─▶ 6 revise each variant ─▶ 7 round-robin review, round 2
   ─▶ 8 synthesizer takes the best parts ─▶ 9/10 review and fix, until no majors (at most 3 rounds)
   ─▶ 11 final check ─▶ 12 shown to you for a yes or notes
```

The five review lenses are:
1. format fidelity;
2. story and hook;
3. lore, spoilers and continuity;
4. speech and text;
5. production.

## Files

| File | Purpose |
|---|---|
| `ORCHESTRATOR_PROMPT.md` | The prompt to paste |
| `TRAILER_BRIEF.md` | What the trailer must and mustn't do, the default format and the output format |
| `RUBRIC.md` | The five lenses, scores, what counts as a major, and the stopping rule |
| `STATE.md` | The orchestrator's log; it lets a session resume after a usage limit or restart |
| `agents/01–09_*.md` | One brief template per agent role |
| `refs/` | Your references (`REFERENCES.md`, plus images and screenshots) |
| `work/` | Agents' outputs: `format_profile.md`, `context_digest.md`, `variants/`, `reviews/`, `trailer_merged.md`, `final_check.md` |
| `TRAILER.md` | The finished trailer (written at step 11) |

## Context the agents use

- `HANDOFF.md`
- `miniseries/PICKS.md`
- `miniseries/options/` (BRIEF.md and the nine episodes' picked options)
- `miniseries/SERIES_PLAN.md`
- `miniseries/speech_check.py`

Ep 9 is still in revision (see HANDOFF §6), so the trailer should use Ep 9 shots that survive any version: the departure, the farewells and the Endeavor last. It should not rely on her takes' exact wording.

## Cost notes

- Agents run on a cheaper model, except the synthesizer.
- Runs are linear, so a usage limit pauses one agent rather than many.
- A full run is about 27 agent runs if both review rounds and two fix rounds happen: 1 + 1 + 4 + 5 + 1 + 4 + 5 + 1 + 5 × 2 + 2 + 1.
