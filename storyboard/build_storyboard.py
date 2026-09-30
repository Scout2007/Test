#!/usr/bin/env python3
"""Build the Operation Tidebreak storyboard from storyboard/tidebreak_data.py.

    pip install pillow            # only needed the first time, to convert renders
    python3 storyboard/build_storyboard.py [--fragment PATH] [--doc-base URL]

Writes:
  storyboard/index.html      the board (maps, timeline, shot cards)
  storyboard/shots.csv       one row per shot
  storyboard/shots.md        the readable shot list
  ASSET_REQUESTS.md          everything the storyboard needs that is not built
  storyboard/img/*.jpg       reference frames (converted once from pack/renders)

It checks the data on the way (doctrine rule IDs, asset IDs, shot references,
the mission clock, subtitle reading speed, what each camera body can hear,
rig controls marked new, the spinal impact time, set coverage) and prints what
it finds, with the render budget against the gate.

--fragment writes the page without <html>/<head>/<body> for the artifact viewer.
--doc-base sets where doctrine rule links point (default: the local reading edition).
"""
import csv
import html
import importlib.util
import math
import os
import pathlib
import random
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SB = ROOT / "storyboard"
spec = importlib.util.spec_from_file_location("data", SB / "tidebreak_data.py")
D = importlib.util.module_from_spec(spec)
spec.loader.exec_module(D)

DOC_BASE = "../doctrine/reading/Tidebreak_doctrines.html"
if "--doc-base" in sys.argv:
    DOC_BASE = sys.argv[sys.argv.index("--doc-base") + 1]

E = html.escape
FPS = D.FPS
ESTIMATE = {c: float(re.search(r"([\d.]+) s/frame", cost).group(1)) for c, (_, cost) in D.RENDER_CLASSES.items()}
SEC_PER_FRAME = {**ESTIMATE, **{k: v for k, v in D.MEASURED.items() if k in ESTIMATE}}
MAX_CPS = 12          # subtitle reading speed ceiling (round 1 cinematography review)
MARGIN = 0.30         # re-render allowance on the render budget
BODY_LABEL = {"hull": "hull camera", "drone": "drone camera", "tracker": "tracker", "hud": "HUD insert"}
NOTES = []            # what the checks found; printed at the end


def clock_s(c):
    h, m, s = c[2:].split(":")
    return int(h) * 3600 + int(m) * 60 + int(s)


def fmt_clock(sec):
    sec = round(sec)
    return f"T+{sec // 3600}:{sec % 3600 // 60:02d}:{sec % 60:02d}"


def mmss(sec):
    return f"{int(sec // 60)}:{sec % 60:04.1f}"


def rule_doc(rid):
    return "maren" if rid.startswith("H") else "lref"


def rule_anchor(rid):
    """The rule's anchor in the reading edition; '§13' cites a section of the LREF doctrine."""
    return f"lref-s{rid[1:]}" if rid.startswith("§") else f"{rule_doc(rid)}-{rid}"


# ----------------------------------------------------------------- shot numbers and references
TITLES = {}
for i, s in enumerate(D.SHOTS, 1):
    if s["title"] in TITLES:
        sys.exit(f"duplicate shot title: {s['title']}")
    TITLES[s["title"]] = i
REF = re.compile(r"\{#([^}]+)\}")


def resolve(text):
    def sub(m):
        if m.group(1) not in TITLES:
            sys.exit(f"unknown shot reference {{#{m.group(1)}}}")
        return str(TITLES[m.group(1)])
    return REF.sub(sub, text)


def walk(x):
    """Resolve {#Title} references everywhere except in sketch code."""
    if isinstance(x, str):
        return resolve(x)
    if isinstance(x, list):
        return [walk(v) for v in x]
    if isinstance(x, tuple):
        return tuple(walk(v) for v in x)
    if isinstance(x, dict):
        return {k: (v if k == "sketch" else walk(v)) for k, v in x.items()}
    return x


for _name in ("PHASES", "KEY_NUMBERS", "LIGHTING", "CLOCK_HUD", "SCREEN_DIRECTION", "CAMERA_BODIES", "FLEET",
              "DEFENDERS", "ASSETS", "RENDER_NOTE", "PRODUCTION_PLAN", "ACTS", "MAPS", "REVIEW_STATUS", "REVIEWS",
              "SHOTS"):
    setattr(D, _name, walk(getattr(D, _name)))


def shot_no(title, where):
    if title not in TITLES:
        sys.exit(f"{where}: no shot titled '{title}'")
    return TITLES[title]


CLOSEST = {a: (shot_no(t, f"CLOSEST[{a}]"), resolve(what), size) for a, (t, what, size) in D.CLOSEST.items()}
SETS = [(name, sorted(shot_no(t, f"SETS[{name}]") for t in titles)) for name, titles in D.SETS]

# ----------------------------------------------------------------- timing
t = 0
tagged = set()        # speakers whose tag the viewer has read once
for n, s in enumerate(D.SHOTS, 1):
    s["n"] = n
    s.setdefault("hud", [])
    s.setdefault("see", "")
    s.setdefault("group", None)
    # A comm line may carry a cue: the second in the shot where it starts, after its event.
    s["cues"] = [c[2] if len(c) > 2 else None for c in s["comm"]]
    s["comm"] = [(c[0], c[1]) for c in s["comm"]]
    # A speaker's first tag is read like any text (it may carry the ship's class); later ones, or a short form
    # of it (ACTUAL after TIDEBREAK ACTUAL), are taken in at a glance.
    s["tagc"] = []
    for sp, _ in s["comm"]:
        name = sp.split(" · ")[0]
        s["tagc"].append(0 if any(p == name or p.endswith(" " + name) for p in tagged) else len(sp))
        tagged.add(name)
    if s["comm"] and "SUB" not in s["assets"]:
        s["assets"].append("SUB")
    s["t0"], s["t1"] = t, t + s["dur"]
    s["f0"], s["f1"] = t * FPS + 1, (t + s["dur"]) * FPS
    s["shields"] = clock_s(s["clock"]) < clock_s(D.SHIELDS_OFF)
    t += s["dur"]
RUNTIME = t
FRAMES = RUNTIME * FPS
MISSION_END = D.SHOTS[-1]["clock"][:-3]


def ranges(nums):
    """[1, 2, 3, 5] -> '1–3, 5'"""
    out, i = [], 0
    while i < len(nums):
        j = i
        while j + 1 < len(nums) and nums[j + 1] == nums[j] + 1:
            j += 1
        out.append(str(nums[i]) if i == j else f"{nums[i]}–{nums[j]}")
        i = j + 1
    return ", ".join(out)


# ----------------------------------------------------------------- images
IMG_SOURCES = {
    "bow_v4b_combat.jpg": "pack/storyboard_draft/img/bow_v4b_combat.jpg",
    "endeavor_combat_demo_f060.jpg": "pack/storyboard_draft/img/endeavor_combat_demo_f060.jpg",
    "lookpair_final.jpg": "pack/storyboard_draft/img/lookpair_final.jpg",
    "lookyoke_final.jpg": "pack/storyboard_draft/img/lookyoke_final.jpg",
    "orbit_v8d.jpg": "pack/renders/orbit_v8d.png",
    "lookmast_v8d.jpg": "pack/renders/lookmast_v8d.png",
    "lookaft_s1combat.jpg": "pack/renders/lookaft_s1combat.png",
    "house_s1combat.jpg": "pack/renders/house_s1combat.png",
    "hero_s1combat.jpg": "pack/renders/hero_s1combat.png",
}


def prepare_images():
    (SB / "img").mkdir(parents=True, exist_ok=True)
    for name, src in IMG_SOURCES.items():
        dst = SB / "img" / name
        if dst.exists():
            continue
        src = ROOT / src
        if src.suffix == ".jpg":
            shutil.copy(src, dst)
            continue
        from PIL import Image  # only needed for the first conversion
        im = Image.open(src).convert("RGB")
        if im.width > 1280:
            im = im.resize((1280, round(im.height * 1280 / im.width)))
        im.save(dst, "JPEG", quality=82, optimize=True)


# ----------------------------------------------------------------- checks
def clock_rate(real):
    """Mission seconds per screen second, or None when the shot doesn't say."""
    if real.startswith(("1:1", "the clock jumps")):
        return 1.0
    m = re.match(r"(compressed|slowed) ~?([\d.]+)×", real)
    if m:
        k = float(m.group(2))
        return k if m.group(1) == "compressed" else 1 / k
    return None


def shot_end(s):
    """Mission clock (s) at the end of a shot: its explicit `end`, or its start plus duration × rate."""
    if s.get("end"):
        return clock_s(s["end"])
    rate = clock_rate(s["real"])
    return None if rate is None else clock_s(s["clock"]) + s["dur"] * rate


def state_of(asset, clock):
    """The asset's state (STATES) at a mission clock, or None."""
    out = None
    for start, text in D.STATES.get(asset, []):
        if clock_s(clock) >= clock_s(start):
            out = text
    return out


# Words a camera that can't hear must not be given, unless the same clause (split at , ; and .)
# puts them in the score or a channel ("no bangs" is fine).
HEARD = re.compile(r"through the|(?<!no )\b(roar|clang|bang|thump|thud|clunk|groan|shear|whin|boom|tick|hiss|crack|"
                   r"rumbl|pop|hum(?!an))\w*", re.I)
EXEMPT = re.compile(r"score|channel|sub-bass", re.I)


def world_of(s):
    """The World preset a shot renders in: its own `world`, else its map's."""
    return s.get("world") or s["map"]


def clockless(s):
    """The report's own cards, before the record and after it, carry no mission clock."""
    return s["act"] in ("P", "E")


def reading_groups():
    """Runs of shots that share one reading window: consecutive shots with the same `group`, else one shot each."""
    out = []
    for s in D.SHOTS:
        if out and s["group"] and out[-1][0]["group"] == s["group"]:
            out[-1].append(s)
        else:
            out.append([s])
    return out


def cue_windows(run):
    """(shot, characters to read, line, start s, window s) for every cued line in a run of shots, the characters
    counting a first tag; a shot's last line may run on
    over the following shots of the run that have no lines of their own."""
    out = []
    for i, s in enumerate(run):
        for j, ((sp, line), cue) in enumerate(zip(s["comm"], s["cues"])):
            if cue is None:
                continue
            later = [c for c in s["cues"][j + 1:] if c is not None]
            if later:
                end = later[0]
            else:
                end = s["dur"]
                for nxt in run[i + 1:]:
                    if nxt["comm"]:
                        break
                    end += nxt["dur"]
            out.append((s, len(line) + s["tagc"][j], line, cue, end - cue))
    return out


def rig_controls(item):
    """The control names in a rig item marked '(new)': 'fin_* 0→1 (new)' -> ['fin_*']."""
    head = re.split(r"[\d→]", item.split("(new")[0])[0]
    return [p.split()[0] for p in head.split("/") if p.strip()]


