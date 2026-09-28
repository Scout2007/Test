# LREF doctrine: the Expeditionary Response Element in a system assault

**Status:** phase 1 draft, for sign-off. **Scope:** how an LREF task group fights its way into a defended star system, written for the *Operation Tidebreak* film but general enough to reuse.

**How to read the labels:**
- **[Lore]**: stated in JCB's posts (`pack/lore/WPAtaMS_LREF_lore_posts.md`).
- **[Model]**: already built in the Blender project (`pack/project_docs/`).
- **[A-nn]**: a *production assumption*: the lore is silent, so this extends it from physics. Every assumption is listed in §14 and the ones you may want to overrule are also in `OPEN_QUESTIONS.md`.
- **WN §n** points to section n of `doctrine/working_numbers.md`. `working_numbers.py` generates that file, so every figure can be re-derived. A bare **§n** is a section of this document.
- **Rule IDs:** O = offensive, D = defensive. O1–O7 and D1–D7 keep the draft's numbering so the storyboard's citations still line up; where a rule changed, the table says how and why.

The setting is "a soft sci-fi setting wearing a hard sci-fi coat" [Lore]. So the soft parts (warp, plasma lances, ECW that can reach into a ship's systems) are taken as given, and everything that happens at sublight is held to real physics: momentum, light-lag, diffraction, heat.

---

## 1. The problem the doctrine solves

An LREF task group arrives by warp at a world it does not own. Everything else follows from five facts:

1. **It is seen the moment it arrives.** The warp-exit flash, the drive plumes and even a cold 300 K hull are visible to infrared sensors across the system (WN §5: a dark Endeavor is detectable at about 0.9 AU; its drive at 1 g, across the whole system). There is no stealth for a crewed warship in space. What *can* be hidden is intent: which ship is which, where it will be in ten minutes, and what it will shoot at.
2. **It must cross the last few hundred thousand kilometres on its drives.** A bubble cannot be formed or collapsed inside a system's debris [Lore: bunny-hopping because of debris; A-01, A-02]. At Harrow that means a 4–6 hour approach (WN §6).
3. **It arrives with only what it brought.** Magazines, drones, heat-sink capacity and spare radiators are finite, and the tender is back at the warp exit.
4. **It must eventually brake.** A braking ship points its drive, reactor and radiators at the enemy and its forward guns away (§10).
5. **The defender chose the ground.** Every rock in the belt has been surveyed, every lane pre-registered, and the planet's lasers have unlimited power and cooling.

So the LREF fights for three things: **the picture** (see first, and deny the enemy a clean one), **tempo** (strike at the moments it chooses, faster than the defender can adapt), and **heat** (it can only fight dark for tens of minutes).

---

## 2. Force structure and roles by class

The task group for *Tidebreak*, compared with the draft:

| Ship | Class | Count | Draft | Why changed |
|---|---|---|---|---|
| L.R.E.F.S. **Astrid** | Hanuman heavy cruiser (SCC) | 1 | 1 | — |
| L.R.E.F.S. **Endeavor** | Ryland cruiser (MRV) | 1 | 1 | — |
| Garibaldi-Ivanova, **hedgehog (MAV)** configuration | Frigate | **3** | 1 | Lore: "a sole MAV frigate is more than likely insufficient… hedgehogs operate in packs." Three is the smallest pack that can saturate Bastion (see §5). |
| Garibaldi-Ivanova, **gun** configuration | Frigate | 1 | 1 | — |
| Garibaldi-Ivanova, **PD** configuration | Frigate | **1** | 0 | Guards the tender and the shield park (D11). The lore lists the PD fit ("lasers, bulletstorm CIWS, kinetic kill clouds"). |
| ECW destroyer | Destroyer | 2 | 2 | — |
| Corvette | Corvette | 4 | 4 | — |
| Fleet **tender** | Auxiliary | **1** | 0 | Lore: "there WILL be tenders somewhere in the backline." It holds the spare shields and reloads. It can stay off-screen or distant. |
| Drones | Picket, decoy, PD, EW | ~200 | "some" | Roles in §6–7. |

All the frigates are one hull with swappable modules [Lore], so the extra frigates are instances of one asset. Whether to add them is your call (`OPEN_QUESTIONS.md` Q3).

### Roles by class

**Corvettes (50–150 m) [Lore].** Anti-drone and anti-strike-craft screen, and harassment. They are fast and agile (A-10: 4 g, flip in ~8 s at 3 g at the ends, WN §6), with weapons heavier than a big ship's PD for dealing with drones and bombers.
- **Tidebreak job:** they ride 500–2,000 km ahead of the line as the outer drone screen (D6), and they sweep the lane with PD fire for loose rock and parked munitions (O8).
- **What they don't do:** they never trade fire with emplacements. They can't carry the armour.

**ECW destroyers (100–225 m; this class ~200 m) [Lore].** No main weapons, only CIWS and a few PD emplacements [Lore]. They carry the fleet's computing, sensors and **network screen** ("capable of silencing the radio-emissions of an entire fleet"), plus drones and satellites for comms, sensor nets and counter-EW [Lore].
- **Kit:** the aft third of the hull is a huge parabolic antenna, which is the ship's eyes and ears once the impact shield is off [Lore].
- **Tidebreak job:** fight the invisible war (§7). Keep the fleet's fire control connected and the defender's disconnected.
- **Vulnerability:** they are the net, so the defender hunts them first. They sit inside the line, behind the corvettes and the frigates' PD.

**Frigates (300–500 m; the Garibaldi-Ivanova is ~400–450 m) [Lore].** "The premier generalist platform." One hull; the module decides the role, and each module locks the ship into a narrow doctrine [Lore]. Modules are swapped at a tender [Lore].
- **Hedgehog (MAV):** ~360 missile pods [Lore]. The typical load is:
  - capital-ship killers in single pods: nuclear, for "mid to backline distances";
  - the back third as multi-silo packs of smaller nuclear missiles, many with MIRVs.

  Once empty it has only **4 CIWS** [Lore], so an empty hedgehog is withdrawn to the tender (O11).
- **Gun:** "4 large kinetic batteries", with the rest of the hull as magazine, for "sustained fire at medium distances, filling in that awkward middle-range gap" [Lore]. At Tidebreak it is the medium-range hammer against emplacements and Harrow's frigates (O4).
- **PD:** lasers, CIWS and kinetic kill clouds [Lore]. It escorts the tender (D11).

**Light cruisers (700–900 m) [Lore].** A frigate with a cruiser powerplant, one weapon type in quantity, and able to carry a plasma lance [Lore]. None in this group.

**Cruiser: L.R.E.F.S. Endeavor (Ryland class, 1,194 m in the model) [Lore, Model].** "The greatest generalist of the fleet": every weapon family at once, and no spinal cannon [Lore].
- **Weapons [Model]:** 6 M-1C twin railcannon turrets (12 guns, ~100 m class [Lore]), 8 laser focusing arrays, 8 PD lasers, 16 CIWS, 4 plasma lances, 16 VLS cells, 6 chaff/flare/smoke launchers, 2 EW jammers, 4 telescoping radiator fins.
- **Tidebreak job:** the line of battle. It is the ship that goes into the Shoals, kills emplacements at close range, and delivers the knife-range blow (O6).
- **Heat:** at full combat it produces ~13.7 GW, more than its fins reject even at 1,200 K (WN §4). So it fights in bursts.

**Heavy cruiser: L.R.E.F.S. Astrid (Hanuman class, ~1,600–1,700 m) [Lore].**
- **Spinal cannon [Lore]:** runs the full length (about a kilometre of it is gun). The ship aims by turning its whole hull (§10).
- **Weapons [Lore]:** "more than triple" the Ryland's laser arrays and railgun batteries (so at least 25 arrays and 19 turrets), and dense CIWS and PD lasers.
- **AVPSA [Lore]:** the Articulated Variable Position Sensor Array, a dish ~100 m across.
- **Power and heat [Lore]:** an overpowered reactor and 8 stacked radiator fins that "extend further than the warp ring boundary" (retracted in warp). It "glows in thermals".
- **Weaknesses [Lore]:** manoeuvrability, passive armour, stealth.

What that makes it in doctrine:
- **the fleet's eye:** its radar sees a 1 m² target at ~180,000 km and a railgun slug at ~57,000 km (WN §5);
- **its lighthouse:** it can't hide, so it doesn't try;
- **its PD anchor;**
- **its long-range hammer against anything that can't dodge** (O4).

It stays at the back of the line, well protected and far away, and it closes only for the kill (O10).

**Tender [Lore, A-11].** The fleet support ship. It carries spare impact shields, reload pods, drones, spare radiator segments, fuel and a repair shop. At Tidebreak it holds station at the warp exit with the parked shields (the **shield park**) under the PD frigate and one corvette.

**Command [A-12].** The task group commander flies in the Astrid: it has the picture, the power and the survivability. The Endeavor holds the alternate command. The destroyers carry the network both depend on. The LREF's strategic mobile command centre (the repurposed dreadnought [Lore]) is not present.

**The follow-on force [Lore: T-SEC; A-13].** The operation exists to win orbital control for a T-SEC landing and boarding operation (void assault [Lore]). That is why the LREF must *break* the defence rather than bypass it, and why it cannot simply bombard the planet (see "What the LREF avoids", §13).

---

## 3. The kill chain

Every engagement runs the same four links. The defender's doctrine attacks each one, so each has a backup.

| Link | Primary | Backup | How it fails |
|---|---|---|---|
| **1. Sense** | Astrid AVPSA: passive IR and optical, radar in bursts. Destroyer antennas. Picket drones pushed 5,000–20,000 km ahead. | Every ship's own IR search and track, phased arrays and star trackers [Model]. | Clutter (the Shoals), dazzle (planetary lasers), decoys. |
| **2. Network** | The destroyers' **local network screen**: laser-link mesh, relays and EW drones [Lore]. The fleet is radio-silent. | Direct ship-to-ship laser links; pre-briefed autonomous fire plans. | Jamming, spoofing, a destroyer lost. |
| **3. Fire control** | Fleet-level track fusion on the Astrid and both destroyers: each target is assigned to the best-placed shooter. | Each ship's own fire control from its own sensors. | Late or false tracks; light-lag (1.3 s at 380,000 km, WN §5). |
| **4. Weapons by range band** | See below. | — | Heat, magazines, geometry. |

### Range bands (numbers from WN §1–3 and §7–8)

| Band | Range | What the LREF uses | What it is for |
|---|---|---|---|
| **S** Strategic | > 300,000 km | Sensors; missile launch (1–3 h flights); spinal only at fixed targets and only with long flight times | Picture, first missile wave, shaping |
| **L** Long | 30,000–300,000 km | Missiles in midcourse; spinal at fixed targets (flight 8–80 min); lasers **dazzle only** | Stripping emplacements; blinding |
| **M** Medium | 3,000–30,000 km | Laser arrays kill missiles side-on (≤ ~30,000 km) and burn fins (≤ ~10,000 km); spinal at a crippled monitor (≤ ~11,000–15,000 km); missiles in terminal | The PD battle; the start of the fin war |
| **C** Close | 300–3,000 km | M-1C at a monitor (≤ ~1,500–2,700 km); spinal at a mobile monitor (≤ ~3,600–4,800 km); arrays burn through missile noses (≤ ~1,000 km) | Killing things that are big and slow |
| **K** Knife | < 300 km | M-1C at frigates (≤ ~190–340 km) and corvettes (≤ ~80–150 km); plasma lances (≤ 50 km); PD lasers; CIWS kill clouds (5–30 km); Casaba standoff (2–4 km) | Only where terrain or a crippled target makes it happen (O6) |

---

## 4. Weapon employment by family

The four families [Lore]: kinetics, directed energy, plasma, nuclear. Missiles are a delivery platform, not a family [Lore].

### 4.1 Kinetics: M-1C railcannons and the spinal cannon

**Working numbers [A-20]:**

| Gun | Slug | Muzzle speed | Energy per slug |
|---|---|---|---|
| M-1C (per gun) | 10 kg | 25 km/s | 3.1 GJ (0.75 t TNT) |
| Spinal cannon | 500 kg | 60 km/s | 0.9 TJ (215 t TNT) |

- **Rate of fire (M-1C):** a salvo every few seconds in bursts, as the rig's firing cycle shows [Model], but only one shot per gun every ~15 s *sustained*, because of heat (WN §4).
- **Rate of fire (spinal):** about one shot a minute, limited by capacitor recharge and ~2.3 TJ of heat per shot. On a 60 TJ sink the Astrid can fire ~27 shots dark (WN §4).

**The governing fact is time of flight.** A slug is unguided and can't turn. A target that sees the launch (and the muzzle flash is always seen) only needs to be somewhere else when the slug arrives.
- **The no-escape range (WN §2)** is the distance inside which the target can't move clear in time. Outside it, a single slug is a waste of heat and ammunition.
- **Salvo patterns** stretch it by 2–4×, at the cost of hit probability per slug.

| Target | M-1C no-escape range | Spinal no-escape range |
|---|---|---|
| Capital ship end-on, on RCS only (0.1 g) | 510–920 km | 1,230–1,640 km |
| Capital ship broadside, RCS only | 1,020–1,840 km | 2,450–3,260 km |
| Monitor (0.05 g) | 1,500–2,700 km | 3,600–4,800 km |
| Monitor with its drive crippled (0.005 g) | 4,600–8,300 km | 11,000–14,700 km |
| Frigate (2 g) | 190–340 km | 450–600 km |
| Corvette (4 g) | 80–150 km | 200–260 km |
| **Fixed installation** (a surface site or a rock) | limited only by aim: ~10,000 km | ~100,000 km (flight ~28 min) [A-21] |

The second figure in each range includes 20 km/s of closing speed.

**Doctrine:**
- Kinetics are for **fixed, committed or crippled targets** (O4, O10).
- The **spinal cannon's natural prey** is anything nailed to a rock or a moon: the Kest mass driver, Shoals platforms that have revealed themselves, orbital emplacements. Its other prey is a monitor whose drive has been cut.
- The Astrid must **point its whole hull** to fire (§10). A spinal shot is therefore an event the fleet plans around: the Astrid stops any burn, slews and steadies, then fires.

### 4.2 Directed energy: laser focusing arrays and PD lasers

**Working numbers [A-22]:**
- **Laser focusing array:** 3.3 m aperture, 350 nm UV (matching the violet lens glow the user chose [Model]), 25 MW beam, 75 MW of waste heat while firing.
- **PD laser:** 1.6 m aperture, 5 MW.
- Beams are invisible; only the lens glows [Model].

**The governing fact is diffraction.** The spot grows linearly with range, so intensity falls with range squared (WN §1). One laser therefore does very different jobs at different ranges:

| Job | Laser focusing array | PD laser |
|---|---|---|
| Dazzle a sensor | Any range the target can be tracked (> 10⁶ km) | Same |
| Kill a missile seeker | ~0.6 s at 10,000 km | ~12 s at 10,000 km |
| Burn a radiator fin | ~11 s at 10,000 km; ~5 min at 50,000 km | ~2 s at 1,000 km |
| Kill a missile side-on (spinning) | ~17 s at 10,000 km; 0.2 s at 1,000 km | ~4 s at 1,000 km |
| Burn through a hardened missile nose | ~28 s at 1,000 km; 0.3 s at 100 km | ~6 s at 100 km |
| Melt through a 0.72 m hull belt | ~2 min at 1,000 km, *if* the target doesn't roll | Not practical |

**Doctrine:**
- Lasers **strip; they don't sink.** They kill missiles, seekers, sensors, radiators and PD mounts. They do not kill armoured hulls except at knife range against a target that can't roll.
- **Dazzle is free.** Every array dazzles the enemy's optics at any range where it can be pointed (O5).
- **Fins first.** Against a warship, the laser's best target is its radiators. A ship that loses its fins must stop fighting within tens of minutes (§8).
- **Rotate the duty.** Arrays generate heat even when the guns are silent. The fleet rotates PD duty between ships and between arrays (D3).

### 4.3 Plasma: lances and torpedoes

Lore: plasma "requires an active electromagnetic field to maintain its form lest it just fizzles out". A **torpedo** carries its own field generator; a **lance** uses the ship's field to deliver plasma straight to the target. Plasma weapons are "finicky and specialized" [Lore].

**Working model [A-23]:**
- **Lance:** the lance fires compact magnetised plasma toroids (plasma "smoke rings" that hold their own field for a while). They leave at ~1,000 km/s, so a 40 km shot arrives in 0.04 s, and each carries ~1 GJ.
- **Range:** they hold together for ~50 km before they expand and cool.
- **Torpedo:** a self-propelled field generator that closes to ~50–100 km and fires or becomes one large toroid.

**Doctrine (O12):**
- Plasma is a **knife weapon**, and it is less reliable than nuclear [Lore: "Nuclear is ironically much more commonplace and reliable"].
- **Uses:** an emplacement unmasking at close range in the Shoals; a crippled ship; a frigate that strays inside 50 km.
- It is **never a primary weapon at range**.
- The four nose lances on the Endeavor [Model] fire along its bow, so the ship must point at the target (§10).

### 4.4 Nuclear: Casaba howitzers and conventional warheads

**In vacuum there is no blast wave** (WN §7). A bare burst kills by X-rays that flash the target's surface off.
- **Radiators and sensors:** stripped out to ~1 km (100 kt) or ~3 km (1 Mt).
- **Hulls:** breached only within ~30–110 m.

A **Casaba howitzer** (a nuclear shaped charge) throws ~25 % of its yield into a narrow plasma jet [A-24: 0.01 rad jet]:
- it breaches a 0.72 m hull belt from **~2 km (20 kt) to ~4 km (100 kt)**;
- anything in the jet's path is wrecked out to 50–130 km.

That standoff is its point: it detonates **outside the CIWS kill-cloud zone**, so PD has to kill it earlier (WN §8).

**Doctrine:**
- Capital-ship killers carry Casaba charges for armoured targets. "Teller-device" (thermonuclear) bare warheads go against radiator farms, sensor fields, emplacement clusters and drone swarms.
- **Nuclear ammunition is not fired at the planet's surface** (ROE, §13).
- The LREF expects nuclear mines in the defender's lanes (see `Defence_doctrine.md`) and keeps ships 50+ km apart (D2).

### 4.5 Missiles as a delivery platform

Missiles carry nuclear, Casaba, kinetic (kill-cloud dispensers), decoy and EW payloads [Lore: "a warhead delivery platform"].

**Working numbers [A-25]** (flight times from WN §3, launched from rest):

| Missile | Accel | Δv | 100,000 km | 300,000 km | Arrives at |
|---|---|---|---|---|---|
| Hedgehog capital-ship killer | 30 g | 150 km/s | 18 min | 48 min | ~110 km/s |
| Hedgehog multi-pack missile | 50 g | 60 km/s | 38 min | 1.9 h | ~45 km/s |
| Endeavor VLS precision missile | 40 g | 100 km/s | 24 min | 68 min | ~75 km/s |

A quarter of each missile's Δv is held back for terminal jinking.

- **Design points that matter for doctrine [A-25]:**
  - a hardened ablative nose (the defender's lasers see it head-on);
  - spin in flight (spreads laser heat on the flank);
  - three guidance paths: an on-board seeker, an inertial track, and datalink updates through the destroyer net.
- **Flight times are minutes to hours, not seconds.** The first wave at Tidebreak is launched from the warp exit and arrives long after (O3).
- **The Endeavor's 16 VLS cells** [Model] carry precision missiles: decoy carriers, EW missiles, and Casaba shots for specific targets. The **hedgehogs carry the saturation.**

---

## 5. Saturation economics: hedgehog packs

Lore: saturation is "deploying enough missiles to overwhelm an enemy's missile defense systems to the point where you either deplete their defensive capacity, or manage to break through during that point of saturation". And: "it becomes a matter of time before the economics of war turns in the favor of the side with the ability to sustain the offensive".

**What one wave has to spend (WN §8).** These are the kills each defensive element makes on a single wave. Side-on missiles show a spinning flank; nose-on missiles show a hardened nose.

| Defence | Missiles at 45 km/s, side-on | Missiles at 45 km/s, nose-on | Missiles at 100 km/s, side-on | Missiles at 100 km/s, nose-on |
|---|---|---|---|---|
| Bastion's 24 PD lasers | ~360 | ~20 | ~160 | ~10 |
| Harrow's 4 ground laser sites, *if all see the wave* | ~970 | ~140 | ~440 | ~60 |
| 40 CIWS on Bastion | ~7 kills per second of the wave's arrival spread | | | |

Three conclusions shape the doctrine:

1. **Geometry beats numbers (O9).** Arriving nose-on cuts the lasers' kills 7–17×, and arriving where the planetary sites can't see the wave removes their share entirely. Such a wave needs a fraction of the missiles of one that shows its flanks to four GW-class lasers.
2. **Time on target beats CIWS (O3).** Kill clouds kill a few missiles per second. A wave that arrives within ~1 s is almost untouched by them; one that dribbles in over a minute is shredded.
3. **Decoys are missiles too.** Each decoy the defender engages costs a retarget (0.5–2 s of laser time) and part of a CIWS cloud.

**Pack arithmetic for Bastion [A-26].** One hedgehog carries ~360 pods: ~240 capital-ship killers and ~120 multi-packs of ~4 small missiles each, so **~700 missiles, plus MIRV warheads**.
- **Plan:** two waves of about 400–600 missiles plus decoys each, from a pack of three, with about a third of the magazine held in reserve.
- **Delivered in the laser shadow, nose-on, within a second:** the defence can stop only ~100 of a wave.
- **Delivered in the open against all four ground sites:** the same waves are mostly wasted.

**Wave roles (O3):**
- **Wave 1 spends:** decoys, EW missiles and kinetic kill clouds, with enough real warheads that the defender must answer. It drains PD ammunition and heat, and it **makes the defender reveal** every PD battery and emplacement.
- **Wave 2 kills:** Casaba capital-ship killers, timed to arrive within ~1 s, from the laser shadow, with the fleet's EW peaking as it arrives (O5).

---

## 6. Layered point defence

**Draft D1 revised.** The layers are ordered by range, and each gets the missiles the previous one missed.

| Layer | Range | What it does | Notes |
|---|---|---|---|
| 1. **EW** | Launch to impact | Cuts the missile's datalink, spoofs its seeker, feeds it false tracks | The destroyers' job (§7). A missile without links or a seeker is blind against a jinking target. |
| 2. **Decoys** | 1,000–100,000 km | Drones and decoy missiles that mimic ships in IR and radar; flares for IR seekers | Flares must match a ship's signature, so they are powered decoys, not pyrotechnics [A-27]. |
| 3. **Laser focusing arrays** | 30,000 km in | Kill seekers first, then side-on missiles, then noses inside ~1,000 km | Fleet track fusion assigns each target to the array that sees its flank. |
| 4. **PD lasers** | 5,000 km in | The same, faster retarget, less power | |
| 5. **Chaff and smoke** | Within ~50 km of the ship, for seconds to minutes | Chaff hides the ship from radar; smoke (graphite and metal flake) blocks laser and optical sight lines | Screens in vacuum expand and thin fast, so they are fired just in time and refreshed [A-28]. |
| 6. **CIWS kill clouds** | 5–30 km | Pellet clouds placed on the missile's predicted path; the missile's own speed does the killing (WN §8) | ~3 missiles/s for the Endeavor's 16 mounts. Useless against a Casaba that stands off at 2–4 km. |

**The Casaba rule.** Any missile that could carry a Casaba must be dead before ~10 km. The inner layers exist for the missiles the outer layers were *meant* to let through (the defender's cheap ones), not for the real threat.

**The Astrid** carries more CIWS and PD lasers than anything else in the group [Lore]. It is the PD anchor: the line keeps within ~10,000 km of it so its arrays can cover the others (D2).

---

## 7. Electronic and cyber warfare

Lore gives the destroyers three lines of work:
- a **local network and comms infrastructure**;
- an **active local sensor net**;
- **scrubbing the fleet's chatter** and building network and counter-EW screens.

On top of that they carry offensive ECW: scrambling battle control, spoofing sensors and breaking comms, up to direct infiltration of the enemy's systems. Hijacked drones are the "return to sender" move. A ship can even be driven to self-destruct, but that is "nigh impossible" against an enemy with real countermeasures [Lore].

**What that means physically [A-29]:**
- **EMCON.** The fleet does not use radio. Ships talk by laser link, relayed by the destroyers and their drones.
  - **What it hides:** where each ship is, and which heat source is which.
  - **What it can't hide:** heat.
- **The network screen** is the destroyers and their drones broadcasting masking noise and false emitters around the fleet. The enemy's passive RF sensors learn nothing, and its radar has to burn through.
- **Offensive ECW needs a way in.** Radar and datalinks can be jammed and spoofed at range. Cyber intrusion needs a receiver to talk to: a drone's control link, an emplacement's command link, a relay.
  - Buried fibre on a moon can't be reached. Air-gapped fire control can't be reached.
  - So the realistic targets are **the drones** (many, cheap, remote-controlled: return to sender) and **the links between command and dispersed emplacements** (sever them, and the emplacements fall back to pre-loaded autonomous fire plans).
- **Passive IR can't be jammed.** It is beaten by decoys, flares, smoke and clutter, not by EW.
- **Laser dazzle is the EW of optics.** Every LREF laser dazzles.

**ECW rules:** see O2, O5, D10.

---

## 8. Heat management

Lore: "Heat still needs to go somewhere… the name of the game is radiators, Radiators, and MORE RADIATORS!" All radiators retract in warp. The Astrid glows in thermals.

**Working numbers (WN §4) [A-30, A-31]:**

| | Endeavor | Astrid |
|---|---|---|
| Fin area (measured off the size chart) | ~72,000 m² per face (4 fins) | ~360,000 m² per face (8 fins) |
| Heat rejected at 1,200 K (orange) | ~12 GW | ~61 GW |
| Heat rejected at 1,500 K (bright orange) | ~30 GW | ~150 GW |
| Full-combat heat load | ~13.7 GW | ~25 GW (assumed) |
| Heat sink capacity | 20 TJ (assumed) | 60 TJ (assumed) |
| **Fighting dark at full combat** | **~24 min** | **~40 min** |
| Dark with guns silent (lasers, hotel) | ~91 min | — |
| Cruising dark (hotel only) | ~3.7 h | — |

**Why fins can't just stay out:**
- **They burn.** A fin burns through in ~20 s at 100,000 km under one Harrow ground laser, in ~11 s at 10,000 km under an LREF-class array, and in milliseconds to a pellet cloud.
- **They show.** Fins at 1,200 K are visible at several AU (WN §5).
- **Rules:**
  - inside any enemy laser envelope, fins stay stowed and the ship runs on its sink (D3);
  - fins come out only behind cover (a rock, the planet's limb, the Shoals' dust) or with the threat on the ship's long axis.

**Fins are edge-on along the axis.** The four fins extend radially, in planes that contain the ship's long axis [Model].
- Seen from ahead or astern, all four are edge-on: the least area to a laser or slug, and the least glow toward the enemy.
- Seen broadside, two are face-on.
- So: **fins out means nose-on or tail-on to the threat. Broadsides happen with fins stowed** (O6).

**The emergency dump [A-32].** Open-cycle cooling boils stored water or ammonia and vents it.
- **Capacity:** 1,000 t of water absorbs ~2.3 TJ, about 3 minutes at full combat.
- **Cost:** the white vapour plume is visible.
- **When:** this is what a ship does when it has lost fins and must keep fighting.

**The Astrid's heat budget:** each spinal shot costs ~2.3 TJ, about 37 s of fin rejection. Its overpowered plant [Lore] lets it keep firing, but not dark: after ~27 dark shots its sink is full.

---

## 9. Warp arrival, departure and the impact shield

**From the lore:**
- Bubbles are made and held by **two warp rings**, one at each end [Lore].
- Impacts in warp are possible, hence the **forward impact shield** [Lore]. It protects "at speed and in warp" [Lore, frigate post].
- Radiators and sensor booms **retract** to stay inside the bubble [Lore].
- Every GUN ship warps **independently** [Lore].
- Warp travel is **bunny-hopped** because of debris [Lore; not detailed].
- Shields are **jettisoned before battle** because all the guns point forward, and **collected afterwards**. Tenders carry spares, and enemy sorties against parked shields are a known risk [Lore].
- Only the gold shield launches; **both rings stay** [Model; user decision].

**Production assumptions:**
- **A-01, velocity:** a ship leaves the bubble with the velocity it entered with, relative to the local star. Arrival velocity is set at the last hop point.
- **A-02, the debris line:** a bubble cannot be formed or collapsed inside dense debris. At Harrow this keeps exits outside the Shoals torus: ≥ ~300,000 km in the ring plane.
- **A-03, precision:** exits land within ~1,000 km of the aim point. Ships stagger their exits by seconds and by 50+ km so bubbles don't overlap.
- **A-04, the flash:** bubble collapse makes a flash visible across the system at light speed. The defender knows the fleet has arrived ~1.5 s after it does, at 450,000 km (WN §5).
- **A-05, spool times:** ~3–5 min to spool a bubble; ~5 s to collapse one (the rig's `warp_charge` ramp).
- **A-06, bunny-hop:** jumps are made in legs, because debris met in warp is lethal and unpredictable. Each exit is a chance to scan ahead and re-plot. The final leg into a defended system starts from a staging point outside it.
  - A side effect: if the staging point is light-hours out, the fleet arrives before the light from its staging flash does.
- **A-07, warp without a shield:** possible, but it accepts the impact risk. Only a short hop into pre-surveyed space.

**Doctrine:**
- **Arrival (O1).** Exit slow (near rest relative to the target world), outside the debris line and outside the defender's effective reach. At Harrow that is ~450,000 km: beyond Kest's and the ground lasers' fin-kill envelope, and ≥ 1 h of missile flight from any defender launcher.
- **Draft change:** the draft arrived at ~180 km/s. Braking that away at 1 g takes 5.1 hours over 1.65 million km (WN §6). It also means jettisoned shields fly on at 180 km/s and can never be collected, which contradicts the lore.
- **The shield park.** Shields are released at the exit point, at near-zero velocity, where the tender holds. They are recovered there after the battle. Any ship that needs to leave by warp comes back to the park, or accepts a shieldless short hop (D9).
- **Radiators and booms stow for warp [Lore].** A ship with damaged, jammed-out fins can't warp until they're cut away. That is one more reason fins are consumables (D7).

---

## 10. Newtonian manoeuvre

**Working numbers (WN §6).**
- **180° flips** are limited by what the ship's ends feel [A-33]:
  - at 1 g at the ends: Astrid ~58 s, Endeavor ~49 s, frigate ~29 s, destroyer ~20 s, corvette ~14 s;
  - at 3 g: Astrid ~33 s, Endeavor ~28 s, corvette ~8 s.
- **Aiming slews** are quicker: a 90° slew takes the Astrid ~29 s at 1 g at the ends.
- **Sustained thrust [A-10]:** capital ships 1 g for hours and 2–3 g for minutes; frigates 2 g; corvettes 4 g.

**What flip-and-burn means for a warship:**
- **Accelerating toward the enemy**, the bow faces it: all forward guns bear, the spinal cannon bears, the fins are edge-on.
- **Coasting**, the ship can point anywhere. This is the best fighting attitude.
- **Braking toward the enemy**, the drive, reactor and radiators face it and the bow guns face away. Only the turrets and lasers bear. The spinal can't fire at the target at all without stopping the burn and turning.
- **Braking along the line of fire** also means the ship's big dodge (throttling the main drive) moves it only along the slug's path. That changes *when* a slug arrives, not *whether* it hits. Only RCS (0.1 g) moves the ship sideways, which is why the end-on no-escape ranges in §4.1 are the ones that matter to a braking fleet.

**Doctrine:**
- **O13, brake late and off-axis.** Hold the fighting attitude (coast, bow-on) as long as possible. Brake with the thrust line off the main threat axis, so throttle changes move the ship across the line of fire. Brake when the enemy's long weapons are blinded or busy.
- **D8, never turn your back without cover.** A flip is the most vulnerable minute a ship has: ~30–60 s with its PD geometry changing and its guns swinging away. Flips happen under smoke, EW peaks and escort cover, and never all ships at once.
- **The spinal turn.** The Astrid aims by turning. Before a spinal shot, it cuts thrust, slews (~30 s for 90°), steadies on RCS, and fires. Recoil is negligible to its trajectory (~cm/s) but a hard jolt to its structure.
- **Hab rings.** Both classes have counter-rotating twin rings [Lore; Model], so the rings' spin doesn't fight a flip. At action stations the rings keep turning but are **depopulated**. The crew goes to the armoured, non-rotating citadel stations on acceleration couches [A-34].
  - **Draft change:** the draft's D7 spun the rings down. Spinning them down and back up costs time and energy and buys nothing.

---

## 11. Damage control and reserves

- **Battle state [A-35].**
  - Crew in suits; threatened sections depressurised, so a hit vents little and can't start a fire.
  - Watertight and airtight doors shut.
  - Magazines and capacitor banks isolated.
  - The reactor ready to scram.
- **Heat casualties.** A lost fin means shifting load: ration fire (guns silent first, since they are ~70 % of the heat load, WN §4), then use the emergency dump (§8), then break off.
- **Radiators and drones are consumables (D7).** Damaged fin segments are cut loose so the rest can retract. Spares are at the tender.
- **Reserves:**
  - about a third of the hedgehog magazine;
  - the gun frigate, held back until emplacements reveal themselves;
  - the PD frigate at the park;
  - one destroyer's drone load.
- **Casualty and recovery:** damaged ships fall back toward the park, and the tender comes forward only after the defence is broken.

---

## 12. Rules

### LREF: offensive

| ID | Rule | Detail | Numbers | Change from draft |
|---|---|---|---|---|
| **O1** | **Arrive slow, outside, together** | Exit near rest relative to the target world, outside the debris line and the defender's reach. Stagger exits by seconds and 50+ km. Park the shields at the exit with the tender, then approach on drives. | Harrow: exit ~450,000 km; approach 4.6–6.3 h at a 20–30 km/s cruise (WN §6) | *Was:* arrive at 180 km/s, flip, jettison shields in the burn. *Why:* braking takes 5 h; shields released at speed can't be recovered [Lore]. |
| **O2** | **See first, speak last** | The Astrid's AVPSA builds the picture: passive always, radar in bursts (it glows anyway). Everyone else is EMCON on laser links. Destroyers push picket and EW drones 5,000–20,000 km ahead. | AVPSA radar: 1 m² at ~180,000 km, a slug at ~57,000 km (WN §5) | Numbers added; the Astrid named as the lighthouse. |
| **O3** | **Saturate on a clock** | Hedgehog packs fire in waves timed to arrive within ~1 s. Wave 1 spends and reveals; wave 2 kills. Mixed payloads: Casaba, thermonuclear, kill-cloud, decoy, EW. | One wave arriving nose-on in the laser shadow faces ~100 kills; side-on to four ground sites, ~500+ (WN §8) | Numbers added; pack of three (lore). |
| **O4** | **Guns on what can't dodge** | Kinetics only inside the no-escape range, or at fixed or committed targets. The spinal cannon hunts fixed installations at long range and crippled ships at medium range. | Table in §4.1 | *Was:* ≤ 1,000 km against manoeuvring ships. *Now:* by target type; against frigates only ≤ ~200–340 km. |
| **O5** | **Blind before the blow** | Arrays dazzle optics at any range. Destroyers jam radar, cut links and spoof tracks, so the defender's emplacements fall back to autonomous fire plans. The strike lands in that window. | Dazzle > 10⁶ km (WN §1) | Clarified: passive IR can't be jammed, only blinded by lasers or hidden by smoke. |
| **O6** | **Close with purpose** | Knife range only where terrain forces it (rocks in the Shoals block sight lines until contact) or against crippled targets. Broadsides only with fins stowed. Plasma lances ≤ 50 km. | M-1C against a frigate ≤ ~190–340 km | *Why:* in open space, knife range is where emplacements win (§4.1). Added fin rule (§8). |
| **O7** | **Layer the arms** | Drones, then corvettes, frigates, the cruiser, and the heavy cruiser. Each layer spends the enemy's attention and heat for the next. The spinal cannon fires into the gap. | — | Unchanged. |
| **O8** | **Speed is the defender's ammunition** | Cross prepared space at ≤ ~20 km/s relative. Corvettes and drones lead and sweep the lane. Never make a high-speed ballistic pass through a defended system. | A 1 kg rock at 20 km/s = 48 kg TNT; at 180 km/s = 3.9 t (WN §6) | New. |
| **O9** | **Choose the geometry, not the fight** | Attack from where the enemy's lasers see hardened noses or nothing: below the sites' horizon, behind rocks, through the Shoals' dust. Time strikes to planetary rotation and weather. Make every defender that can see the wave see it nose-on. | Nose-on vs side-on changes the kills per wave 7–17× (WN §8) | New. |
| **O10** | **Cripple, then kill** | Against a mobile heavy target: strip its fins and sensors (lasers), cut its drive (Casaba, missiles), and only then commit heavy kinetics, from inside its now-larger no-escape range. | Monitor: 0.05 g → 0.005 g grows the spinal no-escape range from ~4,000 to ~12,000 km (WN §2) | New. Reverses the draft's last beats (spinal before Casaba). |
| **O11** | **Spend missiles, keep ships** | Frigate packs are the currency. Hold about a third of the magazine in reserve. Withdraw empty hedgehogs to the tender (4 CIWS only [Lore]). | ~700 missiles per hedgehog [A-26] | New, from lore. |
| **O12** | **Plasma where the field holds** | Lances and torpedoes are knife weapons for emerging emplacements, crippled ships and strays. They are never the plan at range. | Lance ≤ ~50 km; torpedo launch ≤ ~100 km [A-23] | New, from lore. |
| **O13** | **Brake late and off-axis** | Fight coasting and bow-on. Brake with the thrust line off the main threat axis, under cover, when the enemy's long weapons are blinded or busy. | Braking 20 km/s at 1 g: 34 min over ~20,000 km (WN §6) | New. |

### LREF: defensive

| ID | Rule | Detail | Numbers | Change from draft |
|---|---|---|---|---|
| **D1** | **Six layers against missiles** | EW, decoys, laser arrays, PD lasers, chaff and smoke, CIWS kill clouds (§6). Kill anything that might be a Casaba before ~10 km. | CIWS ~3 missiles/s per 16 mounts; Casaba standoff 2–4 km (WN §7–8) | Reordered by range; Casaba rule added. |
| **D2** | **Spread out, stay covered** | Ships ≥ 50 km apart (well beyond a 1 Mt burst's fin-kill radius) but within ~10,000 km of the Astrid's arrays. | 1 Mt strips fins to ~3 km; LFAs kill side-on missiles to ~30,000 km (WN §1, §7) | *Was:* 50–200 km. The upper bound is now set by mutual PD cover. |
| **D3** | **Heat discipline** | Fins stowed inside any enemy laser envelope; run on sinks. Fins out only behind cover or with the threat on the long axis. Rotate firing duty. Know the heat clock. | Endeavor dark: ~24 min full combat, ~91 min guns silent (WN §4) | *Was:* "a few minutes" on sinks. Numbers and the edge-on rule added. |
| **D4** | **Random walk** | Inside any slug's no-escape range, jink on RCS and modulate the drive by ±10–20 %. Never fly a straight coast in the Shoals. | RCS 0.1 g moves a capital ship ~150 m in ~20 s (WN §2) | Linked to the no-escape table. |
| **D5** | **Use the terrain** | Rocks, the planet's limb and the Shoals' dust give cover from lasers and sensors, and a place to vent heat. | — | Adds heat venting behind cover. |
| **D6** | **Screen the screen** | Corvettes and PD drones kill drones and strike craft before they reach the line. The defender's drones are parked ahead in the lanes, so screen the lane ahead, not only the flank. | Drones from Kest need hours to reach the Shoals (WN §3) | Updated for pre-positioned drones. |
| **D7** | **Spend what is spendable** | Radiators, drones, decoys and the parked shields are consumables. Hab rings keep spinning but are depopulated; crew at citadel stations, suited; threatened sections depressurised. | — | *Was:* rings spin down. *Why:* counter-rotating rings don't fight a flip (§10). |
| **D8** | **Never turn your back without cover** | Flips under smoke, EW peaks and escort cover, one ship at a time. | Flip: Endeavor ~28–49 s, Astrid ~33–58 s (WN §6) | New. |
| **D9** | **Keep the way home** | The shield park and the tender are the line of retreat. Emergency warp without a shield only into a surveyed short hop. Keep 3–5 min of spool time in hand. | [A-05, A-07] | New, from lore. |
| **D10** | **Protect the net** | Air-gapped fire control, authenticated laser links, kill switches on every drone. Assume spoofed tracks until two sensors agree. | — | New, from lore. |
| **D11** | **Guard the park** | The PD frigate and a corvette hold the shield park and the tender. A defender raid on the park is a trade the LREF accepts only if it costs the defender its strike craft [Lore]. | — | New, from lore. |

---

## 13. What the LREF avoids

- **High-speed passes through prepared space.** Relative velocity arms every pebble the defender has left in the lane (O8).
- **Braking straight down the threat axis** with nothing covering the stern (O13, D8).
- **Fins out inside a laser envelope** (D3).
- **Radio.**
- **Firing kinetics outside the no-escape range** at anything that can move (O4).
- **Committing all the hedgehogs in one wave, or firing a wave without EW cover** (O3, O11). The destroyers can "sever the coordinated strikes of hedgehog packs" [Lore], and the defender's can too.
- **Knife fights in open space** (O6).
- **Leading with the Astrid.** It is the eye, the PD anchor and the hammer, and it has weak armour and poor manoeuvrability [Lore].
- **Leaving the park unguarded** (D11).
- **Carriers and crewed strike craft.** Lore calls carriers controversial, expensive and nullified by good screens. The LREF uses drones.
- **Bombarding a populated world.** A slug or warhead fired at a planet's surface is a weapon of mass destruction. The operation exists to put T-SEC on the ground, not to ruin the ground.
  - Whether the LREF may strike Harrow's isolated military laser sites is an ROE question for you (`OPEN_QUESTIONS.md` Q6). This doctrine assumes **no**: the fleet beats the ground lasers by geometry, weather, smoke and EW.

---

## 14. Assumption register

Each of these goes beyond the lore. The ones marked ★ are also in `OPEN_QUESTIONS.md` because they change what the film shows.

| ID | Assumption | Why this value |
|---|---|---|
| A-01 ★ | A ship leaves warp with its entry velocity; arrival velocity is set at the last hop point | Lets the fleet arrive slow, so the shields can be recovered [Lore] |
| A-02 ★ | No bubble can form or collapse inside dense debris; at Harrow the debris line is the outer edge of the Shoals (~300,000 km) | Gives "bunny-hopping because of debris" [Lore] a tactical meaning |
| A-03 | Exit precision ~1,000 km; exits staggered by seconds and ≥ 50 km | Avoids overlapping bubbles |
| A-04 | Bubble collapse flashes, visible at light speed | The draft's opening shot; tells the defender |
| A-05 | Spool 3–5 min, collapse ~5 s | Matches the rig's `warp_charge` ramp |
| A-06 | Bunny-hop legs with a staging point outside the target system | Lore mentions bunny-hopping without detail |
| A-07 | Warp without a shield = accepted impact risk, short surveyed hops only | Follows from the shield's purpose [Lore] |
| A-10 | Sustained thrust: capital ships 1 g (2–3 g for minutes), frigates 2 g, corvettes 4 g, missiles 30–50 g | Crew tolerance; lore calls corvettes fast and heavy cruisers poor manoeuvrers |
| A-11 ★ | A tender accompanies the task group and holds the shield park | Lore: tenders "WILL be" in the backline |
| A-12 | The commander flies in the Astrid; the Endeavor is the alternate | Picture, power, survivability |
| A-13 ★ | The objective is orbital control for a T-SEC landing | Explains why the LREF must break the defence and won't bombard |
| A-20 | M-1C: 10 kg at 25 km/s; spinal: 500 kg at 60 km/s | A ~100 m barrel [Lore] at ~3×10⁵ g; ~1 km barrel at ~2×10⁶ g |
| A-21 | The spinal cannon can hit a fixed point target at ~100,000 km (slug divert kit or salvo) | Aim error of ~0.1 µrad is at the edge of plausible; beyond that, salvo |
| A-22 | Laser focusing array: 3.3 m, 350 nm, 25 MW; PD laser: 1.6 m, 5 MW; 25 % wall-plug; 1.5× jitter | Apertures from the draft; UV matches the violet lens [Model] |
| A-23 | Plasma lance = compact toroids at ~1,000 km/s, ~1 GJ each, ~50 km coherence | Gives the lore's "ship generates the EMF" a mechanism |
| A-24 | Casaba: 20–100 kt, 25 % into a 0.01 rad jet | At the optimistic end of published concepts; the soft coat |
| A-25 | Missiles: hardened nose, spin, a quarter of Δv held for the terminal phase; specs in §4.5 | Makes the PD maths honest |
| A-26 | Hedgehog: ~240 capital-ship killers + ~120 multi-packs of ~4 = ~700 missiles | Lore: ~360 pods, "back 1/3" multi-silo, MIRVs |
| A-27 | Flares are powered decoys matching a ship's IR signature | A pyrotechnic can't match a GW-class ship |
| A-28 | Smoke and chaff screens expand and thin in seconds to minutes | Vacuum has no air to hold them |
| A-29 | EMCON plus laser mesh; ECW can only enter through a receiver | Physical reading of the lore's "network screen" and infiltration |
| A-30 | Fin areas measured off Sir_Lazz's size chart | See WN §4 |
| A-31 ★ | Heat sinks: Endeavor 20 TJ, Astrid 60 TJ | Sets the heat clock (24 and 40 min); the storyboard's overheating beat depends on it |
| A-32 | Emergency dump: ~1,000 t of water, ~3 min at full combat, visible vapour plume | Open-cycle cooling |
| A-33 | Flip time limited by ~1 g (routine) or ~3 g (combat) at the ship's ends | Structure and crew |
| A-34 | Rings keep spinning at action stations, crew moved to citadel stations | Counter-rotating rings [Model] |
| A-35 | Battle state: suited crew, depressurised sections | Standard hard-SF practice |
