#!/usr/bin/env python3
"""Build the mini-series picker: compare each episode's three options, choose a base, borrow and cut shots, add notes.

    pip install markdown-it-py
    python3 miniseries/build_picker.py [--fragment PATH]

Reads miniseries/options/ep*.md (the layout in options/BRIEF.md §7) and writes miniseries/picker.html (a full page).
--fragment also writes the page without <html>/<head>/<body> for the artifact viewer. The page saves picks to the
artifact's db (collection `picks`, one document per episode, each with a plain-text `readable` field for Claude);
without db it keeps them in the browser and offers a copy-as-text.
"""
import html
import json
import pathlib
import re
import sys

from markdown_it import MarkdownIt

ROOT = pathlib.Path(__file__).resolve().parent
SRC = ROOT / "options"
MD = MarkdownIt("commonmark", {"html": False, "typographer": False}).enable("table").enable("strikethrough")
QUOTE = re.compile(r"[\"“]([^\"”]+)[\"”]")
FIELDS = ("Logline", "The idea", "Look and sound", "Storyboard", "Words", "Built from", "Render")


def inline(s):
    return MD.renderInline(s.strip())


def plain(s):
    return re.sub(r"\s+", " ", re.sub(r"[*_`]", "", s)).strip()


def paragraphs(block):
    paras, cur = [], []
    for line in block.splitlines():
        if line.startswith("|") or not line.strip() or set(line.strip()) <= set("-*_"):
            if cur:
                paras.append(" ".join(cur))
            cur = []
        else:
            cur.append(line.strip())
    if cur:
        paras.append(" ".join(cur))
    return "".join(f"<p>{inline(p)}</p>" for p in paras)


def duration(t):
    m = re.match(r"\s*(\d+(?:\.\d+)?)\s*[–-]\s*(\d+(?:\.\d+)?)", t)
    if m:
        return round(float(m.group(2)) - float(m.group(1)), 1)
    m = re.match(r"\s*(\d+(?:\.\d+)?)", t)
    return float(m.group(1)) if m else 0


def parse_option(head, body):
    m = re.match(r"Option ([ABC])\s*[·:]\s*\*(.+?)\*:?\s*(.*?)\s*\((\d+)\s*s\)\s*$", head.strip())
    if not m:
        sys.exit(f"can't read option heading: {head!r}")
    letter, title, medium, rt = m.groups()
    chunks = re.split(r"^\*\*(" + "|".join(FIELDS) + r")\.\*\*", body, flags=re.M)
    f = {chunks[i]: chunks[i + 1].strip() for i in range(1, len(chunks) - 1, 2)}
    missing = [k for k in FIELDS if k not in f]
    if missing:
        sys.exit(f"option {letter} ({title}) is missing {missing}")
    shots = []
    for row in f["Storyboard"].splitlines():
        if not row.startswith("|") or set(row) <= set("|-: "):
            continue
        cells = [c.strip() for c in row.strip().strip("|").split("|")]
        if cells[0] in ("#", "Shot") or len(cells) < 4:
            continue
        n, t, pic, snd = cells[0], cells[1], cells[2], " | ".join(cells[3:])
        said = QUOTE.findall(snd)
        shots.append({"n": n, "t": t, "d": duration(t), "pic": inline(pic), "snd": inline(snd),
                      "pt": plain(pic), "st": plain(snd), "w": sum(len(s.split()) for s in said),
                      "tag": bool(re.match(r"\*\*Tag", pic))})
    look = [inline(li[2:]) for li in f["Look and sound"].splitlines() if li.startswith("- ")]
    look_t = [plain(li[2:]) for li in f["Look and sound"].splitlines() if li.startswith("- ")]
    # the writers bold the total ("**~6.8 h**"); a few write "about 7 h plus the tag"
    hours = (re.search(r"\*\*~?(\d+(?:\.\d+)?)\s*h", f["Render"]) or re.search(r"about (\d+(?:\.\d+)?) h\b", f["Render"])
             or re.search(r"(\d+(?:\.\d+)?)\s*h\b", f["Render"]))
    return {"L": letter, "title": title, "medium": medium, "rt": int(rt), "words": sum(s["w"] for s in shots),
            "logline": inline(f["Logline"]), "idea": inline(f["The idea"]), "look": look, "lookT": look_t,
            "shots": shots, "built": inline(f["Built from"]), "render": inline(f["Render"]),
            "hours": float(hours.group(1)) if hours else None}


