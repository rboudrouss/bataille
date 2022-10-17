import numpy as np  # type: ignore
from random import randint, choice
import matplotlib.pyplot as plt  # type: ignore

from utils.constants import COULE_F, DIM_PLATEAU, DIR_L, END_F, HOR_D, LEN_B, MAX_IT,\
    MIN_LB, RATE_F, TOUCHE_F, VER_D
from utils.types import Pos, PosList
from .Bateau import Bateau


class Engine:
    def __init__(self, dim : Pos = DIM_PLATEAU, bateauxL:list[int] = LEN_B):
        self.plateau = np.zeros(dim, dtype=int)
        self.bateauxL = bateauxL

        self.bateaux: list[Bateau | None] = [None]*self.nbB
        self.coules: list[bool] = [False]*self.nbB
        self.end: bool = False

    @property
    def dim(self) -> Pos:
        return self.plateau.shape
    
    @property
    def nbB(self)->int:
        return len(self.bateauxL)

    def peut_placer(self, pos: Pos, type: int, direction: int) -> bool:
        """
        vérifie si le bateau peut être posé
        pos c'est (y,x) (avec y coord verticale et x coord horizontale)
        du type on récupère la longueur des bateaux, ex type = 1 => longueur = self.bateauxL[1 - 1] = 5
        Pour la direction :
            0 -> verticale
            1 -> horizotale
        Nous vérifions si la case *pos* est libre et nous vérifions suivont direction les cases suivantes
        """
        # préconditions :
        assert 0 <= type <= self.nbB
        assert direction in DIR_L

        # on récupère la taille
        size: int = self.bateauxL[type-1]

        if direction:
            return pos[1] + size <= self.dim[1] and all(self.plateau[pos[0], pos[1]:pos[1]+size] == 0)

        return pos[0] + size <= self.dim[0] and all(self.plateau[pos[0]:pos[0]+size, pos[1]] == 0)

    def place(self, pos: Pos, type: int, direction: int) -> None:
        """
        Place le bateau si les cases est vide
        pos c'est (y,x) (avec y coord verticale et x coord horizontale)
        du type on récupère la longueur des bateaux, ex type = 1 => longueur = self.bateau[1 - 1] = 5
        Pour la direction :
            0 -> verticale
            1 -> horizontale
        """
        assert direction in DIR_L
        assert 0 <= type <= self.nbB

        if not self.peut_placer(pos, type, direction):
            print(
                f"Warning: bateau {type} pas placé sur {pos}, ce n'est pas libre")
            return
        # sinon bateau déjà placé c'est bizarre
        if self.bateaux[type-1]:
            print("Warning : bateau déjà placé (?)")
            exit(1)

        size: int = self.bateauxL[type-1]
        self.bateaux[type-1] = Bateau(length=size,
                                      direction=direction, pos=pos)

        if direction:
            self.plateau[pos[0], pos[1]:pos[1]+size] = type
            return

        self.plateau[pos[0]:pos[0]+size, pos[1]] = type

    def place_posL(self, posL: PosList) -> None:
        """
        Place un bateau aux coordonnées PosL
        """
        assert len(posL) >= MIN_LB
        assert posL[0][0] == posL[1][0] or posL[0][1] == posL[1][1]

        length = len(posL)

        # assert that batteau of this length exists
        try:
            type = self.bateauxL.index(length) + 1
        except ValueError:
            print("Error : no boat of len {} in list self.bateauL {}".format(
                length, str(self.bateauxL)))
            exit(1)

        while type <= self.nbB and self.bateauxL[type-1] == length and self.bateaux[type-1]:
            type += 1

        if self.bateauxL[type-1] != length or type > self.nbB:
            type -= 1
            print("Warning : Les bateaux de la taille {} (type : {}) ont déjà été placés ??".format(
                length, type))

        pos = min(map(lambda x: x[0], posL)), min(map(lambda x: x[1], posL))
        assert pos in posL

        direction = HOR_D if posL[0][1] - posL[1][1] else VER_D

        self.place(pos, type, direction)

    def place_alea(self, type: int) -> None:
        """
        Place aléatoirement le bateau de type type
        """

        pos = (randint(0, self.dim[0]-1), randint(0, self.dim[1]-1))
        direction = choice(DIR_L)

        i: int = 0

        while not self.peut_placer(pos, type, direction):
            i += 1

            pos = (randint(0, self.dim[0]-1), randint(0, self.dim[1]-1))
            direction = randint(0, 1)

            if i > MAX_IT:
                print(
                    f"Error : Plus de {MAX_IT} itération dans place_alea avec type {type}")
                return

        self.place(pos, type, direction)

    def affiche(self) -> None:
        """
        affiche le plateau avec imshow
        """
        print(self.plateau)
        plt.imshow(self.plateau)
        plt.show()

    def genere_grille(self) -> None:
        """
        genere une grille aléatoirement
        """
        for type in range(1, self.nbB+1):
            self.place_alea(type)
        
        assert self.isPlayable()

    def reset(self) -> None:
        """
        réinitialise à 0 l'objet
        """
        self.plateau = np.zeros(DIM_PLATEAU, dtype=int)

        for bateau in self.bateaux:  # on libère la mémoire sur python lol
            del bateau

        self.bateaux = [None]*self.nbB
        self.coules = [False]*self.nbB
        self.end = False

    def joue(self, pos: Pos) -> tuple[int, PosList | None]:
        """
        retourne 0 si raté, 1 si touché, 2 si coulé et -1 si le jeu est terminé
        si coulé retourne aussi les positions du bateau
        """
        if self.end:
            print("Warning: le jeu est terminé, mais ça joue encore ?")
            return END_F, None
        y, x = pos
        type: int = self.plateau[y, x]
        if type == 0:
            return RATE_F, None

        if self.bateaux[type-1] is None:
            print("Error : self.bateaux{} is None <!>".format(type-1))
            exit()

        bateau: Bateau = self.bateaux[type-1]  # type: ignore

        bateau.touche(pos)
        if bateau.est_coule():
            self.coules[type-1] = True
            return END_F if self.victoire() else COULE_F, bateau.get_pos()

        return TOUCHE_F, None

    def victoire(self) -> bool:
        if all(self.coules):
            self.end = True
            return True
        return False

    def isPlayable(self) -> bool:
        return all(self.bateaux)

    @staticmethod
    def eq(grilleA: np.ndarray, grilleB: np.ndarray) -> bool:
        """
        vérifie que deux grilles sont égales
        """
        return np.array_equal(grilleA, grilleB)
