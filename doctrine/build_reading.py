#!/usr/bin/env python3
"""Build the reading edition of the Tidebreak doctrines.

    pip install markdown-it-py beautifulsoup4
    python3 doctrine/build_reading.py [--fragment PATH]

Writes doctrine/reading/Tidebreak_doctrines.html, a standalone page that
opens in any browser. With --fragment it also writes the same page without
the <html>/<head>/<body> wrapper, which is the form the claude.ai artifact
viewer expects.

The Markdown files stay the source of truth; re-run this after editing them.
"""
import html
import math
import pathlib
import re
import sys

from bs4 import BeautifulSoup, NavigableString
from markdown_it import MarkdownIt

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "doctrine" / "reading" / "Tidebreak_doctrines.html"

DOCS = [
    # key, tab label, source, side (accent), bare-§ target, wide tables
    ("lref", "LREF doctrine", "doctrine/LREF_doctrine.md", "lref", "lref", False),
    ("maren", "Maren defence", "doctrine/Defence_doctrine.md", "maren", "maren", False),
    ("dec", "Decisions", "OPEN_QUESTIONS.md", "plain", None, False),
    ("wn", "Working numbers", "doctrine/working_numbers.md", "plain", "wn", True),
    ("draft", "Draft check", "doctrine/Draft_corrections.md", "plain", "lref", False),
]

FILE_TABS = {
    "OPEN_QUESTIONS.md": "dec",
    "doctrine/working_numbers.md": "wn",
    "working_numbers.md": "wn",
    "working_numbers.py": "wn",
    "doctrine/Defence_doctrine.md": "maren",
    "Defence_doctrine.md": "maren",
    "doctrine/LREF_doctrine.md": "lref",
    "LREF_doctrine.md": "lref",
    "doctrine/Draft_corrections.md": "draft",
}

TERMS = {
    "AVPSA": "Articulated Variable Position Sensor Array: the Astrid's ~100 m sensor dish.",
    "CIWS": "Close-in weapon system: rotary point-defence cannons that throw kill clouds.",
    "ECW": "Electronic and cyber warfare: the destroyers' job.",
    "EW": "Electronic warfare: jamming, spoofing and deception.",
    "EMCON": "Emission control: no radio; ships talk by laser link.",
    "PD": "Point defence: everything that kills incoming missiles and drones.",
    "LFA": "Laser focusing array: the main laser turret.",
    "LFAs": "Laser focusing arrays: the main laser turrets.",
    "MAV": "Missile attack vessel: a frigate in the hedgehog configuration.",
    "MRV": "Multi-role vessel: a hull class with no spinal cannon.",
    "SCC": "Spinal-cannon-capable vessel: a hull built around a spinal cannon.",
    "ROE": "Rules of engagement.",
    "RCS": "Reaction control system: the small manoeuvring thrusters.",
    "MDC": "Maren Defence Command: the Compact's system-defence headquarters.",
    "T-SEC": "Terrestrial and Space Expeditionary Corps: the GUN's space marines.",
    "AU": "Astronomical unit: about 150 million km.",
    "MIRV": "Multiple independently targetable vehicle: one missile, several warheads.",
    "MIRVs": "Multiple independently targetable vehicles: one missile, several warheads.",
    "HUD": "Head-up display: the 2D tactical overlays in the film.",
    "Δv": "Delta-v: the total change of velocity a drive can deliver.",
    "IR": "Infrared.",
    "UV": "Ultraviolet.",
}

SECTION_RE = re.compile(r"^(\d+(?:\.\d+)?)\.?\s+(.*)$")
RULE_IDS = re.compile(r"^(?:O|D|HO|HD)\d{1,2}$")

TOKEN_RE = re.compile(
    r"(?P<chip>\[(?:Lore|Model)(?:[;,] (?:Lore|Model))*\])"
    r"|(?P<wn>WN §\d+(?:[–-]\d+)?(?:(?:, | and )§\d+(?:[–-]\d+)?)*)"
    r"|(?P<docsec>(?:LREF|Defence) §\d+(?:\.\d+)?)"
    r"|(?P<sec>§\d+(?:\.\d+)?)"
    r"|(?P<rule>\b(?:HO|HD|O|D)\d{1,2}\b)"
    r"|(?P<asm>\b[AH]-\d{2}\b)"
    r"|(?P<term>\b(?:" + "|".join(sorted((re.escape(t) for t in TERMS), key=len, reverse=True)) + r")\b)"
)


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def sec_id(key, num):
    return f"{key}-s{num.replace('.', '-')}"


