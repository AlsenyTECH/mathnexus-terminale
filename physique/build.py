# -*- coding: utf-8 -*-
"""Générateur du site « Sciences physiques TS2 » de MathNexus Education.

    python3 build.py            # écrit le site (index.html, p1.html, p2.html, scripts.html)
    python3 build.py --pdf      # et compile les séries PDF (series/*.pdf)

Le contenu est dans contenu/ : un module par chapitre (P1, P2…).
"""
import html, json, os, re, shutil, subprocess, sys, textwrap

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ICI)

# ---------------------------------------------------------------- mini-markup
# Paragraphes séparés par une ligne vide ; "- " liste ; "1. " questions numérotées
# (lignes suivantes indentées = suite de la question) ; "|a|b|" tableau ; "$$...$$" formule centrée ;
# $...$ formule en ligne ; **gras**.

def _blocks(s):
    s = textwrap.dedent(s).strip("\n")
    return [b for b in re.split(r"\n\s*\n", s) if b.strip()]

def _split_math(t):
    """Découpe en morceaux (texte, False) / (formule, True)."""
    out, i = [], 0
    for m in re.finditer(r"\$(.+?)\$", t, re.S):
        out.append((t[i:m.start()], False)); out.append((m.group(1), True)); i = m.end()
    out.append((t[i:], False))
    return out

def _marques(t):
    t = re.sub(r"\*\*(.+?)\*\*", "\x01\\1\x02", t)
    return re.sub(r"__(.+?)__", "\x03\\1\x04", t)

def inl_html(t):
    t = _marques(t)
    r = []
    for seg, isM in _split_math(t):
        if isM:
            r.append("\\(" + html.escape(seg, quote=False) + "\\)")
        else:
            r.append(html.escape(seg, quote=False))
    return "".join(r).replace("\x01", "<strong>").replace("\x02", "</strong>").replace("\x03", "<em>").replace("\x04", "</em>")

def inl_tex(t):
    t = _marques(t)
    r = []
    for seg, isM in _split_math(t):
        if isM:
            r.append("$" + seg.replace("°", "^{\\circ}") + "$")
        else:
            seg = seg.replace("%", "\\%").replace("&", "\\&").replace("#", "\\#")
            r.append(seg)
    return "".join(r).replace("\x01", "\\textbf{").replace("\x02", "}").replace("\x03", "\\emph{").replace("\x04", "}")

def _items(lines, pat):
    items = []
    for ln in lines:
        m = re.match(pat, ln)
        if m: items.append(ln[m.end():].strip())
        elif items: items[-1] += "\n" + ln.strip()
    return items

def _item_html(it):
    return "<br>".join(inl_html(x) for x in it.split("\n"))

def _item_tex(it):
    return "\\\\\n".join(inl_tex(x) for x in it.split("\n"))

GRAPHES = {}   # id -> spécification (remplie par contenu/graphes.py)

def md(s):
    out = []
    for b in _blocks(s):
        lines = b.split("\n"); f = lines[0].lstrip()
        m = re.match(r"\[\[(graphe|simu):([\w-]+)\]\]", f)
        if m:
            from contenu import graphes
            out.append(graphes.svg(m.group(2)) if m.group(1) == "graphe" else graphes.simu(m.group(2)))
        elif f.startswith("$$"):
            out.append("<p class='disp'>\\[" + html.escape(b.strip().strip("$").strip(), quote=False) + "\\]</p>")
        elif f.startswith("|"):
            rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines if ln.strip()]
            h = "<div class='table-wrap'><table><thead><tr>" + "".join("<th>%s</th>" % inl_html(c) for c in rows[0]) + "</tr></thead><tbody>"
            for r in rows[1:]:
                h += "<tr>" + "".join("<td>%s</td>" % inl_html(c) for c in r) + "</tr>"
            out.append(h + "</tbody></table></div>")
        elif re.match(r"- ", f):
            out.append("<ul>" + "".join("<li>%s</li>" % _item_html(i) for i in _items(lines, r"\s*- ")) + "</ul>")
        elif re.match(r"\d+\. ", f):
            st = re.match(r"\s*(\d+)\.", f).group(1)
            out.append("<ol class='q' start='%s'>" % st + "".join("<li>%s</li>" % _item_html(i) for i in _items(lines, r"\s*\d+\. ")) + "</ol>")
        else:
            out.append("<p>" + inl_html(" ".join(x.strip() for x in lines)) + "</p>")
    return "\n".join(out)

