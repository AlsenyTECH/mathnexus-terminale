# -*- coding: utf-8 -*-
"""P2 : compléments interactifs, questions flash et évaluation complète du chapitre."""
c = lambda label, val, unite="", err=(), tol=0.03: dict(label=label, val=val, unite=unite, err=list(err), tol=tol)

EXTRA = {
"p2-a1": dict(
    entree=[("Le centre d'inertie de deux billes de même masse est :", ["au milieu du segment", "sur l'une des billes", "hors du segment"], 0,
             "Masses égales : le barycentre est au milieu. Masses différentes : il se rapproche de la plus lourde.")],
    indices=["Prends l'origine sur la première bille.", "$x_G=\\dfrac{m_1x_1+m_2x_2}{m_1+m_2}$.", "Pour $P$, garde le signe de chaque vitesse."],
    rep_app=[c("$x_G$", 30, "cm", [(25, "Tu as pris le milieu : les masses sont différentes.")]),
             c("$P$", 0.1, "kg·m/s", [(0.7, "La seconde bille va dans l'autre sens : sa quantité de mouvement est négative.")])],
    rep_exos={1: [c("Distance au centre de la Terre", 4683, "km")], 2: [c("Vitesse du camion", 2, "m/s")]},
    pieges=["Placer $G$ au milieu alors que les masses sont différentes.", "Additionner les quantités de mouvement sans leurs signes."]),
"p2-a2": dict(
    entree=[("Une voiture roule à vitesse constante en ligne droite. La somme des forces qui s'exercent sur elle est :",
             ["dans le sens du mouvement", "nulle", "opposée au mouvement"], 1, "Principe de l'inertie : MRU, donc les forces se compensent.")],
    indices=["MRU : les forces se compensent.", "Sur l'horizontale : $F=f$.", "Sur la verticale : $R=P=mg$."],
    rep_app=[c("$F$", 500, "N"), c("$R$", 10000, "N")],
    rep_exos={2: [c("Tension", 4000, "N", [(400, "Multiplie par $g$ : la tension est une force, en newtons.")])]},
    pieges=["Croire qu'il faut une force nette vers l'avant pour avancer à vitesse constante.", "Oublier de préciser le référentiel."]),
"p2-b1": dict(
    entree=[("Une caisse accélère vers l'avant. La somme des forces qui s'exercent sur elle est :", ["nulle", "dans le sens de l'accélération", "opposée au mouvement"], 1,
             "$\\sum\\vec F=m\\vec a$ : même sens que $\\vec a$.")],
    indices=["Forces : poids, réaction, force de freinage.", "Projection sur l'axe du mouvement : $-f=ma$.", "Puis $0-v_0^2=2a\\,d$."],
    rep_app=[c("$a$", -5, "m/s²", [(5, "Le freinage s'oppose au mouvement : l'accélération est négative.")]), c("Distance d'arrêt", 40, "m")],
    rep_exos={1: [c("Tension", 6000, "N", [(5000, "C'est le poids : l'ascenseur accélère vers le haut, donc $T>mg$.")])], 2: [c("Distance", 12, "m")]},
    pieges=["Écrire le TCI sans avoir fait le bilan des forces.", "Projeter sans choisir d'axe ni de sens."]),
"p2-b2": dict(
    entree=[("Sans frottement, l'accélération d'un solide sur un plan incliné dépend :", ["de sa masse", "de l'angle (et de $g$)", "de sa vitesse"], 1,
             "$a=g\\sin\\alpha$ : la masse se simplifie.")],
    indices=["Projette le TCI sur l'axe parallèle au plan.", "$mg\\sin\\alpha-f=ma$.", "$a=5-\\dfrac{4}{2}$, puis $v^2=2a\\,d$."],
    rep_app=[c("$a$", 3, "m/s²", [(5, "Tu as oublié la force de frottement : $a=g\\sin\\alpha-\\frac{f}{m}$."), (1, "$\\frac{f}{m}=\\frac{4}{2}=2$, pas $4$.")]),
             c("$v$ après 2 m", 12 ** 0.5, "m/s")],
    rep_exos={1: [c("Distance", 3.6, "m")], 2: [c("$f$", 0.51, "N", tol=0.05)]},
    pieges=["Utiliser $\\cos\\alpha$ sur l'axe parallèle au plan.", "Croire que la réaction vaut $mg$ sur un plan incliné."]),
"p2-c1": dict(
    entree=[("Le travail de la réaction d'un plan sans frottement est :", ["positif", "nul", "négatif"], 1, "Elle est perpendiculaire au déplacement : $W=0$.")],
    indices=["$W(\\vec f)=-f\\times AB$.", "TEC : $\\frac12mv_B^2=W(\\vec P)+W(\\vec f)$.", "$\\frac12\\times2\\times v_B^2=20-8$."],
    rep_app=[c("$v_B$", 12 ** 0.5, "m/s", [(20 ** 0.5, "Tu as oublié le travail du frottement, qui est résistant.")])],
    rep_exos={1: [c("Distance de freinage", 25, "m")], 2: [c("Vitesse au sol", 20, "m/s")]},
    pieges=["Donner un signe positif au travail d'une force opposée au mouvement.", "Oublier l'énergie cinétique initiale quand le solide ne part pas du repos."]),
"p2-c2": dict(
    entree=[("Sans frottement, l'énergie mécanique :", ["augmente", "se conserve", "diminue"], 1, "Seul le poids travaille : $E_m$ reste constante.")],
    indices=["$E_m$ se conserve entre le bas et le sommet.", "$z_{\\max}=\\dfrac{v^2}{2g}$.", "Perte $=E_m$(départ) $-E_m$(sommet)."],
    rep_app=[c("Hauteur sans frottement", 3.2, "m"), c("Énergie perdue", 200, "J")],
    rep_exos={1: [c("Vitesse en bas", 10 ** 0.5, "m/s")], 2: [c("Énergie perdue", 2.75, "J")]},
    pieges=["Oublier de préciser la référence de l'énergie potentielle.", "Mettre $z$ en centimètres dans $mgz$."]),
"p2-d1": dict(
    entree=[("Avant le tir, le fusil et la balle sont immobiles. La quantité de mouvement totale vaut :", ["$0$", "$m\\,v_{\\text{balle}}$", "on ne peut pas savoir"], 0,
             "Tout est immobile : $\\vec P=\\vec 0$, et elle le reste juste après le tir.")],
    indices=["$\\vec P_{\\text{avant}}=\\vec 0$.", "$60\\,v_A+40\\times3=0$.", "$v_A=-\\dfrac{120}{60}$."],
    rep_app=[c("$v_A$", -2, "m/s", [(2, "Garde le signe : A part dans le sens opposé à B.")])],
    rep_exos={1: [c("Vitesse de recul", -2, "m/s", [(2, "Le canon recule : la vitesse est négative sur l'axe de l'obus.")])],
              2: [c("Vitesse de la barque", -1, "m/s", [(1, "La barque part en sens opposé : vitesse négative.")])]},
    pieges=["Oublier que les vitesses sont des vecteurs (signes).", "Appliquer la conservation à un système qui n'est pas isolé."]),
"p2-d2": dict(
    entree=[("Dans un choc mou, l'énergie cinétique du système :", ["se conserve", "diminue", "augmente"], 1,
             "Une partie devient chaleur et déformation. Seule la quantité de mouvement se conserve.")],
    indices=["Choc élastique, cible au repos : deux formules.", "$v_1'=\\dfrac{m_1-m_2}{m_1+m_2}v_1$.", "$v_2'=\\dfrac{2m_1}{m_1+m_2}v_1$."],
    rep_app=[c("$v_1'$", -1, "m/s", [(1, "La petite bille rebondit : sa vitesse est négative.")]), c("$v_2'$", 1, "m/s")],
    rep_exos={2: [c("Vitesse après le choc", 6, "m/s")]},
    pieges=["Conserver l'énergie cinétique dans un choc mou.", "Oublier que la bille légère peut rebondir (vitesse négative)."]),
}

