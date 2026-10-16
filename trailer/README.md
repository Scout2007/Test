# Trailer package: an orchestrated pipeline

This package makes a trailer for *Operation Tidebreak*, **in its own style**, independent of the mini-series episodes. One orchestrator session oversees the work: it asks the questions, delegates every task to agents one at a time, and stops at checkpoints for the user.

## How to start

1. Open a new Claude Code session in this repo.
2. Paste the part of `ORCHESTRATOR_PROMPT.md` below its line.
3. The orchestrator sends you the questionnaire (`QUESTIONS.md`) and asks for your references. Have them ready:
   - **Video files are best.** The agents extract and study the frames, the cut points and the audio structure.
   - **Links** need timestamps of the moments you mean. Some sites can't be fetched, so attach the files or screenshots if you can.
   - **Images and stills.** Say what you like about each.

## Pipeline

```
Phase 0  questionnaire + references  ──▶ you answer
Phase 1  one deep analyst per reference ─▶ research audit (redo loop) ─▶ synthesis
         ──▶ CHECKPOINT: round-2 questions, format profile, angles to rank ─▶ world digest
Phase 2  style bible ─▶ review (L1 L2 L4 L8) ─▶ tally ─▶ fix, until clean
Phase 3  treatment variants (default 4) ─▶ round-robin review (6 lenses, rotated) ─▶ tally
         ─▶ revise ─▶ round-robin review 2 ─▶ CHECKPOINT: choose a spine and parts
         ─▶ synthesizer takes the best parts ─▶ review, until clean
Phase 4  beat sheet ─▶ review (L1 L3 L5 L7), until clean
Phase 5  storyboard, shot by shot (framing, lens, composition, movement, transitions)
         ─▶ review (L1 L3 L4 L5 L6 L7 L8), until clean ─▶ CHECKPOINT
Phase 6  motion and timing (camera keyframes, easing, the animatic timing sheet)
         ─▶ review (L1 L6 L7 L8), until clean
Phase 7  final check ─▶ TRAILER.md ─▶ FINAL CHECKPOINT
```

The eight review lenses (`RUBRIC.md`) are:
- **L1:** reference fidelity
- **L2:** distinctness
- **L3:** story and hook
- **L4:** lore and spoilers
- **L5:** speech and text
- **L6:** cinematography
- **L7:** movement and editing
- **L8:** production

## Files

| File | Purpose |
|---|---|
| `ORCHESTRATOR_PROMPT.md` | The prompt to paste |
| `QUESTIONS.md` | The round-1 questionnaire, asked before any work |
| `TRAILER_BRIEF.md` | What the trailer is, its defaults, and each stage's deliverable |
| `RUBRIC.md` | The eight lenses, which run at each stage, the findings format and the stopping rule |
| `STATE.md` | The orchestrator's log and the user's answers, verbatim; it lets a session resume |
| `agents/01–14_*.md` | The agent templates: reference analyst, research auditor, research synthesis, world digest, style bible, treatment writer, reviewer, tally, synthesizer, beat sheet, storyboard artist, motion and timing, fixer, final check |
| `refs/` | Your references (`REFERENCES.md`, plus files) |
| `work/` | All agent outputs: `research/`, `treatments/`, `reviews/`, the style bible, beat sheet, storyboard and motion sheet |
| `TRAILER.md` | The finished trailer package (written at phase 7) |

## Cost and pace

The pipeline is long by design, roughly 60–90 agent runs. With 3 references, 4 treatments and two review rounds per stage, it comes to:
- research: about 6–10 runs;
- style: about 6–10;
- treatments: about 25;
- beats: about 6;
- storyboard: about 10–20;
- motion: about 6–10;
- final: 1.

Every run is linear, so a usage limit pauses one agent, and STATE.md lets the orchestrator resume. Agents run on a cheaper model, except the synthesizer.