def md_tex(s):
    out = []
    for b in _blocks(s):
        lines = b.split("\n"); f = lines[0].lstrip()
        m = re.match(r"\[\[(graphe|simu):([\w-]+)\]\]", f)
        if m:
            if m.group(1) == "graphe":
                from contenu import graphes
                out.append(graphes.tikz(m.group(2)))
        elif f.startswith("$$"):
            out.append("\\[" + b.strip().strip("$").strip() + "\\]")
        elif f.startswith("|"):
            rows = [[c.strip() for c in ln.strip().strip("|").split("|")] for ln in lines if ln.strip()]
            n = len(rows[0])
            t = "\\begin{center}\\renewcommand{\\arraystretch}{1.35}\\begin{tabular}{|" + "c|" * n + "}\\hline\n"
            t += " & ".join("\\textbf{%s}" % inl_tex(c) for c in rows[0]) + "\\\\\\hline\n"
            for r in rows[1:]:
                t += " & ".join(inl_tex(c) for c in r) + "\\\\\\hline\n"
            out.append(t + "\\end{tabular}\\end{center}")
        elif re.match(r"- ", f):
            out.append("\\begin{itemize}" + "".join("\\item %s\n" % _item_tex(i) for i in _items(lines, r"\s*- ")) + "\\end{itemize}")
        elif re.match(r"\d+\. ", f):
            st = re.match(r"\s*(\d+)\.", f).group(1)
            out.append("\\begin{enumerate}[label=\\textbf{\\arabic*.},leftmargin=*,start=%s]" % st + "".join("\\item %s\n" % _item_tex(i) for i in _items(lines, r"\s*\d+\. ")) + "\\end{enumerate}")
        else:
            out.append(inl_tex(" ".join(x.strip() for x in lines)) + "\n")
    return "\n\n".join(out)

# ---------------------------------------------------------------- briques
def retenir(titre, s):
    return "<div class='retenir'><p class='lab'>À retenir · %s</p>%s</div>" % (titre, md(s))

def prof(s):
    return "<div class='prof'><p class='lab'>Le mot du prof</p>%s</div>" % md(s)

def cours(s):
    return md(s)

def soustitre(t):
    return "<h3>%s</h3>" % t

def qcm(items, titre="Question d'entrée", intro=""):
    h = ["<div class='qcm'><p class='lab'>%s</p>%s" % (titre, ("<p class='muted'>%s</p>" % intro) if intro else "")]
    for q, opts, ok, expl in items:
        h.append("<div class='q1' data-ok='%d'><p class='qq'>%s</p><div class='opts'>" % (ok, inl_html(q)))
        for k, o in enumerate(opts):
            h.append("<button type='button' class='opt' data-k='%d'>%s</button>" % (k, inl_html(o)))
        h.append("</div><p class='qfb' hidden></p><div class='qex' hidden>%s</div></div>" % md(expl))
    h.append("</div>")
    return "".join(h)

def indices(lst):
    if not lst: return ""
    h = ["<div class='indices'><p class='lab'>Besoin d'aide ? Ouvre les indices un par un</p>"]
    for k, t in enumerate(lst, 1):
        h.append("<details class='indice'><summary>Indice %d</summary>%s</details>" % (k, md(t)))
    return "".join(h) + "</div>"

