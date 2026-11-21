# -*- coding: utf-8 -*-
"""Graphes (SVG pour le site, pgfplots pour les PDF) et simulations interactives.

Dans le texte d'un exercice, une ligne seule « [[graphe:id]] » insère le graphe, « [[simu:id]] » la simulation.
"""
from math import cos, sin, pi, sqrt  # noqa: F401  (utilisés dans les expressions)

def _fr(v):
    s = ("%g" % v).replace(".", ",")
    return s.replace("-", "−")

# id -> spécification. Chaque courbe : py (expression en t ou x), pgf (expression pgfplots), dom (intervalle)
G = {
    "p1-a1-traj": dict(x=(-1, 5), y=(-1.5, 5), xt=[1, 2, 3, 4], yt=[-1, 1, 2, 3, 4], xl="x (m)", yl="y (m)",
                       courbes=[dict(py="x**2/4-1", pgf="x^2/4-1", dom=(0, 4.6))], points=[(2, 0, "M (t = 1 s)"), (0, -1, "M₀")]),
    "p1-c3-v": dict(x=(0, 5.6), y=(0, 9.5), xt=[1, 2, 3, 4, 5], yt=[2, 4, 6, 8], xl="t (s)", yl="v (m/s)",
                    courbes=[dict(py="2+2*x", pgf="2+2*x", dom=(0, 3)), dict(py="8+0*x", pgf="8", dom=(3, 5))]),
    "p1-d2-x": dict(x=(0, 0.85), y=(-2.8, 2.8), xt=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], yt=[-2, -1, 1, 2], xl="t (s)", yl="x (cm)",
                    courbes=[dict(py="2*cos(5*pi*x-pi/2)", pgf="2*cos(deg(5*pi*x-pi/2))", dom=(0, 0.8))]),
    "p1-evd-x": dict(x=(0, 0.85), y=(-3.6, 3.6), xt=[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8], yt=[-3, -1.5, 1.5, 3], xl="t (s)", yl="x (cm)",
                     courbes=[dict(py="3*cos(5*pi*x-pi/3)", pgf="3*cos(deg(5*pi*x-pi/3))", dom=(0, 0.8))]),
    "p2-c2-em": dict(x=(0, 5.6), y=(0, 110), xt=[1, 2, 3, 4, 5], yt=[25, 50, 75, 100], xl="z (m)", yl="E (J)",
                     courbes=[dict(py="20*x", pgf="20*x", dom=(0, 5)), dict(py="100-20*x", pgf="100-20*x", dom=(0, 5)),
                              dict(py="100+0*x", pgf="100", dom=(0, 5))],
                     legendes=[(4.2, 92, "Eₚ"), (4.2, 8, "E꜀"), (0.4, 104, "Eₘ")]),
    "bac12-vx": dict(x=(0, 2.6), y=(0, 12), xt=[0.5, 1, 1.5, 2, 2.5], yt=[2, 4, 6, 8, 10], xl="t (s)", yl="vx (m/s)",
                     courbes=[dict(py="10+0*x", pgf="10", dom=(0, 2.05))]),
    "bac12-vy": dict(x=(0, 3), y=(-12, 12), xt=[0.5, 1, 1.5, 2, 2.5], yt=[-10, -5, 5, 10], xl="t (s)", yl="vy (m/s)",
                     courbes=[dict(py="9-9.8*x", pgf="9-9.8*x", dom=(0, 2.05))]),
}

W, H, ML, MR, MT, MB = 600, 300, 52, 22, 18, 40

