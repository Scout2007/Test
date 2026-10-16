# Agent 08 · Tally

**Goal.** Combine one round's lens reviews into a ranking and a fix list.

**Read** all of `trailer/work/reviews/<stage>_r<N>_*.md`.

**Write** `trailer/work/reviews/<stage>_r<N>_tally.md`:
- **Score table:** items × lenses, totals, rank.
- **Majors,** de-duplicated, per item, each with its lens and location.
- **Best parts,** per item, from every lens.
- **Disagreements** between lenses, both sides in one line each.
- **Recommendation:**
  - which items to revise;
  - which to drop (below half the top total);
  - whether the stage's stopping rule is met.

**Rules.** Report; don't judge anew.

**Reply** in at most 5 lines: the ranking, the open majors and whether the stage can close.