class Site:
    """Everything the cross-reference pass needs to know about all documents."""

    def __init__(self):
        self.targets = {}   # id -> tip text

    def add(self, tid, tip):
        self.targets[tid] = tip


def parse(md_text):
    md = MarkdownIt("commonmark", {"html": False, "typographer": False}).enable("table")
    return BeautifulSoup(md.render(md_text), "html.parser")


def first_pass(key, soup, site):
    """Titles, heading ids, rule cards, register ids, tables."""
    h1 = soup.find("h1")
    title = h1.get_text(" ", strip=True) if h1 else key
    if h1:
        h1.decompose()

    toc = []
    for h in soup.find_all(["h2", "h3"]):
        text = h.get_text(" ", strip=True)
        m = SECTION_RE.match(text)
        if m:
            hid = sec_id(key, m.group(1))
            h.clear()
            num = soup.new_tag("span", attrs={"class": "num"})
            num.string = m.group(1)
            h.append(num)
            h.append(" " + m.group(2))
            site.add(hid, f"§{m.group(1)} {m.group(2)}")
        else:
            hid = f"{key}-{slug(text)}"
        h["id"] = hid
        toc.append((h.name, hid, text))

    for tbl in list(soup.find_all("table")):
        heads = [th.get_text(" ", strip=True) for th in tbl.find_all("th")]
        rows = tbl.find("tbody").find_all("tr") if tbl.find("tbody") else []
        if len(heads) >= 3 and heads[0] == "ID" and heads[1] == "Rule":
            tbl.replace_with(rule_cards(soup, key, heads, rows, site))
            continue
        if heads and heads[0] == "ID" and len(heads) >= 2 and heads[1] == "Assumption":
            for tr in rows:
                tds = tr.find_all("td")
                aid = tds[0].get_text(" ", strip=True).replace("★", "").strip()
                tr["id"] = f"{key}-{aid}"
                site.add(tr["id"], f"{aid}: {tds[1].get_text(' ', strip=True)}")
        for tr in rows:
            for i, td in enumerate(tr.find_all("td")):
                if i < len(heads):
                    td["data-label"] = heads[i]
        tbl["class"] = "stack"
        wrap = soup.new_tag("div", attrs={"class": "table-wrap"})
        tbl.wrap(wrap)

    # the status line becomes a callout
    for p in soup.find_all("p"):
        s = p.find("strong")
        if s and s.get_text().startswith("Status") and p.contents and p.contents[0] is s:
            p["class"] = "callout"
            break
    return title, toc


def rule_cards(soup, key, heads, rows, site):
    box = soup.new_tag("div", attrs={"class": "rules"})
    for tr in rows:
        tds = tr.find_all("td")
        rid = tds[0].get_text(" ", strip=True)
        name = tds[1].get_text(" ", strip=True)
        art = soup.new_tag("article", attrs={"class": "rule", "id": f"{key}-{rid}"})
        badge = soup.new_tag("div", attrs={"class": "rule-id"})
        badge.string = rid
        art.append(badge)
        body = soup.new_tag("div", attrs={"class": "rule-body"})
        h = soup.new_tag("h4")
        h.string = name
        body.append(h)
        detail = soup.new_tag("p", attrs={"class": "rule-detail"})
        for c in list(tds[2].contents):
            detail.append(c)
        body.append(detail)
        meta = soup.new_tag("dl", attrs={"class": "rule-meta"})
        for label, td in zip(heads[3:], tds[3:]):
            if td.get_text(strip=True) in ("", "—"):
                continue
            dt = soup.new_tag("dt")
            dt.string = label
            dd = soup.new_tag("dd")
            for c in list(td.contents):
                dd.append(c)
            meta.append(dt)
            meta.append(dd)
        if meta.contents:
            body.append(meta)
        art.append(body)
        box.append(art)
        site.add(f"{key}-{rid}", f"{rid}: {name}")
    return box