def svg(gid):
    g = G[gid]; x0, x1 = g["x"]; y0, y1 = g["y"]
    X = lambda v: ML + (v - x0) / (x1 - x0) * (W - ML - MR)
    Y = lambda v: MT + (y1 - v) / (y1 - y0) * (H - MT - MB)
    ax_y = Y(0) if y0 <= 0 <= y1 else Y(y0)
    o = ["<figure class='graphe'><svg viewBox='0 0 %d %d' role='img' aria-label='graphe %s en fonction de %s'>" % (W, H, g["yl"], g["xl"])]
    for v in g["xt"]:
        o.append("<line x1='%.1f' y1='%d' x2='%.1f' y2='%d' stroke='var(--grid)'/>" % (X(v), MT, X(v), H - MB))
        o.append("<text x='%.1f' y='%.1f' font-size='13' text-anchor='middle' fill='var(--muted)'>%s</text>" % (X(v), ax_y + 17, _fr(v)))
    for v in g["yt"]:
        o.append("<line x1='%d' y1='%.1f' x2='%d' y2='%.1f' stroke='var(--grid)'/>" % (ML, Y(v), W - MR, Y(v)))
        o.append("<text x='%d' y='%.1f' font-size='13' text-anchor='end' fill='var(--muted)'>%s</text>" % (ML - 6, Y(v) + 4, _fr(v)))
    o.append("<line x1='%d' y1='%.1f' x2='%d' y2='%.1f' stroke='var(--ink)' stroke-width='1.3'/>" % (ML, ax_y, W - MR + 6, ax_y))
    o.append("<line x1='%.1f' y1='%d' x2='%.1f' y2='%d' stroke='var(--ink)' stroke-width='1.3'/>" % (X(max(x0, 0)), H - MB, X(max(x0, 0)), MT - 6))
    o.append("<text x='%d' y='%.1f' font-size='14' text-anchor='end' fill='var(--ink)'>%s</text>" % (W - MR + 6, ax_y - 8, g["xl"]))
    o.append("<text x='%.1f' y='%d' font-size='14' fill='var(--ink)'>%s</text>" % (X(max(x0, 0)) + 8, MT + 4, g["yl"]))
    for c in g["courbes"]:
        a, b = c["dom"]; n = 160
        pts = " ".join("%.1f,%.1f" % (X(a + (b - a) * k / n), Y(eval(c["py"], {"cos": cos, "sin": sin, "pi": pi, "sqrt": sqrt, "x": a + (b - a) * k / n})))
                       for k in range(n + 1))
        o.append("<polyline points='%s' fill='none' stroke='var(--pen)' stroke-width='2.4'/>" % pts)
    for px, py, lab in g.get("points", []):
        o.append("<circle cx='%.1f' cy='%.1f' r='4' fill='var(--rouge)'/><text x='%.1f' y='%.1f' font-size='13' fill='var(--rouge)'>%s</text>" % (
            X(px), Y(py), X(px) + 7, Y(py) - 7, lab))
    for px, py, lab in g.get("legendes", []):
        o.append("<text x='%.1f' y='%.1f' font-size='15' font-weight='700' fill='var(--rouge)'>%s</text>" % (X(px), Y(py), lab))
    return "".join(o) + "</svg></figure>"

def tikz(gid):
    g = G[gid]; x0, x1 = g["x"]; y0, y1 = g["y"]
    xt = ",".join("%g" % v for v in g["xt"]); yt = ",".join("%g" % v for v in g["yt"])
    rep = lambda t: t.replace("ₚ", "_p").replace("꜀", "_c").replace("ₘ", "_m").replace("₀", "_0")
    t = ["\\begin{center}\\begin{tikzpicture}\\begin{axis}[width=13cm,height=6cm,axis lines=middle,xmin=%g,xmax=%g,ymin=%g,ymax=%g,"
         "xtick={%s},ytick={%s},grid=major,grid style={mngrey!25},tick label style={font=\\small},"
         "xlabel={%s},ylabel={%s},xlabel style={at={(ticklabel* cs:1)},anchor=south east},ylabel style={at={(ticklabel* cs:1)},anchor=south west},"
         "/pgf/number format/use comma]" % (x0, x1, y0, y1, xt, yt, g["xl"], g["yl"])]
    for c in g["courbes"]:
        t.append("\\addplot[domain=%g:%g,samples=160,very thick,mnblue]{%s};" % (c["dom"][0], c["dom"][1], c["pgf"]))
    for px, py, lab in g.get("points", []):
        t.append("\\addplot[only marks,mark=*,mnnavy] coordinates{(%g,%g)} node[above right,font=\\small]{$%s$};" % (px, py, rep(lab).replace(" (t = 1 s)", "\\,(t=1\\,\\mathrm{s})")))
    for px, py, lab in g.get("legendes", []):
        t.append("\\node[font=\\small\\bfseries,mnnavy] at (axis cs:%g,%g) {$%s$};" % (px, py, rep(lab)))
    return "\n".join(t) + "\n\\end{axis}\\end{tikzpicture}\\end{center}"