def verif(checks):
    if not checks: return ""
    h = ["<div class='verif'><p class='lab'>Vérifie tes résultats</p>"]
    for c in checks:
        data = {"v": c["val"], "t": c.get("tol", 0.03), "e": [[a, inl_html(b)] for a, b in c.get("err", [])]}
        h.append("<div class='chk' data-c='%s'><label>%s = <input type='text' inputmode='decimal' autocomplete='off'></label> <span class='u'>%s</span> "
                 "<button type='button' class='btn ghost small'>Vérifier</button><p class='cfb' aria-live='polite'></p></div>" % (
                     html.escape(json.dumps(data), quote=True), inl_html(c["label"]), inl_html(c.get("unite", ""))))
    return "".join(h) + "</div>"

def pieges(lst):
    if not lst: return ""
    return "<div class='pieges'><p class='lab'>Les pièges</p><ul>%s</ul></div>" % "".join("<li>%s</li>" % inl_html(x) for x in lst)

# ---------------------------------------------------------------- rendu d'une étape
def _video(v, num):
    f = os.path.join(ICI, "videos", v["id"] + ".mp4")
    if os.path.exists(f):
        return ("<figure class='video'><video controls preload='metadata' src='videos/%s.mp4'></video>"
                "<figcaption><span class='tag'>Vidéo</span> %s</figcaption></figure>") % (v["id"], v["titre"])
    return ("<div class='video-attente'><p class='lab'>Vidéo %s</p><p><strong>%s</strong></p>"
            "<p>La vidéo arrive bientôt. En attendant, lis le cours et l'exemple : ils disent la même chose.</p></div>") % (num, v["titre"])

def _exo(n, titre, enonce, corr, cls="exo", avant=""):
    return ("<div class='%s'><p class='exo-n'>%s</p><div class='exo-q'>%s</div>%s"
            "<details><summary>Voir la correction</summary><div class='copie'>%s</div></details></div>") % (
        cls, (n + (" · " + titre if titre else "")), md(enonce), avant, md(corr))

def etape_html(chap, partie, e, num):
    h = ["<section class='lesson' id='%s' data-part='Partie %s · %s' data-title='%s' hidden>" % (
        e["id"], partie["lettre"], html.escape(partie["titre"], quote=True), html.escape(e["titre"], quote=True))]
    h.append("<header class='lhead'><p class='eyebrow'>%s · Partie %s · Étape %d <span class='meta'>%d min</span></p><h2>%s</h2></header>" % (
        chap["code"], partie["lettre"], num, e["duree"], e["titre"]))
    h.append("<div class='lbody'>")
    if e.get("flash"):
        h.append(qcm(e["flash"], "Questions flash", "Trois questions rapides sur ce que tu as déjà vu. Réponds sans chercher dans le cours."))
    h.append("<p class='objectif'>%s</p>" % e["objectif"])
    if e.get("entree"):
        h.append(qcm(e["entree"], "Question d'entrée", "Réponds avant de lire le cours : te tromper ici n'est pas grave, c'est ce qui fait retenir."))
    h += e["cours"]
    h.append(pieges(e.get("pieges")))
    h.append(soustitre("La vidéo"))
    h.append(_video(e["video"], num))
    ex = e["exemple"]
    h.append(soustitre("Exemple corrigé"))
    h.append("<div class='exemple'><p class='exo-n'>Exemple · %s</p>%s<div class='copie'><p class='lab'>Solution rédigée</p>%s</div></div>" % (
        ex[0], md(ex[1]), md(ex[2])))
    ap = e["application"]
    h.append(soustitre("Exercice d'application"))
    h.append("<p class='consigne'>Fais-le avec l'aide de l'exemple, puis compare avec la correction.</p>")
    h.append(_exo("Application", ap[0], ap[1], ap[2], "exo appli", indices(e.get("indices")) + verif(e.get("rep_app"))))
    h.append(soustitre("À toi de jouer"))
    h.append("<p class='consigne'>Seul, sur une feuille, sans regarder l'exemple. Ouvre la correction seulement à la fin.</p>")
    for k, x in enumerate(e["exos"], 1):
        h.append(_exo("Exercice %d" % k, x[0], x[1], x[2], "exo", verif(e.get("rep_exos", {}).get(k))))
    h.append("</div></section>")
    return "\n".join(h)

TITRES = {}