def link(soup, href, text, tip, cls="xref"):
    a = soup.new_tag("a", attrs={"href": "#" + href, "class": cls})
    if tip:
        a["data-tip"] = tip
    a.string = text
    return a


def second_pass(key, bare_target, soup, site):
    """Turn references in running text into links, chips and terms."""
    skip = {"a", "code", "h1", "h2", "h3", "h4", "script", "style", "summary"}
    for node in list(soup.find_all(string=True)):
        if any(p.name in skip for p in node.parents if p.name):
            continue
        text = str(node)
        if not TOKEN_RE.search(text):
            continue
        parts, pos = [], 0
        for m in TOKEN_RE.finditer(text):
            parts.append(text[pos:m.start()])
            pos = m.end()
            kind, tok = m.lastgroup, m.group(0)
            if kind == "chip":
                for i, word in enumerate(re.findall(r"Lore|Model", tok)):
                    span = soup.new_tag("span", attrs={"class": f"chip chip-{word.lower()}",
                                                        "data-tip": "Stated in JCB's lore posts." if word == "Lore"
                                                        else "Already built in the Blender project."})
                    span.string = word
                    parts.append(span)
                    if i == 0 and "Model" in tok and "Lore" in tok:
                        parts.append(" ")
            elif kind == "wn":
                for i, piece in enumerate(re.split(r"((?:, | and ))", tok)):
                    mm = re.search(r"§(\d+)", piece)
                    if mm and (f"wn-s{mm.group(1)}" in site.targets):
                        parts.append(link(soup, f"wn-s{mm.group(1)}", piece,
                                          "Working numbers " + site.targets[f"wn-s{mm.group(1)}"]))
                    else:
                        parts.append(piece)
            elif kind == "docsec":
                doc = "lref" if tok.startswith("LREF") else "maren"
                num = tok.split("§")[1]
                tid = sec_id(doc, num)
                parts.append(link(soup, tid, tok, site.targets.get(tid)) if tid in site.targets else tok)
            elif kind == "sec":
                num = tok[1:]
                tid = sec_id(bare_target, num) if bare_target else None
                parts.append(link(soup, tid, tok, site.targets.get(tid)) if tid in site.targets else tok)
            elif kind == "rule":
                doc = "maren" if tok.startswith("H") else "lref"
                tid = f"{doc}-{tok}"
                parts.append(link(soup, tid, tok, site.targets.get(tid)) if tid in site.targets else tok)
            elif kind == "asm":
                doc = "maren" if tok.startswith("H") else "lref"
                tid = f"{doc}-{tok}"
                parts.append(link(soup, tid, tok, site.targets.get(tid), "xref asm") if tid in site.targets else tok)
            elif kind == "term":
                ab = soup.new_tag("abbr", attrs={"data-tip": TERMS[tok], "tabindex": "0"})
                ab.string = tok
                parts.append(ab)
        parts.append(text[pos:])
        for p in parts:
            if isinstance(p, str):
                if p:
                    node.insert_before(NavigableString(p))
            else:
                node.insert_before(p)
        node.extract()

    for code in soup.find_all("code"):
        tab = FILE_TABS.get(code.get_text())
        if tab and not code.find_parent("a"):
            a = soup.new_tag("a", attrs={"href": "#" + tab, "class": "xref file"})
            code.wrap(a)