def check():
    rule_ids = set()
    for f in ("LREF_doctrine.md", "Defence_doctrine.md"):
        rule_ids |= set(re.findall(r"^\|\s*\*\*((?:O|D|HO|HD)\d+)\*\*", (ROOT / "doctrine" / f).read_text(), re.M))
    rule_ids |= {f"§{n}" for n in re.findall(r"^## (\d+)\.", (ROOT / "doctrine" / "LREF_doctrine.md").read_text(), re.M)}
    requested = set(re.findall(r"`([^`]+)`", " ".join(v[3] for v in D.ASSETS.values())))
    for s in D.SHOTS:
        tag = f"shot {s['n']} ({s['title']})"
        bad = ([f"rule {r}" for r in s["rules"] if r not in rule_ids] +
               [f"asset {a}" for a in s["assets"] if a not in D.ASSETS] +
               ([f"camera body {s['body']}"] if s["body"] not in D.CAMERA_BODIES else []) +
               ([f"render class {s['cost']}"] if s["cost"] not in D.RENDER_CLASSES else []) +
               ([f"map {s['map']}"] if s["map"] not in D.MAPS else []) +
               ([f"reference frame {s['render']}"] if s["render"] and s["render"][4:] not in IMG_SOURCES else []))
        if bad:
            sys.exit(f"{tag}: unknown " + ", ".join(bad))
        if len(s["comm"]) > s["dur"]:
            NOTES.append(f"{tag}: {len(s['comm'])} lines in {s['dur']} s (at least 1 s a line)")
        if not s["see"]:
            NOTES.append(f"{tag}: no `see` line, so the audience script can't show it")
        if s["sketch"] and re.search(r"['\"]", re.sub(r"'(?:[^'\\\n]|\\.)*'|\"(?:[^\"\\\n]|\\.)*\"", "", s["sketch"])):
            NOTES.append(f"{tag}: the sketch has an unmatched quote (an apostrophe in its text?), which breaks every sketch on the page")
        if s["body"] != "hull":
            for clause in re.split(r"[;.,]", s["sound"]):
                if HEARD.search(clause) and not EXEMPT.search(clause):
                    NOTES.append(f"{tag}: a {s['body']} camera can't hear '{clause.strip()}'")
        if s["body"] == "hud" and "plot" in s["cam"] and s["dur"] < 5:
            NOTES.append(f"{tag}: a geography insert holds {s['dur']} s (at least 5 s)")
        for item in s["rig"]:
            if "(new" in item:
                for c in rig_controls(item):
                    if not (any(r.startswith(c[:-1]) for r in requested) if c.endswith("*") else c in requested):
                        NOTES.append(f"{tag}: rig control '{c}' is marked new but no asset requests it")
        if shot_end(s) is None:
            NOTES.append(f"{tag}: no stated rate or end clock, so its end can't be checked")
        for asset, start, needed in D.STATE_ASSETS:
            if asset in s["assets"] and clock_s(s["clock"]) >= clock_s(start) and needed not in s["assets"]:
                NOTES.append(f"{tag}: {asset} is in its '{state_of(asset, s['clock'])}' state, so it needs {needed}")
        if s["body"] != "hud" and world_of(s) not in D.ENVS:
            NOTES.append(f"{tag}: no World preset '{world_of(s)}'")
    for run in reading_groups():
        chars = (sum(len(line) + c for s in run for (_, line), c in zip(s["comm"], s["tagc"]))
                 + sum(len(h) for s in run for h in s["hud"]))
        dur = sum(s["dur"] for s in run)
        ceiling = min(s.get("cps", MAX_CPS) for s in run)     # title cards may set a higher one
        if chars / dur > ceiling:
            where = f"shot {run[0]['n']}" + (f"–{run[-1]['n']}" if len(run) > 1 else "") + f" ({run[0]['title']})"
            NOTES.append(f"{where}: subtitles and HUD text at {chars / dur:.1f} characters a second (ceiling {ceiling})")
        for s, chars, line, cue, window in cue_windows(run):
            if window <= 0 or chars / window > MAX_CPS:
                NOTES.append(f"shot {s['n']} ({s['title']}): '{line}' has {window:.1f} s from its cue ({chars / max(window, 0.01):.1f} cps)")
    wait = D.SHOTS[shot_no("The wait", "the sunrise check") - 1]
    first, full = sunrise("Breakwater")
    if not clock_s(wait["clock"]) <= first < full <= shot_end(wait):
        NOTES.append(f"Breakwater's sunrise ({fmt_clock(first)}–{fmt_clock(full)}) doesn't fall inside shot {wait['n']} (The wait)")
    for a, b in zip(D.SHOTS, D.SHOTS[1:]):
        end = shot_end(a)
        if end is None:
            continue
        if clock_s(b["clock"]) < end - 0.5:
            NOTES.append(f"shot {b['n']} ({b['title']}) starts at {b['clock']}, before shot {a['n']} ends at {fmt_clock(end)}")
        if clock_s(b["clock"]) - end >= 1800 and not re.search(r"roll|dissolve", b["real"]):
            NOTES.append(f"shot {b['n']} ({b['title']}) jumps {round((clock_s(b['clock']) - end) / 60)} min with no roll or dissolve marked")
    impact = D.SHOTS[shot_no("Impact", "the spinal check") - 1]
    if abs(clock_s(impact["clock"]) - T_HIT * 3600) > 1:
        NOTES.append(f"shot {impact['n']} (Impact) starts at {impact['clock']}, but the slug arrives at {fmt_clock(T_HIT * 3600)}")
    for start, text in D.STATES["BW"]:
        if text == "back broken" and abs(clock_s(start) - T_HIT * 3600) > 1:
            NOTES.append(f"Breakwater's back breaks at {start} in STATES, but the slug arrives at {fmt_clock(T_HIT * 3600)}")
    for a, (n, _, _) in CLOSEST.items():
        if a not in D.SHOTS[n - 1]["assets"]:
            NOTES.append(f"closest view of {a} is shot {n}, which doesn't use it")
    counts = {}
    for _, nums in SETS:
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
    for s in D.SHOTS:
        if counts.get(s["n"], 0) != 1:
            NOTES.append(f"shot {s['n']} ({s['title']}) is in {counts.get(s['n'], 0)} set-ups, not one")
    grouped = [a for _, ids in ASSET_GROUPS for a in ids]
    for a in D.ASSETS:
        if grouped.count(a) != 1:
            NOTES.append(f"asset {a} is in {grouped.count(a)} groups of ASSET_REQUESTS.md, not one")


# ----------------------------------------------------------------- geometry
# Maren-centred inertial frame in km. The fleet arrives from -x, so on every map
# Maren is screen right, as in the film's HUD. Angles are degrees counter-clockwise
# from +x. At T+5:09 Anchor, Breakwater and Site 1 line up at 180°.
G1 = 9.80665e-3                                   # 1 g, km/s²
W_MAREN = 360 / 23.934                            # °/h (sidereal day)
W_ANCHOR = math.degrees(1.63 / 150_000 * 3600)    # °/h (1.63 km/s at 150,000 km)
T_ALIGN = 5 + 9 / 60                              # hours: Anchor over Site 1
SUN = 33.2                                        # direction of the sun from Maren, in the ring plane (Maren's
                                                  # equinox); chosen so Breakwater's sunrise falls in The wait
SUN_R = math.radians(0.2666)                      # the sun's angular radius at 1 AU
R_MAREN = 6_400
BURN = 20 / G1                                    # s: 0 → 20 km/s at 1 g
BURN_KM = 0.5 * G1 * BURN ** 2
FLIP = 49                                         # s: the Endeavor's flip
MAREN_HALF = math.degrees(math.asin(6_400 / 42_164))   # Maren's half-width seen from Breakwater


def hours(clock):
    return clock_s(clock) / 3600


def pol(r, deg, origin=(0.0, 0.0)):
    return (origin[0] + r * math.cos(math.radians(deg)), origin[1] + r * math.sin(math.radians(deg)))


def bearing(p, q):
    return math.degrees(math.atan2(q[1] - p[1], q[0] - p[0]))


def angdiff(a, b):
    """Smallest angle between two directions, degrees."""
    return abs((a - b + 180) % 360 - 180)


def line_miss(p, q):
    """Distance from Maren's centre to the straight line through p and q (km)."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    return abs(dx * p[1] - dy * p[0]) / math.hypot(dx, dy)


def path_point(p0, p1, s):
    L = math.dist(p0, p1)
    return (p0[0] + (p1[0] - p0[0]) * s / L, p0[1] + (p1[1] - p0[1]) * s / L)


def th_bw(t):
    return 180 + W_MAREN * (t - T_ALIGN)


def bw_at(t):
    return pol(42_164, th_bw(t))


def site1_at(t):
    return pol(6_400, th_bw(t))


def anchor_at(t):
    return pol(150_000, 180 + W_ANCHOR * (t - T_ALIGN))


def off_zenith(t, rng, off):
    """A point rng km from Breakwater, off degrees from its zenith, on Anchor's side."""
    return pol(rng, th_bw(t) - off, bw_at(t))


EXIT, ANCHOR = (-450_000.0, 20_000.0), anchor_at(T_ALIGN)
SKERRY = pol(380_000, 140)


def approach_r(t):
    """Distance from Maren during the approach: wait, burn at T+0:25, coast, flip at T+4:34:10, brake."""
    s, start, turn = t * 3600, 25 * 60, clock_s("T+4:34:10")
    if s <= start:
        return 450_000
    if s <= start + BURN:
        return 450_000 - 0.5 * G1 * (s - start) ** 2
    coasted = min(s, turn + FLIP) - start - BURN
    x = min(max(s - turn - FLIP, 0), BURN)
    return 450_000 - BURN_KM - 20 * coasted - (20 * x - 0.5 * G1 * x * x)


def track(r):
    """The point on the exit → Anchor line at distance r from Maren (along x)."""
    return (-r, 20_000 * (r - 150_000) / 300_000)


T_DEP = hours("T+5:43:00")
A_DEP = anchor_at(T_DEP)
ESCORTS = (8_500, 25)      # km from Breakwater, degrees off its zenith: where the escorts stop
ASTRID = (10_000, 15)      # where the Astrid stops and fires (the spinal's line clears Maren)


def _final_approach():
    """Anchor (T+5:43) to the escorts' stop: 1 g, coast, flip, 1 g."""
    t_stop = hours("T+7:50:00")
    for _ in range(30):
        stop = off_zenith(t_stop, *ESCORTS)
        L = math.dist(A_DEP, stop)
        coast = (L - 2 * BURN_KM - 20 * FLIP) / 20
        t_stop = T_DEP + (2 * BURN + FLIP + coast) / 3600
    return stop, L, coast, t_stop


STOP, FINAL_KM, COAST, T_STOP = _final_approach()
T_TURN = T_DEP + (BURN + COAST) / 3600


def final_at(t):
    s = (t - T_DEP) * 3600
    if s <= BURN:
        d = 0.5 * G1 * s * s
    elif s <= BURN + COAST + FLIP:
        d = BURN_KM + 20 * (s - BURN)
    else:
        x = min(s - BURN - COAST - FLIP, BURN)
        d = BURN_KM + 20 * (COAST + FLIP) + 20 * x - 0.5 * G1 * x * x
    return path_point(A_DEP, STOP, d)


V_SPINAL = 60.0                      # km/s: the Astrid's spinal slug (WN §2)
T_FIRE = hours("T+7:54:40")


def _spinal():
    """The Astrid fires from rest and leads the moving monitor: where it fires from, the hit, the impact time."""
    ast, t = off_zenith(T_FIRE, *ASTRID), T_FIRE
    for _ in range(50):
        hit = bw_at(t)
        t = T_FIRE + math.dist(ast, hit) / V_SPINAL / 3600
    return ast, hit, t


AST_FIRE, HIT, T_HIT = _spinal()


# ----------------------------------------------------------------- Maren's shadow
def light(p):
    """'sun', 'penumbra' or 'umbra' at a point (km, Maren-centred), from the solid planet's shadow."""
    s = (math.cos(math.radians(SUN)), math.sin(math.radians(SUN)))
    behind = -(p[0] * s[0] + p[1] * s[1])        # distance behind Maren along the anti-sun axis
    off = abs(p[0] * s[1] - p[1] * s[0])         # distance from that axis
    if behind <= 0 or off >= R_MAREN + behind * math.tan(SUN_R):
        return "sun"
    return "umbra" if off < R_MAREN - behind * math.tan(SUN_R) else "penumbra"


def escort_at(t):
    return final_at(t) if t < T_STOP else off_zenith(t, *ESCORTS)


def astrid_at(t):
    """The Astrid trails the line, then holds 10,000 km out, 15° off Breakwater's zenith."""
    return escort_at(t) if t < T_STOP else off_zenith(t, *ASTRID)


BODIES = {"Breakwater": bw_at, "the escorts": escort_at, "the Astrid": astrid_at}
BODY_ASSETS = {"Breakwater": ["BW"], "the escorts": ["EN", "DD", "CV"], "the Astrid": ["AST"]}


def shadow_changes(fn, t0="T+6:00:00", t1="T+8:30:00", step=1):
    """[(clock s, state)] each time a body's light changes between two clocks."""
    out, prev = [], None
    for sec in range(clock_s(t0), clock_s(t1) + 1, step):
        st = light(fn(sec / 3600))
        if st != prev:
            out.append((sec, st))
            prev = st
    return out


SHADOW = {name: shadow_changes(fn) for name, fn in BODIES.items()}