def eval_html(chap, partie):
    ev = partie["evaluation"]; eid = "%s-eval-%s" % (chap["code"].lower(), partie["lettre"].lower())
    tot = sum(x["pts"] for x in ev["exos"])
    h = ["<section class='lesson' id='%s' data-part='Partie %s · %s' data-title='Évaluation de la partie %s' hidden>" % (
        eid, partie["lettre"], html.escape(partie["titre"], quote=True), partie["lettre"])]
    h.append("<header class='lhead'><p class='eyebrow'>%s · Partie %s · Consolidation <span class='meta'>%d min</span></p><h2>Évaluation : %s</h2></header>" % (
        chap["code"], partie["lettre"], ev["duree"], partie["titre"]))
    h.append("<div class='lbody'><p class='lead'>Cette évaluation vérifie que la partie est comprise. Traite-la comme un devoir : feuille, calculatrice, chronomètre, sans le cours.</p>")
    h.append("<div class='chrono' data-min='%d'><p class='chrono-lab'>Durée conseillée : %d minutes</p><p class='chrono-t'>%02d:00</p>"
             "<div class='chrono-b'><button type='button' class='btn c-start'>Démarrer</button><button type='button' class='btn ghost c-reset'>Remettre à zéro</button></div>"
             "<p class='chrono-end' hidden>Temps écoulé : pose le stylo et corrige-toi.</p></div>" % (ev["duree"], ev["duree"], ev["duree"]))
    for k, x in enumerate(ev["exos"], 1):
        h.append("<div class='exo eval'><p class='exo-n'>Exercice %d · %s <span class='pts'>%s pts</span></p><div class='exo-q'>%s</div>"
                 "<details><summary>Correction et barème</summary><div class='copie'>%s</div></details></div>" % (
                     k, x["titre"], _pt(x["pts"]), md(x["enonce"]), md(x["corr"])))
    rev = [(k, x["revoir"]) for k, x in enumerate(ev["exos"], 1) if x.get("revoir")]
    if rev:
        rows = "".join("<tr><td>Exercice %d · %s</td><td>%s</td></tr>" % (
            k, inl_html(q), ", ".join("<a href='#%s'>%s</a>" % (eid_, TITRES.get(eid_, eid_)) for eid_ in ids))
            for k, r in rev for q, ids in r)
        h.append("<div class='retenir'><p class='lab'>Mon bilan : quoi revoir ?</p><p>Corrige-toi question par question. "
                 "Pour chaque question ratée, reprends l'étape indiquée avant de passer à la suite.</p>"
                 "<div class='table-wrap'><table><thead><tr><th>Si tu as raté…</th><th>Revois l'étape</th></tr></thead><tbody>%s</tbody></table></div></div>" % rows)
    h.append("<div class='note'><label>Ma note sur %d : <input type='number' class='score' min='0' max='%d' step='0.25' inputmode='decimal' data-tot='%d'></label>"
             "<p class='note-msg' aria-live='polite'></p></div>" % (tot, tot, tot))
    h.append("</div></section>")
    return "\n".join(h)

def _pt(p):
    return ("%g" % p).replace(".", ",")

# ---------------------------------------------------------------- page
def lire(chemin):
    return open(os.path.join(ICI, chemin), encoding="utf-8").read()

MATHJAX_CFG = r"""window.MathJax = {
  tex: { inlineMath: [['\\(','\\)']], displayMath: [['\\[','\\]']],
    macros: { vect: ['\\overrightarrow{#1}',1], U: ['\\,\\mathrm{#1}',1], ms: '\\,\\mathrm{m\\cdot s^{-1}}', mss: '\\,\\mathrm{m\\cdot s^{-2}}',
      dd: '\\mathrm{d}', R: '\\mathbb{R}' } },
  svg: { fontCache: 'global' }, startup: { typeset: false }
};"""