def range_figure():
    """Range bands on a log scale, 1 km to 1,000,000 km, with key envelopes."""
    x0, w, decades = 40, 680, 6

    def x(km):
        return x0 + math.log10(km) / decades * w

    bands = [("K", "knife", 1, 300, .85, "on"), ("C", "close", 300, 3e3, .62, "on"),
             ("M", "medium", 3e3, 3e4, .42, "off"), ("L", "long", 3e4, 3e5, .26, "off"),
             ("S", "strategic", 3e5, 1e6, .14, "off")]
    marks = [  # label, km, lane, (bar_from_km)
        ("Casaba 2–4 km", 3, 1, 2), ("CIWS clouds 5–30 km", 17, 2, None),
        ("M-1C vs frigates", 340, 1, None), ("M-1C vs Breakwater", 2700, 2, None),
        ("Spinal vs crippled", 15000, 1, None), ("Planet lasers burn fins", 1e5, 2, None),
        ("Warp exit", 4.5e5, 1, None)]
    out = ['<figure class="range"><svg viewBox="0 0 760 118" role="img" '
           'aria-label="Range bands on a logarithmic scale from 1 km to 1,000,000 km">']
    for letter, name, a, b, op, txt in bands:
        xa, xb = x(a), x(b)
        out.append(f'<rect class="band" x="{xa:.1f}" y="60" width="{xb - xa:.1f}" height="24" '
                   f'fill-opacity="{op}"/>')
        out.append(f'<text class="band-t band-{txt}" x="{(xa + xb) / 2:.1f}" y="76.5" '
                   f'text-anchor="middle">{letter} · {name}</text>')
    # CIWS bar
    out.append(f'<rect class="bar" x="{x(5):.1f}" y="52" width="{x(30) - x(5):.1f}" height="4"/>')
    for label, km, lane, _ in marks:
        xm = x(km)
        ly = 14 if lane == 1 else 34
        out.append(f'<line class="tick-m" x1="{xm:.1f}" y1="{ly + 5}" x2="{xm:.1f}" y2="59"/>')
        out.append(f'<text class="mark-t" x="{xm:.1f}" y="{ly}" text-anchor="middle">{html.escape(label)}</text>')
    out.append(f'<line class="axis" x1="{x0}" y1="90" x2="{x0 + w}" y2="90"/>')
    for i, lab in enumerate(["1 km", "10", "100", "1,000", "10,000", "100,000", "1,000,000 km"]):
        xi = x0 + i * w / decades
        out.append(f'<line class="axis" x1="{xi:.1f}" y1="87" x2="{xi:.1f}" y2="93"/>')
        out.append(f'<text class="axis-t" x="{xi:.1f}" y="108" text-anchor="middle">{lab}</text>')
    out.append('</svg><figcaption>Range bands to scale (logarithmic), with a few envelopes from '
               'WN §2, §7 and §8 and the warp exit.</figcaption></figure>')
    return "".join(out)


