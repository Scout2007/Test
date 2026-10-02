# Round 5 review: military doctrine and tactics

Revision 5 (commit bcc0994), read from the frozen checkout. Shots are cited by title.

## Verdict

**No major issues.** All four round 4 issues are resolved. The new material is doctrinally sound: the traffic reads as a fleet net, the fire plan states the plan in a crew's words, the AI lore lands where HD9 says it should, and the eclipse helps the attack rather than hurting it. Two minor issues remain, both about words and settings rather than beats:
- *Blind it* puts full array power on Site 1, which goes past dazzle into the fire the report's own restriction forbids.
- The fire plan's order leaves the Pillar of Autumn out, so "Everyone else, on me" takes the reserve along.

## Round 4 issues: status

| Round 4 issue | Status | Note |
|---|---|---|
| 1. [MINOR] The spend wave can't "die against" the PD | Resolved | It is mostly decoy, EW and kill-cloud birds, with warheads fused to burst 1–3 km out. *The spend wave* shows the bursts, *Wall of fire* meets "a wall thinned by the spend wave", and the odds row is now a floor. One count still needs reconciling (issue 3). |
| 2. [MINOR] Decoys must match the killers through the boost and be steered with them | Resolved | O3 now requires one 30 g boost and decoys matched in plume, size and signature ("by launch, boost, speed or signature"). MSL-V carries a matched motor, the net ship steers the whole wave, and the line is "Kill wave steering clear." |
| 3. [MINOR] Skerry's clouds aimed at the rock | Resolved | The clouds are steered onto the pack's slot in their last hour (~40 m/s). The pack watches the burns and slides 20 km down the shadow: "Skerry's last salvo, wide!" |
| 4. [NIT] The waves' backup guidance | Resolved | *Sixty-four* shows "BACKUP: ASTRID DIRECT", and Actual says "If she drops, the waves are yours." |

## Issues, ranked

### 1. [MINOR] *Blind it* puts full array power on Site 1 (*Blind it*, *Restrictions*)
- **Problem:**
  - The report's fourth card reads "No fire was to fall on the planet's surface, its laser sites included." Its own action note adds: "The fleet may blind the planet's lasers, never fire on them."
  - *Blind it* then takes the arrays "from low power to full on Breakwater's optics and Site 1's trackers", over the line "Arrays on Site One. Dazzle only."
  - The picture and the rig say full power, and the words say dazzle, so a viewer who has just read the restriction sees the fleet turn its lasers on the planet.
- **Evidence:**
  - Dazzle needs ~10 W/m² (WN §1). From the escorts' stop, ~43,600 km from Site 1, a full-power array puts ~93 kW/m² on a ~17 m spot above the air: about 70 suns and ~9,000 times the dazzle level. That is a burn, on the surface, of a populated world.
  - §7 treats dazzle as EW, which Q6 allows. That covers the low setting the fleet has held since T+5:43 (under ~1 % of power, KEY_NUMBERS), not full power.
