"""Operation Tidebreak: storyboard data (phase 2, revision 2).

One source for the storyboard page, shots.csv, shots.md and ASSET_REQUESTS.md.
Build with:  python3 storyboard/build_storyboard.py

Revision 2 applies the round 1 reviews (review/round1/*.md, synthesis in
review/round1/synthesis.md). Shot numbers changed: every internal cut is now
its own shot; the rev 1 → rev 2 mapping is in the synthesis.

Conventions
- `dur` is screen time in seconds at 24 fps; frames are computed from it.
- `clock` is real mission time at the start of the shot (T+h:mm:ss from warp exit).
- `real` says how the shot treats time: "1:1", "compressed N×", "slowed N×", or a clock jump.
- `body` is the camera body (CAMERA_BODIES): only hull cameras hear the ship.
- `rules` cite doctrine rule IDs (doctrine/LREF_doctrine.md, doctrine/Defence_doctrine.md).
- `assets` cite IDs in ASSETS; `rig` names Endeavor rig properties
  (pack/project_docs/README_blender_project.md) or ones requested in ASSETS (marked "new").
- `cost` is the render class in RENDER_CLASSES.
- `sketch` is a call into storyboard/sketchlib.js; `render` is a current Blender
  frame used as look reference. Sketches drop the gold shields automatically once
  the shields are parked.
- Text refers to shots by title, as `{#Title}`; the builder turns that into the
  shot's number, so renumbering never breaks a reference.
"""

TITLE = "Operation Tidebreak"
REVISION = "Revision 2 · after review round 1"
FPS = 24
FORMAT = "2.39:1 · 1920×804 · 24 fps · Cycles"
SHIELDS_OFF = "T+0:02:00"   # the shields leave the ships; sketches drop them from here on

# ---------------------------------------------------------------- mission
PHASES = [
    ("T+0:00", "T+0:25", "Arrival", "Exit at 450,000 km, near rest relative to Maren. Shields parked with the Nauvoo (T+0:02). Net up. Skerry throws three rounds (T+0:04) and its laser dazzles the Astrid's dish, so the fins stay in. Wave one away at Skerry (T+0:18)."),
    ("T+0:25", "T+0:59", "Turn and burn", "1 g along the approach line for 34 min: 0 → 20 km/s over 20,400 km."),
    ("T+0:59", "T+3:20", "Coast", "20 km/s, bow on Maren. Skerry's laser dies at T+1:02 and its depot flushes 40 drones toward the shield park; the fins come out edge-on at T+1:10."),
    ("T+3:20", "T+4:34", "The Breakers", "Fins stowed in the debris. Site 1 dazzles; the pods wake; the Canterbury is lost (T+3:52); the Astrid answers; drones wake; the Normandy is lost (T+4:25)."),
    ("T+4:34", "T+5:09", "Turnover", "Flip (49 s) and brake at 1 g for 34 min, ending on Anchor's orbital velocity (1.63 km/s; thrust tilted ~4.7°)."),
    ("T+5:09", "T+5:43", "Anchor", "An 18 km rock that at T+5:09 lies over Site 1. The fleet sweeps it (a mine), vents, loses the port fin to a platform 400 km off, lances a frigate, kills the platform, and vents again with three fins (94 % → 31 %)."),
    ("T+5:43", "T+7:51", "Final approach", "An inertial path of ~113,000 km: 1 g to 20 km/s (to T+6:17), coast, turnover at T+7:16, then brake to a stop ~8,500 km from Breakwater (T+7:51). The Astrid, trailing, stops 10,800 km out. Skerry's net at T+6:40; Site 1's fire from T+6:55; Breakwater's 64 missiles at the Extenuating (T+7:25), killed under the Astrid's umbrella (T+7:31). The pack stays at Anchor as a fire base."),
    ("T+7:27", "T+7:58", "Hammer and anvil", "From Anchor, 118,000 km out, the spend wave (Infinity) arrives at T+7:52:00 and the kill wave (Galactica) at T+7:53:30. Both fly straight in, nose-on to Breakwater and ~48° off its zenith, so misses and wreckage clear Maren. Casaba jets cut the drive. The Astrid hails, then fires from rest at T+7:54:40, 15° off Breakwater's zenith; impact T+7:57:44."),
    ("T+7:58", "T+8:24", "Terms", "Sink 98 %: the Endeavor dumps water (T+8:00). Maren asks for terms (T+8:10). Site 1 goes dark; the fleet vents at last (T+8:24)."),
]

KEY_NUMBERS = [
    ("Warp exit and shield park", "450,000 km from Maren", "LREF O1, A-01/A-02"),
    ("The Breakers", "120,000–260,000 km, ±25°", "Defence §4.1"),
    ("Anchor (the rock)", "~18 km, 150,000 km out; over Site 1 at T+5:09; drifts 12.8°/h relative to Site 1", "D5"),
    ("Skerry", "380,000 km, 40° off the approach line; mass driver 12.5 km/s", "H-14"),
    ("Breakwater", "synchronous orbit, 42,164 km, over Site 1", "H-04"),
    ("Cruise speed", "20 km/s (O8)", "WN §6"),
    ("Burns and flips", "1 g, 34 min; flips 49 s (Endeavor), 58 s (Astrid)", "WN §6"),
    ("Final approach", "~113,000 km from Anchor; turnover T+7:16; the escorts stop ~8,500 km from Breakwater, the Astrid 10,800 km", "WN §6"),
    ("Lines of fire", "The waves arrive ~48° off Breakwater's zenith, the spinal shot 15° off it. Maren fills ±8.7° around Breakwater's nadir, so misses and wreckage clear it: a wave's by ~25,000 km, a spinal miss (aimed ahead of the moving monitor) by ~7,000 km", "O9, §13"),
    ("Site 1 against the waves", "~15 kills per wave: aimed at Breakwater, the waves never come within ~36,000 km of it (5 on a 15° line, so there is nothing to gain by bending the waves)", "WN §8"),
    ("Spinal shot", "from rest at 10,800 km (no-escape ≤ 11,017 km vs a crippled monitor); flight 184 s", "WN §2, O10"),
    ("Endeavor heat", "20 TJ sink: 94 % at Anchor, 31 % leaving it, 98 % at T+8:00; a 1,000 t water dump buys ~25 min", "WN §4, A-32"),
    ("Light-lag", "0.87 s to Skerry at T+1:02; 0.48 s from Anchor to Site 1", "WN §5"),
]

# ---------------------------------------------------------------- film rules
LIGHTING = [
    "The sun sits behind Maren, about 30° off the approach line. From the fleet Maren is a thin crescent with a bright limb, and the Breakers glow faintly lit from behind (dust scatters forward).",
    "Hulls are lit hard from ahead and to one side; the shadow side falls to black. No stars behind sunlit hulls.",
    "Anchor's lee faces away from both Site 1 and the sun: the fleet shelters in darkness, so the fins, muzzle flashes and the lance light the scene (the M-1C 'fins1dark' look).",
    "At the end Site 1 is on the night side: its lights can be seen going out, and the final frame puts the Endeavor against the night side's city lights.",
]
CLOCK_HUD = [
    "The mission clock is small, persistent and clear of the subtitles. It starts on the flash in shot {#Black, then a star} (T+0:00:00).",
    "It runs at the shot's rate: spinning seconds mean compressed time, crawling ones slowed. On jumps over 30 minutes the digits roll or the shot dissolves.",
    "One master tactical plot, always with Maren screen right. Inserts hold for at least 5 s where they carry geography, with no more than about four labels.",
    "A fixed corner readout carries ENDEAVOR SINK nn % and FINS n/4 from Act III, so the heat builds visibly toward the dump.",
    "Subtitles and the clock go in during the edit, after the grade, so a changed line never forces a re-render.",
]
SCREEN_DIRECTION = [
    "Maren and the enemy stay screen right. The LREF travels and fires left to right.",
    "Until the turnover (shot {#Turnover}) bows point right. After it bows point left while travel stays left to right, so the drives burn toward screen right.",
    "The final approach repeats the pattern: bows right from Anchor to the second turnover (T+7:16), bows left while braking, and the Astrid swings its bow back to screen right for the spinal shot.",
    "Enemy reverses only over an enemy foreground. At Anchor the Endeavor's bow points at the frigate's moonlet: the frigate is off the port bow, the platform off the port quarter, and shots {#Fins in}–{#The platform dies} share that axis.",
]
CAMERA_BODIES = {
    "hull": "Hull camera: bolted to a ship, shakes with it, and is the only body that hears (sound through structure).",
    "drone": "Drone camera: free-flying, silent; score and sub-bass only.",
    "tracker": "Tracker: a long lens (300–2,000 mm) on a ship or drone; heavy slow pans, sensor noise; silent.",
    "hud": "HUD insert: 2D compositing, UI tones only.",
}

# ---------------------------------------------------------------- forces
FLEET = [
    ("L.R.E.F.S. Astrid", "Hanuman heavy cruiser, 1.6 km", "Flagship, 'Tidebreak Actual'. Spinal cannon, AVPSA, PD anchor. Trails the line; stops behind the escorts and fires from rest."),
    ("L.R.E.F.S. Endeavor", "Ryland cruiser", "The line. Loses its port fin at Anchor."),
    ("Infinity · Pillar of Autumn · Galactica", "Hedgehog frigates (~700 missiles each)", "Wave one (Infinity, 150), the spend wave (Infinity, the rest), the kill wave (Galactica). The Pillar holds its load in reserve. The pack stays at Anchor as a fire base."),
    ("Donnager", "Gun frigate", "Sweeps the rocks round Anchor; fights the Compact frigate."),
    ("Excelsior · Tantive IV", "PD frigate · corvette", "Guard the Nauvoo and the parked shields (D11); beat off Skerry's drone raid."),
    ("Canterbury", "ECW destroyer", "Brings the net up; lost in the Breakers ambush (T+3:52)."),
    ("Extenuating Circumstances", "ECW destroyer", "Holds what's left of the net; rides under the Astrid's umbrella, which kills the 64 missiles Breakwater sends after it."),
    ("Rocinante · Wallfish · Normandy", "Corvettes", "The drone screen. Normandy lost to a plasma-bomb drone (T+4:25)."),
    ("Nauvoo", "Tender", "Holds the shield park 450,000 km out."),
]
DEFENDERS = [
    ("Breakwater", "Warpless monitor", "Synchronous orbit over Site 1. Its guns never get a shot (the LREF stays outside their no-escape range); it fires its 64 missiles at the last ECW destroyer."),
    ("Site 1 (of 4)", "Ground laser, 2 GW", "The only site that sees Breakwater's sky. Dazzles and burns; never struck (ROE)."),
    ("Skerry", "Moon complex", "Throws three rounds at T+0:04; its laser dazzles the fleet until wave one kills it; its depot flushes 40 drones at the shield park."),
    ("The Breakers garrison", "Emplacements", "Cold pods, railgun platforms, mines, parked drones and a drone-control craft."),
    ("Inner ring", "12 emplacements", "Sensor pickets and sector defence along the orbit; too far apart to thicken Breakwater's wall."),
    ("Compact frigates", "3", "One ambushes the Endeavor at Anchor; two hold behind Maren's limb."),
]