CSS = r"""
/* Layout: a doctrine publication. Masthead, sticky tab strip, a contents rail
   beside a ~68ch reading column; rules set as numbered plates between hairlines. */
:root{
  --paper:#f2f4f7; --panel:#ffffff; --ink:#141922; --muted:#5a6475; --line:#d4dae3;
  --lref:#6232d4; --maren:#0c7571; --heat:#bf4f0e; --accent:var(--lref);
  --f-display:"Barlow Condensed","Arial Narrow",Arial,sans-serif;
  --f-body:"Source Serif 4",Georgia,"Times New Roman",serif;
  --f-mono:"IBM Plex Mono",ui-monospace,Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){ :root:not([data-theme="light"]){
  --paper:#0b0e13; --panel:#121720; --ink:#e3e7ed; --muted:#97a2b4; --line:#262e3b;
  --lref:#a47bff; --maren:#3cc0b9; --heat:#ff8b44; color-scheme:dark; } }
:root[data-theme="dark"]{
  --paper:#0b0e13; --panel:#121720; --ink:#e3e7ed; --muted:#97a2b4; --line:#262e3b;
  --lref:#a47bff; --maren:#3cc0b9; --heat:#ff8b44; color-scheme:dark; }
body{background:var(--paper); color:var(--ink); font:400 1rem/1.6 var(--f-body);}
.wrap{max-width:1180px; margin:0 auto; padding-inline:max(16px,3.5vw);}
.masthead{padding-block:2.2rem 1.4rem;}
.eyebrow{font:600 .8rem var(--f-display); letter-spacing:.14em; text-transform:uppercase; color:var(--muted);}
.masthead h1{font:700 clamp(2.4rem,6vw,3.6rem)/1 var(--f-display); letter-spacing:.01em; margin:.35rem 0 .7rem; text-wrap:balance;}
.lead{max-width:62ch; margin:0; font-size:1.08rem;}
.meta{margin:.8rem 0 0; font:400 .8rem var(--f-mono); color:var(--muted);}
.tabbar{position:sticky; top:env(safe-area-inset-top,0px); z-index:5; background:var(--paper); border-bottom:1px solid var(--line);}
.tabs{display:flex; gap:.2rem; overflow-x:auto; scrollbar-width:none;}
.tabs::-webkit-scrollbar{display:none;}
[role=tab]{font:600 .92rem var(--f-display); letter-spacing:.07em; text-transform:uppercase; color:var(--muted);
  background:none; border:0; border-bottom:3px solid transparent; padding:.85rem .8rem .7rem; white-space:nowrap; cursor:pointer;}
[role=tab][aria-selected=true]{color:var(--ink); border-bottom-color:var(--tab-accent,var(--ink));}
[role=tab]:focus-visible, a:focus-visible, abbr:focus-visible, summary:focus-visible, .chip:focus-visible{outline:2px solid var(--accent); outline-offset:2px; border-radius:3px;}
.side-lref{--accent:var(--lref);} .side-maren{--accent:var(--maren);} .side-plain{--accent:var(--lref);}
[data-key=lref]{--tab-accent:var(--lref);} [data-key=maren]{--tab-accent:var(--maren);}
.doc{display:grid; grid-template-columns:14.5rem minmax(0,1fr); gap:3rem; padding-block:2rem 5rem;}
.toc{position:sticky; top:calc(env(safe-area-inset-top,0px) + 3.8rem); align-self:start; max-height:calc(100vh - 5rem); overflow:auto; font:500 .9rem/1.35 var(--f-display);}
.toc summary{font:600 .8rem var(--f-display); letter-spacing:.12em; text-transform:uppercase; color:var(--muted); cursor:pointer; padding-block:.3rem;}
.toc ol{list-style:none; margin:.4rem 0 0; padding:0; display:grid; gap:.1rem;}
.toc a{display:block; padding:.28rem .5rem; color:var(--muted); text-decoration:none; border-left:2px solid var(--line);}
.toc a:hover{color:var(--ink); border-left-color:var(--accent);}
.toc .l3 a{padding-left:1.3rem; font-size:.84rem;}
.article{min-width:0; max-width:72ch;}
.wide .article{max-width:none;}
.doc-title{font:700 clamp(1.8rem,4vw,2.5rem)/1.05 var(--f-display); margin:0 0 1rem; text-wrap:balance;}
.doc-title .side{display:block; font:600 .8rem var(--f-display); letter-spacing:.14em; text-transform:uppercase; color:var(--accent); margin-bottom:.4rem;}
.article h2{font:700 1.85rem/1.1 var(--f-display); margin:3.2rem 0 .9rem; text-wrap:balance; letter-spacing:.005em;}
.article h3{font:600 1.3rem/1.2 var(--f-display); margin:2.2rem 0 .6rem; text-wrap:balance;}
.article h2 .num, .article h3 .num{color:var(--accent); margin-right:.35em; font-variant-numeric:tabular-nums;}
.article p, .article li{hyphens:auto;}
.article ul, .article ol{padding-left:1.3rem;}
.article li{margin:.25rem 0;}
.article li > ul{margin:.2rem 0;}
.article hr{border:0; border-top:1px solid var(--line); margin:2.6rem 0;}
.article a{color:var(--accent);}
strong{font-weight:600;}
code{font:400 .86em var(--f-mono); background:color-mix(in srgb, var(--ink) 7%, transparent); padding:.05em .3em; border-radius:3px; overflow-wrap:anywhere;}
.callout{border:1px solid var(--line); background:var(--panel); padding:.75rem 1rem; border-radius:6px; font-size:.95rem;}
a.xref{color:var(--accent); text-decoration:none; border-bottom:1px solid color-mix(in srgb, var(--accent) 45%, transparent); font-variant-numeric:tabular-nums;}
a.xref:hover{border-bottom-color:var(--accent);}
a.xref.asm{font:500 .82em var(--f-mono);}
a.file{border:0;}
abbr{text-decoration:underline dotted color-mix(in srgb, var(--muted) 60%, transparent); text-underline-offset:.18em; cursor:help;}
.chip{display:inline-block; font:500 .7rem/1.5 var(--f-mono); letter-spacing:.02em; padding:0 .38rem; border-radius:3px; vertical-align:.12em;
  border:1px solid color-mix(in srgb, var(--accent) 40%, transparent); color:var(--accent); cursor:help;}
.chip-model{border-color:color-mix(in srgb, var(--muted) 45%, transparent); color:var(--muted);}
.table-wrap{overflow-x:auto; margin:1.2rem 0; border:1px solid var(--line); border-radius:6px; background:var(--panel);}
table{border-collapse:collapse; width:100%; font:400 .9rem/1.45 var(--f-body); font-variant-numeric:tabular-nums;}
th{font:600 .76rem var(--f-display); letter-spacing:.08em; text-transform:uppercase; color:var(--muted); text-align:left; padding:.6rem .75rem; border-bottom:1px solid var(--line); vertical-align:bottom;}
td{padding:.6rem .75rem; border-top:1px solid var(--line); vertical-align:top;}
tr:first-child td{border-top:0;}
tr:target td, .rule:target, .flash, tr.flash td{background:color-mix(in srgb, var(--accent) 12%, transparent);}
.rules{margin:1.2rem 0 2rem; border-top:1px solid var(--line);}
.rule{display:grid; grid-template-columns:3.6rem minmax(0,1fr); gap:.2rem 1rem; padding:1.1rem .5rem 1.2rem 0; border-bottom:1px solid var(--line); scroll-margin-top:5rem;}
.rule-id{font:700 1.5rem/1.1 var(--f-display); color:var(--accent); font-variant-numeric:tabular-nums; padding-top:.1rem;}
.rule h4{font:600 1.22rem/1.2 var(--f-display); margin:0 0 .35rem; letter-spacing:.01em;}
.rule-detail{margin:0;}
.rule-meta{display:grid; grid-template-columns:max-content minmax(0,1fr); gap:.3rem .9rem; margin:.7rem 0 0; font-size:.86rem; color:var(--muted);}
.rule-meta dt{font:600 .72rem/1.9 var(--f-display); letter-spacing:.08em; text-transform:uppercase;}
.rule-meta dd{margin:0;}
[id]{scroll-margin-top:5rem;}
figure.range{margin:1.4rem 0; padding:1rem 1rem .6rem; border:1px solid var(--line); border-radius:6px; background:var(--panel); overflow-x:auto;}
figure.range svg{display:block; width:100%; min-width:560px; height:auto;}
figure.range figcaption{font-size:.82rem; color:var(--muted); margin-top:.4rem;}
.band{fill:var(--lref);} .bar{fill:var(--heat);}
.band-t{font:600 11px var(--f-display); letter-spacing:.06em; text-transform:uppercase;}
.band-on{fill:var(--paper);} .band-off{fill:var(--ink);}
.mark-t{font:500 11.5px var(--f-display); fill:var(--ink);}
.tick-m{stroke:var(--muted); stroke-width:1; stroke-dasharray:2 2;}
.axis{stroke:var(--muted); stroke-width:1;} .axis-t{font:400 10.5px var(--f-mono); fill:var(--muted);}
#tip{position:fixed; z-index:20; max-width:min(22rem, calc(100vw - 32px)); background:var(--panel); color:var(--ink); border:1px solid var(--line);
  border-radius:6px; padding:.6rem .75rem; font:400 .88rem/1.45 var(--f-body); box-shadow:0 6px 24px color-mix(in srgb, var(--ink) 18%, transparent);}
#tip a{display:inline-block; margin-top:.35rem; font:600 .78rem var(--f-display); letter-spacing:.08em; text-transform:uppercase; color:var(--accent);}
footer{border-top:1px solid var(--line); padding-block:1.4rem 2.4rem; color:var(--muted); font-size:.85rem;}
@media (max-width: 900px){
  .doc{grid-template-columns:minmax(0,1fr); gap:1rem; padding-block:1.2rem 4rem;}
  .toc{position:static; max-height:none; border:1px solid var(--line); border-radius:6px; padding:.4rem .8rem; background:var(--panel);}
}
@media (max-width: 640px){
  .article{font-size:1rem;}
  table.stack thead{display:none;}
  table.stack, table.stack tbody, table.stack tr, table.stack td{display:block; width:100%;}
  table.stack tr{padding:.7rem .85rem; border-top:1px solid var(--line);}
  table.stack tr:first-child{border-top:0;}
  table.stack td{display:grid; grid-template-columns:minmax(6.5rem,34%) minmax(0,1fr); gap:.7rem; border:0; padding:.18rem 0;}
  table.stack td::before{content:attr(data-label); font:600 .7rem/1.9 var(--f-display); letter-spacing:.08em; text-transform:uppercase; color:var(--muted);}
  .rule{grid-template-columns:minmax(0,1fr);}
  .rule-meta{grid-template-columns:minmax(0,1fr);}
}
@media (prefers-reduced-motion: reduce){ *{scroll-behavior:auto !important;} }
"""

