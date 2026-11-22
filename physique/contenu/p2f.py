# -*- coding: utf-8 -*-
"""P2 : les deux évaluations de fin de chapitre (2 h chacune), qui balaient tout le chapitre."""
G10 = r"On prend $g=10\mss$."

EVAL1 = dict(duree=120, exos=[
    dict(titre="La piste ABC (questions 1 à 3 : bac 2024)", pts=7, enonce=r"""
    __Les questions 1 à 3 sont extraites du bac S2 2024 (exercice 3, partie 3.1).__ Un objet se déplace sur une piste située dans un plan vertical : $AB$ est rectiligne, de longueur $\ell=1\U{m}$, inclinée d'un angle $\alpha=30°$ par rapport à l'horizontale ; $BC$ est rectiligne, horizontale, de longueur $\ell=1\U{m}$. Sur $AB$ et $BC$ s'exercent des forces de frottement équivalentes à une force unique $\vec f$ parallèle à la piste, opposée au vecteur vitesse et d'intensité constante. Un solide $S$, ponctuel, de masse $m=200\U{g}$, part du point $A$ sans vitesse à la date $t=0$. On prendra $g=10\U{SI}$.

    1. Exprimer la norme $v_B$ de la vitesse du solide en $B$ en fonction de $m$, $g$, $\ell$, $f$ et $\alpha$.
    2. Calculer l'intensité de $\vec f$ pour que le solide arrive en $C$ avec une vitesse nulle.
    3. Déterminer la date à laquelle le solide arrive en $B$.
    4. Par le TCI, calculer l'accélération sur $BC$ et la durée du trajet $BC$.
    5. Calculer la composante normale $\vec R_N$ de la réaction sur $AB$, puis la valeur de la réaction totale.
    6. On prend $E_p=0$ au niveau de $BC$. Calculer l'énergie mécanique en $A$ et en $C$. Comparer la perte au travail des frottements.
    """, corr=r"""
    1. TEC de $A$ à $B$ : $\frac12mv_B^2=mg\ell\sin\alpha-f\ell$, donc $v_B=\sqrt{2\ell\left(g\sin\alpha-\dfrac fm\right)}$. **(1,5 pt)**
    2. TEC de $A$ à $C$ : $0=mg\ell\sin\alpha-2f\ell$, donc $f=\dfrac{mg\sin\alpha}{2}=0{,}5\U{N}$. **(1,5 pt)**
    3. Sur $AB$ : $a=g\sin\alpha-\dfrac fm=2{,}5\mss$ ; $\ell=\frac12at_B^2$, donc $t_B=\sqrt{0{,}8}\approx0{,}89\U{s}$ ($v_B=\sqrt5\approx2{,}24\ms$). **(1 pt)**
    4. Sur $BC$ : $-f=ma_2$, $a_2=-2{,}5\mss$ ; durée $\dfrac{v_B}{2{,}5}\approx0{,}89\U{s}$ (le solide parcourt bien $\dfrac{5}{5}=1\U{m}$). **(1 pt)**
    5. $R_N=mg\cos\alpha\approx1{,}73\U{N}$ ; $R=\sqrt{1{,}73^2+0{,}5^2}\approx1{,}80\U{N}$. **(1 pt)**
    6. $E_m(A)=mg\ell\sin\alpha=1\U{J}$ ; $E_m(C)=0$. Perte $1\U{J}$ $=f\times2\ell$ : c'est le travail des frottements (changé en chaleur). **(1 pt)**
    """, revoir=[("questions 1 et 2", ["p2-c1"]), ("questions 3 et 4", ["p2-b1", "p2-b2"]), ("question 5", ["p2-b2"]), ("question 6", ["p2-c2"])]),
    dict(titre="Le pendule balistique", pts=6, enonce=r"""
    Un fusil de $2\U{kg}$ tire horizontalement une balle de $10\U{g}$, qui s'enfonce dans un bloc de bois de $990\U{g}$ suspendu à un fil. Juste après le choc, le bloc (avec la balle) remonte d'une hauteur $h=5\U{cm}$. On néglige les frottements. """ + G10 + r"""

    1. Calculer la vitesse $v'$ du bloc juste après le choc.
    2. Quel est le type de choc ? En déduire la vitesse $v$ de la balle avant le choc.
    3. Calculer l'énergie cinétique perdue dans le choc et la comparer à l'énergie initiale.
    4. Calculer la vitesse de recul du fusil.
    5. Calculer la vitesse du centre d'inertie du système {balle + bloc} juste avant et juste après le choc. Commenter.
    """, corr=r"""
    1. Conservation de $E_m$ après le choc : $v'=\sqrt{2gh}=1\ms$. **(1,25 pt)**
    2. Balle et bloc restent ensemble : choc **mou**. $\vec P$ conservée : $0{,}01\,v=1\times1$, donc $v=100\ms$. **(1,5 pt)**
    3. Avant : $\frac12\times0{,}01\times10^4=50\U{J}$ ; après : $\frac12\times1\times1=0{,}5\U{J}$. Perte $49{,}5\U{J}$, soit $99$ %. **(1,25 pt)**
    4. {fusil + balle} pseudo-isolé : $2\,v_f+0{,}01\times100=0$, donc $v_f=-0{,}5\ms$. **(1 pt)**
    5. $v_G=\dfrac{P}{M}=\dfrac{1}{1}=1\ms$ avant et après : le système est isolé pendant le choc, $\vec P=M\vec v_G$ ne change pas. **(1 pt)**
    """, revoir=[("question 1", ["p2-c2"]), ("questions 2 et 3", ["p2-d2"]), ("question 4", ["p2-d1"]), ("question 5", ["p2-a1"])]),
    dict(titre="Le téléski", pts=7, enonce=r"""
    Un skieur de $70\U{kg}$ est tiré par la perche d'un téléski, parallèle à une piste inclinée de $20°$ sur l'horizontale. Les frottements équivalent à une force constante de $50\U{N}$. """ + G10 + r""" ($\sin20°\approx0{,}342$ ; $\cos20°\approx0{,}940$)

    1. Le skieur monte à vitesse constante. Énoncer le principe utilisé, puis calculer la tension $T$ de la perche et la réaction normale de la piste.
    2. Au démarrage, l'accélération vaut $0{,}5\mss$. Calculer la tension.
    3. À $3\ms$, le skieur lâche la perche. Calculer sa décélération (TCI), la distance qu'il parcourt encore en montant et la durée correspondante.
    4. Retrouver cette distance avec le théorème de l'énergie cinétique.
    5. À vitesse constante, sur $200\U{m}$ de piste : calculer les travaux de la tension, du poids et des frottements. Vérifier le TEC.
    """, corr=r"""
    1. Principe de l'inertie (MRU) : $T=mg\sin\alpha+f\approx239{,}4+50=289{,}4\U{N}$ ; $R_N=mg\cos\alpha\approx658\U{N}$. **(1,5 pt)**
    2. $T-mg\sin\alpha-f=ma$, donc $T\approx289{,}4+35=324{,}4\U{N}$. **(1 pt)**
    3. $a=-\left(g\sin\alpha+\dfrac fm\right)\approx-4{,}13\mss$ ; $d=\dfrac{9}{2\times4{,}13}\approx1{,}09\U{m}$ ; $t=\dfrac{3}{4{,}13}\approx0{,}73\U{s}$. **(1,5 pt)**
    4. $0-\frac12\times70\times9=-(mg\sin\alpha+f)\,d$, donc $d=\dfrac{315}{289{,}4}\approx1{,}09\U{m}$. **(1,5 pt)**
    5. $W(\vec T)=289{,}4\times200\approx57\,880\U{J}$ ; $W(\vec P)=-mg\times200\sin\alpha\approx-47\,880\U{J}$ ; $W(\vec f)=-10\,000\U{J}$ ; somme nulle $=\Delta E_c$. **(1,5 pt)**
    """, revoir=[("question 1", ["p2-a2", "p2-b2"]), ("questions 2 et 3", ["p2-b1", "p2-b2"]), ("questions 4 et 5", ["p2-c1"])]),
])