def sunrise(name):
    """(first light, full sun) in clock seconds: the last time a body leaves Maren's umbra."""
    ch = SHADOW[name]
    i = max(k for k, (_, st) in enumerate(ch) if st == "umbra")
    return ch[i + 1][0], ch[i + 2][0]


def eclipse_text():
    bw_in = next(sec for sec, st in SHADOW["Breakwater"] if st == "umbra")
    es_in = next(sec for sec, st in SHADOW["the escorts"] if st == "umbra")
    (b0, b1), (e0, e1), (a0, a1) = sunrise("Breakwater"), sunrise("the escorts"), sunrise("the Astrid")
    c = lambda sec: fmt_clock(sec)
    return (f"Maren's shadow reaches past Breakwater's orbit. Breakwater is in it from {c(bw_in)}; its sunrise falls inside "
            f"{{#The wait}}: first light {c(b0)}, full sun {c(b1)}, before the slug lands. The escorts are in the shadow from "
            f"{c(es_in)} to {c(e0)}–{c(e1)}, and the Astrid, at its stop, until {c(a0)}–{c(a1)}. In the shadow nothing is sunlit: "
            "hulls are lit by the thin red ring of Maren's atmosphere (sunlight bent round the limb), the night side's city glow "
            "from below, and their own lenses, plumes and flashes. First light is red through the limb and turns white as the sun clears it.")


def light_note(s):
    """Where Breakwater, the escorts (Endeavor, destroyers) and the Astrid stand in Maren's shadow during a shot."""
    t0 = clock_s(s["clock"])
    t1 = shot_end(s) or t0
    if s["map"] not in ("D", "E") or t1 < clock_s("T+6:00:00"):
        return ""
    out = []
    for name, ids in (("Breakwater", ["BW"]), ("the escorts", ["EN", "DD"]), ("the Astrid", ["AST"])):
        if any(a in s["assets"] for a in ids):
            states = [light(BODIES[name](t0 / 3600))] + [st for sec, st in SHADOW[name] if t0 < sec <= t1]
            out.append(f"{name} in {' → '.join('sun' if x == 'sun' else x for x in states)}")
    return "; ".join(out)