JS = r"""
(function(){
  var tabs = Array.prototype.slice.call(document.querySelectorAll('[role=tab]'));
  var panels = Array.prototype.slice.call(document.querySelectorAll('[role=tabpanel]'));
  var tip = document.getElementById('tip');
  var touch = window.matchMedia('(hover: none)').matches;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function show(key){
    tabs.forEach(function(t){ var on = t.getAttribute('data-key') === key;
      t.setAttribute('aria-selected', on ? 'true' : 'false'); t.tabIndex = on ? 0 : -1; });
    panels.forEach(function(p){ p.hidden = p.getAttribute('data-key') !== key; });
    try { localStorage.setItem('tidebreak-tab', key); } catch (e) {}
  }
  function go(id){
    var el = document.getElementById(id); if (!el) return;
    var panel = el.closest('[role=tabpanel]');
    if (panel) show(panel.getAttribute('data-key'));
    if (el.getAttribute('role') === 'tabpanel') { window.scrollTo(0, 0); }
    else {
      el.scrollIntoView({behavior: reduce ? 'auto' : 'smooth', block: 'start'});
      el.classList.add('flash'); setTimeout(function(){ el.classList.remove('flash'); }, 1600);
    }
    try { history.replaceState(null, '', '#' + id); } catch (e) {}
  }
  tabs.forEach(function(t, i){
    t.addEventListener('click', function(){ go(t.getAttribute('data-key')); });
    t.addEventListener('keydown', function(e){
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (!d) return;
      var n = tabs[(i + d + tabs.length) % tabs.length]; n.focus(); go(n.getAttribute('data-key'));
    });
  });
  function hideTip(){ tip.hidden = true; tip.removeAttribute('data-for'); }
  function showTip(el){
    var text = el.getAttribute('data-tip'); if (!text) return;
    tip.textContent = text;
    var href = el.getAttribute('href');
    if (href && touch){ var a = document.createElement('a'); a.href = href; a.textContent = 'Go there';
      tip.appendChild(document.createElement('br')); tip.appendChild(a); }
    tip.hidden = false;
    var r = el.getBoundingClientRect(), tw = tip.offsetWidth, th = tip.offsetHeight;
    var left = Math.min(Math.max(16, r.left), window.innerWidth - tw - 16);
    var top = r.bottom + 8; if (top + th > window.innerHeight - 12) top = r.top - th - 8;
    tip.style.left = left + 'px'; tip.style.top = Math.max(12, top) + 'px';
    tip.setAttribute('data-for', href || text);
  }
  document.addEventListener('click', function(e){
    var inTip = e.target.closest('#tip');
    var a = e.target.closest('a[href^="#"]');
    var tipEl = e.target.closest('[data-tip]');
    if (touch && tipEl && !inTip){
      var key = tipEl.getAttribute('href') || tipEl.getAttribute('data-tip');
      if (tip.hidden || tip.getAttribute('data-for') !== key){ e.preventDefault(); showTip(tipEl); return; }
    }
    if (a){ e.preventDefault(); hideTip(); go(a.getAttribute('href').slice(1)); return; }
    if (!inTip) hideTip();
  });
  if (!touch){
    var timer;
    document.addEventListener('mouseover', function(e){
      var el = e.target.closest('[data-tip]'); if (!el) return;
      clearTimeout(timer); timer = setTimeout(function(){ showTip(el); }, 180);
    });
    document.addEventListener('mouseout', function(e){
      if (e.target.closest('[data-tip]')){ clearTimeout(timer); hideTip(); }
    });
    document.addEventListener('focusin', function(e){ var el = e.target.closest('[data-tip]'); if (el) showTip(el); });
    document.addEventListener('focusout', hideTip);
  }
  window.addEventListener('scroll', function(){ if (!tip.hidden) hideTip(); }, {passive: true});
  if (window.matchMedia('(max-width: 900px)').matches){
    Array.prototype.forEach.call(document.querySelectorAll('details.toc'), function(d){ d.open = false; });
  }
  var start = (location.hash || '').slice(1), stored = null;
  try { stored = localStorage.getItem('tidebreak-tab'); } catch (e) {}
  if (start && document.getElementById(start)) go(start);
  else if (stored && document.getElementById(stored)) show(stored);
})();
"""