# ---------------------------------------------------------------- assets
# status: built / extend / new; concept: concept sheet first (user rule).
ASSETS = {
    "EN": ("L.R.E.F.S. Endeavor (rigged)", "extend", False, "Hero ship. Rebuild after the M-1C wake-style and PDC picks that are still pending in the modelling session (Q15), then link it into shot files with a library override on the rig empty."),
    "EN-FIN": ("Endeavor: per-fin control and damage", "extend", False, "Per-fin deploy properties `fin_port`, `fin_starboard`, `fin_dorsal`, `fin_ventral` (the ship-wide `radiator_deploy` stays as a master). Port fin states via `fin_port_state`: intact, pre-fractured (shot {#Fin hit}), stump (shots {#Off the port bow}–{#Hold})."),
    "EN-PD": ("Endeavor: defence, countermeasure and emergency controls", "extend", False, "`ciws_phase` (a keyed angle, with a spin-blur swap above ~600 rpm, because `ciws_rpm` changes jump and strobe), `ciws_fire` (muzzle empties), `cm_chaff`, `cm_flare`, `cm_smoke`, `ew_active`, `water_dump` (valve and plume emitter)."),
    "EN-MAST": ("Endeavor: sensor-mast shutters", "extend", False, "`mast_shutter`: armoured shutters close over the mast windows."),
    "EN-DMG": ("Endeavor: hull damage", "extend", False, "`dmg_belt`: spall and scorching on the port belt from shot {#Off the port bow} on; it must read in shot {#Heat}, which runs along the port flank."),
    "M1C": ("M-1C twin railcannon", "extend", False, "Fleet gun. Wake style still to be picked (split, ripple, bulk, extend, combined: Q15); per-gun `charge_a/b`, `shot_a/b`, `fins_a/b`, `heat_a/b` for shot 35 (only the gun that fired vents)."),
    "MSL": ("Missile asset (26 m, plume, thrust)", "built", False, "Base for every variant."),
    "MSL-V": ("Missile variants", "new", True, "Concept sheet first (five new weapon designs): the Casaba killer (hardened ablative nose, spin), the small multi-pack missile with MIRV bus, decoy, EW missile, Compact belt-pod missile. Three LODs each for the swarm system."),
    "AST": ("L.R.E.F.S. Astrid (Hanuman heavy cruiser)", "new", False, "Hero, ~1,650 m. Build from lref_kit: M-1Cs, arrays, CIWS, fins, rings and shield are instances, so the new hero work is the hull, the AVPSA dish and the spinal. Concept sheet for the spinal muzzle and its FX look. Controls: `avpsa_az`, `avpsa_el`, `fins_deploy` (8), `spinal_charge`, `spinal_shot`, plus the Endeavor's `ciws_phase` and `ciws_fire` on its instanced CIWS. Art exists."),
    "GI": ("Garibaldi-Ivanova frigate hull", "new", False, "Hero, ~420 m. One hull for all five frigates; module bay; warp rings; shield; spinning hab section. Art exists."),
    "GI-MAV": ("Hedgehog (MAV) module", "new", False, "~360 pods; `pod_ripple` launch control. Art exists."),
    "GI-GUN": ("Gun module (4 large kinetic batteries)", "new", True, "Four scaled M-1C twins; the concept sheet only settles the layout."),
    "GI-PD": ("PD module", "new", True, "Build after the PDC pick. Seen only far off in shot 4: a silhouette is enough if the user agrees (Q13)."),
    "DD": ("ECW destroyer", "new", False, "Hero, ~200 m. Dish placement follows the art (forward, behind the shield) unless the user decides otherwise (Q14). Controls: `dish_deploy`, `booms_deploy`, `drone_bay`. Art exists."),
    "DD-BRK": ("Destroyer break-up (Canterbury)", "new", False, "Section-break rig: holed bow to stern, venting, the hull parting in two."),
    "CV": ("Corvette class", "new", True, "No reference art: concept sheet first. Brief: 50–150 m; two warp rings at the ends; a jettisonable forward shield; radiators and booms that stow for warp; no spin section; anti-drone weapons 'far more powerful and varied' than a big ship's PD."),
    "CV-BRK": ("Corvette destruction (Normandy)", "new", False, "Section-break rig variant."),
    "TND": ("Nauvoo, fleet tender", "new", True, "No reference art: concept sheet first. Brief: two warp rings, forward shield, stowable radiators; cradles for spare shields; a rig for swapping frigate modules. Seen only far off: a silhouette if the user agrees (Q13)."),
    "SHD": ("Parked impact shields", "extend", False, "Scaled instances of the gold shield for the park cluster."),
    "DRN-L": ("LREF drone", "new", True, "One design (picket/PD/EW variants by payload only), concept first."),
    "BW": ("Breakwater, Compact monitor", "new", True, "Concept sheet first. ~1,800 m warpless monitor: no rings or shield, ~2 m belt, 6 twin heavy turrets, 24 PD lasers, 40 CIWS, 64 cells, armoured louvred radiators. Controls: `turret_traverse`, `turret_elevation`, `cells_open`, `drive_glow`, `vent`."),
    "BW-BRK": ("Breakwater break-up", "new", False, "Section-break rig: spear wounds on the drive bells, the spinal entry amidships, secondaries, the back breaking."),
    "CF": ("Compact frigate", "new", True, "Concept sheet first. ~350 m; coilgun and missiles; section-break variant. Seen at ~470 px in shot {#Lance} (1,000 mm at 40 km), so it needs real detail."),
    "DRN-C": ("Compact drone and its hide", "new", True, "One design (plasma-bomb payload) plus the cold hide on a rock; concept first."),
    "EMP-POD": ("Cold missile pod on a rock", "new", True, "Concept first. Controls: `heave`, `petals`."),
    "EMP-RG": ("Breakers railgun platform", "new", True, "Concept first. Buried twin railgun. Controls: `unmask`, `shot`."),
    "RING": ("Inner-ring station", "new", True, "Only ever a point of light at ~21,800 km spacing: lights only, if the user agrees (Q13)."),
    "SKR": ("Skerry", "new", False, "One still plate of an airless moon; the battery, tracks and depot are flash and light positions only."),
    "WORLD": ("World presets and sun", "extend", False, "World presets for arrival, the Breakers, Anchor and Breakwater, with planet-shine scaled to each (Maren is 1.6° across from the exit, ~17.5° from Breakwater's orbit); a Sun object that drives the World (today `TO_SUN` needs a rebuild); Skerry as a second body at the right angular size; each set-up's camera kept near the world origin."),
    "MAREN": ("Maren: planet re-dress", "extend", False, "New continents and weather, night-side cities, the Site 1 plateau as a light cluster that can go out (shot 53)."),
    "BRK": ("The Breakers environment", "new", False, "The dust haze as the Mist pass plus a sparse glitter layer; a generic rock kit; large rocks at realistic spacing."),
    "ANCHOR": ("Anchor: hero rock", "new", False, "~18 km rubble pile: a Geometry Nodes boulder scatter from the BRK kit, with hero surface tiles only where the camera goes close (shots {#The sweep}, {#The pack fires})."),
    "FX-WARP": ("Warp-exit flash", "new", False, "Bubble collapse bloom (comp plus a light)."),
    "FX-SWARM": ("Swarm system", "new", False, "One Geometry Nodes system for missiles, drones and canister pellets: per-instance launch time, three LODs (hero mesh only for the nearest ~10), each plume a single emissive mesh with emission sampling off, real lights only on the ~5 nearest plumes or flashes, pellets as emissive points whose brightness follows the lamp angle, rendered in its own view layer."),
    "FX-FAR": ("Distant drive plumes", "new", False, "Cheap far plumes for long-lens fleet shots."),
    "FX-NUKE": ("Nuclear flashes", "new", False, "Point flashes: Skerry's surface, the mine at Anchor."),
    "FX-PD": ("Point-defence fire", "new", False, "CIWS tracers and kill clouds, chaff, flares, intercept flashes, in their own view layer at low samples."),
    "FX-SMOKE": ("Smoke screen", "new", False, "One low-resolution cached VDB in its own layer, reused in shots {#Countermeasures}, {#Turnover} and {#Site One}."),
    "FX-SLUG": ("Slug streaks and impacts", "new", False, "Glints, impact flash, spall cone, shock ring."),
    "FX-BREAK": ("Section-break rig and debris kit", "new", False, "No cell fracture (the plated kit hulls defeat it): split each hull along its bulkhead frames into 3–8 sections, cap the torn edges with kit parts, drive the pieces apart with a procedural `break` 0→1, scatter an instanced debris kit."),
    "FX-VENT": ("Venting in vacuum", "new", False, "Short-lived sprays of glinting ice (what gas and coolant do in vacuum), plus the Endeavor's water-dump plume; one small cached VDB reused."),
    "FX-FIN": ("Fin shatter", "new", False, "The pre-fractured port fin's shards and glow."),
    "FX-LANCE": ("Plasma lance", "new", False, "A field-held violet-white jet from the nose channels to the target inside a faint field sheath; it fizzles back when `lance_power` cuts."),
    "FX-CASABA": ("Casaba jets", "new", False, "Narrow nuclear spears from 2 km standoff."),
    "FX-SPINAL": ("Spinal fire and impact", "new", False, "Muzzle bloom down the Astrid's kilometre barrel; impact flash and spall."),
    "FX-DAZZLE": ("Dazzle and whiteout", "new", False, "Comp: bloom on optics, POV whiteout."),
    "FX-EW": ("EW overlay", "new", False, "Comp: glitch bands on HUD inserts."),
    "HUD": ("Tactical HUD and mission clock", "new", False, "2D comp. The user approves a style frame first; the plots can reuse the SVG map code in build_storyboard.py."),
    "SUB": ("Comm subtitles", "new", False, "2D comp, added in the edit; short dim speaker tags."),
}