def parse_episode(path):
    text = path.read_text()
    first, *parts = re.split(r"^## ", text, flags=re.M)
    h1 = re.search(r"^# Ep (\d+) · (.+?)\s*\((T[−-]\d+)[^)]*\)", first, re.M)
    if not h1:
        sys.exit(f"{path.name}: can't read the title line")
    intro = paragraphs(first[h1.end():])
    opts, rec = [], ""
    for part in parts:
        head, _, body = part.partition("\n")
        if head.startswith("Option"):
            opts.append(parse_option(head, body))
        elif head.startswith("Recommendation"):
            rec = paragraphs(body)
    if [o["L"] for o in opts] != ["A", "B", "C"]:
        sys.exit(f"{path.name}: expected options A, B and C")
    return {"n": int(h1.group(1)), "subject": h1.group(2), "tag": h1.group(3), "intro": intro, "rec": rec, "opts": opts}


CSS = """
/* Layout: a sticky episode bar over one episode at a time: the merge card, then the three options side by side
   (one at a time, by tab, below 1100px). Borrowed = teal, cut = orange, base = violet. */
:root{
  --bg:#f3f4f7; --panel:#ffffff; --ink:#12161d; --muted:#5a6475; --line:#d8dde5;
  --lref:#6232d4; --clock:#0e7c70; --heat:#c2510d; --code:#eef0f5;
  --lref-t:#ece6fb; --clock-t:#dcf1ee; --heat-t:#fbe9de;
  --f-display:"Barlow Condensed","Arial Narrow",sans-serif;
  --f-body:"IBM Plex Sans",system-ui,-apple-system,"Segoe UI",sans-serif;
  --f-mono:"IBM Plex Mono",ui-monospace,"SFMono-Regular",Menlo,monospace;
}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){
  --bg:#07090c; --panel:#0e1218; --ink:#e4e8ee; --muted:#8a95a6; --line:#1f2631;
  --lref:#a47bff; --clock:#6fd3c4; --heat:#ff9a4a; --code:#151b24;
  --lref-t:#211a38; --clock-t:#0f2a27; --heat-t:#33200f; color-scheme:dark}}
:root[data-theme="dark"]{
  --bg:#07090c; --panel:#0e1218; --ink:#e4e8ee; --muted:#8a95a6; --line:#1f2631;
  --lref:#a47bff; --clock:#6fd3c4; --heat:#ff9a4a; --code:#151b24;
  --lref-t:#211a38; --clock-t:#0f2a27; --heat-t:#33200f; color-scheme:dark}
body{background:var(--bg); color:var(--ink); font:15px/1.55 var(--f-body); padding-inline:16px; padding-block:20px 64px}
.wrap{max-width:96rem; margin:0 auto; display:grid; gap:18px}
button{font:inherit; color:inherit}
:focus-visible{outline:2px solid var(--lref); outline-offset:2px}
header.top{display:grid; gap:8px; padding-bottom:6px}
.eyebrow{font:600 12px/1.4 var(--f-mono); letter-spacing:.08em; text-transform:uppercase; color:var(--clock)}
h1{font:700 clamp(2rem,5vw,3rem)/1.05 var(--f-display); letter-spacing:.01em; margin:0; text-wrap:balance}
.steps{margin:0; padding-left:1.3em; display:grid; gap:2px; max-width:70ch; color:var(--muted)}
.steps strong{color:var(--ink); font-weight:600}
.bar{position:sticky; top:env(safe-area-inset-top,0px); z-index:5; background:var(--bg); padding-block:8px;
  border-bottom:1px solid var(--line); display:flex; gap:10px; align-items:center; flex-wrap:wrap}
.chips{display:flex; gap:6px; overflow-x:auto; min-width:0; flex:1 1 30rem; padding-bottom:2px}
.chip{border:1px solid var(--line); background:var(--panel); border-radius:999px; padding:4px 11px; cursor:pointer;
  font:600 13px/1.3 var(--f-mono); white-space:nowrap; display:flex; gap:6px; align-items:center}
.chip .st{font-weight:500; color:var(--muted)}
.chip.on{border-color:var(--lref); box-shadow:inset 0 0 0 1px var(--lref)}
.chip.done .st{color:var(--lref)}
.save{font:500 12px/1.3 var(--f-mono); color:var(--muted); padding:4px 0}
.save.ok{color:var(--clock)} .save.bad{color:var(--heat)}
h2{font:700 1.9rem/1.1 var(--f-display); margin:6px 0 0; text-wrap:balance}
h2 .t{font:600 13px var(--f-mono); color:var(--muted); letter-spacing:.06em; margin-left:8px}
.intro p{margin:4px 0; max-width:80ch}
details{max-width:80ch} summary{cursor:pointer; color:var(--muted); font:600 13px var(--f-mono)}
details p{margin:6px 0}
.mine{background:var(--panel); border:1px solid var(--line); border-left:3px solid var(--lref); border-radius:8px;
  padding:14px 16px; display:grid; gap:10px}
.mine h3{font:700 1.25rem/1.2 var(--f-display); margin:0}
.bases{display:flex; flex-wrap:wrap; gap:6px}
.base{border:1px solid var(--line); background:var(--bg); border-radius:6px; padding:6px 10px; cursor:pointer; text-align:left}
.base[aria-pressed="true"]{border-color:var(--lref); background:var(--lref-t)}
.base b{font-family:var(--f-mono); margin-right:6px; color:var(--lref)}
.stats{font:500 13px var(--f-mono); color:var(--muted); font-variant-numeric:tabular-nums}
.stats strong{color:var(--ink)}
.picks{display:grid; gap:4px; margin:0; padding:0; list-style:none}
.picks li{display:flex; gap:8px; align-items:baseline; font-size:14px}
.picks .k{font:600 12px var(--f-mono); white-space:nowrap}
.picks .b .k{color:var(--clock)} .picks .c .k{color:var(--heat)}
.picks .x{border:0; background:none; cursor:pointer; color:var(--muted); padding:0 4px; font-size:16px; line-height:1}
.picks .ex{color:var(--muted); min-width:0; overflow-wrap:anywhere}
label.nl{font:600 12px var(--f-mono); color:var(--muted); letter-spacing:.04em}
textarea{width:100%; box-sizing:border-box; min-height:4.5em; resize:vertical; border:1px solid var(--line); border-radius:6px;
  background:var(--bg); color:var(--ink); font:14px/1.5 var(--f-body); padding:8px 10px}
.hint{font-size:13px; color:var(--muted); margin:0}
.tabs{display:none; gap:6px}
.tab{flex:1; border:1px solid var(--line); background:var(--panel); border-radius:6px; padding:6px; cursor:pointer;
  font:600 13px var(--f-mono)}
.tab.on{border-color:var(--ink)} .tab.isbase{color:var(--lref)}
.cols{display:grid; grid-template-columns:repeat(3,minmax(0,1fr)); gap:14px; align-items:start}
@media (max-width:1099px){
  .tabs{display:flex}
  .cols{grid-template-columns:minmax(0,1fr)}
  .cols[data-show="A"] .col:not([data-l="A"]), .cols[data-show="B"] .col:not([data-l="B"]),
  .cols[data-show="C"] .col:not([data-l="C"]){display:none}
}
.col{background:var(--panel); border:1px solid var(--line); border-radius:8px; padding:14px; display:grid; gap:10px; min-width:0}
.col.isbase{border-color:var(--lref); box-shadow:inset 0 3px 0 var(--lref)}
.col h3{font:700 1.4rem/1.15 var(--f-display); margin:0; text-wrap:balance}
.col h3 .l{font:700 13px var(--f-mono); color:var(--lref); margin-right:8px; vertical-align:middle}
.med{color:var(--muted); font-size:14px; margin:0}
.use{justify-self:start; border:1px solid var(--lref); color:var(--lref); background:none; border-radius:6px;
  padding:5px 12px; cursor:pointer; font:600 13px var(--f-mono)}
.use[aria-pressed="true"]{background:var(--lref); color:var(--panel)}
.col h4{font:600 11px/1.3 var(--f-mono); letter-spacing:.08em; text-transform:uppercase; color:var(--muted); margin:6px 0 0}
.col p{margin:0}
.shots, .look{display:grid; gap:6px; margin:0; padding:0; list-style:none}
.shot{border-top:1px solid var(--line); padding-top:6px; display:grid; gap:4px}
.shot .no{font:600 12px var(--f-mono); color:var(--muted); font-variant-numeric:tabular-nums}
.tg{display:block; width:100%; text-align:left; border:1px solid transparent; border-left:3px solid var(--line);
  background:none; border-radius:4px; padding:5px 8px; cursor:pointer; position:relative; font-size:14px; line-height:1.5}
.tg:hover{border-color:var(--line); border-left-color:var(--muted)}
.tg .lab{font:600 10.5px var(--f-mono); letter-spacing:.06em; text-transform:uppercase; color:var(--muted); display:block}
.tg.b{background:var(--clock-t); border-left-color:var(--clock)}
.tg.b .lab{color:var(--clock)}
.tg.c{background:var(--heat-t); border-left-color:var(--heat)}
.tg.c .body{text-decoration:line-through; text-decoration-color:var(--heat); color:var(--muted)}
.tg.c .lab{color:var(--heat)}
.tg[disabled]{cursor:default; opacity:.75; border-left-style:dashed}
.small{font-size:13px; color:var(--muted)}
.summary table{border-collapse:collapse; width:100%; font-size:14px}
.summary .tbl{overflow-x:auto; border:1px solid var(--line); border-radius:8px; background:var(--panel)}
.summary th{font:600 11px/1.3 var(--f-mono); letter-spacing:.07em; text-transform:uppercase; color:var(--muted);
  text-align:left; padding:9px 10px; border-bottom:1px solid var(--line); white-space:nowrap}
.summary td{padding:8px 10px; border-top:1px solid var(--line); vertical-align:top; font-variant-numeric:tabular-nums}
.summary tr:first-child td{border-top:0}
.summary tfoot td{font-weight:600; border-top:2px solid var(--line)}
.btn{border:1px solid var(--ink); background:var(--ink); color:var(--bg); border-radius:6px; padding:7px 14px; cursor:pointer;
  font:600 13px var(--f-mono)}
.copybox{width:100%; min-height:12em; font:12.5px/1.5 var(--f-mono)}
.toast{position:fixed; left:50%; transform:translateX(-50%); bottom:calc(env(safe-area-inset-bottom,0px) + 18px);
  background:var(--ink); color:var(--bg); padding:8px 14px; border-radius:6px; font:600 13px var(--f-mono); z-index:9}
footer{color:var(--muted); font:12px var(--f-mono); border-top:1px solid var(--line); padding-top:12px}
@media (prefers-reduced-motion: reduce){*{scroll-behavior:auto; transition:none}}
"""