def page(titre, marque, sous, nav_extra, corps, key, desc):
    return """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%s</title>
<meta name="description" content="%s">
<link rel="icon" href="assets/logo.png">
<style>
%s
%s
</style>
<script>%s</script>
<script src="assets/mathjax/tex-svg.js" defer></script>
</head>
<body>
<div class="app">
  <div class="topbar">
    <button type="button" class="btn ghost" id="menu-btn" aria-controls="side" aria-expanded="false">Sommaire</button>
    <p class="brand">%s</p>
    <p class="mini" id="mini-prog"></p>
  </div>
  <div class="scrim" id="scrim" hidden></div>
  <nav class="side" id="side" aria-label="Sommaire">
    <a class="logo" href="index.html"><img src="assets/logo.png" alt="MathNexus Education" width="64" height="55"></a>
    <p class="brand">%s</p>
    <p class="brand-sub">%s</p>
    %s
    <div class="prog">
      <div class="prog-bar"><div class="prog-fill" id="prog-fill"></div></div>
      <p class="prog-txt" id="prog-txt"></p>
      <button type="button" class="linkbtn" id="reset" hidden>Remettre ma progression à zéro</button>
    </div>
    <div id="nav"></div>
  </nav>
  <main class="main" id="main">
%s
    <div class="pager">
      <a class="btn ghost" id="prev" href="#">← Étape précédente</a>
      <div class="right">
        <p class="done-note" id="done-note" hidden>Étape validée ✓</p>
        <button type="button" class="linkbtn" id="undo" hidden>Annuler</button>
        <a class="btn" id="next" href="#">Étape suivante →</a>
      </div>
    </div>
    <footer class="foot">MathNexus Education · « L'excellence par le travail et la persévérance »<br>Voix des vidéos : « Pierre », corpus UPMC (licence CC BY-SA 4.0), synthèse Piper.</footer>
  </main>
</div>
<script>
var PARCOURS_KEY = %s;
%s
</script>
</body>
</html>
""" % (titre, desc, lire("modele/style.css"), lire("modele/extra.css"), MATHJAX_CFG, marque, titre, sous, nav_extra, corps,
       json.dumps(key), __import__("contenu.graphes", fromlist=["x"]).SIMU_JS + lire("modele/site.js"))

def accueil_chap(chap):
    parts = "".join("<li><strong>Partie %s</strong> · %s (%d étapes + évaluation)</li>" % (
        p["lettre"], p["titre"], len(p["etapes"])) for p in chap["parties"])
    pdf = "series/%s.pdf" % chap["serie"]
    return """<section class='lesson' id='accueil' data-part='' data-title='Comment travailler' hidden>
<header class='lhead'><p class='eyebrow'>Bienvenue · %s</p><h2>%s</h2></header><div class='lbody'>
<p class='lead'>%s</p>
<div class='howto'>
<div><p class='num'>1</p><p><strong>Réponds à la question d'entrée</strong>, puis lis le cours. Les encadrés rouges sont à savoir par cœur ; les pièges sont ceux des copies.</p></div>
<div><p class='num'>2</p><p><strong>Regarde la vidéo</strong>, puis l'exemple corrigé ligne par ligne.</p></div>
<div><p class='num'>3</p><p><strong>Fais l'exercice d'application</strong> : ouvre les indices un par un si tu bloques, et vérifie tes résultats dans les cases.</p></div>
<div><p class='num'>4</p><p><strong>Fais seul les exercices</strong> « À toi de jouer » : vérifie tes réponses, puis compare ta rédaction à la correction.</p></div>
</div>
<p>Chaque partie commence par des <strong>questions flash</strong> sur ce que tu as déjà vu, pour ne rien oublier, et se termine par une <strong>évaluation chronométrée</strong>. Note-toi honnêtement avec le barème : en dessous de 12 sur 20, refais les étapes de la partie avant d'avancer. Le chapitre se termine par <strong>deux évaluations complètes</strong> de deux heures qui balaient tout le chapitre (avec des extraits du bac) : la première pour t'entraîner, la seconde, quelques jours plus tard, pour vérifier que tout est acquis. Un tableau te dit quelles étapes revoir selon les questions ratées.</p>
<h3>Le plan</h3><ul>%s</ul>
<div class='retenir'><p class='lab'>La série à imprimer</p><p>Les exercices « À toi de jouer » et les évaluations du chapitre sont réunis dans une série PDF à imprimer, avec le corrigé à la fin : <a href='%s'>télécharger la série %s (PDF)</a>.</p></div>
<div class='prof'><p class='lab'>Le mot du prof</p><p>Une étape par jour vaut mieux que tout le chapitre la veille du devoir. Ta progression est gardée sur cet appareil.</p></div>
</div></section>""" % (chap["code"], chap["titre"], chap["intro"], parts, pdf, chap["code"])

