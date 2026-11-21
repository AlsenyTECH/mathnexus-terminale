# -*- coding: utf-8 -*-
"""P2 Bases de la dynamique : parties A (centre d'inertie, référentiels) et B (théorème du centre d'inertie)."""
from build import retenir, prof, cours, soustitre

G10 = r"On prend $g=10\mss$."

# =====================================================================
# PARTIE A — Centre d'inertie, quantité de mouvement, référentiels
# =====================================================================
A1 = dict(
    id="p2-a1", titre="Centre d'inertie et quantité de mouvement", duree=15,
    objectif="Placer le centre d'inertie d'un système et calculer sa quantité de mouvement.",
    cours=[
        retenir("Centre d'inertie", r"""
        Le centre d'inertie $G$ d'un système est le barycentre de ses points affectés de leurs masses. Pour des solides de masses $m_1, m_2,\dots$ et de centres $G_1, G_2,\dots$ :

        $$\vect{OG}=\frac{m_1\vect{OG_1}+m_2\vect{OG_2}+\cdots}{m_1+m_2+\cdots}\qquad\text{sur un axe : }x_G=\frac{m_1x_1+m_2x_2+\cdots}{m_1+m_2+\cdots}$$

        Pour un solide homogène et symétrique, $G$ est au centre de symétrie (milieu d'une tige, centre d'une sphère).
        """),
        retenir("Quantité de mouvement", r"""
        $$\vec p=m\,\vec v_G\quad(\mathrm{kg\cdot m\cdot s^{-1}})\qquad\text{système : }\vec P=\vec p_1+\vec p_2+\cdots=M\,\vec v_G$$
        """),
        prof(r"""
        Choisis l'origine de l'axe sur l'un des objets : un terme du numérateur devient nul et le calcul est plus court.
        """),
    ],
    video=dict(id="p2-a1", titre="Centre d'inertie et quantité de mouvement", phrases=[
        ("Le centre d'inertie et la quantité de mouvement.", "Centre d'inertie"),
        ("Le centre d'inertie d'un système est le barycentre de ses parties, chacune affectée de sa masse. Sur un axe, x G égale la somme des m x, divisée par la masse totale.", r"x_G=\dfrac{m_1x_1+m_2x_2+\cdots}{m_1+m_2+\cdots}"),
        ("Exemple : une tige de soixante-douze centimètres et de masse m porte une masse deux m à l'extrémité A, et trois m à l'extrémité B.", r"m\ (\text{tige}),\ 2m\ (A),\ 3m\ (B)"),
        ("On place l'origine en A. La masse deux m est à zéro, la tige compte en son milieu, à trente-six centimètres, et la masse trois m est à soixante-douze centimètres.", r"x_A=0,\ x_{\text{tige}}=36,\ x_B=72"),
        ("A G égale m fois trente-six, plus trois m fois soixante-douze, le tout divisé par six m. Les m se simplifient : on trouve quarante-deux centimètres.", r"AG=\dfrac{36m+216m}{6m}=42\ \mathrm{cm}"),
        ("La quantité de mouvement d'un solide est le produit de sa masse par la vitesse de son centre d'inertie. C'est un vecteur.", r"\vec p=m\,\vec v_G"),
        ("Pour un système, on additionne les vecteurs. Attention aux signes : deux objets qui vont en sens contraires se compensent en partie.", r"\vec P=\vec p_1+\vec p_2"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("la tige lestée", r"""
    Une tige homogène $AB$ de longueur $72\U{cm}$ et de masse $m$ porte en $A$ une masselotte de masse $2m$ et en $B$ une masselotte de masse $3m$ (masselottes ponctuelles). Déterminer la position du centre d'inertie $G$ du système.
    """, r"""
    Axe d'origine $A$, dirigé vers $B$. Le centre de la tige est en $x=36\U{cm}$.

    $AG=\dfrac{2m\times0+m\times36+3m\times72}{2m+m+3m}=\dfrac{252\,m}{6\,m}=42\U{cm}$. $G$ est à $42\U{cm}$ de $A$, du côté de la masse la plus lourde.
    """),
    application=("deux billes", r"""
    Une bille de $200\U{g}$ est en $x=0$ et une bille de $300\U{g}$ en $x=50\U{cm}$.

    1. Calculer $x_G$.
    2. La première bille roule à $+2\ms$ et la seconde à $-1\ms$ sur l'axe. Calculer la quantité de mouvement du système.
    """, r"""
    1. $x_G=\dfrac{0{,}2\times0+0{,}3\times50}{0{,}5}=30\U{cm}$.
    2. $P=0{,}2\times2+0{,}3\times(-1)=0{,}1\U{kg\cdot m\cdot s^{-1}}$, dirigée dans le sens de l'axe.
    """),
    exos=[
        ("le système Terre-Lune", r"""
        La masse de la Terre vaut 81 fois celle de la Lune ; la distance entre leurs centres vaut $384\,000\U{km}$. Où est le centre d'inertie du système Terre-Lune ? Est-il à l'intérieur de la Terre (rayon $6400\U{km}$) ?
        """, r"""
        Origine au centre de la Terre : $x_G=\dfrac{81M_L\times0+M_L\times384\,000}{82\,M_L}\approx4683\U{km}$. C'est moins que $6400\U{km}$ : $G$ est **à l'intérieur de la Terre**.
        """),
        ("comparer des quantités de mouvement", r"""
        1. Calculer la quantité de mouvement d'une voiture de $1000\U{kg}$ roulant à $72\U{km/h}$.
        2. À quelle vitesse un camion de $10\U{t}$ a-t-il la même quantité de mouvement ?
        """, r"""
        1. $p=1000\times20=2\times10^4\U{kg\cdot m\cdot s^{-1}}$.
        2. $v=\dfrac{2\times10^4}{10^4}=2\ms=7{,}2\U{km/h}$.
        """),
    ],
)

A2 = dict(
    id="p2-a2", titre="Référentiels galiléens et principe de l'inertie", duree=15,
    objectif="Choisir le bon référentiel et utiliser le principe de l'inertie pour trouver une force inconnue.",
    cours=[
        retenir("Référentiels galiléens", r"""
        Un référentiel est galiléen si le principe de l'inertie y est vérifié.

        - **Terrestre** (le sol) : mouvements sur Terre de courte durée.
        - **Géocentrique** (centre de la Terre, axes vers des étoiles fixes) : satellites, Lune.
        - **Héliocentrique** (centre du Soleil) : planètes.
        """),
        retenir("Principe de l'inertie", r"""
        Dans un référentiel galiléen, si les forces extérieures appliquées à un système se compensent ($\sum\vec F_{\text{ext}}=\vec 0$), son centre d'inertie est au repos ou en mouvement rectiligne uniforme, et réciproquement.

        - Système **isolé** : aucune force. **Pseudo-isolé** : les forces se compensent.
        """),
        prof(r"""
        « Vitesse constante en ligne droite » se traduit toujours par « les forces se compensent ». C'est la clé pour trouver une force de frottement ou une tension.
        """),
    ],
    video=dict(id="p2-a2", titre="Le principe de l'inertie", phrases=[
        ("Référentiels galiléens et principe de l'inertie.", "Principe de l'inertie"),
        ("Un mouvement se décrit toujours dans un référentiel. Pour un objet sur Terre, on prend le référentiel terrestre. Pour un satellite, le géocentrique. Pour une planète, l'héliocentrique.", r"\text{terrestre}\ \cdot\ \text{géocentrique}\ \cdot\ \text{héliocentrique}"),
        ("Le principe de l'inertie : si les forces extérieures se compensent, le centre d'inertie est immobile, ou en mouvement rectiligne uniforme.", r"\sum\vec F_{\text{ext}}=\vec 0\iff\vec v_G=\vec{\text{cte}}"),
        ("Il marche dans les deux sens. Si un objet avance en ligne droite à vitesse constante, alors les forces se compensent.", r"\text{MRU}\Rightarrow\sum\vec F=\vec 0"),
        ("Exemple : une voiture roule à vitesse constante sur une route droite et horizontale. Les frottements valent cinq cents newtons.", r"f=500\ \mathrm N"),
        ("Les forces se compensent : le poids et la réaction verticale s'annulent, et la force motrice compense les frottements. Elle vaut donc cinq cents newtons.", r"F=f=500\ \mathrm N"),
        ("Un piège courant : croire qu'il faut une force dans le sens du mouvement pour avancer. Non : à vitesse constante, la somme des forces est nulle.", r"\vec v=\text{cte}\ \Rightarrow\ \sum\vec F=\vec 0"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("le mobile autoporteur", r"""
    Un mobile autoporteur glisse sur une table horizontale ; un coussin d'air supprime les frottements. On enregistre ses positions à intervalles réguliers. Que prévoit le principe de l'inertie, et que doit-on observer ?
    """, r"""
    Système : le mobile. Référentiel terrestre, supposé galiléen. Forces : le poids $\vec P$ et la réaction $\vec R$ du coussin d'air, verticale, qui le compense : $\vec P+\vec R=\vec 0$.

    D'après le principe de l'inertie, le centre d'inertie est en **mouvement rectiligne uniforme** : sur l'enregistrement, les points de $G$ sont alignés et régulièrement espacés.
    """),
    application=("la voiture à vitesse constante", r"""
    Une voiture de $1000\U{kg}$ roule à vitesse constante sur une route droite et horizontale. Les frottements sont équivalents à une force de $500\U{N}$ opposée au mouvement. """ + G10 + r"""

    Faire le bilan des forces et calculer la force motrice $\vec F$ et la réaction verticale $\vec R$.
    """, r"""
    Forces : poids $\vec P$, réaction $\vec R$, force motrice $\vec F$, frottements $\vec f$. Mouvement rectiligne uniforme, donc $\vec P+\vec R+\vec F+\vec f=\vec 0$.

    Sur l'horizontale : $F=f=500\U{N}$. Sur la verticale : $R=P=mg=10^4\U{N}$.
    """),
    exos=[
        ("choisir le référentiel", r"""
        Quel référentiel choisir pour étudier : a) un satellite autour de la Terre ; b) la Terre autour du Soleil ; c) un ballon de football ?
        """, r"""
        a) Géocentrique. b) Héliocentrique. c) Terrestre.
        """),
        ("l'ascenseur", r"""
        Un ascenseur de $400\U{kg}$ monte à vitesse constante. """ + G10 + r""" Calculer la tension du câble.
        """, r"""
        Forces : poids et tension. Mouvement rectiligne uniforme : $\vec T+\vec P=\vec 0$, donc $T=mg=4000\U{N}$.
        """),
    ],
)

EVAL_A = dict(duree=30, exos=[
    dict(titre="L'haltère", pts=10, enonce=r"""
    Un haltère est formé d'une barre homogène de masse $1\U{kg}$ et de deux boules : $m_1=2\U{kg}$ et $m_2=3\U{kg}$, dont les centres sont aux extrémités de la barre, distants de $50\U{cm}$.

    1. Déterminer la position du centre d'inertie $G$ par rapport au centre de la boule 1.
    2. L'haltère est déplacé en translation à $0{,}5\ms$. Calculer sa quantité de mouvement.
    3. Un élève affirme : « $G$ est au milieu de la barre ». Expliquer son erreur.
    """, corr=r"""
    1. Origine au centre de la boule 1 : $x_G=\dfrac{2\times0+1\times25+3\times50}{6}=\dfrac{175}{6}\approx29{,}2\U{cm}$. **(5 pts)**
    2. $P=Mv_G=6\times0{,}5=3\U{kg\cdot m\cdot s^{-1}}$. **(3 pts)**
    3. Les boules n'ont pas la même masse : $G$ est décalé vers la plus lourde, la boule 2. **(2 pts)**
    """),
    dict(titre="Le bloc tiré à vitesse constante", pts=10, enonce=r"""
    Un bloc de masse $4\U{kg}$ est tiré sur un plan horizontal par une force horizontale $\vec F$ de valeur $12\U{N}$. Il se déplace en ligne droite à vitesse constante. """ + G10 + r"""

    1. Énoncer le principe de l'inertie.
    2. Faire le bilan des forces. En déduire la force de frottement $\vec f$ et la composante normale $\vec R_N$ de la réaction.
    3. Calculer la valeur de la réaction totale $\vec R=\vec R_N+\vec f$ et l'angle qu'elle fait avec la verticale.
    """, corr=r"""
    1. Dans un référentiel galiléen, si les forces se compensent, le centre d'inertie est au repos ou en MRU (et réciproquement). **(2 pts)**
    2. Forces : $\vec P$, $\vec F$, $\vec R_N$, $\vec f$. MRU : leur somme est nulle. Horizontale : $f=F=12\U{N}$. Verticale : $R_N=mg=40\U{N}$. **(4 pts)**
    3. $R=\sqrt{40^2+12^2}\approx41{,}8\U{N}$ ; $\tan\varphi=\dfrac{12}{40}$, donc $\varphi\approx16{,}7°$. **(4 pts)**
    """),
])

# =====================================================================
# PARTIE B — Théorème du centre d'inertie
# =====================================================================
B1 = dict(
    id="p2-b1", titre="Le théorème du centre d'inertie et sa méthode", duree=20,
    objectif="Appliquer le théorème du centre d'inertie en cinq temps pour calculer une accélération ou une force.",
    cours=[
        retenir("Théorème du centre d'inertie (TCI)", r"""
        Dans un référentiel galiléen :

        $$\sum\vec F_{\text{ext}}=m\,\vec a_G$$

        C'est la relation fondamentale de la dynamique appliquée au centre d'inertie. Si la somme des forces est constante, $\vec a_G$ est constante : le mouvement est uniformément varié.
        """),
        retenir("La méthode en cinq temps", r"""
        1. **Système** : je le nomme.
        2. **Référentiel** : terrestre, supposé galiléen.
        3. **Bilan des forces** : je les nomme et je les représente sur un schéma.
        4. **TCI** : j'écris la relation vectorielle.
        5. **Projection** sur un axe bien choisi (souvent celui du mouvement), puis calcul.
        """),
        prof(r"""
        Le correcteur note la méthode autant que le résultat : écris les cinq temps, même quand le calcul te paraît évident.
        """),
    ],
    video=dict(id="p2-b1", titre="Le TCI en cinq temps", phrases=[
        ("Le théorème du centre d'inertie, en cinq temps.", "Théorème du centre d'inertie"),
        ("Dans un référentiel galiléen, la somme des forces extérieures égale la masse fois l'accélération du centre d'inertie.", r"\sum\vec F_{\text{ext}}=m\,\vec a_G"),
        ("Exemple : une caisse de cinquante kilogrammes, au repos, est tirée horizontalement par une force de deux cents newtons. Les frottements valent cinquante newtons.", r"m=50\ \mathrm{kg},\ F=200\ \mathrm N,\ f=50\ \mathrm N"),
        ("Premier temps, le système : la caisse. Deuxième temps, le référentiel : terrestre, supposé galiléen.", r"\text{système, référentiel}"),
        ("Troisième temps, le bilan des forces : le poids, la réaction normale, la force de traction, et les frottements.", r"\vec P,\ \vec R,\ \vec F,\ \vec f"),
        ("Quatrième temps, le théorème : la somme de ces quatre vecteurs égale m a. Cinquième temps, la projection sur l'axe du mouvement : F moins f égale m a.", r"F-f=ma"),
        ("Deux cents moins cinquante, divisé par cinquante : a égale trois mètres par seconde carrée. L'accélération est constante : le mouvement est uniformément accéléré.", r"a=\dfrac{150}{50}=3\ \mathrm{m\cdot s^{-2}}"),
        ("On enchaîne avec la cinématique : après quatre secondes, v égale douze mètres par seconde, et la caisse a parcouru vingt-quatre mètres.", r"v=12\ \mathrm{m/s},\ d=24\ \mathrm m"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("la caisse tirée", r"""
    Une caisse de $50\U{kg}$, au repos sur un sol horizontal, est tirée par une force horizontale de $200\U{N}$. Les frottements sont équivalents à une force constante de $50\U{N}$.

    1. Calculer l'accélération de la caisse.
    2. Calculer sa vitesse et la distance parcourue au bout de $4\U{s}$.
    """, r"""
    1. Système : la caisse. Référentiel terrestre supposé galiléen. Forces : $\vec P$, $\vec R$, $\vec F$, $\vec f$. TCI : $\vec P+\vec R+\vec F+\vec f=m\vec a$. Sur l'axe du mouvement : $F-f=ma$, donc $a=\dfrac{200-50}{50}=3\mss$.
    2. MRUV partant du repos : $v=3\times4=12\ms$ ; $d=\frac12\times3\times16=24\U{m}$.
    """),
    application=("le freinage d'urgence", r"""
    Une voiture de $1200\U{kg}$ roule à $20\ms$. Le conducteur freine : l'ensemble des forces de freinage équivaut à une force constante de $6000\U{N}$.

    1. Calculer la décélération.
    2. Calculer la distance d'arrêt.
    """, r"""
    1. TCI projeté sur l'axe du mouvement : $-f=ma$, donc $a=-\dfrac{6000}{1200}=-5\mss$.
    2. $0-20^2=2\times(-5)\times d$, donc $d=40\U{m}$.
    """),
    exos=[
        ("l'ascenseur qui démarre", r"""
        Un ascenseur de $500\U{kg}$ démarre vers le haut avec une accélération de $2\mss$. """ + G10 + r""" Calculer la tension du câble. La comparer au poids.
        """, r"""
        Axe vertical vers le haut : $T-mg=ma$, donc $T=m(g+a)=500\times12=6000\U{N}$. C'est plus que le poids ($5000\U{N}$) : il faut une force supplémentaire pour accélérer.
        """),
        ("sans frottement", r"""
        Un solide de $5\U{kg}$, au repos sur un plan horizontal sans frottement, est poussé par une force horizontale constante de $30\U{N}$. Calculer son accélération, puis sa vitesse et la distance parcourue après $2\U{s}$.
        """, r"""
        $a=\dfrac{F}{m}=6\mss$ ; $v=12\ms$ ; $d=\frac12\times6\times4=12\U{m}$.
        """),
    ],
)

B2 = dict(
    id="p2-b2", titre="Projeter sur deux axes : le plan incliné", duree=20,
    objectif="Projeter le TCI sur deux axes pour trouver l'accélération et la réaction sur un plan incliné.",
    cours=[
        retenir("Solide sur un plan incliné", r"""
        Plan incliné d'un angle $\alpha$ sur l'horizontale.

        Axe $(Ox)$ parallèle au plan, vers le bas ; axe $(Oy)$ perpendiculaire au plan.

        - Poids : $P_x=mg\sin\alpha$ et $P_y=-mg\cos\alpha$.
        - Sur $(Oy)$ : pas de mouvement, donc $R_N=mg\cos\alpha$.
        - Sur $(Ox)$ : $mg\sin\alpha-f=ma$, donc $a=g\sin\alpha-\dfrac{f}{m}$.
        - Sans frottement : $a=g\sin\alpha$, qui ne dépend pas de la masse.
        """),
        prof(r"""
        Le $\sin$ va avec l'axe parallèle au plan. Vérifie avec $\alpha=0$ (plan horizontal) : $a=0$ sans frottement, c'est logique.
        """),
    ],
    video=dict(id="p2-b2", titre="Le plan incliné", phrases=[
        ("Le plan incliné : projeter le théorème sur deux axes.", "Le plan incliné"),
        ("Un solide glisse sur un plan incliné d'un angle alpha. On prend un axe x parallèle au plan, vers le bas, et un axe y perpendiculaire au plan.", r"(Ox)\parallel\text{plan},\ (Oy)\perp\text{plan}"),
        ("Le poids se décompose : m g sinus alpha le long du plan, et moins m g cosinus alpha perpendiculairement.", r"P_x=mg\sin\alpha\qquad P_y=-mg\cos\alpha"),
        ("Sur l'axe y, le solide ne décolle pas et ne s'enfonce pas : l'accélération est nulle. Donc la réaction vaut m g cosinus alpha.", r"R_N=mg\cos\alpha"),
        ("Sur l'axe x, sans frottement : m g sinus alpha égale m a. Donc a égale g sinus alpha, quelle que soit la masse.", r"a=g\sin\alpha"),
        ("Exemple : alpha égale trente degrés, g égale dix. L'accélération vaut cinq mètres par seconde carrée.", r"a=10\times\sin30°=5\ \mathrm{m\cdot s^{-2}}"),
        ("Avec une force de frottement f, on la retire : a égale g sinus alpha, moins f sur m.", r"a=g\sin\alpha-\dfrac fm"),
        ("Le réflexe : vérifier avec alpha égale zéro. Sur un plan horizontal et sans frottement, a est nulle. La formule est cohérente.", r"\alpha=0\Rightarrow a=0"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("descente sans frottement", r"""
    Un solide de $2\U{kg}$ est lâché sans vitesse sur un plan incliné de $30°$, sans frottement. """ + G10 + r"""

    1. Calculer son accélération et la réaction du plan.
    2. Calculer sa vitesse après $2\U{m}$ de descente.
    """, r"""
    1. Système : le solide ; référentiel terrestre galiléen ; forces : $\vec P$ et $\vec R$. TCI : $\vec P+\vec R=m\vec a$. Sur $(Ox)$ : $mg\sin\alpha=ma$, donc $a=10\times0{,}5=5\mss$. Sur $(Oy)$ : $R=mg\cos\alpha=20\times0{,}866\approx17{,}3\U{N}$.
    2. $v^2=2ad=2\times5\times2=20$, donc $v\approx4{,}47\ms$.
    """),
    application=("avec frottement", r"""
    Même solide et même plan, mais une force de frottement constante $f=4\U{N}$ s'oppose au mouvement. Calculer l'accélération et la vitesse après $2\U{m}$.
    """, r"""
    Sur $(Ox)$ : $mg\sin\alpha-f=ma$, donc $a=5-\dfrac42=3\mss$. $v=\sqrt{2\times3\times2}=\sqrt{12}\approx3{,}46\ms$.
    """),
    exos=[
        ("la montée", r"""
        Un solide est lancé vers le haut d'un plan incliné de $30°$ (sans frottement) avec une vitesse de $6\ms$. """ + G10 + r""" Quelle distance parcourt-il avant de s'arrêter, et en combien de temps ?
        """, r"""
        Axe vers le haut du plan : $a=-g\sin\alpha=-5\mss$. $0-36=2\times(-5)\times d$, donc $d=3{,}6\U{m}$. $0=-5t+6$, donc $t=1{,}2\U{s}$.
        """),
        ("mesurer un frottement", r"""
        Un solide de $0{,}5\U{kg}$ glisse sur un plan incliné de $20°$. On mesure $a=2{,}4\mss$. """ + G10 + r""" Calculer la force de frottement.
        """, r"""
        $f=m(g\sin\alpha-a)=0{,}5\times(3{,}42-2{,}4)\approx0{,}51\U{N}$.
        """),
    ],
)

EVAL_B = dict(duree=45, exos=[
    dict(titre="Le plan incliné puis le plan horizontal", pts=10, enonce=r"""
    Un solide de masse $m=1\U{kg}$ part sans vitesse du sommet $A$ d'un plan incliné de $30°$, de longueur $AB=4\U{m}$. Sur tout le trajet, une force de frottement constante $f=2\U{N}$ s'oppose au mouvement. """ + G10 + r"""

    1. Appliquer le TCI sur $AB$ et calculer l'accélération $a_1$ ainsi que la réaction normale $R_N$.
    2. Calculer la vitesse en $B$ et la durée du trajet $AB$.
    3. Le solide aborde en $B$ un plan horizontal, avec le même frottement. Calculer sa nouvelle accélération et la distance parcourue avant l'arrêt.
    """, corr=r"""
    1. Forces : $\vec P$, $\vec R_N$, $\vec f$. Sur $(Ox)$ : $mg\sin\alpha-f=ma_1$, donc $a_1=5-2=3\mss$. Sur $(Oy)$ : $R_N=mg\cos\alpha\approx8{,}66\U{N}$. **(4 pts)**
    2. $v_B=\sqrt{2\times3\times4}=\sqrt{24}\approx4{,}90\ms$ ; $t=\dfrac{v_B}{a_1}\approx1{,}63\U{s}$. **(3 pts)**
    3. $-f=ma_2$, donc $a_2=-2\mss$. $0-24=2\times(-2)\times d$, donc $d=6\U{m}$. **(3 pts)**
    """),
    dict(titre="La luge tirée par une corde", pts=10, enonce=r"""
    Une luge de $20\U{kg}$ est tirée sur un sol horizontal par une corde inclinée de $30°$ au-dessus de l'horizontale. La tension vaut $T=100\U{N}$ et les frottements $f=50\U{N}$. """ + G10 + r"""

    1. Faire le bilan des forces et écrire le TCI.
    2. Projeter sur l'horizontale : calculer l'accélération.
    3. Projeter sur la verticale : calculer la réaction normale du sol. Pourquoi est-elle inférieure au poids ?
    4. Partie du repos, quelle vitesse la luge atteint-elle en $5\U{s}$ ?
    """, corr=r"""
    1. Forces : $\vec P$, $\vec R_N$, $\vec T$, $\vec f$. TCI : $\vec P+\vec R_N+\vec T+\vec f=m\vec a$. **(2 pts)**
    2. $T\cos30°-f=ma$, donc $a=\dfrac{86{,}6-50}{20}\approx1{,}83\mss$. **(3 pts)**
    3. $R_N+T\sin30°-mg=0$, donc $R_N=200-50=150\U{N}$. La corde tire aussi un peu vers le haut et soulage le sol. **(3 pts)**
    4. $v=1{,}83\times5\approx9{,}15\ms$. **(2 pts)**
    """),
])

PARTIE_A = dict(lettre="A", titre="Centre d'inertie et référentiels", etapes=[A1, A2], evaluation=EVAL_A)
PARTIE_B = dict(lettre="B", titre="Le théorème du centre d'inertie", etapes=[B1, B2], evaluation=EVAL_B)
