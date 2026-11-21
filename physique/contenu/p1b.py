# -*- coding: utf-8 -*-
"""P1 Cinématique du point : parties D (mouvement rectiligne sinusoïdal) et E (mouvements circulaires)."""
from build import retenir, prof, cours, soustitre

# =====================================================================
# PARTIE D — Mouvement rectiligne sinusoïdal
# =====================================================================
D1 = dict(
    id="p1-d1", titre="Équation horaire et phase à l'origine", duree=20,
    objectif="Reconnaître un mouvement rectiligne sinusoïdal, donner ses grandeurs caractéristiques et trouver la phase à l'origine.",
    cours=[
        retenir("Mouvement rectiligne sinusoïdal", r"""
        $$x(t)=X_m\cos(\omega t+\varphi)\qquad \ddot x+\omega^2x=0$$

        - $X_m>0$ : amplitude (m). Le mobile oscille entre $-X_m$ et $+X_m$ : le segment parcouru mesure $2X_m$.
        - $\omega$ : pulsation ($\mathrm{rad\cdot s^{-1}}$) ; période $T=\dfrac{2\pi}{\omega}$ (s) ; fréquence $N=\dfrac1T$ (Hz).
        - $\varphi$ : phase à l'origine (rad), fixée par l'état du mobile à $t=0$.
        """),
        cours(r"""
        [[simu:phase]]
        """),
        retenir("Trouver φ", r"""
        1. $x_0=X_m\cos\varphi$ donne $\cos\varphi$, donc deux valeurs opposées $\pm\alpha$.
        2. $v_0=-X_m\,\omega\sin\varphi$ : le **sens du mouvement** à $t=0$ choisit. Sens positif ($v_0>0$) : $\sin\varphi<0$. Sens négatif : $\sin\varphi>0$.
        """),
        prof(r"""
        Une phase est définie à $2\pi$ près : $-\frac{2\pi}{3}$ et $\frac{4\pi}{3}$ désignent le même mouvement. On choisit en général $\varphi\in\,]-\pi\,;\,\pi]$.
        """),
    ],
    video=dict(id="p1-d1", titre="Trouver la phase à l'origine", phrases=[
        ("Le mouvement rectiligne sinusoïdal : trouver la phase à l'origine.", "Mouvement rectiligne sinusoïdal"),
        ("L'équation horaire s'écrit x égale X m cosinus de oméga t plus phi. X m est l'amplitude, oméga la pulsation, phi la phase à l'origine.", r"x=X_m\cos(\omega t+\varphi)"),
        ("La pulsation se calcule avec la période : oméga égale deux pi sur T. Et l'équation différentielle est x seconde plus oméga carré x égale zéro.", r"\omega=\dfrac{2\pi}{T}\qquad \ddot x+\omega^2x=0"),
        ("Exemple : amplitude quatre centimètres, période zéro virgule cinq seconde. À t égale zéro, le mobile est à deux centimètres et va dans le sens négatif.", r"X_m=4\ \mathrm{cm},\ T=0{,}5\ \mathrm s"),
        ("D'abord oméga : deux pi sur zéro virgule cinq, soit quatre pi radians par seconde.", r"\omega=4\pi\ \mathrm{rad\cdot s^{-1}}"),
        ("Ensuite la position : deux égale quatre cosinus phi, donc cosinus phi égale un demi. Phi vaut pi sur trois, ou moins pi sur trois.", r"\cos\varphi=\tfrac12\ \Rightarrow\ \varphi=\pm\tfrac{\pi}{3}"),
        ("Enfin le sens : v zéro égale moins X m oméga sinus phi. Le mobile va dans le sens négatif, donc v zéro est négatif, et sinus phi est positif. On garde pi sur trois.", r"v_0<0\Rightarrow\sin\varphi>0\Rightarrow\varphi=\tfrac{\pi}{3}"),
        ("Résultat : x égale quatre cosinus de quatre pi t plus pi sur trois, en centimètres. Sans le sens du mouvement, on ne peut pas conclure.", r"x=4\cos\!\left(4\pi t+\tfrac{\pi}{3}\right)\ \mathrm{cm}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("phase positive", r"""
    Un mobile a un mouvement rectiligne sinusoïdal d'amplitude $X_m=4\U{cm}$ et de période $T=0{,}5\U{s}$. À $t=0$, il passe à l'abscisse $x_0=2\U{cm}$ en allant dans le sens négatif. Écrire son équation horaire.
    """, r"""
    $\omega=\dfrac{2\pi}{T}=4\pi\U{rad\cdot s^{-1}}$.

    $x_0=X_m\cos\varphi$ : $\cos\varphi=\dfrac24=\dfrac12$, donc $\varphi=\pm\dfrac{\pi}{3}$.

    Sens négatif : $v_0=-X_m\,\omega\sin\varphi<0$, donc $\sin\varphi>0$ : $\varphi=\dfrac{\pi}{3}$.

    $x(t)=4\cos\left(4\pi t+\dfrac{\pi}{3}\right)$ ($x$ en cm, $t$ en s).
    """),
    application=("départ au centre", r"""
    Amplitude $5\U{cm}$, période $0{,}2\U{s}$. À $t=0$, le mobile passe par le centre $O$ dans le sens positif. Écrire $x(t)$.
    """, r"""
    $\omega=\dfrac{2\pi}{0{,}2}=10\pi\U{rad\cdot s^{-1}}$. $x_0=0$ : $\cos\varphi=0$, $\varphi=\pm\dfrac{\pi}{2}$. Sens positif : $\sin\varphi<0$, donc $\varphi=-\dfrac{\pi}{2}$.

    $x(t)=5\cos\left(10\pi t-\dfrac{\pi}{2}\right)$ (cm).
    """),
    exos=[
        ("à partir de l'équation différentielle", r"""
        Un mobile vérifie $\ddot x+400\,x=0$ (SI). Son amplitude est $3\U{cm}$ et, à $t=0$, il est en $x_0=-3\U{cm}$.

        1. Calculer $\omega$, $T$ et $N$.
        2. Déterminer $\varphi$ et écrire $x(t)$.
        """, r"""
        1. $\omega^2=400$ donc $\omega=20\U{rad\cdot s^{-1}}$ ; $T=\dfrac{2\pi}{20}=\dfrac{\pi}{10}\approx0{,}314\U{s}$ ; $N\approx3{,}18\U{Hz}$.
        2. $\cos\varphi=-1$ donc $\varphi=\pi$ (le mobile est à une extrémité, sa vitesse est nulle). $x=3\cos(20t+\pi)$ (cm).
        """),
        ("lire une équation horaire", r"""
        $x(t)=0{,}02\cos\left(50t+\dfrac{\pi}{6}\right)$ (SI).

        1. Donner $X_m$, $\omega$, $T$ et la longueur du segment parcouru.
        2. Calculer $x$ et $v$ à $t=0$. Dans quel sens part le mobile ?
        """, r"""
        1. $X_m=2\U{cm}$, $\omega=50\U{rad\cdot s^{-1}}$, $T=\dfrac{2\pi}{50}\approx0{,}126\U{s}$, segment de $4\U{cm}$.
        2. $x_0=0{,}02\cos\frac{\pi}{6}\approx1{,}73\U{cm}$. $v=-0{,}02\times50\sin(50t+\frac{\pi}{6})$, donc $v_0=-1\times\frac12=-0{,}5\ms$ : il part dans le **sens négatif**.
        """),
    ],
)

D2 = dict(
    id="p1-d2", titre="Vitesse, dates de passage et relation v² = f(x²)", duree=20,
    objectif="Exprimer la vitesse, calculer une date de passage et utiliser la relation entre vitesse et élongation.",
    cours=[
        retenir("Vitesse et accélération", r"""
        $$v=-X_m\,\omega\sin(\omega t+\varphi)\qquad a=-\omega^2x\qquad v^2=\omega^2\,(X_m^2-x^2)$$

        - $v_{\max}=X_m\,\omega$, atteinte au centre ($x=0$) ; $v=0$ aux extrémités.
        - La courbe $v^2=f(x^2)$ est une droite de pente $-\omega^2$ et d'ordonnée à l'origine $\omega^2X_m^2$.
        """),
        retenir("Date de passage en un point avec un sens donné", r"""
        1. Écrire $\cos(\omega t+\varphi)=\dfrac{x}{X_m}$ : deux angles $\pm\alpha$ à $2k\pi$ près.
        2. Sens positif : $\sin(\omega t+\varphi)<0$ ; sens négatif : $\sin>0$. On garde un seul angle.
        3. Résoudre en $t$, puis choisir $k$ pour obtenir le premier, le deuxième… passage (avec $t\geq0$).
        """),
        prof(r"""
        Les passages au même point et dans le même sens sont espacés d'une période $T$.
        """),
    ],
    video=dict(id="p1-d2", titre="Dates de passage et vitesse", phrases=[
        ("Mouvement sinusoïdal : vitesse et dates de passage.", "Vitesse et dates de passage"),
        ("On dérive l'équation horaire : v égale moins X m oméga sinus de oméga t plus phi. La vitesse maximale vaut X m oméga, au centre.", r"v=-X_m\omega\sin(\omega t+\varphi)"),
        ("Reprenons x égale quatre cosinus de quatre pi t plus pi sur trois, en centimètres. La vitesse maximale vaut zéro virgule zéro quatre fois quatre pi, environ zéro virgule cinq mètre par seconde.", r"v_{\max}=0{,}04\times4\pi\approx0{,}50\ \mathrm{m\cdot s^{-1}}"),
        ("Question type : à quelle date le mobile passe-t-il pour la première fois à moins deux centimètres, dans le sens négatif ?", r"x=-2\ \mathrm{cm},\ v<0"),
        ("Cosinus de l'angle égale moins un demi : l'angle vaut deux pi sur trois, ou moins deux pi sur trois.", r"\cos\theta=-\tfrac12"),
        ("Sens négatif : le sinus doit être positif. On garde deux pi sur trois, plus deux k pi.", r"\theta=\tfrac{2\pi}{3}+2k\pi"),
        ("Quatre pi t plus pi sur trois égale deux pi sur trois plus deux k pi. Donc t égale un douzième plus k demis. Le premier passage, pour k égale zéro, a lieu à un douzième de seconde.", r"t=\tfrac{1}{12}+\tfrac{k}{2}\ \mathrm s"),
        ("Dernier outil : v carré égale oméga carré, facteur de X m carré moins x carré. Il donne la vitesse en un point sans passer par le temps.", r"v^2=\omega^2(X_m^2-x^2)"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("premier passage", r"""
    $x(t)=4\cos\left(4\pi t+\dfrac{\pi}{3}\right)$ ($x$ en cm, $t$ en s).

    1. Calculer la vitesse maximale.
    2. À quelle date le mobile passe-t-il pour la première fois en $x=-2\U{cm}$ dans le sens négatif ?
    3. Calculer la valeur de la vitesse en $x=2\U{cm}$.
    """, r"""
    1. $v_{\max}=X_m\,\omega=0{,}04\times4\pi\approx0{,}503\ms$.
    2. $\cos(4\pi t+\frac{\pi}{3})=-\frac12$ et $\sin>0$ (sens négatif) : $4\pi t+\frac{\pi}{3}=\frac{2\pi}{3}+2k\pi$, donc $t=\dfrac{1}{12}+\dfrac{k}{2}$. Premier passage ($k=0$) : $t=\dfrac{1}{12}\approx0{,}083\U{s}$.
    3. $|v|=\omega\sqrt{X_m^2-x^2}=4\pi\sqrt{16-4}\approx43{,}5\U{cm\cdot s^{-1}}=0{,}435\ms$.
    """),
    application=("à une extrémité", r"""
    $x(t)=5\cos\left(10\pi t-\dfrac{\pi}{2}\right)$ (cm, s).

    1. Calculer $v$ à $t=0$.
    2. À quelle date le mobile atteint-il pour la première fois l'extrémité $x=+5\U{cm}$ ?
    3. Calculer la valeur de la vitesse en $x=3\U{cm}$.
    """, r"""
    1. $v=-0{,}05\times10\pi\sin(10\pi t-\frac{\pi}{2})$ ; $v_0=+0{,}5\pi\approx1{,}57\ms$.
    2. $\cos(10\pi t-\frac{\pi}{2})=1\iff10\pi t-\frac{\pi}{2}=2k\pi\iff t=\dfrac{1}{20}+\dfrac{k}{5}$. Premier : $t=0{,}05\U{s}=\frac{T}{4}$.
    3. $|v|=10\pi\sqrt{25-9}=40\pi\U{cm\cdot s^{-1}}\approx1{,}26\ms$.
    """),
    exos=[
        ("à partir de la courbe x(t)", r"""
        La courbe ci-dessous donne l'élongation $x(t)$ d'un mobile en mouvement rectiligne sinusoïdal.

        [[graphe:p1-d2-x]]

        1. Déterminer $X_m$, $T$ et $\omega$.
        2. Déterminer $\varphi$ et écrire $x(t)$.
        """, r"""
        1. $X_m=2\U{cm}$. Du départ au retour au même état, il faut $0{,}4\U{s}$ : $T=0{,}4\U{s}$, $\omega=5\pi\U{rad\cdot s^{-1}}$.
        2. $x_0=0$ et la courbe monte ($v_0>0$) : $\varphi=-\dfrac{\pi}{2}$. $x=2\cos\left(5\pi t-\dfrac{\pi}{2}\right)$ (cm).
        """),
        ("la droite v² = f(x²)", r"""
        Pour un mobile en mouvement rectiligne sinusoïdal, on a établi $v^2=0{,}25-25\,x^2$ (SI).

        1. Justifier l'allure de la courbe $v^2=f(x^2)$.
        2. En déduire $\omega$ et $X_m$.
        """, r"""
        1. $v^2=-\omega^2x^2+\omega^2X_m^2$ est une fonction affine de $x^2$ : droite décroissante.
        2. Pente : $\omega^2=25$, donc $\omega=5\U{rad\cdot s^{-1}}$. Ordonnée à l'origine : $\omega^2X_m^2=0{,}25$, donc $X_m^2=0{,}01$ et $X_m=0{,}1\U{m}$.
        """),
    ],
)

EVAL_D = dict(duree=40, exos=[
    dict(titre="Équation horaire et tableau de valeurs", pts=10, enonce=r"""
    Un mobile vérifie l'équation différentielle $\ddot x+25\pi^2x=0$ (SI). Son amplitude vaut $X_m=3\U{cm}$. À $t=0$, il passe en $x_0=1{,}5\U{cm}$ en allant dans le sens positif.

    1. Quelle est la nature du mouvement ? Calculer $\omega$ et $T$.
    2. Déterminer $\varphi$ et écrire $x(t)$.
    3. Compléter le tableau : $x$ aux dates $0$, $T/4$, $T/2$, $3T/4$, $T$. Quelle distance le mobile parcourt-il en une période ?
    4. Calculer $v_0$ et $v_{\max}$.
    """, corr=r"""
    1. Équation de la forme $\ddot x+\omega^2x=0$ : mouvement **rectiligne sinusoïdal**. $\omega=5\pi\U{rad\cdot s^{-1}}$, $T=0{,}4\U{s}$. **(2 pts)**
    2. $\cos\varphi=\frac12$ et sens positif ($\sin\varphi<0$) : $\varphi=-\dfrac{\pi}{3}$. $x=3\cos\left(5\pi t-\dfrac{\pi}{3}\right)$ (cm). **(3 pts)**
    3. **(3 pts)**

    | $t$ (s) | 0 | 0,1 | 0,2 | 0,3 | 0,4 |
    | $x$ (cm) | 1,5 | 2,6 | $-1{,}5$ | $-2{,}6$ | 1,5 |

    En une période : $4X_m=12\U{cm}$.

    4. $v_0=-0{,}03\times5\pi\sin(-\frac{\pi}{3})\approx0{,}408\ms$ ; $v_{\max}=0{,}15\pi\approx0{,}471\ms$. **(2 pts)**
    """),
    dict(titre="Dates de passage", pts=10, enonce=r"""
    On reprend le mobile précédent : $x(t)=3\cos\left(5\pi t-\dfrac{\pi}{3}\right)$ ($x$ en cm, $t$ en s). Sa courbe est donnée ci-dessous.

    [[graphe:p1-evd-x]]

    1. Déterminer les dates des deux premiers passages en $x=-1{,}5\U{cm}$ dans le sens positif.
    2. Calculer la valeur de la vitesse en ce point, de deux façons.
    3. Calculer l'accélération en ce point. Vers où est-elle dirigée ?
    """, corr=r"""
    1. $\cos\theta=-\frac12$ avec $\sin\theta<0$ (sens positif) : $\theta=-\dfrac{2\pi}{3}+2k\pi$. $5\pi t-\frac{\pi}{3}=-\frac{2\pi}{3}+2k\pi$, donc $t=-\dfrac{1}{15}+0{,}4k$. Avec $t\geq0$ : $k=1$, $t_1=\dfrac13\approx0{,}333\U{s}$ ; $k=2$, $t_2\approx0{,}733\U{s}$. **(5 pts)**
    2. $|v|=\omega\sqrt{X_m^2-x^2}=5\pi\sqrt{9-2{,}25}\approx40{,}8\U{cm\cdot s^{-1}}$. Ou $v(t_1)=-0{,}15\pi\sin(-\frac{2\pi}{3})\approx0{,}408\ms$. **(3 pts)**
    3. $a=-\omega^2x=25\pi^2\times0{,}015\approx3{,}70\mss$ : positive, dirigée vers le centre $O$. **(2 pts)**
    """),
])

# =====================================================================
# PARTIE E — Mouvements circulaires
# =====================================================================
E1 = dict(
    id="p1-e1", titre="Le mouvement circulaire uniforme", duree=15,
    objectif="Utiliser l'abscisse angulaire, la vitesse angulaire, la période et l'accélération centripète d'un MCU.",
    cours=[
        retenir("Mouvement circulaire uniforme (MCU)", r"""
        Sur un cercle de rayon $R$, la position est repérée par l'abscisse angulaire $\theta$ (rad) ou l'abscisse curviligne $s=R\,\theta$ (m).

        $$\theta(t)=\omega\,t+\theta_0\qquad v=R\,\omega\qquad T=\frac{2\pi}{\omega}\qquad a=a_n=\frac{v^2}{R}=R\,\omega^2$$

        - $\omega$ : vitesse angulaire ($\mathrm{rad\cdot s^{-1}}$), constante.
        - $a_t=0$ : l'accélération est **centripète** (dirigée vers le centre).
        """),
        prof(r"""
        Une fréquence en tours par seconde se convertit ainsi : $\omega=2\pi N$. Pour des tours par minute, divise d'abord par 60.
        """),
    ],
    video=dict(id="p1-e1", titre="Le mouvement circulaire uniforme", phrases=[
        ("Le mouvement circulaire uniforme.", "Mouvement circulaire uniforme"),
        ("Sur un cercle, on repère le mobile par un angle, l'abscisse angulaire thêta, en radians. L'arc parcouru vaut R thêta.", r"s=R\,\theta"),
        ("Dans un mouvement circulaire uniforme, thêta augmente régulièrement : thêta égale oméga t plus thêta zéro. Oméga est la vitesse angulaire.", r"\theta=\omega t+\theta_0"),
        ("La vitesse vaut R oméga, et la période deux pi sur oméga.", r"v=R\omega\qquad T=\dfrac{2\pi}{\omega}"),
        ("La vitesse est constante en valeur, mais pas en direction. Il y a donc une accélération, dirigée vers le centre : v carré sur R.", r"a=\dfrac{v^2}{R}=R\omega^2"),
        ("Exemple : l'extrémité d'une pale de ventilateur, à trente centimètres de l'axe, fait trois tours par seconde.", r"R=0{,}30\ \mathrm m,\ N=3\ \mathrm{tr/s}"),
        ("Oméga égale deux pi N, soit six pi, environ dix-huit virgule neuf radians par seconde. La vitesse vaut R oméga, environ cinq virgule sept mètres par seconde.", r"\omega=6\pi\ \mathrm{rad/s},\ v\approx5{,}65\ \mathrm{m/s}"),
        ("L'accélération vaut R oméga carré, environ cent sept mètres par seconde carrée. Plus de dix fois l'accélération de la pesanteur !", r"a=R\omega^2\approx107\ \mathrm{m\cdot s^{-2}}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("une pale de ventilateur", r"""
    L'extrémité d'une pale de ventilateur est à $R=30\U{cm}$ de l'axe et tourne à $3\U{tours/s}$ (mouvement uniforme). Calculer $\omega$, $T$, $v$ et $a$.
    """, r"""
    $\omega=2\pi N=6\pi\approx18{,}9\U{rad\cdot s^{-1}}$ ; $T=\dfrac13\approx0{,}333\U{s}$ ; $v=R\omega=0{,}30\times6\pi\approx5{,}65\ms$ ; $a=R\omega^2=0{,}30\times36\pi^2\approx107\mss$, dirigée vers l'axe.
    """),
    application=("un rond-point", r"""
    Une voiture parcourt un rond-point de rayon $R=20\U{m}$ à $36\U{km/h}$ constante. Calculer $\omega$, la durée d'un tour et l'accélération.
    """, r"""
    $v=10\ms$ ; $\omega=\dfrac{v}{R}=0{,}5\U{rad\cdot s^{-1}}$ ; $T=\dfrac{2\pi}{0{,}5}=4\pi\approx12{,}6\U{s}$ ; $a=\dfrac{v^2}{R}=5\mss$.
    """),
    exos=[
        ("un point de l'équateur", r"""
        La Terre fait un tour sur elle-même en $24\U{h}$ (on prend cette valeur). Le rayon terrestre vaut $6400\U{km}$. Pour un point de l'équateur, calculer $\omega$, $v$ et $a$.
        """, r"""
        $\omega=\dfrac{2\pi}{86\,400}\approx7{,}27\times10^{-5}\U{rad\cdot s^{-1}}$ ; $v=R\omega\approx465\ms$ ; $a=R\omega^2\approx3{,}4\times10^{-2}\mss$.
        """),
        ("une loi horaire angulaire", r"""
        Un point décrit un cercle de rayon $0{,}5\U{m}$ avec $\theta(t)=2t+\dfrac{\pi}{4}$ (SI).

        1. Calculer $\omega$ et $v$.
        2. Quel angle et quelle longueur d'arc le point parcourt-il en $3\U{s}$ ? Combien de tours cela fait-il ?
        """, r"""
        1. $\omega=2\U{rad\cdot s^{-1}}$ ; $v=0{,}5\times2=1\ms$.
        2. $\Delta\theta=6\U{rad}$ ; arc $=R\,\Delta\theta=3\U{m}$ ; $\dfrac{6}{2\pi}\approx0{,}95$ tour.
        """),
    ],
)

E2 = dict(
    id="p1-e2", titre="Le mouvement circulaire uniformément varié", duree=20,
    objectif="Utiliser les relations du MCUV et calculer les accélérations tangentielle et normale d'un point.",
    cours=[
        retenir("Mouvement circulaire uniformément varié (MCUV)", r"""
        L'accélération angulaire $\ddot\theta$ ($\mathrm{rad\cdot s^{-2}}$) est constante :

        $$\dot\theta=\ddot\theta\,t+\omega_0\qquad \theta=\frac12\,\ddot\theta\,t^2+\omega_0\,t+\theta_0\qquad \dot\theta^{\,2}-\omega_0^2=2\,\ddot\theta\,(\theta-\theta_0)$$

        - Pour un point à la distance $R$ de l'axe : $v=R\,\dot\theta$, $a_t=R\,\ddot\theta$, $a_n=R\,\dot\theta^{\,2}$.
        - Ce sont les relations du MRUV où $x$ devient $\theta$, $v$ devient $\dot\theta$ et $a$ devient $\ddot\theta$.
        """),
        prof(r"""
        Un nombre de tours $n$ correspond à l'angle $\theta=2\pi n$ radians. Convertis toujours en radians avant d'utiliser les formules.
        """),
    ],
    video=dict(id="p1-e2", titre="Le mouvement circulaire uniformément varié", phrases=[
        ("Le mouvement circulaire uniformément varié.", "MCUV"),
        ("Dans ce mouvement, l'accélération angulaire, thêta seconde, est constante. Les formules sont celles du MRUV, avec des angles.", r"\ddot\theta=\text{constante}"),
        ("Vitesse angulaire : thêta point égale thêta seconde t plus oméga zéro. Angle : un demi thêta seconde t carré, plus oméga zéro t, plus thêta zéro.", r"\dot\theta=\ddot\theta t+\omega_0"),
        ("Et la relation sans le temps : thêta point carré moins oméga zéro carré égale deux thêta seconde, facteur de l'angle parcouru.", r"\dot\theta^2-\omega_0^2=2\ddot\theta\,\Delta\theta"),
        ("Exemple : un disque part du repos et atteint dix radians par seconde en cinq secondes. Son accélération angulaire vaut deux radians par seconde carrée.", r"\ddot\theta=\dfrac{10}{5}=2\ \mathrm{rad\cdot s^{-2}}"),
        ("Angle parcouru : un demi fois deux fois vingt-cinq, soit vingt-cinq radians. Divisé par deux pi, cela fait environ quatre tours.", r"\theta=25\ \mathrm{rad}\approx4\ \text{tours}"),
        ("Pour un point à dix centimètres de l'axe, à cinq secondes : a t égale R thêta seconde, zéro virgule deux. Et a n égale R thêta point carré, dix mètres par seconde carrée.", r"a_t=R\ddot\theta\qquad a_n=R\dot\theta^2"),
        ("Le réflexe : un tour égale deux pi radians. Convertis les tours avant de calculer.", r"1\ \text{tour}=2\pi\ \mathrm{rad}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("un disque qui démarre", r"""
    Un disque part du repos et atteint $10\U{rad\cdot s^{-1}}$ en $5\U{s}$, d'un mouvement uniformément accéléré.

    1. Calculer $\ddot\theta$ et le nombre de tours effectués pendant ces $5\U{s}$.
    2. Pour un point situé à $R=10\U{cm}$ de l'axe, calculer $a_t$ et $a_n$ à $t=5\U{s}$.
    """, r"""
    1. $\ddot\theta=\dfrac{10-0}{5}=2\U{rad\cdot s^{-2}}$. $\theta=\frac12\times2\times25=25\U{rad}$, soit $\dfrac{25}{2\pi}\approx3{,}98$ tours.
    2. $a_t=R\ddot\theta=0{,}1\times2=0{,}2\mss$ ; $a_n=R\dot\theta^{\,2}=0{,}1\times100=10\mss$.
    """),
    application=("un freinage", r"""
    Une roue tourne à $\omega_0=20\U{rad\cdot s^{-1}}$. Freinée uniformément, elle s'arrête après $10$ tours. Calculer $\ddot\theta$ et la durée du freinage.
    """, r"""
    $\theta=10\times2\pi=20\pi\U{rad}$. $0-20^2=2\,\ddot\theta\times20\pi$, donc $\ddot\theta=-\dfrac{10}{\pi}\approx-3{,}18\U{rad\cdot s^{-2}}$. Durée : $0=-\frac{10}{\pi}t+20$, donc $t=2\pi\approx6{,}28\U{s}$.
    """),
    exos=[
        ("une loi horaire", r"""
        $\theta(t)=0{,}5\,t^2+2t$ (rad, s) pour un point à $R=0{,}2\U{m}$ de l'axe.

        1. Donner $\ddot\theta$ et $\dot\theta(t)$.
        2. À $t=4\U{s}$, calculer $v$, $a_t$ et $a_n$.
        """, r"""
        1. $\ddot\theta=1\U{rad\cdot s^{-2}}$ ; $\dot\theta=t+2$.
        2. $\dot\theta(4)=6\U{rad\cdot s^{-1}}$ ; $v=1{,}2\ms$ ; $a_t=0{,}2\mss$ ; $a_n=0{,}2\times36=7{,}2\mss$.
        """),
        ("un moteur", r"""
        Un moteur passe de $1200\U{tr/min}$ à $3000\U{tr/min}$ en $6\U{s}$, d'un mouvement uniformément varié. Calculer l'accélération angulaire et le nombre de tours effectués.
        """, r"""
        $\omega_0=\dfrac{1200\times2\pi}{60}=40\pi$ et $\omega=100\pi\U{rad\cdot s^{-1}}$. $\ddot\theta=\dfrac{60\pi}{6}=10\pi\approx31{,}4\U{rad\cdot s^{-2}}$. $\theta=\dfrac{\omega^2-\omega_0^2}{2\ddot\theta}=\dfrac{8400\pi^2}{20\pi}=420\pi\U{rad}$, soit $210$ tours.
        """),
    ],
)

EVAL_E = dict(duree=40, exos=[
    dict(titre="Un disque vinyle", pts=8, enonce=r"""
    Un disque tourne à $45\U{tr/min}$ d'un mouvement uniforme. On étudie un point $M$ situé à $12\U{cm}$ de l'axe.

    1. Calculer la vitesse angulaire et la période.
    2. Calculer la vitesse et l'accélération de $M$. Préciser la direction de l'accélération.
    3. Combien de temps faut-il pour faire 10 tours ?
    """, corr=r"""
    1. $\omega=\dfrac{45\times2\pi}{60}=1{,}5\pi\approx4{,}71\U{rad\cdot s^{-1}}$ ; $T=\dfrac{2\pi}{\omega}\approx1{,}33\U{s}$. **(3 pts)**
    2. $v=R\omega=0{,}12\times4{,}71\approx0{,}565\ms$ ; $a=R\omega^2\approx2{,}66\mss$, dirigée vers le centre. **(3 pts)**
    3. $10T\approx13{,}3\U{s}$. **(2 pts)**
    """),
    dict(titre="La meule", pts=12, enonce=r"""
    Une meule de rayon $10\U{cm}$, initialement au repos, est mise en rotation avec une accélération angulaire constante $\ddot\theta_1=5\U{rad\cdot s^{-2}}$ pendant $8\U{s}$.

    1. Calculer la vitesse angulaire atteinte à $t=8\U{s}$ et le nombre de tours effectués pendant cette phase.
    2. À $t=8\U{s}$, calculer pour un point de la périphérie : $v$, $a_t$ et $a_n$.
    3. On coupe le moteur : la meule s'arrête après 50 tours, d'un mouvement uniformément retardé. Calculer l'accélération angulaire de freinage et la durée du freinage.
    """, corr=r"""
    1. $\dot\theta=5\times8=40\U{rad\cdot s^{-1}}$. $\theta=\frac12\times5\times64=160\U{rad}$, soit $\approx25{,}5$ tours. **(4 pts)**
    2. $v=0{,}1\times40=4\ms$ ; $a_t=0{,}1\times5=0{,}5\mss$ ; $a_n=0{,}1\times1600=160\mss$. **(4 pts)**
    3. $\theta=100\pi\U{rad}$ ; $0-40^2=2\,\ddot\theta_2\times100\pi$, donc $\ddot\theta_2=-\dfrac{8}{\pi}\approx-2{,}55\U{rad\cdot s^{-2}}$. Durée : $t=\dfrac{40}{8/\pi}=5\pi\approx15{,}7\U{s}$. **(4 pts)**
    """),
])

PARTIE_D = dict(lettre="D", titre="Le mouvement rectiligne sinusoïdal", etapes=[D1, D2], evaluation=EVAL_D)
PARTIE_E = dict(lettre="E", titre="Les mouvements circulaires", etapes=[E1, E2], evaluation=EVAL_E)