def build():
    site = Site()
    parsed = []
    for key, tab, src, side, bare, wide in DOCS:
        soup = parse((ROOT / src).read_text())
        title, toc = first_pass(key, soup, site)
        parsed.append((key, tab, src, side, bare, wide, soup, title, toc))
    # rule tips need the rule titles, which exist only after every first pass
    panels = []
    for key, tab, src, side, bare, wide, soup, title, toc in parsed:
        second_pass(key, bare, soup, site)
        if key == "lref":
            h = soup.find(id="lref-range-bands-numbers-from-wn-1-3-and-7-8") or \
                next((x for x in soup.find_all("h3") if x.get_text().startswith("Range bands")), None)
            if h:
                slot = soup.new_tag("div", attrs={"id": "range-fig-slot"})
                h.insert_after(slot)
        toc_html = "".join(
            f'<li class="l{lvl[1]}"><a href="#{hid}">{html.escape(text)}</a></li>'
            for lvl, hid, text in toc if lvl in ("h2", "h3"))
        side_label = {"lref": "Long Range Expeditionary Forces", "maren": "The Maren Compact",
                      "plain": "Operation Tidebreak"}[side]
        panels.append(
            f'<section id="{key}" class="doc-panel side-{side}{" wide" if wide else ""}" role="tabpanel" '
            f'data-key="{key}" aria-labelledby="tab-{key}"{"" if key == "lref" else " hidden"}>'
            f'<div class="wrap doc"><details class="toc" open><summary>Contents</summary>'
            f'<nav aria-label="Contents: {html.escape(tab)}"><ol>{toc_html}</ol></nav></details>'
            f'<div class="article"><h2 class="doc-title"><span class="side">{side_label}</span>'
            f'{html.escape(title)}</h2>{str(soup).replace(chr(60) + "div id=" + chr(34) + "range-fig-slot" + chr(34) + "></div>", range_figure())}'
            f'<p class="source">Source: <code>{src}</code></p></div></div></section>')

    tabs = "".join(
        f'<button role="tab" id="tab-{k}" data-key="{k}" aria-controls="{k}" '
        f'aria-selected="{"true" if k == "lref" else "false"}" tabindex="{0 if k == "lref" else -1}">'
        f'{html.escape(t)}</button>' for k, t, *_ in DOCS)

    head = f"""<title>Tidebreak Doctrines</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap">
<style>{CSS}</style>
"""
    body = f"""<header class="wrap masthead">
  <div class="eyebrow">Operation Tidebreak · phase 1</div>
  <h1>Tidebreak doctrines</h1>
  <p class="lead">How the LREF task group fights its way into the Maren system, and how the Maren Compact defends it. Revised with your sign-off answers, and waiting for your OK before the storyboard starts.</p>
  <p class="meta">Reading edition of the Markdown in doctrine/ · tap any rule, assumption or term for a preview</p>
</header>
<div class="tabbar"><div class="wrap"><div class="tabs" role="tablist" aria-label="Documents">{tabs}</div></div></div>
<main>{"".join(panels)}</main>
<footer class="wrap">Built from the Markdown files on the branch by <code>doctrine/build_reading.py</code>. The Markdown stays the source of truth.</footer>
<div id="tip" role="tooltip" hidden></div>
<script>{JS}</script>
"""
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
                   "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
                   + head + "</head>\n<body>\n" + body + "</body>\n</html>\n")
    if "--fragment" in sys.argv:
        frag = pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1])
        frag.parent.mkdir(parents=True, exist_ok=True)
        frag.write_text(head + body)
    print(f"wrote {OUT.relative_to(ROOT)} ({OUT.stat().st_size:,} bytes); "
          f"{len(site.targets)} link targets")


if __name__ == "__main__":
    build()
