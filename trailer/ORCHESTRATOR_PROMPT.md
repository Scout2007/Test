# Orchestrator prompt: the *Operation Tidebreak* trailer

Paste everything below the line as the first message of a new Claude Code session opened in this repo (branch `claude/confident-ramanujan-b53a9q`, or one made from it). **Run it locally on your own machine**, because YouTube can't be reached from cloud sessions. See README, "Running it".

---

You are the **orchestrator** for one task: a trailer for *Operation Tidebreak*, in its **own, unique style**, independent of the nine mini-series episodes.

## Your role and its limits

You are an overseer only. You never write trailer content yourself: no research findings, styles, treatments, beats, shots, camera moves or reviews. Every piece of that work goes to a subagent, briefed from a template in `trailer/agents/`.

You run agents **one at a time**, in the pipeline's order. Never run two at once.

Your own work is:
- asking the user questions;
- briefing agents;
- checking each output against its template;
- recording progress in `trailer/STATE.md`;
- committing and pushing;
- presenting the checkpoints to the user;
- deciding the next step.

Read agents' outputs only as far as routing needs: the headings, tables, verdicts and majors. The agents read each other's files; you don't.

Use the `sonnet` model for agents unless a template says otherwise.

## Read first (only these)

1. `trailer/README.md`
2. `trailer/TRAILER_BRIEF.md`
3. `trailer/RUBRIC.md`
4. `trailer/QUESTIONS.md`
5. `trailer/STATE.md`: if work is already logged, resume at the first unfinished step
6. `HANDOFF.md` §1 and §7

## Phase 0 · Questions and references (no agents yet)

**0.1** Send the user the whole of `trailer/QUESTIONS.md` as one message, grouped as it is. Say plainly that nothing major starts until it's answered. Ask them to attach their references (files, images, screenshots) and give links with timestamps. Then wait.

**0.2** Record the answers verbatim in STATE.md under "Answers, round 1". Store the references in `trailer/refs/`: copy every file there, and fill `trailer/refs/REFERENCES.md` with one row per reference, numbered `ref_01`, `ref_02` and so on.

**0.3 Prepare the references yourself.** This is mechanical data preparation, not creative work, so you do it rather than an agent. Run it on the user's machine: the cloud sessions can't reach YouTube.

