# Round 2 synthesis

Round 2 read **storyboard revision 2** (54 shots, 3:34) with the same five reviewers who read revision 1. Each first checked how its round 1 issues were handled, then reviewed revision 2 fresh. They raised **7 major issues** (26 in round 1), 20 minor ones and a handful of nits. The lore reviewer had no major issue left.

**Revision 3** (62 shots, 4:11) answers all seven major issues and nearly every minor one. It also adds the user's request from this round: close-ups of the weapons at work. This file records the decisions. The reports are in this folder. Shot numbers below are revision 3's unless marked "rev 2".

## The verdicts

- **Physics:** the round 1 fixes hold. The inertial approach, the ~48° waves, the backstop clearances, the spinal shot from rest, the heat to T+8:00 and all 54 clocks check out. The two new problems both break the doctrine's own numbers: Skerry's rounds and the multi-pack missiles.
- **Doctrine:** Act IV now runs by the book (dazzle, spend wave, kill wave, cripple, hail, then kill from rest). The one new problem is the pack, left unguarded at Anchor, with a defender that never tries for it.
- **Lore:** every round 1 issue is resolved. Nothing on screen contradicts the posts. **No major issues.**
- **Cinematography:** 3:34 is earned once two cheap things are fixed: HUD text nobody could read, and two payoffs that happen off-screen.
- **Production:** every shot is buildable. The week rests on costs nobody would measure until the end, and several shots were in the wrong class.

## Major issues and decisions

| Lens | Issue | Decision | Where |
|---|---|---|---|
| Physics | With the mirrored geometry, 12.5 km/s rounds from Skerry can't reach the six nets on time (the first could arrive T+7:03 at the earliest, the last T+8:53) | H-14 raised: the mass driver throws at **up to 15.5 km/s** (13.5–15.5 for the lane salvos, per the reviewer's integration). Five nets on the lane at T+6:40–7:30; the sixth salvo, at 12.5 km/s, rings Anchor instead (T+6:52) | 7, 12, 43, 44; Defence HO3, H-14; WN §2 |
| Physics | Most of the "hundreds of plumes" are multi-pack missiles (60 km/s), which can't fly Anchor → Breakwater in 25 min | The waves leave in two parts. The **slow multi-packs go first** (T+7:07 and T+7:08:30, 45-minute flights), the killers at T+7:27 and T+7:28:30, and each wave still lands within a second | 46, 48; PHASES, KEY_NUMBERS |
| Doctrine | The pack, with ~1,950 missiles, sits unguarded at Anchor for 1 h 44 min, and the defender, which predicted Anchor, never tries for it | The **Donnager and the Wallfish guard the pack** (D11 now covers any detached fire base; O11 now holds empty hedgehogs with the pack until the way home is safe). The defender makes its try: Skerry's sixth salvo rings Anchor with canister clouds and drones wake behind them. The pack tucks in behind the rock and the guard beats the drones off | 42, 44 (new *Anchor ringed*); FLEET; LREF D11, O11 |
| Cinematography | HUD text isn't counted, so the fire plan (~33 cps) and the lost ships' callback can't be read | The check now counts **HUD labels** (a new `hud` field) with the subtitles, and needs at least 1 s per line. The fire plan is 8 s in two beats with two labels. The callback holds alone at the end of *Terms* (8 s). The Anchor insert runs 5 s | 8, 26, 29, 42, 60; builder |
| Cinematography | Both spinal shots fire on their last frame, and Site 1's lights going out are 1–2 px | Both spinal shots now **fire two seconds in**, so the bloom stays on screen, and the payback jumps count from the firing. A new 2 s **2,000 mm tracker** shot shows Site 1 going dark (~10 px) | 23, 56, 61 (new *Site One goes dark*), 62 |
| Production | The week rests on unmeasured class B and C costs; the benchmarks measured only A, A2 and D | Step 1 benchmarks the **methods with stand-ins**: linked Endeavors plus 600 existing missiles through the swarm system, the two volumes, and the dark lee. A **go/no-go gate** follows (C above ~230 s/frame or B above ~100 s/frame) with fallbacks agreed in advance | RENDER_NOTE; PRODUCTION_PLAN |
| Production | Classes don't follow the pixels | Small subjects on black move down: 22, 27, 37 to B; 21, 41 to D. The last shot becomes class P (a planet plate plus a ship layer). The smoke shot 45 moves up to C, the turnover to A2, and the water dump (59) gets its own asset (FX-DUMP) and class V (~250 s/frame) | RENDER_CLASSES; shots |

The render estimate is now **123 h, or 159 h with the 30 % margin**, inside the 168 h week. That includes the user's five close-ups and three new review shots.

## The user's request: weapon close-ups

The user asked for close-ups of the other weapon systems: missiles in flight, the nose sensors, railcannons waking up and firing, and laser arrays flashing and tracking. Revision 3 adds five shots. They use assets that are built or already requested, and add ~4.6 h of render:

| Shot | What it shows | Class |
|---|---|---|
| 10 *Birds away* | A drone camera paces one of wave one's 150 a minute into its boost (cinematic licence: no camera keeps up with 30 g) | B |
| 18 *Lenses* | A laser focusing array slews onto a pod missile and pulses violet; the beams stay invisible; a far-off kill | A |
| 39 *Rails wake* | An M-1C unlocks, rises and charges (the wake at 2×). This also answers the cinematography note that the wake played inside a 5× roll | A |
| 40 *Fire* | The muzzles: gun A fires (the bore pulse, cinematic licence Q12), and only that gun vents | A2 |
| 52 *Seeker* | A Casaba killer's nose in its last seconds: the ablative cap glowing under Breakwater's lasers, the seeker shutter opening, Breakwater growing from a point to a sliver | B |

"The nose sensors" was read as the missiles' seeker heads; `OPEN_QUESTIONS.md` asks whether the user meant the Endeavor's own nose sensors instead.

## Minor issues and nits

All applied, except where marked.

- **Physics.**
  - **Site 1's 72-minute wait.** It now fires from the moment the fleet clears the shadow; the fleet answers at once with rolls, smoke and low-power dazzle (45).
  - **The heat margin after the dump.** The Endeavor's arrays stand down when Breakwater dies, and the Astrid keeps Site 1 dazzled.
  - **The spinal margin.** The Astrid now stops at **10,000 km**: a ~167 s flight with ~17 s of margin. "Impact in two forty-seven." (57).
  - **The pack's hiding place.** It is a slot in the rock's shadow that hides it from Site 1 and, after T+6:55, from the western site. It no longer claims to be hidden from Breakwater.
  - **Nits:**
    - the departure burn tilts ~4.5°;
    - the escorts match Breakwater's orbit after the stop, so the terms distance holds;
    - the Endeavor sits within ~9 km of the lee surface, where the sun's shadow and Site 1's overlap (map C).
- **Doctrine.**
  - **Site 1 and the free dazzle:** as above.
  - **The kill wave's mix.** It is **~40 Casaba killers among ~300 decoy and EW birds**, sized to cripple; ~1,100 missiles stay in reserve.
  - **The frigate.** It waits in a pre-dug cleft on the moonlet's far side, at 45 km throughout. The Donnager reports honestly ("Rocks inside three hundred done. Moonlets next."), and *Too hot* makes the risk explicit ("Sweep's not done." / "Can't wait. Fins out.").
  - **Nits:**
    - the Astrid now sits 50 km above the Extenuating and the destroyers are 50 km apart (D2);
    - "eleven drives";
    - the Astrid cuts its drive during the umbrella so its plume won't blind its own point defence;
    - D8's conditions for the second turnover are written into PHASES;
    - the Endeavor's VLS are named as the fast reserve;
    - the neighbouring site is noted in WN §8.
- **Lore.**
  - **The stale "toroid" lines** (the torpedo in §4.3, the Draft_corrections row) are rewritten.
  - **The pack's guard:** as above.
  - **Q14 and LREF §2** now quote the post exactly.
  - **Nits:**
    - "eleven drives";
    - the destroyer's dish is fixed on its truss (`dish_deploy` dropped);
    - T-SEC's transports wait at the shield park (A-13, FLEET), so the last line has a listener.
- **Cinematography.**
  - **Screen direction.** The rule names the exception: at Anchor the frigate is the one enemy on screen left. The fin-hit slug comes from the right, the lance crosses from right to left, and the Casaba jets, the kill wave and the spinal slug come from screen left.
  - **Lines:**
    - *Holed* keeps only "Canterbury's gone.";
    - *Normandy* is 5 s with a 2 s hold on the hiss;
    - the turnover drops "Normandy's gone.";
    - the lines in *Countermeasures* and the broadside are cut;
    - *The wait* is 6 s;
    - the last line plays over black.
  - **Not applied as asked: *Too hot*.** The reviewer wanted its line cut because it repeated the picture. It now carries the sweep's risk instead ("Sweep's not done." / "Can't wait. Fins out."), which the doctrine reviewer asked for and which is new information.
  - **Framings:**
    - the Canterbury at 1,500 mm and the Normandy at 800 mm;
    - a new 1 s insert, *The flash*, shows the platform firing, and *The platform dies* matches its framing;
    - *The spend wave* is at 250 mm, with the limb in frame and a line ("Their batteries are lit. Steering round.").
  - **The checks** now cover HUD text, at least 1 s per line, explicit end clocks for compound rates (and a note for any shot with no rate), a roll or dissolve on every jump of 30 minutes or more, and a wider list of words a silent camera can't hear.
    - **Not done:** a cue offset per line. Lines are placed in the edit.
  - **The SINK readout** is now keyed so the heat builds: 94 → 31 → 62 → 88 → 98 %.
  - **Nits:**
    - the task-group shot is a drone camera;
    - the spinal shot is an MS;
    - the first line is tagged "ACTUAL · ASTRID".