# Closest view of the main assets: (shot title, what, approx. size on screen).
# The builder checks that the asset really is in that shot.
CLOSEST = {
    "AST": ("Spinal", "EWS 200 mm, end-on at ~2 km", "fills the frame"),
    "GI": ("Wave one", "hull camera on the Infinity", "fills the frame"),
    "DD": ("Net up", "MS 40 mm at ~600 m", "fills the frame"),
    "CV": ("Normandy", "300 mm at ~20 km", "~150 px"),
    "TND": ("Shields to the park", "behind the parked shields", "~40 px"),
    "GI-PD": ("Shields to the park", "behind the parked shields", "~40 px"),
    "BW": ("The hail", "drone camera near the monitor", "fills the frame"),
    "CF": ("Lance", "1,000 mm at 40 km", "~470 px"),
    "RING": ("The anvil", "far along the orbit", "points of light"),
    "SKR": ("Skerry burns", "1,200 mm at ~262,000 km", "a quarter-frame disc"),
    "EMP-RG": ("The platform", "drone over the platform", "fills the frame"),
    "EMP-POD": ("The belt wakes", "drone near the rock", "~300 px"),
    "DRN-C": ("Screens out", "28 mm, nearest drones", "~30 px"),
    "DRN-L": ("Net up", "MS 40 mm", "~40 px"),
    "ANCHOR": ("The sweep", "low over the surface", "fills the frame"),
}

RENDER_CLASSES = {
    "A": ("Endeavor close-up", "~45 s/frame"),
    "A2": ("Endeavor close-up with heavy FX", "~90 s/frame"),
    "B": ("One hero ship or rock, full view", "~75 s/frame"),
    "C": ("Several ships or heavy FX (FX in own layers)", "~200 s/frame"),
    "D": ("Wide, distant or plate", "~15 s/frame"),
    "E": ("2D comp / HUD", "~2 s/frame"),
}
RENDER_NOTE = ("These costs are estimates, not measurements. Benchmark shots {#Rings cool}, {#Turn and burn}, {#Countermeasures} "
               "and {#Broadside} on the rebuilt Endeavor, plus one volume test, before the first full pass, and replace the numbers.")

# Set-ups: each shot belongs to exactly one (the builder checks).
SETS = [
    ("the Endeavor", ["Black, then a star", "Rings cool", "Shields to the park", "Fins edge-on", "Blind", "Spin-up",
                      "Countermeasures", "Turnover", "Too hot", "Fins in", "Fin hit", "Lance channels", "Broadside",
                      "Blind it", "Heat", "Hold"]),
    ("the Astrid", ["The Astrid looks", "Answer", "Umbrella", "Spinal"]),
    ("the destroyers", ["Net up", "Canterbury", "Holed", "The net", "Site One"]),
    ("the Breakers", ["The Breakers", "The belt wakes", "The platform", "Payback", "Screens out", "Normandy"]),
    ("the pack and Anchor", ["Wave one", "The sweep", "Off the port bow", "Lance", "The platform dies", "The pack fires",
                             "Kill wave away"]),
    ("Breakwater over Maren", ["The anvil", "The spend wave", "Wall of fire", "Casaba", "The hail", "Three minutes",
                               "Impact", "Terms"]),
    ("long-lens plates", ["The task group", "Turn and burn", "Skerry burns"]),
    ("2D", ["Skerry throws", "The picture", "Return to sender", "Anchor", "The fire plan"]),
]

PRODUCTION_PLAN = [
    ("Order", "1) The user's pending picks (Q15), the Endeavor rebuild and its new rig items, the World presets, the benchmarks and a timing animatic. 2) One batched concept round, since it waits on the user. 3) Meanwhile the assets with art: the FX library, the Breakers then Anchor, the frigate with its hedgehog module, the destroyer, the Astrid. 4) The concept-gated assets: missile variants, corvette and drones, emplacements, Breakwater, the gun module. 5) Proxies and the long-lens plates last."),
    ("Rendering", "One job per shot to multilayer EXR sequences (DWAA), Placeholders on and Overwrite off so a crashed render resumes; the grade (`LREF_Compositor`) as a separate pass; emissive FX in their own view layers at 16–32 spp with 1–3 proxy lights in the beauty layer; Persistent Data; adaptive sampling with denoising; vector blur in comp; plan ~100 GB of disk."),
]

ACTS = [
    ("I", "Arrival", "The fleet arrives slow, parks its shields, reads the system, and strikes Skerry first because Skerry's laser can burn its fins."),
    ("II", "The Breakers", "Hours of coasting, then the debris ring: the ambush, the Canterbury, the Astrid's answer, the drones and the Normandy."),
    ("III", "Anchor", "Turnover into the lee of a rock over Site 1: the sweep, the heat, the fin hit, the frigate, the lance and the broadside."),
    ("IV", "Hammer and anvil", "Across to Breakwater: Skerry's net, Site 1's fire, Breakwater's missiles at the last net ship, the spend wave, the kill wave, the Casaba jets, the hail and the spinal shot, then terms."),
]

MAPS = {
    "A": "Arrival and the coast (T+0:00 → T+3:20)",
    "B": "The Breakers (T+3:20 → T+5:09)",
    "C": "Anchor (T+5:09 → T+5:43)",
    "D": "The final approach, inertial frame (T+5:43 → T+7:51)",
    "E": "The kill, around Breakwater (T+7:25 → T+7:58)",
}

# ---------------------------------------------------------------- reviews
# Each round: (name, what was reviewed, [(lens, major issue, how the next revision answers it)]).
# Full reports and the synthesis are in review/.
REVIEW_STATUS = "Round 2 reads revision 2 with the same five lenses; the rounds continue until no reviewer has a major issue left."
REVIEWS = [
    ("Round 1", "Revision 1", [
        ("Physics", "The Astrid could not stop after its spinal shot.", "It stops 10,800 km out and fires from rest: no-escape 11,017 km, flight still 184 s."),
        ("Physics", "'The line' down Site 1's zenith turns at 15°/h, so nothing can coast down it.", "No line to hold: the waves fly straight from Anchor to where Breakwater will be. Map D is now in the inertial frame (a ~113,000 km approach, turnover T+7:16)."),
        ("Physics", "Straight down Site 1's line, Maren is the backstop.", "The waves arrive ~48° off Breakwater's zenith and the spinal shot 15° off it: misses and wreckage clear Maren."),
        ("Physics", "The heat readouts don't add up.", "Three fins vent again at Anchor (31 %), 98 % and a water dump at T+8:00, the fins out at T+8:24."),
        ("Physics", "Two hours in Site 1's sky with no effect.", "Site 1 scorches the Extenuating's boom; the fleet rolls and lays smoke, then dazzles at T+7:50."),
        ("Physics", "Skerry's rounds are too slow for the clock.", "The mass driver is 12.5 km/s: flight time 6 h 36 m."),
        ("Doctrine", "The spend wave lands an hour before the kill wave.", "90 s apart (T+7:52:00, T+7:53:30); the spend wave's arrival has its own shot."),
        ("Doctrine", "The Astrid ends up leading the fleet into the anvil.", "It brakes with the line and stops behind the escorts."),
        ("Doctrine", "An unswept, predictable anchorage.", "The fleet sweeps Anchor and trips a mine; the Donnager shells the nearby rocks; the platform (400 km) and the frigate (45 km) strike in the same minute."),
        ("Doctrine", "Nobody hunts the last ECW destroyer.", "Breakwater fires all 64 cells at the Extenuating; the Astrid's umbrella kills them (new shot {#Umbrella})."),
        ("Doctrine", "Site 1 falls silent during the final approach.", "It burns and dazzles; the fleet answers with rolls and smoke, then its own dazzle."),
        ("Doctrine", "The hedgehogs' magazines don't add up.", "The Infinity empties into the spend wave, the Galactica fires the kill wave, the Pillar holds ~700 in reserve, and the pack stays at Anchor."),
        ("Lore", "The lance was a free-flying ring.", "A field-held jet from the nose to the target; ~50 km is the field's reach (A-23 reworded)."),
        ("Lore", "The Astrid is not kilometre-long.", "'Its 1.6-kilometre hull': the kilometre is the gun."),
        ("Cinematography", "Subtitles bury the picture.", "Lines cut to ≤ 12 characters a second with short tags; the builder checks every shot."),
        ("Cinematography", "One tempo throughout.", "Re-timed with holds: the coast on the clock, the hiss after each loss, three minutes on the crippled monitor."),
        ("Cinematography", "Real lenses can't see the far end of the exchanges.", "Long-lens tracker cameras (300–2,000 mm) and matched framings for each payback."),
        ("Cinematography", "No clock or HUD plan.", "A persistent clock that runs at the shot's rate, one master plot with Maren screen right, a fixed SINK/FINS readout."),
        ("Cinematography", "The losses and the antagonist aren't set up.", "The Canterbury speaks first, the Normandy calls the drones, Breakwater gets a reveal, and the last plot names both lost ships."),
        ("Cinematography", "Time compression turns big hulls into models.", "Rotations at ≤ 4× with the middle cut out; every internal cut is now its own shot."),
        ("Production", "The render budget is unmeasured.", "Reclassified costs, computed per class, with named benchmark shots."),
        ("Production", "Detail isn't tied to what the camera sees.", "A closest-view table; proxies proposed for the ring stations, tender and PD module (Q13)."),
        ("Production", "The Endeavor and M-1C aren't built for this board.", "Marked 'extend: rebuild after the pending picks' (Q15) and first in the build order."),
        ("Production", "Rig controls are missing.", "Per-fin control, CIWS phase and fire, countermeasures, water dump and belt damage, plus controls for every new asset."),
        ("Production", "Break-ups and volumes would eat the schedule.", "A section-break rig instead of cell fracture, ice-glint venting, one cached smoke VDB, the Mist pass for haze."),
        ("Production", "Swarms with hundreds of plumes.", "One Geometry Nodes swarm system with LODs, emissive plumes and few lights."),
    ]),
]

# ---------------------------------------------------------------- shots
S = []


def shot(**k):
    S.append(k)


