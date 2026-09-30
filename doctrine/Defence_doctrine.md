# Defence doctrine: the Maren system defence

**Status:** phase 1, revised with the user's sign-off answers (see `OPEN_QUESTIONS.md`); awaiting the final OK. **Scope:** the force that holds the system the LREF must break in *Operation Tidebreak*.

**Names (decided at sign-off):** the planet **Maren**, its moon **Skerry**, the debris ring **the Breakers**, the monitor ***Breakwater***, and the defending faction, **the Maren Compact**. Its system defence is run by Maren Defence Command (MDC). They replace the draft's Harrow, Kest, the Shoals and *Bastion*.

**Labels:** **[H-nn]** is a production assumption about the defender (register in §11). **WN §n** points to `doctrine/working_numbers.md`. **[Lore]** is JCB's posts, which describe only the GUN side; nothing in them constrains the defender except the shared physics and the general rules of ship design (warp rings, impact shields, radiators).

**Rule IDs:** HO = offensive, HD = defensive. HO1–HO6 and HD1–HD6 keep the draft's numbering; new rules follow on.

---

## 1. Mission and the defender's bargain

**Mission:** deny an attacker orbital control of Maren, keep its population and its foundries safe, and make any assault cost more than it can win: in ships, in magazines, and in time far from its tender.

**Who they are [H-01, decided].** The Maren Compact is a human splinter faction that broke from the GUN and allied itself with the AI. Artificial intelligence was outlawed after it first went rogue; a later government licensed Charon Innovations to try again, and it went rogue a second time, in the Charon Innovations incident [User]. Maren is a manufacturing world, and its foundries now arm the AI. Humans crew *Breakwater* and the laser sites; the AI runs the drones, the hidden emplacements and the foundries. The lore's extrasolar wars are the precedent for humans fighting the GUN (the dreadnought was built for "the final extrasolar war" [Lore]). Four things follow:
- **The same technology base.** The same four weapon families, the same physics, the same kind of ships, so the two doctrines are symmetric.
- **It knows LREF doctrine.** Its officers read the same manuals, so its doctrine is written against LREF habits: the destroyer net and EMCON (HO9, HD9), the hedgehog pack (HD5, HD10), the shield park (HO8) and the braking burn (HO1).
- **No relief is coming.** It can't wait the LREF out. It has to make the assault cost more than it can win, and it can't afford to lose *Breakwater*.
- **The AI runs what has no crew.** Its drones and emplacements fly and fire on their own, with no link to hijack and no override anyone can use, the Compact's own officers included (HD9).

**The bargain.** The defender cannot out-build a GUN expeditionary fleet ship for ship, and it has no warp fleet at Maren [H-01]. So it doesn't fight fleet against fleet in open space. It turns the whole system into the weapon:
- **ground the attacker has to cross;**
- **clocks the attacker has to beat:** heat sinks, magazines, crew endurance;
- **one moment the attacker can't avoid:** the braking burn toward the planet.

## 2. The defender's advantages, and how the doctrine uses them

| Advantage | What it gives | Rules |
|---|---|---|
| **Prepared, surveyed ground** | Every rock in the Breakers is catalogued, with precise orbits, pre-computed firing tables and pre-dug hides. Lanes are pre-registered for the mass driver. | HO2, HO3, HD3, HD8 |
| **Cold, hidden assets** | Emplacements buried at rock temperature are indistinguishable from the 10⁶ rocks around them until they move or fire (WN §5). | HO2, HD3 |
| **No need to decelerate** | Everything the defender owns is already at rest in the battle's frame. Its frigates keep their whole Δv for fighting; the attacker has to spend hours of burn just to arrive. | HO1, HO6 |
| **Interior lines** | Frigates, drones and Breakwater's guns shift between threatened sectors across tens of thousands of km. The attacker has to cross hundreds of thousands. | HO6, HD4 |
| **Planetary power and cooling** | Ground lasers draw on a planet's grid and dump heat into an ocean and an atmosphere: GW beams with no heat clock. | HO5, HD5 |
| **Supply** | Reloads, repair, fresh drones from Skerry's factory, fresh crews. The attacker's resupply sits at a parked tender ~450,000 km away. | HD6, HO8 |
| **Big, cheap sensors** | Ground telescopes can have 30 m apertures and unlimited cooling. They track every hot LREF hull from Maren's surface (WN §5). | HD1, HO7 |