def build_chapitre(chap):
    secs = [accueil_chap(chap)]
    n = 0
    for p in chap["parties"]:
        for e in p["etapes"]:
            n += 1
            secs.append(etape_html(chap, p, e, n))
        secs.append(eval_html(chap, p))
    for k, fin in enumerate(chap.get("finals", []), 1):
        fp = dict(lettre="Z%d" % k, titre="Évaluation %d du chapitre" % k, evaluation=fin)
        h = eval_html(chap, fp)
        role = "entraînement" if k == 1 else "contrôle"
        h = h.replace("data-part='Partie Z%d · Évaluation %d du chapitre' data-title='Évaluation de la partie Z%d'" % (k, k, k),
                      "data-part='Bilan du chapitre' data-title='Évaluation %d (%s)'" % (k, role))
        h = h.replace("%s · Partie Z%d · Consolidation" % (chap["code"], k), "%s · Bilan du chapitre · Évaluation %d" % (chap["code"], k))
        h = h.replace("Évaluation : Évaluation %d du chapitre" % k, "Évaluation %d : %s" % (k, chap["titre"]))
        h = h.replace("Cette évaluation vérifie que la partie est comprise.",
                      "Ce sujet balaie tout le chapitre, comme un devoir de deux heures. Évaluation %d : %s." % (
                          k, "fais-la après la dernière partie, pour t'entraîner" if k == 1 else "fais-la quelques jours plus tard, sans revoir le cours : elle dit si le chapitre est acquis"))
        secs.append(h)
    nav_extra = "<p class='brand-sub'><a href='index.html'>← Tous les chapitres</a></p>"
    out = page("%s · %s" % (chap["code"], chap["titre"]), "%s · %s" % (chap["code"], chap["titre_court"]),
               "Sciences physiques · Terminale S2", nav_extra, "\n".join(secs), "ts2-" + chap["code"].lower(),
               "%s %s : cours pas à pas, vidéos, exercices corrigés et évaluations (Terminale S2)." % (chap["code"], chap["titre"]))
    open(os.path.join(ICI, chap["fichier"]), "w", encoding="utf-8").write(out)
    return n

# ---------------------------------------------------------------- page d'accueil du site
PROGRAMME = [
    ("P1", "Cinématique du point", "p1.html"), ("P2", "Bases de la dynamique", "p2.html"),
    ("P3", "Applications des bases de la dynamique", None), ("P4", "Gravitation universelle", None),
    ("P5", "Généralités sur les champs magnétiques", None), ("P6", "Particule chargée dans un champ magnétique uniforme", None),
    ("P7", "Loi de Laplace", None), ("P8", "Induction électromagnétique", None), ("P9", "Dipôle RC", None),
    ("P10", "Oscillations électriques libres et forcées", None), ("P11", "Oscillations mécaniques libres", None),
    ("P12", "Interférences lumineuses", None), ("P13", "Effet photoélectrique", None),
    ("P14", "Niveaux d'énergie de l'atome", None), ("P15", "Réactions nucléaires", None),
]

