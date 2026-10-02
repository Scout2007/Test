#!/usr/bin/env python3
"""Render miniseries/SERIES_PLAN.md as a reading page for review.

    pip install markdown-it-py beautifulsoup4
    python3 miniseries/build_plan_page.py [--fragment PATH]

Writes miniseries/plan.html (a full page). --fragment also writes the page without <html>/<head>/<body>
for the artifact viewer. The look follows the storyboard page: the same faces, colours and theme tokens.
"""
import html
import pathlib
import re
import sys

from bs4 import BeautifulSoup
from markdown_it import MarkdownIt

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "SERIES_PLAN.md"

CSS = """
/* Layout: one reading column with a section index; tables scroll inside their own frame. */
:root{
  --bg:#f3f4f7; --panel:#ffffff; --ink:#12161d; --muted:#5a6475; --line:#d8dde5;
  --lref:#6232d4; --clock:#0e7c70; --heat:#c2510d; --code:#eef0f5;
  --f-display:"Barlow Condensed","Arial Narrow",sans-serif;
  --f-body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#07090c; --panel:#0e1218; --ink:#e4e8ee; --muted:#8a95a6; --line:#1f2631;
  --lref:#a47bff; --clock:#6fd3c4; --heat:#ff9a4a; --code:#151b24; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#07090c; --panel:#0e1218; --ink:#e4e8ee; --muted:#8a95a6; --line:#1f2631;
  --lref:#a47bff; --clock:#6fd3c4; --heat:#ff9a4a; --code:#151b24; color-scheme:dark}
body{background:var(--bg); color:var(--ink); font:16px/1.6 var(--f-body); padding-inline:16px; padding-block:24px 64px}
.wrap{max-width:68rem; margin:0 auto; display:grid; grid-template-columns:minmax(0,1fr); gap:24px}
@media (min-width:980px){.wrap{grid-template-columns:13rem minmax(0,1fr)}}
header.top{grid-column:1/-1; display:grid; gap:8px; padding-block:8px 16px; border-bottom:1px solid var(--line)}
.eyebrow{font:600 12px/1.4 var(--f-mono); letter-spacing:.08em; text-transform:uppercase; color:var(--clock)}
h1{font:700 clamp(2rem,5vw,3.2rem)/1.05 var(--f-display); letter-spacing:.01em; margin:0; text-wrap:balance}
.lede{color:var(--muted); max-width:62ch; margin:0}
nav.toc{font:500 13px/1.5 var(--f-mono); color:var(--muted); align-self:start; display:grid; gap:4px}
@media (min-width:980px){nav.toc{position:sticky; top:calc(env(safe-area-inset-top, 0px) + 16px)}}
nav.toc a{color:inherit; text-decoration:none; padding:2px 0; border-left:2px solid transparent; padding-left:8px}
nav.toc a:hover, nav.toc a:focus-visible{color:var(--ink); border-left-color:var(--lref); outline:none}
nav.toc .sub{padding-left:20px; font-size:12px}
main{min-width:0; display:grid; gap:4px}
main h2{font:700 1.9rem/1.15 var(--f-display); letter-spacing:.02em; margin:32px 0 4px; padding-top:12px; border-top:2px solid var(--ink); text-wrap:balance}
main h3{font:700 1.35rem/1.2 var(--f-display); letter-spacing:.02em; margin:24px 0 2px; text-wrap:balance}
main h3.ep{color:var(--lref)}
main h4{font:600 12px/1.4 var(--f-mono); letter-spacing:.08em; text-transform:uppercase; color:var(--muted); margin:16px 0 0}
main p, main li{max-width:68ch}
main p{margin:6px 0}
main ul, main ol{margin:6px 0; padding-left:1.4em; display:grid; gap:3px}
main strong{font-weight:600}
main code{font:13px var(--f-mono); background:var(--code); padding:1px 5px; border-radius:3px}
main a{color:var(--lref)}
.tbl{overflow-x:auto; margin:10px 0; border:1px solid var(--line); border-radius:6px; background:var(--panel)}
.tbl table{border-collapse:collapse; width:100%; font-size:14px; line-height:1.45}
.tbl th{font:600 11px/1.3 var(--f-mono); letter-spacing:.07em; text-transform:uppercase; color:var(--muted); text-align:left; padding:10px 12px; border-bottom:1px solid var(--line); white-space:nowrap}
.tbl td{padding:9px 12px; border-top:1px solid var(--line); vertical-align:top; font-variant-numeric:tabular-nums}
.tbl tr:first-child td{border-top:0}
main blockquote{margin:10px 0; padding:4px 14px; border-left:3px solid var(--heat); color:var(--muted)}
footer{grid-column:1/-1; color:var(--muted); font:12px var(--f-mono); border-top:1px solid var(--line); padding-top:12px}
@media (prefers-reduced-motion: reduce){*{scroll-behavior:auto}}
"""


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60] or "section"


def build():
    md = MarkdownIt("commonmark", {"html": False, "typographer": False}).enable("table").enable("strikethrough")
    soup = BeautifulSoup(md.render(SRC.read_text()), "html.parser")
    h1 = soup.find("h1")
    title_html = h1.decode_contents() if h1 else "Pre-release mini-series"
    if h1:
        h1.decompose()
    toc, used = [], set()
    for h in soup.find_all(["h2", "h3"]):
        sid = slug(h.get_text())
        while sid in used:
            sid += "-x"
        used.add(sid)
        h["id"] = sid
        if h.name == "h3" and h.get_text().startswith("Ep "):
            h["class"] = ["ep"]
        if h.name == "h2" or h.get("class") == ["ep"]:
            label = h.get_text().split(" (")[0]
            cls = ' class="sub"' if h.name == "h3" else ""
            toc.append(f'<a href="#{sid}"{cls}>{html.escape(label)}</a>')
    for t in soup.find_all("table"):
        t.wrap(soup.new_tag("div", attrs={"class": "tbl"}))
    head = ('<title>Tidebreak Mini-Series</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700'
            '&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;600&display=swap">\n'
            f"<style>{CSS}</style>\n")
    body = (f'<div class="wrap">\n<header class="top"><div class="eyebrow">Operation Tidebreak · pre-release mini-series · '
            f'plan for sign-off</div><h1>{title_html}</h1><p class="lede">Nine short in-world films that count down to the '
            f'film, one per main weapon system or ship class, each in its own style. Generated from '
            f'<code>miniseries/SERIES_PLAN.md</code>.</p></header>\n'
            f'<nav class="toc" aria-label="Sections">{"".join(toc)}</nav>\n<main>{soup.decode()}</main>\n'
            f'<footer>Generated by miniseries/build_plan_page.py from miniseries/SERIES_PLAN.md.</footer>\n</div>\n')
    return head, body


def main():
    head, body = build()
    page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            + head + "</head>\n<body>\n" + body + "</body>\n</html>\n")
    (ROOT / "plan.html").write_text(page)
    if "--fragment" in sys.argv:
        frag = pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1])
        frag.parent.mkdir(parents=True, exist_ok=True)
        frag.write_text(head + body)
    print(f"wrote {ROOT / 'plan.html'} ({len(page):,} bytes)")


if __name__ == "__main__":
    main()
