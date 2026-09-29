"""Operation Tidebreak: storyboard data (phase 2, revision 3).

One source for the storyboard page, shots.csv, shots.md and ASSET_REQUESTS.md.
Build with:  python3 storyboard/build_storyboard.py

Revision 3 applies the round 2 reviews (review/round2/*.md, synthesis in
review/round2/synthesis.md) and adds the user's five weapon close-ups
(Birds away, Lenses, Rails wake, Fire, Seeker).

Conventions
- `dur` is screen time in seconds at 24 fps; frames are computed from it.
- `clock` is real mission time at the start of the shot (T+h:mm:ss from warp exit).
- `real` says how the shot treats time: "1:1", "compressed N×", "slowed N×", or a clock jump.
  Every jump of 30 minutes or more says the digits roll. `end` gives the end clock
  when the rate can't be stated as one number.
- `body` is the camera body (CAMERA_BODIES): only hull cameras hear the ship.
- `hud` lists the text on screen besides the subtitles (plot labels, the SINK readout);
  it counts toward the reading-speed ceiling.
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
REVISION = "Revision 3 · after review round 2"
FPS = 24
FORMAT = "2.39:1 · 1920×804 · 24 fps · Cycles"
SHIELDS_OFF = "T+0:02:00"   # the shields leave the ships; sketches drop them from here on

# ---------------------------------------------------------------- mission
PHASES = [
    ("T+0:00", "T+0:25", "Arrival", "Exit at 450,000 km, near rest relative to Maren. Shields parked with the Nauvoo (T+0:02). Net up. Skerry starts throwing (T+0:04; three rounds every ten minutes) and its laser dazzles the Astrid's dish, so the fins stay in. Wave one away at Skerry (T+0:18)."),
    ("T+0:25", "T+0:59", "Turn and burn", "1 g along the approach line for 34 min: 0 → 20 km/s over 20,400 km."),
    ("T+0:59", "T+3:20", "Coast", "20 km/s, bow on Maren. Skerry's laser dies at T+1:02 and its depot flushes 40 drones toward the shield park; the fins come out edge-on at T+1:10."),
    ("T+3:20", "T+4:34", "The Breakers", "Fins stowed in the debris. Site 1 dazzles; the pods wake; the Canterbury is lost (T+3:52); the Astrid answers; drones wake; the Normandy is lost (T+4:25)."),
    ("T+4:34", "T+5:09", "Turnover", "Flip (49 s) and brake at 1 g for 34 min, ending on Anchor's orbital velocity (1.63 km/s; thrust tilted ~4.7°)."),
    ("T+5:09", "T+5:43", "Anchor", "An 18 km rock that at T+5:09 lies over Site 1. The fleet sweeps it (a mine) but can't finish before the heat forces the fins out; it loses the port fin to a platform 400 km off, lances a frigate hidden on a moonlet, kills the platform, and vents again with three fins (94 % → 31 %)."),
    ("T+5:43", "T+7:51", "Final approach", "The pack stays at Anchor as a fire base, guarded by the Donnager and the Wallfish, in the slot of the rock's shadow that hides it from Site 1 and, after T+6:55, the western site. The rest fly an inertial path of ~113,000 km: 1 g to 20 km/s (burn tilted ~4.5° to cancel the rock's orbital velocity), coast, a turnover at T+7:16 under smoke and an EW peak, one ship at a time (D8), then brake to a stop ~8,500 km from Breakwater (T+7:51), matching its orbit. The Astrid, trailing, stops 10,000 km out. Site 1 dazzles and burns from the moment the fleet clears the shadow; the fleet rolls, lays smoke and dazzles back at low power. Skerry's five nets on the lane from T+6:40, ten minutes apart, side-stepped one by one; its sixth salvo rings Anchor at T+6:52. Breakwater's 64 missiles at the Extenuating (T+7:25), killed under the Astrid's umbrella (T+7:31)."),
    ("T+7:07", "T+7:58", "Hammer and anvil", "The waves leave Anchor in two parts so each lands within a second. The slow multi-packs go first (T+7:07 and T+7:08:30; 45 min flights), then the killers (T+7:27 and T+7:28:30; 25 min). The spend wave (the Infinity, ~570) lands at T+7:52:00; the kill wave (the Galactica: ~40 Casaba killers among ~300 decoy and EW birds) at T+7:53:30. Both fly straight in, nose-on to Breakwater and ~48° off its zenith, so misses and wreckage clear Maren. The Casaba jets cut the drive. The Astrid hails, then fires from rest at T+7:54:40, 15° off Breakwater's zenith; impact T+7:57:27."),
    ("T+7:58", "T+8:24", "Terms", "The Endeavor's arrays stand down when Breakwater dies; the Astrid keeps Site 1 dazzled. Sink 98 %: the Endeavor dumps water (T+8:00), which buys it to ~T+8:30. Maren asks for terms (T+8:10). Site 1 goes dark; the fleet vents at last (T+8:24)."),
]

KEY_NUMBERS = [
    ("Warp exit and shield park", "450,000 km from Maren", "LREF O1, A-01/A-02"),
    ("The Breakers", "120,000–260,000 km, ±25°", "Defence §4.1"),
    ("Anchor (the rock)", "~18 km, 150,000 km out; over Site 1 at T+5:09; drifts 12.8°/h relative to Site 1", "D5"),
    ("Skerry", "380,000 km, 40° off the approach line; mass driver throws at up to 15.5 km/s (13.5–15.5 for the lane salvos, 12.5 for the one aimed at Anchor)", "H-14"),
    ("Breakwater", "synchronous orbit, 42,164 km, over Site 1", "H-04"),
    ("Cruise speed", "20 km/s (O8)", "WN §6"),
    ("Burns and flips", "1 g, 34 min; flips 49 s (Endeavor), 58 s (Astrid)", "WN §6"),
    ("Final approach", "~113,000 km from Anchor; turnover T+7:16; the escorts stop ~8,500 km from Breakwater and match its orbit, the Astrid stops 10,000 km out", "WN §6"),
    ("The pack's missiles", "~2,100: wave one 150; spend wave ~570 (~480 multi-packs + ~90 killers); kill wave ~340 (~300 decoy and EW multi-packs + ~40 Casaba killers); ~1,100 held in reserve", "A-26, O11, WN §3"),
    ("Lines of fire", "The waves arrive ~48° off Breakwater's zenith, the spinal shot 15° off it. Maren fills ±8.7° around Breakwater's nadir, so misses and wreckage clear it: a wave's by ~25,000 km, a spinal miss (aimed ahead of the moving monitor) by ~7,000 km", "O9, §13"),
    ("Site 1 against the waves", "~15 kills per wave: aimed at Breakwater, the waves never come within ~36,000 km of it", "WN §8"),
    ("Spinal shot", "from rest at 10,000 km; flight ~167 s, about 17 s inside the time a crippled monitor needs to clear its own length (no-escape ~10,800 km with the range opening)", "WN §2, O10"),
    ("Endeavor heat", "20 TJ sink: 94 % at Anchor, 31 % leaving it, 98 % at T+8:00; a 1,000 t water dump buys it to ~T+8:30", "WN §4, A-32"),
    ("Light-lag", "0.87 s to Skerry at T+1:02; 0.48 s from Anchor to Site 1", "WN §5"),
]

# ---------------------------------------------------------------- film rules
LIGHTING = [
    "The sun sits behind Maren, about 30° off the approach line. From the fleet Maren is a thin crescent with a bright limb, and the Breakers glow faintly lit from behind (dust scatters forward).",
    "Hulls are lit hard from ahead and to one side; the shadow side falls to black. No stars behind sunlit hulls.",
    "Anchor's lee faces away from both Site 1 and the sun. The Endeavor sits within ~9 km of the rock's surface, where the two shadows overlap, so the fins, muzzle flashes and the lance light the scene (the M-1C 'fins1dark' look).",
    "At the end Site 1 is on the night side: a long lens sees its lights go out, and the final frame puts the Endeavor against the night side's city lights.",
]
CLOCK_HUD = [
    "The mission clock is small, persistent and clear of the subtitles. It starts on the flash in shot {#Black, then a star} (T+0:00:00).",
    "It runs at the shot's rate: spinning seconds mean compressed time, crawling ones slowed. Every jump of 30 minutes or more rolls the digits.",
    "One master tactical plot, always with Maren screen right. Geography inserts hold for at least 5 s, and their labels count toward the reading-speed ceiling like subtitles.",
    "The SINK readout appears only on HUD inserts and on hull-camera shots where the heat matters, with values that build to the dump: 94 % ({#Too hot}), 31 % ({#The fire plan}), 62 % ({#Anchor ringed}), 88 % ({#Blind it}), 98 % ({#Heat}).",
    "Subtitles and the clock go in during the edit, after the grade, so a changed line never forces a re-render.",
]
SCREEN_DIRECTION = [
    "Maren and the enemy stay screen right. The LREF travels and fires left to right.",
    "Until the turnover (shot {#Turnover}) bows point right. After it bows point left while travel stays left to right, so the drives burn toward screen right.",
    "The final approach repeats the pattern: bows right from Anchor to the second turnover (T+7:16), bows left while braking, and the Astrid swings its bow back to screen right for the spinal shot.",
    "At Anchor the Endeavor's bow points at the frigate's moonlet. The frigate, off the port bow, is the one enemy on screen left; the platform, off the port quarter, stays screen right. Shots {#The flash}–{#The platform dies} share that axis: the platform's slugs and the broadside cross from and toward the right, the lance from right to left.",
    "The kill wave, the Casaba jets and the spinal slug come in from screen left, the side the waves and the Astrid are on, and Breakwater faces them from screen right ({#Seeker}–{#Impact}).",
    "Enemy reverses only over an enemy foreground.",
]
CAMERA_BODIES = {
    "hull": "Hull camera: bolted to a ship, shakes with it, and is the only body that hears (sound through structure).",
    "drone": "Drone camera: free-flying, silent; score and sub-bass only.",
    "tracker": "Tracker: a long lens (300–2,000 mm) on a ship or drone; heavy slow pans, sensor noise; silent.",
    "hud": "HUD insert: 2D compositing, UI tones only.",
}
# World presets, one per map (render batches follow them).
ENVS = {
    "A": "arrival and coast (sunlit crescent, Maren 1.6°)",
    "B": "the Breakers (backlit haze)",
    "C": "Anchor's dark lee",
    "D": "the final approach (Maren growing, night side)",
    "E": "Breakwater over Maren's night side",
}
# How the hero objects change through the film. The builder shows the state on each
# shot that uses the asset, and checks that the listed state assets are in those shots.
STATES = {
    "EN": [("T+0:00:00", "shield on, four fins"), ("T+0:02:00", "shield parked, four fins"),
           ("T+5:13:16", "port fin shattering"), ("T+5:13:19", "port fin a stump"),
           ("T+5:13:32", "port fin a stump, port belt scorched")],
    "DD": [("T+0:00:00", "intact"), ("T+6:55:00", "Extenuating: forward boom scorched")],
    "BW": [("T+0:00:00", "intact"), ("T+7:53:30", "drive breached, venting"), ("T+7:57:27", "back broken")],
}
STATE_ASSETS = [("EN", "T+5:13:16", "EN-FIN"), ("EN", "T+5:13:32", "EN-DMG"),
                ("BW", "T+7:53:30", "BW-BRK")]

# ---------------------------------------------------------------- forces
FLEET = [
    ("L.R.E.F.S. Astrid", "Hanuman heavy cruiser, 1.6 km", "Flagship, 'Tidebreak Actual'. Spinal cannon, AVPSA, PD anchor. Trails the line; stops behind the escorts and fires from rest."),
    ("L.R.E.F.S. Endeavor", "Ryland cruiser", "The line. Loses its port fin at Anchor. Its 16 VLS cells stay loaded as the fast reserve: ~4 min to Breakwater from the stop."),
    ("Infinity · Pillar of Autumn · Galactica", "Hedgehog frigates (~700 missiles each)", "Wave one (the Infinity, 150 killers). The spend wave: the rest of the Infinity (~570). The kill wave: ~40 Casaba killers among ~300 decoy and EW birds (the Galactica). The Pillar and the rest of the Galactica (~1,100) stay in reserve. The pack stays at Anchor as a fire base."),
    ("Donnager", "Gun frigate", "Sweeps the rocks round Anchor; then guards the pack there with the Wallfish (D11)."),
    ("Excelsior · Tantive IV", "PD frigate · corvette", "Guard the Nauvoo and the parked shields (D11); beat off Skerry's drone raid."),
    ("Canterbury", "ECW destroyer", "Brings the net up; lost in the Breakers ambush (T+3:52)."),
    ("Extenuating Circumstances", "ECW destroyer", "Holds what's left of the net; rides under the Astrid's umbrella, which kills the 64 missiles Breakwater sends after it."),
    ("Rocinante · Wallfish · Normandy", "Corvettes", "The drone screen. Normandy lost to a plasma-bomb drone (T+4:25). The Wallfish stays with the pack; the Rocinante goes on with the fleet."),
    ("Nauvoo", "Tender", "Holds the shield park 450,000 km out; the T-SEC transports wait there for the sky (A-13)."),
]
DEFENDERS = [
    ("Breakwater", "Warpless monitor", "Synchronous orbit over Site 1. Its guns never get a shot (the LREF stays outside their no-escape range); it fires its 64 missiles at the last ECW destroyer."),
    ("Site 1 (of 4)", "Ground laser, 2 GW", "The only site that sees Breakwater's sky. Dazzles and burns from the moment the fleet leaves Anchor's shadow; never struck (ROE)."),
    ("Skerry", "Moon complex", "Throws three rounds every ten minutes from T+0:04 until wave one kills it: five nets on the fleet's lane and one ring of canister clouds on Anchor. Its laser dazzles the fleet; its depot flushes 40 drones at the shield park."),
    ("The Breakers garrison", "Emplacements", "Cold pods, railgun platforms, mines, parked drones and a drone-control craft. Its last drones go for the pack at Anchor."),
    ("Inner ring", "12 emplacements", "Sensor pickets and sector defence along the orbit; too far apart to thicken Breakwater's wall."),
    ("Compact frigates", "3", "One waits in a cleft on a moonlet near Anchor; two hold behind Maren's limb."),
]

# ---------------------------------------------------------------- assets
# status: built / extend / new; concept: concept sheet first (user rule).
ASSETS = {
    "EN": ("L.R.E.F.S. Endeavor (rigged)", "extend", False, "Hero ship. Rebuild after the M-1C wake-style and PDC picks that are still pending in the modelling session (Q15), then link it into shot files with a library override on the rig empty. Its states (STATES) are presets the shot files load."),
    "EN-FIN": ("Endeavor: per-fin control and damage", "extend", False, "Per-fin deploy properties `fin_port`, `fin_starboard`, `fin_dorsal`, `fin_ventral` (the ship-wide `radiator_deploy` stays as a master). Port fin states via `fin_port_state`: intact, pre-fractured (shot {#Fin hit}), stump (every Endeavor shot after it)."),
    "EN-PD": ("Endeavor: defence, countermeasure and emergency controls", "extend", False, "`ciws_phase` (a keyed angle, with a spin-blur swap above ~600 rpm, because `ciws_rpm` changes jump and strobe), `ciws_fire` (muzzle empties), `cm_chaff`, `cm_flare`, `cm_smoke`, `ew_active`, `water_dump` (valve and emitter for FX-DUMP)."),
    "EN-MAST": ("Endeavor: sensor-mast shutters", "extend", False, "`mast_shutter`: armoured shutters close over the mast windows."),
    "EN-DMG": ("Endeavor: hull damage", "extend", False, "`dmg_belt`: spall and scorching on the port belt from shot {#Off the port bow} on; it must read in shot {#Heat}, which runs along the port flank."),
    "M1C": ("M-1C twin railcannon", "extend", False, "Fleet gun. Wake style still to be picked (split, ripple, bulk, extend, combined: Q15). Per-gun `charge_a/b`, `shot_a/b`, `fins_a/b`, `heat_a/b` for {#Rails wake} and {#Fire}, where only the gun that fired vents."),
    "MSL": ("Missile asset (26 m, plume, thrust)", "built", False, "Base for every variant; the hero LOD flies alongside the camera in {#Birds away}."),
    "MSL-V": ("Missile variants", "new", True, "Concept sheet first (five new weapon designs): the Casaba killer (hardened ablative nose, a seeker window behind a shutter, spin; seen in extreme close-up in {#Seeker}), the small multi-pack missile with MIRV bus, decoy, EW missile, Compact belt-pod missile. Three LODs each, dropped into the swarm system's slots."),
    "AST": ("L.R.E.F.S. Astrid (Hanuman heavy cruiser)", "new", False, "Hero, ~1,650 m. Build from lref_kit: M-1Cs, arrays, CIWS, fins, rings and shield are instances, so the new hero work is the hull, the AVPSA dish and the spinal. Concept sheet for the spinal muzzle and its FX look. Controls: `avpsa_az`, `avpsa_el`, `fins_deploy` (8), `spinal_charge`, `spinal_shot`, `engine_throttle`, `rcs_bow`/`rcs_stern`, `laser_power`/`laser_traverse`, plus the Endeavor's `ciws_phase` and `ciws_fire` on its instanced CIWS. Art exists."),
    "GI": ("Garibaldi-Ivanova frigate hull", "new", False, "Hero, ~420 m. One hull for all five frigates; module bay; warp rings; shield; spinning hab section. Art exists."),
    "GI-MAV": ("Hedgehog (MAV) module", "new", False, "~360 pods; `pod_ripple` launch control, driven from the swarm system's per-pod launch-time attribute so doors and launches can't drift apart. Art exists."),
    "GI-GUN": ("Gun module (4 large kinetic batteries)", "new", True, "Four scaled M-1C twins; the concept sheet only settles the layout. Seen only far off in {#The sweep}: a silhouette is enough if the user agrees (Q13)."),
    "GI-PD": ("PD module", "new", True, "Build after the PDC pick. Seen only far off in shot {#Shields to the park}: a silhouette is enough if the user agrees (Q13)."),
    "DD": ("ECW destroyer", "new", False, "Hero, ~200 m. The dish sits fixed, forward, behind the shield, as in the art (Q14); it is unmasked when the shield leaves. Controls: `booms_deploy`, `drone_bay`, `rcs`, `dmg_boom` (the Extenuating's scorched boom from {#Site One}). Model it in sections at its bulkhead frames for the section-break rig. Art exists."),
    "DD-BRK": ("Destroyer break-up (Canterbury)", "new", False, "Section-break rig: holed bow to stern, venting, the hull parting in two."),
    "CV": ("Corvette class", "new", True, "No reference art: concept sheet first. Brief: 50–150 m; two warp rings at the ends; a jettisonable forward shield; radiators and booms that stow for warp; no spin section; anti-drone weapons 'far more powerful and varied' than a big ship's PD. Model it in sections at its bulkhead frames."),
    "CV-BRK": ("Corvette destruction (Normandy)", "new", False, "Section-break rig variant."),
    "TND": ("Nauvoo, fleet tender", "new", True, "No reference art: concept sheet first. Brief: two warp rings, forward shield, stowable radiators; cradles for spare shields; a rig for swapping frigate modules. Seen only far off: a silhouette if the user agrees (Q13)."),
    "SHD": ("Parked impact shields", "extend", False, "Scaled instances of the gold shield for the park cluster."),
    "DRN-L": ("LREF drone", "new", True, "One design (picket/PD/EW variants by payload only), concept first."),
    "BW": ("Breakwater, Compact monitor", "new", True, "Concept sheet first. ~1,800 m warpless monitor: no rings or shield, ~2 m belt, 6 twin heavy turrets, 24 PD lasers, 40 CIWS, 64 cells, armoured louvred radiators. Controls: `turret_traverse`, `turret_elevation`, `cells_open`, `drive_glow`, `vent`, `ciws_phase`/`ciws_fire` with muzzle empties, PD `laser_power`. Model it in sections at its bulkhead frames."),
    "BW-BRK": ("Breakwater break-up", "new", False, "Section-break rig: spear wounds on the drive bells, the spinal entry amidships, secondaries, the back breaking."),
    "CF": ("Compact frigate", "new", True, "Concept sheet first. ~350 m; coilgun and missiles; simple instanced escape pods; modelled in sections for its break-up. Seen at ~420 px in shot {#Lance} (1,000 mm at 45 km), so it needs real detail."),
    "DRN-C": ("Compact drone and its hide", "new", True, "One design (plasma-bomb payload) plus the cold hide on a rock; concept first."),
    "EMP-POD": ("Cold missile pod on a rock", "new", True, "Concept first. Controls: `heave`, `petals`."),
    "EMP-RG": ("Breakers railgun platform", "new", True, "Concept first. Buried twin railgun. Controls: `unmask`, `shot`."),
    "RING": ("Inner-ring station", "new", True, "Only ever a point of light at ~21,800 km spacing: lights only, if the user agrees (Q13)."),
    "SKR": ("Skerry", "new", False, "One still plate of an airless moon; the battery, tracks and depot are flash and light positions only."),
    "WORLD": ("World presets and sun", "extend", False, "Used by every 3D shot. One preset per environment (ENVS), with planet-shine scaled to each (Maren is 1.6° across from the exit, ~17.5° from Breakwater's orbit); a Sun object that drives the World (today `TO_SUN` needs a rebuild); Skerry as a second body at the right angular size; a sun-direction gradient on the Breakers haze in comp; each set-up's camera kept near the world origin."),
    "MAREN": ("Maren: planet re-dress", "extend", False, "New continents and weather, night-side cities, the Site 1 plateau as a light cluster that goes out (shot {#Site One goes dark}), about 10 px at 2,000 mm."),
    "BRK": ("The Breakers environment", "new", False, "The dust haze as the Mist pass plus a sparse glitter layer; a generic rock kit; large rocks at realistic spacing."),
    "ANCHOR": ("Anchor: hero rock", "new", False, "~18 km rubble pile: a Geometry Nodes boulder scatter from the BRK kit, with hero surface tiles only where the camera goes close (shots {#The sweep}, {#The pack fires}); the moonlet with the frigate's cleft."),
    "PROXY": ("Blocking proxies", "new", False, "True-scale stand-ins for every ship and rock, built in step 1 for the timing animatic and the benchmarks."),
    "FX-WARP": ("Warp-exit flash", "new", False, "Bubble collapse bloom (comp plus a light)."),
    "FX-SWARM": ("Swarm system", "new", False, "One Geometry Nodes system for missiles, drones and canister pellets: per-instance launch time, three LODs (hero mesh only for the nearest ~10), each plume a single emissive mesh with emission sampling off, real lights only on the ~5 nearest plumes or flashes (faded in and out over ~6 frames so the hull lighting doesn't pop), pellets as emissive points whose brightness follows the lamp angle, rendered in its own view layer. Built first on the existing missile (MSL); the variants drop into its LOD slots later."),
    "FX-FAR": ("Distant drive plumes", "new", False, "Cheap far plumes for long-lens fleet shots."),
    "FX-NUKE": ("Nuclear flashes", "new", False, "Point flashes: Skerry's surface, the mine at Anchor."),
    "FX-PD": ("Point-defence fire", "new", False, "CIWS tracers and kill clouds, chaff, flares, intercept flashes, laser lens pulses, in their own view layer at low samples."),
    "FX-SMOKE": ("Smoke screen", "new", False, "A cached VDB in two resolutions (medium shot in {#Countermeasures} and {#Turnover}, fleet scale in {#Site One}), rendered in a half-resolution layer."),
    "FX-SLUG": ("Slug streaks and impacts", "new", False, "Glints, impact flash, spall cone, shock ring."),
    "FX-BREAK": ("Section-break rig and debris kit", "new", False, "No cell fracture (the plated kit hulls defeat it): each breakable hull is modelled in 3–8 sections at its bulkhead frames, the torn edges capped with kit parts, the pieces driven apart with a procedural `break` 0→1, and an instanced debris kit scattered."),
    "FX-VENT": ("Venting in vacuum", "new", False, "Short-lived sprays of glinting ice (what gas and coolant do in vacuum); one small cached VDB reused."),
    "FX-DUMP": ("Water-dump plume", "new", False, "A Geometry Nodes ice point cloud with a thin low-resolution VDB core, in its own layer at half resolution with one volume bounce. Costed at ~250 s/frame and part of the volume benchmark."),
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
    "AST": ("The Astrid looks", "MS 50 mm along the dorsal hull (the muzzle: {#Spinal})", "fills the frame"),
    "GI": ("Wave one", "hull camera on the Infinity", "fills the frame"),
    "GI-MAV": ("Wave one", "hull camera beside the pods", "fills the frame"),
    "MSL": ("Birds away", "CU 85 mm alongside one missile", "fills the frame"),
    "MSL-V": ("Seeker", "ECU 100 mm on a Casaba killer's nose", "fills the frame"),
    "M1C": ("Fire", "ECU 85 mm on the muzzles", "fills the frame"),
    "DD": ("Net up", "MS 40 mm at ~600 m", "fills the frame"),
    "CV": ("Normandy", "800 mm at ~20 km", "~200 px"),
    "TND": ("Shields to the park", "behind the parked shields", "~40 px"),
    "GI-PD": ("Shields to the park", "behind the parked shields", "~40 px"),
    "GI-GUN": ("The sweep", "far off, shelling rocks", "a few px"),
    "BW": ("The hail", "drone camera near the monitor", "fills the frame"),
    "CF": ("Lance", "1,000 mm at 45 km", "~420 px"),
    "RING": ("The anvil", "far along the orbit", "points of light"),
    "SKR": ("Skerry burns", "1,200 mm at ~262,000 km", "a quarter-frame disc"),
    "EMP-RG": ("The platform", "drone over the platform", "fills the frame"),
    "EMP-POD": ("The belt wakes", "drone near the rock", "~300 px"),
    "DRN-C": ("Screens out", "28 mm, nearest drones ~1 km off", "~30 px"),
    "DRN-L": ("Net up", "MS 40 mm", "~40 px"),
    "ANCHOR": ("The sweep", "low over the surface", "fills the frame"),
}

RENDER_CLASSES = {
    "A": ("Endeavor close-up", "~45 s/frame"),
    "A2": ("Endeavor close-up with heavy FX", "~90 s/frame"),
    "V": ("Close-up with a hero volume (the water dump)", "~250 s/frame"),
    "B": ("One hero ship or rock, full view", "~75 s/frame"),
    "C": ("Several ships or heavy FX (FX in own layers)", "~200 s/frame"),
    "P": ("Planet plate rendered once, plus one ship layer", "~30 s/frame"),
    "D": ("Wide, distant, small subject on black, or plate", "~15 s/frame"),
    "E": ("2D comp / HUD", "~2 s/frame"),
}
RENDER_NOTE = ("These costs are estimates, not measurements. Step 1 benchmarks the methods with stand-ins, so nothing waits on new assets: "
               "class C (two or three linked Endeavors, 600 instances of the existing missile through the swarm system and an FX-PD layer at 16–32 spp; "
               "record s/frame and VRAM), the volumes (the fleet-scale smoke of {#Site One} and the water dump of {#Heat}), the dark lee "
               "(the Endeavor lit only by its fins, and one M-1C shot, as in {#Too hot} and {#Fire}), plus shots {#Rings cool} and {#Broadside}. "
               "Gate before the full pass: if C comes in above ~230 s/frame or B above ~100 s/frame, apply the levers agreed in advance "
               "(half-resolution volume and FX layers; swarm layers at 16 spp with earlier LOD switches; a second trimmed from each of "
               "{#Wave one}, {#The pack fires} and {#Wall of fire}).")

# Asset set-ups: each shot belongs to exactly one (the builder checks). Render
# batches follow the World preset (ENVS) within each set-up.
SETS = [
    ("the Endeavor", ["Black, then a star", "Rings cool", "Shields to the park", "Fins edge-on", "Blind", "Spin-up",
                      "Lenses", "Countermeasures", "Turnover", "Too hot", "Fins in", "Fin hit", "Lance channels",
                      "Broadside", "Rails wake", "Fire", "Blind it", "Heat", "Hold"]),
    ("the Astrid", ["The Astrid looks", "Answer", "Umbrella", "Spinal"]),
    ("the destroyers", ["Net up", "Canterbury", "Holed", "The net", "Site One"]),
    ("the Breakers", ["The Breakers", "The belt wakes", "The platform", "Payback", "Screens out", "Normandy"]),
    ("the pack and Anchor", ["Wave one", "The sweep", "The flash", "Off the port bow", "Lance", "The platform dies",
                             "The pack fires", "Kill wave away"]),
    ("missile close-ups", ["Birds away", "Seeker"]),
    ("Breakwater over Maren", ["The anvil", "The spend wave", "Wall of fire", "Casaba", "The hail", "The wait",
                               "Impact", "Terms", "Site One goes dark"]),
    ("long-lens plates", ["The task group", "Turn and burn", "Skerry burns"]),
    ("2D", ["Skerry throws", "The picture", "Return to sender", "Anchor", "The fire plan", "Anchor ringed"]),
]

PRODUCTION_PLAN = [
    ("Order", "1) Step 1: the user's pending picks (Q15); the Endeavor rebuild and its new rig items; the World presets; blocking proxies (PROXY) and a timing animatic; the method benchmarks and the gate (see the render note); the swarm system, built on the existing missile with LOD slots for the variants. "
              "2) One batched concept round, missile variants first, since it waits on the user. "
              "3) Meanwhile the assets with art: the FX library, the Breakers then Anchor, the frigate with its hedgehog module, the destroyer, the Astrid. "
              "4) The concept-gated assets: the missile variants into the swarm's slots, the corvette and drones, the emplacements, Breakwater, the gun module. Every breakable hull (DD, CV, CF, BW) is modelled in sections at its bulkhead frames. "
              "5) The long-lens plates last; {#Umbrella} renders last of all, since it waits on three gates (the Astrid, the missile variants, the PDC pick)."),
    ("Methods", "The foreground pods of {#Kill wave away} in their own layer, defocused in comp. Every rock and plume instanced, with a rock tile in the class C benchmark ({#The sweep}, {#The pack fires}). "
                "In the dark lee, area lights on each fin driven by `heat`, with emission sampling off on the fin meshes. {#Hold} is a planet plate rendered once plus a ship layer."),
    ("Rendering", "One job per shot to multilayer EXR sequences (DWAA), Placeholders on and Overwrite off so a crashed render resumes; the grade (`LREF_Compositor`) as a separate pass; emissive FX in their own view layers at 16–32 spp with 1–3 proxy lights in the beauty layer; Persistent Data; adaptive sampling with denoising; vector blur in comp; plan ~150 GB of disk."),
]

ACTS = [
    ("I", "Arrival", "The fleet arrives slow, parks its shields, reads the system, and strikes Skerry first because Skerry's laser can burn its fins."),
    ("II", "The Breakers", "Hours of coasting, then the debris ring: the ambush, the Canterbury, the Astrid's answer, the drones and the Normandy."),
    ("III", "Anchor", "Turnover into the lee of a rock over Site 1: the sweep, the heat, the fin hit, the frigate, the lance and the broadside."),
    ("IV", "Hammer and anvil", "Across to Breakwater: Skerry's nets, the try at the pack, Site 1's fire, Breakwater's missiles at the last net ship, the spend wave, the kill wave, the Casaba jets, the hail and the spinal shot, then terms."),
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
# Full reports and the syntheses are in review/.
REVIEW_STATUS = "Round 3 reads revision 3 with the same five lenses; the rounds continue until no reviewer has a major issue left."
REVIEWS = [
    ("Round 1", "Revision 1", [
        ("Physics", "The Astrid could not stop after its spinal shot.", "It stops short of Breakwater and fires from rest."),
        ("Physics", "'The line' down Site 1's zenith turns at 15°/h, so nothing can coast down it.", "No line to hold: the waves fly straight from Anchor to where Breakwater will be. Map D is now in the inertial frame (a ~113,000 km approach, turnover T+7:16)."),
        ("Physics", "Straight down Site 1's line, Maren is the backstop.", "The waves arrive ~48° off Breakwater's zenith and the spinal shot 15° off it: misses and wreckage clear Maren."),
        ("Physics", "The heat readouts don't add up.", "Three fins vent again at Anchor (31 %), 98 % and a water dump at T+8:00, the fins out at T+8:24."),
        ("Physics", "Two hours in Site 1's sky with no effect.", "Site 1 scorches the Extenuating's boom; the fleet rolls, lays smoke and dazzles back."),
        ("Physics", "Skerry's rounds are too slow for the clock.", "The mass driver was raised to 12.5 km/s (and to 15.5 km/s in round 2)."),
        ("Doctrine", "The spend wave lands an hour before the kill wave.", "90 s apart (T+7:52:00, T+7:53:30); the spend wave's arrival has its own shot."),
        ("Doctrine", "The Astrid ends up leading the fleet into the anvil.", "It brakes with the line and stops behind the escorts."),
        ("Doctrine", "An unswept, predictable anchorage.", "The fleet sweeps Anchor and trips a mine; the Donnager shells the nearby rocks; the platform (400 km) and the frigate (45 km) strike in the same minute."),
        ("Doctrine", "Nobody hunts the last ECW destroyer.", "Breakwater fires all 64 cells at the Extenuating; the Astrid's umbrella kills them (new shot {#Umbrella})."),
        ("Doctrine", "Site 1 falls silent during the final approach.", "It burns and dazzles; the fleet answers with rolls, smoke and its own dazzle."),
        ("Doctrine", "The hedgehogs' magazines don't add up.", "The Infinity empties into the spend wave, the Galactica fires the kill wave, ~1,100 stay in reserve, and the pack stays at Anchor."),
        ("Lore", "The lance was a free-flying ring.", "A field-held jet from the nose to the target; ~50 km is the field's reach (A-23 reworded)."),
        ("Lore", "The Astrid is not kilometre-long.", "'Its 1.6-kilometre hull': the kilometre is the gun."),
        ("Cinematography", "Subtitles bury the picture.", "Lines cut to ≤ 12 characters a second with short tags; the builder checks every shot."),
        ("Cinematography", "One tempo throughout.", "Re-timed with holds: the coast on the clock, the hiss after each loss, the wait on the crippled monitor."),
        ("Cinematography", "Real lenses can't see the far end of the exchanges.", "Long-lens tracker cameras (300–2,000 mm) and matched framings for each payback."),
        ("Cinematography", "No clock or HUD plan.", "A persistent clock that runs at the shot's rate, one master plot with Maren screen right, a SINK readout that builds to the dump."),
        ("Cinematography", "The losses and the antagonist aren't set up.", "The Canterbury speaks first, the Normandy calls the drones, Breakwater gets a reveal, and the last plot names both lost ships."),
        ("Cinematography", "Time compression turns big hulls into models.", "Rotations at ≤ 4× with the middle cut out; every internal cut is now its own shot."),
        ("Production", "The render budget is unmeasured.", "Reclassified costs, computed per class, with named benchmark shots."),
        ("Production", "Detail isn't tied to what the camera sees.", "A closest-view table; proxies proposed for the ring stations, tender and PD module (Q13)."),
        ("Production", "The Endeavor and M-1C aren't built for this board.", "Marked 'extend: rebuild after the pending picks' (Q15) and first in the build order."),
        ("Production", "Rig controls are missing.", "Per-fin control, CIWS phase and fire, countermeasures, water dump and belt damage, plus controls for every new asset."),
        ("Production", "Break-ups and volumes would eat the schedule.", "A section-break rig instead of cell fracture, ice-glint venting, cached smoke, the Mist pass for haze."),
        ("Production", "Swarms with hundreds of plumes.", "One Geometry Nodes swarm system with LODs, emissive plumes and few lights."),
    ]),
    ("Round 2", "Revision 2", [
        ("Physics", "With the mirrored geometry, Skerry's 12.5 km/s rounds can't reach the nets on time.", "The mass driver throws at up to 15.5 km/s: five nets on the lane at T+6:40–7:30; the sixth salvo, at 12.5 km/s, rings Anchor instead."),
        ("Physics", "The multi-pack missiles can't fly the 25-minute waves.", "They leave Anchor twenty minutes ahead of the killers (T+7:07 and T+7:08:30) on a 45-minute profile, so each wave still lands within a second."),
        ("Doctrine", "The pack is left unguarded at Anchor, and the defender never tries for it.", "The Donnager and the Wallfish guard it (D11 now covers fire bases); Skerry's clouds ring Anchor and drones wake behind them, and the guard beats them off (new shot {#Anchor ringed})."),
        ("Cinematography", "HUD text isn't counted, so the fire plan and the callback can't be read.", "The reading check now counts HUD labels; the fire plan carries two labels over 8 s, the lost ships' callback holds on its own, the Anchor insert runs 5 s."),
        ("Cinematography", "The spinal shots fire on their last frame, and Site 1's lights are 1–2 px.", "Both fire two seconds in, so the bloom stays on screen; a 2,000 mm tracker shows Site 1 going dark (new shot {#Site One goes dark})."),
        ("Production", "The week rests on unmeasured class B and C costs.", "Step 1 benchmarks the methods with stand-ins, and a go/no-go gate applies fallbacks agreed in advance."),
        ("Production", "Classes don't follow the pixels.", "Small subjects on black move down, the smoke and water-dump shots move up, the dump gets its own asset (FX-DUMP), and the last shot becomes a plate plus a ship layer."),
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
shot(act="I", title="The task group", dur=5, clock="T+0:00:10", real="compressed 7× (13 exits over ~36 s)", body="drone",
     cam="EWS · 85 mm · locked off, far out on the group's flank",
     action="Staggered warp flashes, seconds and 50+ km apart: the Astrid, the hedgehog pack, the Donnager, the Excelsior, both destroyers, four corvettes, the Nauvoo. Screen right, Maren is a thin crescent with the sun behind it, ringed by the faint backlit glow of the Breakers.",
     comm=[("ACTUAL · ASTRID", "All fourteen. All home.")], rules=["O1", "D2"], vfx="13 warp flashes, backlit ring glow",
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
shot(act="I", title="Net up", dur=3, clock="T+0:02:40", real="compressed 10× (the booms run out over ~30 s)", body="drone",
     cam="MS · 40 mm · off the Canterbury's bow",
     action="With its shield gone, the Canterbury's forward dish is clear on its truss. Its sensor booms run out and its drones scatter ahead. From here the fleet talks only by laser.",
     comm=[("CANTERBURY", "Net's up. Going quiet.")], rules=["O2", "D10"], vfx="Drone launch",
     rig=["booms_deploy (new)", "drone_bay (new)"], assets=["DD", "DRN-L"],
     sound="Silence.", cost="B", map="A", render=None,
     sketch="panel([ship('destroyer',110,50,3.2,0,true), sparks(190,40,14,40,5)], 5)")
shot(act="I", title="The Astrid looks", dur=3, clock="T+0:03:20", real="compressed 10× (the slew takes ~30 s)", body="drone",
     cam="MS · 50 mm · along the Astrid's dorsal hull",
     action="The Astrid's 100 m AVPSA dish slews toward Maren. Its eight stacked fins stay stowed: Skerry's laser can see them.",
     comm=[], rules=["O2", "D3"], vfx="", rig=["avpsa_az / avpsa_el (new)"], assets=["AST"],
     sound="Silence.", cost="B", map="A", render=None,
     sketch="panel([ship('astrid',110,56,1.3,-3,true), '<ellipse cx=\"100\" cy=\"38\" rx=\"9\" ry=\"4\" fill=\"none\" stroke=\"#cfd6dc\" stroke-width=\"0.8\"/>'], 21)")
shot(act="I", title="Skerry throws", dur=6, clock="T+0:04:10", real="1:1", body="hud",
     cam="HUD insert · the Astrid's telescope feed, 2,000 mm equivalent",
     action="A thread of light runs along Skerry's dark limb: the mass driver throwing. Three rounds leave; the plot tags their arrival. Then a glare blooms across the feed: Skerry's laser has found the dish.",
     comm=[("ASTRID", "Skerry's throwing down our lane."), ("ACTUAL", "They'll be hours.")], hud=["ARRIVE T+6:40"],
     rules=["HO3", "HO5", "O2"], vfx="HUD, telescope grain, dazzle glare", rig=[], assets=["HUD", "SKR", "FX-DAZZLE"],
     sound="Soft sensor tones.", cost="E", map="A", render=None,
     sketch="panel([moon(120,50,26), '<path d=\"M104,38 Q118,30 134,34\" fill=\"none\" stroke=\"#ffe3b0\" stroke-width=\"0.9\"/>', glow(150,30,30,'#f2e8ff',0.35), hud(70,12,100,76), label(74,86,'ARRIVE T+6:40','#33b3a2')], 5)")
shot(act="I", title="The picture", dur=7, clock="T+0:09:00", real="compressed ~43× (the picture builds over ~5 min)", body="hud",
     cam="HUD insert · the master plot",
     action="The master plot, Maren screen right: Breakwater parked over Site 1; Skerry, with its laser and mass driver; the Breakers; the approach line. The fins stay in while Skerry's laser can see them.",
     comm=[("ACTUAL", "Picture's up. Breakwater's right where the brief said.")], hud=["BREAKWATER", "SKERRY", "THE BREAKERS"],
     rules=["O2", "D3"], vfx="HUD", rig=[], assets=["HUD"], sound="Sensor tones.", cost="E", map="A", render=None,
     sketch="panel([hud(16,10,208,80), planet(200,50,9,'right'), label(166,36,'BREAKWATER','#e2603f'), label(120,22,'SKERRY','#e2603f'), '<ellipse cx=\"200\" cy=\"50\" rx=\"44\" ry=\"20\" fill=\"none\" stroke=\"#9fb0bc\" stroke-width=\"0.5\" stroke-dasharray=\"1 2\"/>', label(120,82,'THE BREAKERS','#9fb0bc'), '<line x1=\"24\" y1=\"50\" x2=\"150\" y2=\"50\" stroke=\"#33b3a2\" stroke-width=\"0.6\"/>'], 8)")
shot(act="I", title="Wave one", dur=5, clock="T+0:18:00", real="1:1", body="hull",
     cam="WS · 24 mm · on the Infinity's hull, shaking with each launch",
     action="The Infinity ripple-fires 150 capital-ship killers at Skerry's laser, mass driver and depot in fifteen seconds. Pod doors open in waves down the hull and the plumes curve away screen right. Skerry goes first because its laser can burn the fleet's fins all the way in.",
     comm=[("ACTUAL", "Infinity, wave one. Skerry."), ("INFINITY", "Wave one away.")],
     rules=["O3", "O9", "D3"], vfx="150 missiles (swarm system), pod doors", rig=["pod_ripple (new)"],
     assets=["GI", "GI-MAV", "MSL-V", "FX-SWARM"], sound="Launch cracks through the hull; the camera shakes with each.",
     cost="C", map="A", render=None,
     sketch="panel([ship('hedgehog',70,60,1.4,-6,true), trail('M96,50 Q150,30 230,18','#ffd9a0','0.6 0.9',0.8), trail('M96,54 Q150,36 230,26','#ffd9a0','0.6 0.9',0.6), sparks(170,30,26,40,4)], 7)")
shot(act="I", title="Birds away", dur=3, clock="T+0:19:00", real="1:1", body="drone",
     cam="CU · 85 mm · a drone camera pacing one missile (cinematic licence: it keeps up with a 30 g boost)",
     action="Alongside one of the 150, a minute into its boost: the 26 m body in a slow spin, its plume a white-hot needle, the Infinity already a spark far behind. Ahead, screen right, Maren's thin crescent.",
     comm=[], rules=["O3", "O9"], vfx="Hero missile and plume, far launch sparks", rig=["thrust 1 (MSL)", "spin"],
     assets=["MSL", "MSL-V", "MAREN"], sound="Silence; the score lifts.", cost="B", map="A", render=None,
     sketch="panel([planet(236,50,22,'right'), glow(24,58,3,'#ffffff',0.8), plume(81,50,60,180,2.6), ship('missile',120,50,2.6,0,true)], 10)")
shot(act="I", title="Turn and burn", dur=6, clock="T+0:25:00", real="compressed 8× (the turn takes ~49 s)", body="tracker",
     cam="EWS · 400 mm · the whole group",
     action="Through a long lens, eleven drives light one after another as the group turns onto the approach line, bows toward Maren and plumes streaming screen left; the three ships at the park stay dark behind them. One g for 34 minutes.",
     comm=[("ACTUAL", "All ships, execute. One g.")], rules=["O1", "D2"], vfx="Distant drive plumes",
     rig=[], assets=["AST", "EN", "GI", "DD", "CV", "FX-FAR"], sound="Sub-bass swell.", cost="D", map="A", render=None,
     sketch="panel([plume(60,40,-40,0,1.4), ship('corvette',64,40,1,0,true), plume(96,58,-46,0,1.8), ship('frigate',104,58,0.5,0,true), plume(130,44,-60,0,2.2), ship('endeavorNoShield',150,44,0.35,0,true), plume(170,66,-50,0,2), ship('astrid',196,66,0.3,0,true)], 13)")

# ============================================================ ACT II
shot(act="II", title="Skerry burns", dur=4, clock="T+1:02:00", real="compressed 5× (~20 s of hits); the digits roll 36 min into it", body="tracker",
     cam="EWS · 1,200 mm · Skerry a quarter-frame disc",
     action="Pinpricks of white on Skerry's limb: wave one arriving, nose-on to the battery. The light left Skerry 0.9 s ago. Just before the hits, a faint spray of points leaves the depot: its drones, flushed toward the shield park. Its eighteen rounds are already on their way.",
     comm=[("ASTRID", "Splash on Skerry. Their laser's gone.")], rules=["O3", "O9", "HO8"],
     vfx="Distant nuclear flashes, flushed drones", rig=[], assets=["SKR", "FX-NUKE"],
     sound="Nothing; a swell of score.", cost="D", map="A", render=None,
     sketch="panel([moon(120,50,22), glow(106,40,6,'#ffffff',0.95), glow(112,34,4,'#ffffff',0.9), glow(100,48,3,'#ffffff',0.8), sparks(86,30,12,16,9)], 9)")
shot(act="II", title="Fins edge-on", dur=6, clock="T+1:10:00", end="T+3:20:00", real="compressed; the digits roll through a 2 h 10 min coast", body="drone",
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
shot(act="II", title="Lenses", dur=3, clock="T+3:45:01", real="1:1", body="hull",
     cam="ECU · 135 mm · a laser focusing array on its yoke",
     action="The array's lens assembly slews onto an incoming pod missile, steadies, and flashes violet in rapid pulses, each one a shot; the beams themselves are invisible in vacuum. Far off, a spark as the missile dies, and the yoke is already swinging to the next.",
     comm=[], rules=["D1", "O5"], vfx="Lens glow pulses, a distant intercept flash",
     rig=["laser_power pulses", "laser_traverse", "laser_elevation"], assets=["EN", "FX-PD"],
     sound="Capacitor whine and the yoke's servo through the hull, one tick per pulse.", cost="A", map="B",
     render=None,
     sketch="panel(['<circle cx=\"120\" cy=\"50\" r=\"30\" fill=\"#2a3037\"/>', '<rect x=\"60\" y=\"44\" width=\"30\" height=\"12\" fill=\"#3a4048\"/>', glow(120,50,26,'#b476ff',0.75), '<circle cx=\"120\" cy=\"50\" r=\"15\" fill=\"#140c24\" stroke=\"#b476ff\" stroke-width=\"1.2\"/>', glow(214,22,3,'#ffffff',0.9), sparks(214,22,10,10,18)], 18)")
shot(act="II", title="Countermeasures", dur=4, clock="T+3:45:04", real="1:1", body="drone",
     cam="MS · 35 mm · along the port flank",
     action="Chaff and flares bloom and a smoke screen unfurls, thinning as it spreads. The CIWS lay kill clouds in the missiles' paths; the laser lenses glow violet, beams invisible. Missiles pop one by one.",
     comm=[], rules=["D1"],
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
     cam="Tracker · 1,500 mm · from the Extenuating Circumstances",
     action="The Canterbury, fifty kilometres off, jinks hard on RCS, its dish forward.",
     comm=[("EXTENUATING", "Canterbury, jink!")], rules=["D4"], vfx="RCS puffs", rig=["rcs (new)"], assets=["DD"],
     sound="Silence.", cost="D", map="B", render=None,
     sketch="panel([ship('destroyer',120,50,3.4,4,true), smoke(80,46,6)], 31)")
shot(act="II", title="Holed", dur=5, clock="T+3:52:13", real="1:1", body="tracker",
     cam="Tracker · 1,500 mm · holding on the Canterbury",
     action="The slugs arrive from ahead. The Canterbury is holed bow to stern in three white flashes; it vents glittering ice, the hull parts in two and tumbles. Hold on it as its channel dies to hiss.",
     comm=[("EXTENUATING", "Canterbury's gone.")],
     rules=["HO9"], vfx="Impact flashes, venting, section break", rig=["break 0→1 (new)"],
     assets=["DD", "DD-BRK", "FX-BREAK", "FX-VENT"], sound="The dying channel's hiss, then silence.",
     cost="B", map="B", render=None,
     sketch="panel([ship('destroyer',110,50,3.2,10,true), glow(150,46,10,'#ffffff',0.85), glow(120,50,7,'#ffffff',0.7), sparks(140,50,30,30,11), smoke(100,56,14)], 33)")
shot(act="II", title="Answer", dur=4, clock="T+3:52:38", real="1:1 (the last degrees of the slew; it fires two seconds in)", body="drone",
     cam="EWS · 135 mm · the Astrid in profile, bow screen right",
     action="The Astrid's 1.6-kilometre hull swings its last few degrees onto the platform, steadies on RCS, and two seconds in fires down the spinal: a blue-white bloom at the bow that holds to the cut.",
     comm=[("ACTUAL", "Astrid, spinal on the platform."), ("ASTRID", "Firing.")], rules=["O4"],
     vfx="Spinal muzzle bloom", rig=["rcs_bow / rcs_stern (new)", "spinal_charge / spinal_shot (new)"], assets=["AST", "FX-SPINAL"],
     sound="A sub-bass punch.", cost="B", map="B", render=None,
     sketch="panel([ship('astrid',110,52,1.1,0,true), glow(176,52,14,'#bfe1ff',0.9), plume(180,52,30,0,3)], 37)")
shot(act="II", title="Payback", dur=3, clock="T+3:54:28", real="the clock jumps 108 s from the shot", body="drone",
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
shot(act="II", title="Return to sender", dur=5, clock="T+4:14:00", real="1:1", body="hud",
     cam="HUD insert · the Extenuating Circumstances' plot",
     action="A block of drone tracks flips from red to teal: the drones still on a control link are hijacked and turned on their own swarm. The control craft behind the rocks is found and dazzled; the Canterbury's drifting drones are picked up. The autonomous drones keep coming.",
     comm=[("EXTENUATING", "Return to sender.")], hud=["LINKED → OURS", "AUTONOMOUS", "NET DEGRADED"],
     rules=["O5", "HD9", "D10"], vfx="HUD, EW overlay",
     rig=[], assets=["HUD", "FX-EW"], sound="Clipped data chatter.", cost="E", map="B", render=None,
     sketch="panel([hud(30,10,180,80), sparks(90,50,24,40,43), '<g opacity=\"0.9\">' + sparks(150,44,24,40,44).replace(/#ffe7b0/g,'#33b3a2') + '</g>', label(34,18,'LINKED → OURS','#33b3a2'), label(34,86,'AUTONOMOUS','#e2603f'), label(140,18,'NET DEGRADED','#e2603f'), glitch(45)], 45)")
shot(act="II", title="Normandy", dur=5, clock="T+4:25:00", real="1:1", body="tracker",
     cam="Tracker · 800 mm · from the Wallfish",
     action="One autonomous drone slips the screen and dives on the Normandy. A plasma bomb goes off against its flank and the corvette breaks up. Hold two seconds on the wreck as its channel dies to hiss.",
     comm=[("WALLFISH", "One's through—on Normandy!")], rules=["HO4"], vfx="Plasma-bomb flash, break-up",
     rig=["break 0→1 (new)"], assets=["CV", "CV-BRK", "DRN-C", "FX-SWARM", "FX-BREAK"],
     sound="The dying channel's hiss, then silence.", cost="B", map="B", render=None,
     sketch="panel([ship('corvette',120,50,5,-4,true), glow(128,48,16,'#e3c7ff',0.9), sparks(128,48,40,40,47)], 47)")

# ============================================================ ACT III
shot(act="III", title="Turnover", dur=6, clock="T+4:34:10", end="T+4:34:59", real="rotation at ~4×, the middle of the 49 s flip cut out", body="hull",
     cam="WS · 24 mm · on the dorsal hull looking aft",
     action="Under smoke and an EW peak, one ship at a time, the fleet flips. The stars wheel over the hull as the stern swings toward Maren; now the bow points screen left while the ship still travels right. The drive lights: 34 minutes of braking toward Anchor.",
     comm=[("ACTUAL", "Turnover, one at a time.")], rules=["D8", "O8"],
     vfx="Main plume, RCS, smoke screen", rig=["rcs_bow / rcs_stern pulses", "engine_throttle 0→1", "cm_smoke (new)"],
     assets=["EN", "EN-PD", "FX-SMOKE"], sound="RCS thumps, then the drive's roar through the hull.", cost="A2", map="B", render=None,
     sketch="panel([smoke(60,40,40), '<rect x=\"0\" y=\"80\" width=\"240\" height=\"20\" fill=\"#3a4048\"/>', '<path d=\"M20,20 Q120,-10 220,20\" fill=\"none\" stroke=\"#cfd8e0\" stroke-width=\"0.4\" opacity=\"0.5\"/>', plume(200,78,60,-8,6)], 49)")
shot(act="III", title="Anchor", dur=5, clock="T+5:08:00", real="1:1; the digits roll 33 min into it", body="hud",
     cam="HUD insert · the master plot, zoomed",
     action="Anchor, an 18 km rock, with its shadow pointing away from Site 1. The fleet will string out along it; two nearby rocks are tagged '?'.",
     comm=[("ACTUAL", "Into Anchor's lee.")], hud=["ANCHOR", "SITE 1", "?", "?", "SINK 94%"],
     rules=["D5", "D2"], vfx="HUD", rig=[], assets=["HUD"],
     sound="Sensor tones.", cost="E", map="C", render=None,
     sketch="panel([hud(16,10,208,80), rocks(2,1,140,152,44,56,6,6.5), '<path d=\"M140,46 L30,40 L30,60 L140,54Z\" fill=\"#33b3a2\" opacity=\"0.15\"/>', label(154,40,'ANCHOR','#33b3a2'), label(200,30,'?','#e2603f'), label(110,80,'?','#e2603f'), label(20,86,'SINK 94%','#33b3a2'), '<line x1=\"160\" y1=\"50\" x2=\"220\" y2=\"50\" stroke=\"#e2603f\" stroke-width=\"0.5\" stroke-dasharray=\"2 2\"/>', label(186,46,'SITE 1','#e2603f')], 52)")
shot(act="III", title="The sweep", dur=4, clock="T+5:09:00", real="compressed ~20× (minutes)", body="drone",
     cam="WS · 24 mm · low over Anchor's surface",
     action="The Endeavor settles into darkness in the lee, a few kilometres off the surface, where the rock blocks the sun as well as Site 1. Corvettes and drones sweep the rock: a drone trips a mine on the far side, and the flash lights Anchor's limb from behind. Far off, the Donnager's shells land on the nearest rocks.",
     comm=[("DONNAGER", "Rocks inside three hundred done. Moonlets next.")], rules=["O8", "D6", "O4"],
     vfx="Mine flash behind the limb, distant impacts", rig=["rcs_bow / rcs_stern pulses"],
     assets=["EN", "ANCHOR", "BRK", "CV", "DRN-L", "GI", "GI-GUN", "FX-NUKE"], sound="Silence.",
     cost="C", map="C", render=None,
     sketch="panel([rocks(12,1,-40,120,40,160,90,92), glow(40,20,30,'#ffffff',0.5), ship('endeavorNoShield',176,34,0.8,0)], 53)")
shot(act="III", title="Too hot", dur=4, clock="T+5:12:00", real="compressed 5× (the fins take ~20 s)", body="hull",
     cam="MS · 35 mm · on the stern shoulder",
     action="Heat alarms. The sweep isn't finished, but the sink can't wait: the slot doors slide open and all four fins telescope out, glowing orange against black, the only light in the lee.",
     comm=[("DONNAGER", "Sweep's not done."), ("ENDEAVOR", "Can't wait. Fins out.")], hud=["SINK 94%"],
     rules=["D3", "D5"], vfx="Fin glow, light spill",
     rig=["fin_* 0→1 (new)", "heat 1.9→2.4", "radiator_glow"], assets=["EN", "EN-FIN"],
     sound="Alarm tones; the fins' hydraulic groan.", cost="A", map="C",
     render="img/lookaft_s1combat.jpg", sketch=None)
shot(act="III", title="The flash", dur=1, clock="T+5:13:00", real="1:1", body="tracker",
     cam="Tracker · 1,200 mm · on a rock 400 km off the port quarter",
     action="A muzzle flash on a rock: the platform, unmasked for half a second.",
     comm=[], rules=["HO7", "HO1"], vfx="Muzzle flash", rig=["unmask / shot (new)"],
     assets=["EMP-RG", "BRK", "FX-SLUG"], sound="Silence.", cost="D", map="C", render=None,
     sketch="panel([rocks(19,1,90,150,30,70,28,30), glow(122,44,7,'#bfe1ff',0.95)], 32)")
shot(act="III", title="Fins in", dur=3, clock="T+5:13:01", real="compressed 5× (the fins crawl in against a 16 s flight)", body="hull",
     cam="MS · 35 mm · the same shoulder, the clock large",
     action="The fins start in, crawling against the clock.",
     comm=[("ENDEAVOR", "Launch, four hundred! Fins in!")], rules=["HO7", "HO1", "D3"],
     vfx="", rig=["fin_* 1→0.5 (new)"], assets=["EN", "EN-FIN"],
     sound="The call; alarms; the fins' groan.", cost="A", map="C", render=None,
     sketch="panel([ship('endeavorNoShield',110,50,1.9,0), label(8,92,'T+5:13:09','#6fd3c4')], 55)")
shot(act="III", title="Fin hit", dur=3, clock="T+5:13:16", real="1:1", body="hull",
     cam="CU · 50 mm · on the port fin",
     action="Halfway in, the port fin takes a slug from screen right. It shatters into glowing shards and its coolant flashes to glittering ice.",
     comm=[("ENDEAVOR", "Port fin's gone. Cut it loose.")], rules=["HO7", "D7"], vfx="Fin shatter, coolant venting",
     rig=["fin_port_state → pre-fractured (new)"], assets=["EN", "EN-FIN", "FX-FIN", "FX-VENT", "FX-SLUG"],
     sound="Metal shear through the hull; a hiss.", cost="A2", map="C", render=None,
     sketch="panel([ship('endeavorNoShield',110,50,1.9,0), glow(176,24,12,'#ff8a3c',0.8), sparks(178,22,40,36,55), smoke(184,20,16), streak(236,4,180,22,'#8fb1ff')], 57)")
shot(act="III", title="Off the port bow", dur=4, clock="T+5:13:30", real="1:1", body="hull",
     cam="Hull camera · 600 mm · on the Endeavor's port side",
     action="A Compact frigate slides out of a pre-dug cleft on the far side of a moonlet, 45 km off the port bow, and fires its coilgun. Two seconds later the camera shakes as the slug spalls the port belt.",
     comm=[("DONNAGER", "Frigate, off your port bow!")], rules=["HO6", "O6"], vfx="Coilgun flash, hull spall",
     rig=["dmg_belt 0→1 (new)"], assets=["CF", "ANCHOR", "EN", "EN-FIN", "EN-DMG", "FX-SLUG"],
     sound="The hit through the hull.", cost="A2", map="C", render=None,
     sketch="panel(['<rect x=\"0\" y=\"82\" width=\"240\" height=\"18\" fill=\"#3a4048\"/>', rocks(21,1,40,120,30,70,18,20), ship('hfrigate',90,44,3,0), glow(112,44,6,'#bfe1ff',0.9)], 59)")
shot(act="III", title="Lance channels", dur=2, clock="T+5:13:53", real="1:1", body="hull",
     cam="CU · 28 mm · the Endeavor's nose",
     action="The four lance channels in the nose glow violet-white as the field builds.",
     comm=[("ENDEAVOR", "Lance. Now.")], rules=["O12"], vfx="Lance core glow", rig=["lance_power 0→1"],
     assets=["EN", "EN-FIN", "EN-DMG"], sound="A rising electric whine through the hull.", cost="A", map="C", render=None,
     sketch="panel([ship('endeavorNoShield',210,50,2.6,0), glow(114,50,10,'#e3c7ff',0.9)], 61)")
shot(act="III", title="Lance", dur=2, clock="T+5:13:55", real="1:1", body="tracker",
     cam="Tracker · 1,000 mm · on the frigate, 45 km out",
     action="The ship's field reaches out and a spear of plasma crosses the frame from the right to the frigate, forty-five kilometres off, inside the ~50 km the field can hold. The frigate's midsection opens; escape pods scatter as it breaks.",
     comm=[], rules=["O12", "O6"], vfx="Field-held plasma jet, break-up",
     rig=["break 0→1 (new)"], assets=["CF", "FX-LANCE", "FX-BREAK", "FX-VENT"],
     sound="A crack in the score.", cost="B", map="C", render=None,
     sketch="panel(['<line x1=\"240\" y1=\"54\" x2=\"122\" y2=\"50\" stroke=\"#e3c7ff\" stroke-width=\"2.2\"/>', ship('hfrigate',100,50,3.2,0), glow(120,50,12,'#e3c7ff',0.9), sparks(100,50,40,40,63)], 63)")
shot(act="III", title="Broadside", dur=3, clock="T+5:14:00", real="compressed 5× (the roll)", body="hull",
     cam="MS · 35 mm · the port batteries, the rock beyond",
     action="Fins stowed, the Endeavor rolls to bring its port batteries onto the platform's rock, off the port quarter, screen right. The dorsal well battery rises.",
     comm=[], rules=["O6", "O4", "D3"], vfx="",
     rig=["rail_traverse", "rail_elevation", "battery_raise 0→1", "battery_traverse", "battery_elevation"],
     assets=["EN", "EN-FIN", "EN-DMG", "M1C"], sound="The roll's RCS thumps and the battery's rise through the hull.",
     cost="A", map="C", render="img/house_s1combat.jpg", sketch=None)
shot(act="III", title="Rails wake", dur=4, clock="T+5:14:15", real="compressed 2× (the 6–9 s wake)", body="hull",
     cam="CU · 50 mm · on one M-1C turret",
     action="The rails unlock, the twin barrels rise onto the rock, and the charge builds: the capacitor bank's glow creeps up the housing until the turret locks.",
     comm=[], rules=["O4", "O6"], vfx="Rail glow, capacitor glow",
     rig=["rail_wake", "rail_lock", "rail_arm", "charge_a/b"], assets=["EN", "EN-FIN", "EN-DMG", "M1C"],
     sound="A rising whine through the hull, then the lock's clunk.", cost="A", map="C", render=None,
     sketch="panel(['<rect x=\"20\" y=\"38\" width=\"80\" height=\"30\" rx=\"4\" fill=\"#3a4048\"/>', '<rect x=\"96\" y=\"42\" width=\"130\" height=\"6\" fill=\"#9aa6b0\"/>', '<rect x=\"96\" y=\"56\" width=\"130\" height=\"6\" fill=\"#9aa6b0\"/>', glow(96,45,6,'#8fb1ff',0.7), glow(96,59,6,'#8fb1ff',0.7)], 39)")
shot(act="III", title="Fire", dur=2, clock="T+5:14:23", real="1:1", body="hull",
     cam="ECU · 85 mm · on the muzzles",
     action="Gun A fires: the bore pulse (cinematic licence, Q12) and a tracer blast toward the rock. Only the gun that fired vents; gun B waits its turn.",
     comm=[], rules=["O4", "O6"], vfx="Muzzle blast, tracer, venting",
     rig=["shot_a", "fins_a", "heat_a"], assets=["EN", "EN-FIN", "EN-DMG", "M1C", "FX-SLUG"],
     sound="The shot's crack and the recoil's clunk through the hull.", cost="A2", map="C", render=None,
     sketch="panel(['<rect x=\"0\" y=\"42\" width=\"170\" height=\"6\" fill=\"#9aa6b0\"/>', '<rect x=\"0\" y=\"56\" width=\"170\" height=\"6\" fill=\"#9aa6b0\"/>', glow(176,45,22,'#bfe1ff',0.95), streak(180,45,240,40,'#bfe1ff'), glow(60,40,8,'#ff8a3c',0.6)], 40)")
shot(act="III", title="The platform dies", dur=2, clock="T+5:14:40", real="the clock jumps 16 s of flight from the shot", body="tracker",
     cam="Tracker · 1,200 mm · the flash's framing",
     action="The platform's rock flashes: sixteen seconds of flight, and a target that could not move.",
     comm=[], rules=["O4"], vfx="Impact flash", rig=[], assets=["EMP-RG", "BRK", "FX-SLUG"],
     sound="The score.", cost="D", map="C", render=None,
     sketch="panel([rocks(19,1,90,150,30,70,28,30), glow(120,50,20,'#ffd9a0',0.9), sparks(120,50,40,40,65)], 65)")

# ============================================================ ACT IV
shot(act="IV", title="The fire plan", dur=8, clock="T+5:40:00", real="1:1", body="hud",
     cam="HUD insert · the master plot",
     action="The plan builds in two beats, each tied to a clause of the line. First the waves' two tracks from Anchor to where Breakwater will be; then the Astrid's firing point. The pack stays at Anchor with its guard.",
     comm=[("ACTUAL", "Pack, Donnager and Wallfish hold Anchor. The rest, with me.")], hud=["SPEND 7:52 · KILL 7:53", "ASTRID", "SINK 31%"],
     rules=["O9", "O3", "O10", "O11", "D11"], vfx="HUD", rig=[], assets=["HUD"],
     sound="Sensor tones; the score gathers.", cost="E", map="D", render=None,
     sketch="panel([hud(16,10,208,80), planet(196,60,12,'right'), ship('monitor',176,40,0.1,0), rocks(2,1,30,38,26,34,4,4.5), '<line x1=\"38\" y1=\"30\" x2=\"172\" y2=\"40\" stroke=\"#33b3a2\" stroke-width=\"0.6\" stroke-dasharray=\"1 1.5\"/>', label(60,24,'SPEND 7:52 · KILL 7:53','#33b3a2'), '<rect x=\"150\" y=\"20\" width=\"4\" height=\"4\" fill=\"#b476ff\"/>', label(132,16,'ASTRID','#b476ff'), label(20,86,'SINK 31%','#33b3a2')], 67)")
shot(act="IV", title="The net", dur=5, clock="T+6:40:00", real="compressed ~24× (2 min); the digits roll 60 min into it", body="drone",
     cam="WS · 50 mm · over the Extenuating Circumstances",
     action="Hours after Skerry threw them, the first of its rounds arrive. Ahead of the fleet the destroyer's drones light up a spreading cloud of pellets about 20 km across, glittering in their lamps. The fleet side-steps, drives angled off the line; four more nets follow on the lane, ten minutes apart.",
     comm=[("EXTENUATING", "Skerry's rounds. Right on time."), ("ACTUAL", "All ships, left two degrees.")],
     rules=["HO3", "D4", "O8"], vfx="Canister cloud glitter (swarm system)", rig=[],
     assets=["DD", "DRN-L", "FX-SWARM"], sound="Silence; the score ticks.", cost="B", map="D", render=None,
     sketch="panel([ship('destroyer',50,60,1.6,0,true), sparks(170,40,90,70,67), glow(150,30,10,'#e8f2ff',0.3)], 67)")
shot(act="IV", title="Anchor ringed", dur=6, clock="T+6:52:00", real="1:1", body="hud",
     cam="HUD insert · the Donnager's plot at Anchor",
     action="Skerry's sixth salvo was never meant for the lane: three canister clouds ring Anchor, and drones wake on the nearby rocks behind them. The pack has tucked in behind the rock, away from the clouds; the Donnager's batteries and the Wallfish pick the drones off as they come round.",
     comm=[("DONNAGER", "Clouds on Anchor. Drones behind. Pack's tucked in.")], hud=["ANCHOR", "3 CLOUDS", "SINK 62%"],
     rules=["HO3", "HO4", "HD6", "D11", "D6"], vfx="HUD, drone tracks dying", rig=[], assets=["HUD"],
     sound="Sensor tones; clipped chatter.", cost="E", map="D", render=None,
     sketch="panel([hud(16,10,208,80), rocks(2,1,116,124,46,54,5,5.5), sparks(96,40,30,14,44), sparks(144,62,30,14,45), sparks(120,24,24,12,46), label(128,52,'ANCHOR','#33b3a2'), label(150,24,'3 CLOUDS','#e2603f'), label(20,86,'SINK 62%','#33b3a2')], 44)")
shot(act="IV", title="Site One", dur=4, clock="T+6:55:00", real="compressed ~15× (a minute)", body="drone",
     cam="WS · 40 mm · ahead of the Extenuating Circumstances",
     action="Site 1 has been firing since the fleet cleared Anchor's shadow, against rolling hulls, smoke and the fleet's low-power dazzle. Now its invisible beam holds long enough on the destroyer's forward sensor boom: it scorches and smokes, the one visible cost. The ships roll on, and a fresh smoke screen blooms ahead, travelling with the fleet.",
     comm=[("EXTENUATING", "Site One's on our booms. Smoke forward.")], rules=["HO5", "D1", "D3", "O5"],
     vfx="Scorching, fleet-scale smoke screen", rig=["dmg_boom 0→1 (new)"], assets=["DD", "FX-SMOKE", "FX-DAZZLE"],
     sound="Silence.", cost="C", map="D", render=None,
     sketch="panel([ship('destroyer',90,56,2.2,-6,true), smoke(118,40,10), smoke(200,50,40), glow(122,40,4,'#ff8a3c',0.8)], 69)")
shot(act="IV", title="The pack fires", dur=4, clock="T+7:07:00", real="1:1", body="drone",
     cam="WS · 24 mm · low over Anchor, looking toward Breakwater",
     action="From Anchor's shadow the Infinity ripple-fires its multi-pack missiles: hundreds of small plumes on a 45-minute flight, the slow part of the spend wave. Its last killers will follow at T+7:27 so everything lands together.",
     comm=[("ACTUAL", "Spend wave, go."), ("INFINITY", "Slow birds away.")], rules=["O3", "O11"],
     vfx="Ripple launch (swarm system)", rig=["pod_ripple (new)"],
     assets=["GI", "GI-MAV", "MSL-V", "FX-SWARM", "ANCHOR"], sound="Silence; the score drops out.",
     cost="C", map="D", render=None,
     sketch="panel([rocks(14,1,-20,60,60,120,50,52), ship('hedgehog',90,40,1.1,-4), ship('hedgehog',120,62,0.9,-4), trail('M112,38 Q170,28 240,24','#ffd9a0','0.6 0.9',0.8), trail('M136,60 Q190,44 240,40','#ffd9a0','0.6 0.9',0.7), sparks(200,34,30,40,63)], 73)")
shot(act="IV", title="The anvil", dur=4, clock="T+7:25:00", real="compressed 10× (the ripple takes ~40 s)", body="drone",
     cam="WS · 40 mm · above Breakwater, Maren's night side below",
     action="Breakwater's reveal. Its turrets track the fleet but stay silent: the fleet never comes within the range they could hit. Its 64 cells open and ripple-fire, every missile at the Extenuating Circumstances, 17,000 km off, into the fleet's braking burn. Far along the orbit, ring stations wake as points of light.",
     comm=[("ASTRID", "Sixty-four inbound. All on Extenuating.")], rules=["HD7", "HO9", "HD1", "HO1", "D1"],
     vfx="Cell doors, missile launch (swarm system)", rig=["turret_traverse / cells_open (new)"],
     assets=["BW", "RING", "MAREN", "MSL-V", "FX-SWARM"], sound="A low brass sting.", cost="C", map="E", render=None,
     sketch="panel([planet(120,160,120,'right'), ship('monitor',120,34,0.9,0), trail('M86,30 Q50,20 10,24','#ff9d7a','0.6 1',0.6), trail('M86,36 Q50,34 10,40','#ff9d7a','0.6 1',0.6), sparks(226,90,6,10,71)], 71)")
shot(act="IV", title="Kill wave away", dur=3, clock="T+7:28:30", real="1:1", body="tracker",
     cam="Tracker · 300 mm · from the Pillar of Autumn, across Anchor's shadow",
     action="Ninety seconds behind the spend wave's killers, pod doors open down the Galactica's hull and ~40 Casaba killers leave, to arrive among the ~300 decoy and EW birds it launched twenty minutes earlier. In the foreground the Pillar of Autumn's pods stay shut: the reserve.",
     comm=[("GALACTICA", "Kill wave away.")], rules=["O3", "O10", "O11"],
     vfx="Ripple launch (swarm system), defocused foreground", rig=["pod_ripple (new)"],
     assets=["GI", "GI-MAV", "MSL-V", "FX-SWARM", "ANCHOR"], sound="Silence.",
     cost="C", map="D", render=None,
     sketch="panel([rocks(15,1,190,250,-10,30,40,42), ship('hedgehog',60,78,2.4,-3), ship('hedgehog',150,40,1.1,-4), trail('M172,36 Q208,26 240,22','#ffd9a0','0.6 0.9',0.8), trail('M172,42 Q208,38 240,36','#ffd9a0','0.6 0.9',0.7), sparks(212,30,30,30,64)], 74)")
shot(act="IV", title="Umbrella", dur=3, clock="T+7:31:00", real="1:1", body="tracker",
     cam="Tracker · 400 mm · from the Extenuating Circumstances, the Astrid 50 km above",
     action="Breakwater's missiles arrive up the fleet's drive axis. The Astrid has cut its drive for the minute so its plume won't blind its own point defence: its lenses glow violet and its CIWS lay kill clouds across the missiles' path. The flashes walk in toward the Extenuating and stop short.",
     comm=[("EXTENUATING", "Sixty-four down. Thanks, Actual.")], rules=["D1", "D2", "D10", "HO9", "O13"],
     vfx="Kill clouds, intercept flashes, lens glow, the drive's dying glow", rig=["engine_throttle 1→0 (new)", "laser_power (new)", "ciws_phase / ciws_fire (new, on the Astrid)"],
     assets=["AST", "MSL-V", "FX-PD", "FX-SWARM"], sound="Silence; the score's pulse.",
     cost="C", map="E", render=None,
     sketch="panel([ship('astrid',110,40,1.0,0), glow(170,40,4,'#9ec8ff',0.5), tracers(150,34,-15,40,91), glow(206,22,6,'#ffffff',0.85), glow(222,44,4,'#ffffff',0.7), glow(196,58,5,'#ffffff',0.6), sparks(210,36,40,50,92)], 91)")
shot(act="IV", title="Blind it", dur=4, clock="T+7:50:00", real="1:1", body="hull",
     cam="MS · 35 mm · the Endeavor's laser arrays",
     action="The Extenuating Circumstances floods the ring's links. The arrays go from low power to full on Breakwater's optics and Site 1's trackers: lenses violet, beams invisible.",
     comm=[("EXTENUATING", "Their net's down."), ("ENDEAVOR", "All arrays, full power.")], hud=["SINK 88%"],
     rules=["O5", "HD9"],
     vfx="Lens glow, EW overlay on inserts", rig=["laser_power 0.2→1", "laser_traverse", "laser_elevation"],
     assets=["EN", "EN-FIN", "EN-DMG", "FX-EW"], sound="The lenses' capacitor whine through the hull.", cost="A", map="E",
     render="img/lookyoke_final.jpg", sketch=None)
shot(act="IV", title="The spend wave", dur=4, clock="T+7:52:00", real="1:1", body="tracker",
     cam="Tracker · 250 mm · from the Astrid, Maren's limb in frame",
     action="Five degrees off Maren's limb, a sparkle: the spend wave dying against Breakwater's point defence, which lights up and gives away every battery. The destroyer steers the kill wave around them.",
     comm=[("EXTENUATING", "Their batteries are lit. Steering round.")], rules=["O3", "O5", "HD5"],
     vfx="Distant PD sparkle", rig=[], assets=["BW", "FX-PD", "MAREN"],
     sound="The score.", cost="D", map="E", render=None,
     sketch="panel([planet(170,150,110,'right'), sparks(150,36,40,30,75)], 75)")
shot(act="IV", title="Seeker", dur=4, clock="T+7:53:14", real="compressed ~3.5× (the last 14 s of flight)", body="drone",
     cam="ECU · 100 mm · riding a Casaba killer's nose",
     action="The hardened nose of a Casaba killer through its last seconds. The ablative cap glows where Breakwater's lasers are burning it, and tracers streak past; then the seeker shutter opens, and ahead, screen right, Breakwater grows from a point to a sliver.",
     comm=[], rules=["O3", "O10", "HD5"], vfx="Glowing ablative cap, tracers, the seeker window",
     rig=["spin", "seeker_shutter (new)"], assets=["MSL-V", "FX-PD", "BW"],
     sound="Silence; the score climbs.", cost="B", map="E", render=None,
     sketch="panel(['<path d=\"M10,32 L150,40 L150,60 L10,68Z\" fill=\"#6b737b\"/>', '<path d=\"M150,40 L196,50 L150,60Z\" fill=\"#3a3f45\"/>', glow(194,50,12,'#ff8a3c',0.85), '<circle cx=\"176\" cy=\"50\" r=\"3\" fill=\"#0a0d12\" stroke=\"#9aa6b0\" stroke-width=\"0.6\"/>', glow(232,49,2,'#ffffff',0.9), tracers(232,49,180,20,52)], 52)")
shot(act="IV", title="Wall of fire", dur=4, clock="T+7:53:28", real="slowed 5× (the wave arrives within ~1 s)", body="drone",
     cam="WS · 40 mm · above Breakwater",
     action="The kill wave arrives in the same second, nose-on to Breakwater, from screen left. Tracers and dying decoys fill the sky; the hardened noses keep coming.",
     comm=[("GALACTICA", "Kill wave. Three, two—")], rules=["O3", "HD5", "O9"],
     vfx="Tracer streams, intercept flashes, swarm", rig=["ciws_fire (new, on Breakwater)"], assets=["BW", "FX-PD", "FX-SWARM", "MSL-V"],
     sound="A dense crackle in the score; no air, no bangs.", cost="C", map="E", render=None,
     sketch="panel([ship('monitor',140,62,1.0,0), tracers(140,58,-150,60,73), sparks(90,40,60,90,74)], 77)")
shot(act="IV", title="Casaba", dur=4, clock="T+7:53:30", real="slowed 3×", body="drone",
     cam="WS · 35 mm · off Breakwater's quarter",
     action="Two kilometres out, the surviving Casaba charges fire from screen left: nuclear jets lance into Breakwater's drive bells and its engines go dark. The monitor is whole, but it can no longer move.",
     comm=[("ASTRID", "Spears in. Her drive's dark.")], rules=["O10"], vfx="Casaba jets, drive breach, venting",
     rig=["drive_glow 1→0 (new)", "vent (new)"], assets=["BW", "BW-BRK", "MSL-V", "FX-CASABA", "FX-VENT"],
     sound="The comm channels white out, then silence.", cost="C", map="E", render=None,
     sketch="panel([ship('monitor',140,50,1.0,0), '<line x1=\"0\" y1=\"20\" x2=\"86\" y2=\"48\" stroke=\"#ffffff\" stroke-width=\"1.3\"/><line x1=\"2\" y1=\"84\" x2=\"86\" y2=\"54\" stroke=\"#ffffff\" stroke-width=\"1.1\"/>', glow(88,50,12,'#ffffff',0.85)], 79)")
shot(act="IV", title="The hail", dur=5, clock="T+7:54:00", real="1:1", body="drone",
     cam="MS · 50 mm · slow push on Breakwater over the night side",
     action="Breakwater hangs dead-engined over Maren's night side, venting from the spear wounds, its turrets still tracking. On an open channel the Astrid hails it. No answer comes.",
     comm=[("ACTUAL", "Breakwater, you can't move. Strike, or we fire.")], rules=["O10"],
     vfx="Venting", rig=["vent (new)"], assets=["BW", "BW-BRK", "MAREN", "FX-VENT"],
     sound="Silence where the answer should be.", cost="B", map="E", render=None,
     sketch="panel([planet(120,170,120,'right'), sparks(160,92,20,40,81), ship('monitor',120,40,1.0,0), smoke(70,44,12)], 81)")
shot(act="IV", title="Spinal", dur=3, clock="T+7:54:38", real="1:1 (the last degree of the slew; it fires two seconds in, at T+7:54:40)", body="drone",
     cam="MS · 200 mm · the Astrid end-on",
     action="The Astrid, stopped 10,000 km out and 15° off Breakwater's zenith so a miss would clear Maren, settles its last degree and fires. The bloom fills the last second.",
     comm=[("ACTUAL", "Fire.")], rules=["O4", "O10", "HD7", "O9"], vfx="Spinal muzzle bloom",
     rig=["rcs_bow / rcs_stern (new)", "spinal_shot (new)"], assets=["AST", "FX-SPINAL"], sound="Everything drops out.", cost="B", map="E", render=None,
     sketch="panel([glow(120,50,36,'#bfe1ff',0.8), '<circle cx=\"120\" cy=\"50\" r=\"10\" fill=\"#cfd6dc\"/>', '<g stroke=\"#ff8a3c\" stroke-width=\"2\">' + [0,1,2,3,4,5,6,7].map(function(i){var a=i/8*6.283;return '<line x1=\"'+(120+Math.cos(a)*12).toFixed(1)+'\" y1=\"'+(50+Math.sin(a)*12).toFixed(1)+'\" x2=\"'+(120+Math.cos(a)*34).toFixed(1)+'\" y2=\"'+(50+Math.sin(a)*34).toFixed(1)+'\"/>';}).join('') + '</g>', glow(120,50,8,'#ffffff',0.95)], 83)")
shot(act="IV", title="The wait", dur=6, clock="T+7:54:41", real="compressed ~27× (163 of the slug's 167 s; the clock races)", body="drone",
     cam="WS · 35 mm · the Casaba shot's angle",
     action="Hold on the crippled monitor, turrets swinging uselessly, while the clock races through the slug's flight.",
     comm=[("ASTRID", "Impact in two forty-seven.")], rules=["O10"], vfx="Venting", rig=["turret_traverse (new)"],
     assets=["BW", "BW-BRK"], sound="Silence; one held note.", cost="B", map="E", render=None,
     sketch="panel([ship('monitor',140,50,1.0,0), smoke(88,50,14), label(8,92,'T+7:56:10','#6fd3c4')], 85)")
shot(act="IV", title="Impact", dur=3, clock="T+7:57:27", real="1:1", body="drone",
     cam="WS · 35 mm · the Casaba shot's angle",
     action="The slug arrives amidships, near the spear damage: a white flash, a spall cone, and Breakwater's back breaks in a chain of secondary flashes.",
     comm=[], rules=["O4"], vfx="Impact, spall, section break", rig=["break 0→1 (new)"],
     assets=["BW", "BW-BRK", "FX-SPINAL", "FX-BREAK"], sound="One deep boom in the score, on the cut.", cost="C", map="E", render=None,
     sketch="panel([ship('monitor',140,50,1.2,12), glow(140,50,26,'#ffd9a0',0.8), sparks(140,50,70,60,83), smoke(150,56,30)], 87)")
shot(act="IV", title="Heat", dur=4, clock="T+8:00:00", real="1:1", body="hull",
     cam="MS · 35 mm · along the Endeavor's scorched port flank",
     action="Its arrays stood down when Breakwater died, but the Endeavor's sink still reads 98 %. A valve opens and a thousand tonnes of water boil out in a white plume streaming off the ship: half an hour of margin.",
     comm=[("ENDEAVOR", "Dump the water.")], hud=["SINK 98%"], rules=["D3", "D7"], vfx="Water-dump plume",
     rig=["water_dump 0→1 (new)"], assets=["EN", "EN-FIN", "EN-DMG", "EN-PD", "FX-DUMP"],
     sound="A roar through the hull, then a long hiss.", cost="V", map="E", render=None,
     sketch="panel([ship('endeavorNoShield',150,50,1.2,0), glow(120,30,20,'#e8eef4',0.6), glow(92,20,24,'#e8eef4',0.4), glow(60,12,26,'#e8eef4',0.25)], 89)")
shot(act="IV", title="Terms", dur=8, clock="T+8:10:00", real="1:1", body="tracker",
     cam="Tracker · 2,000 mm · from the Endeavor's standoff",
     action="Far off, 8,500 km away, Breakwater's wreck is a glittering smear venting over the night side; the Astrid's firing line has already swung onto the next ring station. The exchange plays first; then the last plot holds alone for two seconds on the two dark channels.",
     comm=[("EXTENUATING", "Actual, Maren's asking for terms."), ("ACTUAL", "Site One goes dark first.")], hud=["CANTERBURY · NORMANDY: NO CARRIER"],
     rules=["O4", "D7"], vfx="Distant wreck, HUD tag", rig=[], assets=["BW", "BW-BRK", "MAREN", "RING", "HUD"],
     sound="The score, low.", cost="D", map="E", render=None,
     sketch="panel([planet(120,170,120,'right'), sparks(120,50,30,20,90), glow(120,50,6,'#ffd9a0',0.6), label(8,92,'CANTERBURY · NORMANDY: NO CARRIER','#9fb0bc')], 90)")
shot(act="IV", title="Site One goes dark", dur=2, clock="T+8:24:00", real="1:1", body="tracker",
     cam="Tracker · 2,000 mm · on Site 1's plateau, night side",
     action="A cluster of lights on Maren's night side, about ten pixels wide: Site 1. They go out, block by block.",
     comm=[("ENDEAVOR", "Site One's dark.")], rules=["O9"], vfx="City lights going out", rig=[],
     assets=["MAREN", "WORLD"], sound="The score falls away.", cost="D", map="E", render=None,
     sketch="panel([planet(120,190,160,'right'), sparks(120,52,24,16,61), glow(120,52,10,'#ffd9a0',0.25)], 61)")
shot(act="IV", title="Hold", dur=7, clock="T+8:24:02", real="1:1", body="drone",
     cam="EWS · 35 mm · locked off, the Endeavor end-on",
     action="The Endeavor, end-on, runs out its three fins (already part-way out) in silence, into a broken cross glowing orange against the night side, the stump where the fourth was. Cut to black under the last line.",
     comm=[("ACTUAL", "Nauvoo, bring the shields in. T-SEC, the sky's yours.")],
     rules=["D3"], vfx="Fin glow",
     rig=["fin_starboard / fin_dorsal / fin_ventral 0.5→1 (new)", "heat 2.4", "radiator_glow"],
     assets=["EN", "EN-FIN", "EN-DMG", "MAREN", "WORLD"], sound="The score resolves; then silence.",
     cost="P", map="E", render="img/hero_s1combat.jpg", sketch=None)

SHOTS = S
