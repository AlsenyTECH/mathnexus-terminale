# Sciences physiques TS2 · MathNexus Education

Site d'apprentissage pas à pas pour la Terminale S2 (programme sénégalais) : chaque étape
enchaîne **cours → vidéo → exemple corrigé → exercice d'application → exercices à faire seul**,
et chaque partie se termine par **une évaluation chronométrée** (consolidation, avec barème).
Chaque chapitre a sa **série PDF à imprimer** (exercices + évaluations, corrigé à la fin).

État : **P1 Cinématique du point** (5 parties, 10 étapes) et **P2 Bases de la dynamique**
(4 parties, 8 étapes). P3 à P15 puis la chimie suivront sur le même modèle.

## Publier

Ce dossier est la partie physique du site https://alsenytech.github.io/mathnexus-terminale/
(adresse : `…/mathnexus-terminale/physique/`). Le site est statique : `index.html`, `p1.html`,
`p2.html`, `scripts.html`, `assets/`, `videos/`, `series/`. Les commandes ci-dessous se lancent
depuis ce dossier `physique/`.
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

## Vidéos (voix de MathNexus)

1. Ouvrir `scripts.html` : un texte par vidéo, phrases numérotées.
2. Enregistrer un fichier par vidéo (`p1-a1.m4a`…) avec **2 s de silence entre deux phrases**.
3. `python3 outils/video/monter.py p1-a1 chemin/p1-a1.m4a` puis `python3 build.py`.

Le montage cale chaque phrase sur son image (détection des silences) et écrit `videos/<id>.mp4`.
Prévoir Git LFS si les vidéos deviennent nombreuses (`git lfs track "videos/*.mp4"`).

Licences : MathJax (Apache 2.0) et polices Caveat, Kalam, Source Sans 3 (SIL OFL 1.1), voir `assets/`.
