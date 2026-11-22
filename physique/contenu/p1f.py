# -*- coding: utf-8 -*-
"""P1 : les deux évaluations de fin de chapitre (2 h chacune). Chacune balaie toutes les questions types
du chapitre ; « revoir » relie chaque groupe de questions aux étapes à reprendre."""

EVAL1 = dict(duree=120, exos=[
    dict(titre="Mouvement plan : du vecteur accélération à la base de Frenet", pts=7, enonce=r"""
    Dans un repère $(O;\vec i,\vec j)$, $O$ au sol, $(Oy)$ vertical vers le haut, un mobile a une accélération constante $\vec a=-10\,\vec j$ (SI). À $t=0$, il est en $O$ avec la vitesse $\vec v_0=6\,\vec i+8\,\vec j$.

    1. Déterminer les coordonnées du vecteur vitesse $\vec v(t)$, puis les équations horaires $x(t)$ et $y(t)$.
    2. Établir l'équation de la trajectoire et préciser sa nature. Préciser la nature du mouvement de la projection du mobile sur chaque axe.
    3. Calculer la valeur $v_0$ de la vitesse initiale et l'angle $\alpha$ que $\vec v_0$ fait avec l'horizontale.
    4. Déterminer la date et les coordonnées du sommet $S$. Que vaut la vitesse en $S$ ?
    5. À quelle date le mobile revient-il au sol ? Calculer la portée et la vitesse d'arrivée.
    6. Calculer $a_t$, $a_n$ et le rayon de courbure à $t=0$, puis au sommet. Commenter.
    7. En justifiant par le signe de $\vec v\cdot\vec a$, préciser la nature du mouvement avant puis après le sommet.
    """, corr=r"""
    1. $v_x=6$ et $v_y=-10t+8$ (primitives de $\vec a$, constantes fixées par $\vec v_0$). Puis $x=6t$ et $y=-5t^2+8t$ (le mobile part de $O$). **(1 pt)**
    2. $t=\dfrac{x}{6}$, donc $y=-\dfrac{5}{36}x^2+\dfrac{4}{3}x$ : **parabole**. Sur $(Ox)$ : $v_x$ constante, MRU ; sur $(Oy)$ : $a_y=-10$ constante, MRUV. **(1 pt)**
    3. $v_0=\sqrt{36+64}=10\ms$ ; $\tan\alpha=\dfrac86$, donc $\alpha\approx53{,}1°$. **(0,75 pt)**
    4. Sommet : $v_y=0$, $t_S=0{,}8\U{s}$ ; $S(4{,}8\,;\,3{,}2)$ ; $v_S=6\ms$ (horizontale). **(1 pt)**
    5. $y=0$ pour $t=1{,}6\U{s}$ ; portée $x=9{,}6\U{m}$ ; $\vec v\,(6\,;\,-8)$, donc $v=10\ms$ (même valeur qu'au départ). **(0,75 pt)**
    6. À $t=0$ : $a_t=\dfrac{6\times0+8\times(-10)}{10}=-8\mss$, $a_n=\dfrac{|6\times(-10)-8\times0|}{10}=6\mss$ ($64+36=100=a^2$), $\rho_0=\dfrac{100}{6}\approx16{,}7\U{m}$. Au sommet : $a_t=0$, $a_n=a=10\mss$, $\rho_S=\dfrac{36}{10}=3{,}6\U{m}$. La trajectoire est la plus courbée au sommet. **(1,5 pt)**
    7. $\vec v\cdot\vec a=-10(-10t+8)$ : négatif pour $t<0{,}8\U{s}$ (**retardé**), positif après (**accéléré**). **(1 pt)**
    """, revoir=[("questions 1 et 2", ["p1-a2", "p1-a1"]), ("questions 3 à 5", ["p1-a2"]), ("questions 6 et 7", ["p1-b1"])]),
    dict(titre="Mouvements rectilignes : la course d'élan (d'après bac 2018)", pts=6, enonce=r"""
    __La question 1 est extraite du bac S2 2018 (exercice 3, question 3.1).__ Dans la course d'élan du triple saut, l'athlète, partie sans vitesse initiale, parcourt $32\U{m}$ pour arriver au point A de la ligne d'envol avec une vitesse horizontale de norme $8\ms$. Le mouvement est supposé rectiligne uniformément varié.

    1. Évaluer l'accélération du mouvement et le temps mis par l'athlète sur ce parcours.
    2. Écrire $x(t)$ et $v(t)$, l'origine des espaces et des dates étant prise au départ.
    3. Un enregistrement donne les positions de l'athlète toutes les $\tau=0{,}5\U{s}$ à partir de $t=2\U{s}$ : $M_0M_1=1{,}125\U{m}$, $M_1M_2=1{,}375\U{m}$, $M_2M_3=1{,}625\U{m}$. Montrer qu'il confirme la nature du mouvement et la valeur de $a$. Calculer la vitesse au point $M_1$.
    4. Au départ de l'athlète, son entraîneur, posté en A, court vers elle à la vitesse constante de $4\ms$. Écrire son équation horaire, puis déterminer la date et le lieu de leur rencontre.
    5. Lors d'un essai, l'athlète renonce au saut : partie de A à $8\ms$, elle s'arrête en $4\U{m}$ d'un mouvement uniformément varié. Calculer sa décélération et la durée de l'arrêt. Justifier la nature du mouvement.
    """, corr=r"""
    1. $v_A^2-0=2a\,d$, donc $a=\dfrac{64}{64}=1\mss$ ; $t=\dfrac{v_A}{a}=8\U{s}$. **(1 pt)**
    2. $x=\frac12t^2$ et $v=t$ (SI). **(0,5 pt)**
    3. Les distances augmentent toujours de $\Delta d=0{,}25\U{m}$ : MRUV avec $a=\dfrac{\Delta d}{\tau^2}=\dfrac{0{,}25}{0{,}25}=1\mss$. $v_1=\dfrac{M_0M_2}{2\tau}=\dfrac{2{,}5}{1}=2{,}5\ms$ (c'est bien $v(2{,}5)=2{,}5$). **(1,5 pt)**
    4. $x_E=32-4t$ (il va dans le sens négatif). $\frac12t^2=32-4t\iff t^2+8t-64=0$, donc $t=-4+4\sqrt5\approx4{,}94\U{s}$ et $x\approx12{,}2\U{m}$. **(1,5 pt)**
    5. $0-64=2a\times4$, donc $a=-8\mss$ ; $0=-8t+8$, donc $t=1\U{s}$. $a\cdot v<0$ : mouvement **retardé**. **(1,5 pt)**
    """, revoir=[("questions 1 et 2", ["p1-c2"]), ("question 3", ["p1-c3"]), ("question 4", ["p1-c1", "p1-c2"]), ("question 5", ["p1-c2"])]),
    dict(titre="Mouvement sinusoïdal et mouvements circulaires", pts=7, enonce=r"""
    Un mobile $M$ effectue un mouvement rectiligne sinusoïdal sur un axe $x'Ox$ de centre $O$ : $x(t)=X_m\cos(\omega t+\varphi)$. Sa courbe $x(t)$ est donnée ci-dessous.

    [[graphe:p1-ev1-x]]

    1. Déterminer graphiquement $X_m$, $T$, la fréquence $N$, puis $\omega$.
    2. Déterminer $\varphi$ en utilisant le sens du mouvement à $t=0$. Écrire $x(t)$.
    3. Établir $v(t)$, calculer $v_{\max}$, montrer que $a=-\omega^2x$ et écrire l'équation différentielle.
    4. Déterminer par le calcul les dates des deux premiers passages par $O$, avec le sens du mouvement. Vérifier sur la courbe.
    5. Calculer la valeur de la vitesse en $x=1\U{cm}$. Quelle est l'allure de la courbe $v^2=f(x^2)$ ?
    6. En justifiant par le signe de $\vec v\cdot\vec a$, préciser la nature du mouvement entre $t=0$ et la première arrivée en $x=-2\U{cm}$.
    7. Un point $P$ décrit un cercle de centre $O$, de rayon $X_m$, à la vitesse angulaire $\omega$ ; $M$ est sa projection. Donner la position angulaire de $P$ à $t=0$ (repérée depuis $(Ox)$, sens trigonométrique), sa vitesse et son accélération. Comparer à $v_{\max}$ et $a_{\max}$.
    8. Le disque qui porte $P$ est freiné uniformément et s'arrête après 5 tours. Calculer l'accélération angulaire et la durée du freinage.
    """, corr=r"""
    1. $X_m=2\U{cm}$ ; $T=0{,}4\U{s}$ ; $N=2{,}5\U{Hz}$ ; $\omega=5\pi\U{rad\cdot s^{-1}}$. **(0,75 pt)**
    2. $x_0=-1\U{cm}$ : $\cos\varphi=-\frac12$ ; la courbe descend, $v_0<0$, donc $\sin\varphi>0$ : $\varphi=\dfrac{2\pi}{3}$. $x=2\cos\left(5\pi t+\dfrac{2\pi}{3}\right)$ (cm). **(1 pt)**
    3. $v=-0{,}1\pi\sin\left(5\pi t+\frac{2\pi}{3}\right)$ ($\mathrm{m\cdot s^{-1}}$) ; $v_{\max}=0{,}1\pi\approx0{,}314\ms$. $a=-25\pi^2x$, donc $\ddot x+25\pi^2x=0$. **(1 pt)**
    4. $\cos\theta=0$ ; l'angle part de $\frac{2\pi}{3}$ : $\theta=\frac{3\pi}{2}$ donne $t=\dfrac16\approx0{,}167\U{s}$ ($\sin<0$ : sens **positif**) ; $\theta=\frac{5\pi}{2}$ donne $t=\dfrac{11}{30}\approx0{,}367\U{s}$ (sens **négatif**). **(1 pt)**
    5. $|v|=5\pi\sqrt{4-1}\approx27{,}2\U{cm\cdot s^{-1}}$. $v^2=\omega^2(X_m^2-x^2)$ : droite décroissante de pente $-25\pi^2$. **(0,75 pt)**
    6. De $t=0$ à $t=\frac{1}{15}\U{s}$ : $x<0$ donc $a=-\omega^2x>0$, et $v<0$ ; $\vec v\cdot\vec a<0$ : **retardé** (le mobile ralentit jusqu'à l'extrémité). **(0,5 pt)**
    7. Position angulaire $\frac{2\pi}{3}$ ; $v_P=r\omega=0{,}314\ms=v_{\max}$ ; $a_P=r\omega^2\approx4{,}93\mss=a_{\max}$. **(1 pt)**
    8. $\theta=10\pi\U{rad}$ ; $0-(5\pi)^2=2\,\ddot\theta\times10\pi$, donc $\ddot\theta=-1{,}25\pi\approx-3{,}93\U{rad\cdot s^{-2}}$ ; durée $\dfrac{5\pi}{1{,}25\pi}=4\U{s}$. **(1 pt)**
    """, revoir=[("questions 1 à 3", ["p1-d1"]), ("questions 4 à 6", ["p1-d2"]), ("question 7", ["p1-e1"]), ("question 8", ["p1-e2"])]),
])

