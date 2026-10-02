# Round 2 review: lore fidelity

Lens: JCB's four posts and Sir_Lazz's art. The user's decisions are taken as given. Shot numbers are revision 2's.

## Verdict

Revision 2 answers every round 1 lore issue. The lance is now the posts' own lance, the Astrid is 1.6 km and glows, the net thins, the magazines add up, and the concept briefs carry the design rules. Nothing on screen contradicts the posts, so there are **no major issues**. Three minor ones remain: two stale "toroid" lines in the doctrine, the empty hedgehogs left at Anchor without a screen, and Q14 misquoting the post.

## Round 1 issues: status

| Round 1 issue | Status | Note |
|---|---|---|
| 1 [MAJOR] The lance as a free-flying ring | Resolved | Shots 33–34 and FX-LANCE draw a field-held jet; A-23 makes ~50 km the field's reach. Two stale "toroid" lines survive in the doctrine (issue 1). |
| 2 [MAJOR] The "kilometre-long" Astrid | Resolved | Shot 21 says "1.6-kilometre hull"; FLEET says 1.6 km; AST ~1,650 m. |
| 3 [MINOR] One destroyer holds the net alone | Resolved | Shot 20: "the net's yours". Shot 24: NET DEGRADED · DIRECT LINKS. LREF §3 now quotes "if present in large enough numbers". |
| 4 [MINOR] The Infinity is dry after 150 missiles | Resolved | 150 go at Skerry and the rest in the spend wave (~700 each); MSL-V gets a MIRV bus. What happens to the empties is issue 2. |
| 5 [MINOR] The destroyer's dish placed aft | Resolved | DD follows the art and Q14 asks the user, but Q14 misquotes the post (issue 3). |
| 6 [MINOR] Corvette and tender briefs | Resolved | Both briefs now require warp rings, a shield and radiators that stow for warp. CV: no spin section. TND: spare shields and a module-swap rig. |
| 7 [MINOR] The shieldless crossing | Resolved | Shot 13: "No shields from here." |
| 8 [MINOR] Assumptions stated as canon | Resolved | LREF §3 now tags [A-29], §10 tags [Model], and shot 34 reads "the ~50 km the field can hold". |
| 9 [NIT] The Endeavor's VLS | Declined | Acceptable. Holding missiles for self-defence contradicts nothing: the posts make missiles a delivery platform, not a duty to fire. |
| 10 [NIT] The Astrid never glows | Resolved | Fins stay stowed while Skerry's laser can see them (6), then glow "like a lantern" in the coast (12). |
| 11 [NIT] "Nuclear plasma spears" | Resolved | Shot 47 says "nuclear jets"; FX-CASABA is "Casaba jets". |
| 12 [NIT] Tone against the GUN's values | Resolved | "Remember the Cant." goes to ASTRID GUNS (22); the hail goes unanswered (48). |
| 13 [NIT] Close the canon loops | Resolved | Shot 54: "Nauvoo, bring the shields in. T-SEC, the sky's yours." NIT 6 covers who hears it. |

## Issues, ranked

### 1. [MINOR] Free-flying toroids survive in two doctrine lines (LREF §4.3; Draft_corrections)

- **Problem:** The lance is fixed, but two lines still describe free-flying plasma:
  - The torpedo in LREF §4.3 "closes to ~50–100 km and fires or becomes one large toroid". That is plasma crossing 50–100 km with no generator: the mechanism round 1 removed from the lance.
  - `Draft_corrections.md` still calls the lance "compact toroids at ~1,000 km/s (LREF A-23)", which the new A-23 contradicts. In the reading edition the stale row sits beside a tooltip giving the new A-23.

  Neither line is on screen, so only the doctrine is wrong, not the film.
- **Evidence:** Part 1, item 4: plasma needs "an active electromagnetic field to maintain its form lest it just fizzles out; hence the need for a self-contained ‘topredo’ [sic] with an EMF generator".
- **Fix:**
  - Torpedo: "a self-propelled field generator that carries its plasma to the target and releases it at contact, or within the few kilometres its own field can hold".
  - Draft_corrections row: "a field-held jet, ~50 km of field reach (A-23)".
  - Rebuild the reading edition.

### 2. [MINOR] The empty hedgehogs are left at Anchor without a screen (shots 37, 41–42; FLEET; O11)

- **Problem:** After T+7:28 the Infinity is dry and the Galactica has fired the kill wave. Yet "Pack holds Anchor. The rest, with me." leaves all three hedgehogs in the Breakers with nothing to screen them from drones. Shots 41–42 cite O11, which still says "Withdraw empty hedgehogs to the tender (4 CIWS only [Lore])", so the board contradicts its own rule.
- **Evidence:**
  - Part 2: "once your missiles are expended, you're more or less left with just 4 CIWS mounts. That's… enough to take out some stray anti-ship missiles, some drones, and some attack craft, but it's not much".
  - Part 2: a frigate is "more useful as a broad category, integrated into a fleet, rather than acting as a solo ‘hero ship’".
  - Part 1: the corvette is "a dedicated anti-drone and anti-bomber/fighter warfare screen".
