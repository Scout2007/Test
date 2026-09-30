# Round 5 review: production feasibility

## Verdict
No major issues. Every round 4 item landed. The gate's inputs now resolve per shot, and the modelling session can run the gate by hand. The eclipse is costed in a sensible way, and the new cards and inserts are nearly free to render. Nothing is unbuildable.

The weak point is the margin. The estimate now sits 0.5 h under the gate. In my risk case the three render levers no longer close the gap, so the fourth step (a smaller re-render allowance or shorter holds) becomes the likely outcome. The gate's report also breaks at exactly the moment it fires. A single full pass still fits the week, with 30 h to spare even in my risk case. So this is a planning risk to fix and to tell the user about, not a blocker.

## Round 4 issues: status

| Round 4 issue | Status | Note |
|---|---|---|
| 1. MEASURED can't hold its benchmarks; the modelling session can't run the gate | resolved | MEASURED takes a shot title, a class in one World preset, or a class, and the most specific entry wins; I tested this in a scratch copy. BENCHMARKS names each benchmark's entry. `ASSET_REQUESTS.md` has a hand worksheet with "send the numbers back". Coverage gaps: #2. |
| 2. The levers have no size and no last step | resolved | Step 1 sizes levers 1 and 2 on the C stand-in, and a fourth step (a smaller allowance or shorter holds) closes the loop. At today's margin the fourth step is the likely outcome (#1). |
| 3. Stale hero rock tile | resolved | ANCHOR's hero tile is for *The sweep* only; in *The pack fires* the rock is a black disc. |
| 4. *The wait*'s shadows; *Seeker*'s rack focus | resolved | *The wait* renders with the hull as holdout and shadow catcher; *Seeker*'s rack focus is done in comp. *The wait*'s new sunrise needs a method of its own (#3). |
| GI-GUN in *The pack fires* | resolved | Added. |

## Issues, ranked

### 1. [MINOR] The budget sits on the gate, and the gate's report breaks when it fires (all 3D shots)
- **Problem:**
  - The estimate is 122.7 h raw and 159.5 h with the allowance: 0.5 h under the gate (the builder rounds this to "1 h to spare"). Every class breaks even within 0.5–7 % of its estimate (C at 201 s/frame against 200), so any overrun at all fires the gate.
  - In my risk case, levers 1–3 no longer bring the total under 160 h, so lever 4 becomes the likely outcome.
  - When the gate fires, the report written into `ASSET_REQUESTS.md` breaks. I entered plausible high numbers in a throwaway copy (C 230, C@E 260, B 90, A@C 70, V 320). The total came to 187 h, and the report read "-27 h to spare", with negative break-evens (A −13, A2 −65, V −453 s/frame).
  - Lever 4's allowance is `MARGIN`, which is hard-coded in the builder rather than kept in the data beside `GATE_HOURS`.
- **Evidence:**
  - Builder output from the scratch copy.
  - My risk case, same method as rounds 3 and 4 (the heavy C swarm shots at 250–300 s/frame, the dark lee at +50 %): 137.9 h raw and 179 h with the allowance, 19 h over the gate. Levers 2 and 3 bring it to ~166–169 h. A single pass still has 30 h to spare.
  - The 3D hours grew only 3.4 h since revision 4, but that was the whole slack.
  - Round 4's synthesis still quotes 121 h, 157 h and 5:55.
- **Fix:**
  - Tell the user now, in `OPEN_QUESTIONS.md`, that the budget is at the gate and that a smaller allowance or shorter holds is the likely fallback if the benchmarks run high. That choice shouldn't arrive as a surprise after step 1.
  - Point lever 3 at the costliest seconds. *Heat* costs 1.7 h raw per screen second, and the class C shots 1.3 h. Trimming the card and plot holds saves nothing: class E costs ~0.01 h per second.
  - In the builder, print "N h over" instead of a negative spare, and "can't close alone" instead of a negative break-even. Move `MARGIN` into `tidebreak_data.py` beside `GATE_HOURS`.

### 2. [MINOR] Three eclipse shots and two smoke shots ride on benchmarks that don't match them (25, 34, 56, 58, 61, 62)
- **Problem:**
  - *The hail* (61) is a hero hull filling the frame, lit only by a dim red ring, the city glow and its ports: the noisiest kind of frame in the film. Yet it, *Seeker* (58) and *Spinal* (62) are covered by the sunlit B stand-in, 6 h in all.
  - *Countermeasures* (25) and *Turnover* (34) carry the medium-scale smoke cache, but no benchmark covers them (6 h). The *Site One* run measures the fleet-scale cache instead.
  - *Blind it* (56), in the dark, sits under the sunlit A benchmark.
- **Evidence:** the worksheet's "Stands for" column; LIGHTING; FX-SMOKE's two caches. C@E already shows the right pattern.
- **Fix:**
  - Add `B@E`: the B stand-in relit for Maren's shadow.
  - Point 25 and 34 at a medium-smoke run, or at the *Site One* entry to be conservative.
  - Move 56 under `A@C`, the dark close-up entry.

### 3. [MINOR] *The wait*'s sunrise can't come from a cross-fade of two plates (63)
- **Problem:** The hull's light has to climb "from red to white" through the ~2 min penumbra. A cross-fade from an eclipse plate to a sunlit plate only blends the two end states, so the red-lit middle is never rendered. The moving layer gets the keyed Sun; the plate under it won't match.
- **Evidence:** 63's VFX line; the Methods row ("renders an eclipse plate and a sunlit plate and cross-fades them").
- **Fix:** Render one plate with Cycles light groups (the Sun; the ring and city glow; the emitters), then key the Sun group's colour and strength in comp. Light adds linearly, so this is exact, and it needs one plate instead of two.

### 4. [MINOR] The 2D work has no owner or step (1–6, 13–14, 32, 35, 48, 54, 69)
- **Problem:** Class E is now 179 s, 43 % of the film: 76 s of report cards and 103 s of plot inserts. The budget rightly counts it as ~2.4 h of rendering. But building it is motion-graphics work that no step of the production plan assigns, and the HUD style frame the user must approve isn't in step 1.
- **Evidence:** PRODUCTION_PLAN, "Order"; the HUD asset note.
- **Fix:**
  - Give the 2D work to the storyboard session, which already draws every plot as SVG: generate the insert sequences from the same geometry.
  - Put the style frame in step 1 and the sequences in step 3; the edit composites them.
  - Grade the cards' star plate on its own, so the black crush doesn't eat the stars.

### 5. [NIT] Small asset and builder details
- **Problem:**
  - BW's "rows of small lit ports" have no method, and they are hundreds of tiny emitters.
  - Q15 lists what the gun-defence (PDC) design pick sets, but not the CIWS now instanced on every frigate hull and on the Astrid.
  - The node syntax check skips silently where node isn't installed, which may be the case on the user's machine.
- **Evidence:** the BW and GI notes; OPEN_QUESTIONS Q15; `check_script()`.
- **Fix:**
  - Make the ports emissive with emission sampling off, with any light pools painted into the texture.
  - Add the frigates' and the Astrid's CIWS to Q15.
  - Print a note when the node check is skipped.

## Asset list corrections
- **BW:** ports emissive with emission sampling off; light pools in the texture.
- **GI, AST:** their CIWS inherit the PDC pick (Q15).
- **WORLD:** a still star plate for the seven report cards, graded separately from the film's black crush.
- **Benchmark worksheet:** add `B@E`; give 25 and 34 a smoke entry; move 56 to `A@C`.
- **Render note:** lever 3's list includes *Heat* and the costliest class C holds.

## What works
- The gate machinery is sound:
  - entries resolve title > class in a preset > class, and my test reproduced every hour by hand;
  - the worksheet lets the modelling session run the gate without the storyboard repo;
  - levers 1 and 2 are sized in step 1, and there is a last step.
- The eclipse is costed sensibly:
  - a C@E benchmark covers the four heavy dark shots;
  - the red ring and the city glow are two large area lights, which are cheap to sample;
  - the sunrise is confined to one locked P shot, and the builder checks it stays there.
- The new cards and plot inserts cost ~2.4 h for 179 s. *The net* as a 300 mm tracker renders as a small subject on black.
- All 60 page sketches run without error in node, not just parse (my test). The rig check still passes, and nothing is unbuildable.