JS = r"""
(function () {
  "use strict";
  const DATA = JSON.parse(document.getElementById("picker-data").textContent);
  const EPS = DATA.eps;
  const KEYS = EPS.map(e => "ep" + e.n);
  const byKey = Object.fromEntries(EPS.map(e => ["ep" + e.n, e]));
  const LS = "tidebreak-picker-v1";
  const blank = () => ({ base: null, sel: {}, note: "" });
  const state = Object.fromEntries(KEYS.map(k => [k, blank()]));
  let view = "ep1";
  const tabs = {};
  let db = null, mode = "connecting", writable = true;
  const pending = {}, inflight = {}, again = {}, timers = {};
  const $ = s => document.querySelector(s);

  function norm(d) {
    const out = blank();
    if (!d || typeof d !== "object") return out;
    if (["A", "B", "C"].includes(d.base)) out.base = d.base;
    if (d.sel && typeof d.sel === "object")
      for (const [id, v] of Object.entries(d.sel)) if (/^[ABC](\d+[pw]|l\d+)$/.test(id) && (v === "b" || v === "c")) out.sel[id] = v;
    if (typeof d.note === "string") out.note = d.note.slice(0, 4000);
    return out;
  }
  const isEmpty = s => !s.base && !Object.keys(s.sel).length && !s.note.trim();

  function lsLoad() {
    try {
      const s = JSON.parse(localStorage.getItem(LS) || "null");
      if (s && s.picks) for (const k of KEYS) if (s.picks[k]) state[k] = norm(s.picks[k]);
      if (s && (KEYS.includes(s.view) || s.view === "summary")) view = s.view;
      if (s && s.tabs) Object.assign(tabs, s.tabs);
    } catch (e) { /* storage unavailable: start empty */ }
  }
  function lsSave() {
    try { localStorage.setItem(LS, JSON.stringify({ picks: state, view, tabs })); } catch (e) { /* ignore */ }
  }

  // ---- what an element is, and what the picks add up to
  function opt(ep, L) { return ep.opts.find(o => o.L === L); }
  function element(ep, id) {
    const o = opt(ep, id[0]);
    if (id[1] === "l") { const i = +id.slice(2); return { o, kind: "look", label: id[0] + " · look " + (i + 1), text: o.lookT[i] || "" }; }
    const n = id.slice(1, -1), part = id.slice(-1), s = o.shots.find(x => x.n === n);
    if (!s) return null;
    return { o, s, kind: part, label: id[0] + " · shot " + n + " · " + (part === "p" ? "picture" : "sound"), text: part === "p" ? s.pt : s.st };
  }
  function active(k) {
    const st = state[k], ep = byKey[k], b = [], c = [];
    for (const [id, v] of Object.entries(st.sel)) {
      const el = element(ep, id);
      if (!el || !st.base) continue;
      if (v === "b" && id[0] !== st.base) b.push([id, el]);
      if (v === "c" && id[0] === st.base) c.push([id, el]);
    }
    const order = (x, y) => x[0].localeCompare(y[0], undefined, { numeric: true });
    return { b: b.sort(order), c: c.sort(order) };
  }
  function estimate(k) {
    const st = state[k], ep = byKey[k];
    if (!st.base) return null;
    const base = opt(ep, st.base), { b, c } = active(k);
    let rt = base.rt, w = base.words;
    for (const [, el] of c) { if (el.kind === "p") rt -= el.s.d; if (el.kind === "w") w -= el.s.w; }
    for (const [, el] of b) { if (el.kind === "p") rt += el.s.d; if (el.kind === "w") w += el.s.w; }
    return { rt: Math.max(0, Math.round(rt)), w: Math.max(0, w), h: base.hours, title: base.title };
  }
  function short(t, n) { t = t || ""; return t.length > n ? t.slice(0, n - 1).trimEnd() + "…" : t; }
  function describe(k) {
    const st = state[k], ep = byKey[k];
    const head = "Ep " + ep.n + " · " + ep.subject;
    if (!st.base) return head + ": no base chosen" + (st.note.trim() ? ". Note: " + st.note.trim() : ".");
    const e = estimate(k), { b, c } = active(k), out = [];
    out.push(head + ": base " + st.base + " · " + e.title + " (about " + e.rt + " s, " + e.w + " spoken words)");
    for (const [, el] of b) out.push("  + borrow " + el.label + ": " + short(el.text, 110));
    for (const [, el] of c) out.push("  − cut " + el.label + ": " + short(el.text, 110));
    if (st.note.trim()) out.push("  note: " + st.note.trim());
    return out.join("\n");
  }
  function status(k) {
    const st = state[k];
    if (!st.base) return st.note.trim() ? "note" : "—";
    const { b, c } = active(k), n = b.length + c.length;
    return n ? st.base + "+" + n : st.base;
  }

  // ---- saving
  function setSave(cls, text) { const el = $("#save"); el.className = "save " + cls; el.textContent = text; }
  function showSave() {
    if (mode === "db") setSave(Object.values(pending).some(Boolean) || Object.values(inflight).some(Boolean) ? "" : "ok",
      Object.values(pending).some(Boolean) || Object.values(inflight).some(Boolean) ? "Saving…" : "Saved here · Claude can read your picks");
    else if (mode === "local") setSave("bad", "Saved on this device only · use Copy picks on the Summary");
    else if (mode === "readonly") setSave("bad", "View only · you can't change picks here");
    else setSave("", "Connecting…");
  }
  function changed(k, ms) {
    lsSave();
    if (mode !== "db") { showSave(); return; }
    pending[k] = true; showSave();
    clearTimeout(timers[k]);
    timers[k] = setTimeout(() => save(k), ms == null ? 500 : ms);
  }
  async function save(k, retried) {
    if (inflight[k]) { again[k] = true; return; }
    inflight[k] = true; pending[k] = false;
    const st = state[k];
    try {
      await db.doc("picks/" + k).set({ episode: byKey[k].n, base: st.base, sel: st.sel, note: st.note,
        readable: describe(k), updatedAt: new Date().toISOString() });
    } catch (e) {
      const code = e && e.code;
      if (code === "invalid_argument" || code === "not_granted" || code === "revoked") { mode = "readonly"; writable = false; render(); }
      else if (code === "unavailable" && !retried) { inflight[k] = false; setTimeout(() => save(k, true), 400 + Math.random() * 900); return; }
      else { pending[k] = true; setSave("bad", "Couldn't save (" + (code || "error") + "). Your picks are kept on this device."); inflight[k] = false; return; }
    }
    inflight[k] = false;
    if (again[k]) { again[k] = false; save(k); return; }
    showSave();
  }

  async function connect() {
    const c = window.claude;
    const use = c && typeof c.use === "function" ? n => c.use(n) : null;
    let d = null, u = null;
    try { [d, u] = await Promise.all([use ? use("db") : null, use ? use("user") : null]); } catch (e) { d = null; }
    if (!d) { mode = "local"; showSave(); return; }
    let can = null;
    try { can = u ? await u.can("data.write") : null; } catch (e) { can = null; }
    db = d; mode = can === false ? "readonly" : "db"; writable = can !== false;
    let first = true;
    db.collection("picks").onSnapshot(snap => {
      const seen = new Set();
      let any = false;
      for (const doc of snap.docs) {
        const k = doc.id;
        if (!state[k]) continue;
        seen.add(k);
        if (pending[k] || inflight[k]) continue;
        const n = norm(doc.data());
        const typing = k === view && document.activeElement && document.activeElement.id === "note";
        if (typing) n.note = state[k].note;
        if (JSON.stringify(n) !== JSON.stringify(state[k])) { state[k] = n; any = true; }
      }
      if (first) {
        first = false;
        if (mode === "db") for (const k of KEYS) if (!seen.has(k) && !isEmpty(state[k])) changed(k, 50);
      }
      if (any) { lsSave(); render(); }
      showSave();
    }, err => setSave("bad", "Lost the connection (" + ((err && err.code) || "error") + "). Picks stay on this device."));
    render();
  }

  // ---- actions
  let toastTimer = null;
  function toast(text) {
    let el = $("#toast");
    el.textContent = text; el.hidden = false;
    clearTimeout(toastTimer); toastTimer = setTimeout(() => { el.hidden = true; }, 2200);
  }
  function setBase(k, L) {
    if (!writable) return toast("This view is read-only.");
    const st = state[k];
    if (st.base === L) return;
    st.base = L;
    for (const [id, v] of Object.entries(st.sel)) if ((id[0] === L && v === "b") || (id[0] !== L && v === "c")) delete st.sel[id];
    tabs[k] = L;
    render(); changed(k);
  }
  function clearEp(k) {
    if (!writable) return toast("This view is read-only.");
    state[k] = blank(); render(); changed(k);
  }
  function toggle(k, id) {
    if (!writable) return toast("This view is read-only.");
    const st = state[k];
    if (!st.base) { toast("Choose a base first"); const b = document.querySelector(".base"); if (b) b.focus(); return; }
    const want = id[0] === st.base ? "c" : "b";
    if (st.sel[id] === want) delete st.sel[id]; else st.sel[id] = want;
    render(); changed(k);
  }
  function unpick(k, id) { delete state[k].sel[id]; render(); changed(k); }
  function go(v) {
    view = v; lsSave();
    try { history.replaceState(null, "", "#" + v); } catch (e) { /* ignore */ }
    render(); window.scrollTo({ top: 0 });
  }

  // ---- rendering
  function h(tag, attrs, ...kids) {
    const el = document.createElement(tag);
    for (const [a, v] of Object.entries(attrs || {})) {
      if (v == null || v === false) continue;
      if (a === "html") el.innerHTML = v;            // trusted: generated from the repo's markdown
      else if (a === "text") el.textContent = v;
      else if (a.startsWith("on")) el.addEventListener(a.slice(2), v);
      else el.setAttribute(a, v === true ? "" : v);
    }
    for (const kid of kids.flat()) if (kid != null && kid !== false) el.append(kid.nodeType ? kid : document.createTextNode(kid));
    return el;
  }
  function chips() {
    const box = $("#chips"); box.replaceChildren();
    for (const k of KEYS) {
      const ep = byKey[k], s = status(k);
      box.append(h("button", { type: "button", class: "chip" + (view === k ? " on" : "") + (state[k].base ? " done" : ""),
        "aria-current": view === k ? "page" : null, onclick: () => go(k), title: ep.subject },
        "Ep " + ep.n, h("span", { class: "st", text: s })));
    }
    const done = KEYS.filter(k => state[k].base).length;
    box.append(h("button", { type: "button", class: "chip" + (view === "summary" ? " on" : ""), onclick: () => go("summary") },
      "Summary", h("span", { class: "st", text: done + "/9" })));
  }
  function toggleBtn(k, id, labelText, bodyHtml, disabled) {
    const st = state[k], v = st.sel[id], L = id[0];
    const cls = st.base && v === "b" && L !== st.base ? "b" : st.base && v === "c" && L === st.base ? "c" : "";
    const lab = cls === "b" ? labelText + " · borrowed" : cls === "c" ? labelText + " · cut" : labelText;
    return h("button", { type: "button", class: "tg " + cls, "data-key": id, "aria-pressed": cls ? "true" : "false",
      disabled: disabled || !writable ? true : null, onclick: () => toggle(k, id) },
      h("span", { class: "lab", text: lab }), h("span", { class: "body", html: bodyHtml }));
  }
  function column(k, ep, o) {
    const st = state[k], isBase = st.base === o.L;
    const col = h("section", { class: "col" + (isBase ? " isbase" : ""), "data-l": o.L, "aria-label": "Option " + o.L },
      h("h3", {}, h("span", { class: "l", text: o.L }), o.title),
      h("p", { class: "med", text: o.medium }),
      h("div", { class: "stats" }, h("strong", { text: o.rt + " s" }), " · " + o.words + " words" + (o.hours != null ? " · ~" + o.hours + " h render" : "")),
      h("button", { type: "button", class: "use", "aria-pressed": isBase ? "true" : "false", disabled: writable ? null : true,
        onclick: () => setBase(k, o.L) }, isBase ? "Your base" : "Use as base"),
      h("h4", { text: "What happens" }), h("p", { html: o.logline }),
      h("h4", { text: "The idea" }), h("p", { html: o.idea }),
      h("h4", { text: "Look and sound" }),
      h("ul", { class: "look" }, o.look.map((li, i) => h("li", {}, toggleBtn(k, o.L + "l" + i, "Look " + (i + 1), li)))),
      h("h4", { text: "Storyboard" }),
      h("ol", { class: "shots" }, o.shots.map(s => h("li", { class: "shot" },
        h("span", { class: "no", text: "Shot " + s.n + " · " + s.t + " s" + (s.w ? " · " + s.w + " words" : "") }),
        toggleBtn(k, o.L + s.n + "p", "Picture", s.pic, s.tag),
        toggleBtn(k, o.L + s.n + "w", "Sound and words", s.snd, s.tag)))),
      h("details", {}, h("summary", { text: "Built from, and render" }),
        h("p", { class: "small", html: o.built }), h("p", { class: "small", html: o.render })));
    return col;
  }
  function mine(k, ep) {
    const st = state[k], e = estimate(k), { b, c } = active(k);
    const card = h("section", { class: "mine", "aria-label": "Your version" },
      h("h3", { text: "Your version of Ep " + ep.n }),
      h("div", { class: "bases", role: "group", "aria-label": "Base" }, ep.opts.map(o =>
        h("button", { type: "button", class: "base", "aria-pressed": st.base === o.L ? "true" : "false", disabled: writable ? null : true,
          onclick: () => setBase(k, o.L) }, h("b", { text: o.L }), o.title))),
      e ? h("div", { class: "stats" }, "About ", h("strong", { text: e.rt + " s" }), " · ", h("strong", { text: e.w + " spoken words" }),
            e.h != null ? " · ~" + e.h + " h render (base)" : "")
        : h("p", { class: "hint", text: "Start by choosing a base: the option whose event you want to make. Then tap pictures or sound in the other options to borrow them, and tap your base's to cut them." }));
    if (b.length || c.length) {
      card.append(h("ul", { class: "picks" },
        b.map(([id, el]) => h("li", { class: "b" }, h("span", { class: "k", text: "+ " + el.label }), h("span", { class: "ex", text: short(el.text, 140) }),
          h("button", { type: "button", class: "x", "aria-label": "Remove " + el.label, onclick: () => unpick(k, id), text: "×" }))),
        c.map(([id, el]) => h("li", { class: "c" }, h("span", { class: "k", text: "− " + el.label }), h("span", { class: "ex", text: short(el.text, 140) }),
          h("button", { type: "button", class: "x", "aria-label": "Restore " + el.label, onclick: () => unpick(k, id), text: "×" })))));
    }
    const ta = h("textarea", { id: "note", placeholder: "Anything the taps can't say: “keep the mug gag, but at night”, “end on the bloom”…",
      disabled: writable ? null : true });
    ta.value = st.note;
    ta.addEventListener("input", () => { state[k].note = ta.value; changed(k, 900); chips(); });
    card.append(h("label", { class: "nl", for: "note", text: "Note to the writer" }), ta);
    if (!isEmpty(st)) card.append(h("button", { type: "button", class: "x small", style: "justify-self:start;border:0;background:none;cursor:pointer;padding:0",
      onclick: () => clearEp(k), disabled: writable ? null : true, text: "Clear this episode" }));
    return card;
  }
  function episode(k) {
    const ep = byKey[k], st = state[k];
    const show = tabs[k] || st.base || "A";
    return [
      h("h2", {}, "Ep " + ep.n + " · " + ep.subject, h("span", { class: "t", text: ep.tag })),
      h("div", { class: "intro", html: ep.intro }),
      ep.rec ? h("details", {}, h("summary", { text: "The writer's recommendation" }), h("div", { html: ep.rec })) : null,
      mine(k, ep),
      h("div", { class: "tabs", role: "tablist", "aria-label": "Options" }, ep.opts.map(o =>
        h("button", { type: "button", role: "tab", class: "tab" + (show === o.L ? " on" : "") + (st.base === o.L ? " isbase" : ""),
          "aria-selected": show === o.L ? "true" : "false", onclick: () => { tabs[k] = o.L; lsSave(); render(); } },
          o.L + " · " + o.title + (st.base === o.L ? " (base)" : "")))),
      h("div", { class: "cols", "data-show": show }, ep.opts.map(o => column(k, ep, o))),
    ];
  }
  function summary() {
    const rows = [], text = [];
    let rt = 0, w = 0, hrs = 0, n = 0;
    for (const k of KEYS) {
      const ep = byKey[k], st = state[k], e = estimate(k), { b, c } = active(k);
      if (e) { rt += e.rt; w += e.w; hrs += e.h || 0; n++; }
      rows.push(h("tr", {},
        h("td", {}, h("button", { type: "button", class: "chip", onclick: () => go(k) }, "Ep " + ep.n)),
        h("td", { text: ep.subject }),
        h("td", { text: st.base ? st.base + " · " + opt(ep, st.base).title : "—" }),
        h("td", { text: b.length ? b.map(([, el]) => el.label).join("; ") : "" }),
        h("td", { text: c.length ? c.map(([, el]) => el.label).join("; ") : "" }),
        h("td", { text: e ? e.rt + " s" : "" }), h("td", { text: e ? String(e.w) : "" }),
        h("td", { text: st.note })));
      text.push(describe(k));
    }
    const box = h("textarea", { class: "copybox", readonly: true, "aria-label": "Your picks as text" });
    box.value = "Tidebreak mini-series picks\n\n" + text.join("\n\n");
    const copy = h("button", { type: "button", class: "btn", onclick: async () => {
      try { await navigator.clipboard.writeText(box.value); toast("Copied"); }
      catch (e) { box.focus(); box.select(); toast("Select and copy the text below"); }
    } }, "Copy picks as text");
    const mm = Math.floor(rt / 60), ss = String(rt % 60).padStart(2, "0");
    return [
      h("h2", { text: "Summary" }),
      h("p", { class: "hint", text: mode === "db"
        ? "Your picks are saved here as you go. When you're done, tell Claude “picks are in” and it will read them from this page."
        : "This view can't save picks for Claude. Copy them and paste them into the chat." }),
      h("div", { class: "summary" }, h("div", { class: "tbl" }, h("table", {},
        h("thead", {}, h("tr", {}, ["Ep", "Subject", "Base", "Borrowed", "Cut", "≈ Time", "≈ Words", "Note"].map(t => h("th", { text: t })))),
        h("tbody", {}, rows),
        h("tfoot", {}, h("tr", {}, h("td", { colspan: "5", text: n + " of 9 episodes with a base · ~" + Math.round(hrs) + " h render (bases)" }),
          h("td", { text: mm + ":" + ss }), h("td", { text: String(w) }), h("td", {})))))),
      h("div", {}, copy), box,
    ];
  }
  function render() {
    const focused = document.activeElement && document.activeElement.dataset ? document.activeElement.dataset.key : null;
    chips();
    const main = $("#view");
    main.replaceChildren(...(view === "summary" ? summary() : episode(view)));
    if (focused) { const el = document.querySelector('[data-key="' + focused + '"]'); if (el) el.focus(); }
    showSave();
  }

  lsLoad();
  const hash = (location.hash || "").slice(1);
  if (KEYS.includes(hash) || hash === "summary") view = hash;
  render();
  connect();
})();
"""


