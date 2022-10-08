#
# Config général du jeu :
#
MAX_IT = 100
MIN_LB = 2  # minimum taille bateau : 2
DIM_PLATEAU = (10, 10)  # dimension du plateau de jeu en y,x


# LEN_B est la liste des tailles des bateaux, déclare aussi les bateaux qu'il y a dans le jeu
# Sup la liste suivante : [5,4], On aura donc dans le jeu un bateau de taille 5 et
# et un bateau de taille 4
LEN_B = [5, 4, 3, 3, 2]

# Mode Debug :
# affiche les informations de debug
# par exemple affiche le plateau enemie en mode HumanPlayer
DEBUG = True


#
# Config & convention dev
# **<!> ne pas toucher sauf si vous savez ce que vous faite <!>**
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