EVAL2 = dict(duree=120, exos=[
    dict(titre="Mouvement plan et base de Frenet", pts=7, enonce=r"""
    Un mobile a pour équations horaires $x=2t+1$ et $y=t^2-2t$ (SI, $t\geq0$).

    1. Établir l'équation de la trajectoire et la nommer. Où est le mobile à $t=0$ ?
    2. Déterminer $\vec v$ et $\vec a$. Montrer que l'accélération est constante.
    3. À $t=0$, calculer $v$, $a_t$, $a_n$ et le rayon de courbure.
    4. À quelle date la vitesse est-elle minimale ? Où est alors le mobile ? Calculer $a_t$, $a_n$ et le rayon de courbure en ce point.
    5. En justifiant par le signe de $\vec v\cdot\vec a$, préciser la nature du mouvement.
    6. À quelle date et en quel point le mobile recoupe-t-il l'axe $(Ox)$ ? Avec quelle vitesse ?
    """, corr=r"""
    1. $t=\dfrac{x-1}{2}$, donc $y=\dfrac{(x-1)^2}{4}-(x-1)$ : parabole ; à $t=0$, $M_0(1\,;\,0)$. **(1 pt)**
    2. $\vec v\,(2\,;\,2t-2)$ et $\vec a\,(0\,;\,2)$ : vecteur constant, $a=2\mss$. **(1 pt)**
    3. $\vec v_0\,(2\,;\,-2)$, $v_0=2\sqrt2\approx2{,}83\ms$ ; $a_t=\dfrac{2\times0+(-2)\times2}{2{,}83}\approx-1{,}41\mss$ ; $a_n=\dfrac{|2\times2-(-2)\times0|}{2{,}83}\approx1{,}41\mss$ ; $\rho=\dfrac{8}{1{,}41}\approx5{,}66\U{m}$. **(2 pts)**
    4. $v^2=4+(2t-2)^2$ est minimal pour $t=1\U{s}$ : $v=2\ms$, point $(3\,;\,-1)$. Là, $a_t=0$, $a_n=2\mss$, $\rho=\dfrac{4}{2}=2\U{m}$. **(1,5 pt)**
    5. $\vec v\cdot\vec a=4t-4$ : retardé pour $t<1\U{s}$, accéléré ensuite. **(0,75 pt)**
    6. $y=0$ avec $t>0$ : $t=2\U{s}$, point $(5\,;\,0)$, $\vec v\,(2\,;\,2)$, $v\approx2{,}83\ms$. **(0,75 pt)**
    """, revoir=[("questions 1, 2 et 6", ["p1-a1", "p1-a2"]), ("questions 3 à 5", ["p1-b1"])]),
    dict(titre="Mouvements rectilignes : graphes et rencontre (partie A : bac 2012)", pts=6, enonce=r"""
    __Partie A : extrait du bac S2 2012, exercice 3, partie 3.1 (figures redessinées).__ On étudie le centre d'inertie d'un boulet lancé à $t=0$. Les graphes donnent les composantes horizontale $v_x$ et verticale $v_y$ de sa vitesse.

    [[graphe:bac12-vx]]

    [[graphe:bac12-vy]]

    1. Déterminer $v_{0x}$ et la nature du mouvement de la projection sur $Ox$.
    2. Déterminer $v_{0y}$, la nature du mouvement de la projection sur $Oy$ et l'accélération $a_y$.
    3. Exprimer $v_{0x}$ et $v_{0y}$ en fonction de $V_0$ et de l'angle $\alpha$ de $\vec V_0$ avec l'horizontale.
    4. En déduire $V_0$ et $\alpha$.

    __Partie B.__ Au moment où un feu passe au vert ($t=0$), une voiture démarre avec $a=2\mss$ ; au même instant, un camion roulant à $10\ms$ constante se trouve $100\U{m}$ devant elle, dans le même sens. Origine : le feu.

    5. Écrire les équations horaires de la voiture et du camion.
    6. Déterminer la date et le lieu où la voiture rattrape le camion.
    7. Calculer la vitesse de la voiture à cet instant ; la retrouver avec la relation indépendante du temps.
    """, corr=r"""
    1. $v_{0x}=10\ms$ ; $v_x$ constante : MRU sur $Ox$. **(0,5 pt)**
    2. $v_{0y}=9\ms$ ; $v_y$ affine décroissante : MRUV (décéléré puis accéléré) ; $a_y\approx\dfrac{0-9}{0{,}92}\approx-9{,}8\mss$. **(1 pt)**
    3. $v_{0x}=V_0\cos\alpha$ et $v_{0y}=V_0\sin\alpha$. **(0,5 pt)**
    4. $V_0=\sqrt{100+81}\approx13{,}5\ms$ ; $\tan\alpha=0{,}9$, $\alpha\approx42°$ (corrigé officiel). **(1 pt)**
    5. $x_V=t^2$ et $x_C=10t+100$. **(1 pt)**
    6. $t^2-10t-100=0$, donc $t=5+5\sqrt5\approx16{,}2\U{s}$ ; $x\approx262\U{m}$. **(1 pt)**
    7. $v=2t\approx32{,}4\ms$ ; $v^2=2\times2\times262\approx1047$, donc $v\approx32{,}4\ms$. **(1 pt)**
    """, revoir=[("questions 1 à 4", ["p1-c3", "p1-a2"]), ("questions 5 à 7", ["p1-c1", "p1-c2"])]),
    dict(titre="Mouvement sinusoïdal et mouvements circulaires", pts=7, enonce=r"""
    Un mobile vérifie l'équation différentielle $\ddot x+400\,x=0$ (SI). À $t=0$, il passe par le centre $O$ dans le sens positif, à la vitesse $v_0=0{,}6\ms$.

    1. Quelle est la nature du mouvement ? Calculer $\omega$ et $T$.
    2. Calculer $X_m$, déterminer $\varphi$ et écrire $x(t)$.
    3. Établir la relation entre $v^2$ et $x^2$. Décrire la courbe $v^2=f(x^2)$ (pente, ordonnée à l'origine).
    4. Déterminer la date du premier passage en $x=1{,}5\U{cm}$ dans le sens négatif, et la valeur de la vitesse en ce point.
    5. Calculer la distance parcourue entre $t=0$ et $t=0{,}2\U{s}$.
    6. Un point $P$ de la périphérie d'une roue de rayon $3\U{cm}$ tourne uniformément à $20\U{rad\cdot s^{-1}}$. Calculer sa vitesse et son accélération ; comparer à $v_{\max}$ et $a_{\max}$ du mobile.
    7. Cette roue est partie du repos et a atteint $20\U{rad\cdot s^{-1}}$ en $2\U{s}$, d'un mouvement uniformément accéléré. Calculer l'accélération angulaire, le nombre de tours effectués et, à $t=2\U{s}$, les accélérations tangentielle et normale de $P$.
    """, corr=r"""
    1. Forme $\ddot x+\omega^2x=0$ : rectiligne sinusoïdal ; $\omega=20\U{rad\cdot s^{-1}}$, $T=\dfrac{\pi}{10}\approx0{,}314\U{s}$. **(1 pt)**
    2. Au centre, $v_0=v_{\max}=X_m\omega$, donc $X_m=0{,}03\U{m}$ ; $x_0=0$ et sens positif : $\varphi=-\dfrac{\pi}{2}$. $x=3\cos\left(20t-\dfrac{\pi}{2}\right)$ (cm). **(1 pt)**
    3. $v^2=\omega^2(X_m^2-x^2)=0{,}36-400\,x^2$ : droite de pente $-400\U{s^{-2}}$, d'ordonnée à l'origine $0{,}36\U{m^2\cdot s^{-2}}$. **(1 pt)**
    4. $\cos\theta=\frac12$ et $\sin\theta>0$ : $\theta=\frac{\pi}{3}$ ; $20t=\frac{\pi}{3}+\frac{\pi}{2}$, donc $t=\dfrac{\pi}{24}\approx0{,}131\U{s}$. $|v|=20\sqrt{9-2{,}25}\approx52\U{cm\cdot s^{-1}}$. **(1 pt)**
    5. Le mobile atteint $+3\U{cm}$ à $t=\frac{\pi}{40}\approx0{,}079\U{s}$, puis repart ; à $0{,}2\U{s}$ (avant le demi-tour suivant, à $0{,}236\U{s}$) : $x=3\cos(4-\frac{\pi}{2})\approx-2{,}27\U{cm}$. Distance : $3+5{,}27\approx8{,}27\U{cm}$. **(1 pt)**
    6. $v=R\omega=0{,}6\ms=v_{\max}$ ; $a=R\omega^2=12\mss=a_{\max}$. **(0,75 pt)**
    7. $\ddot\theta=10\U{rad\cdot s^{-2}}$ ; $\theta=\frac12\times10\times4=20\U{rad}$, soit $\approx3{,}2$ tours ; $a_t=R\ddot\theta=0{,}3\mss$, $a_n=R\dot\theta^{\,2}=12\mss$. **(1,25 pt)**
    """, revoir=[("questions 1 et 2", ["p1-d1"]), ("questions 3 à 5", ["p1-d2"]), ("question 6", ["p1-e1"]), ("question 7", ["p1-e2"])]),
])

FINALS = [EVAL1, EVAL2]
