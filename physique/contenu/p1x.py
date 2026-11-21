# -*- coding: utf-8 -*-
"""P1 : compléments interactifs (question d'entrée, indices, vérifications, pièges),
questions flash de début de partie et évaluation complète du chapitre."""
PI = 3.141592653589793
c = lambda label, val, unite="", err=(), tol=0.03: dict(label=label, val=val, unite=unite, err=list(err), tol=tol)
CONV = "Convertis d'abord en unités SI (m, s, rad)."

EXTRA = {
"p1-a1": dict(
    entree=[("Un mobile a pour équations horaires $x=t$ et $y=2t$. Sa trajectoire est :", ["une droite", "une parabole", "un cercle"], 0,
             "On a $t=x$, donc $y=2x$ : une droite passant par $O$.")],
    indices=["Isole $t$ dans l'équation de $x$.", "$t=\\dfrac{x-1}{3}$.", "Remplace dans $y=-2t+4$, puis développe."],
    rep_app=[c("Coefficient directeur", -2/3, "", [(-2, "Tu as gardé le coefficient de $t$ : remplace d'abord $t$ par $\\frac{x-1}{3}$.")]),
             c("Ordonnée à l'origine", 14/3, "m")],
    rep_exos={1: [c("Rayon", 4, "m", [(16, "$16$ est $R^2$ : le rayon vaut $\\sqrt{16}$.")])], 2: [c("Ordonnée maximale", 5, "m")]},
    pieges=["Oublier que $t\\geq0$ limite la trajectoire à une portion de courbe.",
            "Pour un cercle, chercher à isoler $t$ au lieu de calculer $x^2+y^2$."]),
"p1-a2": dict(
    entree=[("Si $x=3t^2$, alors $v_x$ vaut :", ["$3t$", "$6t$", "$6$"], 1, "$(t^2)'=2t$, donc $v_x=6t$. On dérive encore : $a_x=6$.")],
    indices=["Dérive $x$ et $y$ par rapport à $t$.", "$v_x=6t-2$ et $v_y=4$.", "À $t=2\\U{s}$ : $v=\\sqrt{v_x^2+v_y^2}$."],
    rep_app=[c("$v$ à $t=2$ s", 116 ** 0.5, "m/s", [(14, "Tu as additionné $v_x+v_y$ : la valeur est $\\sqrt{v_x^2+v_y^2}$.")]), c("$a$", 6, "m/s²")],
    rep_exos={1: [c("Date d'arrêt", 2, "s")], 2: [c("$a$", 10, "m/s²")]},
    pieges=["Additionner les composantes au lieu de calculer la norme.",
            "Oublier la constante d'intégration en remontant de $\\vec v$ à $\\vect{OM}$."]),
"p1-b1": dict(
    entree=[("Une voiture prend un virage à vitesse constante. Son accélération est :", ["nulle", "dirigée vers l'intérieur du virage", "dans le sens du mouvement"], 1,
             "$v$ constante donne $a_t=0$, mais la direction change : $a_n=\\frac{v^2}{\\rho}$, vers l'intérieur du virage.")],
    indices=["Calcule $\\vec v$ et $\\vec a$ à $t=1\\U{s}$.", "$a_t=\\dfrac{v_xa_x+v_ya_y}{v}$ et $a_n=\\dfrac{|v_xa_y-v_ya_x|}{v}$.", "$\\rho=\\dfrac{v^2}{a_n}$ avec $v^2=25$."],
    rep_app=[c("$a_t$", 3.2, "m/s²"), c("$a_n$", 2.4, "m/s²"),
             c("$\\rho$", 25 / 2.4, "m", [(6.25, "Tu as divisé $v^2$ par $a$ : il faut diviser par $a_n$.")])],
    rep_exos={1: [c("$\\rho$", 2, "m")], 2: [c("$\\rho$", 9.37, "m", [(5.2, "Tu as divisé $v^2$ par $a$ : il faut $a_n$.")])]},
    pieges=["Calculer $\\rho$ avec $a$ au lieu de $a_n$.", "Croire que $a_t=a$ : ce n'est vrai que pour un mouvement rectiligne."]),
"p1-c1": dict(
    entree=[("Une voiture roule à $72\\U{km/h}$. Sa vitesse en $\\mathrm{m\\cdot s^{-1}}$ vaut :", ["$72$", "$20$", "$259{,}2$"], 1,
             "On divise par $3{,}6$ : $72/3{,}6=20\\ms$.")],
    indices=["La vitesse est la distance parcourue divisée par la durée.", "$v=\\dfrac{15-5}{2-0}$.", "$x_0$ se lit à $t=0$ ; puis résous $5t+5=80$."],
    rep_app=[c("$v$", 5, "m/s"), c("Date", 15, "s", [(16, "Tu as divisé $80$ par $5$ sans retirer $x_0=5\\U{m}$.")])],
    rep_exos={1: [c("Date de rattrapage", 30, "s", [(20, "Le second train part à $t=10\\U{s}$ : écris $x_2=30(t-10)$.")])],
              2: [c("$v$", -3, "m/s", [(3, "Le mobile va vers les $x$ décroissants : $v$ est négative.")])]},
    pieges=["Oublier le signe moins pour un mobile qui va dans le sens négatif.",
            "Prendre deux origines des dates différentes quand les départs sont décalés."]),
"p1-c2": dict(
    entree=[("Dans $x=3t^2+2t$, l'accélération vaut :", ["$3\\mss$", "$6\\mss$", "$2\\mss$"], 1, "$\\frac12a=3$, donc $a=6\\mss$. Attention au $\\frac12$.")],
    indices=["Compare avec $x=\\frac12at^2+v_0t+x_0$.", "$a=4$ et $v_0=-8$, donc $v=4t-8$.", "Le signe de $a\\cdot v$ donne la nature du mouvement."],
    rep_app=[c("$a$", 4, "m/s²", [(2, "N'oublie pas le $\\frac12$ : $\\frac12a=2$, donc $a=4$.")]), c("Date d'arrêt", 2, "s"), c("Position à l'arrêt", -5, "m")],
    rep_exos={1: [c("Distance", 225, "m")], 2: [c("Abscisse maximale", 25, "m")]},
    pieges=["Oublier le facteur $\\frac12$ en identifiant $a$.", "Dire « accéléré » parce que $a>0$, sans regarder le signe de $v$."]),
"p1-c3": dict(
    entree=[("Sur un enregistrement, les distances entre points successifs augmentent toujours de la même quantité. Le mouvement est :",
             ["uniforme", "uniformément varié", "circulaire"], 1, "$\\Delta d=a\\tau^2$ constant : MRUV.")],
    indices=["Calcule les différences entre distances successives.", "$\\Delta d=5\\times10^{-3}\\U{m}$ et $\\tau=0{,}05\\U{s}$.", "$v_2=\\dfrac{M_1M_3}{2\\tau}$."],
    rep_app=[c("$a$", 2, "m/s²", [(0.02, CONV), (200, CONV)]), c("$v_2$", 0.55, "m/s", [(1.1, "Divise par $2\\tau$, pas par $\\tau$.")])],
    rep_exos={1: [c("$v$", 0.375, "m/s")], 2: [c("Distance", 15, "m")]},
    pieges=["Calculer avec des centimètres et des millisecondes.", "Diviser $M_{i-1}M_{i+1}$ par $\\tau$ au lieu de $2\\tau$."]),
"p1-d1": dict(
    entree=[("À $t=0$, le mobile est au centre ($x=0$). Que peut valoir $\\varphi$ ?", ["$0$", "$\\pm\\frac{\\pi}{2}$", "$\\pi$"], 1,
             "$\\cos\\varphi=0$, donc $\\varphi=\\pm\\frac{\\pi}{2}$ ; c'est le sens du mouvement qui choisit le signe.")],
    indices=["$\\omega=\\dfrac{2\\pi}{T}$.", "$x_0=0$ donne $\\cos\\varphi=0$.", "Sens positif : $v_0>0$, donc $\\sin\\varphi<0$."],
    rep_app=[c("$\\omega$", 10 * PI, "rad/s"), c("$\\varphi$", -PI / 2, "rad", [(PI / 2, "C'est le sens négatif : en sens positif, $\\sin\\varphi<0$.")])],
    rep_exos={1: [c("$T$", 0.314, "s")], 2: [c("$v_0$", -0.5, "m/s", [(0.5, "Le signe compte : $v_0=-X_m\\omega\\sin\\varphi<0$.")])]},
    pieges=["Choisir $\\varphi$ avec $x_0$ seul, sans regarder le sens du mouvement.", "Confondre l'amplitude $X_m$ et la longueur du segment $2X_m$."]),
"p1-d2": dict(
    entree=[("Où la vitesse d'un mobile en mouvement sinusoïdal est-elle maximale ?", ["aux extrémités", "au centre", "elle est constante"], 1,
             "$v^2=\\omega^2(X_m^2-x^2)$ est maximal pour $x=0$ : au centre.")],
    indices=["$v=-X_m\\omega\\sin(\\omega t+\\varphi)$.", "En $x=+5\\U{cm}$ : $\\cos(10\\pi t-\\frac{\\pi}{2})=1$.", "$|v|=\\omega\\sqrt{X_m^2-x^2}$ avec $X_m=5$ et $x=3$."],
    rep_app=[c("$v_0$", 0.5 * PI, "m/s"), c("Date", 0.05, "s"), c("$|v|$ en $x=3$ cm", 0.4 * PI, "m/s", [(0.5 * PI, "C'est $v_{\\max}$ : en $x=3\\U{cm}$, utilise $\\omega\\sqrt{X_m^2-x^2}$.")])],
    rep_exos={1: [c("$\\omega$", 5 * PI, "rad/s")], 2: [c("$X_m$", 0.1, "m", [(0.01, "$0{,}01$ est $X_m^2$ : prends la racine.")])]},
    pieges=["Garder les deux angles $\\pm\\alpha$ au lieu de trier avec le signe du sinus.", "Prendre $k=0$ alors qu'il donne une date négative."]),
"p1-e1": dict(
    entree=[("Un point tourne à $2$ tours par seconde. Sa vitesse angulaire vaut :", ["$2\\U{rad/s}$", "$4\\pi\\U{rad/s}$", "$\\pi\\U{rad/s}$"], 1,
             "$\\omega=2\\pi N=4\\pi\\U{rad/s}$.")],
    indices=["Convertis $36\\U{km/h}$ en $\\mathrm{m\\cdot s^{-1}}$.", "$\\omega=\\dfrac{v}{R}$.", "$a=\\dfrac{v^2}{R}$."],
    rep_app=[c("$\\omega$", 0.5, "rad/s"), c("$T$", 4 * PI, "s"), c("$a$", 5, "m/s²", [(64.8, "Convertis d'abord $36\\U{km/h}$ en $10\\ms$.")])],
    rep_exos={1: [c("$v$", 465, "m/s")], 2: [c("Longueur d'arc", 3, "m")]},
    pieges=["Oublier de convertir les tours par minute en radians par seconde.", "Croire qu'un mouvement uniforme n'a pas d'accélération."]),
"p1-e2": dict(
    entree=[("Combien de radians font $10$ tours ?", ["$10$", "$20\\pi$", "$10\\pi$"], 1, "Un tour vaut $2\\pi\\U{rad}$, donc $10$ tours valent $20\\pi\\U{rad}$.")],
    indices=["Convertis $10$ tours en radians.", "$\\dot\\theta^{\\,2}-\\omega_0^2=2\\ddot\\theta\\,\\theta$.", "Durée : $0=\\ddot\\theta\\,t+\\omega_0$."],
    rep_app=[c("$\\ddot\\theta$", -10 / PI, "rad/s²", [(-20, "Tu as pris $10$ au lieu de $20\\pi\\U{rad}$ : convertis les tours.")]), c("Durée", 2 * PI, "s")],
    rep_exos={1: [c("$a_n$", 7.2, "m/s²")], 2: [c("Nombre de tours", 210, "")]},
    pieges=["Mettre des tours dans les formules au lieu de radians.", "Confondre $a_t=R\\ddot\\theta$ et $a_n=R\\dot\\theta^{\\,2}$."]),
}