# ---------------------------------------------------------------- simulations
def simu(sid):
    if sid == "phase":
        return """<div class='simu' data-simu='phase'><p class='lab'>Manipule : la phase à l'origine</p>
<div class='ctl'><label for='s-xm'>X<sub>m</sub> (cm)</label><input id='s-xm' type='range' min='1' max='5' step='0.5' value='4'><output>4</output>
<label for='s-t'>T (s)</label><input id='s-t' type='range' min='0.2' max='1' step='0.1' value='0.5'><output>0,5</output>
<label for='s-phi'>φ (rad)</label><input id='s-phi' type='range' min='-12' max='12' step='1' value='4'><output>π/3</output></div>
<svg viewBox='0 0 600 260' class='s-svg' role='img' aria-label='courbe x(t)'></svg>
<p class='s-txt'></p></div>"""
    return ""

SIMU_JS = r"""
window.SIMU = window.SIMU || {};
SIMU.phase = function(el){
  var xm = el.querySelector('#s-xm'), tt = el.querySelector('#s-t'), ph = el.querySelector('#s-phi'), svg = el.querySelector('.s-svg'), txt = el.querySelector('.s-txt');
  function frac(k){ if (k === 0) return '0'; var g = function(a,b){ return b ? g(b, a % b) : a; }, d = g(Math.abs(k), 12), n = k / d, q = 12 / d;
    return (n < 0 ? '−' : '') + (Math.abs(n) === 1 ? '' : Math.abs(n)) + 'π' + (q === 1 ? '' : '/' + q); }
  function draw(){
    var A = +xm.value, T = +tt.value, k = +ph.value, p = k * Math.PI / 12, w = 2 * Math.PI / T;
    xm.nextElementSibling.textContent = String(A).replace('.', ',');
    tt.nextElementSibling.textContent = String(T).replace('.', ',');
    ph.nextElementSibling.textContent = frac(k);
    var X = function(t){ return 40 + t * 540; }, Y = function(x){ return 130 - x * 22; }, s = '';
    s += "<line x1='40' y1='130' x2='590' y2='130' stroke='var(--ink)'/><line x1='40' y1='15' x2='40' y2='245' stroke='var(--ink)'/>";
    s += "<line x1='40' y1='" + Y(A) + "' x2='590' y2='" + Y(A) + "' stroke='var(--grid)' stroke-dasharray='4 4'/><line x1='40' y1='" + Y(-A) + "' x2='590' y2='" + Y(-A) + "' stroke='var(--grid)' stroke-dasharray='4 4'/>";
    s += "<text x='586' y='148' font-size='13' text-anchor='end' fill='var(--muted)'>t = 1 s</text><text x='46' y='24' font-size='13' fill='var(--muted)'>x (cm)</text>";
    var pts = []; for (var i = 0; i <= 300; i++){ var t = i / 300; pts.push(X(t).toFixed(1) + ',' + Y(A * Math.cos(w * t + p)).toFixed(1)); }
    s += "<polyline points='" + pts.join(' ') + "' fill='none' stroke='var(--pen)' stroke-width='2.4'/>";
    var x0 = A * Math.cos(p), v0 = -A * w * Math.sin(p);
    s += "<circle cx='40' cy='" + Y(x0).toFixed(1) + "' r='5' fill='var(--rouge)'/>";
    svg.innerHTML = s;
    var sens = Math.abs(Math.sin(p)) < 1e-9 ? 'il est à une extrémité, sa vitesse est nulle' : (v0 > 0 ? 'il part dans le sens positif (la courbe monte)' : 'il part dans le sens négatif (la courbe descend)');
    txt.innerHTML = 'À t = 0 : x₀ = X<sub>m</sub> cos φ = ' + x0.toFixed(2).replace('.', ',') + ' cm, et ' + sens + '. Change le signe de φ : x₀ ne bouge pas, mais le sens s’inverse.';
  }
  [xm, tt, ph].forEach(function(r){ r.addEventListener('input', draw); }); draw();
};
"""
