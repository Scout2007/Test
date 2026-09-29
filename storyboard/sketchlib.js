// Sketch library, taken from the draft storyboard (pack/storyboard_draft/index.html)
// so the revised board keeps the draft's look. Additions are marked "added".
var W = 240, H = 100;
function esc(t) { return String(t).replace(/&/g, "&amp;").replace(/</g, "&lt;"); }
function rng(seed) { var s = seed * 9301 + 49297; return function () { s = (s * 9301 + 49297) % 233280; return s / 233280; }; }
  function stars(seed, n) {
    var r = rng(seed), out = "";
    for (var i = 0; i < n; i++) {
      var x = (r() * W).toFixed(1), y = (r() * H).toFixed(1), a = (0.25 + r() * 0.6).toFixed(2), rad = (r() < 0.08 ? 0.55 : 0.28);
      out += '<circle cx="' + x + '" cy="' + y + '" r="' + rad + '" fill="#cfd8e0" opacity="' + a + '"/>';
    }
    return out;
  }
  var C = { hull: "#cfd6dc", ring: "#eef1f3", gold: "#c9922f", dark: "#2a3037", heat: "#ff8a3c", teal: "#1f6b61",
            hostile: "#5a2a24", hlight: "#e2603f", dew: "#b476ff", kin: "#8fb1ff", plume: "#fff4de" };
  var SHIP = {
    endeavor: function () {
      return '<ellipse cx="-47" cy="0" rx="1.8" ry="14" fill="' + C.gold + '"/>' +
        '<rect x="-44.5" y="-13.5" width="2.6" height="27" rx="1" fill="' + C.ring + '"/>' +
        '<rect x="-42" y="-1.4" width="6.5" height="2.8" fill="' + C.dark + '"/>' +
        '<path d="M-36,-3 L-29,-4.6 L6,-4.6 L8,-3.2 L8,3.2 L6,4.6 L-29,4.6 L-36,3Z" fill="' + C.hull + '"/>' +
        '<rect x="-24" y="-0.9" width="18" height="1.8" fill="' + C.teal + '"/>' +
        '<rect x="4" y="-9.2" width="11" height="2.6" rx="1.2" fill="' + C.hull + '"/>' +
        '<rect x="4" y="6.6" width="11" height="2.6" rx="1.2" fill="' + C.hull + '"/>' +
        '<path d="M10,-2.6 L34,-3 L36,-2 L36,2 L34,3 L10,2.6Z" fill="' + C.hull + '"/>' +
        '<path d="M18,-3 L26,-3 L38,-13 Z" fill="' + C.heat + '"/><path d="M18,3 L26,3 L38,13 Z" fill="' + C.heat + '"/>' +
        '<rect x="37" y="-14.5" width="2.6" height="29" rx="1" fill="' + C.ring + '"/>' +
        '<path d="M39.6,-2.2 L44.5,-3.6 L44.5,3.6 L39.6,2.2Z" fill="' + C.dark + '"/>';
    },
    endeavorNoShield: function () { return SHIP.endeavor().replace(/<ellipse[^>]*\/>/, ""); },
    astrid: function () {
      return '<rect x="-68" y="-0.6" width="16" height="1.2" fill="' + C.dark + '"/>' +
        '<ellipse cx="-52" cy="0" rx="1.8" ry="15" fill="' + C.gold + '"/>' +
        '<rect x="-49.5" y="-14.5" width="2.6" height="29" rx="1" fill="' + C.ring + '"/>' +
        '<path d="M-46,-3.4 L-38,-5 L14,-5 L16,-3.4 L16,3.4 L14,5 L-38,5 L-46,3.4Z" fill="' + C.hull + '"/>' +
        '<circle cx="-4" cy="-8.5" r="3.6" fill="none" stroke="' + C.hull + '" stroke-width="1.2"/>' +
        '<rect x="12" y="-9.5" width="11" height="2.6" rx="1.2" fill="' + C.hull + '"/><rect x="12" y="6.9" width="11" height="2.6" rx="1.2" fill="' + C.hull + '"/>' +
        '<path d="M18,-3 L46,-3.4 L48,-2 L48,2 L46,3.4 L18,3Z" fill="' + C.hull + '"/>' +
        '<path d="M26,-3.4 L32,-3.4 L40,-18 Z" fill="' + C.heat + '"/><path d="M34,-3.4 L40,-3.4 L48,-18 Z" fill="' + C.heat + '"/>' +
        '<path d="M26,3.4 L32,3.4 L40,18 Z" fill="' + C.heat + '"/><path d="M34,3.4 L40,3.4 L48,18 Z" fill="' + C.heat + '"/>' +
        '<rect x="49" y="-15" width="2.6" height="30" rx="1" fill="' + C.ring + '"/>' +
        '<path d="M51.6,-2.4 L57,-4 L57,4 L51.6,2.4Z" fill="' + C.dark + '"/>';
    },
    frigate: function () {
      return '<path d="M-30,0 L-26,-7 L-26,7Z" fill="' + C.gold + '"/><rect x="-25" y="-4" width="5" height="8" rx="1" fill="' + C.hull + '"/>' +
        '<rect x="-20" y="-0.8" width="22" height="1.6" fill="' + C.hull + '"/>' +
        '<rect x="2" y="-5.5" width="10" height="11" rx="1" fill="' + C.teal + '" stroke="' + C.hull + '" stroke-width="0.6"/>' +
        '<rect x="14" y="-9" width="3" height="18" fill="' + C.heat + '"/><rect x="18" y="-3" width="6" height="6" fill="' + C.dark + '"/>';
    },
    hedgehog: function () {
      var s = SHIP.frigate();
      for (var i = 0; i < 11; i++) { var x = -19 + i * 2; s += '<rect x="' + x + '" y="-4.2" width="1.4" height="8.4" fill="' + C.dark + '"/>'; }
      return s;
    },
    destroyer: function () {
      return '<path d="M-14,0 L-11,-5.5 L-11,5.5Z" fill="' + C.gold + '"/><rect x="-10.5" y="-1" width="5" height="2" fill="' + C.dark + '"/>' +
        '<rect x="-5.5" y="-3.6" width="9" height="7.2" rx="1" fill="' + C.teal + '" stroke="' + C.hull + '" stroke-width="0.5"/>' +
        '<path d="M3,-2 L10,-7 L12,-7 L6,-2Z" fill="' + C.heat + '"/><path d="M3,2 L10,7 L12,7 L6,2Z" fill="' + C.heat + '"/>' +
        '<rect x="3.5" y="-1.8" width="8" height="3.6" fill="' + C.hull + '"/>';
    },
    corvette: function () { return '<path d="M-6,0 L3,-2.4 L6,0 L3,2.4Z" fill="' + C.hull + '"/>'; },
    drone: function () { return '<path d="M-2,0 L2,-1.4 L2,1.4Z" fill="' + C.hull + '"/>'; },
    monitor: function () {
      return '<path d="M-52,-7 L-40,-11 L38,-11 L50,-5 L50,5 L38,11 L-40,11 L-52,7Z" fill="' + C.hostile + '" stroke="#9b4a3a" stroke-width="0.7"/>' +
        '<rect x="-30" y="-15" width="10" height="4" fill="' + C.hostile + '"/><rect x="-6" y="-15" width="10" height="4" fill="' + C.hostile + '"/><rect x="18" y="-15" width="10" height="4" fill="' + C.hostile + '"/>' +
        '<rect x="-30" y="11" width="10" height="4" fill="' + C.hostile + '"/><rect x="-6" y="11" width="10" height="4" fill="' + C.hostile + '"/>' +
        '<circle cx="-44" cy="0" r="1.2" fill="' + C.hlight + '"/><circle cx="44" cy="0" r="1.2" fill="' + C.hlight + '"/>' +
        '<rect x="-40" y="-0.6" width="78" height="1.2" fill="#8a3a2e"/>';
    },
    hfrigate: function () {
      return '<path d="M-24,0 L-10,-5 L18,-4.5 L24,0 L18,4.5 L-10,5Z" fill="' + C.hostile + '" stroke="#9b4a3a" stroke-width="0.6"/>' +
        '<circle cx="-18" cy="0" r="0.9" fill="' + C.hlight + '"/>';
    },
    pod: function () { return '<path d="M-3,-2.6 L0,-4 L3,-2.6 L3,2.6 L0,4 L-3,2.6Z" fill="' + C.hostile + '" stroke="' + C.hlight + '" stroke-width="0.4"/>'; },
    railplat: function () { return '<rect x="-4" y="-3" width="8" height="6" fill="' + C.hostile + '"/><rect x="-16" y="-0.6" width="12" height="1.2" fill="#8a3a2e"/>'; },
    tender: function () { // added: the Nauvoo, a boxy hauler with cargo frames
      var s = '<rect x="-26" y="-6" width="40" height="12" rx="1" fill="' + C.hull + '"/>' +
        '<rect x="14" y="-3" width="10" height="6" fill="' + C.dark + '"/><rect x="24" y="-8" width="2.4" height="16" fill="' + C.ring + '"/>' +
        '<rect x="-30" y="-8" width="2.4" height="16" fill="' + C.ring + '"/>';
      for (var i = 0; i < 5; i++) s += '<rect x="' + (-22 + i * 7) + '" y="-5" width="5" height="10" fill="none" stroke="' + C.dark + '" stroke-width="0.6"/>';
      return s;
    },
    shield: function () { return '<ellipse cx="0" cy="0" rx="2" ry="14" fill="' + C.gold + '"/>'; }
  };
  var SHIELDS = true; // added: the builder clears it for shots after the shields are parked
  function ship(kind, x, y, s, rot, flip) {
    var body = SHIP[kind]();
    if (!SHIELDS && kind !== "shield") body = body.replace(/<(ellipse|path)[^>]*fill="#c9922f"[^>]*\/>/g, "");
    return '<g transform="translate(' + x + ',' + y + ') rotate(' + (rot || 0) + ') scale(' + (flip ? -s : s) + ',' + s + ')">' + body + '</g>';
  }
  function glow(x, y, r, col, op) {
    var id = "g" + Math.random().toString(36).slice(2, 8);
    return '<defs><radialGradient id="' + id + '"><stop offset="0" stop-color="' + col + '" stop-opacity="' + (op || 1) + '"/><stop offset="1" stop-color="' + col + '" stop-opacity="0"/></radialGradient></defs>' +
      '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="url(#' + id + ')"/>';
  }
  function planet(x, y, r, lit) {
    var id = "p" + Math.random().toString(36).slice(2, 8);
    return '<defs><radialGradient id="' + id + '" cx="' + (lit === "left" ? "0.25" : "0.75") + '" cy="0.3" r="0.9"><stop offset="0" stop-color="#6d8fa8"/><stop offset="0.55" stop-color="#1e3446"/><stop offset="1" stop-color="#05080b"/></radialGradient></defs>' +
      '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="url(#' + id + ')"/><circle cx="' + x + '" cy="' + y + '" r="' + (r + 0.8) + '" fill="none" stroke="#4d86c4" stroke-opacity="0.55" stroke-width="1.2"/>';
  }
  function moon(x, y, r) { return '<circle cx="' + x + '" cy="' + y + '" r="' + r + '" fill="#5c6166"/><circle cx="' + (x + r * 0.3) + '" cy="' + (y - r * 0.2) + '" r="' + (r * 0.25) + '" fill="#474b50"/>'; }
  function rocks(seed, n, x0, x1, y0, y1, smin, smax) {
    var r = rng(seed), out = "";
    for (var i = 0; i < n; i++) {
      var cx = x0 + r() * (x1 - x0), cy = y0 + r() * (y1 - y0), s = smin + r() * (smax - smin), pts = [];
      for (var k = 0; k < 7; k++) { var a = k / 7 * 6.283, rr = s * (0.65 + r() * 0.5); pts.push((cx + Math.cos(a) * rr).toFixed(1) + "," + (cy + Math.sin(a) * rr * 0.8).toFixed(1)); }
      out += '<polygon points="' + pts.join(" ") + '" fill="#3a3f45" stroke="#6b737b" stroke-width="0.4"/>';
    }
    return out;
  }
  function plume(x, y, len, rot, w) {
    var id = "pl" + Math.random().toString(36).slice(2, 8);
    return '<defs><linearGradient id="' + id + '"><stop offset="0" stop-color="#fff8ea"/><stop offset="0.3" stop-color="#c7d4ff" stop-opacity="0.7"/><stop offset="1" stop-color="#6f86ff" stop-opacity="0"/></linearGradient></defs>' +
      '<g transform="translate(' + x + ',' + y + ') rotate(' + rot + ')"><path d="M0,-' + (w || 2.5) + ' L' + len + ',0 L0,' + (w || 2.5) + 'Z" fill="url(#' + id + ')"/></g>';
  }
  function trail(d, col, dash, wdt) { return '<path d="' + d + '" fill="none" stroke="' + (col || "#cfd8e0") + '" stroke-width="' + (wdt || 0.6) + '" stroke-dasharray="' + (dash || "1.2 1.6") + '" opacity="0.85"/>'; }
  function streak(x1, y1, x2, y2, col) { return '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="' + (col || C.kin) + '" stroke-width="0.8" opacity="0.9"/>'; }
  function tracers(x, y, ang, n, seed) {
    var r = rng(seed || 3), out = "";
    for (var i = 0; i < n; i++) { var a = (ang + (r() - 0.5) * 30) * Math.PI / 180, d0 = 4 + r() * 50, d1 = d0 + 2 + r() * 2;
      out += '<line x1="' + (x + Math.cos(a) * d0).toFixed(1) + '" y1="' + (y + Math.sin(a) * d0).toFixed(1) + '" x2="' + (x + Math.cos(a) * d1).toFixed(1) + '" y2="' + (y + Math.sin(a) * d1).toFixed(1) + '" stroke="#ffd9a0" stroke-width="0.5"/>'; }
    return out;
  }
  function smoke(x, y, r) { return glow(x, y, r, "#9aa6b0", 0.35); }
  function sparks(x, y, n, spread, seed) {
    var r = rng(seed || 7), out = "";
    for (var i = 0; i < n; i++) out += '<circle cx="' + (x + (r() - 0.5) * spread).toFixed(1) + '" cy="' + (y + (r() - 0.5) * spread * 0.6).toFixed(1) + '" r="0.5" fill="#ffe7b0"/>';
    return out;
  }
  function hud(x, y, w, h) {
    return '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h + '" fill="none" stroke="#33b3a2" stroke-width="0.5" opacity="0.8"/>' +
      '<line x1="' + x + '" y1="' + (y + h / 2) + '" x2="' + (x + w) + '" y2="' + (y + h / 2) + '" stroke="#33b3a2" stroke-width="0.3" opacity="0.5"/>' +
      '<line x1="' + (x + w / 2) + '" y1="' + y + '" x2="' + (x + w / 2) + '" y2="' + (y + h) + '" stroke="#33b3a2" stroke-width="0.3" opacity="0.5"/>';
  }
  function glitch(seed) {
    var r = rng(seed), out = "";
    for (var i = 0; i < 9; i++) { var y = r() * H, h = 0.6 + r() * 3; out += '<rect x="0" y="' + y.toFixed(1) + '" width="' + W + '" height="' + h.toFixed(1) + '" fill="' + (r() < 0.5 ? "#b476ff" : "#33b3a2") + '" opacity="' + (0.1 + r() * 0.25).toFixed(2) + '"/>'; }
    return out;
  }
  function label(x, y, t, col) { return '<text x="' + x + '" y="' + y + '" font-size="4.2" fill="' + (col || "#9fb0bc") + '">' + esc(t) + '</text>'; }
  function panel(parts, seed) {
    return '<svg viewBox="0 0 ' + W + ' ' + H + '" preserveAspectRatio="xMidYMid slice" role="img" aria-hidden="true">' +
      '<rect width="' + W + '" height="' + H + '" fill="#020304"/>' + stars(seed || 1, 70) + parts.join("") + '</svg>';
  }
