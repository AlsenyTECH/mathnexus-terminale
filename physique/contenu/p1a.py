# -*- coding: utf-8 -*-
"""P1 Cinématique du point : parties A (repérage), B (Frenet), C (mouvements rectilignes)."""
from build import retenir, prof, cours, soustitre

# =====================================================================
# PARTIE A — Repérage, équations horaires, vitesse et accélération
# =====================================================================
A1 = dict(
    id="p1-a1", titre="Repère, équations horaires et trajectoire", duree=15,
    objectif="Savoir repérer un mobile dans un repère, lire ses équations horaires et trouver l'équation de sa trajectoire.",
    cours=[
        cours(r"""
        Étudier un mouvement, c'est d'abord choisir **par rapport à quoi** on l'observe : c'est le **référentiel** (le sol, un train, la Terre…). Dans ce référentiel, on fixe un **repère** $(O;\vec i,\vec j)$ et une origine des dates.

        La position du mobile $M$ à la date $t$ est donnée par son **vecteur position** :

        $$\vect{OM}=x(t)\,\vec i+y(t)\,\vec j$$

        Les fonctions $x(t)$ et $y(t)$ sont les **équations horaires** du mouvement. La **trajectoire** est l'ensemble des positions occupées : c'est une courbe, et son équation ne contient plus le temps.
        """),
        retenir("Trouver l'équation de la trajectoire", r"""
        1. Dans l'équation la plus simple (souvent $x(t)$), j'exprime $t$ en fonction de $x$.
        2. Je remplace $t$ dans l'autre équation.
        3. J'obtiens $y=f(x)$ et je reconnais la courbe : droite ($y=ax+b$), parabole ($y=ax^2+bx+c$), cercle ($x^2+y^2=R^2$).
        """),
        prof(r"""
        Pour un cercle, on n'exprime pas $t$ : on calcule $x^2+y^2$ et on utilise $\cos^2+\sin^2=1$.
        """),
    ],
    video=dict(id="p1-a1", titre="Des équations horaires à la trajectoire", phrases=[
        ("Des équations horaires à la trajectoire.", "Des équations horaires à la trajectoire"),
        ("Un mobile se déplace dans un plan muni d'un repère O, i, j. À chaque date t, sa position est donnée par le vecteur O M, de coordonnées x de t et y de t.", r"\vect{OM}=x(t)\,\vec i+y(t)\,\vec j"),
        ("Ces deux fonctions s'appellent les équations horaires. Prenons x égale deux t, et y égale t au carré moins un.", r"x=2t\qquad y=t^2-1"),
        ("Premier réflexe : placer une position. À la date t égale un seconde, x vaut deux et y vaut zéro. Le mobile est au point de coordonnées deux, zéro.", r"t=1\ \mathrm{s}:\ M(2\,;\,0)"),
        ("Maintenant, la trajectoire. On veut une relation entre x et y, sans le temps. Dans la première équation, t égale x sur deux.", r"t=\dfrac{x}{2}"),
        ("On remplace t dans la deuxième équation : y égale x sur deux, au carré, moins un, soit x carré sur quatre, moins un.", r"y=\dfrac{x^2}{4}-1"),
        ("C'est l'équation d'une parabole. Attention : comme t est positif, x l'est aussi. Le mobile ne décrit que la branche de droite.", r"\text{parabole, }x\geq 0"),
        ("À retenir : on isole t dans l'équation la plus simple, puis on remplace. Pour un cercle, on calcule plutôt x carré plus y carré.", r"\text{isoler }t\ \to\ \text{remplacer}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape, sur une feuille.", "À toi de jouer"),
    ]),
    exemple=("une parabole", r"""
    Un mobile se déplace dans le plan. Ses équations horaires sont $x=2t$ et $y=t^2-1$ ($x$, $y$ en m ; $t$ en s ; $t\geq 0$).

    1. Où est le mobile à $t=1\U{s}$ ? À quelle distance de $O$ ?
    2. Déterminer l'équation de la trajectoire.
    """, r"""
    1. À $t=1\U{s}$ : $x=2\times1=2\U{m}$ et $y=1^2-1=0$. Le mobile est en $M(2\,;\,0)$ et $OM=\sqrt{2^2+0^2}=2\U{m}$.
    2. De $x=2t$ on tire $t=\dfrac{x}{2}$. On remplace : $y=\left(\dfrac{x}{2}\right)^2-1$, soit $y=\dfrac{x^2}{4}-1$. La trajectoire est une **portion de parabole** ($x\geq0$ car $t\geq0$).

    [[graphe:p1-a1-traj]]
    """),
    application=("une droite", r"""
    Les équations horaires d'un mobile sont $x=3t+1$ et $y=-2t+4$ (unités SI).

    1. Donner la position du mobile à $t=0$ et à $t=2\U{s}$.
    2. Déterminer l'équation de la trajectoire et la nommer.
    """, r"""
    1. À $t=0$ : $M_0(1\,;\,4)$. À $t=2\U{s}$ : $x=7\U{m}$, $y=0$, donc $M(7\,;\,0)$.
    2. $t=\dfrac{x-1}{3}$, donc $y=-2\times\dfrac{x-1}{3}+4=-\dfrac{2}{3}x+\dfrac{14}{3}$. C'est une **droite** : le mouvement est rectiligne.
    """),
    exos=[
        ("un cercle", r"""
        Un point $M$ a pour équations horaires $x=4\cos(2t)$ et $y=4\sin(2t)$ (SI).

        1. Calculer $x^2+y^2$.
        2. En déduire la nature de la trajectoire et ses caractéristiques.
        """, r"""
        1. $x^2+y^2=16\cos^2(2t)+16\sin^2(2t)=16\,(\cos^2+\sin^2)=16$.
        2. $x^2+y^2=4^2$ : la trajectoire est le **cercle de centre $O$ et de rayon $4\U{m}$**.
        """),
        ("lire une parabole", r"""
        Un mobile a pour équations horaires $x=t$ et $y=-5t^2+10t$ (SI, $t\geq0$).

        1. Montrer que la trajectoire a pour équation $y=-5x^2+10x$.
        2. Pour quelles valeurs de $x$ le mobile est-il sur l'axe $(Ox)$ ?
        3. Quelle est l'ordonnée maximale atteinte ?
        """, r"""
        1. $t=x$, donc $y=-5x^2+10x$.
        2. $y=0\iff x(-5x+10)=0\iff x=0$ ou $x=2\U{m}$.
        3. Le sommet de la parabole est au milieu des racines : $x=1\U{m}$, et $y=-5+10=5\U{m}$.
        """),
    ],
)

