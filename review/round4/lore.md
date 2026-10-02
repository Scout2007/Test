# Round 4 review: lore fidelity

Lens: JCB's four posts, Sir_Lazz's art, and the Endeavor README for the weapon close-ups. The user's decisions are taken as given. Shot numbers are revision 4's (commit 9eb9a5f).

## Verdict

Revision 4 resolves all three round 3 lore issues, and every round 2 fix still holds. Nothing on screen contradicts the posts, the art or the README: **no major issues**.
- The M-1C run now plays the user's gun step by step.
- The hero missile fits Sir_Lazz's pods.
- The drones at Anchor die to the guns the posts give that job.

One minor issue is left. The kill wave's ~300 decoy and EW birds fit the Galactica only as a mission load packed in its multi-silo packs, and no file says so. There are also two nits.

## Round 2/3 issues: status

| Issue | Status | Note |
|---|---|---|
| R3-1 [MINOR] *Rails wake* didn't follow the M-1C's wake | Resolved | Shot 39 runs the README's order and keeps the barrel dark ("no glow on the barrel until it fires"). Shot 38 leaves the guns clamped through the roll. Shot 40 adds the charge, the recoil and the crest fins of the gun that fired. |
| R3-2 [MINOR] The capital-ship killer was too long for the pods | Resolved | MSL-V is sized to the art (no more than ~20 m, with the measurements written into the brief) and is the hero in both 10 and 51. "26 m" is gone from 10, and the built MSL is now only the swarm's stand-in. |
| R3-3 [MINOR] The Donnager's batteries killed drones | Resolved | Shot 45: "the Wallfish and the Donnager's CIWS cut them down". FLEET keeps the batteries for the two frigates behind the limb, and GI asks for instanced CIWS controls. |
| R2 issues: toroid lines, the pack's guard, the Q14 quote, "eleven drives", the fixed dish, T-SEC's listener | Still resolved | No regressions. "Toroid" appears in no deliverable. Q14 quotes the post exactly. Shot 11 keeps "eleven drives". DD keeps the dish fixed. A-13 keeps the T-SEC transports at the park. |

## Issues, ranked

### 1. [MINOR] The kill wave's decoys fit only if they ride in the Galactica's multi-silo packs, and nothing says so (46, 51–52; FLEET, KEY_NUMBERS, MSL-V)

- **Problem:** The pack's arithmetic uses A-26's typical load: per hedgehog, ~240 capital-ship killers in single pods and ~120 multi-silo packs of ~4 small missiles, ~720 in all.
  - The Infinity matches it exactly: 150 plus ~90 killers, and ~480 multi-packs.
  - The Galactica doesn't. Its kill wave is ~40 Casaba killers among ~300 decoy and EW birds, and A-26 has no decoys at all.
  - The MSL-V decoy "mimics a killer's signature and size". If it launches killer-sized, the kill wave's 340 birds need 340 single pods, and a hedgehog has ~240.
  - The numbers close only if the ~300 decoy and EW birds ride in ~75 of the Galactica's ~120 multi-silo packs, in place of the posts' "smaller nuclear-armed missiles", and open their shrouds after launch. The board's own reserve figure already assumes this: ~380 left on the Galactica plus ~720 on the Pillar makes ~1,100.

  The posts allow such a mission load, but no file states it, and the decoy's concept sheet needs the size limit.
- **Evidence:**
  - Part 2: "the back 1/3 of the missile pods being multi-silo launch packs, with smaller nuclear-armed missiles".
  - Part 2 leaves the load to the mission: "any number or variant of missiles you want for that particular mission", and the count "is subject to change depending on what particular type of pod and missile system the commander chooses".
  - A-26: "~240 capital-ship killers + ~120 multi-packs of ~4".
- **Fix:** Add one line to each of:
  - FLEET and KEY_NUMBERS: the Galactica flies a mission load, with ~300 decoy and EW birds in ~75 of its multi-silo packs.
  - MSL-V: the decoy fits a multi-silo cell and opens its shroud to killer size after launch.

  The reserve stays ~1,100 (~200 killers and ~180 small missiles on the Galactica, ~720 on the Pillar).

### 2. [NIT] The GI brief doesn't give the frigate's CIWS count (45; GI)

- **Problem:** The brief asks for "CIWS instanced from the Endeavor's" but gives no number. The film now leans on that number twice: the Donnager kills drones with its CIWS (45), and O11 holds empty hedgehogs with the pack because they have only 4.
- **Evidence:** Part 2: "once your missiles are expended, you're more or less left with just 4 CIWS mounts". The frigate's shared design language includes "the aforementioned CIWS mounts".
- **Fix:** In GI: "4 CIWS mounts on the hull, whatever the module".

### 3. [NIT] "A nuclear and a Casaba version" reads as if a Casaba weren't nuclear (MSL-V)

- **Problem:** The MSL-V brief pairs "a nuclear and a Casaba version" of the capital-ship killer. In the posts both belong to the nuclear family.
- **Evidence:** Part 1: "D. Nuclear (Casaba howitzers, conventional, etc)". Part 2: "nuclear-tipped and teller-device armed missiles".
- **Fix:** Say "a conventional (teller-device) version and a Casaba version, both nuclear".

## What works

- **The M-1C run (38–41) is now the user's gun as built.**
  - The turrets stay clamped through the roll.
  - The lids open on amber charge cells, the louvres ripple and the beacons flash.
  - The clamps swing off and the crutch folds, then the cradle lays.
  - The latches drop, the halves crack, rise and clunk, and the jaws open. The barrel stays dark.
  - Then the charge's buzz and chatter, the bore pulse (Q12), the recoil, and only gun A's crest fins venting.

  This matches the README step for step and keeps the user's rule: "The blue in the cannon should be the plasma during firing".
- **One hero missile is used in *Birds away* and *Seeker*.**
  - It is sized to Sir_Lazz's pods and nuclear-tipped, as the posts describe the "capital-ship killers — nuclear-tipped warheads … seen housed here in individual pods".
  - The 26 m model is demoted to a stand-in.
- **The drones at Anchor die to the right guns.**
  - The corvette does the posts' "dedicated anti-drone" job, and the frigate's CIWS are "enough to take out … some drones".
  - The Donnager's four batteries wait for the Compact frigates, the gun fit's medium-range shooting match.
- **The two waves play the posts' two ways through a defence.** The spend wave is there to "deplete their defensive capacity", and the kill wave to "break through during that point of saturation". Launching each wave in one go keeps the decoys honest, and nothing in the posts is against it.
- **Breakwater's answer honours the destroyer post (47).** It spends every cell on "the ship that will steer the birds". A ship ten times its size rethinking around one destroyer is the post's own claim.
- **GUN values hold to the end.**
  - The terms ask for the Breakers charts, because the garrison's emplacements "answer to no one".
  - Site 1 goes dark on terms, never struck (§13).
  - The Endeavor keeps its fins edge-on until the terms are signed.
- **Names and call signs are consistent in every new line.** "T-SEC, you're next." keeps T-SEC as the next boots on the ground ("Along with the LREF and the EAF, T-SEC tends to be the first boots on the ground"), with a listener at the park (A-13). "Site One dark, and the Breakers charts." and "Last drones down. Pack's clear." read cleanly.