EVAL2 = dict(duree=120, exos=[
    dict(titre="Aller et retour sur un plan incliné", pts=7, enonce=r"""
    Un solide de $0{,}5\U{kg}$ est lancé depuis le bas $O$ d'un plan incliné de $30°$, vers le haut, à $6\ms$. Une force de frottement constante $f=0{,}5\U{N}$ s'oppose au mouvement. """ + G10 + r"""

    1. Appliquer le TCI pendant la montée : calculer l'accélération et la réaction normale.
    2. Calculer la distance parcourue avant l'arrêt et la durée de la montée.
    3. Montrer que le solide redescend, puis calculer son accélération pendant la descente.
    4. Calculer sa vitesse en repassant en $O$, puis la retrouver par le TEC sur l'aller-retour.
    5. Calculer l'énergie mécanique perdue sur l'aller-retour. Que devient-elle ?
    """, corr=r"""
    1. Axe vers le haut : $-mg\sin\alpha-f=ma_1$, $a_1=-(5+1)=-6\mss$ ; $R_N=mg\cos\alpha\approx4{,}33\U{N}$. **(1,5 pt)**
    2. $d=\dfrac{36}{12}=3\U{m}$ ; $t=1\U{s}$. **(1,5 pt)**
    3. $mg\sin\alpha=2{,}5\U{N}>f$ : il redescend. Axe vers le bas : $a_2=5-1=4\mss$. **(1 pt)**
    4. $v^2=2\times4\times3=24$, $v\approx4{,}90\ms$. TEC : $\frac12\times0{,}5\,v^2-9=-0{,}5\times6$, donc $v^2=24$. **(1,5 pt)**
    5. $E_m$ : $9\U{J}$ au départ, $6\U{J}$ au retour ; $3\U{J}$ perdus, changés en chaleur par les frottements. **(1,5 pt)**
    """, revoir=[("questions 1 à 3", ["p2-b1", "p2-b2"]), ("question 4", ["p2-b2", "p2-c1"]), ("question 5", ["p2-c2"])]),
    dict(titre="Le choc des billes", pts=6, enonce=r"""
    Une bille A de $200\U{g}$ roulant à $4\ms$ heurte une bille B de $600\U{g}$ immobile, sur un plan horizontal. Le choc est élastique.

    1. Calculer la vitesse du centre d'inertie du système {A + B} avant le choc. Que vaut-elle après ? Justifier.
    2. Calculer les vitesses de A et de B juste après le choc. Vérifier la vitesse de $G$.
    3. Vérifier la conservation de l'énergie cinétique.
    4. B glisse ensuite sur un sol où s'exerce une force de frottement constante de $0{,}3\U{N}$. Quelle distance parcourt-elle avant de s'arrêter ?
    5. Si les billes étaient restées collées, quelle aurait été leur vitesse ? Quelle énergie aurait été perdue ?
    """, corr=r"""
    1. $v_G=\dfrac{0{,}2\times4}{0{,}8}=1\ms$ ; le système est isolé pendant le choc : $\vec P$, donc $\vec v_G$, ne change pas. **(1 pt)**
    2. $v_A'=\dfrac{0{,}2-0{,}6}{0{,}8}\times4=-2\ms$ ; $v_B'=\dfrac{0{,}4}{0{,}8}\times4=2\ms$ ; $v_G=\dfrac{-0{,}4+1{,}2}{0{,}8}=1\ms$. **(1,5 pt)**
    3. Avant : $1{,}6\U{J}$ ; après : $0{,}4+1{,}2=1{,}6\U{J}$. **(1 pt)**
    4. TEC : $0-1{,}2=-0{,}3\,d$, donc $d=4\U{m}$. **(1,25 pt)**
    5. $v'=v_G=1\ms$ ; $E_c=\frac12\times0{,}8\times1=0{,}4\U{J}$ : $1{,}2\U{J}$ perdus. **(1,25 pt)**
    """, revoir=[("question 1", ["p2-a1", "p2-d1"]), ("questions 2, 3 et 5", ["p2-d2"]), ("question 4", ["p2-c1"])]),
    dict(titre="Le remorquage", pts=7, enonce=r"""
    Une voiture de $1000\U{kg}$ tire une remorque de $500\U{kg}$ par une barre horizontale, sur une route droite et horizontale. Les frottements valent $200\U{N}$ sur la voiture et $100\U{N}$ sur la remorque. """ + G10 + r"""

    1. Le convoi roule à vitesse constante. Calculer la tension de la barre et la force motrice.
    2. Au démarrage, l'accélération vaut $1{,}2\mss$. Calculer la tension de la barre (système : la remorque) et la force motrice (système : le convoi).
    3. Partie du repos, quelle vitesse le convoi atteint-il après $50\U{m}$ ? Vérifier avec le TEC appliqué au convoi.
    4. Le centre d'inertie de la remorque est à $6\U{m}$ derrière celui de la voiture. Situer le centre d'inertie du convoi et calculer sa quantité de mouvement à $20\ms$.
    5. À $20\ms$ constante, la barre casse. Calculer la décélération de la remorque et la distance qu'elle parcourt avant de s'arrêter.
    """, corr=r"""
    1. Remorque en MRU : $T=100\U{N}$ ; convoi en MRU : $F=200+100=300\U{N}$. **(1,5 pt)**
    2. Remorque : $T-100=500\times1{,}2$, $T=700\U{N}$. Convoi : $F-300=1500\times1{,}2$, $F=2100\U{N}$. **(1,5 pt)**
    3. $v=\sqrt{2\times1{,}2\times50}=\sqrt{120}\approx11\ms$. TEC : $2100\times50-300\times50=90\,000\U{J}=\frac12\times1500\times120$. **(1,5 pt)**
    4. Origine sur $G_{\text{voiture}}$, axe vers l'arrière : $x_G=\dfrac{500\times6}{1500}=2\U{m}$ derrière la voiture. $P=1500\times20=3\times10^4\U{kg\cdot m\cdot s^{-1}}$. **(1,25 pt)**
    5. $-100=500\,a$, $a=-0{,}2\mss$ ; $d=\dfrac{400}{0{,}4}=1000\U{m}$. **(1,25 pt)**
    """, revoir=[("question 1", ["p2-a2"]), ("questions 2 et 5", ["p2-b1"]), ("question 3", ["p2-c1"]), ("question 4", ["p2-a1"])]),
])

FINALS = [EVAL1, EVAL2]