# ============================================================ ACT I
shot(act="I", title="Black, then a star", dur=6, clock="T+0:00:00", real="1:1", body="drone",
     cam="EWS · 35 mm · locked off",
     action="Starfield. A point of light swells into a blue-white bloom as the bubble collapses (~5 s). The Endeavor resolves out of it, bow screen right, shield forward, both warp rings glowing, fins stowed as they must be in warp. The mission clock starts on the flash.",
     comm=[], rules=["O1"], vfx="Warp-exit flash", rig=["warp_charge 1→0.3"],
     assets=["EN", "FX-WARP", "HUD"], sound="Silence; a sub-bass drop as the bubble collapses.",
     cost="D", map="A", render=None,
     sketch="panel([glow(120,50,55,'#9ec8ff',0.55), glow(120,50,14,'#ffffff',0.95), ship('endeavor',120,50,0.45,0,true)], 11)")
shot(act="I", title="Rings cool", dur=4, clock="T+0:00:06", real="1:1", body="hull",
     cam="CU · 50 mm · slow push along the bow ring truss",
     action="The front warp ring's emitters fade from blue to dark. A burst of bow RCS trims the drift.",
     comm=[], rules=["O1"], vfx="Emitter glow fade, RCS puffs", rig=["warp_charge 0.3→0", "rcs_bow pulse"],
     assets=["EN"], sound="Ticking metal and RCS thumps through the truss.",
     cost="A", map="A", render="img/bow_v4b_combat.jpg", sketch=None)
shot(act="I", title="The task group", dur=5, clock="T+0:00:10", real="compressed 7× (13 exits over ~36 s)", body="tracker",
     cam="EWS · 85 mm · long lens, locked off",
     action="Staggered warp flashes, seconds and 50+ km apart: the Astrid, the hedgehog pack, the Donnager, the Excelsior, both destroyers, four corvettes, the Nauvoo. Screen right, Maren is a thin crescent with the sun behind it, ringed by the faint backlit glow of the Breakers.",
     comm=[("ACTUAL", "All fourteen. All home.")], rules=["O1", "D2"], vfx="13 warp flashes, backlit ring glow",
     rig=[], assets=["AST", "GI", "GI-MAV", "DD", "CV", "TND", "MAREN", "BRK", "WORLD", "FX-WARP", "FX-FAR"],
     sound="Distant low thuds, one per exit (score, not diegetic).", cost="D", map="A", render=None,
     sketch="panel([planet(236,52,30,'right'), '<ellipse cx=\"236\" cy=\"52\" rx=\"70\" ry=\"9\" fill=\"none\" stroke=\"#cfd8e0\" stroke-width=\"0.5\" opacity=\"0.25\"/>', glow(40,40,9,'#9ec8ff',0.6), glow(70,58,7,'#9ec8ff',0.5), glow(26,66,6,'#9ec8ff',0.5), ship('astrid',40,40,0.16,0,true), ship('hedgehog',70,58,0.2,0,true), ship('destroyer',26,66,0.35,0,true), ship('endeavor',104,48,0.16,0,true), ship('tender',140,72,0.3,0,true)], 3)")
shot(act="I", title="Shields to the park", dur=5, clock="T+0:02:00", real="compressed 8× (~40 s)", body="hull",
     cam="MS · 35 mm · riding the shield's backplate, looking back at the bow",
     action="Separation thrusters fire between the front ring's spokes. The camera, riding the shield, backs away from the Endeavor's bow; both warp rings stay on the ship. Around it, other gold shields hang parked at near-zero speed, to be collected after the battle.",
     comm=[("ENDEAVOR", "Nauvoo, Endeavor. The shield's yours."), ("NAUVOO", "Porch light's off.")],
     rules=["O1", "D9", "D11"], vfx="Shield separation, thruster plumes",
     rig=["shield_thrusters 1", "shield_separation 0→400"], assets=["EN", "SHD", "TND", "GI-PD"],
     sound="Clamp bangs through the backplate, then silence.", cost="A", map="A",
     render="img/endeavor_combat_demo_f060.jpg", sketch=None)
shot(act="I", title="Net up", dur=3, clock="T+0:02:40", real="compressed 10× (the dish unfolds over ~30 s)", body="drone",
     cam="MS · 40 mm · off the Canterbury's bow",
     action="The Canterbury swings its big dish out behind where its shield sat and runs out its sensor booms; its drones scatter ahead. From here the fleet talks only by laser.",
     comm=[("CANTERBURY", "Net's up. Going quiet.")], rules=["O2", "D10"], vfx="Drone launch",
     rig=["dish_deploy (new)", "booms_deploy (new)", "drone_bay (new)"], assets=["DD", "DRN-L"],
     sound="Silence.", cost="B", map="A", render=None,
     sketch="panel([ship('destroyer',110,50,3.2,0,true), sparks(190,40,14,40,5)], 5)")
shot(act="I", title="The Astrid looks", dur=3, clock="T+0:03:20", real="compressed 10× (the slew takes ~30 s)", body="drone",
     cam="MS · 50 mm · along the Astrid's dorsal hull",
     action="The Astrid's 100 m AVPSA dish slews toward Maren. Its eight stacked fins stay stowed: Skerry's laser can see them.",
     comm=[], rules=["O2", "D3"], vfx="", rig=["avpsa_az / avpsa_el (new)"], assets=["AST"],
     sound="Silence.", cost="B", map="A", render=None,
     sketch="panel([ship('astrid',110,56,1.3,-3,true), '<ellipse cx=\"100\" cy=\"38\" rx=\"9\" ry=\"4\" fill=\"none\" stroke=\"#cfd6dc\" stroke-width=\"0.8\"/>'], 21)")
shot(act="I", title="Skerry throws", dur=5, clock="T+0:04:10", real="1:1", body="hud",
     cam="HUD insert · the Astrid's telescope feed, 2,000 mm equivalent",
     action="A thread of light runs along Skerry's dark limb: the mass driver throwing. Three rounds leave; the plot tags them ARRIVE T+6:40 · OUR LANE. Then a glare blooms across the feed: Skerry's laser has found the dish.",
     comm=[("ASTRID", "Skerry's thrown three rounds down our lane."), ("ACTUAL", "They'll be hours.")],
     rules=["HO3", "HO5", "O2"], vfx="HUD, telescope grain, dazzle glare", rig=[], assets=["HUD", "SKR", "FX-DAZZLE"],
     sound="Soft sensor tones.", cost="E", map="A", render=None,
     sketch="panel([moon(120,50,26), '<path d=\"M104,38 Q118,30 134,34\" fill=\"none\" stroke=\"#ffe3b0\" stroke-width=\"0.9\"/>', glow(150,30,30,'#f2e8ff',0.35), hud(70,12,100,76), label(74,20,'SKERRY · 3 ROUNDS','#e2603f'), label(74,86,'ARRIVE T+6:40 · OUR LANE','#33b3a2')], 5)")
shot(act="I", title="The picture", dur=5, clock="T+0:09:00", real="compressed 60× (the picture builds over ~5 min)", body="hud",
     cam="HUD insert · the master plot",
     action="The master plot, Maren screen right: Breakwater parked over Site 1; Skerry with its laser and mass driver; the Breakers; the approach line. The fins stay in while Skerry's laser can see them.",
     comm=[("ACTUAL", "Picture's up. Breakwater's right where the brief said.")],
     rules=["O2", "D3"], vfx="HUD", rig=[], assets=["HUD"], sound="Sensor tones.", cost="E", map="A", render=None,
     sketch="panel([hud(16,10,208,80), planet(200,50,9,'right'), label(150,40,'BREAKWATER · SITE 1','#e2603f'), label(120,22,'SKERRY · LASER + DRIVER','#e2603f'), '<ellipse cx=\"200\" cy=\"50\" rx=\"44\" ry=\"20\" fill=\"none\" stroke=\"#9fb0bc\" stroke-width=\"0.5\" stroke-dasharray=\"1 2\"/>', label(120,82,'THE BREAKERS','#9fb0bc'), '<line x1=\"24\" y1=\"50\" x2=\"150\" y2=\"50\" stroke=\"#33b3a2\" stroke-width=\"0.6\"/>', label(24,44,'APPROACH','#33b3a2')], 8)")
shot(act="I", title="Wave one", dur=5, clock="T+0:18:00", real="1:1", body="hull",
     cam="WS · 24 mm · on the Infinity's hull, shaking with each launch",
     action="The Infinity ripple-fires 150 missiles at Skerry's laser, mass driver and depot in fifteen seconds. Pod doors open in waves down the hull and the plumes curve away screen right. Skerry goes first because its laser can burn the fleet's fins all the way in.",
     comm=[("ACTUAL", "Infinity, wave one. Skerry."), ("INFINITY", "Wave one away.")],
     rules=["O3", "O9", "D3"], vfx="150 missiles (swarm system), pod doors", rig=["pod_ripple (new)"],
     assets=["GI", "GI-MAV", "MSL-V", "FX-SWARM"], sound="Launch cracks through the hull; the camera shakes with each.",
     cost="C", map="A", render=None,
     sketch="panel([ship('hedgehog',70,60,1.4,-6,true), trail('M96,50 Q150,30 230,18','#ffd9a0','0.6 0.9',0.8), trail('M96,54 Q150,36 230,26','#ffd9a0','0.6 0.9',0.6), sparks(170,30,26,40,4)], 7)")
shot(act="I", title="Turn and burn", dur=6, clock="T+0:25:00", real="compressed 8× (the turn takes ~49 s)", body="tracker",
     cam="EWS · 400 mm · the whole group",
     action="Through a long lens, fourteen drives light one after another as the group turns onto the approach line: bows toward Maren, plumes streaming screen left. One g for 34 minutes.",
     comm=[("ACTUAL", "All ships, execute. One g.")], rules=["O1", "D2"], vfx="Distant drive plumes",
     rig=[], assets=["AST", "EN", "GI", "DD", "CV", "FX-FAR"], sound="Sub-bass swell.", cost="D", map="A", render=None,
     sketch="panel([plume(60,40,-40,0,1.4), ship('corvette',64,40,1,0,true), plume(96,58,-46,0,1.8), ship('frigate',104,58,0.5,0,true), plume(130,44,-60,0,2.2), ship('endeavorNoShield',150,44,0.35,0,true), plume(170,66,-50,0,2), ship('astrid',196,66,0.3,0,true)], 13)")

