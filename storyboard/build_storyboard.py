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

--fragment writes the page without <html>/<head>/<body> for the artifact viewer.
--doc-base sets where doctrine rule links point (default: the local reading edition).
"""
import csv
import html
import importlib.util
import math
import pathlib
import random
import shutil
import sys

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
SEC_PER_FRAME = {"A": 35, "B": 75, "C": 150, "D": 15, "E": 2}

# ----------------------------------------------------------------- timing
t = 0
for n, s in enumerate(D.SHOTS, 1):
    s["n"] = n
    if s["comm"] and "SUB" not in s["assets"]:
        s["assets"].append("SUB")
    s["t0"], s["t1"] = t, t + s["dur"]
    s["f0"], s["f1"] = t * FPS + 1, (t + s["dur"]) * FPS
    t += s["dur"]
RUNTIME = t
FRAMES = RUNTIME * FPS


def mmss(sec):
    return f"{int(sec // 60)}:{sec % 60:04.1f}"


def clock_hours(c):
    h, m, s = c[2:].split(":")
    return int(h) + int(m) / 60 + int(s) / 3600


def rule_doc(rid):
    return "maren" if rid.startswith("H") else "lref"


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

    def curve(self, a, c, b, cls):
        (ax, ay), (cx, cy), (bx, by) = self.P(*a), self.P(*c), self.P(*b)
        self.add(f'<path d="M{ax:.1f},{ay:.1f} Q{cx:.1f},{cy:.1f} {bx:.1f},{by:.1f}" class="{cls}"/>')

    def text(self, x, y, s, cls="m-t", anchor="start", dx=0, dy=0):
        px, py = self.P(x, y)
        self.add(f'<text x="{px + dx:.1f}" y="{py + dy:.1f}" class="{cls}" text-anchor="{anchor}">{E(s)}</text>')

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


def path_point(p0, p1, s):
    L = math.dist(p0, p1)
    return (p0[0] + (p1[0] - p0[0]) * s / L, p0[1] + (p1[1] - p0[1]) * s / L)


EXIT, LEE = (450_000, 20_000), (150_000, 0)
SKERRY = (380_000 * math.cos(math.radians(40)), 380_000 * math.sin(math.radians(40)))


def x_on_track(x):
    return (x, 20_000 * (x - 150_000) / 300_000)


def map_a():
    m = Map(-60_000, 480_000, -130_000, 300_000, 1_000)
    cx, cy = m.P(0, 0)
    m.add(f'<path d="M{cx - 260:.1f},{cy:.1f} a260,260 0 1,0 520,0 a260,260 0 1,0 -520,0 '
          f'M{cx - 120:.1f},{cy:.1f} a120,120 0 1,1 240,0 a120,120 0 1,1 -240,0Z" class="m-torus" fill-rule="evenodd"/>')
    m.text(0, -205_000, "THE BREAKERS · 120,000–260,000 km", "m-t m-muted", "middle")
    m.circle(0, 0, 380_000, "m-orbit")
    m.circle(0, 0, 42_164, "m-orbit")
    m.circle(0, 0, 6_400, "m-planet", 4)
    m.text(0, 0, "Maren", "m-t", "end", -7, 14)
    m.mark(42_164, 0, "m-comp", "dia", 3)
    m.text(42_164, 0, "Breakwater", "m-t m-compt", "start", 5, -6)
    m.mark(*SKERRY, "m-moon", "dot", 4)
    m.text(*SKERRY, "Skerry (mass driver, laser, depot)", "m-t", "start", 7, 4)
    m.line([EXIT, LEE], "m-lref")
    m.mark(*EXIT, "m-lreff", "sq", 3.5)
    m.text(*EXIT, "Warp exit · shield park", "m-t m-lreft", "end", -2, 20)
    m.text(*EXIT, "Nauvoo, Excelsior", "m-t m-muted", "end", -2, 32)
    for s_km, lab in ((20_400, "T+0:59 at 20 km/s"),):
        p = path_point(EXIT, LEE, s_km)
        m.mark(*p, "m-lreff", "dot", 2.5)
        m.text(*p, lab, "m-t", "middle", 0, -9)
    for x, lab, dy in ((260_000, "T+3:20 into the Breakers", 14), (170_400, "T+4:35 turnover", -8)):
        p = x_on_track(x)
        m.mark(*p, "m-lreff", "dot", 2.5)
        m.text(*p, lab, "m-t", "middle", 0, dy)
    m.mark(*LEE, "m-rock", "dot", 3.5)
    m.text(*LEE, "the Lee · T+5:09", "m-t m-lreft", "middle", 0, 16)
    m.curve(EXIT, (380_000, 170_000), SKERRY, "m-missile")
    m.text(400_000, 120_000, "wave one · T+0:18 → T+1:04", "m-t m-lreft", "middle")
    m.curve(SKERRY, (160_000, 180_000), (92_000, -6_000), "m-kin")
    m.text(150_000, 125_000, "Skerry's three rounds · T+0:04 → T+6:40", "m-t m-compt", "middle")
    m.scalebar(100_000, "100,000 km")
    return m.svg(D.MAPS["A"])


def map_b():
    m = Map(130_000, 290_000, -40_000, 40_000, 250)
    cx, cy = m.P(0, 0)
    m.add(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{260_000 / 250:.1f}" class="m-edge"/>')
    rnd = random.Random(7)
    for _ in range(170):
        x, y = rnd.uniform(130_000, 290_000), rnd.uniform(-40_000, 40_000)
        if math.hypot(x, y) < 260_000:
            m.mark(x, y, "m-rockdot", "dot", rnd.uniform(0.6, 1.5))
    m.text(257_000, 36_000, "outer edge of the Breakers", "m-t m-muted", "end")
    m.text(140_000, -36_000, "Large rocks shown are a sample: real spacing is hundreds of km.", "m-t m-muted")
    m.line([x_on_track(290_000), LEE], "m-lref")
    ev = [(260_000, "T+3:20 enter", -10), (248_000, "T+3:30 Site 1 dazzles", 14),
          (236_000, "T+3:40 pods launch", -22), (221_600, "T+3:52 Canterbury lost", 26),
          (200_000, "T+4:10 drones wake", -10), (182_000, "T+4:25 Normandy lost", 14),
          (170_400, "T+4:35 turnover", -22)]
    for x, lab, dy in ev:
        p = x_on_track(x)
        m.mark(*p, "m-lreff", "dot", 2.4)
        m.text(*p, lab, "m-t", "middle", 0, dy)
    for dx, dy in ((0, 3_000), (-1_500, 4_500), (1_000, -2_500)):
        p = x_on_track(236_000)
        m.mark(p[0] + dx, p[1] + dy, "m-comp", "dia", 2.2)
    plat = (221_000, x_on_track(221_000)[1] + 500)
    m.mark(*plat, "m-comp", "x", 3)
    ast = x_on_track(229_600)
    m.mark(*ast, "m-lreff", "sq", 3)
    m.text(*ast, "Astrid (8,000 km back)", "m-t m-lreft", "middle", 0, -36)
    m.line([ast, plat], "m-spinal")
    m.mark(*LEE, "m-rock", "dot", 4)
    m.text(*LEE, "the Lee", "m-t m-lreft", "start", 7, 4)
    m.scalebar(10_000, "10,000 km")
    return m.svg(D.MAPS["B"])


def map_c():
    m = Map(-200, 1_400, -900, 900, 10 / 3)
    m.add(f'<rect x="{m.P(0, 9)[0]:.1f}" y="{m.P(0, 9)[1]:.1f}" width="{1_400 * 0.3:.1f}" height="{18 * 0.3:.1f}" class="m-shadow"/>')
    m.text(1_380, -45, "the rock's shadow: hidden from Site 1 and Breakwater", "m-t m-lreft", "end")
    m.text(1_380, -85, "the fleet strings out along it, 50–250 km apart", "m-t m-muted", "end")
    m.line([(-20, 0), (-190, 0)], "m-arrow", 'marker-end="url(#arr)"')
    m.text(-190, -130, "to Breakwater 108,000 km", "m-t m-muted")
    m.text(-190, -170, "to Site 1 143,600 km", "m-t m-muted")
    m.mark(0, 0, "m-rock", "dot", 3.2)
    m.text(0, 0, "the Lee (18 km)", "m-t", "end", -6, -10)
    for x, lab in ((6, "Endeavor"), (110, "Donnager"), (220, ""), (330, ""), (440, ""), (700, "Astrid")):
        m.mark(x, 0, "m-lreff", "sq" if lab in ("Astrid", "Endeavor") else "dot", 2.4)
        if lab:
            m.text(x, 0, lab, "m-t", "middle", 0, -10 if lab != "Endeavor" else 16)
    plat = (400, 693)
    m.mark(*plat, "m-comp", "x", 4)
    m.text(*plat, "railgun platform on a rock, 800 km", "m-t m-compt", "middle", 0, -10)
    m.line([plat, (8, 6)], "m-kin")
    m.text(210, 360, "T+5:21 salvo: 32 s flight", "m-t m-compt", "start", 6)
    m.line([(8, 4), (396, 688)], "m-lref", 'stroke-dasharray="1 3"')
    m.text(150, 290, "T+5:22 broadside", "m-t m-lreft", "end", -6)
    frig_rock, frig = (20, -56), (14, -38)
    m.mark(*frig_rock, "m-rockdot", "dot", 2.2)
    m.mark(*frig, "m-comp", "dia", 2.8)
    m.text(*frig, "Compact frigate: 60 km off, lanced at 40 km", "m-t m-compt", "start", 8, 30)
    m.scalebar(200, "200 km")
    return m.svg(D.MAPS["C"])


def map_d():
    m = Map(-20_000, 160_000, -70_000, 70_000, 1_000 / 3)
    x_h, _ = m.P(6_400, 0)
    m.add(f'<rect x="{x_h:.1f}" y="{m.pad}" width="{m.w - x_h - m.pad:.1f}" height="{m.h - 2 * m.pad:.1f}" class="m-sky"/>')
    m.text(158_000, 66_000, "Site 1's sky (above its horizon)", "m-t m-compt", "end")
    m.circle(0, 0, 42_164, "m-orbit")
    for k in range(12):
        a = math.radians(30 * k)
        if k:
            m.mark(42_164 * math.cos(a), 42_164 * math.sin(a), "m-comp", "dot", 1.8)
    m.circle(0, 0, 6_400, "m-planet")
    m.mark(6_400, 0, "m-comp", "tri", 3)
    m.text(0, -8_000, "Maren · Site 1", "m-t", "middle", 0, 12)
    m.mark(42_164, 0, "m-comp", "dia", 4)
    m.text(42_164, 0, "Breakwater", "m-t m-compt", "middle", 0, 18)
    m.text(-19_000, 52_000, "inner ring: 12 emplacements", "m-t m-muted")
    lee_509, lee_545 = (150_000, 0), (148_600, -20_100)
    m.mark(*lee_509, "m-rock", "dot", 3)
    m.mark(*lee_545, "m-rock", "dot", 3)
    m.text(*lee_509, "the Lee at T+5:09", "m-t", "end", -6, -8)
    m.text(*lee_545, "the Lee at T+5:45", "m-t", "end", -6, 14)
    stand = (54_000, 0)
    m.line([lee_545, stand], "m-lref")
    m.curve(lee_509, (100_000, 4_000), (42_900, 400), "m-missile")
    m.text(105_000, 13_000, "wave two · T+5:42 → T+6:01", "m-t m-lreft", "middle")
    net = (93_000, -7_600)
    rnd = random.Random(3)
    for _ in range(40):
        m.mark(net[0] + rnd.gauss(0, 1_500), net[1] + rnd.gauss(0, 1_500), "m-kindot", "dot", 0.8)
    m.text(*net, "Skerry's net · T+6:40 (fleet steps aside)", "m-t m-compt", "middle", 0, 22)
    to2 = path_point(lee_545, stand, math.dist(lee_545, stand) - 20_400)
    m.mark(*to2, "m-lreff", "dot", 2.4)
    m.text(*to2, "T+7:05 turnover", "m-t", "middle", 0, -9)
    ast = (42_164 + 14_700, 0)
    m.mark(*ast, "m-lreff", "sq", 3)
    m.line([ast, (42_600, 0)], "m-spinal")
    m.text(*ast, "Astrid fires from 14,700 km · T+7:26", "m-t m-lreft", "middle", 0, 32)
    m.text(-19_000, -62_000, "Maren-fixed frame: Site 1 and Breakwater stay put; the Lee drifts 12.8°/h.", "m-t m-muted")
    m.scalebar(20_000, "20,000 km")
    return m.svg(D.MAPS["D"])


MAP_SVGS = {"A": map_a, "B": map_b, "C": map_c, "D": map_d}


# ----------------------------------------------------------------- timeline
def timeline_svg():
    W, x0, x1 = 1000, 40, 960
    hours = 9.5
    fx = lambda s: x0 + (x1 - x0) * s / RUNTIME
    mx = lambda h: x0 + (x1 - x0) * h / hours
    out = [f'<svg viewBox="0 0 {W} 250" role="img" aria-label="Film time against mission time">']
    act_span = {}
    for s in D.SHOTS:
        a = act_span.setdefault(s["act"], [s["t0"], s["t1"]])
        a[1] = s["t1"]
    for i, (num, name, _) in enumerate(D.ACTS):
        a, b = act_span[num]
        out.append(f'<rect x="{fx(a):.1f}" y="18" width="{fx(b) - fx(a):.1f}" height="22" class="tl-act tl-act{i}"/>')
        out.append(f'<text x="{fx(a) + 6:.1f}" y="33" class="tl-actt">{num} · {E(name.upper())}</text>')
    for s in D.SHOTS:
        h = clock_hours(s["clock"])
        out.append(f'<line x1="{fx(s["t0"]):.1f}" y1="42" x2="{mx(h):.1f}" y2="196" class="tl-link tl-l{"I II III IV".split().index(s["act"])}"/>')
        out.append(f'<line x1="{fx(s["t0"]):.1f}" y1="40" x2="{fx(s["t0"]):.1f}" y2="46" class="tl-tick"/>')
    for sec in range(0, RUNTIME + 1, 15):
        out.append(f'<text x="{fx(sec):.1f}" y="12" class="tl-t" text-anchor="middle">{sec // 60}:{sec % 60:02d}</text>')
    out.append(f'<line x1="{x0}" y1="198" x2="{x1}" y2="198" class="tl-axis"/>')
    for hr in range(0, 10):
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
.tbl{overflow-x:auto; border:1px solid var(--line); border-radius:8px; background:var(--panel); margin:1rem 0;}
table{border-collapse:collapse; width:100%; font-size:.86rem; font-variant-numeric:tabular-nums;}
th{font:600 .74rem var(--f-display); letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:.55rem .7rem; border-bottom:1px solid var(--line);}
td{padding:.5rem .7rem; border-top:1px solid var(--line); vertical-align:top;}
tr:first-child td{border-top:0;}
td.mono, .mono{font-family:var(--f-mono); font-size:.8rem;}
.figure{background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:.8rem; margin:0; min-width:0;}
.figure svg{display:block; width:100%; height:auto;}
.figure figcaption{font-size:.8rem; color:var(--muted); margin-top:.5rem;}
.scrollx{overflow-x:auto;} .scrollx svg{min-width:760px;}
.maps{display:grid; grid-template-columns:repeat(2,minmax(0,1fr)); gap:1rem;}
.legend{display:flex; flex-wrap:wrap; gap:.3rem 1.2rem; font:400 .78rem var(--f-mono); color:var(--muted); margin:0 0 .8rem;}
.legend i{display:inline-block; width:22px; height:0; vertical-align:middle; margin-right:.4rem; border-top:2px solid;}
.lg-lref{border-color:var(--lref);} .lg-comp{border-color:var(--comp);} .lg-mis{border-top-style:dotted!important; border-color:var(--lref);} .lg-kin{border-top-style:dashed!important; border-color:var(--comp);}
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
.m-kindot{fill:var(--comp); fill-opacity:.8;}
.m-spinal{fill:none; stroke:var(--lref); stroke-width:1.2; stroke-dasharray:6 2 1 2;}
.m-arrow{fill:none; stroke:var(--muted); stroke-width:1;}
.m-arrowhead{fill:var(--muted);}
.m-shadow{fill:var(--lref); fill-opacity:.25;}
.m-sky{fill:var(--comp); fill-opacity:.06;}
.m-scale{fill:none; stroke:var(--ink); stroke-width:1;}
/* timeline */
.tl-act{fill-opacity:.9;} .tl-act0{fill:var(--lref); fill-opacity:.35;} .tl-act1{fill:var(--clock); fill-opacity:.3;} .tl-act2{fill:var(--heat); fill-opacity:.3;} .tl-act3{fill:var(--comp); fill-opacity:.3;}
.tl-actt{font:600 12px var(--f-display); letter-spacing:.06em; fill:var(--ink);}
.tl-t{font:400 10px var(--f-mono); fill:var(--ink);} .tl-muted{fill:var(--muted);}
.tl-tick, .tl-axis{stroke:var(--muted); stroke-width:1;}
.tl-link{stroke-width:1; stroke-opacity:.6;} .tl-l0{stroke:var(--lref);} .tl-l1{stroke:var(--clock);} .tl-l2{stroke:var(--heat);} .tl-l3{stroke:var(--comp);}
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
footer{border-top:1px solid var(--line); margin-top:3rem; padding-block:1.4rem 2.6rem; color:var(--muted); font-size:.82rem;}
a:focus-visible{outline:2px solid var(--lref); outline-offset:2px;}
@media (max-width: 900px){ .grid2, .maps, .shots{grid-template-columns:minmax(0,1fr);} }
@media (max-width: 520px){ .rows{grid-template-columns:minmax(0,1fr);} .rows dt{margin-top:.2rem;} dl.kv{grid-template-columns:minmax(0,1fr);} }
"""


