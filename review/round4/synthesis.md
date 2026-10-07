# Round 4 synthesis

Round 4 read **storyboard revision 4** (61 shots, 4:08) with the same five reviewers. **No reviewer raised a major issue**, down from 2 in round 3, 7 in round 2 and 26 in round 1. That meets the brief's stopping rule: at least two rounds, and none of the five with a major realism issue left.

Three reviewers were stopped by a session limit and resumed. Doctrine and production finished on a frozen copy of revision 4 (commit 9eb9a5f), because revision 5 work had already begun in the main tree.

**Revision 5** applies every round 4 minor and nit below. It also carries three things the user asked for after reading revision 4:
- **The eclipse (Q16).** The user's words: "The alt sounds fire."
- **A text prologue** on the stars.
- **A rewritten script** that carries the story on its own, tested by an agent with no knowledge of the lore (`review/coldread/`).

Because revision 5 changes lighting across ~15 shots and every line of dialogue, round 5 reads it with the same five lenses.

Shot numbers below are revision 4's. Revision 5 adds three prologue cards at the front and a new plot insert, *Sixty-four*, after *The anvil*, so numbers from shot 1 on shift by three, and from *Umbrella* on by four.

## The verdicts

- **Physics:** no major issues. The ring salvo needs 12.68 km/s, and both waves close at 48.6° and 49.0°. The spinal numbers match the reviewer's own integration. Left: the boost in "one profile", the odds as a floor, Skerry's phase, and a thin margin in Anchor's lee.
- **Doctrine:** no major issues. The round 3 major is fixed at the root. Left: the spend wave's payload, decoys that must match through the boost, the clouds aimed at the rock rather than the pack, and the backup for the waves' guidance.
- **Lore:** no major issues. The M-1C run plays the user's gun step for step, the hero missile fits the pods, and the drones die to the guns the posts give that job. Left: where the decoys ride, and two nits.
- **Cinematography:** no major issues. The volley-and-answer order (45 → 46 → 47) is the stronger cut. Left: cued lines that outrun their windows, the run-in's even tempo, and the heat readout's gap.
- **Production:** no major issues. The estimate is 155 h, 5 h under the gate. Left: the gate can't hold the benchmarks that feed it, the levers have no measured size and no last step, and two nits.

## Minor issues and nits

All applied, except where marked.

- **Physics.**
  - **"One profile" means the killers' 30 g boost**, the multi-packs throttling down to match. Now in O3, PHASES and KEY_NUMBERS.
  - **The kill wave's odds are a floor:** "at least ~33 of the ~40". The waves share the lasers, Site 1 is dazzled, and the spend wave has stripped the facing side.
  - **Skerry is a thin crescent on a dark disc** in *Birds away* and *Skerry burns*.
  - **Anchor's lee.** The Endeavor now sits on the bisector of the two shadows, ~4 km inside each (map C draws both), and holds that spot through the lee shots.
- **Doctrine.**
  - **The spend wave's payload.** It is mostly decoy, EW and kill-cloud birds, with a few dozen warheads fused to burst 1–3 km out. They strip the facing side's sensors, radiators and point defence, and leave the hull whole (PHASES, KEY_NUMBERS, *The spend wave*). The kill wave then meets a thinner wall.
  - **Decoys through the boost.** MSL-V's decoy carries a motor sized to match a killer's plume and acceleration. O3 now reads "by launch, boost, speed or signature", and the net ship steers the whole wave.
  - **Skerry's clouds are steered onto the pack's slot** in their last hour (~40 m/s of the divert kits). The pack, having watched the burns, slides 20 km down the shadow before it fires (*The pack fires*).
  - **The waves' backup guidance is on screen:** the new insert *Sixty-four* carries "BACKUP: ASTRID DIRECT" and "If you go dark, Astrid steers them."
- **Lore.**
  - **The Galactica flies a mission load:** the ~300 decoy and EW birds ride in ~75 of its ~120 multi-silo packs and open their shrouds after launch. Now in FLEET, KEY_NUMBERS and MSL-V. The reserve stays ~1,100.
  - **The frigate hull carries 4 CIWS mounts,** whatever the module (GI).
  - **The capital-ship killer** comes in a conventional (teller-device) version and a Casaba version, both nuclear.
- **Cinematography.**
  - **Cued lines.** Lines can now carry a cue, and the builder checks each within its own window. *The pack fires*, *Umbrella* and *Site One goes dark* are cued and pass.
  - **The run-in's tempo:** superseded. The user's script request changed the run-in: *Sixty-four* now sits between the reveal and the umbrella, and *Blind it* holds 5 s for its lines. The even run of 4 s shots is broken anyway, and round 5 can judge the new rhythm.
  - **The heat readout's gap.** *Site One* carries "SINK 63%", the one drone-camera exception, stated in the film rules.
  - **Nits.** *Terms* drops the Astrid's unseen firing line. *Kill wave away* opens on the Pillar's shut pods and racks to the Galactica. The sound check now splits at commas and catches every form of its words.
- **Production.**
  - **The gate's inputs.** `MEASURED` now takes a shot title, a class in one World preset (`A@C`) or a class, and the most specific entry wins. A new `BENCHMARKS` table names the entry each benchmark fills. `ASSET_REQUESTS.md` gets the gate as a worksheet the modelling session can fill in by hand, with a note to send the numbers back.
  - **The levers.** Step 1 now sizes levers 1 and 2 on the C stand-in, and a fourth step lets the storyboard session and the user choose between a smaller re-render allowance and shorter holds.
  - **Nits.**
    - The hero rock tile is for *The sweep* only.
    - *The wait*'s moving layer renders with the hull as holdout and shadow catcher.
    - *Seeker*'s rack focus is done in comp.
    - GI-GUN is added to *The pack fires*.

## Revision 5's other changes

- **The eclipse.** The sun sits in the ring plane at ~33°, and the builder computes Maren's shadow:
  - Breakwater is in it from T+6:47. Its sunrise falls inside *The wait*: first light T+7:55:12, full sun T+7:57:20, 9 s before the slug lands.
  - The escorts are in it from T+7:24:36 to T+8:06, and the Astrid, at its stop, until T+8:00.

  New World presets are E (Maren's shadow) and F (after the sunrise). Every card near the end shows its Light, and maps D and E draw the shadow. The builder checks that the sunrise stays inside *The wait*.
- **The prologue and the script** are recorded in `OPEN_QUESTIONS.md` and in the cold-read reports.
- **The render estimate** is 121 h, or 157 h with the 30 % margin: 3 h under the gate and 11 h under the week. The film is 5:55.