# ----------------------------------------------------------------- maps
class Map:
    def __init__(self, x0, x1, y0, y1, scale, pad=12):
        self.x0, self.x1, self.y0, self.y1, self.s, self.pad = x0, x1, y0, y1, scale, pad
        self.w = (x1 - x0) / scale + 2 * pad
        self.h = (y1 - y0) / scale + 2 * pad
        self.out = []

    def P(self, x, y):
        return ((x - self.x0) / self.s + self.pad, (self.y1 - y) / self.s + self.pad)

    def add(self, s):
        self.out.append(s)

    def circle(self, x, y, r_km, cls, min_px=0, extra=""):
        px, py = self.P(x, y)
        r = max(r_km / self.s, min_px)
        self.add(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r:.1f}" class="{cls}" {extra}/>')

    def line(self, pts, cls, extra=""):
        d = " ".join(f"{'M' if i == 0 else 'L'}{self.P(x, y)[0]:.1f},{self.P(x, y)[1]:.1f}" for i, (x, y) in enumerate(pts))
        self.add(f'<path d="{d}" class="{cls}" {extra}/>')

    def arrow(self, p0, p1, cls="m-arrow"):
        self.line([p0, p1], cls, 'marker-end="url(#arr)"')

    def poly(self, pts, cls):
        d = " ".join(f"{'M' if i == 0 else 'L'}{x:.1f},{y:.1f}" for i, (x, y) in enumerate(self.P(*q) for q in pts))
        self.add(f'<path d="{d}Z" class="{cls}"/>')

    def halfplane(self, p, deg, cls):
        """Shade the side of the line through p, perpendicular to deg, that deg points into."""
        nx, ny = math.cos(math.radians(deg)), math.sin(math.radians(deg))
        side = lambda q: (q[0] - p[0]) * nx + (q[1] - p[1]) * ny
        rect = [(self.x0, self.y0), (self.x1, self.y0), (self.x1, self.y1), (self.x0, self.y1)]
        out = []
        for i in range(4):
            a, b = rect[i], rect[(i + 1) % 4]
            sa, sb = side(a), side(b)
            if sa >= 0:
                out.append(a)
            if (sa >= 0) != (sb >= 0):
                k = sa / (sa - sb)
                out.append((a[0] + (b[0] - a[0]) * k, a[1] + (b[1] - a[1]) * k))
        if len(out) > 2:
            self.poly(out, cls)

    def curve(self, a, c, b, cls):
        (ax, ay), (cx, cy), (bx, by) = self.P(*a), self.P(*c), self.P(*b)
        self.add(f'<path d="M{ax:.1f},{ay:.1f} Q{cx:.1f},{cy:.1f} {bx:.1f},{by:.1f}" class="{cls}"/>')

    def text(self, x, y, s, cls="m-t", anchor="start", dx=0, dy=0):
        px, py = self.P(x, y)
        self.add(f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" class="{cls}" text-anchor="{anchor}">{E(s)}</text>')

    def text_along(self, p0, p1, s, cls="m-t", f=0.0, off=12):
        """Text laid along the segment p0→p1, starting a fraction f along it; off > 0 sits below the line."""
        (x0, y0), (x1, y1) = self.P(*p0), self.P(*p1)
        ang = math.degrees(math.atan2(y1 - y0, x1 - x0))
        x, y = x0 + (x1 - x0) * f, y0 + (y1 - y0) * f
        self.add(f'<text transform="translate({x:.1f},{y:.1f}) rotate({ang:.1f})" y="{off}" class="{cls}">{E(s)}</text>')

    def mark(self, x, y, cls, shape="dot", size=3.2):
        px, py = self.P(x, y)
        if shape == "dot":
            self.add(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{size}" class="{cls}"/>')
        elif shape == "sq":
            self.add(f'<rect x="{px - size:.1f}" y="{py - size:.1f}" width="{2 * size}" height="{2 * size}" class="{cls}"/>')
        elif shape == "dia":
            self.add(f'<path d="M{px:.1f},{py - size * 1.3:.1f} L{px + size:.1f},{py:.1f} L{px:.1f},{py + size * 1.3:.1f} L{px - size:.1f},{py:.1f}Z" class="{cls}"/>')
        elif shape == "x":
            self.add(f'<path d="M{px - size:.1f},{py - size:.1f} L{px + size:.1f},{py + size:.1f} M{px + size:.1f},{py - size:.1f} L{px - size:.1f},{py + size:.1f}" class="{cls}"/>')
        elif shape == "tri":
            self.add(f'<path d="M{px:.1f},{py - size * 1.2:.1f} L{px + size:.1f},{py + size * 0.8:.1f} L{px - size:.1f},{py + size * 0.8:.1f}Z" class="{cls}"/>')

    def scalebar(self, km, label):
        x0, y0 = self.pad, self.h - self.pad + 2
        L = km / self.s
        self.add(f'<path d="M{x0},{y0 - 6} L{x0},{y0} L{x0 + L:.1f},{y0} L{x0 + L:.1f},{y0 - 6}" class="m-scale"/>')
        self.add(f'<text x="{x0 + L + 5:.1f}" y="{y0:.1f}" class="m-t">{E(label)}</text>')

    def svg(self, title):
        return (f'<svg viewBox="0 0 {self.w:.0f} {self.h + 8:.0f}" role="img" aria-label="{E(title)}">'
                f'<rect width="100%" height="100%" class="m-bg"/>' + "".join(self.out) + "</svg>")


def map_a():
    m = Map(-480_000, 60_000, -140_000, 300_000, 1_000)
    cx, cy = m.P(0, 0)
    m.add(f'<path d="M{cx - 260:.1f},{cy:.1f} a260,260 0 1,0 520,0 a260,260 0 1,0 -520,0 '
          f'M{cx - 120:.1f},{cy:.1f} a120,120 0 1,1 240,0 a120,120 0 1,1 -240,0Z" class="m-torus" fill-rule="evenodd"/>')
    m.text(-115_000, -125_000, "THE BREAKERS · 120,000–260,000 km", "m-t m-muted", "middle")
    m.circle(0, 0, 380_000, "m-orbit")
    m.circle(0, 0, 42_164, "m-orbit")
    m.circle(0, 0, 6_400, "m-planet", 4)
    m.text(0, 0, "Maren", "m-t", "middle", 0, 58)
    bw = bw_at(hours("T+1:10:00"))
    m.mark(*bw, "m-comp", "dia", 3)
    m.text(*bw, "Breakwater, over Site 1", "m-t m-compt", "middle", 0, -9)
    m.arrow(pol(12_000, SUN), pol(52_000, SUN))
    m.text(*pol(52_000, SUN), "sun", "m-t m-muted", "start", 4, 4)
    m.mark(*SKERRY, "m-moon", "dot", 4)
    m.text(*SKERRY, "Skerry: mass driver, laser, depot", "m-t", "start", 8, 4)
    m.line([EXIT, ANCHOR], "m-lref")
    m.mark(*EXIT, "m-lreff", "sq", 3.5)
    m.text(*EXIT, "Warp exit and shield park", "m-t m-lreft", "start", -3, 17)
    m.text(*EXIT, "Nauvoo, Excelsior, Tantive IV", "m-t m-muted", "start", -3, 29)
    for clock, lab, anchor in (("T+0:59:00", "T+0:59 · 20 km/s", "start"), ("T+3:20:00", "T+3:20 into the Breakers", "middle")):
        p = track(approach_r(hours(clock)))
        m.mark(*p, "m-lreff", "dot", 2.5)
        m.text(*p, lab, "m-t", anchor, -2 if anchor == "start" else 0, -9)
    m.mark(*ANCHOR, "m-rock", "dot", 3.5)
    m.text(*ANCHOR, "Anchor · T+5:09", "m-t m-lreft", "middle", 0, 16)
    m.curve(EXIT, (-420_000, 170_000), SKERRY, "m-missile")
    m.text(-470_000, 200_000, "wave one", "m-t m-lreft", "start")
    m.text(-470_000, 200_000, "T+0:18 → T+1:02", "m-t m-lreft", "start", 0, 12)
    m.line([SKERRY, (-430_000, 60_000), EXIT], "m-kin m-thin")
    m.text(-352_000, 70_000, "40 drones → the park", "m-t m-compt", "start")
    net = final_at(hours("T+6:40:00"))
    m.curve(SKERRY, (-170_000, 95_000), net, "m-kin")
    m.mark(*net, "m-kindot", "dot", 2)
    m.curve(SKERRY, (-230_000, 110_000), anchor_at(hours("T+7:07:00")), "m-kin m-thin")
    m.text(-150_000, 132_000, "Skerry's 18 rounds · thrown T+0:04–0:54", "m-t m-compt", "middle")
    m.text(-150_000, 132_000, "five nets on the lane T+6:40–7:20, one ring on Anchor", "m-t m-compt", "middle", 0, 12)
    m.scalebar(100_000, "100,000 km")
    return m.svg(D.MAPS["A"])


def map_b():
    m = Map(-290_000, -130_000, -40_000, 40_000, 250)
    cx, cy = m.P(0, 0)
    m.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{260_000 / 250:.1f}" class="m-edge"/>')
    rnd = random.Random(7)
    for _ in range(170):
        x, y = rnd.uniform(-290_000, -130_000), rnd.uniform(-40_000, 40_000)
        if math.hypot(x, y) < 260_000:
            m.mark(x, y, "m-rockdot", "dot", rnd.uniform(0.6, 1.5))
    m.text(-286_000, 36_000, "outer edge of the Breakers", "m-t m-muted", "start")
    m.text(-286_000, -36_000, "Large rocks shown are a sample: real spacing is hundreds of km.", "m-t m-muted")
    m.line([track(290_000), ANCHOR], "m-lref")
    ev = [("T+3:20:00", "T+3:20 enter", -10), ("T+3:30:00", "T+3:30 Site 1 dazzles", 16),
          ("T+3:40:00", "T+3:40 pods launch", -22), ("T+3:52:13", "T+3:52 Canterbury holed", 28),
          ("T+4:10:00", "T+4:10 drones wake", -10), ("T+4:25:00", "T+4:25 Normandy lost", 16),
          ("T+4:34:10", "T+4:34 turnover", -22)]
    for clock, lab, dy in ev:
        p = track(approach_r(hours(clock)))
        m.mark(*p, "m-lreff", "dot", 2.4)
        m.text(*p, lab, "m-t", "middle", 0, dy)
    r40 = approach_r(hours("T+3:40:00"))
    for dx, dy in ((2_500, 3_000), (4_000, -2_600), (6_000, 1_800)):
        p = track(r40 - dx)
        m.mark(p[0], p[1] + dy, "m-comp", "dia", 2.2)
    plat_r = approach_r(hours("T+3:52:00")) - 600
    plat = (track(plat_r)[0], track(plat_r)[1] - 1_600)
    m.mark(*plat, "m-comp", "x", 3)
    ast = track(plat_r + 8_600)
    m.mark(*ast, "m-lreff", "sq", 3)
    m.line([ast, plat], "m-spinal")
    m.text(*ast, "Astrid fires: 8,600 km, 108 s", "m-t m-lreft", "middle", 0, -38)
    ctl = track(approach_r(hours("T+4:14:00")))
    ctl = (ctl[0], ctl[1] - 9_000)
    m.mark(*ctl, "m-comp", "dia", 2.6)
    m.text(*ctl, "control craft, dazzled (T+4:14)", "m-t m-compt", "middle", 0, 16)
    m.mark(*ANCHOR, "m-rock", "dot", 4)
    m.text(*ANCHOR, "Anchor", "m-t m-lreft", "end", -7, -8)
    m.text(*ANCHOR, "T+5:09", "m-t m-lreft", "end", -7, 18)
    m.scalebar(10_000, "10,000 km")
    return m.svg(D.MAPS["B"])


def maren_shadow(length=120_000):
    """Maren's umbra in the ring plane: from the terminator back along the anti-sun axis, narrowing with distance."""
    back, side = SUN + 180, SUN + 90
    far = pol(length, back)
    w = R_MAREN - length * math.tan(SUN_R)
    return [pol(R_MAREN, side), pol(R_MAREN, side + 180), pol(w, side + 180, far), pol(w, side, far)]


def shadow_label(m, text, a, b):
    """Label a band along the segment a→b, whichever way reads left to right."""
    (x0, _), (x1, _) = m.P(*a), m.P(*b)
    m.text_along(*((a, b) if x1 >= x0 else (b, a)), text, "m-t m-muted", 0.05, 4)


def map_c():
    """Local frame around Anchor, km; Site 1 and Breakwater off to +x."""
    m = Map(-420, 420, -420, 330, 2)
    m.circle(0, 0, 300, "m-edge")
    m.text(0, 300, "rocks shelled inside 300 km (the Donnager); moonlets next", "m-t m-muted", "middle", 0, -6)
    x0, y0 = m.P(-420, 9)
    x1, y1 = m.P(-9, -9)
    m.add(f'<rect x="{x0:.1f}" y="{y0:.1f}" width="{x1 - x0:.1f}" height="{y1 - y0:.1f}" class="m-shadow"/>')
    back = SUN + 180
    m.poly([pol(9, SUN + 90), pol(9, SUN - 90), pol(9, SUN - 90, pol(430, back)), pol(9, SUN + 90, pol(430, back))], "m-shadow")
    shadow_label(m, "Site 1's shadow", (-400, -14), (-250, -14))
    shadow_label(m, "the sun's shadow", pol(250, back), pol(400, back))
    m.circle(0, 0, 9, "m-rock", 2.5)
    m.text(0, 0, "Anchor (18 km)", "m-t", "start", 7, 17)
    m.arrow((330, 0), (412, 0))
    m.text(412, 0, "to Site 1 · 143,600 km", "m-t m-muted", "end", 0, -32)
    m.text(412, 0, "to Breakwater · 108,000 km", "m-t m-muted", "end", 0, -20)
    m.arrow(pol(260, SUN), pol(360, SUN))
    m.text(*pol(360, SUN), "sun", "m-t m-muted", "end", -4, -4)
    m.mark(14, 8, "m-comp", "x", 3)
    m.text(14, 8, "mine, T+5:10", "m-t m-compt", "start", 6, 4)
    en = pol(15, 180 + SUN / 2)          # on the bisector of the two shadows, ~4 km inside each
    for p, lab, shape, anchor, dx, dy in ((en, "Endeavor", "sq", "end", -4, -9), ((-80, 5), "", "dot", "", 0, 0),
                                          ((-150, -4), "", "dot", "", 0, 0), ((-180, 4), "the pack", "dot", "middle", 0, -9),
                                          ((-210, -3), "", "dot", "", 0, 0), ((-290, 0), "Astrid", "sq", "middle", 0, -9)):
        m.mark(*p, "m-lreff", shape, 2.6 if shape == "sq" else 2.2)
        if lab:
            m.text(*p, lab, "m-t", anchor, dx, dy)
    m.mark(-150, 190, "m-lreff", "dot", 2.2)
    m.text(-150, 190, "Donnager, shelling outward", "m-t", "middle", 0, -8)
    for p in ((-60, 70), (60, -60), (-120, -250)):
        m.mark(*p, "m-lreff", "dot", 1.6)
    m.text(-120, -250, "corvettes and drones sweep", "m-t m-muted", "middle", 0, 14)
    moon, frig = pol(42, 220, en), pol(46, 220, en)
    m.circle(*moon, 3, "m-rockdot", 2.6)
    m.mark(*frig, "m-comp", "dia", 2.6)
    m.line([en, frig], "m-lance")
    for i, line in enumerate(("Compact frigate in a cleft", "on a moonlet, 45 km", "lanced at T+5:13:55")):
        m.text(*frig, line, "m-t m-compt", "end", -8, 4 + 12 * i)
    plat = pol(400, -45, en)
    m.mark(*plat, "m-comp", "x", 4)
    m.text(*plat, "railgun platform, 400 km", "m-t m-compt", "middle", 0, 18)
    m.text(*plat, "off the port quarter", "m-t m-compt", "middle", 0, 30)
    m.line([plat, en], "m-kin")
    m.text(185, -170, "T+5:13 salvo · 16 s", "m-t m-compt", "start", 10)
    m.line([(en[0] + 6, en[1] + 4), (plat[0] + 4, plat[1] + 6)], "m-lref", 'stroke-dasharray="1 3"')
    m.text(150, -185, "T+5:14 broadside", "m-t m-lreft", "end", -10)
    m.scalebar(100, "100 km")
    return m.svg(D.MAPS["C"])


def map_d():
    m = Map(-160_000, 50_000, -52_000, 46_000, 1_000 / 3)
    t52 = hours("T+7:52:00")
    m.halfplane(site1_at(t52), th_bw(t52), "m-sky")
    m.poly(maren_shadow(200_000), "m-shadow")
    shadow_label(m, "Maren's shadow", pol(78_000, SUN + 180), pol(95_000, SUN + 180))
    m.text(*pol(33_000, th_bw(t52) + 90), "Site 1's sky at T+7:52", "m-t m-compt", "middle")
    m.circle(0, 0, 42_164, "m-orbit")
    for k in range(1, 12):
        m.mark(*pol(42_164, th_bw(t52) + 30 * k), "m-comp", "dot", 1.6)
    m.text(48_000, 44_000, "inner ring: 11 stations", "m-t m-muted", "end")
    m.circle(0, 0, 6_400, "m-planet")
    m.mark(*site1_at(t52), "m-comp", "tri", 3)
    m.text(0, 0, "Maren", "m-t", "middle", 0, 34)
    b43, b52 = bw_at(T_DEP), bw_at(t52)
    m.mark(*b43, "m-comp", "dia", 3)
    m.text(*b43, "Breakwater, T+5:43", "m-t m-compt", "end", -6, -6)
    m.mark(*b52, "m-comp", "dia", 3.6)
    m.text(*b52, "Breakwater, T+7:52", "m-t m-compt", "start", 7, 14)
    for f in (pol(10_500, 6), pol(11_500, 16)):
        m.mark(*f, "m-comp", "dia", 2.2)
    m.text(*pol(11_000, 11), "2 Compact frigates", "m-t m-compt", "start", 9, 0)
    m.text(*pol(11_000, 11), "behind the limb", "m-t m-compt", "start", 9, 12)
    m.mark(*A_DEP, "m-rock", "dot", 3.5)
    m.text(*A_DEP, "Anchor: the pack stays, guarded", "m-t m-lreft", "start", 2, -9)
    ring = anchor_at(hours("T+7:07:00"))
    m.circle(*ring, 2_400, "m-kin m-thin")
    m.text(*ring, "Skerry's ring on Anchor, T+7:07", "m-t m-compt", "start", 2, 56)
    a07 = anchor_at(hours("T+7:07:00"))
    m.line([a07, b52], "m-missile")
    m.text_along(a07, b52, "waves away T+7:07 and 7:08, land T+7:52 and 7:53", "m-t m-lreft", 0.03, 13)
    m.line([A_DEP, STOP], "m-lref")
    ev = [("T+6:40:00", "T+6:40 Skerry's first net", "start", 4, -9), ("T+6:55:00", "T+6:55 Site 1 fires", "start", 4, -31),
          (fmt_clock(T_TURN * 3600), f"{fmt_clock(T_TURN * 3600)[:-3]} turnover", "middle", 0, -9)]
    for clock, lab, anchor, dx, dy in ev:
        p = final_at(hours(clock))
        m.mark(*p, "m-lreff", "dot", 2.4)
        m.text(*p, lab, "m-t", anchor, dx, dy)
    m.mark(*STOP, "m-lreff", "sq", 3)
    m.text(*STOP, f"stop, {fmt_clock(T_STOP * 3600)[:-3]}", "m-t m-lreft", "end", -7, 16)
    m.text(-157_000, 42_000, "Inertial frame: Maren turns 15°/h under Breakwater; Anchor drifts 2.2°/h.", "m-t m-muted")
    m.scalebar(20_000, "20,000 km")
    return m.svg(D.MAPS["D"])


def map_e():
    t_kill = hours("T+7:53:30")
    b = bw_at(t_kill)
    z = th_bw(t_kill)
    m = Map(b[0] - 27_000, b[0] + 19_000, b[1] - 15_000, b[1] + 17_000, 80)
    nad = z + 180
    m.poly(maren_shadow(200_000), "m-shadow")
    m.poly([b, pol(80_000, nad - MAREN_HALF, b), pol(80_000, nad + MAREN_HALF, b)], "m-wedge")
    m.text(*pol(12_000, nad + MAREN_HALF + 4, b), "towards Maren", "m-t m-muted", "end", -6, 0)
    m.text(*pol(12_000, nad + MAREN_HALF + 4, b), f"(its disc ±{MAREN_HALF:.1f}°)", "m-t m-muted", "end", -6, 12)
    m.circle(0, 0, 42_164, "m-orbit")
    m.line([b, pol(16_000, z, b)], "m-zenith")
    m.text(*pol(15_500, z, b), "Breakwater's zenith", "m-t m-compt", "start", 6, 4)
    b25 = bw_at(hours("T+7:25:00"))
    m.mark(*b25, "m-comp", "dia", 2.6)
    m.text(*b25, "Breakwater, T+7:25", "m-t m-compt", "middle", 0, -10)
    path = [final_at(hours(f"T+7:{mm:02d}:00")) for mm in range(10, 52)] + [STOP]
    m.line(path, "m-lref")
    f25, f31 = final_at(hours("T+7:25:00")), final_at(hours("T+7:31:00"))
    m.line([b25, f31], "m-kin")
    m.text_along(f31, b25, "64 missiles at the Extenuating", "m-t m-compt", 0.1, 13)
    for p, lab, dy in ((f25, "fleet, T+7:25", -9), (f31, "umbrella, T+7:31", 17)):
        m.mark(*p, "m-lreff", "dot", 2.4)
        m.text(*p, lab, "m-t", "middle", 0, dy)
    m.mark(*STOP, "m-lreff", "sq", 3)
    m.text(*STOP, f"escorts stop, {ESCORTS[0]:,} km", "m-t m-lreft", "end", -8, 14)
    ast, hit = AST_FIRE, HIT
    shot_dir = bearing(ast, hit)
    m.mark(*ast, "m-lreff", "sq", 3.6)
    m.text(*ast, f"Astrid, stopped {ASTRID[0]:,} km out", "m-t m-lreft", "end", -7, 14)
    m.line([ast, hit], "m-spinal")
    m.line([pol(8_000, shot_dir, hit), pol(60_000, shot_dir, hit)], "m-ghost")
    m.text(*pol(18_000, shot_dir, hit), f"a spinal miss passes {line_miss(ast, hit) - 6_400:,.0f} km above Maren",
           "m-t m-muted", "end", 0, -8)
    a_kill = anchor_at(hours("T+7:08:30"))
    come = bearing(b, a_kill)
    m.line([pol(40_000, come, b), b], "m-missile")
    m.line([pol(8_000, come + 180, b), pol(60_000, come + 180, b)], "m-ghost")
    m.text(*pol(26_000, come, b), f"waves from Anchor, {angdiff(come, z):.0f}° off the zenith", "m-t m-lreft", "start", 0, -8)
    miss = line_miss(anchor_at(hours("T+7:07:00")), bw_at(hours("T+7:52:00")))
    m.text(b[0] + 18_700, pol(18_000, come + 180, b)[1], f"misses pass {miss:,.0f} km from Maren",
           "m-t m-muted", "end", 0, 16)
    m.mark(*b, "m-comp", "dia", 4.2)
    m.text(*b, "Breakwater", "m-t m-compt", "middle", 0, -12)
    m.text(b[0] + 18_500, b[1] - 13_500, "At Breakwater: spend wave T+7:52:00; kill wave and Casaba jets",
           "m-t m-muted", "end", 0, -12)
    m.text(b[0] + 18_500, b[1] - 13_500, f"T+7:53:30; spinal fired T+7:54:40, impact {fmt_clock(T_HIT * 3600)}.", "m-t m-muted", "end")
    first, full = sunrise("Breakwater")
    m.text(b[0] + 18_500, b[1] - 13_500, f"Breakwater leaves Maren's shadow {fmt_clock(first)}–{fmt_clock(full)}.",
           "m-t m-muted", "end", 0, 12)
    m.scalebar(5_000, "5,000 km")
    return m.svg(D.MAPS["E"])


MAP_SVGS = {"A": map_a, "B": map_b, "C": map_c, "D": map_d, "E": map_e}


# ----------------------------------------------------------------- timeline
def timeline_svg():
    W, x0, x1 = 1000, 40, 960
    hrs = math.ceil(hours(D.SHOTS[-1]["clock"]) + 0.25)
    fx = lambda s: x0 + (x1 - x0) * s / RUNTIME
    mx = lambda h: x0 + (x1 - x0) * h / hrs
    out = [f'<svg viewBox="0 0 {W} 250" role="img" aria-label="Film time against mission time">']
    act_span = {}
    for s in D.SHOTS:
        a = act_span.setdefault(s["act"], [s["t0"], s["t1"]])
        a[1] = s["t1"]
    for num, name, _ in D.ACTS:
        a, b = act_span[num]
        out.append(f'<rect x="{fx(a):.1f}" y="18" width="{fx(b) - fx(a):.1f}" height="22" class="tl-act tl-act-{num}"/>')
        wide = fx(b) - fx(a) > 90         # a narrow act gets its number only
        out.append(f'<text x="{fx(a) + (6 if wide else 2):.1f}" y="33" class="tl-actt">{num}{" · " + E(name.upper()) if wide else ""}</text>')
    for s in D.SHOTS:
        out.append(f'<line x1="{fx(s["t0"]):.1f}" y1="42" x2="{mx(hours(s["clock"])):.1f}" y2="196" class="tl-link tl-l-{s["act"]}"/>')
        out.append(f'<line x1="{fx(s["t0"]):.1f}" y1="40" x2="{fx(s["t0"]):.1f}" y2="46" class="tl-tick"/>')
    for sec in range(0, RUNTIME + 1, 15):
        out.append(f'<text x="{fx(sec):.1f}" y="12" class="tl-t" text-anchor="middle">{sec // 60}:{sec % 60:02d}</text>')
    out.append(f'<line x1="{x0}" y1="198" x2="{x1}" y2="198" class="tl-axis"/>')
    for hr in range(0, hrs + 1):
        out.append(f'<line x1="{mx(hr):.1f}" y1="196" x2="{mx(hr):.1f}" y2="202" class="tl-axis"/>')
        out.append(f'<text x="{mx(hr):.1f}" y="216" class="tl-t" text-anchor="middle">T+{hr}h</text>')
    out.append(f'<text x="{x0}" y="240" class="tl-t tl-muted">Top: film time (min:s). Bottom: real mission time. Each line is one shot; '
               f'shallow lines play near real time, long slanted ones jump hours.</text>')
    out.append("</svg>")
    return "".join(out)


# ----------------------------------------------------------------- page
CSS = r"""
/* Layout: a pre-production board. Dark-first like the draft; wide sections for
   maps and the timeline, a two-column grid of shot cards with sketch or render. */
:root{
  --bg:#07090c; --panel:#0e1218; --panel2:#141a23; --ink:#e4e8ee; --muted:#8a95a6; --line:#1f2631;
  --lref:#a47bff; --comp:#ff7a59; --clock:#6fd3c4; --heat:#ff9a4a;
  --f-display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;
  --f-body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
  color-scheme:dark;
}
@media (prefers-color-scheme: light){ :root:not([data-theme="dark"]){
  --bg:#f3f4f7; --panel:#ffffff; --panel2:#f6f7fa; --ink:#12161d; --muted:#5a6475; --line:#d8dde5;
  --lref:#6232d4; --comp:#c2410c; --clock:#0e7c70; --heat:#c2510d; color-scheme:light; } }
:root[data-theme="light"]{
  --bg:#f3f4f7; --panel:#ffffff; --panel2:#f6f7fa; --ink:#12161d; --muted:#5a6475; --line:#d8dde5;
  --lref:#6232d4; --comp:#c2410c; --clock:#0e7c70; --heat:#c2510d; color-scheme:light; }
body{background:var(--bg); color:var(--ink); font:400 .95rem/1.55 var(--f-body);}
.wrap{max-width:1240px; margin:0 auto; padding-inline:max(16px,3vw);}
header.top{padding-block:2.2rem 1.2rem;}
.eyebrow{font:500 .75rem var(--f-mono); letter-spacing:.12em; text-transform:uppercase; color:var(--muted);}
h1{font:700 clamp(2.4rem,6vw,3.8rem)/1 var(--f-display); margin:.4rem 0 .8rem; letter-spacing:.01em;}
.lead{max-width:70ch; margin:0 0 1rem; font-size:1.02rem;}
.facts{display:flex; flex-wrap:wrap; gap:.4rem 1.2rem; font:400 .8rem var(--f-mono); color:var(--muted); margin:0; padding:0; list-style:none;}
.facts b{color:var(--ink); font-weight:500;}
.note{max-width:78ch; font-size:.82rem; color:var(--muted); margin:.8rem 0 0;}
nav.toc{position:sticky; top:env(safe-area-inset-top,0px); z-index:5; background:var(--bg); border-block:1px solid var(--line);}
nav.toc .wrap{display:flex; gap:.2rem; overflow-x:auto; scrollbar-width:none;}
nav.toc a{font:600 .85rem var(--f-display); letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-decoration:none; padding:.75rem .7rem; white-space:nowrap;}
nav.toc a:hover{color:var(--ink);}
section{padding-block:2.4rem .6rem;}
h2{font:700 1.9rem/1.1 var(--f-display); margin:0 0 1rem; text-wrap:balance;}
h3{font:600 1.25rem/1.2 var(--f-display); margin:0 0 .5rem;}
.grid2{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem;}
.card{background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:1rem 1.1rem; min-width:0;}
.side-lref{border-top:3px solid var(--lref);} .side-comp{border-top:3px solid var(--comp);}
.side-lref h3{color:var(--lref);} .side-comp h3{color:var(--comp);}
dl.kv{display:grid; grid-template-columns:minmax(8rem,34%) minmax(0,1fr); gap:.45rem .9rem; margin:.4rem 0 0; font-size:.88rem;}
dl.kv dt{font:500 .78rem var(--f-mono); color:var(--muted);}
dl.kv dd{margin:0;}
ul.rules{margin:.3rem 0 0; padding-left:1.1rem; font-size:.88rem;}
ul.rules li{margin:.3rem 0;}
.tbl{overflow-x:auto; border:1px solid var(--line); border-radius:8px; background:var(--panel); margin:1rem 0;}
.card .tbl{margin:.6rem 0 0;}
table{border-collapse:collapse; width:100%; font-size:.86rem; font-variant-numeric:tabular-nums;}
th{font:600 .74rem var(--f-display); letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:.55rem .7rem; border-bottom:1px solid var(--line);}
td{padding:.5rem .7rem; border-top:1px solid var(--line); vertical-align:top;}
tr:first-child td{border-top:0;}
td.mono, .mono{font-family:var(--f-mono); font-size:.8rem;}
td.mono{white-space:nowrap;}
.span2{grid-column:1/-1;}
#reviews h3{margin-top:1.4rem;}
.figure{background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:.8rem; margin:0; min-width:0;}
.figure svg{display:block; width:100%; height:auto;}
.figure figcaption{font-size:.8rem; color:var(--muted); margin-top:.5rem;}
.scrollx{overflow-x:auto;} .scrollx svg{min-width:760px;}
.maps{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem;}
.legend{display:flex; flex-wrap:wrap; gap:.3rem 1.2rem; font:400 .78rem var(--f-mono); color:var(--muted); margin:0 0 .8rem;}
.legend i{display:inline-block; width:22px; height:0; vertical-align:middle; margin-right:.4rem; border-top:2px solid;}
.legend .sw{display:inline-block; width:14px; height:10px; vertical-align:middle; margin-right:.4rem;}
.lg-lref{border-color:var(--lref);} .lg-comp{border-color:var(--comp);} .lg-mis{border-top-style:dotted!important; border-color:var(--lref);} .lg-kin{border-top-style:dashed!important; border-color:var(--comp);}
.lg-spinal{border-top-style:dashed!important; border-color:var(--lref); border-top-width:1px!important;}
.lg-sky{background:color-mix(in srgb, var(--comp) 22%, transparent);} .lg-shadow{background:color-mix(in srgb, var(--lref) 30%, transparent);}
/* map drawing */
.m-bg{fill:var(--panel2);}
.m-t{font:400 9.5px var(--f-mono); fill:var(--ink);}
.m-muted{fill:var(--muted);} .m-lreft{fill:var(--lref);} .m-compt{fill:var(--comp);}
.m-torus{fill:var(--muted); fill-opacity:.13;}
.m-orbit{fill:none; stroke:var(--muted); stroke-width:.7; stroke-dasharray:3 4; stroke-opacity:.7;}
.m-edge{fill:none; stroke:var(--muted); stroke-width:.8; stroke-dasharray:4 4;}
.m-planet{fill:var(--clock); fill-opacity:.55; stroke:var(--clock); stroke-width:.8;}
.m-moon{fill:var(--muted);}
.m-rock{fill:var(--ink); fill-opacity:.8;} .m-rockdot{fill:var(--muted); fill-opacity:.55;}
.m-lref{fill:none; stroke:var(--lref); stroke-width:1.6;}
.m-lreff{fill:var(--lref);}
.m-comp{fill:var(--comp); stroke:var(--comp); stroke-width:1.2;}
.m-missile{fill:none; stroke:var(--lref); stroke-width:1.1; stroke-dasharray:1 3; stroke-linecap:round;}
.m-kin{fill:none; stroke:var(--comp); stroke-width:1.1; stroke-dasharray:5 3;}
.m-thin{stroke-width:.7; stroke-dasharray:2 3;}
.m-kindot{fill:var(--comp); fill-opacity:.8;}
.m-spinal{fill:none; stroke:var(--lref); stroke-width:1.2; stroke-dasharray:6 2 1 2;}
.m-lance{fill:none; stroke:var(--lref); stroke-width:2.2; stroke-linecap:round;}
.m-ghost{fill:none; stroke:var(--muted); stroke-width:.8; stroke-dasharray:2 3;}
.m-zenith{fill:none; stroke:var(--comp); stroke-width:.8; stroke-dasharray:4 3; stroke-opacity:.8;}
.m-arrow{fill:none; stroke:var(--muted); stroke-width:1;}
.m-arrowhead{fill:var(--muted);}
.m-shadow{fill:var(--lref); fill-opacity:.25;}
.m-sky{fill:var(--comp); fill-opacity:.08;}
.m-wedge{fill:var(--clock); fill-opacity:.14;}
.m-scale{fill:none; stroke:var(--ink); stroke-width:1;}
/* timeline */
.tl-act{fill-opacity:.9;} .tl-act-P,.tl-act-E{fill:var(--muted); fill-opacity:.25;} .tl-act-I{fill:var(--lref); fill-opacity:.35;} .tl-act-II{fill:var(--clock); fill-opacity:.3;} .tl-act-III{fill:var(--heat); fill-opacity:.3;} .tl-act-IV{fill:var(--comp); fill-opacity:.3;}
.tl-actt{font:600 12px var(--f-display); letter-spacing:.06em; fill:var(--ink);}
.tl-t{font:400 10px var(--f-mono); fill:var(--ink);} .tl-muted{fill:var(--muted);}
.tl-tick, .tl-axis{stroke:var(--muted); stroke-width:1;}
.tl-link{stroke-width:1; stroke-opacity:.6;} .tl-l-P,.tl-l-E{stroke:var(--muted);} .tl-l-I{stroke:var(--lref);} .tl-l-II{stroke:var(--clock);} .tl-l-III{stroke:var(--heat);} .tl-l-IV{stroke:var(--comp);}
/* shots */
.act{margin:2.2rem 0 1rem; display:grid; grid-template-columns:auto minmax(0,1fr); gap:.2rem 1rem; align-items:baseline;}
.act .num{font:700 2.2rem/1 var(--f-display); color:var(--muted);}
.act h3{font-size:1.6rem; margin:0;}
.act p{grid-column:2; margin:0; color:var(--muted); font-size:.9rem;}
.act .span{grid-column:2; font:400 .78rem var(--f-mono); color:var(--muted);}
.shots{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem;}
.shot{background:var(--panel); border:1px solid var(--line); border-radius:8px; overflow:hidden; min-width:0; display:flex; flex-direction:column;}
.media{position:relative; aspect-ratio:2.39/1; background:#020304;}
.media img, .media .sketch, .media .sketch svg{position:absolute; inset:0; width:100%; height:100%; object-fit:cover; display:block;}
.badge{position:absolute; top:.45rem; font:500 .72rem var(--f-mono); color:#e9edf2; background:rgba(0,0,0,.55); padding:.12rem .45rem; border-radius:4px;}
.badge.n{left:.45rem; font-weight:600;} .badge.t{right:.45rem;}
.badge.r{top:auto; bottom:.45rem; right:.45rem; color:#ffd48a; border:1px solid rgba(255,212,138,.5);}
.body{padding:.85rem 1rem 1rem; display:grid; gap:.55rem;}
.body h4{font:600 1.25rem/1.15 var(--f-display); margin:0;}
.meta{font:400 .76rem var(--f-mono); color:var(--muted); display:flex; flex-wrap:wrap; gap:.15rem .9rem;}
.clock{color:var(--clock);}
.action{margin:0; font-size:.9rem;}
.comm{margin:0; padding:.5rem .7rem; border-left:2px solid var(--clock); background:var(--panel2); display:grid; gap:.25rem; font-size:.86rem;}
.comm b{font:600 .72rem var(--f-mono); letter-spacing:.04em; color:var(--clock); margin-right:.4rem;}
.comm .cue{font:400 .68rem var(--f-mono); color:var(--muted); margin-left:.5rem; white-space:nowrap;}
.rows{display:grid; grid-template-columns:4.6rem minmax(0,1fr); gap:.3rem .7rem; margin:0; font-size:.82rem;}
.rows dt{font:500 .7rem/1.7 var(--f-mono); letter-spacing:.06em; text-transform:uppercase; color:var(--muted);}
.rows dd{margin:0; min-width:0;}
.chip{display:inline-block; font:500 .72rem/1.5 var(--f-mono); padding:0 .4rem; border-radius:4px; border:1px solid var(--line); margin:0 .25rem .2rem 0; color:var(--ink); text-decoration:none; white-space:nowrap;}
a.chip.r-lref, a.chip.r-maren{font:600 .74rem/1.5 var(--f-body); letter-spacing:.02em;}
a.chip.r-lref{border-color:color-mix(in srgb, var(--lref) 55%, transparent); color:var(--lref);}
a.chip.r-maren{border-color:color-mix(in srgb, var(--comp) 55%, transparent); color:var(--comp);}
.chip.new{border-style:dashed;} .chip.concept{border-color:var(--heat); color:var(--heat); border-style:dashed;}
code{font:400 .76rem var(--f-mono); background:var(--panel2); padding:.05rem .3rem; border-radius:3px; margin:0 .2rem .2rem 0; display:inline-block;}
a{color:var(--lref);}
td.lens{font:600 .8rem var(--f-display); letter-spacing:.06em; text-transform:uppercase; color:var(--muted); white-space:nowrap;}
footer{border-top:1px solid var(--line); margin-top:3rem; padding-block:1.4rem 2.6rem; color:var(--muted); font-size:.82rem;}
a:focus-visible{outline:2px solid var(--lref); outline-offset:2px;}
@media (max-width: 900px){ .grid2, .maps, .shots{grid-template-columns:minmax(0,1fr);} }
@media (max-width: 520px){ .rows{grid-template-columns:minmax(0,1fr);} .rows dt{margin-top:.2rem;} dl.kv{grid-template-columns:minmax(0,1fr);} }
"""


def rich(text):
    """Escape text and turn `code` spans into <code>."""
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", E(text))


def rule_chips(rules):
    out = []
    for r in rules:
        doc = rule_doc(r)
        out.append(f'<a class="chip r-{doc}" href="{DOC_BASE}#{rule_anchor(r)}" target="_blank" rel="noopener">{r}</a>')
    return "".join(out)


def asset_chips(ids):
    out = []
    for a in ids:
        name, status, concept, _ = D.ASSETS[a]
        cls = "chip" + (" concept" if concept else (" new" if status != "built" else ""))
        tip = f"{name} · {status}{' · concept sheet first' if concept else ''}"
        out.append(f'<span class="{cls}" title="{E(tip)}">{a}</span>')
    return "".join(out)


def shot_card(s):
    if s["render"]:
        media = f'<img src="{s["render"]}" alt="{E(s["title"])}: current Blender render used as reference" loading="lazy"><span class="badge r">render</span>'
    else:
        media = f'<div class="sketch" data-shot="{s["n"]}" role="img" aria-label="Sketch: {E(s["title"])}"></div>'
    comm = ""
    if s["comm"]:
        comm = '<div class="comm">' + "".join(
            f"<div><b>{E(sp)}</b>{E(line)}" + (f'<span class="cue">at {cue:g} s</span>' if cue is not None else "") + "</div>"
            for (sp, line), cue in zip(s["comm"], s["cues"])) + "</div>"
    rig = "".join(f"<code>{E(r)}</code>" for r in s["rig"]) or '<span class="mono">none</span>'
    extra = ""
    if s["hud"]:
        extra += "<dt>On screen</dt><dd>" + "".join(f'<code>{E(h)}</code>' for h in s["hud"]) + "</dd>"
    states = [f"{a}: {state_of(a, s['clock'])}" for a in D.STATES if a in s["assets"]]
    if states:
        extra += f"<dt>State</dt><dd>{E('; '.join(states))}</dd>"
    if light_note(s):
        extra += f"<dt>Light</dt><dd>{E(light_note(s))}</dd>"
    world = "" if s["body"] == "hud" else f"<span>World: {E(D.ENVS[world_of(s)])}</span>"
    return f"""<article class="shot" id="shot-{s['n']}">
<div class="media">{media}<span class="badge n">{s['n']}</span><span class="badge t">{mmss(s['t0'])}–{mmss(s['t1'])} · {s['dur']} s</span></div>
<div class="body"><h4>{E(s['title'])}</h4>
<div class="meta"><span>{E(s['cam'])}</span><span>{BODY_LABEL[s['body']]}</span><span>frames {s['f0']}–{s['f1']}</span></div>
<div class="meta"><span class="clock">{E("no clock" if clockless(s) else s['clock'])}</span><span>{E(s['real'])}</span><span>map {s['map']}</span><span>render class {s['cost']}</span>{world}</div>
<p class="action">{E(s['action'])}</p>{comm}
<dl class="rows">{f"<dt>Doctrine</dt><dd>{rule_chips(s['rules'])}</dd>" if s['rules'] else ""}{extra}<dt>VFX</dt><dd>{E(s['vfx'])}</dd>
<dt>Rig</dt><dd>{rig}</dd><dt>Assets</dt><dd>{asset_chips(s['assets'])}</dd><dt>Sound</dt><dd>{E(s['sound'])}</dd></dl>
</div></article>"""


def bench_key(s, keys):
    """The most specific key for a shot among `keys`: its title, its class in its World preset ('A@C'), its class."""
    for k in (s["title"], f"{s['cost']}@{world_of(s)}", s["cost"]):
        if k in keys:
            return k
    return None


def spf(s):
    """Seconds per frame for a shot: the most specific measured entry, else its class's estimate."""
    k = bench_key(s, D.MEASURED)
    return D.MEASURED[k] if k else ESTIMATE[s["cost"]]


def render_budget():
    rows, total = [], 0
    for c, (name, note) in D.RENDER_CLASSES.items():
        shots = [s for s in D.SHOTS if s["cost"] == c]
        fr = sum(s["dur"] for s in shots) * FPS
        hrs = sum(s["dur"] * FPS * spf(s) for s in shots) / 3600
        total += hrs
        if any(bench_key(s, D.MEASURED) for s in shots):
            note = f"{note}, partly measured"
        rows.append((c, name, note, [s["n"] for s in shots], fr, hrs))
    return rows, total


def worksheet():
    """One row per benchmark entry, with the shots it stands for: the gate as arithmetic anyone can do."""
    keys = [k for k, _ in D.BENCHMARKS]
    rows = []
    for k, what in D.BENCHMARKS:
        shots = [s for s in D.SHOTS if bench_key(s, keys) == k]
        fr = sum(s["dur"] for s in shots) * FPS
        est = ESTIMATE[shots[0]["cost"]] if shots else 0
        rows.append((k, resolve(what), [s["n"] for s in shots], fr, est, D.MEASURED.get(k)))
    rest = [s for s in D.SHOTS if bench_key(s, keys) is None]
    return rows, rest


def gate_text():
    """Where the budget stands against the gate, and each class's break-even cost."""
    rows, total = render_budget()
    cap = D.GATE_HOURS / (1 + MARGIN)
    even = [(c, (cap - (total - h)) * 3600 / fr) for c, _, _, _, fr, h in sorted(rows, key=lambda r: -r[5]) if h >= 5]
    state = "measured" if D.MEASURED else "estimated"
    return (f"The gate: {total * (1 + MARGIN):,.0f} h with the allowance ({state}), against {D.GATE_HOURS} h, so "
            f"{D.GATE_HOURS - total * (1 + MARGIN):,.0f} h to spare. Break-even for one class on its own, the others as they stand: "
            + ", ".join(f"{c} {x:,.0f} s/frame ({'measured' if c in D.MEASURED else 'estimate'} {SEC_PER_FRAME[c]:g})" for c, x in even) + ".")


def sets_text():
    return f"{len(SETS)} set-ups cover the film: " + "; ".join(f"{name} ({ranges(nums)})" for name, nums in SETS) + "."


def batches_text():
    out = []
    for k, env in D.ENVS.items():
        nums = [s["n"] for s in D.SHOTS if world_of(s) == k and s["body"] != "hud"]
        out.append(f"{env}: {ranges(nums)}")
    return "Render in batches by World preset: " + "; ".join(out) + "."


def build_html():
    acts_html = []
    for num, name, summary in D.ACTS:
        shots = [s for s in D.SHOTS if s["act"] == num]
        span = f"film {mmss(shots[0]['t0'])}–{mmss(shots[-1]['t1'])} · mission {shots[0]['clock']} → {shots[-1]['clock']}"
        acts_html.append(f'<div class="act"><span class="num">{num}</span><h3>{E(name)}</h3><p>{E(summary)}</p><span class="span">{span}</span></div>'
                         '<div class="shots">' + "".join(shot_card(s) for s in shots) + "</div>")
    fleet = "".join(f"<dt>{E(n)}</dt><dd><b>{E(c)}.</b> {E(r)}</dd>" for n, c, r in D.FLEET)
    defs = "".join(f"<dt>{E(n)}</dt><dd><b>{E(c)}.</b> {E(r)}</dd>" for n, c, r in D.DEFENDERS)
    phases = "".join(f'<tr><td class="mono">{a}–{b}</td><td>{E(n)}</td><td>{E(d)}</td></tr>' for a, b, n, d in D.PHASES)
    keyn = "".join(f"<tr><td>{E(a)}</td><td>{E(b)}</td><td class=\"mono\">{E(c)}</td></tr>" for a, b, c in D.KEY_NUMBERS)
    lis = lambda items: "<ul class=\"rules\">" + "".join(f"<li>{E(x)}</li>" for x in items) + "</ul>"
    cap = lambda x: x[:1].upper() + x[1:]
    bodies = "".join(f"<dt>{E(BODY_LABEL[k])}</dt><dd>{E(cap(v.split(': ', 1)[1]))}</dd>" for k, v in D.CAMERA_BODIES.items())
    maps = "".join(f'<figure class="figure" id="map-{k}">{MAP_SVGS[k]()}<figcaption><b>Map {k}.</b> {E(v)}. To scale, except the ship and site symbols.</figcaption></figure>'
                   for k, v in D.MAPS.items())
    budget, total = render_budget()
    brow = "".join(f'<tr><td class="mono">{c}</td><td>{E(n)}</td><td>{E(note)}</td><td class="mono">{len(ns)}</td><td class="mono">{fr:,}</td><td class="mono">{h:,.0f} h</td></tr>'
                   for c, n, note, ns, fr, h in budget)
    closest = "".join(f'<tr><td class="mono">{a}</td><td>{E(D.ASSETS[a][0])}</td><td class="mono"><a href="#shot-{n}">{n}</a></td><td>{E(what)}</td><td>{E(size)}</td></tr>'
                      for a, (n, what, size) in CLOSEST.items())
    plan = "".join(f"<dt>{E(k)}</dt><dd>{rich(v)}</dd>" for k, v in [("Sets", sets_text()), ("Batches", batches_text())] + list(D.PRODUCTION_PLAN))
    new_assets = [a for a, v in D.ASSETS.items() if v[1] != "built"]
    concept = [a for a, v in D.ASSETS.items() if v[2]]
    reviews = "".join(
        (f'<h3>{E(rnd)} · on {E(on.lower())}</h3><div class="tbl"><table><thead><tr><th>Lens</th><th>Major issue</th><th>How it was answered</th></tr></thead><tbody>'
         + "".join(f'<tr><td class="lens">{E(lens)}</td><td>{E(issue)}</td><td>{E(fix)}</td></tr>' for lens, issue, fix in rows)
         + "</tbody></table></div>") if rows else
        f'<h3>{E(rnd)} · on {E(on.lower())}</h3><p class="action">No reviewer raised a major issue.</p>'
        for rnd, on, rows in D.REVIEWS)
    sk = ",\n".join(f"{s['n']}: function () {{ SHIELDS = {'true' if s['shields'] else 'false'}; return {s['sketch']}; }}"
                    for s in D.SHOTS if s["sketch"])
    lib = (SB / "sketchlib.js").read_text()
    head = f"""<title>Operation Tidebreak</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap">
<style>{CSS}</style>
"""
    body = f"""<header class="top wrap">
<div class="eyebrow">WPAtaMS fan animation · pre-production board · {E(D.REVISION)}</div>
<h1>Operation Tidebreak</h1>
<p class="lead">An LREF task group led by L.R.E.F.S. Astrid and L.R.E.F.S. Endeavor breaks the orbital defence of Maren, a world held by the Maren Compact. The mission runs from T+0:00 to {MISSION_END} of real time; the film tells it in {RUNTIME // 60}:{RUNTIME % 60:02d}, with the mission clock marking every jump. Built on the approved doctrines.</p>
<ul class="facts"><li>Runtime <b>{RUNTIME // 60}:{RUNTIME % 60:02d}</b></li><li>Frames <b>{FRAMES:,}</b> @ 24 fps</li><li>Shots <b>{len(D.SHOTS)}</b></li><li>Mission <b>T+0:00 → {MISSION_END}</b></li><li>Format <b>{E(D.FORMAT)}</b></li></ul>
<p class="note">Sketches are layout drawings; frames marked <em>render</em> are current Blender renders of the Endeavor used as look reference. Doctrine chips open the rule in the doctrine reading edition. Comm lines are GUN side only, as subtitles for now.</p>
</header>
<nav class="toc" aria-label="Sections"><div class="wrap"><a href="#overview">Overview</a><a href="#film">Film rules</a><a href="#timeline">Timeline</a><a href="#maps">Maps</a><a href="#shots">Shots</a><a href="#production">Production</a><a href="#reviews">Reviews</a><a href="{DOC_BASE}" target="_blank" rel="noopener">Doctrine ↗</a></div></nav>
<main class="wrap">
<section id="overview"><h2>Forces and plan</h2>
<div class="grid2"><div class="card side-lref"><h3>LREF task group</h3><dl class="kv">{fleet}</dl></div>
<div class="card side-comp"><h3>The Maren Compact</h3><dl class="kv">{defs}</dl></div></div>
<div class="tbl"><table><thead><tr><th>Mission time</th><th>Phase</th><th>What happens</th></tr></thead><tbody>{phases}</tbody></table></div>
<div class="tbl"><table><thead><tr><th>Key number</th><th>Value</th><th>Source</th></tr></thead><tbody>{keyn}</tbody></table></div>
</section>
<section id="film"><h2>Film rules</h2>
<div class="grid2"><div class="card"><h3>Lighting</h3>{lis(D.LIGHTING + [resolve(eclipse_text())])}</div>
<div class="card"><h3>Mission clock and HUD</h3>{lis(D.CLOCK_HUD)}</div>
<div class="card"><h3>Screen direction</h3>{lis(D.SCREEN_DIRECTION)}</div>
<div class="card"><h3>Camera bodies and sound</h3><dl class="kv">{bodies}</dl></div></div>
</section>
<section id="timeline"><h2>Film time and mission time</h2><figure class="figure"><div class="scrollx">{timeline_svg()}</div></figure></section>
<section id="maps"><h2>Tactical maps</h2>
<div class="legend"><span><i class="lg-lref"></i>LREF</span><span><i class="lg-comp"></i>Maren Compact</span><span><i class="lg-mis"></i>missile track</span><span><i class="lg-kin"></i>kinetic rounds</span><span><i class="lg-spinal"></i>spinal shot</span><span><span class="sw lg-sky"></span>Site 1's sky</span><span><span class="sw lg-shadow"></span>shadow</span></div>
<div class="maps">{maps}</div></section>
<section id="shots"><h2>Shot list</h2>{"".join(acts_html)}</section>
<section id="production"><h2>Production</h2>
<div class="grid2"><div class="card"><h3>Render budget</h3><p class="action">{E(D.RENDER_NOTE)} The ceiling is a week (168 h) per full pass.</p>
<p class="action">{E(gate_text())}</p>
<div class="tbl"><table><thead><tr><th>Class</th><th>Kind</th><th>Cost</th><th>Shots</th><th>Frames</th><th>Time</th></tr></thead><tbody>{brow}
<tr><td></td><td><b>Total</b></td><td></td><td class="mono">{len(D.SHOTS)}</td><td class="mono">{FRAMES:,}</td><td class="mono"><b>{total:,.0f} h</b></td></tr>
<tr><td></td><td>With {MARGIN:.0%} for re-renders</td><td></td><td></td><td></td><td class="mono"><b>{total * (1 + MARGIN):,.0f} h</b></td></tr></tbody></table></div></div>
<div class="card"><h3>Plan</h3><dl class="kv">{plan}</dl></div>
<div class="card span2"><h3>Assets</h3><p class="action">{len(new_assets)} of {len(D.ASSETS)} assets are new or need additions; {len(concept)} of them go through concept sheets first (per the user's rule for new designs): {", ".join(concept)}. The full list, with the shots that need each one, is in <code>ASSET_REQUESTS.md</code>.</p>
<p class="action">Legend: <span class="chip">built</span><span class="chip new">new or extended</span><span class="chip concept">concept first</span></p></div>
<div class="card span2"><h3>Closest view of each main asset</h3><p class="action">Detail is built for the closest view; anything smaller than a few dozen pixels can be a proxy (Q13).</p>
<div class="tbl"><table><thead><tr><th>ID</th><th>Asset</th><th>Shot</th><th>View</th><th>On screen</th></tr></thead><tbody>{closest}</tbody></table></div></div></div>
</section>
<section id="reviews"><h2>Reviews</h2><p class="action">Five reviewers read each revision: physics, military doctrine, lore, cinematography and production. Every major issue is answered in the next revision; the reports and syntheses are in <code>review/</code>. {E(D.REVIEW_STATUS)}</p>{reviews}</section>
</main>
<footer class="wrap">Generated by <code>storyboard/build_storyboard.py</code> from <code>storyboard/tidebreak_data.py</code>. Names are the user's; ship classes and weapon families follow JCB's lore posts.</footer>
<svg width="0" height="0" style="position:absolute"><defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10z" class="m-arrowhead"/></marker></defs></svg>
<script>
(function () {{
  "use strict";
{lib}
  var SK = {{
{sk}
  }};
  Array.prototype.forEach.call(document.querySelectorAll('.sketch[data-shot]'), function (el) {{
    var f = SK[el.getAttribute('data-shot')];
    if (f) {{ try {{ el.innerHTML = f(); }} catch (e) {{ el.textContent = ''; }} }}
  }});
}})();
</script>
"""
    return head, body


# ----------------------------------------------------------------- text outputs
def write_csv():
    with open(SB / "shots.csv", "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["shot", "act", "title", "film_start_s", "film_end_s", "frame_start", "frame_end", "duration_s",
                    "mission_clock", "time_treatment", "camera", "camera_body", "world", "viewer_sees", "action", "comms",
                    "on_screen", "doctrine", "state", "light", "vfx", "rig", "assets", "sound", "render_class", "map",
                    "reference_frame"])
        for s in D.SHOTS:
            w.writerow([s["n"], s["act"], s["title"], s["t0"], s["t1"], s["f0"], s["f1"], s["dur"], s["clock"],
                        s["real"], s["cam"], s["body"], "" if s["body"] == "hud" else D.ENVS[world_of(s)], s["see"],
                        s["action"], " | ".join(comm_text(s)), " | ".join(s["hud"]), " ".join(s["rules"]),
                        "; ".join(f"{a}: {state_of(a, s['clock'])}" for a in D.STATES if a in s["assets"]), light_note(s),
                        s["vfx"], "; ".join(s["rig"]), " ".join(s["assets"]), s["sound"],
                        s["cost"], s["map"], s["render"] or ""])


def write_md():
    L = [f"# {D.TITLE}: shot list", "",
         f"{D.REVISION}. Runtime {RUNTIME // 60}:{RUNTIME % 60:02d} ({FRAMES:,} frames at {FPS} fps), {len(D.SHOTS)} shots, "
         f"mission span T+0:00 → {MISSION_END}, {D.FORMAT}. Generated from `storyboard/tidebreak_data.py`; "
         "the page with maps and sketches is `storyboard/index.html`.", "",
         "Rule IDs refer to `doctrine/LREF_doctrine.md` (O, D, A) and `doctrine/Defence_doctrine.md` (HO, HD, H). "
         "Asset IDs refer to `ASSET_REQUESTS.md`. Render classes: " +
         "; ".join(f"**{k}** {v[0]} ({v[1]})" for k, v in D.RENDER_CLASSES.items()) + ".", "",
         "## Mission phases", "", "| Mission time | Phase | What happens |", "|---|---|---|"]
    L += [f"| {a}–{b} | {n} | {d} |" for a, b, n, d in D.PHASES]
    L += ["", "## Film rules", "", "**Lighting**", ""] + [f"- {x}" for x in D.LIGHTING + [resolve(eclipse_text())]]
    L += ["", "**Mission clock and HUD**", ""] + [f"- {x}" for x in D.CLOCK_HUD]
    L += ["", "**Screen direction**", ""] + [f"- {x}" for x in D.SCREEN_DIRECTION]
    L += ["", "**Camera bodies**", ""] + [f"- {v}" for v in D.CAMERA_BODIES.values()]
    L += ["", "## Overview", "", "| # | Film | Frames | Mission clock | Time | Title | Camera | Doctrine |", "|---|---|---|---|---|---|---|---|"]
    L += [f"| {s['n']} | {mmss(s['t0'])}–{mmss(s['t1'])} | {s['f0']}–{s['f1']} | {s['clock']} | {s['real']} | {s['title']} | {s['cam']} ({BODY_LABEL[s['body']]}) | {' '.join(s['rules'])} |" for s in D.SHOTS]
    for num, name, summary in D.ACTS:
        L += ["", f"## Act {num}: {name}", "", summary]
        for s in [x for x in D.SHOTS if x["act"] == num]:
            L += ["", f"### {s['n']}. {s['title']}", "",
                  f"- **Film:** {mmss(s['t0'])}–{mmss(s['t1'])} ({s['dur']} s), frames {s['f0']}–{s['f1']}",
                  f"- **Mission:** {s['clock']} · {s['real']}",
                  f"- **Camera:** {s['cam']} ({BODY_LABEL[s['body']]})",
                  f"- **Viewer sees:** {s['see']}",
                  f"- **Action:** {s['action']}"]
            if s["comm"]:
                L.append("- **Comms:** " + " / ".join(comm_text(s, quote=True)))
            if s["hud"]:
                L.append("- **On screen:** " + " · ".join(f"`{h}`" for h in s["hud"]))
            states = [f"{a}: {state_of(a, s['clock'])}" for a in D.STATES if a in s["assets"]]
            if states:
                L.append("- **State:** " + "; ".join(states))
            if light_note(s):
                L.append(f"- **Light:** {light_note(s)}")
            if s["body"] != "hud":
                L.append(f"- **World:** {D.ENVS[world_of(s)]}")
            L += [f"- **Doctrine:** {', '.join(s['rules'])}",
                  f"- **VFX:** {s['vfx']}",
                  f"- **Rig:** {'; '.join(s['rig']) if s['rig'] else 'none'}",
                  "- **Assets:** " + ", ".join(f"{a} ({D.ASSETS[a][1]})" for a in s["assets"]),
                  f"- **Sound:** {s['sound']}",
                  f"- **Render class:** {s['cost']} · **Map:** {s['map']}" + (f" · **Reference frame:** `{s['render']}`" if s["render"] else "")]
    (SB / "shots.md").write_text("\n".join(L) + "\n")


def comm_text(s, quote=False):
    """The shot's lines as 'SPEAKER: line', with their cue when they have one."""
    q = (lambda x: f"“{x}”") if quote else (lambda x: x)
    return [f"{sp}: {q(line)}" + (f" (at {cue:g} s)" if cue is not None else "") for (sp, line), cue in zip(s["comm"], s["cues"])]


def audience_clock(s):
    """The mission clock as a viewer sees it over a shot."""
    if clockless(s):
        return "no clock yet" if s["act"] == "P" else "no clock"
    t0, t1 = clock_s(s["clock"]), shot_end(s)
    if t1 is None or (t1 - t0) / s["dur"] < 1.5:
        return fmt_clock(t0)
    return f"{fmt_clock(t0)} → {fmt_clock(t1)} (the clock runs fast)"


def write_audience():
    """What a viewer gets and nothing else: the picture, the words on screen, the lines, the sound, the clock.
    It is the only file the cold-read test sees."""
    L = [f"# {D.TITLE}: the film as a viewer gets it", "",
         f"{RUNTIME // 60}:{RUNTIME % 60:02d}, {len(D.SHOTS)} shots. Each shot gives the mission clock shown in the corner "
         "(from the arrival), what is on screen, any text on screen, the subtitled lines (speaker tags are shown as "
         "written), and the sound.", ""]
    for s in D.SHOTS:
        L += [f"## {s['n']}. ({s['dur']} s) · clock {audience_clock(s)}", "", s["see"]]
        if s["hud"]:
            L.append("On screen: " + " · ".join(f"“{h}”" for h in s["hud"]))
        for sp, line in s["comm"]:
            L.append(f"> **{sp}:** {line}")
        heard = re.sub(r"\s*\([^)]*\)", "", s["sound"]).replace("RCS", "thruster")
        L += [f"Sound: {heard}", ""]
    (SB / "audience_script.md").write_text("\n".join(L) + "\n")


ASSET_GROUPS = [
    ("LREF ships and craft", ["AST", "GI", "GI-MAV", "GI-GUN", "GI-PD", "DD", "DD-BRK", "CV", "CV-BRK", "TND", "SHD", "DRN-L", "MSL", "MSL-V"]),
    ("Endeavor and M-1C", ["EN", "EN-FIN", "EN-PD", "EN-MAST", "EN-DMG", "M1C"]),
    ("The Maren Compact", ["BW", "BW-BRK", "CF", "DRN-C", "EMP-POD", "EMP-RG", "RING", "SKR"]),
    ("Environment", ["WORLD", "MAREN", "BRK", "ANCHOR"]),
    ("Blocking", ["PROXY"]),
    ("Effects", [k for k in D.ASSETS if k.startswith("FX-")]),
    ("2D compositing", ["HUD", "SUB"]),
]


def write_assets():
    used = {a: [s["n"] for s in D.SHOTS if a in s["assets"]] for a in D.ASSETS}
    L = ["# Asset requests", "",
         f"Everything *{D.TITLE}* ({D.REVISION.lower()}) needs from the modelling session, with the shots that need each item. "
         "Generated from `storyboard/tidebreak_data.py`.", "",
         "- **Status:** *built* exists; *extend* exists but needs additions; *new* must be made.",
         "- **Concept first:** per the user's rule, new weapon and ship designs go through concept sheets and the user picks before modelling. "
         "Items without reference art are flagged too.",
         "- **Detail level:** the user asked for everything hero-detailed. The closest view says how much of that detail the camera "
         "can ever see; proxies for the smallest items are open question Q13.",
         f"- **Set-ups:** {sets_text()}", ""]
    for g, ids in ASSET_GROUPS:
        L += [f"## {g}", "", "| ID | Asset | Status | Concept first | Closest view | Shots | Notes |", "|---|---|---|---|---|---|---|"]
        for a in ids:
            name, status, concept, note = D.ASSETS[a]
            near = f"shot {CLOSEST[a][0]}: {CLOSEST[a][1]}, {CLOSEST[a][2]}" if a in CLOSEST else ""
            if a in ("WORLD", "PROXY"):
                shots = "every 3D shot"
            elif a == "MSL":
                shots = f"inside FX-SWARM ({ranges(used['FX-SWARM'])})"
            else:
                shots = ranges(used[a]) or "—"
            L.append(f"| {a} | {name} | {status} | {'yes' if concept else ''} | {near} | {shots} | {note} |")
        L.append("")
    unused = [a for a, v in used.items() if not v and a not in ("PROXY", "MSL")]
    if unused:
        L += ["Not used by any shot yet: " + ", ".join(unused) + ".", ""]
    # The modelling session renders, so it gets the budget, the gate and the plan too.
    budget, total = render_budget()
    L += ["## Render budget and the gate", "",
          "| Class | Kind | Cost | Shots | Frames | Time |", "|---|---|---|---|---|---|"]
    L += [f"| {c} | {n} | {note} | {ranges(ns) or '—'} | {fr:,} | {h:,.1f} h |" for c, n, note, ns, fr, h in budget]
    L += [f"| | **Total** | | {len(D.SHOTS)} shots | {FRAMES:,} | **{total:,.1f} h** |",
          f"| | With {MARGIN:.0%} for re-renders | | | | **{total * (1 + MARGIN):,.1f} h** |", "",
          D.RENDER_NOTE + " The ceiling is a week (168 h) per full pass.", "", gate_text(), "",
          "### The benchmark worksheet", "",
          "Each benchmark stands for the shots listed. Fill in the measured column; each row's hours are frames × s/frame ÷ 3,600. "
          "Add the rows, multiply by 1.3 for re-renders, and compare with the gate "
          f"({D.GATE_HOURS} h). Then send the measured numbers back to the storyboard session, which enters them in "
          "`MEASURED` and rebuilds the board with them.", "",
          "| Entry | Benchmark | Stands for (shots) | Frames | Estimate, s/frame | Measured, s/frame | Hours at the estimate |",
          "|---|---|---|---|---|---|---|"]
    rows, rest = worksheet()
    L += [f"| `{k}` | {what} | {ranges(ns) or '—'} | {fr:,} | {est:g} | {m if m is not None else ''} | {fr * est / 3600:,.1f} h |"
          for k, what, ns, fr, est, m in rows]
    rest_fr = sum(s["dur"] for s in rest) * FPS
    rest_h = sum(s["dur"] * FPS * spf(s) for s in rest) / 3600
    L += [f"| — | not benchmarked: their class estimates stand | {ranges([s['n'] for s in rest])} | {rest_fr:,} | — | — | {rest_h:,.1f} h |",
          "", "## Production plan", ""]
    L += [f"- **{k}:** {v}" for k, v in [("Sets", sets_text()), ("Batches", batches_text())] + list(D.PRODUCTION_PLAN)]
    (ROOT / "ASSET_REQUESTS.md").write_text("\n".join(L) + "\n")


def check_script(page):
    """Parse the page's script with node, when it is installed: one stray quote in a sketch stops every sketch drawing."""
    node = shutil.which("node")
    if not node:
        return
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
        f.write(re.search(r"<script>(.*?)</script>", page, re.S).group(1))
    try:
        r = subprocess.run([node, "--check", f.name], capture_output=True, text=True)
    finally:
        os.unlink(f.name)
    if r.returncode:
        err = next((ln for ln in r.stderr.splitlines() if "Error" in ln), r.stderr.strip()[:200])
        NOTES.append(f"the page's script doesn't parse ({err}), so no sketch will draw")


def main():
    prepare_images()
    check()
    head, body = build_html()
    page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            + head + "</head>\n<body>\n" + body + "</body>\n</html>\n")
    (SB / "index.html").write_text(page)
    check_script(page)
    if "--fragment" in sys.argv:
        frag = pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1])
        frag.parent.mkdir(parents=True, exist_ok=True)
        frag.write_text(head + body)
        (frag.parent / "img").mkdir(exist_ok=True)
        for p in (SB / "img").iterdir():
            shutil.copy(p, frag.parent / "img" / p.name)
    write_csv()
    write_md()
    write_assets()
    write_audience()
    budget, total = render_budget()
    print(f"{len(D.SHOTS)} shots, {RUNTIME} s ({RUNTIME // 60}:{RUNTIME % 60:02d}), {FRAMES} frames; "
          f"render estimate {total:,.0f} h, {total * (1 + MARGIN):,.0f} h with margin")
    print(f"final approach {FINAL_KM:,.0f} km, turnover {fmt_clock(T_TURN * 3600)}, stop {fmt_clock(T_STOP * 3600)}")
    print(f"spinal: {math.dist(AST_FIRE, HIT):,.0f} km in {(T_HIT - T_FIRE) * 3600:.1f} s, impact {fmt_clock(T_HIT * 3600)}, "
          f"a miss passes {line_miss(AST_FIRE, HIT) - 6_400:,.0f} km above Maren")
    print(gate_text())
    for c, name, _, ns, fr, h in budget:
        print(f"  class {c:2s} {len(ns):2d} shots {fr:5,d} frames {h:6.1f} h")
    print("checks: " + ("all clear" if not NOTES else f"{len(NOTES)} to look at"))
    for n in NOTES:
        print("  - " + n)


if __name__ == "__main__":
    main()