FLASH = {
"A": [("Pour un mouvement rectiligne uniforme, l'accélération vaut :", ["$0$", "$v$", "$g$"], 0, "Vitesse constante en ligne droite : $\\vec a=\\vec 0$."),
      ("$v^2-v_0^2=2a(x-x_0)$ sert quand :", ["on connaît la durée", "on ne connaît pas la durée", "le mouvement est circulaire"], 1, "Elle ne contient pas le temps."),
      ("$54\\U{km/h}$ font :", ["$15\\ms$", "$54\\ms$", "$194\\ms$"], 0, "$54/3{,}6=15$.")],
"B": [("Principe de l'inertie : si les forces se compensent, le centre d'inertie est :", ["accéléré", "au repos ou en MRU", "en mouvement circulaire"], 1, "C'est l'énoncé du principe."),
      ("Pour un satellite, le référentiel adapté est :", ["terrestre", "géocentrique", "héliocentrique"], 1, "Centre de la Terre, axes vers des étoiles fixes."),
      ("L'unité de la quantité de mouvement est :", ["$\\mathrm{kg\\cdot m\\cdot s^{-1}}$", "$\\mathrm{N}$", "$\\mathrm{J}$"], 0, "$p=mv$.")],
"C": [("Le théorème du centre d'inertie s'écrit :", ["$\\sum\\vec F=m\\vec v$", "$\\sum\\vec F=m\\vec a_G$", "$\\sum\\vec F=\\vec 0$"], 1, "Dans un référentiel galiléen."),
      ("Sur un plan incliné sans frottement, $a$ vaut :", ["$g\\cos\\alpha$", "$g\\sin\\alpha$", "$g$"], 1, "Projection du poids sur l'axe du plan."),
      ("La réaction normale sur un plan incliné vaut :", ["$mg$", "$mg\\cos\\alpha$", "$mg\\sin\\alpha$"], 1, "Projection sur l'axe perpendiculaire au plan.")],
"D": [("L'énergie cinétique vaut :", ["$mv$", "$\\frac12mv^2$", "$mgz$"], 1, "$E_c=\\frac12mv^2$."),
      ("Quand un solide descend de $h$, le travail du poids vaut :", ["$mgh$", "$-mgh$", "$0$"], 0, "Le poids est moteur pendant la descente."),
      ("Sans frottement, l'énergie mécanique :", ["se conserve", "diminue", "augmente"], 0, "$E_m=E_c+E_p$ reste constante.")],
}