- **Fix:**
  - Leave one corvette with the pack. Shot 37: "Pack and Rocinante hold Anchor. The rest, with me.", plus a tag on the plot.
  - Amend O11: "withdraw empty hedgehogs to the tender, or hold them with the pack under a corvette screen".

### 3. [MINOR] Q14 misquotes the post (OPEN_QUESTIONS Q14; LREF §2)

- **Problem:** Q14 asks the user to choose between text and art. It says the post puts the dish "over the aft third", in quotation marks, but those are not the post's words; LREF §2 repeats the paraphrase. The exact wording is vaguer, and it strengthens the case for the art.
- **Evidence:** Part 3 says the antenna is "taking up a near third of the ship’s overall length (at the aft of the ship)", and also that "the stern is literally taken up by the ship’s engineering section and radiators".
- **Fix:** Quote both sentences verbatim in Q14 and §2. Point out that the post itself gives the stern to engineering and radiators.

### 4. [NIT] "Fourteen drives" includes the three ships that stay at the park (shot 10)

- **Problem:** Shot 10 says "fourteen drives light one after another as the group turns onto the approach line". But the Nauvoo, the Excelsior and the Tantive IV stay at the park (FLEET, D11). The shot's asset list already leaves the tender out.
- **Evidence:** Part 1: "there WILL be tenders somewhere in the backline".
- **Fix:** Change it to "eleven drives"; the park's three stay dark behind them.

### 5. [NIT] `dish_deploy` adds a fold the art doesn't show (shot 5; DD)

- **Problem:** In shot 5 the Canterbury "swings its big dish out", and the DD brief asks for `dish_deploy`. In the art the dish sits fixed on its truss behind the shield, within the front ring's span. The post retracts only booms and masts for warp.
- **Evidence:** Part 3: "The various sensor arrays attached to the boom arms and masts are capable of being retracted of course, so that they don’t extend beyond the warp bubble when in warp". The dish becomes the ship's "eyes and ears … once the front impact shield is removed".
- **Fix:** Keep the dish as drawn: in shot 5 it is unmasked as the shield leaves, and the motion comes from `booms_deploy` and the drone bay. Either drop `dish_deploy`, or mark it in DD as an extension for the user to confirm.

### 6. [NIT] "T-SEC, the sky's yours" has no listener (shots 37, 54; A-13)

- **Problem:** Nothing places T-SEC's craft. "All fourteen" leaves no room for them in the group, and the park readout shows only PARK HOLDING.
- **Evidence:** T-SEC post: its space assets are "often just troop transports, barges, or specialized boarding assault craft (BACs)", and they are "either entirely attached to EAF groups and formations, or are assigned on an operational or deployment-by-deployment basis".
- **Fix:** Add "T-SEC HOLDING AT PARK" under the park readout in shot 37, having arrived after the group. Add one line to A-13 on where the landing force waits.

## What works

- **The lance now reads as the posts' lance.**
  - "The ship's field reaches out and a spear of plasma runs from the nose to the frigate."
  - A-23 makes the ~50 km limit the reach of the ship's own field, so the range and the canon mechanism are one idea.
  - The sketch draws a single continuous line.
- **The Astrid:**
  - It is 1.6 km.
  - Its fins stay stowed under Skerry's laser, then glow in the coast.
  - The AVPSA is articulated.
  - Shot 43's umbrella is the posts' "hard pressed to get close to this thing with drones, fighters, or even missiles".
  - It fires from rest behind the escorts, which respects its weak armour and poor manoeuvrability.
- **The destroyers:**
  - The dish sits forward and is clear once the shield leaves (5, 19).
  - The net thins after the Canterbury.
  - Breakwater spends all 64 cells on one 200 m ship: the posts' destroyers are "enough to force a tactical and strategic rethink of the positioning of ships ten times their size".
- **Shields:**
  - Every ship's shield is off by T+0:02, and every later sketch drops it. I checked the regex in `sketchlib.js` that strips the gold shield.
  - "No shields from here" names the trade.
  - Shot 54 brings the shields home.
- **Magazines:** the numbers now add up against the posts' ~360 pods, multi-silo packs and MIRVs.
- **GUN values:**
  - "Remember the Cant." now comes from a gunner, not the flag officer.
  - The hail goes unanswered.
  - O9 rules out firing with an inhabited world behind the target.
  - The escape pods stay in, and Site 1 is dazzled but never struck.
- **Names and call signs:** consistent throughout (ACTUAL, ASTRID GUNS, EXTENUATING, "Maren's asking for terms"), with L.R.E.F.S. kept for the two lore ships.