## 3. The attacker's constraints, and how the doctrine exploits them

| Constraint | Why it binds | Exploited by |
|---|---|---|
| **It is seen on arrival** | Warp flash; a drive plume visible across the system; a cold hull visible to ~0.9 AU (WN §5) | Picket and ground telescopes track it from the first second (HD1) |
| **It must exit outside the debris line** | No bubble inside the Breakers (LREF A-02) | The Breakers and the polar gates shape its approach (HD8) |
| **It must cross ~400,000 km on drives** | 4.6–6.3 h at a 20–30 km/s cruise (WN §6) | Time for the mass driver to cast smart rocks into its lanes (HO3), for drones to wake (HO4), for emplacements to be ready (HO2) |
| **It must brake toward Maren** | The braking burn points its stern, drive and radiators at the planet, and turns its bow guns away. Throttling moves it only along the line of fire, so only 0.1 g of RCS moves it sideways. | The kinetic window (HO1): Breakers platforms and Breakwater fire inside the end-on no-escape range, ~500–1,000 km (WN §2) |
| **Finite magazines and heat** | Endeavor: ~24 min of full combat dark on its sink (WN §4) | Make it spend: decoys, drones, fake emplacements (HD2, HD6); keep it inside laser range; kill its fins (HO7) |
| **Far from its tender; shields parked** | Repairs, reloads and the way home are all at the warp exit | Threaten the park (HO8); make every hour cost it more than the defender |
| **Its fleet runs on a network** | The destroyers carry fire control and EW | Hunt the destroyers first (HO9) |

## 4. The ground: Maren system reference geometry

These are working values [H-02 … H-08]. They make the doctrine concrete and fix the geometry the storyboard will use.