- **Fix:**
  - Put full power on Breakwater's optics, which are in orbit and are the ones that matter for the kill wave's last minutes (O5).
  - Leave Site 1 at the dazzle setting it has had all along.
  - Line: "Arrays on Breakwater, full power. Site One, dazzle only." Split the rig to match (Breakwater's bearing 0.2→1; Site 1 held).
  - The card could say it too, if reading time allows: "…its laser sites included; they were to be blinded, not struck."

### 2. [MINOR] The fire plan leaves out the Pillar of Autumn (*The fire plan*)
- **Problem:** "Infinity, Galactica: fire from here. Donnager, Wallfish: guard them. Everyone else, on me." That order names only the two firing frigates. As given, it sends the reserve hedgehog (~720 missiles, 4 CIWS) with the fleet into Site 1's sky and the braking window.
  - Everything else puts the Pillar at Anchor: FLEET ("The pack stays at Anchor as a fire base"), KEY_NUMBERS ("~720 on the Pillar" in reserve), and *Kill wave away*, which opens on its shut pods across Anchor's shadow.
  - A crew would query this order, and a viewer who watches the Pillar's pods at Anchor two shots later sees the order broken.
- **Evidence:** O11 (hold the reserve; hedgehogs stay with the pack under guard); D11 (the fire base's guard covers the pack).
- **Fix:** One clause keeps the cold read's clarity. "Infinity, Galactica: fire from here. Pillar holds with them. Donnager, Wallfish: guard them. Everyone else, on me." Or "Pack: fire from here, Pillar in reserve."

### 3. [NIT] Procedure and wording in the traffic
- ***Rings cool* (T+0:00:06):** "All Tidebreak, Actual. Report exit." comes before the Astrid has left warp; it is among the later flashes in *The task group* (T+0:00:10 on). Move Actual's call into *The task group* after the Astrid's flash, and let the Endeavor report first.
- ***The net*:** Every other fleet-wide order is addressed ("All Tidebreak, execute."), but "Come left two degrees." has no addressee. Make it "All Tidebreak, come left two degrees."
- ***The spend wave*:** "Her guns are firing" contradicts *The anvil*'s "turrets track but stay silent". What is lit is her point defence, which is what the kill wave steers round, so say "Her point defence is lit. Kill wave steering clear."
- **The spend wave's warheads:** PHASES and *The spend wave* say "a few dozen warheads". KEY_NUMBERS says "~90 killers fused to burst 1–3 km out", which puts ~80 at Breakwater. Pick one number; either way the stripping and the whole hull still hold.
- **The ring after the terms:** Say who runs it. If it is AI-run like the other uncrewed emplacements, it "doesn't answer" to the Compact either, and is still live ~22,000 km off when the Endeavor's fins come out in *Hold*. Either add it to the terms, or accept it knowingly: ring PD would need minutes of dwell at that range, and the sink leaves no choice.

### 4. [NIT] Make the eclipse the planners' choice (*The fire plan*)
- **Problem:** The eclipse is a lighting pick, but O9 says "time strikes to planetary rotation", and this one pays. Breakwater sits in Maren's umbra for ~70 minutes (T+6:47:41–7:57:20, about the longest a synchronous orbit gets near equinox), and the kill wave, the Casabas and the spinal shot all land inside it.
  - In the dark the defender's optics lose reflected light: no glints to tell a shroud from a real body, and no sunlit silhouettes of cold birds. The decoys only have to match heat and radar.
- **Fix:** One label on the plan: "BREAKWATER IN SHADOW 6:47–7:55". The viewer then learns the fleet chose the dark, and the sunrise in *The wait* becomes the clock running out on it.

## What works

- **The traffic sounds like a fleet net.**
  - The called station comes first ("Infinity, Actual. Wave one. Fire."), orders are acknowledged ("Endeavor, burning."), and reports carry counts and ranges ("Launch, four hundred klicks!", "Vampires, sixty-four!").
  - Brevity is used the way crews use it: vampires for inbound missiles, a leaker for one that got through, splash, no beacons, "Solution. Firing.", "Round away. Time of flight two forty-nine.", terminal.
  - Each call comes from the ship that would see it: the Astrid's watch calls the launches and the sixty-four; the Donnager calls what it is guarding; the Extenuating calls the cloud its drones light and the wave it steers.
- **The fire plan is the plan in three lines:** who fires and who guards, what each wave is for, and O10's cripple-then-kill ("Once she can't move, Astrid takes the kill").
- **"If she drops, the waves are yours."** gives Breakwater's one sensible strike (HO9) a stake and a visible answer.
- **The AI lore lands where the doctrine says.** The hijack stops at the links ("The rest are AI-run, no links. Can't touch those."). The Compact can't stand the AI's guns down, so the terms take the charts. "T-SEC, you're next" leaves the AI as the unfinished business it is. The hail, the silence and "No response. Astrid, fire." are lawful procedure against a ship whose turrets still track.
- **The eclipse costs the plan nothing.** The spend wave's clouds and decoys run on the kill wave's axis at its speed, 90 s (~4,000 km) ahead, so there is no fratricide. The kill falls in the dark and the slug lands in Breakwater's sunrise.
- **The report frame fits the doctrine.** "Laser-link traffic" as a source matches EMCON (A-29), and the one open-channel call is the hail.