FINAL = dict(duree=120, exos=[
    dict(titre="La piste ABC (bac 2024)", pts=6, enonce=r"""
    __Extrait du bac S2 2024, exercice 3, partie 3.1.__ Un objet se déplace sur une piste située dans un plan vertical : $AB$ est rectiligne, de longueur $\ell=1\U{m}$, inclinée d'un angle $\alpha=30°$ par rapport à l'horizontale ; $BC$ est rectiligne, horizontale, de longueur $\ell=1\U{m}$. Sur $AB$ et $BC$ s'exercent des forces de frottement équivalentes à une force unique $\vec f$ parallèle à la piste, opposée au vecteur vitesse et d'intensité constante. Un solide $S$, ponctuel, de masse $m=200\U{g}$, part du point $A$ sans vitesse à la date $t=0$.

    1. Exprimer la norme $v_B$ de la vitesse du solide en $B$ en fonction de $m$, $g$, $\ell$, $f$ et $\alpha$.
    2. Calculer l'intensité de $\vec f$ pour que le solide arrive en $C$ avec une vitesse nulle.
    3. Déterminer la date à laquelle le solide arrive en $B$. On prendra $g=10\U{SI}$.
    """, corr=r"""
    1. TEC entre $A$ et $B$ : $\frac12mv_B^2-0=mg\ell\sin\alpha-f\ell$ ($\vec R$ ne travaille pas), donc $v_B=\sqrt{2\ell\left(g\sin\alpha-\dfrac{f}{m}\right)}$. **(2 pts)**
    2. TEC entre $A$ et $C$ : $0-0=mg\ell\sin\alpha-f\times2\ell$, donc $f=\dfrac{mg\sin\alpha}{2}=\dfrac{0{,}2\times10\times0{,}5}{2}=0{,}5\U{N}$. **(2 pts)**
    3. Sur $AB$, TCI projeté : $a=g\sin\alpha-\dfrac{f}{m}=5-2{,}5=2{,}5\mss$. Départ du repos : $\ell=\frac12at_B^2$, donc $t_B=\sqrt{\dfrac{2\ell}{a}}=\sqrt{0{,}8}\approx0{,}89\U{s}$ (et $v_B=\sqrt5\approx2{,}24\ms$). **(2 pts)**
    """),
    dict(titre="Le choc des chariots", pts=7, enonce=r"""
    Sur un rail horizontal, sans frottement, un chariot A de $2\U{kg}$ roulant à $3\ms$ heurte un chariot B de $1\U{kg}$ immobile. On prend $g=10\mss$.

    1. Le choc est élastique. Calculer les vitesses des chariots juste après le choc et vérifier la conservation de l'énergie cinétique.
    2. Si les chariots restaient accrochés (choc mou), quelle serait leur vitesse commune ? Quelle énergie serait perdue ?
    3. Après le choc élastique, B aborde un plan incliné de $30°$ sans frottement. Quelle distance parcourt-il sur ce plan avant de s'arrêter ?
    """, corr=r"""
    1. $v_A'=\dfrac{2-1}{3}\times3=1\ms$ ; $v_B'=\dfrac{2\times2}{3}\times3=4\ms$. $E_c$ : avant $\frac12\times2\times9=9\U{J}$ ; après $1+8=9\U{J}$. **(3 pts)**
    2. $2\times3=3\,v'$, donc $v'=2\ms$ ; $E_c$ après $=6\U{J}$ : $3\U{J}$ perdus. **(2 pts)**
    3. Conservation de $E_m$ (ou TEC) : $\frac12mv_B'^2=mg\,d\sin30°$, donc $d=\dfrac{16}{2\times10\times0{,}5}=1{,}6\U{m}$. **(2 pts)**
    """),
    dict(titre="La balance dans l'ascenseur", pts=7, enonce=r"""
    Une personne de $60\U{kg}$ se tient sur un pèse-personne posé au fond d'un ascenseur. Le pèse-personne mesure la réaction $R$ qu'il exerce sur la personne. On prend $g=10\mss$.

    1. Faire le bilan des forces sur la personne et écrire le TCI (axe vertical vers le haut).
    2. Calculer $R$ quand l'ascenseur démarre vers le haut avec $a=1{,}5\mss$, puis quand il monte à vitesse constante, puis quand il freine avant l'arrêt avec une décélération de $1{,}5\mss$.
    3. La cabine (masse totale $800\U{kg}$ avec la personne) monte de $12\U{m}$ à vitesse constante. Calculer le travail du poids et celui de la tension du câble. Justifier avec le TEC.
    """, corr=r"""
    1. Forces : poids $\vec P$ et réaction $\vec R$. TCI : $\vec P+\vec R=m\vec a$, soit $R-mg=ma$. **(2 pts)**
    2. Démarrage : $R=60\times11{,}5=690\U{N}$. Vitesse constante : $R=600\U{N}$. Freinage ($a=-1{,}5$) : $R=60\times8{,}5=510\U{N}$. **(3 pts)**
    3. $W(\vec P)=-mgh=-800\times10\times12=-96\,000\U{J}$. Vitesse constante : $\Delta E_c=0=W(\vec P)+W(\vec T)$, donc $W(\vec T)=+96\,000\U{J}$. **(2 pts)**
    """),
])