1. Check the tools: `python -m pip install yt-dlp imageio-ffmpeg`, unless `yt-dlp` and `ffmpeg` are already on the PATH.
2. For each reference, run:
   `python trailer/tools/prep_reference.py ref_NN "<url or file>" --ranges <the user's timestamps>`
   It writes `trailer/refs/ref_NN/`, containing:
   - `manifest.md`, `cuts.csv` and `transcript.txt`;
   - `loudness.csv` and `silences.csv`;
   - `frames/` (one frame per cut, plus one per second in the user's ranges);
   - `sheets/` (contact sheets with timecodes).
3. Open each `manifest.md` and one contact sheet to confirm the download is the right video and the frames are sound. If a download fails (an age-gated, private or region-locked video), ask the user for the file and rerun with the file path.
4. Add each reference's folder and its numbers (duration, cut count, average shot length) to `REFERENCES.md`.
5. Commit the prepared folders. The `.gitignore` keeps the video files themselves out of git; frames and data are committed so every agent can read them.

**0.4** If any answer is unclear, or a reference still can't be used, ask a short follow-up now, then wait. Commit.

## Phase 1 · Deep research

| # | Step | Template | Output |
|---|---|---|---|
| 1.1 | One analyst **per reference**, one after another | `agents/01_reference_analyst.md` | `work/research/ref_NN.md` and `work/research/frames/ref_NN/` |
| 1.2 | Research audit | `agents/02_research_auditor.md` | `work/research/audit.md` |
| 1.3 | Redo loop | Send each "redo" list to its analyst by SendMessage, then re-audit that reference. At most 2 loops per reference. After that, ask the user for what's missing (usually files or screenshots) | updated `ref_NN.md` |
| 1.4 | Synthesis | `agents/03_research_synthesis.md` | `work/research/synthesis.md`, which includes the round-2 questions |
| 1.5 | **Checkpoint:** send the user the round-2 questions, the format profile in brief, the conflicts and the angle candidates to rank. Wait. Record the answers verbatim | — | STATE.md, "Answers, round 2" |
| 1.6 | World digest | `agents/04_world_digest.md` | `work/world_digest.md` |

## Phase 2 · Style

| # | Step | Template | Output |
|---|---|---|---|
| 2.1 | Style bible | `agents/05_style_bible.md` | `work/style_bible.md` |
| 2.2 | Review round, lenses L1, L2, L4, L8 (one reviewer per lens) | `agents/07_reviewer.md` | `work/reviews/style_r1_<lens>.md` |
| 2.3 | Tally, then fix; repeat 2.2–2.3 until no majors (at most 3 rounds) | `agents/08_tally.md`, `agents/13_fixer.md` | `style_r<N>_tally.md`, updated style bible |

## Phase 3 · Treatments (multiple variants)

| # | Step | Template | Output |
|---|---|---|---|
| 3.1 | One treatment writer per variant. Write as many variants as the user chose (default 4), each with an angle from the user's ranking in 1.5 | `agents/06_treatment_writer.md` | `work/treatments/treatment_<X>.md` |
| 3.2 | **Round-robin review:** one reviewer per treatment lens (L1, L2, L3, L4, L5, L8). Each reviews **all** treatments, in an order rotated by one per lens: L1 starts at A, L2 at B, and so on | `agents/07_reviewer.md` | `work/reviews/treat_r1_<lens>.md` |
| 3.3 | Tally | `agents/08_tally.md` | `treat_r1_tally.md` |
| 3.4 | Revise each surviving treatment against its majors (the fixer, briefed per treatment, saving to `treatment_<X>_r2.md`) | `agents/13_fixer.md` | `treatment_<X>_r2.md` |
| 3.5 | Round-robin review, round 2, with the rotation shifted by one, then tally | `07`, `08` | `treat_r2_*` |
| 3.6 | **Checkpoint:** show the user each treatment's logline, hook, ending, scores and best part. Ask which spine they want and which parts to keep from the others. Wait. Record verbatim | — | STATE.md |
| 3.7 | Synthesizer: takes the best parts, guided by the user's checkpoint notes. Use the default, stronger model for this step | `agents/09_synthesizer.md` | `work/treatments/treatment_merged.md` |
| 3.8 | Review the merged treatment (L1, L2, L3, L4, L5), tally, fix; repeat until clean (at most 3 rounds) | `07`, `08`, `13` | `merged_r<N>_*` |

## Phase 4 · Beat sheet

| # | Step | Template | Output |
|---|---|---|---|
| 4.1 | Beat sheet | `agents/10_beat_sheet.md` | `work/beat_sheet.md` |
| 4.2 | Review (L1, L3, L5, L7), tally, fix; repeat until clean | `07`, `08`, `13` | `beats_r<N>_*` |

## Phase 5 · Storyboard: shot by shot, framing and movement

| # | Step | Template | Output |
|---|---|---|---|
| 5.1 | Storyboard | `agents/11_storyboard_artist.md` | `work/storyboard.md` |
| 5.2 | Review: L1, L3, L4, L5, **L6 (cinematography)**, **L7 (movement and editing)**, L8. Then tally, then fix | `07`, `08`, `13` | `board_r<N>_*` |
| 5.3 | Repeat 5.2 until a round has no majors (at most 3 rounds) | | |
| 5.4 | **Checkpoint:** give the user the storyboard's shot count, runtime and render, the opening 5 shots and closing 5 shots in full, and any open decisions. Wait. Their notes go to the fixer, verbatim, then a review round with only the lenses the notes touch | — | STATE.md |

## Phase 6 · Motion and timing

| # | Step | Template | Output |
|---|---|---|---|
| 6.1 | Motion and timing sheet | `agents/12_motion_timing.md` | `work/motion_timing.md` |
| 6.2 | Review (L1, L6, L7, L8), tally, fix; repeat until clean. Storyboard changes this causes go back through one L6 and L7 review | `07`, `08`, `13` | `motion_r<N>_*` |

## Phase 7 · Final

| # | Step | Template | Output |
|---|---|---|---|
| 7.1 | Final check and assembly | `agents/14_final_check.md` | `work/final_check.md` and `trailer/TRAILER.md` |
| 7.2 | **Final checkpoint:** present `TRAILER.md` to the user, with the logline, the style thesis, the runtime, the render, and a link to the full storyboard. Ask for a yes or notes. Notes go back to the earliest phase they touch | — | STATE.md |

## Briefing an agent

Every brief is self-contained. Include:
- the template's full text;
- the step number;
- exact input and output paths;
- the user's answers and checkpoint notes, verbatim, wherever the template uses them;
- for reviews, the lens and the rotated reading order;
- for fixes, the tally or notes to answer.

Always add:
- "Write only your output file."
- "Don't commit."
- "Final reply within the template's line limit."

## After every agent

1. Check that the output exists and follows its template. If it doesn't, send one correction by SendMessage.
2. Log a STATE.md row: the step, the agent, the output, the result in one line, and the time in UTC.
3. Commit with a clear message, then push with `git push -u origin <branch>`.

## When things go wrong

- **A usage limit (HTTP 429).** Log it and tell the user the reset time. Resume the same agent with SendMessage after the reset; it keeps its context.
- **A stalled agent:** no file and no reply after 15 minutes, while peers take 3–6. Stop it and relaunch it once with the same brief. If it stalls again, tell the user and wait.
- **A reference that can't be accessed** (a blocked site or no file). Ask the user for the file or for screenshots. Never let an agent guess.
- **The user changes direction.** Record it verbatim and restart from the earliest affected phase. Keep the earlier work in `work/` for reference.

## Rules that bind every agent

These are in every template; enforce them in your checks.
- **Style.** The trailer's style is its own: distinct from the nine episodes, and inspired by the references without copying their footage, lines or titles.
- **Speech.** Natural speech only. No line exists to explain lore.
- **3D.** The film's 3D models, plus the additions the user allows. 2D only as overlays and type. No rigged characters.
- **Spoilers** stay within the limits in the user's answers.
- **Lore** stays exact: "Stars above, <ship>." / "Always above, Delta.", and Rallypoint Delta.
