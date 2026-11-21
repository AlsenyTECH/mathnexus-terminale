# -*- coding: utf-8 -*-
"""P2 Bases de la dynamique : parties C (théorèmes énergétiques) et D (conservation de la quantité de mouvement)."""
from build import retenir, prof, cours, soustitre

G10 = r"On prend $g=10\mss$."

# =====================================================================
# PARTIE C — Théorèmes relatifs aux énergies
# =====================================================================
C1 = dict(
    id="p2-c1", titre="Travail et théorème de l'énergie cinétique", duree=20,
    objectif="Calculer le travail d'une force constante et appliquer le théorème de l'énergie cinétique.",
    cours=[
        retenir("Travail d'une force constante", r"""
        $$W_{AB}(\vec F)=\vec F\cdot\vect{AB}=F\times AB\times\cos\theta\quad(\mathrm J)$$

        - Travail **moteur** ($W>0$) si $\theta<90°$, **résistant** ($W<0$) si $\theta>90°$, nul si la force est perpendiculaire au déplacement (réaction sans frottement).
        - Poids : $W(\vec P)=mgh$ quand le solide descend d'une hauteur $h$, $-mgh$ quand il monte.
        - Frottement constant opposé au mouvement : $W(\vec f)=-f\times\ell$.
        """),
        retenir("Théorème de l'énergie cinétique (TEC)", r"""
        $$E_c=\frac12\,m\,v^2\qquad E_c(B)-E_c(A)=\sum W_{AB}(\vec F_{\text{ext}})$$
        """),
        prof(r"""
        Le TEC donne une vitesse sans passer par le temps ni par l'accélération : c'est souvent le chemin le plus court.
        """),
    ],
    video=dict(id="p2-c1", titre="Le théorème de l'énergie cinétique", phrases=[
        ("Le travail d'une force, et le théorème de l'énergie cinétique.", "Théorème de l'énergie cinétique"),
        ("Le travail d'une force constante sur un déplacement A B est le produit scalaire de la force par le vecteur A B : F fois A B fois cosinus thêta.", r"W=F\times AB\times\cos\theta"),
        ("Une force perpendiculaire au déplacement ne travaille pas. Une force opposée au mouvement a un travail négatif : il est résistant.", r"W(\vec R)=0\qquad W(\vec f)=-f\,\ell"),
        ("Le théorème : la variation d'énergie cinétique entre A et B égale la somme des travaux des forces extérieures.", r"E_c(B)-E_c(A)=\sum W"),
        ("Exemple : un solide de deux kilogrammes part du repos et descend de deux mètres sur un plan incliné de trente degrés, sans frottement.", r"m=2\ \mathrm{kg},\ AB=2\ \mathrm m,\ \alpha=30°"),
        ("Le poids travaille : m g fois la hauteur descendue, A B sinus alpha, soit un mètre. Cela fait vingt joules. La réaction ne travaille pas.", r"W(\vec P)=mg\,AB\sin\alpha=20\ \mathrm J"),
        ("Un demi m v B carré moins zéro égale vingt joules. Donc v B carré égale vingt, et v B vaut environ quatre virgule quarante-sept mètres par seconde.", r"v_B=\sqrt{20}\approx4{,}47\ \mathrm{m\cdot s^{-1}}"),
        ("C'est le même résultat qu'avec le théorème du centre d'inertie, mais en deux lignes.", r"\text{même résultat, plus vite}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("le plan incliné, version énergie", r"""
    Un solide de $2\U{kg}$ part du repos en $A$ et descend $AB=2\U{m}$ sur un plan incliné de $30°$, sans frottement. """ + G10 + r""" Calculer sa vitesse en $B$ avec le TEC.
    """, r"""
    Système : le solide ; référentiel terrestre galiléen ; forces : $\vec P$ et $\vec R$.

    $W(\vec R)=0$ (perpendiculaire au déplacement) ; $W(\vec P)=mg\,AB\sin30°=2\times10\times2\times0{,}5=20\U{J}$.

    TEC : $\frac12mv_B^2-0=20$, donc $v_B=\sqrt{20}\approx4{,}47\ms$ (même résultat qu'avec le TCI).
    """),
    application=("avec frottement", r"""
    Même situation, mais une force de frottement constante $f=4\U{N}$ s'oppose au mouvement. Calculer $v_B$.
    """, r"""
    $W(\vec f)=-4\times2=-8\U{J}$. TEC : $\frac12\times2\times v_B^2=20-8=12$, donc $v_B=\sqrt{12}\approx3{,}46\ms$.
    """),
    exos=[
        ("la distance de freinage", r"""
        Une voiture de $1000\U{kg}$ roulant à $20\ms$ freine jusqu'à l'arrêt. La force de freinage, constante, vaut $8000\U{N}$.

        1. Calculer le travail de la force de freinage.
        2. En déduire la distance de freinage.
        """, r"""
        1. TEC : $0-\frac12\times1000\times400=W(\vec f)$, donc $W(\vec f)=-2\times10^5\U{J}$ ($\vec P$ et $\vec R$ ne travaillent pas).
        2. $-f\,d=-2\times10^5$, donc $d=25\U{m}$.
        """),
        ("la chute libre", r"""
        Une pierre est lâchée sans vitesse d'une hauteur de $20\U{m}$. On néglige l'air. """ + G10 + r""" Avec quelle vitesse touche-t-elle le sol ?
        """, r"""
        TEC : $\frac12mv^2=mgh$, donc $v=\sqrt{2gh}=\sqrt{400}=20\ms$.
        """),
    ],
)

C2 = dict(
    id="p2-c2", titre="Énergie potentielle et énergie mécanique", duree=20,
    objectif="Calculer une énergie mécanique, utiliser sa conservation et interpréter sa diminution par les frottements.",
    cours=[
        retenir("Énergie potentielle de pesanteur et énergie mécanique", r"""
        Axe vertical $(Oz)$ orienté vers le haut ; origine choisie comme référence ($E_p=0$ en $z=0$) :

        $$E_p=m\,g\,z\qquad E_m=E_c+E_p=\frac12mv^2+mgz$$

        - Sans frottement, l'énergie mécanique se **conserve** : $E_m(A)=E_m(B)$.
        - Avec frottements, elle diminue : $E_m(B)-E_m(A)=W(\vec f)<0$. L'énergie perdue devient de la chaleur.
        """),
        prof(r"""
        Écris toujours ta référence : « on prend $E_p=0$ au sol ». Sans elle, les valeurs de $E_p$ n'ont pas de sens.
        """),
    ],
    video=dict(id="p2-c2", titre="Conservation de l'énergie mécanique", phrases=[
        ("Énergie potentielle et énergie mécanique.", "Énergie mécanique"),
        ("L'énergie potentielle de pesanteur vaut m g z, avec un axe vertical orienté vers le haut. Il faut toujours dire où se trouve la référence, là où elle est nulle.", r"E_p=mgz"),
        ("L'énergie mécanique est la somme de l'énergie cinétique et de l'énergie potentielle.", r"E_m=\tfrac12mv^2+mgz"),
        ("Sans frottement, elle se conserve. Exemple : on lance une balle vers le haut à dix mètres par seconde, depuis le niveau de référence.", r"v_0=10\ \mathrm{m\cdot s^{-1}},\ z_0=0"),
        ("Au départ, toute l'énergie est cinétique. Au sommet, la vitesse est nulle : toute l'énergie est potentielle.", r"\tfrac12mv_0^2=mgz_{\max}"),
        ("Les m se simplifient : z max égale v zéro carré sur deux g, soit cent sur vingt, cinq mètres.", r"z_{\max}=\dfrac{v_0^2}{2g}=5\ \mathrm m"),
        ("Avec des frottements, l'énergie mécanique diminue. La perte est égale au travail des frottements.", r"\Delta E_m=W(\vec f)<0"),
        ("Le réflexe : comparer l'énergie mécanique au départ et à l'arrivée. Si elle a baissé, il y a des frottements.", r"E_m(B)<E_m(A)\Rightarrow\text{frottements}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("la balle lancée vers le haut", r"""
    Une balle est lancée verticalement vers le haut à $10\ms$ depuis le sol (référence de l'énergie potentielle). On néglige l'air. """ + G10 + r""" Calculer la hauteur maximale atteinte.
    """, r"""
    Sans frottement, $E_m$ se conserve entre le départ ($z=0$, $v=10\ms$) et le sommet ($v=0$) : $\frac12mv_0^2=mgz_{\max}$, donc $z_{\max}=\dfrac{v_0^2}{2g}=\dfrac{100}{20}=5\U{m}$.
    """),
    application=("le skateur", r"""
    Un skateur de $50\U{kg}$ arrive en bas d'une rampe à $8\ms$. """ + G10 + r"""

    1. Sans frottement, quelle hauteur peut-il atteindre ?
    2. En réalité, il monte de $2{,}8\U{m}$. Calculer l'énergie perdue.
    """, r"""
    1. $z_{\max}=\dfrac{v^2}{2g}=\dfrac{64}{20}=3{,}2\U{m}$.
    2. $E_m$ au départ : $\frac12\times50\times64=1600\U{J}$ ; au sommet : $50\times10\times2{,}8=1400\U{J}$. Énergie perdue : $200\U{J}$.
    """),
    exos=[
        ("le pendule simple", r"""
        Un pendule de longueur $\ell=1\U{m}$ est lâché sans vitesse quand le fil fait $60°$ avec la verticale. On néglige les frottements. """ + G10 + r""" Calculer la vitesse de la masse au passage par la verticale.
        """, r"""
        La masse descend de $h=\ell(1-\cos60°)=0{,}5\U{m}$. Conservation de $E_m$ : $\frac12mv^2=mgh$, donc $v=\sqrt{2\times10\times0{,}5}=\sqrt{10}\approx3{,}16\ms$.
        """),
        ("le toboggan", r"""
        Un objet de $0{,}5\U{kg}$ part sans vitesse d'une hauteur de $1{,}8\U{m}$ sur un toboggan et arrive en bas à $5\ms$. """ + G10 + r""" Y a-t-il des frottements ? Calculer l'énergie perdue.
        """, r"""
        $E_m$ en haut : $0{,}5\times10\times1{,}8=9\U{J}$ ; en bas : $\frac12\times0{,}5\times25=6{,}25\U{J}$. $E_m$ a diminué : il y a des frottements ; énergie perdue : $2{,}75\U{J}$.
        """),
    ],
)

EVAL_C = dict(duree=40, exos=[
    dict(titre="Le skieur", pts=10, enonce=r"""
    Un skieur de $80\U{kg}$ part sans vitesse du sommet $A$ d'une piste rectiligne $AB$ de longueur $50\U{m}$ ; la dénivellation entre $A$ et $B$ vaut $10\U{m}$. Sur $AB$, les frottements sont négligeables. Il continue ensuite sur une piste horizontale $BC$ où une force de frottement constante de $200\U{N}$ s'oppose au mouvement. """ + G10 + r"""

    1. Calculer le travail du poids entre $A$ et $B$. Que vaut le travail de la réaction ?
    2. Calculer la vitesse en $B$ avec le TEC.
    3. Quelle distance le skieur parcourt-il sur $BC$ avant de s'arrêter ?
    """, corr=r"""
    1. $W(\vec P)=mgh=80\times10\times10=8000\U{J}$ ; $W(\vec R)=0$ (réaction perpendiculaire au déplacement). **(3 pts)**
    2. $\frac12mv_B^2=8000$, donc $v_B=\sqrt{200}\approx14{,}1\ms$. **(3 pts)**
    3. Sur $BC$ : $0-8000=-200\,d$, donc $d=40\U{m}$. **(4 pts)**
    """),
    dict(titre="La balle et l'énergie mécanique", pts=10, enonce=r"""
    Une balle de $200\U{g}$ est lancée verticalement vers le haut à $8\ms$ depuis une hauteur de $1{,}5\U{m}$. On prend $E_p=0$ au sol. """ + G10 + r"""

    1. Calculer l'énergie mécanique au départ.
    2. Sans frottement, calculer la hauteur maximale atteinte et la vitesse en touchant le sol.
    3. En réalité, la balle monte jusqu'à $4{,}2\U{m}$. Calculer l'énergie perdue pendant la montée et la valeur moyenne de la force de frottement de l'air.
    """, corr=r"""
    1. $E_m=\frac12\times0{,}2\times64+0{,}2\times10\times1{,}5=6{,}4+3=9{,}4\U{J}$. **(3 pts)**
    2. Au sommet : $mgz_{\max}=9{,}4$, donc $z_{\max}=4{,}7\U{m}$. Au sol : $\frac12\times0{,}2\,v^2=9{,}4$, donc $v=\sqrt{94}\approx9{,}70\ms$. **(4 pts)**
    3. Au sommet réel : $E_m=0{,}2\times10\times4{,}2=8{,}4\U{J}$ ; perte : $1\U{J}$. Montée de $2{,}7\U{m}$ : $f=\dfrac{1}{2{,}7}\approx0{,}37\U{N}$. **(3 pts)**
    """),
])

# =====================================================================
# PARTIE D — Conservation de la quantité de mouvement
# =====================================================================
D1 = dict(
    id="p2-d1", titre="Système isolé et recul", duree=15,
    objectif="Utiliser la conservation de la quantité de mouvement d'un système isolé pour calculer une vitesse de recul.",
    cours=[
        retenir("Conservation de la quantité de mouvement", r"""
        Si un système est isolé ou pseudo-isolé ($\sum\vec F_{\text{ext}}=\vec 0$), sa quantité de mouvement totale est constante :

        $$\vec P_{\text{avant}}=\vec P_{\text{après}}$$

        Recul : un système au repos ($\vec P=\vec 0$) se sépare en deux parties, $m_1\vec v_1+m_2\vec v_2=\vec 0$, donc $\vec v_1=-\dfrac{m_2}{m_1}\vec v_2$ : les deux parties partent en sens opposés.
        """),
        prof(r"""
        Oriente un axe et garde les signes : une vitesse de recul négative est un bon résultat, elle dit « dans l'autre sens ».
        """),
    ],
    video=dict(id="p2-d1", titre="Le recul d'un fusil", phrases=[
        ("Conservation de la quantité de mouvement : le recul.", "Le recul"),
        ("Quand un système est isolé ou pseudo-isolé, sa quantité de mouvement totale ne change pas.", r"\vec P_{\text{avant}}=\vec P_{\text{après}}"),
        ("Exemple : un fusil de quatre kilogrammes tire une balle de dix grammes, à quatre cents mètres par seconde.", r"m_1=4\ \mathrm{kg},\ m_2=0{,}01\ \mathrm{kg},\ v_2=400\ \mathrm{m/s}"),
        ("Le système fusil plus balle est pseudo-isolé : le poids et la réaction se compensent. Avant le tir, tout est immobile : la quantité de mouvement est nulle.", r"\vec P_{\text{avant}}=\vec 0"),
        ("Après le tir : m un v un plus m deux v deux égale zéro.", r"m_1\vec v_1+m_2\vec v_2=\vec 0"),
        ("Donc v un égale moins m deux sur m un, fois v deux : moins zéro virgule zéro un sur quatre, fois quatre cents, soit moins un mètre par seconde.", r"v_1=-\dfrac{0{,}01}{4}\times400=-1\ \mathrm{m\cdot s^{-1}}"),
        ("Le signe moins veut dire que le fusil recule, en sens inverse de la balle. C'est le recul que ressent le tireur.", r"\text{le fusil recule}"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("le fusil", r"""
    Un fusil de $4\U{kg}$, au repos, tire horizontalement une balle de $10\U{g}$ à $400\ms$. Calculer la vitesse de recul du fusil.
    """, r"""
    Système {fusil + balle}, pseudo-isolé pendant le tir. Avant : $\vec P=\vec 0$. Après : $m_1\vec v_1+m_2\vec v_2=\vec 0$.

    Sur l'axe de la balle : $v_1=-\dfrac{m_2}{m_1}v_2=-\dfrac{0{,}01}{4}\times400=-1\ms$. Le fusil recule à $1\ms$.
    """),
    application=("les patineurs", r"""
    Deux patineurs immobiles sur la glace, A ($60\U{kg}$) et B ($40\U{kg}$), se poussent. B part à $3\ms$. Calculer la vitesse de A (frottements négligés).
    """, r"""
    Système {A + B} pseudo-isolé, $\vec P=\vec 0$ avant. Après : $60\,v_A+40\times3=0$, donc $v_A=-2\ms$ : A part à $2\ms$ dans l'autre sens.
    """),
    exos=[
        ("le canon", r"""
        Un canon de $500\U{kg}$ tire horizontalement un obus de $5\U{kg}$ à $200\ms$. Calculer la vitesse de recul du canon.
        """, r"""
        $v=-\dfrac{5\times200}{500}=-2\ms$ : le canon recule à $2\ms$.
        """),
        ("sauter d'une barque", r"""
        Un homme de $70\U{kg}$ saute horizontalement à $2\ms$ d'une barque de $140\U{kg}$ immobile. Avec quelle vitesse la barque part-elle ? (On néglige les frottements de l'eau.)
        """, r"""
        $70\times2+140\,v=0$, donc $v=-1\ms$ : la barque part à $1\ms$ dans le sens opposé.
        """),
    ],
)

D2 = dict(
    id="p2-d2", titre="Chocs mous et chocs élastiques", duree=20,
    objectif="Calculer les vitesses après un choc mou ou élastique et faire le bilan d'énergie cinétique.",
    cours=[
        retenir("Les deux types de chocs", r"""
        Dans tout choc, la quantité de mouvement du système se conserve : $m_1\vec v_1+m_2\vec v_2=m_1\vec v_1\,'+m_2\vec v_2\,'$.

        - **Choc mou** : les deux corps restent accrochés, $v'=\dfrac{m_1v_1+m_2v_2}{m_1+m_2}$. L'énergie cinétique **n'est pas conservée** : une partie devient chaleur et déformation.
        - **Choc élastique** : l'énergie cinétique **est conservée**. Si la cible est au repos : $v_1'=\dfrac{m_1-m_2}{m_1+m_2}\,v_1$ et $v_2'=\dfrac{2m_1}{m_1+m_2}\,v_1$.
        """),
        prof(r"""
        Deux masses égales en choc élastique échangent leurs vitesses : c'est le principe du pendule de Newton.
        """),
    ],
    video=dict(id="p2-d2", titre="Chocs mous et chocs élastiques", phrases=[
        ("Chocs mous et chocs élastiques.", "Les chocs"),
        ("Dans tout choc, la quantité de mouvement du système se conserve. Ce qui change d'un choc à l'autre, c'est l'énergie cinétique.", r"\vec P_{\text{avant}}=\vec P_{\text{après}}"),
        ("Dans un choc mou, les deux corps restent accrochés et repartent ensemble. Exemple : un wagon de deux tonnes à trois mètres par seconde percute un wagon d'une tonne immobile, et ils s'attellent.", r"m_1=2\ \mathrm t,\ v_1=3\ \mathrm{m/s},\ m_2=1\ \mathrm t"),
        ("Deux mille fois trois égale trois mille fois v prime. Donc v prime égale deux mètres par seconde.", r"v'=\dfrac{6000}{3000}=2\ \mathrm{m\cdot s^{-1}}"),
        ("Énergie cinétique avant : neuf mille joules. Après : six mille joules. Trois mille joules ont été perdus en chaleur et en déformation.", r"E_c:\ 9000\ \mathrm J\to6000\ \mathrm J"),
        ("Dans un choc élastique, l'énergie cinétique est conservée. Avec une cible au repos, on obtient deux formules à connaître.", r"v_1'=\dfrac{m_1-m_2}{m_1+m_2}v_1\qquad v_2'=\dfrac{2m_1}{m_1+m_2}v_1"),
        ("Cas particulier : deux masses égales. La première s'arrête, et la seconde repart avec la vitesse de la première. Elles échangent leurs vitesses.", r"m_1=m_2:\ v_1'=0,\ v_2'=v_1"),
        ("À toi de jouer : fais l'exercice d'application, puis les exercices de l'étape.", "À toi de jouer"),
    ]),
    exemple=("deux wagons qui s'attellent", r"""
    Un wagon de $2\U{t}$ roulant à $3\ms$ heurte un wagon de $1\U{t}$ immobile ; ils restent attelés.

    1. Calculer leur vitesse commune.
    2. Comparer les énergies cinétiques avant et après le choc.
    """, r"""
    1. Conservation de $\vec P$ : $2000\times3=3000\,v'$, donc $v'=2\ms$.
    2. Avant : $\frac12\times2000\times9=9000\U{J}$ ; après : $\frac12\times3000\times4=6000\U{J}$. Perte de $3000\U{J}$ : choc **mou**.
    """),
    application=("deux billes, choc élastique", r"""
    Une bille de $100\U{g}$ à $2\ms$ heurte une bille de $300\U{g}$ immobile. Le choc est élastique. Calculer les vitesses après le choc et vérifier la conservation de l'énergie cinétique.
    """, r"""
    $v_1'=\dfrac{0{,}1-0{,}3}{0{,}4}\times2=-1\ms$ (la petite bille rebondit) ; $v_2'=\dfrac{0{,}2}{0{,}4}\times2=1\ms$.

    $E_c$ avant : $\frac12\times0{,}1\times4=0{,}2\U{J}$ ; après : $0{,}05+0{,}15=0{,}2\U{J}$. Elle est bien conservée.
    """),
    exos=[
        ("masses égales", r"""
        Deux boules de même masse ; la première arrive à $v_1$ sur la seconde, immobile. Le choc est élastique. Que se passe-t-il ?
        """, r"""
        $v_1'=\dfrac{m-m}{2m}v_1=0$ et $v_2'=\dfrac{2m}{2m}v_1=v_1$ : la première s'arrête, la seconde repart avec la vitesse $v_1$.
        """),
        ("la balle dans le bloc", r"""
        Une balle de $20\U{g}$ à $300\ms$ s'enfonce dans un bloc de bois de $980\U{g}$ immobile sur la glace.

        1. Calculer la vitesse de l'ensemble juste après le choc.
        2. Quel pourcentage de l'énergie cinétique a été perdu ?
        """, r"""
        1. $0{,}02\times300=1\times v'$, donc $v'=6\ms$.
        2. Avant : $\frac12\times0{,}02\times9\times10^4=900\U{J}$ ; après : $\frac12\times1\times36=18\U{J}$. Perte : $882\U{J}$, soit $98$ % de l'énergie.
        """),
    ],
)

EVAL_D = dict(duree=40, exos=[
    dict(titre="Le patineur et le ballon", pts=10, enonce=r"""
    Un patineur de $50\U{kg}$, immobile sur la glace, lance horizontalement un ballon de $2\U{kg}$ à $10\ms$. """ + G10 + r"""

    1. Montrer que le système {patineur + ballon} est pseudo-isolé pendant le lancer.
    2. Calculer la vitesse du patineur juste après le lancer.
    3. Le patineur s'arrête après avoir glissé sur $2\U{m}$. En supposant la force de frottement constante, calculer sa valeur (par le TEC).
    """, corr=r"""
    1. Les forces extérieures sont les poids et la réaction de la glace, verticales, qui se compensent (frottements négligeables pendant le lancer). **(2 pts)**
    2. $\vec P=\vec 0$ avant : $50\,v+2\times10=0$, donc $v=-0{,}4\ms$ (sens opposé au ballon). **(4 pts)**
    3. TEC : $0-\frac12\times50\times0{,}16=-f\times2$, donc $f=2\U{N}$. **(4 pts)**
    """),
    dict(titre="Les deux pendules", pts=10, enonce=r"""
    Deux boules identiques de $100\U{g}$ sont suspendues à des fils de même longueur et se touchent au repos. On écarte la boule $B_1$ et on la lâche sans vitesse d'une hauteur $h=20\U{cm}$ au-dessus de sa position de repos. On néglige les frottements. """ + G10 + r"""

    1. Calculer la vitesse $v_1$ de $B_1$ juste avant le choc.
    2. Le choc est élastique. Donner les vitesses juste après le choc. À quelle hauteur remonte $B_2$ ?
    3. On recommence avec des boules en pâte à modeler qui restent collées (choc mou). Calculer leur vitesse commune, la hauteur atteinte et l'énergie perdue dans le choc.
    """, corr=r"""
    1. Conservation de $E_m$ : $v_1=\sqrt{2gh}=\sqrt{4}=2\ms$. **(2 pts)**
    2. Masses égales : $v_1'=0$ et $v_2'=2\ms$. $B_2$ remonte à $h=\dfrac{v_2'^2}{2g}=20\U{cm}$. **(4 pts)**
    3. $0{,}1\times2=0{,}2\,v'$, donc $v'=1\ms$ ; $h'=\dfrac{1}{20}=5\U{cm}$. $E_c$ : $0{,}2\U{J}$ avant, $\frac12\times0{,}2\times1=0{,}1\U{J}$ après : $0{,}1\U{J}$ perdu. **(4 pts)**
    """),
])

PARTIE_C = dict(lettre="C", titre="Les théorèmes énergétiques", etapes=[C1, C2], evaluation=EVAL_C)
PARTIE_D = dict(lettre="D", titre="La conservation de la quantité de mouvement", etapes=[D1, D2], evaluation=EVAL_D)
