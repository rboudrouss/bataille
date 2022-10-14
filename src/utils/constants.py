#
#
# Config général du jeu :
#
#

# minimum (inclu) taille bateau : 2
MIN_LB = 2

# dimension du plateau de jeu en y,x
DIM_PLATEAU = (10, 10)

# maximum d'itération pour chaque boucle while (on est jamais trop prudent)
MAX_IT = DIM_PLATEAU[0] * DIM_PLATEAU[1] * 2

# LEN_B est la liste TRIEE des tailles des bateaux, déclare aussi les bateaux qu'il y a dans le jeu
# Sup la liste suivante : [5,4], On aura donc dans le jeu un bateau de taille 5 et un bateau de taille 4
LEN_B = [5, 4, 3, 3, 2]

# NB_B est le nombre de bateaux
NB_B = len(LEN_B)

# Mode Debug :
# affiche les informations de debug
# par exemple affiche le plateau enemie en mode HumanPlayer
DEBUG = True

#
#
# Config & convention dev
# **<!> ne pas toucher sauf si vous savez ce que vous faite <!>**
#
#

# direction du bateau 0 si vertical, 1 si horizontal
VER_D = 0
HOR_D = 1
DIR_L = [VER_D, HOR_D]

# le feedback du jeu doit être : 0 si raté, 1 si touché, 2 si coulé et -1 si le jeu est terminé
RATE_F = 0
TOUCHE_F = 1
COULE_F = 2
END_F = -1
FEEDBACK_L = [END_F, RATE_F, TOUCHE_F, COULE_F]

# les cases infos du plateau Joueur (dans AbstractPlayer notement) doivent être :
# -1 si no info, 0 si raté, 1 si touché, 2 si coulé
NOINFO_P = -1
RATE_P = RATE_F
TOUCHE_P = TOUCHE_F
COULE_P = COULE_F
INFOP_L = [NOINFO_P, RATE_P, TOUCHE_P, COULE_P]

#
# Vérifications
#

# vérifie que tout les bateaux sont bien >= à la taille min
assert all(map(lambda x: x >= MIN_LB, LEN_B))

# Vérifie que la liste des tailles des bateaux est trié
assert list(sorted(LEN_B, reverse=True)) == LEN_B