# ============================================================ ACT II
shot(act="II", title="Skerry burns", dur=4, clock="T+1:02:00", real="compressed 5× (~20 s of hits)", body="tracker",
     cam="EWS · 1,200 mm · Skerry a quarter-frame disc",
     action="Pinpricks of white on Skerry's limb: wave one arriving, nose-on to the battery. The light left Skerry 0.9 s ago. Just before the hits, a faint spray of points leaves the depot: its drones, flushed toward the shield park.",
     comm=[("ASTRID", "Splash on Skerry. Their laser's gone.")], rules=["O3", "O9", "HO8"],
     vfx="Distant nuclear flashes, flushed drones", rig=[], assets=["SKR", "FX-NUKE"],
     sound="Nothing; a swell of score.", cost="D", map="A", render=None,
     sketch="panel([moon(120,50,22), glow(106,40,6,'#ffffff',0.95), glow(112,34,4,'#ffffff',0.9), glow(100,48,3,'#ffffff',0.8), sparks(86,30,12,16,9)], 9)")
shot(act="II", title="Fins edge-on", dur=6, clock="T+1:10:00", real="compressed; the clock rolls through a 2 h 10 min coast", body="drone",
     cam="MS · 40 mm · arcing round to dead ahead",
     action="With Skerry's laser gone, the four fins run out, glowing a dull red. The camera arcs to dead ahead as they extend, until they collapse to slivers: edge-on to Site 1 and Breakwater, dead ahead. Far behind, the Astrid's eight fins glow like a lantern. The clock rolls on.",
     comm=[("ENDEAVOR", "Fins out. Keep them edge-on.")], rules=["D3"], vfx="Fin glow",
     rig=["radiator_deploy 0.12→1", "heat 0.6", "radiator_glow"], assets=["EN", "AST"],
     sound="Silence; the score carries the coast.", cost="A", map="A", render="img/orbit_v8d.jpg", sketch=None)
shot(act="II", title="The Breakers", dur=4, clock="T+3:20:00", real="1:1", body="drone",
     cam="WS · 24 mm · tracking alongside",
     action="The fins retract before the debris. A faint haze thickens, lit from behind. A single large rock slides past twenty kilometres off, gone across the frame in under two seconds at 20 km/s. The corvettes spread ahead, screen right.",
     comm=[("ACTUAL", "No shields from here. Corvettes, sweep the lane.")], rules=["O8", "D3", "D5", "D6"],
     vfx="Dust haze (Mist pass), one rock fly-by", rig=["radiator_deploy 1→0.12"],
     assets=["EN", "BRK", "CV", "DRN-L"], sound="Silence; a low drone in the score.", cost="B", map="B", render=None,
     sketch="panel([rocks(3,1,40,70,40,60,14,16), ship('endeavorNoShield',130,54,0.7,0,true), ship('corvette',200,40,1.2,0,true), ship('drone',222,48,1.4,0,true), '<rect width=\"240\" height=\"100\" fill=\"#9fb0bc\" opacity=\"0.05\"/>'], 17)")
shot(act="II", title="Blind", dur=3, clock="T+3:30:00", real="1:1", body="hull",
     cam="CU · 85 mm · the sensor mast, with its POV feed inset",
     action="Site 1's beam finds the Endeavor through the haze. The mast's optics flare, the inset feed whites out, and armoured shutters slam shut.",
     comm=[("ENDEAVOR", "Site One's painting us. Shutters.")], rules=["HO5"], vfx="Dazzle bloom, POV whiteout",
     rig=["mast_shutter 0→1 (new)"], assets=["EN", "EN-MAST", "FX-DAZZLE"],
     sound="A static howl on the feed; the shutter slam through the hull.", cost="A", map="B",
     render="img/lookmast_v8d.jpg", sketch=None)
shot(act="II", title="The belt wakes", dur=3, clock="T+3:40:00", real="compressed 10× (~30 s)", body="drone",
     cam="WS · 40 mm · beside a rock ahead of the fleet",
     action="Regolith heaves and petal doors open. Missiles tumble out cold, then light two kilometres clear and turn screen left, toward the fleet. Until now the pods were the temperature of the rock.",
     comm=[("ROCINANTE", "Launch! Cold birds off the rocks!")], rules=["HO2", "HD3"],
     vfx="Pod doors, late motor ignition", rig=["heave / petals (new)"], assets=["EMP-POD", "MSL-V", "BRK"],
     sound="Silence; a sting in the score.", cost="B", map="B", render=None,
     sketch="panel([rocks(8,1,120,180,40,80,26,28), ship('pod',150,48,2.2,0), ship('pod',164,62,1.8,0), trail('M148,48 Q100,30 30,26','#ff9d7a','0.6 1',0.6), glow(70,32,3,'#ffb080',0.9)], 23)")
shot(act="II", title="Spin-up", dur=1, clock="T+3:45:00", real="1:1", body="hull",
     cam="ECU · 100 mm · a CIWS",
     action="Seven barrels blur into motion inside the perforated jacket.",
     comm=[], rules=["D1"], vfx="", rig=["ciws_phase (new)", "ciws_fire (new)"], assets=["EN", "EN-PD"],
     sound="A rising whine through the hull.", cost="A", map="B", render=None,
     sketch="panel([glow(120,50,30,'#2a3037',0.9), '<g fill=\"#9aa6b0\">' + [0,1,2,3,4,5,6].map(function(i){var a=i/7*6.283;return '<circle cx=\"'+(120+Math.cos(a)*14).toFixed(1)+'\" cy=\"'+(50+Math.sin(a)*14).toFixed(1)+'\" r=\"4\"/>';}).join('') + '</g>', '<circle cx=\"120\" cy=\"50\" r=\"24\" fill=\"none\" stroke=\"#6b737b\" stroke-width=\"2\" stroke-dasharray=\"2 2\"/>'], 15)")
shot(act="II", title="Countermeasures", dur=4, clock="T+3:45:01", real="1:1", body="drone",
     cam="MS · 35 mm · along the port flank",
     action="Chaff and flares bloom and a smoke screen unfurls, thinning as it spreads. The CIWS lay kill clouds in the missiles' paths; the laser lenses glow violet, beams invisible. Missiles pop one by one.",
     comm=[("ENDEAVOR", "PD free. Chaff, smoke.")], rules=["D1"],
     vfx="Tracers, kill clouds, chaff, smoke, intercept flashes",
     rig=["ciws_fire (new)", "cm_chaff / cm_flare / cm_smoke (new)", "laser_power 0→1", "laser_traverse"],
     assets=["EN", "EN-PD", "FX-PD", "FX-SMOKE"], sound="Silence (drone camera); the score's pulse.",
     cost="A2", map="B", render="img/lookpair_final.jpg", sketch=None)
shot(act="II", title="The platform", dur=2, clock="T+3:52:00", real="1:1", body="drone",
     cam="WS · 50 mm · over the platform's shoulder",
     action="A buried twin railgun heaves out of a rock 600 km ahead of the fleet and fires a ten-slug pattern screen left, straight down the fleet's path.",
     comm=[], rules=["HO1", "HO2", "HO9"], vfx="Muzzle flashes, slug glints", rig=["unmask / shot (new)"],
     assets=["EMP-RG", "BRK", "FX-SLUG"], sound="Silence.", cost="B", map="B", render=None,
     sketch="panel([rocks(5,1,150,230,50,95,30,32), ship('railplat',160,62,2,0), glow(128,62,5,'#bfe1ff',0.9), streak(126,62,10,48), streak(126,64,8,54)], 29)")
shot(act="II", title="Canterbury", dur=2, clock="T+3:52:05", real="compressed 4× (13 s flight)", body="tracker",
     cam="Tracker · 600 mm · from the Extenuating Circumstances",
     action="The Canterbury, forty kilometres off, jinks hard on RCS, its dish forward.",
     comm=[("EXTENUATING", "Canterbury, jink!")], rules=["D4"], vfx="RCS puffs", rig=[], assets=["DD"],
     sound="Silence.", cost="B", map="B", render=None,
     sketch="panel([ship('destroyer',120,50,3.4,4,true), smoke(80,46,6)], 31)")
shot(act="II", title="Holed", dur=5, clock="T+3:52:13", real="1:1", body="tracker",
     cam="Tracker · 600 mm · holding on the Canterbury",
     action="The slugs arrive from ahead. The Canterbury is holed bow to stern in three white flashes; it vents glittering ice, the hull parts in two and tumbles. Hold on it as its channel dies to hiss.",
     comm=[("EXTENUATING", "Canterbury's gone."), ("ACTUAL", "Extenuating, the net's yours.")],
     rules=["HO9"], vfx="Impact flashes, venting, section break", rig=["break 0→1 (new)"],
     assets=["DD", "DD-BRK", "FX-BREAK", "FX-VENT"], sound="The dying channel's hiss, then silence.",
     cost="C", map="B", render=None,
     sketch="panel([ship('destroyer',110,50,3.2,10,true), glow(150,46,10,'#ffffff',0.85), glow(120,50,7,'#ffffff',0.7), sparks(140,50,30,30,11), smoke(100,56,14)], 33)")
shot(act="II", title="Answer", dur=4, clock="T+3:52:36", real="1:1 (the last degrees of the slew)", body="drone",
     cam="EWS · 135 mm · the Astrid in profile, bow screen right",
     action="The Astrid's 1.6-kilometre hull swings its last few degrees onto the platform, steadies on RCS, and fires down the spinal: a blue-white bloom at the bow.",
     comm=[("ACTUAL", "Astrid, spinal on the platform."), ("ASTRID", "Firing.")], rules=["O4"],
     vfx="Spinal muzzle bloom", rig=["spinal_charge / spinal_shot (new)"], assets=["AST", "FX-SPINAL"],
     sound="A sub-bass punch.", cost="B", map="B", render=None,
     sketch="panel([ship('astrid',110,52,1.1,0,true), glow(176,52,14,'#bfe1ff',0.9), plume(180,52,30,0,3)], 37)")
shot(act="II", title="Payback", dur=3, clock="T+3:54:28", real="the clock jumps 108 s", body="drone",
     cam="WS · 50 mm · the platform shot's framing",
     action="8,600 km away and 108 seconds later, the platform's rock erupts. The platform could not move.",
     comm=[("ASTRID GUNS", "Remember the Cant.")], rules=["O4"], vfx="Impact eruption on the rock",
     rig=[], assets=["EMP-RG", "BRK", "FX-SLUG"], sound="A delayed boom in the score.", cost="B", map="B", render=None,
     sketch="panel([rocks(5,1,150,230,50,95,30,32), glow(168,64,24,'#ffd9a0',0.9), sparks(168,62,50,50,35)], 35)")