def rule_chips(rules):
    out = []
    for r in rules:
        doc = rule_doc(r)
        out.append(f'<a class="chip r-{doc}" href="{DOC_BASE}#{doc}-{r}" target="_blank" rel="noopener">{r}</a>')
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
        comm = '<div class="comm">' + "".join(f"<div><b>{E(sp)}</b>{E(line)}</div>" for sp, line in s["comm"]) + "</div>"
    rig = "".join(f"<code>{E(r)}</code>" for r in s["rig"]) or '<span class="mono">none</span>'
    return f"""<article class="shot" id="shot-{s['n']}">
<div class="media">{media}<span class="badge n">{s['n']}</span><span class="badge t">{mmss(s['t0'])}–{mmss(s['t1'])} · {s['dur']} s</span></div>
<div class="body"><h4>{E(s['title'])}</h4>
<div class="meta"><span>{E(s['cam'])}</span><span>frames {s['f0']}–{s['f1']}</span></div>
<div class="meta"><span class="clock">{E(s['clock'])}</span><span>{E(s['real'])}</span><span>map {s['map']}</span><span>render class {s['cost']}</span></div>
<p class="action">{E(s['action'])}</p>{comm}
<dl class="rows"><dt>Doctrine</dt><dd>{rule_chips(s['rules'])}</dd><dt>VFX</dt><dd>{E(s['vfx'])}</dd>
<dt>Rig</dt><dd>{rig}</dd><dt>Assets</dt><dd>{asset_chips(s['assets'])}</dd><dt>Sound</dt><dd>{E(s['sound'])}</dd></dl>
</div></article>"""