- **Production.**
  - **Build order.** The swarm system is built on the existing missile with LOD slots; the missile variants go first in the concept round; every breakable hull is modelled in sections; blocking proxies (PROXY) come in step 1; *Umbrella* renders last.
  - **World and states.** Each 3D shot names its World preset (ENVS), and render batches follow it. The Endeavor, the destroyers and Breakwater carry states, which the builder shows and checks.
  - **Rig controls and closest views.** The Astrid, Breakwater and the destroyer get the missing controls. The closest-view table fixes the Astrid and adds the hedgehog module, the missiles, the M-1C and the gun module (now in Q13).
  - **Hidden costs.** They are in the plan's methods row:
    - defocused foregrounds as their own layer;
    - a rock tile in the C benchmark;
    - swarm lights fading in over ~6 frames;
    - `pod_ripple` driven from the swarm's launch times;
    - fin area lights in the dark lee.
  - **Nits:** a sun-direction gradient on the haze; ~150 GB of disk.
  - **Asset list corrections:** all applied.

## Beyond the reports

- **The runtime grew to 4:11.** The five close-ups add 15 s. *The flash*, *Anchor ringed* and *Site One goes dark* add 9 s, and the reviewers' holds (the picture, the fire plan, the terms, the wait, the Normandy) add ~17 s. The user left the runtime flexible, and the new holds were asked for, so nothing was cut; round 3 should say if the pace suffers.
- **The spinal miss clearance** is recomputed from the geometry: with the Astrid at 10,000 km, a miss clears Maren's surface by ~7,200 km.
- **The HUD sketches** now show exactly the labels the `hud` field counts.

## Doctrine refinements

- **LREF:**
  - D11 is now "Guard the park and the fire base".
  - O11 holds empty hedgehogs with the pack until the way home is safe.
  - The §4.3 torpedo carries its plasma to contact.
  - §2 quotes the destroyer post exactly.
  - A-13 puts T-SEC at the shield park.
- **Defence:** the mass driver is up to 15.5 km/s (Skerry row, HO3, the envelope table, H-14).
- **Working numbers:** the §2 mass driver at 15.5 km/s; §8 notes the neighbouring site.
- **Draft corrections:** the mass driver's flight time, and the lance row re-explained as a field-held jet.

## Revision 2 → revision 3

Unchanged titles keep their order; the numbers shift as shots are added.

| Rev 2 | Rev 3 | Note |
|---|---|---|
| 1–9 | 1–9 | 3 is now a drone camera; 7 is 6 s with one label; 8 is 7 s |
| — | 10 Birds away | new (user request) |
| 10–16 | 11–17 | 11 has "eleven drives" |
| — | 18 Lenses | new (user request) |
| 17–24 | 19–26 | 19 loses its line; 21–22 at 1,500 mm; 23 fires 2 s in; 26 is 5 s |
| 25 | 27 | 5 s, 800 mm, a hold on the hiss |
| 26–29 | 28–31 | 29 is 5 s; 30 and 31 carry the sweep's honesty and risk |
| — | 32 The flash | new: the platform firing, 1 s at 1,200 mm |
| 30–34 | 33–37 | 35 is the frigate in its cleft; 37 is the lance crossing from the right |
| 35 Broadside | 38 Broadside, 39 Rails wake, 40 Fire | split (user request) |
| 36 | 41 | the platform dies at T+5:14:40 |
| 37 | 42 The fire plan | 8 s, two beats, the guard named |
| 38 | 43 | four more nets on the lane |
| — | 44 Anchor ringed | new: the defender's try at the pack |
| 39 | 45 | Site 1 has been firing since the shadow |
| 41 The pack fires | 46 | now T+7:07, the slow birds |
| 40 The anvil | 47 | |
| 42–43 | 48–49 | 48: ~40 Casaba killers; 49: the Astrid's drive cut |
| 44–45 | 50–51 | 50 goes to full power; 51 at 250 mm with a line |
| — | 52 Seeker | new (user request) |
| 46–49 | 53–56 | 54's jets come from screen left; 56 fires 2 s in, from 10,000 km |
| 50 Three minutes | 57 The wait | 6 s; "Impact in two forty-seven." |
| 51–53 | 58–60 | 59 is FX-DUMP, class V; 60 is 8 s, with the callback held alone |
| — | 61 Site One goes dark | new: 2,000 mm on the plateau |
| 54 | 62 Hold | the fins run out in silence; the last line over black |

## For round 3

Revision 3 changes the least-tested parts of the board, so round 3 should look hardest at:
- **the user's five close-ups** (10, 18, 39, 40, 52): realism, lore, framing, cost;
- **the new beats** (32, 44, 61) and the pack's guard;
- **the two-part waves** (46, 48): whether the timings and missile loads close;
- **Skerry at 15.5 km/s**;
- **the 4:11 runtime and its pace**;
- **the reclassed budget** (159 h with margin) and the benchmark gate;
- **the new checks:** HUD text, rolls, sound words, states.