shot(act="II", title="Screens out", dur=4, clock="T+4:10:00", real="compressed ~30× (2 min)", body="drone",
     cam="WS · 28 mm · behind the corvettes",
     action="Ahead, cold hides crack open on the rocks and drones pour out. The corvettes fan out to meet them, their own drones ahead.",
     comm=[("NORMANDY", "Drones waking on the rocks. Dozens.")], rules=["HO4", "D6", "O7"],
     vfx="Drone swarms (swarm system)", rig=[], assets=["CV", "DRN-C", "DRN-L", "FX-SWARM", "BRK"],
     sound="A rising whine in the score.", cost="C", map="B", render=None,
     sketch="panel([ship('corvette',60,44,2.4,0,true), ship('corvette',46,62,2,0,true), ship('corvette',70,72,1.8,0,true), sparks(180,46,60,70,41), rocks(9,3,190,235,20,90,6,12)], 41)")
shot(act="II", title="Return to sender", dur=4, clock="T+4:14:00", real="1:1", body="hud",
     cam="HUD insert · the Extenuating Circumstances' plot",
     action="A block of drone tracks flips from red to teal: the drones still on a control link are hijacked and turned on their own swarm. The control craft behind the rocks is found and dazzled; the Canterbury's drifting drones are picked up. The autonomous drones keep coming. Tag: NET DEGRADED · DIRECT LINKS.",
     comm=[("EXTENUATING", "Return to sender.")], rules=["O5", "HD9", "D10"], vfx="HUD, EW overlay",
     rig=[], assets=["HUD", "FX-EW"], sound="Clipped data chatter.", cost="E", map="B", render=None,
     sketch="panel([hud(30,10,180,80), sparks(90,50,24,40,43), '<g opacity=\"0.9\">' + sparks(150,44,24,40,44).replace(/#ffe7b0/g,'#33b3a2') + '</g>', label(34,18,'LINKED ×22 → OURS','#33b3a2'), label(34,86,'AUTONOMOUS ×31','#e2603f'), label(130,18,'NET DEGRADED','#e2603f'), glitch(45)], 45)")
shot(act="II", title="Normandy", dur=3, clock="T+4:25:00", real="1:1", body="tracker",
     cam="Tracker · 300 mm · from the Wallfish",
     action="One autonomous drone slips the screen and dives on the Normandy. A plasma bomb goes off against its flank and the corvette breaks up. Its channel dies to hiss.",
     comm=[("WALLFISH", "One's through—on Normandy!")], rules=["HO4"], vfx="Plasma-bomb flash, break-up",
     rig=["break 0→1 (new)"], assets=["CV", "CV-BRK", "DRN-C", "FX-SWARM", "FX-BREAK"],
     sound="The dying channel.", cost="C", map="B", render=None,
     sketch="panel([ship('corvette',120,50,5,-4,true), glow(128,48,16,'#e3c7ff',0.9), sparks(128,48,40,40,47)], 47)")

# ============================================================ ACT III
shot(act="III", title="Turnover", dur=6, clock="T+4:34:10", real="rotation at ~4×, the middle of the 49 s flip cut out", body="hull",
     cam="WS · 24 mm · on the dorsal hull looking aft",
     action="Under smoke and an EW peak, one ship at a time, the fleet flips. The stars wheel over the hull as the stern swings toward Maren; now the bow points screen left while the ship still travels right. The drive lights: 34 minutes of braking toward Anchor.",
     comm=[("ACTUAL", "Normandy's gone. Turnover, one at a time.")], rules=["D8", "O8"],
     vfx="Main plume, RCS, smoke screen", rig=["rcs_bow / rcs_stern pulses", "engine_throttle 0→1"],
     assets=["EN", "FX-SMOKE"], sound="RCS thumps, then the drive's roar through the hull.", cost="A", map="B", render=None,
     sketch="panel([smoke(60,40,40), '<rect x=\"0\" y=\"80\" width=\"240\" height=\"20\" fill=\"#3a4048\"/>', '<path d=\"M20,20 Q120,-10 220,20\" fill=\"none\" stroke=\"#cfd8e0\" stroke-width=\"0.4\" opacity=\"0.5\"/>', plume(200,78,60,-8,6)], 49)")
shot(act="III", title="Anchor", dur=3, clock="T+5:08:00", real="1:1", body="hud",
     cam="HUD insert · the master plot, zoomed",
     action="Anchor, an 18 km rock, with its shadow cone pointing away from Site 1. The fleet will string out along it; two nearby rocks are tagged '?'. Corner readout: ENDEAVOR SINK 94 %.",
     comm=[("ACTUAL", "Into Anchor's lee.")], rules=["D5", "D2"], vfx="HUD", rig=[], assets=["HUD"],
     sound="Sensor tones.", cost="E", map="C", render=None,
     sketch="panel([hud(16,10,208,80), rocks(2,1,140,152,44,56,6,6.5), '<path d=\"M140,46 L30,40 L30,60 L140,54Z\" fill=\"#33b3a2\" opacity=\"0.15\"/>', label(154,40,'ANCHOR','#33b3a2'), label(200,30,'?','#e2603f'), label(110,80,'?','#e2603f'), label(20,86,'ENDEAVOR SINK 94%','#33b3a2'), '<line x1=\"160\" y1=\"50\" x2=\"220\" y2=\"50\" stroke=\"#e2603f\" stroke-width=\"0.5\" stroke-dasharray=\"2 2\"/>', label(186,46,'SITE 1','#e2603f')], 52)")
shot(act="III", title="The sweep", dur=4, clock="T+5:09:00", real="compressed ~20× (minutes)", body="drone",
     cam="WS · 24 mm · low over Anchor's surface",
     action="The Endeavor settles into darkness in the lee; the rock blocks the sun as well as Site 1. Corvettes and drones sweep the rock: a drone trips a mine on the far side, and the flash lights Anchor's limb from behind. Far off, the Donnager's shells land on the nearest rocks.",
     comm=[("DONNAGER", "Clear inside three hundred. Working outward.")], rules=["O8", "D6", "O4"],
     vfx="Mine flash behind the limb, distant impacts", rig=["rcs_bow / rcs_stern pulses"],
     assets=["EN", "ANCHOR", "BRK", "CV", "DRN-L", "GI", "GI-GUN", "FX-NUKE"], sound="Silence.",
     cost="C", map="C", render=None,
     sketch="panel([rocks(12,1,-40,120,40,160,90,92), glow(40,20,30,'#ffffff',0.5), ship('endeavorNoShield',176,34,0.8,0)], 53)")
shot(act="III", title="Too hot", dur=4, clock="T+5:12:00", real="compressed 5× (the fins take ~20 s)", body="hull",
     cam="MS · 35 mm · on the stern shoulder",
     action="Heat alarms. The slot doors slide open and all four fins telescope out, glowing orange against black: the only light in the lee.",
     comm=[("ENDEAVOR", "Sink ninety-four. Dumping heat.")], rules=["D3", "D5"], vfx="Fin glow, light spill",
     rig=["fin_* 0→1 (new)", "heat 1.9→2.4", "radiator_glow"], assets=["EN", "EN-FIN"],
     sound="Alarm tones; the fins' hydraulic groan.", cost="A", map="C",
     render="img/lookaft_s1combat.jpg", sketch=None)
shot(act="III", title="Fins in", dur=4, clock="T+5:13:00", real="compressed ~4× (the fins crawl in against a 16 s flight)", body="hull",
     cam="MS · 35 mm · the same shoulder, the clock large",
     action="A flash on a rock 400 km off the port quarter, a half-second glimpse of the platform. The fins start in, crawling against the clock.",
     comm=[("ENDEAVOR", "Launch, four hundred! Fins in!")], rules=["HO7", "HO1", "D3"],
     vfx="Distant muzzle flash", rig=["fin_* 1→0.5 (new)"], assets=["EN", "EN-FIN", "EMP-RG"],
     sound="The call; alarms; the fins' groan.", cost="A", map="C", render=None,
     sketch="panel([ship('endeavorNoShield',110,50,1.9,0), glow(236,10,4,'#bfe1ff',0.9), label(8,92,'T+5:13:09','#6fd3c4')], 55)")
shot(act="III", title="Fin hit", dur=3, clock="T+5:13:16", real="1:1", body="hull",
     cam="CU · 50 mm · on the port fin",
     action="Halfway in, the port fin takes a slug. It shatters into glowing shards and its coolant flashes to glittering ice.",
     comm=[("ENDEAVOR", "Port fin's gone. Cut it loose.")], rules=["HO7", "D7"], vfx="Fin shatter, coolant venting",
     rig=["fin_port_state → pre-fractured (new)"], assets=["EN", "EN-FIN", "FX-FIN", "FX-VENT", "FX-SLUG"],
     sound="Metal shear through the hull; a hiss.", cost="A2", map="C", render=None,
     sketch="panel([ship('endeavorNoShield',110,50,1.9,0), glow(176,24,12,'#ff8a3c',0.8), sparks(178,22,40,36,55), smoke(184,20,16), streak(10,4,172,22,'#8fb1ff')], 57)")
shot(act="III", title="Off the port bow", dur=4, clock="T+5:13:30", real="1:1", body="hull",
     cam="Hull camera · 600 mm · on the Endeavor's port side",
     action="A Compact frigate clears a moonlet 45 km off the port bow and fires its coilgun. Two seconds later the camera shakes as the slug spalls the port belt.",
     comm=[("DONNAGER", "Frigate, off your port bow!")], rules=["HO6", "O6"], vfx="Coilgun flash, hull spall",
     rig=["dmg_belt 0→1 (new)"], assets=["CF", "ANCHOR", "EN", "EN-DMG", "FX-SLUG"],
     sound="The hit through the hull.", cost="A2", map="C", render=None,
     sketch="panel(['<rect x=\"0\" y=\"82\" width=\"240\" height=\"18\" fill=\"#3a4048\"/>', rocks(21,1,120,200,30,70,18,20), ship('hfrigate',150,44,3,0), glow(128,44,6,'#bfe1ff',0.9)], 59)")
shot(act="III", title="Lance channels", dur=2, clock="T+5:13:53", real="1:1", body="hull",
     cam="CU · 28 mm · the Endeavor's nose",
     action="The four lance channels in the nose glow violet-white as the field builds.",
     comm=[("ENDEAVOR", "Lance. Now.")], rules=["O12"], vfx="Lance core glow", rig=["lance_power 0→1"],
     assets=["EN"], sound="A rising electric whine through the hull.", cost="A", map="C", render=None,
     sketch="panel([ship('endeavorNoShield',210,50,2.6,0), glow(114,50,10,'#e3c7ff',0.9)], 61)")