def build_index(chaps):
    by = {c["code"]: c for c in chaps}
    cards = []
    for code, titre, f in PROGRAMME:
        if f and code in by:
            c = by[code]
            ne = sum(len(p["etapes"]) for p in c["parties"])
            cards.append("<a class='card' href='%s'><span class='c-code'>%s</span><span class='c-t'>%s</span>"
                         "<span class='c-m'>%d parties · %d étapes · %d évaluations</span><span class='c-go'>Commencer →</span></a>" % (
                             f, code, titre, len(c["parties"]), ne, len(c["parties"])))
        else:
            cards.append("<div class='card off'><span class='c-code'>%s</span><span class='c-t'>%s</span><span class='c-m'>Bientôt</span></div>" % (code, titre))
    pdfs = "".join("<li><a href='series/%s.pdf'>Série %s · %s (PDF, corrigé à la fin)</a></li>" % (c["serie"], c["code"], c["titre"]) for c in chaps)
    corps = """<section class='lesson' id='accueil' data-part='' data-title='Accueil' hidden>
<header class='lhead'><p class='eyebrow'>MathNexus Education · Terminale S2</p><h2>Sciences physiques, pas à pas</h2></header><div class='lbody'>
<p class='lead'>Le programme de physique de Terminale S2, chapitre par chapitre. Chaque étape suit le même rythme : une vidéo, un exemple corrigé, un exercice d'application, puis des exercices à faire seul. Chaque partie se termine par une évaluation.</p>
<h3>Physique</h3>
<div class='cards'>%s</div>
<h3>Les séries à imprimer</h3><ul>%s</ul>
<p class='muted'>La chimie arrive ensuite, sur le même modèle.</p>
</div></section>""" % ("".join(cards), pdfs)
    out = page("Sciences physiques TS2", "Sciences physiques TS2", "MathNexus Education · Terminale S2",
               "<p class='brand-sub'><a href='../index.html'>← Accueil MathNexus Terminale S2</a></p>",
               corps, "ts2-accueil", "Sciences physiques Terminale S2 : vidéos, exercices corrigés et évaluations, chapitre par chapitre.")
    open(os.path.join(ICI, "index.html"), "w", encoding="utf-8").write(out)

