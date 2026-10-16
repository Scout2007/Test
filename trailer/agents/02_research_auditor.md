# Agent 02 · Research auditor

**Goal.** Make sure every reference analysis is deep and evidence-backed before anything is built on it.

**Read** all of `trailer/work/research/ref_*.md`, their frame folders, and `trailer/refs/REFERENCES.md`.

**Check each analysis against this list.** Each item scores pass, thin or missing.

| Check | Pass means |
|---|---|
| Access | It says exactly what was seen (files, frames, transcript) and what wasn't |
| Evidence | Every claim cites a timestamp, frame or line, and inferences are labelled |
| Structure | Acts or sections with timecodes; hook, turn and button identified |
| Shot list | Covers the whole reference, or every timestamp range the user gave; all columns filled, framing and movement included |
| Transitions | Every cut in the user's ranges has a named device, an out- and in-frame relation backed by the strips and transitions.csv, a sound bridge and a beat offset |
| Rhythm | Shot-length stats per section, and the acceleration described |
| Sound | Music structure mapped to timecodes; sync with cuts described |
| Type | Every card transcribed, with style and timing |
| Transfer | Borrowable techniques separated from content, and translated to 3D-only means |
| User's notes | Each thing the user said they like is addressed |

**Spot-check accuracy, not just depth.** For each reference, choose 10 claims at random. Use Python's `random` with seed = the reference number, so the choice can be repeated. Draw them from the shot list, the transitions table, the rhythm figures and the sound map. Verify each one against the evidence:
- the frames and strips;
- `cuts.csv`, `transitions.csv`, `beats.csv` and `music_sections.csv`;
- the transcript.

Score each claim **correct**, **wrong** or **unverifiable**. A reference with 2 or more wrong claims, or 4 or more unverifiable, fails, whatever its depth. Treat motion numbers flagged `low_texture` as unverifiable rather than wrong.

**Write** `trailer/work/research/audit.md`:
- the checklist table per reference;
- the spot-check table per reference: each claim, the evidence checked, and the verdict;
- a **verdict** per reference: accept, or redo with a numbered list of exactly what is missing;
- a short list of **cross-reference gaps**: things no reference covers that the trailer will need, such as the ending style.

**Reply** in at most 6 lines: the verdict per reference and the count of items to redo.

The orchestrator sends each "redo" back to the analyst that wrote it, by SendMessage with your numbered list. After the redo, run this audit again on that reference only.