FLASH = {
"A": [("La dérivée de $\\cos(2t)$ est :", ["$\\sin(2t)$", "$-2\\sin(2t)$", "$2\\sin(2t)$"], 1, "$(\\cos u)'=-u'\\sin u$ avec $u=2t$."),
      ("La norme du vecteur $(3\\,;\\,4)$ vaut :", ["$7$", "$5$", "$25$"], 1, "$\\sqrt{3^2+4^2}=5$."),
      ("Une primitive de $2t$ est :", ["$t^2+C$", "$2$", "$2t^2$"], 0, "$(t^2)'=2t$ ; la constante $C$ se fixe avec une condition initiale.")],
"B": [("Le vecteur vitesse est toujours :", ["dirigé vers le centre", "tangent à la trajectoire", "constant"], 1, "Il est tangent à la trajectoire, dans le sens du mouvement."),
      ("Si $\\vec v\\,(2\\,;\\,2t)$, alors $\\vec a$ vaut :", ["$(0\\,;\\,2)$", "$(2\\,;\\,2)$", "$(2t\\,;\\,t^2)$"], 0, "On dérive chaque composante."),
      ("La trajectoire $y=x^2$ est :", ["une droite", "un cercle", "une parabole"], 2, "$y=ax^2+bx+c$ avec $a\\neq0$ : parabole.")],
"C": [("Pour un mouvement rectiligne, $a_n$ vaut :", ["$0$", "$a$", "$v^2$"], 0, "La direction ne change pas : $a_n=0$."),
      ("Le rayon de courbure se calcule avec :", ["$\\frac{v^2}{a}$", "$\\frac{v^2}{a_n}$", "$\\frac{v}{a_t}$"], 1, "$\\rho=\\frac{v^2}{a_n}$, jamais avec $a$."),
      ("$a_t>0$ signifie que le mouvement est :", ["retardé", "accéléré", "circulaire"], 1, "La valeur de la vitesse augmente.")],
"D": [("La relation indépendante du temps du MRUV est :", ["$v^2-v_0^2=2a(x-x_0)$", "$v=at$", "$x=vt$"], 0, "Elle sert quand on ne connaît pas la durée."),
      ("$90\\U{km/h}$ font :", ["$25\\ms$", "$90\\ms$", "$324\\ms$"], 0, "$90/3{,}6=25$."),
      ("Sur un enregistrement de MRUV, $\\Delta d$ vaut :", ["$a\\tau$", "$a\\tau^2$", "$\\frac{a}{\\tau}$"], 1, "$\\Delta d=a\\tau^2$.")],
"E": [("Pour $x=X_m\\cos(\\omega t+\\varphi)$, la période vaut :", ["$\\frac{2\\pi}{\\omega}$", "$2\\pi\\omega$", "$\\frac{\\omega}{2\\pi}$"], 0, "$T=\\frac{2\\pi}{\\omega}$."),
      ("Sens négatif à $t=0$ signifie :", ["$\\sin\\varphi<0$", "$\\sin\\varphi>0$", "$\\cos\\varphi<0$"], 1, "$v_0=-X_m\\omega\\sin\\varphi<0$ donne $\\sin\\varphi>0$."),
      ("La vitesse d'un mobile sinusoïdal est nulle :", ["au centre", "aux extrémités", "jamais"], 1, "Aux extrémités, le mobile fait demi-tour.")],
}