# ---------------------------------------------------------------- textes des vidéos (à enregistrer)
def build_scripts(chaps):
    secs, tot = [], 0
    os.makedirs(os.path.join(ICI, "outils", "video", "scripts"), exist_ok=True)
    for c in chaps:
        secs.append("<h2 class='sc-chap'>%s · %s</h2>" % (c["code"], c["titre"]))
        n = 0
        for p in c["parties"]:
            for e in p["etapes"]:
                n += 1
                v = e["video"]; tot += len(v["phrases"])
                json.dump(v, open(os.path.join(ICI, "outils", "video", "scripts", v["id"] + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                lis = "".join("<li><span class='n'>%d</span><p>%s</p></li>" % (k, html.escape(ph[0])) for k, ph in enumerate(v["phrases"], 1))
                secs.append("<section class='vid'><h3><span class='f'>%s.mp3</span>%s</h3><p class='meta'>%s · Étape %d · %d phrases</p><ol>%s</ol></section>" % (
                    v["id"], v["titre"], c["code"], n, len(v["phrases"]), lis))
    out = """<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Textes des vidéos · TS2</title><style>%s</style></head><body><main>
<h1>Textes des vidéos · P1 et P2</h1><p class="sub">Sciences physiques TS2 · MathNexus Education · %d phrases au total</p>
<div class="guide"><h2>Comment enregistrer</h2><ol>
<li>Un fichier audio par vidéo, nommé comme indiqué en rouge (par exemple <b>p1-a1.mp3</b>). Le format importe peu : mp3, m4a ou wav.</li>
<li>Pièce calme, téléphone à 20 cm de la bouche, même endroit pour tous les enregistrements.</li>
<li>Lis les phrases dans l'ordre, d'une voix posée, comme en classe.</li>
<li><b>Entre deux numéros, fais une pause de 2 secondes en silence.</b> C'est ce qui permet de caler chaque phrase sur la bonne image.</li>
<li>Si tu te trompes, recommence la vidéo depuis le début : chaque fichier dure environ deux minutes.</li>
</ol></div>%s</main></body></html>""" % (lire("modele/scripts.css"), tot, "\n".join(secs))
    open(os.path.join(ICI, "scripts.html"), "w", encoding="utf-8").write(out)
    return tot

# ---------------------------------------------------------------- séries PDF
def build_serie(chap, compile_pdf):
    d = os.path.join(ICI, "series"); os.makedirs(d, exist_ok=True)
    for f in ("mathnexus.sty", "logo.png"):
        shutil.copy(os.path.join(ICI, "outils", "latex", f), d)
    en, co, k = [], [], 0
    for p in chap["parties"]:
        en.append("\\sujet{Partie %s · %s}" % (p["lettre"], p["titre"]))
        co.append("\\sujet{Partie %s · %s}" % (p["lettre"], p["titre"]))
        for e in p["etapes"]:
            for x in e["exos"]:
                k += 1
                en.append("\\Exo{%d}{%s}{}\n%s" % (k, inl_tex(x[0][0].upper() + x[0][1:]), md_tex(x[1])))
                co.append("\\Exo{%d}{%s}{}\n%s" % (k, inl_tex(x[0][0].upper() + x[0][1:]), md_tex(x[2])))
        for x in p["evaluation"]["exos"]:
            k += 1
            en.append("\\Exo{%d}{%s (synthèse)}{%s}\n%s" % (k, inl_tex(x["titre"]), _pt(x["pts"]), md_tex(x["enonce"])))
            co.append("\\Exo{%d}{%s (synthèse)}{%s}\n%s" % (k, inl_tex(x["titre"]), _pt(x["pts"]), md_tex(x["corr"])))
    for j, fin in enumerate(chap.get("finals", []), 1):
        en.append("\\newpage\\sujet{Évaluation %d du chapitre (%d min)}" % (j, fin["duree"]))
        co.append("\\sujet{Évaluation %d du chapitre}" % j)
        for x in fin["exos"]:
            k += 1
            en.append("\\Exo{%d}{%s}{%s}\n%s" % (k, inl_tex(x["titre"]), _pt(x["pts"]), md_tex(x["enonce"])))
            co.append("\\Exo{%d}{%s}{%s}\n%s" % (k, inl_tex(x["titre"]), _pt(x["pts"]), md_tex(x["corr"])))
    tex = lire("outils/latex/serie_pre.tex") % {"code": chap["code"], "titre": chap["titre"]}
    tex += "\\mntitreserie{%s}{%s}\n\n" % (chap["code"], chap["titre"])
    tex += "\n\n".join(en)
    tex += "\n\n\\newpage\n\\mntitreserie{}{Corrigé de la série %s}\n\n" % chap["code"] + "\n\n".join(co)
    tex += "\n\\label{mnlast}\n\\end{document}\n"
    nom = chap["serie"]
    open(os.path.join(d, nom + ".tex"), "w", encoding="utf-8").write(tex)
    if compile_pdf:
        for _ in range(3):
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", nom + ".tex"], cwd=d,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        if r.returncode:
            print(r.stdout.decode("utf-8", "replace")[-3000:]); raise SystemExit("échec LaTeX : " + nom)
        for ext in ("aux", "log", "out"):
            try: os.remove(os.path.join(d, nom + "." + ext))
            except OSError: pass
    return k

# ---------------------------------------------------------------- main
def main():
    from contenu import p1, p2, p1x, p2x
    chaps = [p1.CHAP, p2.CHAP]
    for c, x in ((p1.CHAP, p1x), (p2.CHAP, p2x)):
        for p in c["parties"]:
            if p["lettre"] in x.FLASH:
                p["etapes"][0]["flash"] = x.FLASH[p["lettre"]]
            for e in p["etapes"]:
                e.update(x.EXTRA.get(e["id"], {}))
        c["finals"] = x.FINALS
        for p in c["parties"]:
            for e in p["etapes"]:
                TITRES[e["id"]] = e["titre"]
    for c in chaps:
        n = build_chapitre(c)
        k = build_serie(c, "--pdf" in sys.argv)
        print("%s : %d parties, %d étapes, %d exercices dans la série" % (c["code"], len(c["parties"]), n, k))
    build_index(chaps)
    print("textes des vidéos :", build_scripts(chaps), "phrases")

if __name__ == "__main__":
    main()