A2 = dict(
    id="p1-a2", titre="Vecteurs vitesse et accélération", duree=15,
    objectif="Calculer les composantes et la valeur des vecteurs vitesse et accélération à partir des équations horaires.",
    cours=[
        cours(r"""
        Le **vecteur vitesse** est la dérivée du vecteur position par rapport au temps ; le **vecteur accélération** est la dérivée du vecteur vitesse.
        """),
        retenir("Vitesse et accélération dans un repère", r"""
        $$\vec v=\frac{\dd\vect{OM}}{\dd t}\quad\begin{cases}v_x=\dot x\\ v_y=\dot y\end{cases}\qquad\qquad \vec a=\frac{\dd\vec v}{\dd t}\quad\begin{cases}a_x=\dot v_x=\ddot x\\ a_y=\dot v_y=\ddot y\end{cases}$$

        - Valeurs : $v=\sqrt{v_x^2+v_y^2}$ (en $\mathrm{m\cdot s^{-1}}$) et $a=\sqrt{a_x^2+a_y^2}$ (en $\mathrm{m\cdot s^{-2}}$).
        - Le vecteur vitesse est **tangent à la trajectoire** et orienté dans le sens du mouvement.
        """),
        prof(r"""
        Le chemin inverse sert aussi : si on connaît $\vec a$ ou $\vec v$, on retrouve les équations horaires en cherchant une **primitive**, et les constantes avec les conditions initiales (position et vitesse à $t=0$).
        """),
    ],
    video=dict(id="p1-a2", titre="Dériver pour trouver la vitesse et l'accélération", phrases=[
        ("Dériver pour trouver la vitesse et l'accélération.", "Vitesse et accélération"),
        ("Le vecteur vitesse est la dérivée du vecteur position par rapport au temps. Ses coordonnées sont les dérivées de x et de y.", r"v_x=\dot x\qquad v_y=\dot y"),
        ("Le vecteur accélération est la dérivée du vecteur vitesse. Ses coordonnées sont les dérivées de v x et de v y.", r"a_x=\dot v_x\qquad a_y=\dot v_y"),
        ("Reprenons x égale deux t, et y égale t carré moins un. On dérive : v x égale deux, v y égale deux t.", r"\vec v\,(2\,;\,2t)"),
        ("À t égale un seconde, le vecteur vitesse a pour coordonnées deux et deux. Sa valeur est racine de quatre plus quatre, soit deux racine de deux, environ deux virgule huit mètres par seconde.", r"v=\sqrt{2^2+2^2}\approx 2{,}83\ \mathrm{m\cdot s^{-1}}"),
        ("On dérive encore : a x égale zéro, a y égale deux. L'accélération est constante, elle vaut deux mètres par seconde carrée.", r"\vec a\,(0\,;\,2)\quad a=2\ \mathrm{m\cdot s^{-2}}"),
        ("Le vecteur vitesse est toujours tangent à la trajectoire. Fais toujours la phrase : je dérive x, je dérive y, puis je calcule la norme.", r"v=\sqrt{v_x^2+v_y^2}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("dériver deux fois", r"""
    Équations horaires : $x=2t$ et $y=t^2-1$ (SI).

    1. Déterminer les coordonnées du vecteur vitesse, puis sa valeur à $t=1\U{s}$.
    2. Déterminer le vecteur accélération. Que remarque-t-on ?
    """, r"""
    1. $v_x=\dot x=2$ et $v_y=\dot y=2t$. À $t=1\U{s}$ : $\vec v\,(2\,;\,2)$ et $v=\sqrt{4+4}=2\sqrt2\approx2{,}83\ms$.
    2. $a_x=\dot v_x=0$ et $a_y=\dot v_y=2$ : $\vec a\,(0\,;\,2)$, $a=2\mss$. L'accélération est **constante** (même valeur, même direction à toute date).
    """),
    application=("vitesse à une date", r"""
    Un mobile a pour équations horaires $x=3t^2-2t$ et $y=4t$ (SI).

    1. Exprimer $v_x$, $v_y$, puis calculer $v$ à $t=2\U{s}$.
    2. Déterminer $\vec a$ et sa valeur.
    """, r"""
    1. $v_x=6t-2$ et $v_y=4$. À $t=2\U{s}$ : $v_x=10\ms$, $v_y=4\ms$, $v=\sqrt{100+16}=\sqrt{116}\approx10{,}8\ms$.
    2. $a_x=6$ et $a_y=0$ : $\vec a=6\,\vec i$, $a=6\mss$, constante.
    """),
    exos=[
        ("quand la vitesse s'annule", r"""
        Un mobile a pour équations horaires $x=-t^2+4t$ et $y=3$ (SI).

        1. Quelle est la nature de la trajectoire ?
        2. À quelle date la vitesse s'annule-t-elle ? Où est alors le mobile ?
        3. Donner le vecteur accélération.
        """, r"""
        1. $y=3$ est constant : la trajectoire est la **droite** d'équation $y=3$, le mouvement est rectiligne.
        2. $v_x=-2t+4$ et $v_y=0$. $v=0\iff t=2\U{s}$. Alors $x=-4+8=4\U{m}$ : le mobile est en $(4\,;\,3)$, il fait demi-tour.
        3. $a_x=-2$, $a_y=0$ : $\vec a=-2\,\vec i$, $a=2\mss$.
        """),
        ("le chemin inverse", r"""
        Le vecteur vitesse d'un mobile est $\vec v\,(2\,;\,-10t+5)$ (SI). À $t=0$, le mobile est en $O$.

        1. Déterminer les équations horaires $x(t)$ et $y(t)$.
        2. Déterminer le vecteur accélération.
        """, r"""
        1. On cherche des primitives : $x=2t+x_0$ et $y=-5t^2+5t+y_0$. À $t=0$, le mobile est en $O$ : $x_0=y_0=0$. Donc $x=2t$ et $y=-5t^2+5t$.
        2. $a_x=0$ et $a_y=-10$ : $\vec a\,(0\,;\,-10)$, $a=10\mss$.
        """),
    ],
)

EVAL_A = dict(duree=35, exos=[
    dict(titre="Mouvement dans un plan", pts=10, enonce=r"""
    Dans un repère $(O;\vec i,\vec j)$, un mobile a pour équations horaires $x=2t$ et $y=-t^2+4t$ ($x$, $y$ en m, $t$ en s, $t\geq0$).

    1. Déterminer l'équation de la trajectoire et la nommer.
    2. Déterminer les coordonnées du vecteur vitesse à une date $t$.
    3. À quelle date $t_1$ le vecteur vitesse est-il horizontal ? Donner la position du mobile et la valeur de sa vitesse à cette date.
    4. Déterminer le vecteur accélération et sa valeur.
    """, corr=r"""
    1. $t=\dfrac{x}{2}$, donc $y=-\dfrac{x^2}{4}+2x$ : **parabole** (portion $x\geq0$). **(2 pts)**
    2. $v_x=2$ et $v_y=-2t+4$. **(2 pts)**
    3. Vecteur vitesse horizontal $\iff v_y=0\iff t_1=2\U{s}$. Position : $x=4\U{m}$, $y=-4+8=4\U{m}$. Vitesse : $v=\sqrt{2^2+0^2}=2\ms$. **(4 pts)**
    4. $a_x=0$, $a_y=-2$ : $\vec a=-2\,\vec j$, $a=2\mss$, constant. **(2 pts)**

    Remarque : au sommet de la parabole, la vitesse n'est pas nulle, elle est horizontale.
    """),
    dict(titre="Retrouver les équations horaires", pts=10, enonce=r"""
    Le vecteur vitesse d'un mobile est $\vec v=4\,\vec i+(-2t+2)\,\vec j$ (SI). À $t=0$, le mobile est au point $M_0(0\,;\,1)$.

    1. Déterminer les équations horaires du mouvement.
    2. Déterminer l'équation de la trajectoire.
    3. Calculer la valeur de la vitesse à $t=0$.
    4. Déterminer le vecteur accélération. À quelle date et en quel point le mobile atteint-il son ordonnée maximale ?
    """, corr=r"""
    1. Primitives : $x=4t+x_0$, $y=-t^2+2t+y_0$. Avec $M_0(0\,;\,1)$ : $x=4t$ et $y=-t^2+2t+1$. **(3 pts)**
    2. $t=\dfrac{x}{4}$, donc $y=-\dfrac{x^2}{16}+\dfrac{x}{2}+1$ : parabole. **(2 pts)**
    3. $\vec v_0\,(4\,;\,2)$, $v_0=\sqrt{20}=2\sqrt5\approx4{,}47\ms$. **(2 pts)**
    4. $\vec a\,(0\,;\,-2)$, $a=2\mss$. L'ordonnée est maximale quand $v_y=0$ : $t=1\U{s}$, au point $(4\,;\,2)$. **(3 pts)**
    """),
])

# =====================================================================
# PARTIE B — Base de Frenet
# =====================================================================
B1 = dict(
    id="p1-b1", titre="Accélérations tangentielle et normale, rayon de courbure", duree=20,
    objectif="Décomposer l'accélération dans la base de Frenet et calculer le rayon de courbure à une date donnée.",
    cours=[
        cours(r"""
        La **base de Frenet** est attachée au mobile : $\vec T$ est tangent à la trajectoire (dans le sens du mouvement), $\vec N$ lui est perpendiculaire et pointe **vers l'intérieur de la courbe**.
        """),
        retenir("Base de Frenet", r"""
        $$\vec a=a_t\,\vec T+a_n\,\vec N\qquad a_t=\frac{\dd v}{\dd t}\qquad a_n=\frac{v^2}{\rho}\qquad a^2=a_t^2+a_n^2$$

        - $\rho$ est le **rayon de courbure** (en m). Pour un cercle, $\rho=R$.
        - $a_t>0$ : mouvement accéléré ; $a_t<0$ : retardé ; $a_t=0$ : uniforme.
        - $a_n=0$ à toute date : mouvement rectiligne.
        """),
        retenir("Méthode à une date donnée", r"""
        1. Calculer $\vec v$, $v$ et $\vec a$, $a$ à cette date.
        2. $a_t=\dfrac{\vec v\cdot\vec a}{v}=\dfrac{v_xa_x+v_ya_y}{v}$.
        3. $a_n=\dfrac{|v_xa_y-v_ya_x|}{v}$, ou $a_n=\sqrt{a^2-a_t^2}$.
        4. $\rho=\dfrac{v^2}{a_n}$.
        """),
        prof(r"""
        Ne calcule pas $\rho$ avec $a$ au lieu de $a_n$ : c'est l'erreur la plus fréquente. Vérifie toujours $a_t^2+a_n^2=a^2$.
        """),
    ],
    video=dict(id="p1-b1", titre="La base de Frenet en quatre calculs", phrases=[
        ("La base de Frenet en quatre calculs.", "La base de Frenet"),
        ("La base de Frenet suit le mobile. Le vecteur T est tangent à la trajectoire. Le vecteur N est perpendiculaire, tourné vers l'intérieur de la courbe.", r"\vec a=a_t\vec T+a_n\vec N"),
        ("L'accélération tangentielle mesure la variation de la valeur de la vitesse. L'accélération normale mesure le changement de direction.", r"a_t=\dfrac{\mathrm dv}{\mathrm dt}\qquad a_n=\dfrac{v^2}{\rho}"),
        ("Exemple : x égale deux t, y égale t carré moins un, à la date un seconde. Premier calcul : vitesse deux, deux, de valeur racine de huit. Accélération zéro, deux, de valeur deux.", r"\vec v(2\,;2)\quad \vec a(0\,;2)"),
        ("Deuxième calcul : a t égale le produit scalaire de v et de a, divisé par v. Ici quatre sur racine de huit, soit racine de deux.", r"a_t=\dfrac{v_xa_x+v_ya_y}{v}=\sqrt2"),
        ("Troisième calcul : a n égale la valeur absolue de v x a y moins v y a x, divisée par v. Encore racine de deux. On vérifie : deux plus deux égale quatre, c'est bien a au carré.", r"a_n=\dfrac{|v_xa_y-v_ya_x|}{v}=\sqrt2"),
        ("Quatrième calcul : le rayon de courbure, v carré sur a n. Huit sur racine de deux, environ cinq virgule sept mètres.", r"\rho=\dfrac{v^2}{a_n}\approx5{,}66\ \mathrm m"),
        ("Le piège : diviser v carré par a au lieu de a n. Prends toujours l'accélération normale.", r"\rho=\dfrac{v^2}{a_n}\ \text{et non}\ \dfrac{v^2}{a}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("à la date t = 1 s", r"""
    Équations horaires : $x=2t$, $y=t^2-1$ (SI). Calculer à $t=1\U{s}$ : $a_t$, $a_n$ et le rayon de courbure $\rho$.
    """, r"""
    À $t=1\U{s}$ : $\vec v\,(2\,;\,2)$, $v=\sqrt8\approx2{,}83\ms$ ; $\vec a\,(0\,;\,2)$, $a=2\mss$.

    $a_t=\dfrac{2\times0+2\times2}{\sqrt8}=\sqrt2\approx1{,}41\mss$ (positive : mouvement accéléré).

    $a_n=\dfrac{|2\times2-2\times0|}{\sqrt8}=\sqrt2\approx1{,}41\mss$. Vérification : $a_t^2+a_n^2=2+2=4=a^2$.

    $\rho=\dfrac{v^2}{a_n}=\dfrac{8}{\sqrt2}=4\sqrt2\approx5{,}66\U{m}$.
    """),
    application=("à la date t = 1 s", r"""
    Équations horaires : $x=3t$, $y=2t^2$ (SI). À $t=1\U{s}$, calculer $v$, $a$, $a_t$, $a_n$ et $\rho$.
    """, r"""
    $\vec v\,(3\,;\,4t)$ : à $t=1\U{s}$, $\vec v\,(3\,;\,4)$ et $v=5\ms$. $\vec a\,(0\,;\,4)$, $a=4\mss$.

    $a_t=\dfrac{3\times0+4\times4}{5}=3{,}2\mss$ ; $a_n=\dfrac{|3\times4-4\times0|}{5}=2{,}4\mss$ (vérification : $3{,}2^2+2{,}4^2=16$).

    $\rho=\dfrac{25}{2{,}4}\approx10{,}4\U{m}$.
    """),
    exos=[
        ("un mouvement circulaire", r"""
        Équations horaires : $x=2\cos(3t)$, $y=2\sin(3t)$ (SI).

        1. Calculer $v$. Le mouvement est-il uniforme ?
        2. En déduire $a_t$, puis $a_n$ sachant que $a=18\mss$. Calculer $\rho$ et conclure.
        """, r"""
        1. $v_x=-6\sin(3t)$, $v_y=6\cos(3t)$, donc $v=6\ms$ constante : mouvement **uniforme**.
        2. $a_t=\dfrac{\dd v}{\dd t}=0$, donc $a_n=a=18\mss$ et $\rho=\dfrac{36}{18}=2\U{m}$ : c'est le rayon du cercle décrit ($x^2+y^2=4$).
        """),
        ("à la date t = 0,6 s", r"""
        Équations horaires : $x=4t$, $y=-5t^2$ (SI). À $t=0{,}6\U{s}$, calculer $v$, $a_t$, $a_n$ et $\rho$.
        """, r"""
        $\vec v\,(4\,;\,-10t)$ : à $0{,}6\U{s}$, $\vec v\,(4\,;\,-6)$, $v=\sqrt{52}\approx7{,}21\ms$. $\vec a\,(0\,;\,-10)$, $a=10\mss$.

        $a_t=\dfrac{4\times0+(-6)(-10)}{7{,}21}\approx8{,}32\mss$ ; $a_n=\dfrac{|4\times(-10)-(-6)\times0|}{7{,}21}\approx5{,}55\mss$.

        $\rho=\dfrac{52}{5{,}55}\approx9{,}37\U{m}$.
        """),
    ],
)

EVAL_B = dict(duree=35, exos=[
    dict(titre="Frenet à une date donnée", pts=12, enonce=r"""
    Un mobile a pour équations horaires $x=4t$ et $y=t^2+1$ (SI).

    1. Déterminer l'équation de la trajectoire.
    2. Calculer les valeurs de la vitesse et de l'accélération à $t=3\U{s}$.
    3. Calculer à cette date les accélérations tangentielle et normale. Le mouvement est-il accéléré ou retardé ?
    4. Calculer le rayon de courbure de la trajectoire au point occupé à $t=3\U{s}$.
    """, corr=r"""
    1. $t=\dfrac{x}{4}$ donc $y=\dfrac{x^2}{16}+1$ : parabole. **(2 pts)**
    2. $\vec v\,(4\,;\,2t)$ : à $3\U{s}$, $\vec v\,(4\,;\,6)$, $v=\sqrt{52}\approx7{,}21\ms$. $\vec a\,(0\,;\,2)$, $a=2\mss$. **(3 pts)**
    3. $a_t=\dfrac{4\times0+6\times2}{7{,}21}\approx1{,}66\mss>0$ : mouvement **accéléré**. $a_n=\dfrac{|4\times2-6\times0|}{7{,}21}\approx1{,}11\mss$. Vérification : $1{,}66^2+1{,}11^2\approx4=a^2$. **(5 pts)**
    4. $\rho=\dfrac{v^2}{a_n}=\dfrac{52}{1{,}11}\approx46{,}9\U{m}$. **(2 pts)**
    """),
    dict(titre="Mouvement circulaire uniforme", pts=8, enonce=r"""
    Un point $M$ a pour équations horaires $x=0{,}5\cos(\pi t)$ et $y=0{,}5\sin(\pi t)$ (SI).

    1. Montrer que la trajectoire est un cercle dont on précisera le centre et le rayon.
    2. Calculer la vitesse $v$. Le mouvement est-il uniforme ?
    3. En déduire $a_t$ et $a_n$. Montrer que $\vec a=-\pi^2\,\vect{OM}$ et interpréter.
    """, corr=r"""
    1. $x^2+y^2=0{,}25$ : cercle de centre $O$, de rayon $R=0{,}5\U{m}$. **(2 pts)**
    2. $v_x=-0{,}5\pi\sin(\pi t)$, $v_y=0{,}5\pi\cos(\pi t)$, donc $v=0{,}5\pi\approx1{,}57\ms$ constante : **uniforme**. **(2 pts)**
    3. $a_t=0$ ; $a_n=\dfrac{v^2}{R}=\dfrac{0{,}25\pi^2}{0{,}5}=0{,}5\pi^2\approx4{,}93\mss$. $a_x=-0{,}5\pi^2\cos(\pi t)=-\pi^2x$ et $a_y=-\pi^2y$, donc $\vec a=-\pi^2\vect{OM}$ : l'accélération est dirigée vers le centre (**centripète**). **(4 pts)**
    """),
])

# =====================================================================
# PARTIE C — Mouvements rectilignes
# =====================================================================
C1 = dict(
    id="p1-c1", titre="Le mouvement rectiligne uniforme", duree=15,
    objectif="Écrire l'équation horaire d'un MRU et résoudre un problème de rencontre de deux mobiles.",
    cours=[
        retenir("Mouvement rectiligne uniforme (MRU)", r"""
        Trajectoire droite et vitesse constante : $\vec a=\vec 0$.

        $$x(t)=v\,(t-t_0)+x_0\qquad\text{souvent}\qquad x(t)=vt+x_0$$

        - $v$ est algébrique : $v>0$ si le mobile va dans le sens de l'axe, $v<0$ sinon.
        - $x_0$ est la position à la date $t_0$ (souvent $t_0=0$).
        """),
        retenir("Rencontre de deux mobiles", r"""
        1. Un **seul** repère et une **seule** origine des dates pour les deux mobiles.
        2. Écrire $x_1(t)$ et $x_2(t)$ (attention aux signes et aux départs décalés).
        3. Ils se rencontrent quand $x_1(t)=x_2(t)$ : on trouve la date, puis la position.
        """),
        prof(r"""
        Convertis tout de suite les km/h en m/s : on divise par 3,6. Ainsi 72 km/h = 20 m/s.
        """),
    ],
    video=dict(id="p1-c1", titre="Deux mobiles qui se rencontrent", phrases=[
        ("Le mouvement rectiligne uniforme, et la rencontre de deux mobiles.", "MRU et rencontre"),
        ("Un mouvement est rectiligne uniforme quand la trajectoire est une droite et que la vitesse est constante. L'accélération est nulle.", r"\vec a=\vec 0"),
        ("L'équation horaire est x égale v t plus x zéro. La vitesse v est algébrique : positive si le mobile avance dans le sens de l'axe, négative sinon.", r"x(t)=vt+x_0"),
        ("Exemple : une voiture A part de O à vingt mètres par seconde. Au même instant, une voiture B part du point d'abscisse six cents mètres, à dix mètres par seconde, en sens inverse.", r"x_A=20t\qquad x_B=-10t+600"),
        ("Pour B, la vitesse est négative, car B roule vers O. C'est le point qu'on oublie le plus souvent.", r"v_B=-10\ \mathrm{m\cdot s^{-1}}"),
        ("Les voitures se rencontrent quand elles ont la même abscisse. Vingt t égale moins dix t plus six cents, donc trente t égale six cents, et t égale vingt secondes.", r"x_A=x_B\iff t=20\ \mathrm s"),
        ("On remplace dans l'une des équations : x égale vingt fois vingt, soit quatre cents mètres. On vérifie avec l'autre : moins deux cents plus six cents, quatre cents. C'est juste.", r"x=400\ \mathrm m"),
        ("À retenir : un seul repère, une seule origine des dates, puis x un égale x deux.", r"x_1(t)=x_2(t)"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("deux voitures face à face", r"""
    À $t=0$, une voiture A passe en $O$ à $20\ms$. Au même instant, une voiture B passe au point d'abscisse $600\U{m}$ à $10\ms$, en sens inverse. Les deux mouvements sont rectilignes uniformes sur l'axe $(Ox)$ orienté de A vers B.

    1. Écrire les équations horaires $x_A(t)$ et $x_B(t)$.
    2. Déterminer la date et le lieu de la rencontre.
    """, r"""
    1. $x_A=20t$ et $x_B=-10t+600$ (B va dans le sens négatif).
    2. $x_A=x_B\iff 30t=600\iff t=20\U{s}$. Alors $x=20\times20=400\U{m}$ (vérification : $-200+600=400$). Rencontre à $t=20\U{s}$, à $400\U{m}$ de $O$.
    """),
    application=("un cycliste", r"""
    Un cycliste roule en ligne droite. Le tableau donne sa position :

    | $t$ (s) | 0 | 2 | 4 | 6 |
    | $x$ (m) | 5 | 15 | 25 | 35 |

    1. Montrer que le mouvement est uniforme et calculer sa vitesse.
    2. Écrire l'équation horaire. À quelle date le cycliste passe-t-il à $80\U{m}$ ?
    """, r"""
    1. En $2\U{s}$, il parcourt toujours $10\U{m}$ : la vitesse est constante, $v=\dfrac{10}{2}=5\ms$.
    2. $x=5t+5$. $5t+5=80\iff t=15\U{s}$.
    """),
    exos=[
        ("départs décalés", r"""
        Un train passe en $O$ à $t=0$ à $72\U{km/h}$. Un second train part de $O$ à $t=10\U{s}$, dans le même sens, à $30\ms$ (vitesse constante).

        1. Écrire les équations horaires des deux trains (origine des dates commune).
        2. Où et quand le second train rattrape-t-il le premier ?
        """, r"""
        1. $72\U{km/h}=20\ms$. $x_1=20t$ et $x_2=30(t-10)$ pour $t\geq10\U{s}$.
        2. $20t=30t-300\iff t=30\U{s}$. Alors $x=600\U{m}$.
        """),
        ("deux positions suffisent", r"""
        Un mobile en MRU est en $x=10\U{m}$ à $t=2\U{s}$ et en $x=-2\U{m}$ à $t=6\U{s}$.

        1. Calculer sa vitesse. Dans quel sens se déplace-t-il ?
        2. Écrire son équation horaire. À quelle date passe-t-il par l'origine ?
        """, r"""
        1. $v=\dfrac{-2-10}{6-2}=-3\ms$ : il se déplace dans le sens négatif.
        2. $x=-3t+x_0$ avec $10=-6+x_0$, donc $x_0=16\U{m}$ : $x=-3t+16$. $x=0\iff t=\dfrac{16}{3}\approx5{,}33\U{s}$.
        """),
    ],
)

C2 = dict(
    id="p1-c2", titre="Le mouvement rectiligne uniformément varié", duree=20,
    objectif="Utiliser les trois relations du MRUV, dont la relation indépendante du temps, et reconnaître les phases accélérées ou retardées.",
    cours=[
        retenir("Mouvement rectiligne uniformément varié (MRUV)", r"""
        Trajectoire droite et accélération constante $a$ :

        $$v(t)=a\,t+v_0\qquad x(t)=\frac12\,a\,t^2+v_0\,t+x_0\qquad v^2-v_0^2=2a\,(x-x_0)$$

        - La troisième relation ne contient pas le temps : elle sert quand on ne connaît pas la durée (distance de freinage).
        - Mouvement **accéléré** si $a\cdot v>0$, **retardé** si $a\cdot v<0$.
        """),
        prof(r"""
        Pour identifier $a$, $v_0$ et $x_0$ dans $x=2t^2-8t+3$, attention au $\frac12$ : $\frac12a=2$ donc $a=4\mss$.
        """),
    ],
    video=dict(id="p1-c2", titre="Les trois relations du MRUV", phrases=[
        ("Le mouvement rectiligne uniformément varié.", "MRUV"),
        ("Un mouvement est rectiligne uniformément varié quand la trajectoire est une droite et que l'accélération est constante.", r"a=\text{constante}"),
        ("Trois relations à connaître. La vitesse : v égale a t plus v zéro. La position : x égale un demi a t carré, plus v zéro t, plus x zéro.", r"v=at+v_0\qquad x=\tfrac12at^2+v_0t+x_0"),
        ("Et la relation indépendante du temps : v carré moins v zéro carré égale deux a, facteur de x moins x zéro.", r"v^2-v_0^2=2a(x-x_0)"),
        ("Exemple : une voiture roule à soixante-douze kilomètres heure, soit vingt mètres par seconde. Elle freine avec une accélération de moins quatre mètres par seconde carrée.", r"v_0=20\ \mathrm{m\cdot s^{-1}},\ a=-4\ \mathrm{m\cdot s^{-2}}"),
        ("Durée du freinage : la voiture s'arrête quand v est nulle. Zéro égale moins quatre t plus vingt, donc t égale cinq secondes.", r"0=-4t+20\iff t=5\ \mathrm s"),
        ("Distance de freinage, sans le temps : zéro moins quatre cents égale moins huit fois d. Donc d égale cinquante mètres.", r"d=\dfrac{v_0^2}{2|a|}=50\ \mathrm m"),
        ("Pendant le freinage, a et v sont de signes contraires : le mouvement est retardé. S'ils ont le même signe, il est accéléré.", r"a\cdot v<0\ \Rightarrow\ \text{retardé}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("un freinage", r"""
    Une voiture roule à $72\U{km/h}$ sur une route droite. À $t=0$, le conducteur freine : l'accélération vaut $a=-4\mss$.

    1. Au bout de combien de temps la voiture s'arrête-t-elle ?
    2. Quelle distance parcourt-elle pendant le freinage ?
    """, r"""
    1. $v_0=20\ms$ et $v=-4t+20$. $v=0\iff t=5\U{s}$.
    2. Relation indépendante du temps : $0-20^2=2\times(-4)\times d$, donc $d=\dfrac{400}{8}=50\U{m}$. (Vérification : $x(5)=-2\times25+20\times5=50\U{m}$.)
    """),
    application=("lire une équation horaire", r"""
    Un mobile a pour équation horaire $x=2t^2-8t+3$ (SI).

    1. Identifier $a$, $v_0$ et $x_0$. Écrire $v(t)$.
    2. À quelle date le mobile s'arrête-t-il ? Où est-il alors ?
    3. Préciser la nature du mouvement avant et après cette date.
    """, r"""
    1. $\frac12a=2$ donc $a=4\mss$ ; $v_0=-8\ms$ ; $x_0=3\U{m}$. $v=4t-8$.
    2. $v=0\iff t=2\U{s}$ ; $x(2)=8-16+3=-5\U{m}$.
    3. Pour $t<2\U{s}$ : $v<0$ et $a>0$, $a\cdot v<0$, **retardé**. Pour $t>2\U{s}$ : $v>0$, **accéléré**.
    """),
    exos=[
        ("un démarrage", r"""
        Une voiture démarre sans vitesse initiale avec une accélération constante $a=2\mss$.

        1. Au bout de combien de temps atteint-elle $30\ms$ ?
        2. Quelle distance a-t-elle alors parcourue ? Répondre de deux façons.
        """, r"""
        1. $v=2t$ ; $2t=30\iff t=15\U{s}$.
        2. $x=t^2$, donc $x(15)=225\U{m}$. Ou : $30^2-0=2\times2\times d$, donc $d=225\U{m}$.
        """),
        ("aller et retour", r"""
        Un mobile part de $O$ avec $v_0=10\ms$ ; son accélération est constante, $a=-2\mss$.

        1. Écrire $v(t)$ et $x(t)$.
        2. Quelle est l'abscisse maximale atteinte ?
        3. À quelle date revient-il en $O$, et avec quelle vitesse ?
        """, r"""
        1. $v=-2t+10$ et $x=-t^2+10t$.
        2. $v=0$ à $t=5\U{s}$ : $x_{\max}=-25+50=25\U{m}$.
        3. $x=0\iff t(-t+10)=0\iff t=10\U{s}$ ; $v=-10\ms$ (même valeur qu'au départ, sens opposé).
        """),
    ],
)

C3 = dict(
    id="p1-c3", titre="Enregistrements et graphes", duree=20,
    objectif="Reconnaître un MRU ou un MRUV sur un enregistrement, calculer une vitesse instantanée et une accélération.",
    cours=[
        cours(r"""
        Sur un enregistrement, les positions $M_0, M_1, M_2,\dots$ du mobile sont marquées à intervalles de temps égaux $\tau$.
        """),
        retenir("Exploiter un enregistrement", r"""
        - Distances $M_iM_{i+1}$ toutes égales : **MRU**, $v=\dfrac{M_iM_{i+1}}{\tau}$.
        - Distances qui augmentent (ou diminuent) toujours de la même quantité $\Delta d$ : **MRUV**, avec $\Delta d=a\,\tau^2$.
        - Vitesse instantanée en $M_i$ : $v_i=\dfrac{M_{i-1}M_{i+1}}{2\tau}$.
        - Sur un graphe $v(t)$ : une droite horizontale indique un MRU, une droite oblique un MRUV de pente $a$.
        """),
        prof(r"""
        Convertis les centimètres en mètres et les millisecondes en secondes **avant** de calculer : $\tau^2$ multiplie l'erreur.
        """),
    ],
    video=dict(id="p1-c3", titre="Lire un enregistrement", phrases=[
        ("Lire un enregistrement.", "Lire un enregistrement"),
        ("Sur un enregistrement, les positions du mobile sont marquées à intervalles de temps égaux, notés tau.", r"\tau=\text{durée entre deux points}"),
        ("Si les distances entre deux points successifs sont égales, le mouvement est uniforme.", r"M_iM_{i+1}=\text{cte}\ \Rightarrow\ \text{MRU}"),
        ("Si elles augmentent toujours de la même quantité, delta d, le mouvement est uniformément varié, et delta d égale a tau carré.", r"\Delta d=a\,\tau^2"),
        ("Exemple : tau égale vingt millisecondes, et les distances valent un, un virgule quatre, un virgule huit, deux virgule deux centimètres.", r"1{,}0\ ;\ 1{,}4\ ;\ 1{,}8\ ;\ 2{,}2\ \mathrm{cm}"),
        ("Elles augmentent de zéro virgule quatre centimètre, soit quatre millimètres. Donc a égale quatre millimètres divisés par tau carré.", r"a=\dfrac{4\times10^{-3}}{(0{,}02)^2}=10\ \mathrm{m\cdot s^{-2}}"),
        ("La vitesse au point M deux est la distance de M un à M trois, divisée par deux tau : trois virgule deux centimètres sur quarante millisecondes, soit zéro virgule huit mètre par seconde.", r"v_2=\dfrac{M_1M_3}{2\tau}=0{,}8\ \mathrm{m\cdot s^{-1}}"),
        ("Le réflexe : tout convertir en mètres et en secondes avant de calculer.", r"\mathrm{cm}\to\mathrm m\qquad \mathrm{ms}\to\mathrm s"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("une chute enregistrée", r"""
    Un enregistrement donne, avec $\tau=20\U{ms}$ : $M_0M_1=1{,}0\U{cm}$, $M_1M_2=1{,}4\U{cm}$, $M_2M_3=1{,}8\U{cm}$, $M_3M_4=2{,}2\U{cm}$.

    1. Quelle est la nature du mouvement ? Calculer l'accélération.
    2. Calculer la vitesse au point $M_2$.
    """, r"""
    1. Les distances augmentent toujours de $\Delta d=0{,}4\U{cm}=4\times10^{-3}\U{m}$ : **MRUV**. $a=\dfrac{\Delta d}{\tau^2}=\dfrac{4\times10^{-3}}{(0{,}02)^2}=10\mss$.
    2. $v_2=\dfrac{M_1M_3}{2\tau}=\dfrac{(1{,}4+1{,}8)\times10^{-2}}{0{,}04}=0{,}8\ms$.
    """),
    application=("un chariot", r"""
    Avec $\tau=50\U{ms}$, on mesure : $M_0M_1=2{,}0\U{cm}$, $M_1M_2=2{,}5\U{cm}$, $M_2M_3=3{,}0\U{cm}$, $M_3M_4=3{,}5\U{cm}$.

    1. Nature du mouvement et accélération.
    2. Vitesse au point $M_2$.
    """, r"""
    1. $\Delta d=0{,}5\U{cm}=5\times10^{-3}\U{m}$ constant : MRUV ; $a=\dfrac{5\times10^{-3}}{(0{,}05)^2}=2\mss$.
    2. $v_2=\dfrac{(2{,}5+3{,}0)\times10^{-2}}{0{,}1}=0{,}55\ms$.
    """),
    exos=[
        ("distances égales", r"""
        Un enregistrement ($\tau=40\U{ms}$) montre des distances toutes égales à $1{,}5\U{cm}$. Nature du mouvement et vitesse ?
        """, r"""
        Distances égales pendant des durées égales : **MRU**. $v=\dfrac{1{,}5\times10^{-2}}{0{,}04}=0{,}375\ms$.
        """),
        ("lire un graphe v(t)", r"""
        La vitesse d'un mobile en ligne droite est donnée par le tableau :

        | $t$ (s) | 0 | 1 | 2 | 3 | 4 | 5 |
        | $v$ ($\mathrm{m\cdot s^{-1}}$) | 2 | 4 | 6 | 8 | 8 | 8 |

        [[graphe:p1-c3-v]]

        1. Décrire les deux phases du mouvement. Calculer l'accélération de la première.
        2. Le mobile part de $O$. Calculer la distance parcourue entre $0$ et $3\U{s}$.
        """, r"""
        1. De $0$ à $3\U{s}$, $v$ augmente de $2\ms$ chaque seconde : MRUV, $a=2\mss$. De $3$ à $5\U{s}$, $v=8\ms$ constante : MRU.
        2. $x=t^2+2t$, donc $x(3)=9+6=15\U{m}$.
        """),
    ],
)

EVAL_C = dict(duree=45, exos=[
    dict(titre="La voiture et le bus", pts=10, enonce=r"""
    Une voiture est arrêtée à un feu rouge. Au moment où le feu passe au vert ($t=0$), elle démarre avec une accélération constante $a=1{,}5\mss$. Au même instant, un bus la dépasse à la vitesse constante de $15\ms$. On prend comme origine la position du feu.

    1. Écrire les équations horaires de la voiture et du bus.
    2. À quelle date et à quelle distance du feu la voiture rattrape-t-elle le bus ? Quelle est alors sa vitesse ?
    3. À quelle date l'écart entre les deux véhicules est-il maximal ? Calculer cet écart.
    4. Après le rattrapage, la voiture freine depuis $30\ms$ avec une décélération constante de $5\mss$. Calculer sa distance de freinage sans calculer la durée, puis justifier la nature du mouvement.
    """, corr=r"""
    1. Voiture : $x_V=0{,}75\,t^2$. Bus : $x_B=15t$. **(2 pts)**
    2. $0{,}75t^2=15t\iff t=20\U{s}$ ($t\neq0$). $x=300\U{m}$. Vitesse : $v_V=1{,}5\times20=30\ms$. **(3 pts)**
    3. L'écart $x_B-x_V$ augmente tant que le bus va plus vite que la voiture : il est maximal quand $v_V=15\ms$, soit $t=10\U{s}$. Écart : $150-75=75\U{m}$. **(3 pts)**
    4. Relation indépendante du temps : $0-30^2=2\times(-5)\times d$, donc $d=90\U{m}$. $a\cdot v<0$ : mouvement **retardé**. **(2 pts)**
    """),
    dict(titre="Un enregistrement", pts=10, enonce=r"""
    On enregistre le mouvement rectiligne d'un mobile avec $\tau=50\U{ms}$ : $M_0M_1=2{,}0\U{cm}$, $M_1M_2=3{,}0\U{cm}$, $M_2M_3=4{,}0\U{cm}$, $M_3M_4=5{,}0\U{cm}$.

    1. Montrer que le mouvement est uniformément varié et calculer son accélération.
    2. Calculer les vitesses aux points $M_1$ et $M_2$. Retrouver l'accélération.
    3. On prend $M_1$ comme origine des espaces et des dates. Écrire l'équation horaire $x(t)$.
    4. Quelle distance le mobile parcourt-il entre $t=0$ et $t=0{,}5\U{s}$ (en supposant le mouvement inchangé) ?
    """, corr=r"""
    1. $\Delta d=1{,}0\U{cm}$ constant : MRUV. $a=\dfrac{10^{-2}}{(0{,}05)^2}=4\mss$. **(2 pts)**
    2. $v_1=\dfrac{(2+3)\times10^{-2}}{0{,}1}=0{,}5\ms$ ; $v_2=\dfrac{(3+4)\times10^{-2}}{0{,}1}=0{,}7\ms$. $a=\dfrac{0{,}7-0{,}5}{0{,}05}=4\mss$. **(4 pts)**
    3. $x=\frac12\times4\,t^2+0{,}5\,t=2t^2+0{,}5t$ (SI). **(2 pts)**
    4. $x(0{,}5)=2\times0{,}25+0{,}25=0{,}75\U{m}$. **(2 pts)**
    """),
])

PARTIE_A = dict(lettre="A", titre="Repérage, vitesse et accélération", etapes=[A1, A2], evaluation=EVAL_A)
PARTIE_B = dict(lettre="B", titre="La base de Frenet", etapes=[B1], evaluation=EVAL_B)
PARTIE_C = dict(lettre="C", titre="Les mouvements rectilignes", etapes=[C1, C2, C3], evaluation=EVAL_C)