def build():
    eps = [parse_episode(p) for p in sorted(SRC.glob("ep*.md"), key=lambda p: int(re.match(r"ep(\d+)", p.stem).group(1)))]
    data = json.dumps({"eps": eps}, ensure_ascii=False).replace("</", "<\\/")
    head = ('<title>Tidebreak Episode Options</title>\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
            '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700'
            '&family=IBM+Plex+Mono:wght@500;600&family=IBM+Plex+Sans:wght@400;600&display=swap">\n'
            f"<style>{CSS}</style>\n")
    body = ('<div class="wrap">\n<header class="top"><div class="eyebrow">Operation Tidebreak · pre-release mini-series · '
            'round 2 options</div><h1>Pick and merge</h1><ol class="steps">'
            '<li><strong>Choose a base</strong> for each episode: the option whose event you want to make.</li>'
            '<li><strong>Tap a picture or a line</strong> in another option to borrow it; tap one in your base to cut it.</li>'
            '<li><strong>Add a note</strong> for anything the taps can’t say. Picks save as you go; when you’re done, '
            'tell Claude “picks are in”.</li></ol></header>\n'
            '<nav class="bar" aria-label="Episodes"><div class="chips" id="chips"></div>'
            '<span class="save" id="save" role="status">Connecting…</span></nav>\n'
            '<main id="view"></main>\n'
            '<footer>Generated by miniseries/build_picker.py from miniseries/options/. Writers follow '
            'miniseries/options/BRIEF.md.</footer>\n</div>\n'
            '<div class="toast" id="toast" role="status" aria-live="polite" hidden></div>\n'
            f'<script type="application/json" id="picker-data">{data}</script>\n'
            f"<script>{JS}</script>\n")
    return head, body, eps


def main():
    head, body, eps = build()
    page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
            + head + "</head>\n<body>\n" + body + "</body>\n</html>\n")
    (ROOT / "picker.html").write_text(page)
    if "--fragment" in sys.argv:
        frag = pathlib.Path(sys.argv[sys.argv.index("--fragment") + 1])
        frag.parent.mkdir(parents=True, exist_ok=True)
        frag.write_text(head + body)
    shots = sum(len(o["shots"]) for e in eps for o in e["opts"])
    print(f"wrote {ROOT / 'picker.html'} ({len(page):,} bytes): {len(eps)} episodes, {shots} shots")
    for e in eps:
        print(f"  Ep {e['n']}: " + "; ".join(f"{o['L']} {o['title']} {o['rt']} s, {len(o['shots'])} shots, "
                                             f"{o['words']} w, {o['hours']} h" for o in e["opts"]))


if __name__ == "__main__":
    main()
