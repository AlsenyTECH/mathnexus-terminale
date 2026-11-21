# Sciences physiques TS2 · MathNexus Education

Site d'apprentissage pas à pas pour la Terminale S2 (programme sénégalais) : chaque étape
enchaîne **cours → vidéo → exemple corrigé → exercice d'application → exercices à faire seul**,
et chaque partie se termine par **une évaluation chronométrée** (consolidation, avec barème).
Chaque chapitre a sa **série PDF à imprimer** (exercices + évaluations, corrigé à la fin).

État : **P1 Cinématique du point** (5 parties, 10 étapes) et **P2 Bases de la dynamique**
(4 parties, 8 étapes). P3 à P15 puis la chimie suivront sur le même modèle.

## Publier

Le site est statique : `index.html`, `p1.html`, `p2.html`, `scripts.html`, `assets/`, `videos/`, `series/`.
Avec GitHub Pages : *Settings → Pages → Deploy from a branch → main, / (root)*.
Il fonctionne aussi hors connexion (MathJax et polices embarqués) : ouvrir `index.html`.

## Construire

```bash
python3 build.py          # régénère les pages HTML et scripts.html
python3 build.py --pdf    # + compile les séries PDF (pdflatex, babel-french, tcolorbox)
```

Ne pas modifier les .html à la main : ils sont écrasés à chaque build.

## Organisation

```
build.py                 générateur (mini-markup → HTML et LaTeX)
contenu/p1a.py, p1b.py   P1 : parties A-B-C et D-E (cours, vidéos, exemples, exercices, évaluations)
contenu/p2a.py, p2b.py   P2 : parties A-B et C-D
contenu/p1x.py, p2x.py   questions d'entrée, indices, réponses vérifiées, pièges, questions flash, évaluation complète
contenu/graphes.py       graphes (SVG et pgfplots) et simulations
contenu/p1.py, p2.py     assemblage des chapitres
modele/                  style.css (cahier quadrillé / tableau noir), extra.css, site.js
outils/latex/            mathnexus.sty, logo, préambule des séries
outils/video/            scripts/*.json (textes des vidéos) et monter.py (montage)
series/                  séries PDF générées
videos/                  vidéos .mp4 (une étape sans vidéo affiche « vidéo à venir »)
```

### Écrire du contenu

Chaque étape est un dictionnaire : `objectif`, `cours` (briques `retenir`, `prof`, `cours`),
`video` (phrases à lire + formule affichée), `exemple`, `application`, `exos`.
Le texte utilise un mini-markup : `$...$` formule, `$$...$$` formule centrée, `- ` liste,
`1. ` questions, `| a | b |` tableau, `**gras**`. Macros : `\vect{}`, `\U{}`, `\ms`, `\mss`, `\dd`.

## Vidéos

Narration actuelle : voix « Pierre » (Piper `fr_FR-upmc-medium`, locuteur 1, CC BY-SA 4.0 — attribution affichée en pied de page).

```bash
export VOIX_DIR=~/voices/vits-piper-fr_FR-upmc-medium   # archive sherpa-onnx « vits-piper-fr_FR-upmc-medium »
python3 outils/video/monter.py p1-a1 --pierre
```

Une autre voix au même format (.onnx Piper, par exemple celle de MathNexus après entraînement) se branche avec `VOIX_ONNX` et `VOIX_LOCUTEUR`.

### Avec un enregistrement

1. Ouvrir `scripts.html` : un texte par vidéo, phrases numérotées.
2. Enregistrer un fichier par vidéo (`p1-a1.m4a`…) avec **2 s de silence entre deux phrases**.
3. `python3 outils/video/monter.py p1-a1 chemin/p1-a1.m4a` puis `python3 build.py`.

Le montage cale chaque phrase sur son image (détection des silences) et écrit `videos/<id>.mp4`.
Prévoir Git LFS si les vidéos deviennent nombreuses (`git lfs track "videos/*.mp4"`).

Licences : MathJax (Apache 2.0) et polices Caveat, Kalam, Source Sans 3 (SIL OFL 1.1), voir `assets/`.
