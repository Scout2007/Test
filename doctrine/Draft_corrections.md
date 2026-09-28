# The draft's numbers, checked

This checks the "Mechanics" and "Engagement envelopes" sections of `pack/storyboard_draft/DRAFT_READABLE.md` against `working_numbers.md` (WN). The last table lists shot-level physics problems; they are fixed in phase 2, not here.

## Mechanics

| Draft says | Verdict | Corrected |
|---|---|---|
| "With fins stowed, a ship fights on heat sinks for a few minutes." | Too short, given any reasonable sink | Endeavor: ~24 min at full combat, ~91 min with the guns silent, ~3.7 h cruising dark, on an assumed 20 TJ sink (WN §4; the sink size is Q5 in `OPEN_QUESTIONS.md`). |
| "A 20 km/s slug takes 50 s to cross 1,000 km, and a ship that keeps jinking will not be there." | Arithmetic right; the rule needs the target's axis | Whether it escapes depends on how fast it can move *sideways*. A capital ship braking end-on has only RCS (~0.1 g) and needs ~20 s to clear 150 m. The M-1C (25 km/s) can't miss it inside ~510–920 km (WN §2). |
| "A 3.3 m UV array focuses to roughly a 0.26 m spot at 1,000 km, which is deadly, but 2.6 m at 10,000 km, which is merely hot." | Spot sizes right (0.39 m and 3.9 m with a 1.5× jitter allowance); "merely hot" wrong for most targets | At 10,000 km one array still kills a radiator fin in ~11 s and a missile's side in ~17 s. It is a hull or a hardened missile nose that it can't kill there (WN §1). |
| "Far out, lasers blind optics rather than kill." | Right | Dazzle works past 10⁶ km (WN §1). |
| "You cannot hide a burning drive… Only cold, passive objects in clutter stay hidden." | Right, and stronger than stated | A cold 300 K Endeavor hull is still detectable at ~0.9 AU (WN §5). Crewed warships can't hide at all; only objects at the temperature of their surroundings can. |
| "The group arrives at about 180 km/s closing speed… its path is predictable for minutes." | Wrong by two orders of magnitude | Braking 180 km/s at 1 g takes **5.1 h over 1.65 million km** (WN §6). Shields jettisoned at that speed can never be collected, which contradicts the lore. Proposal: exit slow at ~450,000 km (LREF O1). |
| "Time is compressed in the edit: a real long-range exchange takes minutes." | Hours, not minutes | The whole operation runs ~5–7 h of real time (WN §3, §6). Phase 2 labels every time jump. |

## Engagement envelopes

| System | Draft | Corrected (WN section) |
|---|---|---|
| Laser focusing array (3.3 m UV) | ≤ 2,000 km kill · 50,000 km dazzle | **By target:** fins ≤ ~10,000 km (~11 s); missiles side-on ≤ ~30,000 km; missile noses ≤ ~1,000 km (~28 s); hull belt ≤ ~100 km, or ~2 min at 1,000 km against a target that doesn't roll. **Dazzle:** > 10⁶ km. (§1) |
| PD laser (1.6 m) | ≤ 500 km | Missiles side-on ≤ ~1,000–5,000 km; noses ≤ ~100 km (§1) |
| Twin railgun battery | ≤ 1,000 km vs ships · 5–60 s | **By target** (no-escape range): capital ship end-on 510–920 km; broadside 1,020–1,840 km; frigate 190–340 km; corvette 80–150 km; monitor 1,500–2,700 km. Flight time 4 s per 100 km. (§2) |
| Spinal cannon | ≥ 10,000 km vs fixed · tens of s | Fixed targets out to ~100,000 km (flight ~28 min; at 10,000 km ~2.8 min, not tens of s). Mobile monitor ≤ 3,600–4,800 km; crippled monitor ≤ 11,000–14,700 km. (§2) |
| Mass driver (Kest) | ~100,000 km · minutes | 100,000 km takes **~2.8 h**. It lays nets in pre-planned lanes; it doesn't snipe (Defence HO3). (§2) |
| Missile | 10⁵–10⁶ km · minutes | Capital-ship killer: 18 min to 100,000 km, 2.5 h to 10⁶ km; small multi-pack missiles take twice as long (§3). |
| Casaba howitzer | 1–5 km standoff | Right. It breaches a 0.72 m belt from ~2 km (20 kt) to ~4 km (100 kt), and Bastion's ~2 m belt from ~2.5 km (100 kt). Fins die anywhere along the jet out to 50–130 km. (§7) |
| Plasma lance | ≤ 50 km · near-instant | Kept as a soft-coat value: compact toroids at ~1,000 km/s (LREF A-23). |
| CIWS / PDC | ≤ 5 km · < 1 s | Kill clouds are placed 5–30 km out and the rounds take 2.5–15 s to get there. The missile then crosses the cloud in under a second and dies on its own speed. About 3 missiles/s per 16 mounts. (§8) |

## Shot-level problems to fix in phase 2

| Shot | Problem | Direction |
|---|---|---|
| 4 Flip and burn | A 180° flip in 5 s | The Endeavor needs ~28–49 s (WN §6). Show part of it and cut, or compress and label. |
| 5 Shield away | Released during a 180 km/s braking burn, so unrecoverable | Release at the park, at low speed (O1). |
| 7 Hedgehog | One hedgehog | A pack of three (lore). |
| 13 Into the Shoals | "Tumbling asteroids 2–5 km across" at few-km spacing | Large bodies are hundreds of km apart. Pass one chosen rock close, deliberately (Defence §4.1). |
| 14 Screens out | Swarm pours from Kest during the fight | Drones are parked in the Shoals and wake as the fleet passes (HO4). |
| 16 The moon speaks | A mass-driver slug arriving in real time | Launched hours earlier into the predicted lane; it shatters the rock the Endeavor shelters behind (HO3). |
| 18–20 Too hot / fin hit / broadside | Fins out, then a broadside | Doctrine says fins out only behind cover, and broadsides with fins stowed (D3, O6). Reorder or re-stage. |
| 26 Spinal | "Aligned during the flip, the Astrid fires" | While braking toward the target, the spinal points *away* from it. The Astrid stops, slews and fires (§10). Bastion dodges at > ~4,000 km unless its drive is crippled (O10). |
| 27 Casaba | One Casaba "cuts Bastion in two", *after* the spinal | Casaba spears cripple Bastion first, and the spinal shot kills it (O10). The break-up comes from the spinal hit plus secondary explosions. |
| D7 rule / 28 | Hab rings spin down at action stations | Rings keep spinning, depopulated (A-34). |
| Render plan | EEVEE for the wides | Cycles for everything (user decision). |