shot(act="III", title="Lance", dur=2, clock="T+5:13:55", real="1:1", body="tracker",
     cam="Tracker · 1,000 mm · on the frigate, 40 km out",
     action="The ship's field reaches out and a spear of plasma runs from the nose to the frigate, forty kilometres off, well inside the ~50 km the field can hold. The frigate's midsection opens; escape pods scatter as it breaks.",
     comm=[], rules=["O12", "O6"], vfx="Field-held plasma jet, break-up",
     rig=["break 0→1 (new)"], assets=["CF", "FX-LANCE", "FX-BREAK", "FX-VENT"],
     sound="A crack in the score.", cost="C", map="C", render=None,
     sketch="panel(['<line x1=\"0\" y1=\"54\" x2=\"118\" y2=\"50\" stroke=\"#e3c7ff\" stroke-width=\"2.2\"/>', ship('hfrigate',140,50,3.2,0), glow(120,50,12,'#e3c7ff',0.9), sparks(140,50,40,40,63)], 63)")
shot(act="III", title="Broadside", dur=6, clock="T+5:14:00", real="the roll at 5× (3 s), then 1:1 (3 s)", body="hull",
     cam="MS · 35 mm · the port batteries, the rock beyond",
     action="Fins stowed, the Endeavor rolls to bring its port batteries onto the platform's rock off the port quarter. The dorsal well battery rises; the M-1Cs wake, charge and fire in sequence, and only the gun that fired vents.",
     comm=[("ENDEAVOR", "Batteries up. Fire.")], rules=["O6", "O4", "D3"], vfx="M-1C tracer blasts",
     rig=["rail_traverse", "rail_elevation", "battery_raise 0→1", "battery_traverse", "battery_elevation", "rail_wake", "rail_lock", "rail_arm", "charge_a/b", "shot_a/b", "fins_a/b", "heat_a/b"],
     assets=["EN", "M1C"], sound="Each shot's crack and recoil clunk through the hull.",
     cost="A2", map="C", render="img/house_s1combat.jpg", sketch=None)
shot(act="III", title="The platform dies", dur=2, clock="T+5:14:31", real="the clock jumps 13 s (16 s of flight)", body="tracker",
     cam="Tracker · 1,200 mm · the glimpse's framing",
     action="The platform's rock flashes: sixteen seconds of flight, and a target that could not move.",
     comm=[], rules=["O4"], vfx="Impact flash", rig=[], assets=["EMP-RG", "BRK", "FX-SLUG"],
     sound="The score.", cost="B", map="C", render=None,
     sketch="panel([rocks(19,1,90,150,30,70,28,30), glow(120,50,20,'#ffd9a0',0.9), sparks(120,50,40,40,65)], 65)")

# ============================================================ ACT IV
shot(act="IV", title="The fire plan", dur=5, clock="T+5:40:00", real="1:1", body="hud",
     cam="HUD insert · the master plot",
     action="The plan on the plot: where Breakwater will be at T+7:52, the waves' straight tracks from Anchor, and the Astrid's firing point 10,800 km out, 15° off Breakwater's zenith. Every line of fire clears Maren. The pack stays at Anchor as a fire base. Four labels: SPEND 7:52 · KILL 7:53; RESERVE ~700; FIRING LINE 15°; 2 FRIGATES · LIMB. The corner readout adds PARK HOLDING under SINK 31 % · FINS 3/4.",
     comm=[("ACTUAL", "That's the plan. Pack holds Anchor. The rest, with me.")],
     rules=["O9", "O3", "O10", "O11", "HO6", "HO8", "D11"], vfx="HUD", rig=[], assets=["HUD"],
     sound="Sensor tones; the score gathers.", cost="E", map="D", render=None,
     sketch="panel([hud(16,10,208,80), planet(196,60,12,'right'), ship('monitor',176,40,0.1,0), '<line x1=\"40\" y1=\"30\" x2=\"174\" y2=\"40\" stroke=\"#33b3a2\" stroke-width=\"0.6\" stroke-dasharray=\"1 1.5\"/><line x1=\"150\" y1=\"20\" x2=\"174\" y2=\"38\" stroke=\"#b476ff\" stroke-width=\"0.6\"/>', label(112,16,'FIRING LINE 15°','#b476ff'), rocks(2,1,30,38,26,34,4,4.5), label(22,44,'ANCHOR · PACK','#33b3a2'), label(60,24,'SPEND 7:52 · KILL 7:53','#33b3a2'), label(20,86,'SINK 31% · FINS 3/4 · PARK HOLDING','#33b3a2'), label(150,86,'2 FRIGATES · LIMB','#e2603f')], 67)")
shot(act="IV", title="The net", dur=5, clock="T+6:40:00", real="compressed ~24× (2 min)", body="drone",
     cam="WS · 50 mm · over the Extenuating Circumstances",
     action="Hours after Skerry threw them, its rounds arrive. Ahead of the fleet the destroyer's drones light up a spreading cloud of pellets about 20 km across, glittering in their lamps. The fleet side-steps, drives angled off the line.",
     comm=[("EXTENUATING", "Skerry's rounds. Right on time."), ("ACTUAL", "All ships, left two degrees.")],
     rules=["HO3", "D4", "O8"], vfx="Canister cloud glitter (swarm system)", rig=[],
     assets=["DD", "DRN-L", "FX-SWARM"], sound="Silence; the score ticks.", cost="B", map="D", render=None,
     sketch="panel([ship('destroyer',50,60,1.6,0,true), sparks(170,40,90,70,67), glow(150,30,10,'#e8f2ff',0.3)], 67)")
shot(act="IV", title="Site One", dur=4, clock="T+6:55:00", real="compressed ~15× (a minute)", body="drone",
     cam="WS · 40 mm · ahead of the Extenuating Circumstances",
     action="Site 1's beam, invisible, finds the fleet. The destroyer's forward sensor boom scorches and smokes: the one visible cost. The fleet doesn't fire back, since every laser shot would heat the sinks. The ships begin a slow roll to spread the heat, and a grey smoke screen blooms ahead of the fleet, travelling with it.",
     comm=[("EXTENUATING", "Site One's on our booms. Smoke forward.")], rules=["HO5", "D1", "D3"],
     vfx="Scorching, smoke screen", rig=[], assets=["DD", "FX-SMOKE", "FX-DAZZLE"],
     sound="Silence.", cost="B", map="D", render=None,
     sketch="panel([ship('destroyer',90,56,2.2,-6,true), smoke(118,40,10), smoke(200,50,40), glow(122,40,4,'#ff8a3c',0.8)], 69)")
shot(act="IV", title="The anvil", dur=4, clock="T+7:25:00", real="compressed 10× (the ripple takes ~40 s)", body="drone",
     cam="WS · 40 mm · above Breakwater, Maren's night side below",
     action="Breakwater's reveal. Its turrets track the fleet but stay silent: the fleet never comes within the range they could hit. Its 64 cells open and ripple-fire, every missile at the Extenuating Circumstances, 17,000 km off. Far along the orbit, ring stations wake as points of light.",
     comm=[("ASTRID", "Sixty-four inbound. All on Extenuating.")], rules=["HD7", "HO9", "HD1", "HO1", "D1"],
     vfx="Cell doors, missile launch (swarm system)", rig=["turret_traverse / cells_open (new)"],
     assets=["BW", "RING", "MAREN", "MSL-V", "FX-SWARM"], sound="A low brass sting.", cost="C", map="E", render=None,
     sketch="panel([planet(120,160,120,'right'), ship('monitor',120,34,0.9,0), trail('M86,30 Q50,20 10,24','#ff9d7a','0.6 1',0.6), trail('M86,36 Q50,34 10,40','#ff9d7a','0.6 1',0.6), sparks(226,90,6,10,71)], 71)")
shot(act="IV", title="The pack fires", dur=4, clock="T+7:27:00", real="1:1", body="drone",
     cam="WS · 24 mm · low over Anchor, looking toward Breakwater",
     action="From Anchor's shadow the Infinity ripple-fires everything it has left: the spend wave, hundreds of plumes streaming away toward Breakwater, 118,000 km off.",
     comm=[("ACTUAL", "Spend wave, go."), ("INFINITY", "Spend wave away. We're dry.")], rules=["O3", "O11"],
     vfx="Ripple launch (swarm system)", rig=["pod_ripple (new)"],
     assets=["GI", "GI-MAV", "MSL-V", "FX-SWARM", "ANCHOR"], sound="Silence; the score drops out.",
     cost="C", map="D", render=None,
     sketch="panel([rocks(14,1,-20,60,60,120,50,52), ship('hedgehog',90,40,1.1,-4), ship('hedgehog',120,62,0.9,-4), trail('M112,38 Q170,28 240,24','#ffd9a0','0.6 0.9',0.8), trail('M136,60 Q190,44 240,40','#ffd9a0','0.6 0.9',0.7), sparks(200,34,30,40,63)], 73)")
shot(act="IV", title="Kill wave away", dur=3, clock="T+7:28:30", real="1:1", body="tracker",
     cam="Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow",
     action="Ninety seconds behind the spend wave, pod doors open down the Galactica's hull and the kill wave leaves: Casaba killers, EW missiles and decoys. In the foreground the Pillar of Autumn's pods stay shut: the reserve.",
     comm=[("GALACTICA", "Kill wave away.")], rules=["O3", "O10", "O11"],
     vfx="Ripple launch (swarm system)", rig=["pod_ripple (new)"],
     assets=["GI", "GI-MAV", "MSL-V", "FX-SWARM", "ANCHOR"], sound="Silence.",
     cost="C", map="D", render=None,
     sketch="panel([rocks(15,1,190,250,-10,30,40,42), ship('hedgehog',60,78,2.4,-3), ship('hedgehog',150,40,1.1,-4), trail('M172,36 Q208,26 240,22','#ffd9a0','0.6 0.9',0.8), trail('M172,42 Q208,38 240,36','#ffd9a0','0.6 0.9',0.7), sparks(212,30,30,30,64)], 74)")
shot(act="IV", title="Umbrella", dur=3, clock="T+7:31:00", real="1:1", body="tracker",
     cam="Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 20 km above",
     action="Breakwater's missiles arrive. Above the destroyer the braking Astrid's lenses glow violet and its CIWS lay kill clouds across the missiles' path. The flashes walk in toward the Extenuating and stop short.",
     comm=[("EXTENUATING", "Sixty-four down. Thanks, Actual.")], rules=["D1", "D2", "D10", "HO9"],
     vfx="Kill clouds, intercept flashes, lens glow, the Astrid's drive plume", rig=["ciws_phase / ciws_fire (new, on the Astrid)"],
     assets=["AST", "MSL-V", "FX-PD", "FX-SWARM", "FX-FAR"], sound="Silence; the score's pulse.",
     cost="C", map="E", render=None,
     sketch="panel([plume(167,40,60,0,4), ship('astrid',110,40,1.0,0), tracers(150,34,-15,40,91), glow(206,22,6,'#ffffff',0.85), glow(222,44,4,'#ffffff',0.7), glow(196,58,5,'#ffffff',0.6), sparks(210,36,40,50,92)], 91)")
