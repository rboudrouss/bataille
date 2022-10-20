from pathlib import Path
import logging
import logging.handlers
import matplotlib

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

# GEN_MC est le nombre de génération de plateau avant de prendre une décision pour l'algorithme
# MonteCarlo. Plus le nombre est grand plus l'agorithme sera précis (jusqu'à un certain point)
# mais plus cela prendra du temps
GEN_MC = 10


# MAX_GEN est le nombre de tentative MAXIMAL de génération aléatoire d'un plateau pour l'algorithme
# de montecarlo
MAX_GEN = MAX_IT*10

# Si True affiche des informations nécessaires à la programmation
# mais non nécessaire à la bonne utilisation du programme
DEBUG = False

#
#
# Config & convention dev
# **<!> ne pas toucher sauf si vous savez ce que vous faite <!>**
#
#

#
# PATHS
#

SRC_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = SRC_DIR/"data"

MSG_FILE = DATA_DIR/"messages.json"

LOG_FILE = SRC_DIR/"app.log"


#
# Convention Dev
#

# EMPTY_G est la valeur dans Engine de la case quand elle est vide
EMPTY_G = 0

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

# on force matplotlib a utilisé tkinter
#matplotlib.use('TkAgg') 


#
# Vérifications
#

# vérifie que tout les bateaux sont bien >= à la taille min
assert all(map(lambda x: x >= MIN_LB, LEN_B))

# Vérifie que la liste des tailles des bateaux est trié
assert list(sorted(LEN_B, reverse=True)) == LEN_B

#
# Configuration des logs
#

# format des messages de logs :
# Tuple contenant un string du format de message et un string du format de l'heure
FORMAT = "%(asctime)s [%(levelname)-5.5s]  %(message)s", '%H:%M:%S'

# instance du logger
logger = logging.getLogger()

# instance du gestionnaire des fichiers & de la console
fileHandler = logging.handlers.RotatingFileHandler(
    LOG_FILE, maxBytes=50000, backupCount=3)
consoleHandler = logging.StreamHandler()

# Applique le niveau de log
logger.setLevel(logging.DEBUG if DEBUG else logging.INFO)
# logger.setLevel(logging.WARNING)


# on onlève les log de matplotlib
logging.getLogger('PIL').setLevel(logging.WARNING)
logging.getLogger('matplotlib.font_manager').disabled = True

# Applique le format des messages de logs
logFormatter = logging.Formatter(*FORMAT)
fileHandler.setFormatter(logFormatter)
consoleHandler.setFormatter(logFormatter)

# Ajout des gestionnaires au logger
logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)
