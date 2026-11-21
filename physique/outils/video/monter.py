# -*- coding: utf-8 -*-
"""Monte une vidéo d'étape à partir de TON enregistrement audio.

    python3 outils/video/monter.py p1-a1 enregistrements/p1-a1.m4a
    python3 build.py        # la vidéo apparaît alors dans l'étape

Principe : l'enregistrement suit les phrases de outils/video/scripts/<id>.json, séparées par
des silences d'environ 2 s. Les silences sont détectés (ffmpeg silencedetect) pour caler chaque
phrase sur son image ; chaque image affiche la formule « ecran » de la phrase (rendue par MathJax,
capturée par Playwright en 1280x720). Résultat : videos/<id>.mp4.
Si le nombre de silences ne correspond pas, les durées sont réparties selon la longueur des phrases.

Prérequis : ffmpeg, Python Playwright (pip install playwright ; playwright install chromium).
"""
import json, os, re, subprocess, sys, tempfile

ICI = os.path.dirname(os.path.abspath(__file__))
RACINE = os.path.dirname(os.path.dirname(ICI))


def duree(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", f],
                       stdout=subprocess.PIPE, check=True)
    return float(r.stdout)


def coupes(audio, n, total):
    """Milieux des n-1 plus longs silences, dans l'ordre chronologique."""
    for seuil, d in ((-35, 1.2), (-30, 1.0), (-40, 1.0), (-28, 0.8)):
        r = subprocess.run(["ffmpeg", "-hide_banner", "-i", audio, "-af", "silencedetect=noise=%ddB:d=%s" % (seuil, d), "-f", "null", "-"],
                           stderr=subprocess.PIPE)
        log = r.stderr.decode("utf-8", "replace")
        deb = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]
        fin = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
        sil = [(a, b) for a, b in zip(deb, fin) if a > 0.3 and b < total - 0.3]
        if len(sil) >= n - 1:
            sil = sorted(sorted(sil, key=lambda s: s[1] - s[0], reverse=True)[:n - 1])
            return [(a + b) / 2 for a, b in sil]
    return None


PAGE = r"""<!doctype html><html lang="fr"><head><meta charset="utf-8">
<style>
@font-face{font-family:'Caveat';src:url(%(a)s/fonts/caveat-latin-700-normal.woff2) format('woff2');font-weight:700}
@font-face{font-family:'Source Sans 3';src:url(%(a)s/fonts/source-sans-3-latin-600-normal.woff2) format('woff2');font-weight:600}
html,body{margin:0;width:1280px;height:720px;overflow:hidden}
body{background:#f7f9fc;color:#1b2440;font-family:'Source Sans 3',sans-serif;
 background-image:linear-gradient(#e3e9f5 1px,transparent 1px),linear-gradient(90deg,#e3e9f5 1px,transparent 1px);background-size:32px 32px;
 display:flex;flex-direction:column}
header{display:flex;align-items:center;gap:18px;padding:22px 40px;border-bottom:3px solid #bd1f2b;background:#fff}
header img{height:64px}
header .t{font-family:'Caveat',cursive;font-size:44px;color:#bd1f2b;font-weight:700;line-height:1}
header .c{margin-left:auto;font-size:22px;color:#586381;font-weight:600}
main{flex:1;display:flex;align-items:center;justify-content:center;padding:20px 60px;text-align:center;font-size:54px;color:#1c3bb0}
footer{padding:14px 40px;font-size:18px;color:#586381;background:#fff;border-top:1px solid #d6ddec}
</style>
<script>window.MathJax={tex:{inlineMath:[['\\(','\\)']],macros:{vect:['\\overrightarrow{#1}',1]}},svg:{fontCache:'none'}};</script>
<script src="%(a)s/mathjax/tex-svg.js"></script></head><body>
<header><img src="%(a)s/logo.png"><span class="t">%(titre)s</span><span class="c">%(chap)s</span></header>
<main id="m"></main><footer>MathNexus Education · Sciences physiques TS2</footer>
<script>var e=%(ecran)s;var m=document.getElementById('m');
if(/[\\^_{}]|\\[a-zA-Z]/.test(e)){m.innerHTML='\\('+e+'\\)';}else{m.textContent=e;m.style.fontFamily="'Caveat',cursive";m.style.fontSize='72px';m.style.color='#bd1f2b';}
</script></body></html>"""


def images(script, dossier):
    from playwright.sync_api import sync_playwright
    a = "file://" + os.path.join(RACINE, "assets")
    chap = script["id"].split("-")[0].upper()
    fichiers = []
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1280, "height": 720})
        for k, (voix, ecran) in enumerate(script["phrases"]):
            h = os.path.join(dossier, "s%02d.html" % k)
            open(h, "w", encoding="utf-8").write(PAGE % {"a": a, "titre": script["titre"], "chap": chap, "ecran": json.dumps(ecran)})
            pg.goto("file://" + h)
            pg.wait_for_function("!window.MathJax || !MathJax.startup || MathJax.startup.promise", timeout=10000)
            pg.evaluate("window.MathJax && MathJax.startup ? MathJax.startup.promise : null")
            pg.wait_for_timeout(200)
            png = os.path.join(dossier, "s%02d.png" % k)
            pg.screenshot(path=png)
            fichiers.append(png)
        b.close()
    return fichiers


def main(vid, audio):
    script = json.load(open(os.path.join(ICI, "scripts", vid + ".json"), encoding="utf-8"))
    n = len(script["phrases"]); total = duree(audio)
    c = coupes(audio, n, total)
    if c is None:
        poids = [len(v) for v, _ in script["phrases"]]; s = sum(poids); c = []; acc = 0
        for w in poids[:-1]:
            acc += w; c.append(total * acc / s)
        print("silences introuvables : répartition selon la longueur des phrases")
    bornes = [0.0] + c + [total + 0.8]
    tmp = tempfile.mkdtemp()
    pngs = images(script, tmp)
    liste = os.path.join(tmp, "liste.txt")
    with open(liste, "w") as f:
        for k, png in enumerate(pngs):
            f.write("file '%s'\nduration %.3f\n" % (png, bornes[k + 1] - bornes[k]))
        f.write("file '%s'\n" % pngs[-1])
    sortie = os.path.join(RACINE, "videos", vid + ".mp4")
    os.makedirs(os.path.dirname(sortie), exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", liste, "-i", audio,
                    "-af", "apad=pad_dur=0.8,loudnorm=I=-16:TP=-1.5", "-c:v", "libx264", "-r", "25", "-pix_fmt", "yuv420p",
                    "-tune", "stillimage", "-c:a", "aac", "-b:a", "96k", "-ac", "1", "-shortest", "-movflags", "+faststart", sortie], check=True)
    print("%s : %d phrases, %.0f s, %.1f Mo" % (sortie, n, total, os.path.getsize(sortie) / 1e6))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