| Feature | Working value | Why it matters |
|---|---|---|
| **Maren** | Earth-like: radius 6,400 km, 24 h day, atmosphere and weather, populated | Ground lasers limited by horizon, weather and air; no nuclear fire near its surface on either side |
| **Laser sites 1–4** | Four high-altitude sites, 90° apart in longitude on low latitudes; each 2 GW, 10 m, 1.06 µm (WN §1) | Each site sees only the half of the sky above its horizon (lethal above ~20° elevation) and only through clear air |
| **Breakwater** | Synchronous orbit (42,000 km from Maren's centre), parked above Site 1 | Permanently inside Site 1's umbrella, and always roughly overhead for it |
| **The inner ring** | 12 emplacements along Breakwater's orbit (railgun platforms and PD stations), 30° apart, so ~21,800 km from each other | Sensor pickets and fire bases along the synchronous belt, each defending its own sector. They are too far apart to thicken Breakwater's own PD; that wall is Breakwater's and Site 1's |
| **The Breakers** | A debris torus 120,000–260,000 km from Maren, spread ±25° about its equator. ~10⁶ bodies ≥ 100 m, up to ~20 km across; mean spacing ~500–700 km. A faint dust haze. | The belt the user asked for (§4.1). Warp debris line; hides for emplacements and drones; IR clutter; a laser haze |
| **The polar gates** | Cones over Maren's poles, clear of the torus | The only approach without the Breakers, so pre-registered kill zones (HD8) |
| **Skerry** | Airless moon: radius ~900 km, orbit 380,000 km, period ~27 d, tidally locked | Mass driver, a laser battery with no atmosphere to fight, drone depot and factory, deep observatory. All fixed. |
| **Picket** | ~30 cold passive sensor buoys at 1–5 million km, on laser links | Triangulation and parallax on anything arriving; they watch the LREF's shield park |
| **Warp debris line** | ~300,000 km in the ring plane, ~150,000 km in the gates [H-08] | The attacker exits at ≥ ~450,000 km to also stay outside laser and missile reach |

### 4.1 Why the Breakers is a debris torus, not a classic asteroid field

A natural asteroid belt is almost empty: bodies are typically ~10⁶ km apart. You would never see a second rock in the frame, and a fleet would not need to thread anything. The draft's "tumbling asteroids two to five kilometres across" sliding past the lens is not what a belt looks like.

A **young circumplanetary debris torus** is the densest natural rubble a fleet can realistically meet [H-05]: for example, the wreck of a former moon, broken up within the last few thousand years. Even so, its large bodies are hundreds of km apart. What makes it matter is:

1. **Sensor clutter.** ~10⁶ cold bodies at the same temperature as a buried emplacement. The LREF can radar-map only the rocks near its corridor (the AVPSA sees a 1 m² object at ~180,000 km, WN §5, but the torus holds far too many rocks to map them all).
2. **Fine debris.** Gravel and dust make warp impossible inside it, and make high speed lethal to fins and sensors (WN §6).
3. **Line-of-sight cover.** Anything behind a 10–20 km rock is invisible and unshootable from the other side. Close to a rock, that cover is real.
4. **A dust haze [H-06]** that dims long laser shots (optical depth ~0.1–0.3 over 100,000 km) and adds a warm IR background.

So the realistic "belt fight" is **not threading a dense field**. It is two things:
- crossing a huge, mostly empty volume where any rock might be an emplacement;
- deliberate close passes of *specific* large rocks, used as cover by both sides.

**For the film:** the close-rock shots survive, but each one is a specific rock the story chose, with its own small moonlets and rubble.

---

## 5. Force structure

| Element | Composition [H-10 … H-19] | Role |
|---|---|---|
| **Breakwater** (system-defence monitor) | ~1,800 m, **warpless**: no warp rings, no impact shield, no hab ring (crew on rotation from the planet).<br>The mass a warship spends on those goes into a ~2 m armour belt, a battleship-grade reactor and large armoured louvred radiators.<br>6 twin heavy railgun turrets (50 kg at 30 km/s); 24 PD lasers (2 m, 10 MW); 40 CIWS; 64 missile cells.<br>0.05 g drive, ~2 km/s Δv. | The anchor. Holds synchronous orbit over Site 1, inside the ring and the laser umbrella. It never leaves. |
| **Inner ring** | 12 orbital emplacements: 6 railgun platforms (25 kg at 25 km/s), 6 PD stations, 30° apart | Sector defence and sensors along the orbit; a threat only to ships that come close |
| **Mobile squadron** | 3 frigates (~350 m, 2 g; coilgun and missiles); 6 picket corvettes (4 g); 2 crewed drone-control craft | Flank attacks from cover; drone control; chase stragglers |
| **Breakers garrison** | ~40 emplacements on catalogued rocks: 20 missile pods (24 missiles each), 8 railgun platforms (10-slug salvos), 6 sensor posts, 6 decoy and EW emitters.<br>Minefields of nuclear proximity mines (100 kt–1 Mt) and pellet dispensers.<br>~300 drones parked cold in hides. | Bleed the attacker across the whole crossing |
| **Skerry complex** | Mass driver: 3 fixed tracks, ~40 km long, 10 t smart rocks at up to 15.5 km/s, one per track per ~10 min.<br>Laser battery: 2 × 1 GW, 8 m, 530 nm, airless (WN §1).<br>Drone depot and factory (~500 drones); deep observatory; buried command post. | Casts nets into lanes (HO3); burns fins at long range (HO5, HO7); builds drones |
| **Maren surface** | Laser Sites 1–4; 30 m-class observatories; buried MDC headquarters on fibre | The wall (HD5); the picture (HD1) |
| **Picket** | ~30 passive sensor buoys | Early warning, triangulation, park watch |
| **EW** | Jamming stations on Skerry and in the Breakers; decoy emitters that mimic frigates in IR and radar; hard, air-gapped command nets | Blind and spoof the attacker; resist its intrusion (HD9) |

**Draft changes:**
- Skerry gains a laser battery: an airless moon is the best laser site in the system.
- The drones are parked in the Breakers rather than launched from Skerry during the fight. A drone from Skerry needs over an hour to reach the Breakers (WN §3).
- "Fighters" become mostly uncrewed drones plus two crewed control craft. Crewed fighters are in decline across the setting [Lore], and the defender faces the same physics.

---

## 6. The defender's kill chain

| Link | Primary | Backup |
|---|---|---|
| **Sense** | Maren's big ground telescopes, Skerry's observatory, the picket buoys, and Breakwater's arrays. All passive; radar only from Breakwater and Skerry, in bursts. | The Breakers sensor posts, and each emplacement's own passive sensors |
| **Network** | Buried fibre on Maren and Skerry. Laser links to Breakwater, the ring and the Breakers posts. No radio in combat. | Pre-loaded **autonomous fire plans** in every emplacement: they fire on their own when their triggers are met, and no link can be hijacked if there is none (HD9) |
| **Fire control** | MDC headquarters on Maren | Breakwater; then Skerry |
| **Weapons** | By layer (§8) | — |

The network is the defender's soft spot and it knows it. Everything that can run autonomously does, at the cost of flexibility: an emplacement on an autonomous plan can't be told the target was a decoy.

---

## 7. Rules

### Maren: offensive

| ID | Rule | Detail | Numbers | Change from draft |
|---|---|---|---|---|
| **HO1** | **Strike the committed fleet** | The kinetic window is while the attacker coasts or brakes along the line of fire. Railguns fire **inside the end-on no-escape range**, in salvo patterns, never beyond it. | Breakers platform against an LREF capital ship end-on: 510–920 km (WN §2) | *Was:* "predictable for minutes". *Now:* the braking and coasting phases last hours, but only shots from inside ~1,000 km can hit. That is why platforms are hidden near the attacker's likely corridor. |
| **HO2** | **Cold ambush** | Pods and platforms sit buried at rock temperature. They cold-launch, and missile motors light ~2 km clear. Each fires once and dies, or goes dark and hopes. | Undetectable until it moves or fires (WN §5) | Unchanged. |
| **HO3** | **Cast nets** | The mass driver doesn't snipe: its slugs take hours (100,000 km ≈ 1.8 h at 15.5 km/s, WN §2). It launches smart rocks and canister rounds into the attacker's *predicted* lanes hours ahead, corrected in flight by divert kits, and lets the attacker's own speed do the killing. It can shatter small rocks (up to ~100 m) an attacker hides behind; a large rock it can only ring with canister clouds. | 10 t at 15.5 km/s = 287 t TNT; one per track per ~10 min | *Was:* fires in real time to deny lanes. *Why:* flight times. Keeps the draft's "the moon speaks" shot as a round launched hours earlier. |
| **HO4** | **Swarm the screen** | Drones parked in Breakers hides wake as the fleet passes. They go after fins, sensors and PD mounts with plasma bombs (the lore's "high-yield plasma bombs" delivered up close), kill clouds and decoys. The aim is to make the attacker spend PD and heat. | Drone: 10 g, 30 km/s Δv; Skerry to the Breakers takes > 1 h (WN §3) | *Was:* launched from Skerry's shadow in the fight. *Now:* pre-positioned. |
| **HO5** | **Blind the eye** | Ground and Skerry lasers dazzle the attacker's sensors at any range they can track, and burn fins wherever they show. EW floods radar and spoofs tracks. | Ground site: fin in ~20 s at 100,000 km, ~3 min at 300,000 km; Skerry battery: ~11 s at 100,000 km (WN §1) | *Was:* dazzle only, atmosphere "blunts them for killing". *Now:* the atmosphere costs ~30 %; horizon and weather are the real limits (HD10). |
| **HO6** | **Anvil and hammer** | Breakwater and the ring hold under the laser umbrella. The frigates hammer the flank only from cover (a Breakers rock or Maren's limb) and only against a committed target. | Frigate coilgun against a braking capital ship ≤ ~1,000 km | Adds "from cover only". |
| **HO7** | **Kill the fins** | Radiators are the attacker's weakness: huge, thin, and glowing. Every weapon that can see a fin shoots it first: lasers, pellet clouds, nuclear mines (strip fins to 1–3 km). Then the heat clock does the rest. | Fin 20 MJ/m² against hull 20 GJ/m² (WN §1); Endeavor dark ~24 min (WN §4) | New. |
| **HO8** | **Threaten the park** | If it's cheap, send drones or a corvette toward the LREF's shield park and tender. The goal isn't to win; it's to make the LREF split its screen. | The park is ~450,000 km out: a drone run takes hours (WN §3) | New, from lore ("enemy sorties targeting the detached shields"). |
| **HO9** | **Kill the net** | Hunt the ECW destroyers first. They carry the attacker's fire control and EW, and they must sit where their drones and links reach. | — | New. Fits the draft's "first loss" being a destroyer. |

### Maren: defensive

| ID | Rule | Detail | Numbers | Change from draft |
|---|---|---|---|---|
| **HD1** | **Depth** | The attacker bleeds at every layer, from the outside in: picket, the gates or the Breakers (mines, pods, platforms, drones), the Skerry complex, the inner ring, Breakwater, and the ground lasers. | Layer ranges in §8 | Adds the picket and Skerry; the planetary lasers are now the inner wall. |
| **HD2** | **Decoys everywhere** | Thermal and radar emitters mimic frigates; the real ships hide among them. | Each decoy engaged costs the attacker 0.5–2 s of laser time or a missile (WN §8) | Unchanged. |
| **HD3** | **Hide in clutter** | Use the Breakers, Skerry's far side and Maren's limb. Keep everything at the temperature of its surroundings. | A 300 K frigate is visible at ~0.4 AU against open sky (WN §5), but not against a warm dusty background | Adds rock-temperature discipline. |
| **HD4** | **Trade space for time** | Fall back toward the ground lasers and Breakwater. Make the attacker come through the kill zone at the end of its heat clock. | — | Unchanged. |
| **HD5** | **The wall is strongest where the sky is clear** | Breakwater's PD lasers and CIWS stop tens of missiles a wave. The ground sites stop hundreds, but only when they can see the wave side-on. Keep Breakwater over Site 1 so the two always work together. | Per wave: Breakwater ~10–360; four ground sites ~60–970, depending on aspect and speed (WN §8) | *Was:* "PD wall, can be saturated but not slipped past". *Now:* it can be slipped past, by geometry (LREF O9). |
| **HD6** | **Spend the cheap things** | Pods, mines, drones and decoys exist to drain the attacker's missiles, heat and time. | — | Unchanged. |
| **HD7** | **Never hold still** | Breakwater random-walks within its slot and never lets the attacker's heavy guns get inside its no-escape range while its drive works. | Spinal against Breakwater: no-escape 3,600–4,800 km at 0.05 g; 11,000–14,700 km if its drive is crippled (WN §2) | New. Makes the LREF cripple before killing (LREF O10). |
| **HD8** | **Shape the approach** | The Breakers and the polar gates leave the attacker two ways in. The gates are clear, closer and pre-registered: seeded with sand and mines, covered by the mass driver and lasers. The Breakers look cheaper; make them cost the same, spread over hours. | Gate warp line ~150,000 km against ~300,000 km in the ring plane [H-08] | New. |
| **HD9** | **Hard nets** | Air-gapped fire control; buried fibre; authenticated laser links; no radio. The AI runs the emplacements and drones on pre-loaded autonomous behaviour with no remote override: nobody can order them to stand down, the Compact included. The ECW destroyers can't hijack what has no receiver: "return to sender" works only on drones with links. | — | New. Answers the lore's destroyer threat. |
| **HD10** | **Weather and horizon** | A ground site covers only the sky above its horizon, and only through clear air. Four dispersed sites, and Skerry's battery, cover each other's gaps. Weather is forecast into the fire plan. | Lethal above ~20° elevation [H-12] | New. |

---

## 8. Engagement envelopes (defender)

| System | Working numbers | Effective against | Time to effect | Best use | Beaten by |
|---|---|---|---|---|---|
| **Ground laser site** (×4) | 10 m, 1.06 µm, 2 GW, 70 % through air | Dazzle: any tracked range. Fins: ≤ ~100,000 km (~20 s), ~300,000 km (~3 min). Missiles side-on: ≤ ~100,000 km (~30 s). Missile noses: ≤ ~10,000 km (~50 s). | Light-speed; burn times as listed | The wall around Maren | Horizon, cloud, smoke screens, nose-on geometry |
| **Skerry battery** (×2) | 8 m, 530 nm, 1 GW, airless | Fins ≤ ~100,000 km (~11 s), ≤ ~300,000 km (~1.7 min) | As above | Fin-killing across the approach | Skerry's own horizon; the spinal cannon (it is fixed) |
| **Breakwater heavy railgun** (6 twin) | 50 kg at 30 km/s (5.4 t TNT) | LREF capital ship end-on ≤ 615–1,020 km; broadside ≤ 1,220–2,040 km; frigate ≤ 230–380 km | 1,000 km in ~33 s | A committed, braking attacker | Jinking, range, off-axis braking |
| **Breakwater PD** | 24 lasers (2 m, 10 MW), 40 CIWS | Per wave: ~160–360 side-on, ~10–20 nose-on; CIWS ~7 missiles/s of arrival spread | — | Close missile defence | Time on target, nose-on hardened missiles, Casaba standoff |
| **Breakers railgun platform** (8) | 10 kg at 25 km/s, 10-slug salvo, fires once | Capital ship end-on ≤ 510–920 km | 1,000 km in 22–40 s | The kinetic window (HO1) | Unknown until it fires; dies after |
| **Breakers missile pod** (20) | 24 missiles each: 40 g, 40 km/s Δv | Out to ~100,000 km (~1 h flight) | 10,000 km in ~6 min | Cold flank attack | LREF PD; the pods reveal themselves by launching |
| **Nuclear proximity mine** | 100 kt–1 Mt | Fins and sensors ≤ 1–3 km; hull ≤ 30–110 m (WN §7) | Instant | Stripping fins in the lanes | Sweeping ahead; spacing; lanes the defender didn't expect |
| **Pellet dispenser / canister round** | 10⁵ pellets of 10–100 g | Anything with fins out; energy set by the attacker's speed (1 kg at 20 km/s = 48 kg TNT, WN §6) | — | Area denial in lanes | Slow crossing speed, PD sweeping, luck |
| **Skerry mass driver** | 10 t at up to 15.5 km/s; smart rock (~1 km/s divert) or canister | Pre-planned lanes; canister clouds across predicted routes | 100,000 km in ~1.8 h | Casting nets (HO3) | Changing lanes after launch; killing the tracks (they're fixed) |
| **Strike drone** (~800) | 10 g, 30 km/s Δv; plasma bomb or kill-cloud payload | Close range: fins, sensors, PD mounts | Pre-positioned | Spending the attacker's PD and heat (HO4) | Corvette screens; hijack where linked |
| **Frigate** (3) | Coilgun (20 kg at 20 km/s) and missiles; 2 g | Committed targets ≤ ~1,000 km, from cover | — | Flank hammer (HO6) | The LREF's gun frigate; exposure outside cover |

---

## 9. The defender's plan at Maren (how the rules would play)

This is the defender's side of the scenario the storyboard will use in phase 2. Times are real mission time from the warp flash.

1. **T+0: the flash.** Seen within ~1.5 s (WN §5). The picket and ground telescopes fix the fleet's position and composition from its heat. Everything in the Breakers stays cold. Breakwater begins its random walk (HD7).
2. **T+0 to ~1 h: reading the approach.** The fleet forms up at ~450,000 km and parks its shields. MDC reads the likely route (the Breakers or a gate) from its first burn. Skerry starts casting smart rocks into the predicted Breakers lanes; they are hours in flight and corrected later (HO3).
3. **~1–4 h: the Breakers.** The crossing takes hours at a controlled 20–30 km/s. Pods and platforms fire only inside their no-escape range (HO1, HO2). Drones wake as the fleet passes (HO4). Mines and pellets work the lanes. The ground and Skerry lasers dazzle constantly and burn any fin that shows (HO5, HO7). The destroyers are the priority target (HO9).
4. **~4–6 h: the braking burn.** The fleet flips and brakes toward Breakwater's orbit. This is the window Breakwater, the ring and the frigates have waited for (HO1, HO6), inside the full laser umbrella, at the end of the attacker's heat clock (HD4).

**The LREF's counter** (see `LREF_doctrine.md`) is aimed at exactly these points:
- slow, swept crossings (O8);
- cutting the defender's links so emplacements fall back to rigid autonomous plans (O5);
- attacking from the laser shadow, nose-on (O9);
- braking late and off-axis (O13);
- crippling Breakwater's drive before the spinal shot (O10).

**The defender's weaknesses**, stated plainly so the storyboard doesn't make it stupid:
- Its fixed installations can't dodge. The Skerry mass-driver tracks and laser battery are ideal spinal-cannon targets.
- Its emplacements fire once.
- Its ground lasers see only half the sky and no cloud.
- Breakwater can't leave the umbrella.
- Its autonomy makes it rigid once its network is cut.
- It fights next to its own population.

---

## 10. What the defender avoids

- **Sortieing into open space** against the LREF's capital ships. Its frigates are no match beyond the umbrella.
- **Revealing emplacements early,** or firing them outside their no-escape range: a wasted shot and a lost hide.
- **Radiating.** Emplacements stay cold, radio stays silent, and drones stay dormant until they are used.
- **Chasing feints.** The LREF's decoys and drones exist to draw fire.
- **Letting Breakwater leave Site 1's umbrella,** or letting it hold still inside the attacker's no-escape range.
- **Committing all its drones in the first hour.**
- **Nuclear fire near Maren's atmosphere.** Mines and warheads stay in the Breakers and beyond. A high-altitude burst over its own population would do the attacker's work for it.

---

## 11. Assumption register (defender)

| ID | Assumption | Note |
|---|---|---|
| H-01 ★ | The Maren Compact is a human splinter faction allied with the AI, holding the manufacturing world of Maren, with no warp fleet at Maren and no relief coming; the system defence must hold alone. Humans crew *Breakwater* and the sites; the AI runs the drones, emplacements and foundries | Decided at sign-off (`OPEN_QUESTIONS.md` Q1); the AI alliance and the Charon Innovations incident added by the user in phase 2 |
| H-02 | Maren is Earth-like: 6,400 km radius, 24 h day, populated | Matches the existing planet shader [Model] |
| H-03 | Four ground laser sites, 90° apart in longitude; 2 GW, 10 m, 1.06 µm; 70 % atmospheric transmission | Grid-powered, ocean-cooled |
| H-04 | Breakwater sits in synchronous orbit (42,000 km) above Site 1 | Keeps the monitor inside a laser umbrella at all times |
| H-05 ★ | The Breakers is a young circumplanetary debris torus, 120,000–260,000 km, ±25° about the equator | Decided at sign-off (`OPEN_QUESTIONS.md` Q2): the realistic version of the asteroid belt the user asked for |
| H-06 | A dust haze in the Breakers: optical depth ~0.1–0.3 over 100,000 km | Soft-coat value; gives the LREF a reason to prefer the Breakers |
| H-07 | Skerry: airless, radius ~900 km, orbit 380,000 km, tidally locked | Like Earth's Moon, but smaller |
| H-08 | Warp debris line ~300,000 km in the ring plane, ~150,000 km in the polar gates | Follows from LREF A-02 |
| H-10 | Breakwater: ~1,800 m, warpless, ~2 m belt, 6 twin heavy railguns, 24 PD lasers, 40 CIWS, 64 cells, 0.05 g | A 2 m belt shrinks a 100 kt Casaba's breach standoff to ~2.5 km |
| H-11 | Inner ring: 12 emplacements (6 railgun, 6 PD) | — |
| H-12 | Ground lasers are lethal only above ~20° elevation | Thick air and turbulence near the horizon |
| H-13 | Breakers garrison: 20 pods × 24 missiles, 8 railgun platforms, 6 sensor posts, 6 decoy/EW emitters, nuclear and pellet mines, ~300 drones | — |
| H-14 | Skerry mass driver: 3 fixed tracks, 10 t at up to 15.5 km/s (throw speed set per salvo), smart-rock divert ~1 km/s, one launch per track per ~10 min. Raised from 10 km/s after the round 1 physics review and to 15.5 km/s after round 2, so salvos thrown from T+0:04 to T+0:54 reach the fleet's final lane on time. | Fixed tracks limit its sky coverage; divert kits fill the gaps |
| H-15 | Skerry laser battery: 2 × 1 GW, 8 m, 530 nm | The airless site a sensible defender would use |
| H-16 | Frigates: ~350 m, 2 g, coilgun 20 kg at 20 km/s, missiles; corvettes 4 g | — |
| H-17 | ~800 drones in total (≈300 in the Breakers, ≈500 at Skerry): 10 g, 30 km/s Δv, plasma-bomb or kill-cloud payloads | — |
| H-18 | The defender's combat nets are air-gapped and fibre- or laser-linked; emplacements run pre-loaded autonomous fire plans | The physical answer to the lore's ECW destroyers |
| H-19 | Picket: ~30 cold buoys at 1–5 million km | — |
