# Agent 12 · Motion and timing (the animatic sheet)

**Goal.** Make every camera move and cut buildable and checkable: exact keyframes, plus a timing sheet an editor can cut an animatic from.

**Read.**
- `work/storyboard.md`
- `style_bible.md`
- `synthesis.md` (rhythm)
- `world_digest.md` (physics: distances, speeds, light lag)

**Write** `trailer/work/motion_timing.md`:
1. **Camera-move specs, per moving shot.**
   - the start and end keyframes: position relative to the subject (metres or km), rotation (degrees) and focal length;
   - the easing curve (Bézier handles described, or a named preset);
   - the speed at peak;
   - any shake or drift (amplitude and frequency) with its in-world cause;
   - focus distances and rack timing.
   - Flag any move whose speed or path is physically impossible for its camera body.
2. **Subject-motion specs.** Ship moves, effects timing and the light changes that cuts depend on.
3. **Animatic timing sheet.** One row per shot: frame in, frame out, duration, the cut's sync to the music map (beat or bar), and the cards.
4. **Rhythm check.** Shot lengths per act against the profile targets, and the cut density curve against the reference's.
5. **Mismatches** with the storyboard, and proposed fixes. Don't silently change the storyboard.

**Reply** in at most 5 lines: the moves specified, any physics flags, and the rhythm deviation per act.