shot(act="IV", title="Blind it", dur=3, clock="T+7:50:00", real="1:1", body="hull",
     cam="MS · 35 mm · the Endeavor's laser arrays",
     action="The Extenuating Circumstances floods the ring's links. Every array in the fleet turns on Breakwater's optics and Site 1's trackers: lenses violet, beams invisible.",
     comm=[("EXTENUATING", "Their net's down."), ("ENDEAVOR", "All arrays, dazzle.")], rules=["O5", "HD9"],
     vfx="Lens glow, EW overlay on inserts", rig=["laser_power 1", "laser_traverse", "laser_elevation"],
     assets=["EN", "FX-EW"], sound="The lenses' capacitor whine through the hull.", cost="A", map="E",
     render="img/lookyoke_final.jpg", sketch=None)
shot(act="IV", title="The spend wave", dur=3, clock="T+7:52:00", real="1:1", body="tracker",
     cam="Tracker · 800 mm · from the Astrid, over Maren's limb",
     action="Over the limb, a sparkle: the spend wave dying against Breakwater's point defence, which lights up and gives away every battery. On the plot, the destroyer steers the kill wave around them.",
     comm=[], rules=["O3", "O5", "HD5"], vfx="Distant PD sparkle", rig=[], assets=["BW", "FX-PD", "MAREN"],
     sound="The score.", cost="D", map="E", render=None,
     sketch="panel([planet(170,150,110,'right'), sparks(150,36,40,30,75)], 75)")
shot(act="IV", title="Wall of fire", dur=4, clock="T+7:53:28", real="slowed 5× (the wave arrives within ~1 s)", body="drone",
     cam="WS · 40 mm · above Breakwater",
     action="The kill wave arrives in the same second, nose-on to Breakwater, from the rock's side. Tracers and dying decoys fill the sky; the hardened noses keep coming.",
     comm=[("GALACTICA", "Kill wave. Three, two—")], rules=["O3", "HD5", "O9"],
     vfx="Tracer streams, intercept flashes, swarm", rig=[], assets=["BW", "FX-PD", "FX-SWARM", "MSL-V"],
     sound="A dense crackle in the score; no air, no bangs.", cost="C", map="E", render=None,
     sketch="panel([ship('monitor',120,62,1.0,0), tracers(120,58,-90,60,73), sparks(120,24,50,120,74)], 77)")
shot(act="IV", title="Casaba", dur=4, clock="T+7:53:30", real="slowed 3×", body="drone",
     cam="WS · 35 mm · off Breakwater's quarter",
     action="Two kilometres out, the surviving Casaba charges fire: nuclear jets lance into Breakwater's drive bells and its engines go dark. The monitor is whole, but it can no longer move.",
     comm=[("ASTRID", "Spears in. Her drive's dark.")], rules=["O10"], vfx="Casaba jets, drive breach, venting",
     rig=["drive_glow 1→0 (new)", "vent (new)"], assets=["BW", "BW-BRK", "FX-CASABA", "FX-VENT"],
     sound="White noise, then silence.", cost="C", map="E", render=None,
     sketch="panel([ship('monitor',120,50,1.0,0), '<line x1=\"240\" y1=\"20\" x2=\"174\" y2=\"48\" stroke=\"#ffffff\" stroke-width=\"1.3\"/><line x1=\"238\" y1=\"84\" x2=\"174\" y2=\"54\" stroke=\"#ffffff\" stroke-width=\"1.1\"/>', glow(172,50,12,'#ffffff',0.85)], 79)")
shot(act="IV", title="The hail", dur=5, clock="T+7:54:00", real="1:1", body="drone",
     cam="MS · 50 mm · slow push on Breakwater over the night side",
     action="Breakwater hangs dead-engined over Maren's night side, venting from the spear wounds, its turrets still tracking. On an open channel the Astrid hails it. No answer comes.",
     comm=[("ACTUAL", "Breakwater, you can't move. Strike, or we fire.")], rules=["O10"],
     vfx="Venting", rig=["vent (new)"], assets=["BW", "BW-BRK", "MAREN", "FX-VENT"],
     sound="Silence where the answer should be.", cost="B", map="E", render=None,
     sketch="panel([planet(120,170,120,'right'), sparks(60,92,20,40,81), ship('monitor',120,40,1.0,0), smoke(170,44,12)], 81)")
shot(act="IV", title="Spinal", dur=3, clock="T+7:54:37", real="1:1 (the last degree of the slew; it fires at T+7:54:40)", body="drone",
     cam="EWS · 200 mm · the Astrid end-on",
     action="The Astrid, stopped 10,800 km out and 15° off Breakwater's zenith so a miss would clear Maren, settles its last degree and fires.",
     comm=[("ACTUAL", "Fire.")], rules=["O4", "O10", "HD7", "O9"], vfx="Spinal muzzle bloom",
     rig=["spinal_shot (new)"], assets=["AST", "FX-SPINAL"], sound="Everything drops out.", cost="B", map="E", render=None,
     sketch="panel([glow(120,50,36,'#bfe1ff',0.8), '<circle cx=\"120\" cy=\"50\" r=\"10\" fill=\"#cfd6dc\"/>', '<g stroke=\"#ff8a3c\" stroke-width=\"2\">' + [0,1,2,3,4,5,6,7].map(function(i){var a=i/8*6.283;return '<line x1=\"'+(120+Math.cos(a)*12).toFixed(1)+'\" y1=\"'+(50+Math.sin(a)*12).toFixed(1)+'\" x2=\"'+(120+Math.cos(a)*34).toFixed(1)+'\" y2=\"'+(50+Math.sin(a)*34).toFixed(1)+'\"/>';}).join('') + '</g>', glow(120,50,8,'#ffffff',0.95)], 83)")
shot(act="IV", title="Three minutes", dur=4, clock="T+7:54:40", real="compressed 45× (180 of the slug's 184 s; the clock races)", body="drone",
     cam="WS · 35 mm · the Casaba shot's angle",
     action="Hold on the crippled monitor, turrets swinging uselessly, while the clock races through the slug's three minutes.",
     comm=[("ASTRID", "Impact in three minutes.")], rules=["O10"], vfx="Venting", rig=["turret_traverse (new)"],
     assets=["BW", "BW-BRK"], sound="Silence; one held note.", cost="B", map="E", render=None,
     sketch="panel([ship('monitor',120,50,1.0,0), smoke(172,50,14), label(8,92,'T+7:56:10','#6fd3c4')], 85)")
shot(act="IV", title="Impact", dur=3, clock="T+7:57:44", real="1:1", body="drone",
     cam="WS · 35 mm · the Casaba shot's angle",
     action="The slug arrives amidships, near the spear damage: a white flash, a spall cone, and Breakwater's back breaks in a chain of secondary flashes.",
     comm=[], rules=["O4"], vfx="Impact, spall, section break", rig=["break 0→1 (new)"],
     assets=["BW", "BW-BRK", "FX-SPINAL", "FX-BREAK"], sound="One deep boom on the cut.", cost="C", map="E", render=None,
     sketch="panel([ship('monitor',120,50,1.2,12), glow(120,50,26,'#ffd9a0',0.8), sparks(120,50,70,60,83), smoke(130,56,30)], 87)")
shot(act="IV", title="Heat", dur=4, clock="T+8:00:00", real="1:1", body="hull",
     cam="MS · 35 mm · along the Endeavor's scorched port flank",
     action="The Endeavor's sink reads 98 %. A valve opens and a thousand tonnes of water boil out in a white plume streaming off the ship: twenty-five minutes of margin.",
     comm=[("ENDEAVOR", "Sink ninety-eight. Dump the water.")], rules=["D3", "D7"], vfx="Water-dump plume",
     rig=["water_dump 0→1 (new)"], assets=["EN", "EN-PD", "FX-VENT"],
     sound="A roar through the hull, then a long hiss.", cost="A2", map="E", render=None,
     sketch="panel([ship('endeavorNoShield',150,50,1.2,0), glow(120,30,20,'#e8eef4',0.6), glow(92,20,24,'#e8eef4',0.4), glow(60,12,26,'#e8eef4',0.25)], 89)")
shot(act="IV", title="Terms", dur=5, clock="T+8:10:00", real="1:1", body="tracker",
     cam="Tracker · 2,000 mm · from the Endeavor's standoff",
     action="Far off, 8,500 km away, Breakwater's wreck is a glittering smear venting over the night side. On the last plot two channels stay dark: Canterbury, Normandy.",
     comm=[("EXTENUATING", "Actual, Maren's asking for terms."), ("ACTUAL", "Site One goes dark first.")],
     rules=[], vfx="Distant wreck, HUD tag", rig=[], assets=["BW-BRK", "MAREN", "HUD"],
     sound="The score, low.", cost="D", map="E", render=None,
     sketch="panel([planet(120,170,120,'right'), sparks(120,50,30,20,90), glow(120,50,6,'#ffd9a0',0.6), label(8,92,'CANTERBURY · NORMANDY — NO CARRIER','#9fb0bc')], 90)")
shot(act="IV", title="Hold", dur=9, clock="T+8:24:00", real="1:1", body="drone",
     cam="EWS · 35 mm · locked off, the Endeavor end-on",
     action="On Maren's night side a cluster of lights goes dark: Site 1. The Endeavor, end-on, runs out its three fins (already part-way out) into a broken cross glowing orange against the night side, the stump where the fourth was. Cut to black.",
     comm=[("ENDEAVOR", "Site One's dark."), ("ACTUAL", "Nauvoo, bring the shields in. T-SEC, the sky's yours.")],
     rules=["D3"], vfx="Fin glow, city lights going out",
     rig=["fin_starboard / fin_dorsal / fin_ventral 0.5→1 (new)", "heat 2.4", "radiator_glow"],
     assets=["EN", "EN-FIN", "MAREN", "WORLD"], sound="The score resolves; then silence.",
     cost="B", map="E", render="img/hero_s1combat.jpg", sketch=None)

SHOTS = S