def render_budget():
    rows, total = [], 0
    for c, (name, note) in D.RENDER_CLASSES.items():
        shots = [s for s in D.SHOTS if s["cost"] == c]
        fr = sum(s["dur"] for s in shots) * FPS
        hrs = fr * SEC_PER_FRAME[c] / 3600
        total += hrs
        rows.append((c, name, note, len(shots), fr, hrs))
    return rows, total


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
    maps = "".join(f'<figure class="figure" id="map-{k}">{MAP_SVGS[k]()}<figcaption><b>Map {k}.</b> {E(v)}. To scale, except the ship and site symbols.</figcaption></figure>'
                   for k, v in D.MAPS.items())
    budget, total = render_budget()
    brow = "".join(f'<tr><td class="mono">{c}</td><td>{E(n)}</td><td>{E(note)}</td><td class="mono">{k}</td><td class="mono">{fr:,}</td><td class="mono">{h:,.0f} h</td></tr>'
                   for c, n, note, k, fr, h in budget)
    new_assets = [a for a, v in D.ASSETS.items() if v[1] != "built"]
    concept = [a for a, v in D.ASSETS.items() if v[2]]
    sk = ",\n".join(f"{s['n']}: function () {{ return {s['sketch']}; }}" for s in D.SHOTS if s["sketch"])
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
<p class="lead">An LREF task group led by L.R.E.F.S. Astrid and L.R.E.F.S. Endeavor breaks the orbital defence of Maren, a world held by the Maren Compact. Nine real hours, told in {RUNTIME // 60}:{RUNTIME % 60:02d} of film, every time jump marked with the mission clock. Built on the approved doctrines.</p>
<ul class="facts"><li>Runtime <b>{RUNTIME // 60}:{RUNTIME % 60:02d}</b></li><li>Frames <b>{FRAMES:,}</b> @ 24 fps</li><li>Shots <b>{len(D.SHOTS)}</b></li><li>Mission <b>T+0:00 → T+9:10</b></li><li>Format <b>{E(D.FORMAT)}</b></li></ul>
<p class="note">Sketches are layout drawings; frames marked <em>render</em> are current Blender renders of the Endeavor used as look reference. Doctrine chips open the rule in the doctrine reading edition. Comm lines are GUN side only, as subtitles for now.</p>
</header>
<nav class="toc" aria-label="Sections"><div class="wrap"><a href="#overview">Overview</a><a href="#timeline">Timeline</a><a href="#maps">Maps</a><a href="#shots">Shots</a><a href="#production">Production</a><a href="#reviews">Reviews</a><a href="{DOC_BASE}" target="_blank" rel="noopener">Doctrine ↗</a></div></nav>
<main class="wrap">
<section id="overview"><h2>Forces and plan</h2>
<div class="grid2"><div class="card side-lref"><h3>LREF task group</h3><dl class="kv">{fleet}</dl></div>
<div class="card side-comp"><h3>The Maren Compact</h3><dl class="kv">{defs}</dl></div></div>
<div class="tbl"><table><thead><tr><th>Mission time</th><th>Phase</th><th>What happens</th></tr></thead><tbody>{phases}</tbody></table></div>
<div class="tbl"><table><thead><tr><th>Key number</th><th>Value</th><th>Source</th></tr></thead><tbody>{keyn}</tbody></table></div>
</section>
<section id="timeline"><h2>Film time and mission time</h2><figure class="figure"><div class="scrollx">{timeline_svg()}</div></figure></section>
<section id="maps"><h2>Tactical maps</h2>
<div class="legend"><span><i class="lg-lref"></i>LREF</span><span><i class="lg-comp"></i>Maren Compact</span><span><i class="lg-mis"></i>missile track</span><span><i class="lg-kin"></i>kinetic rounds</span></div>
<div class="maps">{maps}</div></section>
<section id="shots"><h2>Shot list</h2>{"".join(acts_html)}</section>
<section id="production"><h2>Production</h2>
<div class="grid2"><div class="card"><h3>Render budget</h3><p class="action">Estimated with the measured Cycles costs from the project context. The user's ceiling is a week (168 h) per full pass.</p>
<div class="tbl"><table><thead><tr><th>Class</th><th>Kind</th><th>Cost</th><th>Shots</th><th>Frames</th><th>Time</th></tr></thead><tbody>{brow}
<tr><td></td><td><b>Total</b></td><td></td><td class="mono">{len(D.SHOTS)}</td><td class="mono">{FRAMES:,}</td><td class="mono"><b>{total:,.0f} h</b></td></tr></tbody></table></div></div>
<div class="card"><h3>Assets</h3><p class="action">{len(new_assets)} of {len(D.ASSETS)} assets are new or need additions; {len(concept)} of them go through concept sheets first (per the user's rule for new designs): {", ".join(concept)}. The full list, with the shots that need each one, is in <code>ASSET_REQUESTS.md</code>.</p>
<p class="action">Legend: <span class="chip">built</span><span class="chip new">new or extended</span><span class="chip concept">concept first</span></p></div></div>
</section>
<section id="reviews"><h2>Reviews</h2><p class="action">Round 1 is under way: physics, military doctrine, lore, cinematography and production feasibility, each by its own reviewer. Reports and the synthesis go to <code>review/</code>.</p></section>
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
                    "mission_clock", "time_treatment", "camera", "action", "comms", "doctrine", "vfx", "rig",
                    "assets", "sound", "render_class", "map", "reference_frame"])
        for s in D.SHOTS:
            w.writerow([s["n"], s["act"], s["title"], s["t0"], s["t1"], s["f0"], s["f1"], s["dur"], s["clock"],
                        s["real"], s["cam"], s["action"], " | ".join(f"{a}: {b}" for a, b in s["comm"]),
                        " ".join(s["rules"]), s["vfx"], "; ".join(s["rig"]), " ".join(s["assets"]), s["sound"],
                        s["cost"], s["map"], s["render"] or ""])


def write_md():
    L = [f"# {D.TITLE}: shot list", "",
         f"{D.REVISION}. Runtime {RUNTIME // 60}:{RUNTIME % 60:02d} ({FRAMES:,} frames at {FPS} fps), {len(D.SHOTS)} shots, "
         f"mission span T+0:00 → T+9:10, {D.FORMAT}. Generated from `storyboard/tidebreak_data.py`; "
         "the page with maps and sketches is `storyboard/index.html`.", "",
         "Rule IDs refer to `doctrine/LREF_doctrine.md` (O, D, A) and `doctrine/Defence_doctrine.md` (HO, HD, H). "
         "Asset IDs refer to `ASSET_REQUESTS.md`. Render classes: " +
         "; ".join(f"**{k}** {v[0]} ({v[1]})" for k, v in D.RENDER_CLASSES.items()) + ".", "",
         "## Mission phases", "", "| Mission time | Phase | What happens |", "|---|---|---|"]
    L += [f"| {a}–{b} | {n} | {d} |" for a, b, n, d in D.PHASES]
    L += ["", "## Overview", "", "| # | Film | Frames | Mission clock | Time | Title | Camera | Doctrine |", "|---|---|---|---|---|---|---|---|"]
    L += [f"| {s['n']} | {mmss(s['t0'])}–{mmss(s['t1'])} | {s['f0']}–{s['f1']} | {s['clock']} | {s['real']} | {s['title']} | {s['cam']} | {' '.join(s['rules'])} |" for s in D.SHOTS]
    for num, name, summary in D.ACTS:
        L += ["", f"## Act {num}: {name}", "", summary]
        for s in [x for x in D.SHOTS if x["act"] == num]:
            L += ["", f"### {s['n']}. {s['title']}", "",
                  f"- **Film:** {mmss(s['t0'])}–{mmss(s['t1'])} ({s['dur']} s), frames {s['f0']}–{s['f1']}",
                  f"- **Mission:** {s['clock']} · {s['real']}",
                  f"- **Camera:** {s['cam']}",
                  f"- **Action:** {s['action']}"]
            if s["comm"]:
                L.append("- **Comms:** " + " / ".join(f"{a}: “{b}”" for a, b in s["comm"]))
            L += [f"- **Doctrine:** {', '.join(s['rules'])}",
                  f"- **VFX:** {s['vfx']}",
                  f"- **Rig:** {'; '.join(s['rig']) if s['rig'] else 'none'}",
                  "- **Assets:** " + ", ".join(f"{a} ({D.ASSETS[a][1]})" for a in s["assets"]),
                  f"- **Sound:** {s['sound']}",
                  f"- **Render class:** {s['cost']} · **Map:** {s['map']}" + (f" · **Reference frame:** `{s['render']}`" if s["render"] else "")]
    (SB / "shots.md").write_text("\n".join(L) + "\n")


def write_assets():
    groups = [("LREF ships and craft", ["AST", "GI", "GI-MAV", "GI-GUN", "GI-PD", "DD", "DD-BRK", "CV", "CV-BRK", "TND", "SHD", "DRN-L", "MSL", "MSL-V"]),
              ("Endeavor and M-1C", ["EN", "EN-FIN", "EN-MAST", "EN-DMG", "M1C"]),
              ("The Maren Compact", ["BW", "BW-BRK", "CF", "DRN-C", "EMP-POD", "EMP-RG", "RING", "SKR"]),
              ("Environment", ["MAREN", "BRK", "LEE"]),
              ("Effects", [k for k in D.ASSETS if k.startswith("FX-")]),
              ("2D compositing", ["HUD", "SUB"])]
    used = {a: [s["n"] for s in D.SHOTS if a in s["assets"]] for a in D.ASSETS}
    L = ["# Asset requests", "",
         f"Everything *{D.TITLE}* ({D.REVISION.lower()}) needs from the modelling session, with the shots that need each item. "
         "Generated from `storyboard/tidebreak_data.py`.", "",
         "- **Status:** *built* exists; *extend* exists but needs additions; *new* must be made.",
         "- **Concept first:** per the user's rule, new weapon and ship designs go through concept sheets and the user picks before modelling. "
         "Items without reference art are flagged too.",
         "- **Detail level:** the user asked for everything hero-detailed.", ""]
    for g, ids in groups:
        L += [f"## {g}", "", "| ID | Asset | Status | Concept first | Shots | Notes |", "|---|---|---|---|---|---|"]
        for a in ids:
            name, status, concept, note = D.ASSETS[a]
            L.append(f"| {a} | {name} | {status} | {'yes' if concept else ''} | {', '.join(map(str, used[a])) or '—'} | {note} |")
        L.append("")
    unused = [a for a, v in used.items() if not v]
    if unused:
        L += ["Not used by any shot yet: " + ", ".join(unused) + ".", ""]
    (ROOT / "ASSET_REQUESTS.md").write_text("\n".join(L))


def main():
    prepare_images()
    head, body = build_html()
    (SB / "index.html").write_text("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
                                   "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
                                   + head + "</head>\n<body>\n" + body + "</body>\n</html>\n")
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
    budget, total = render_budget()
    print(f"{len(D.SHOTS)} shots, {RUNTIME} s, {FRAMES} frames; render estimate {total:,.0f} h")


if __name__ == "__main__":
    main()