FINAL = dict(duree=120, exos=[
    dict(titre="Mouvement plan et base de Frenet", pts=8, enonce=r"""
    Dans un repère $(O;\vec i,\vec j)$, un mobile a pour équations horaires $x=3t$ et $y=-t^2+4t$ ($x$, $y$ en m, $t$ en s, $t\geq0$).

    1. Déterminer l'équation de la trajectoire.
    2. Déterminer les vecteurs vitesse et accélération.
    3. À $t=1\U{s}$, calculer $v$, $a_t$ et $a_n$. Le mouvement est-il accéléré ou retardé à cette date ?
    4. Calculer le rayon de courbure à $t=1\U{s}$.
    5. Déterminer la position et la vitesse du mobile au sommet de la trajectoire.
    """, corr=r"""
    1. $t=\dfrac{x}{3}$, donc $y=-\dfrac{x^2}{9}+\dfrac{4}{3}x$ : parabole. **(1 pt)**
    2. $\vec v\,(3\,;\,-2t+4)$ et $\vec a\,(0\,;\,-2)$. **(1,5 pt)**
    3. À $1\U{s}$ : $\vec v\,(3\,;\,2)$, $v=\sqrt{13}\approx3{,}61\ms$. $a_t=\dfrac{3\times0+2\times(-2)}{3{,}61}\approx-1{,}11\mss<0$ : **retardé**. $a_n=\dfrac{|3\times(-2)-2\times0|}{3{,}61}\approx1{,}66\mss$. **(3 pts)**
    4. $\rho=\dfrac{13}{1{,}66}\approx7{,}81\U{m}$. **(1 pt)**
    5. Sommet : $v_y=0$ à $t=2\U{s}$, point $(6\,;\,4)$, vitesse $v=3\ms$ (horizontale). **(1,5 pt)**
    """),
    dict(titre="Le triple saut (d'après bac 2018)", pts=5, enonce=r"""
    __Extrait du bac S2 2018, exercice 3, question 3.1.__ Dans la course d'élan, l'athlète, partie sans vitesse initiale, parcourt $32\U{m}$ pour arriver au point A de la ligne d'envol avec une vitesse horizontale $\vec v_1$ de norme $8\ms$. Le mouvement est supposé rectiligne uniformément varié pour cette phase.

    1. Évaluer l'accélération du mouvement et le temps mis par l'athlète sur ce parcours. (question du bac)
    2. Écrire l'équation horaire $x(t)$ de la course d'élan (origine au départ).
    3. Quelle est la vitesse de l'athlète à mi-parcours ($16\U{m}$) ? Pourquoi n'est-elle pas égale à $4\ms$ ?
    """, corr=r"""
    1. $v_1^2-0=2a\,d$, donc $a=\dfrac{64}{64}=1\mss$ ; $v_1=a\,t$, donc $t=8\U{s}$. **(2 pts)**
    2. $x=\frac12t^2$ (SI). **(1 pt)**
    3. $v^2=2\times1\times16=32$, donc $v\approx5{,}66\ms$. La vitesse n'est pas proportionnelle à la distance : elle l'est au temps ($v=at$), et l'athlète met plus de temps sur la première moitié. **(2 pts)**
    """),
    dict(titre="Le lancer du poids (bac 2012)", pts=7, enonce=r"""
    __Extrait du bac S2 2012, exercice 3, partie 3.1 (figures redessinées).__ L'origine des dates est prise au moment du lancer. L'entraîneur a obtenu les graphes des composantes horizontale $v_x$ et verticale $v_y$ du vecteur vitesse du centre d'inertie du boulet.

    [[graphe:bac12-vx]]

    [[graphe:bac12-vy]]

    1. Avec la figure 1, déterminer la composante $v_{0x}$ à $t=0$ et la nature du mouvement de la projection du centre d'inertie sur l'axe $Ox$.
    2. Avec la figure 2, déterminer la composante $v_{0y}$ à $t=0$ et la nature du mouvement de la projection sur l'axe $Oy$. Calculer l'accélération $a_y$.
    3. Exprimer $v_{0x}$ et $v_{0y}$ en fonction de la valeur $V_0$ du vecteur vitesse initiale et de l'angle $\alpha$ qu'il fait avec l'horizontale.
    4. En déduire $V_0$ et $\alpha$.
    """, corr=r"""
    1. $v_{0x}=10\ms$ ; $v_x$ est constante : mouvement **rectiligne uniforme** sur $Ox$. **(1,5 pt)**
    2. $v_{0y}=9\ms$ ; $v_y$ est une fonction affine décroissante du temps : mouvement **rectiligne uniformément varié** (décéléré puis accéléré). Pente : $a_y=\dfrac{0-9}{0{,}92}\approx-9{,}8\mss$. **(2 pts)**
    3. $v_{0x}=V_0\cos\alpha$ et $v_{0y}=V_0\sin\alpha$. **(1,5 pt)**
    4. $V_0=\sqrt{10^2+9^2}\approx13{,}5\ms$ ; $\tan\alpha=\dfrac{9}{10}$, donc $\alpha\approx42°$ (valeurs du corrigé officiel). **(2 pts)**
    """),
])
