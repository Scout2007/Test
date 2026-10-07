# Round 3 review: lore fidelity

Lens: JCB's four posts, Sir_Lazz's art and, for the new weapon close-ups, the Endeavor README. The user's decisions are taken as given. Shot numbers are revision 3's.

## Verdict

Revision 3 resolves all six round 2 lore items, and nothing on screen contradicts the posts: **no major issues**. The user's five close-ups are mostly faithful: violet lenses with invisible beams, per-gun venting, and missiles shown as carriers. Three details should still be fixed before modelling:
- *Rails wake* doesn't follow the README's wake.
- The "26 m" capital-ship killer looks too long for the pods in Sir_Lazz's hedgehog art.
- In *Anchor ringed*, the gun frigate's batteries do the anti-drone work that the posts give to CIWS and corvettes.

## Round 2 issues: status

| Round 2 issue | Status | Note |
|---|---|---|
| 1 [MINOR] Free-flying toroids survive in two doctrine lines | Resolved | The §4.3 torpedo now "carries its plasma to the target and releases it at contact". The Draft_corrections row calls the lance a field-held jet. "Toroid" no longer appears anywhere, including the reading edition. |
| 2 [MINOR] Empty hedgehogs left at Anchor without a screen | Resolved | The Donnager and the Wallfish guard the pack (42, 44). D11 now covers any fire base, and O11 keeps empty hedgehogs with the pack under guard. Issue 3 concerns the Donnager's weapon. |
| 3 [MINOR] Q14 misquotes the post | Resolved | Q14 and LREF §2 now quote both sentences verbatim. |
| 4 [NIT] "Fourteen drives" | Resolved | Shot 11: "eleven drives … the three ships at the park stay dark behind them". |
| 5 [NIT] `dish_deploy` adds a fold | Resolved | Shot 5: the dish is "clear on its truss" once the shield goes. DD fixes it forward, as in the art. |
| 6 [NIT] T-SEC has no listener | Resolved | A-13 and FLEET put the T-SEC transports at the shield park, arriving after the group. |

## Issues, ranked

### 1. [MINOR] *Rails wake* doesn't follow the M-1C's wake (shot 39)

- **Problem:** The user asked to see the railcannons wake, and the README defines how the M-1C does it. Shot 39 departs from that in three ways:
  - Its VFX line asks for "Rail glow", so the rails glow before any shot fires. The user ruled that out.
  - The supershell's split and lift, with the jaws opening (`rail_arm`), is the M-1C's signature move. It is in the rig list but missing from the action.
  - The order is off. The README powers up first (lids, amber cells, beacons), then releases the clamps, lays the gun and opens the shell. "Until the turret locks", at the end of the shot, reads as the travel lock closing again.
- **Evidence:**
  - README: "A plasma slot glows only while a shot runs."
  - Project context: "blue appears only as the plasma pulse during a shot; heat glows only on the fins, and only on their radiator face".
  - Project context, the wake: "1. The capacitor-bank lids and rear radiator louvres open; amber charge cells and meters light; beacons flash. 2. The travel-lock clamps release and the crutch folds flat. 3. The cradle lays onto the target. 4. The shell opens."
  - The user: "The blue in the cannon should be the plasma during firing".
- **Fix:**
  - Action: "Lids open on amber charge cells and the beacons flash; the travel-lock clamps swing off and the crutch folds; the cradle lays onto the rock; the supershell splits and lifts, and the jaws open."
  - VFX: "charge cells, meters, beacons".
  - Keep the only glow on the barrel for shot 40's bore pulse.

### 2. [MINOR] The capital-ship killer looks too long for the hedgehog's pods (shots 10, 52; MSL, MSL-V)

- **Problem:** Shot 10 shows one of wave one's capital-ship killers at hero scale as "the 26 m body", which is the built MSL.
  - The scale bar on Sir_Lazz's hedgehog art gives the forward single pods as ~6–7 m boxes, in an array ~32–49 m across.
  - A pod there holds a missile of about 20 m at most, even if the pods point outward; 26 m doesn't fit.
  - Shot 52 shows the same class of missile, a Casaba killer, from the same pods.
- **Evidence:**
  - Part 2: "just about 360 missile pods in this current pattern", with the capital-ship killers "seen housed here in individual pods".
  - `reference_art/frigate_hedgehog.webp`: the pod section runs ~72–215 m along the ~400 m hull.
- **Fix:**
  - Size the capital-ship killer in the MSL-V concept sheet to fit the GI-MAV pods, scaling the MSL base down.
  - Drop "26 m" from shot 10's action.
  - Make shots 10 and 52 show the same design.

### 3. [MINOR] The Donnager's batteries do the anti-drone work (shot 44)

- **Problem:** In *Anchor ringed*, "the Donnager's batteries and the Wallfish pick the drones off". The Donnager carries the gun module: four large kinetic batteries, built for a medium-range shooting match with ships. The posts give drones to corvettes, the PD fit and CIWS, and say a frigate's module locks it into a narrow doctrine.
- **Evidence:**
  - Part 2: the gun fit is "4 large kinetic batteries … for a prolonged and sustained shooting match with the OPFOR".
  - Part 2: against drones, "Swap out your modules for a pure point defense loadout".
  - Part 2: "once specced into a particular ‘configuration’, you’re more or less locked to a very narrow offensive/defensive doctrine".
  - Part 2: a frigate's CIWS are "enough to take out some stray anti-ship missiles, some drones".
  - Part 1: the corvette is "a dedicated anti-drone and anti-bomber/fighter warfare screen".
- **Fix:** Change it to "the Wallfish and the Donnager's CIWS pick the drones off". Keep the Donnager's batteries for the threat a gun frigate guards against: the two Compact frigates behind the limb.

## What works

- **The round 2 fixes all land, and the round 1 fixes hold.**
  - The Astrid is 1.6 km. Its fins stay stowed under Skerry's laser and glow like a lantern in the coast.
  - The lance is a field-held jet at 45 km, "inside the ~50 km the field can hold".
- ***Lenses* (18) matches the README's array.** A violet lens pulses while it fires, the beams stay invisible, and the yoke is already swinging to the next target.
- ***Fire* (40) matches the README's shot.**
  - Gun A fires alone, in the tracer style.
  - The bore pulse is labelled as the user's licence (Q12).
  - Only the gun that fired vents.
- ***Birds away* (10) and *Seeker* (52) treat missiles as the posts do, as carriers.**
  - The close-ups show the body, plume, spin, hardened nose and seeker.
  - The warhead's family (nuclear, Casaba) is left to shot 54.
  - The drone camera keeping pace is labelled as licence.
- ***Anchor ringed* (44) gives the corvette its canonical job.** The defender's try at the fire base plays like the posts' sorties at the detached shields: it costs the defender its last drones.
- **The degraded net still reads.** The NET DEGRADED tag in 26 carries it now that the line in *Holed* is cut.
- **Names and call signs are consistent in every new line.** "ACTUAL · ASTRID" on the first line places the flag in the Astrid.
