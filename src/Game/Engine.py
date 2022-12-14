import logging
import numpy as np  # type: ignore
from random import randint, choice
import matplotlib.pyplot as plt  # type: ignore

from utils.constants import COULE_F, DIM_PLATEAU, DIR_L, EMPTY_G, END_F, HOR_D, LEN_B, MAX_IT,\
    MIN_LB, RATE_F, TOUCHE_F, VER_D
from utils.types import Pos, PosList
from .Bateau import Bateau


class Engine:
    def __init__(self, dim: Pos = DIM_PLATEAU, bateauxL: list[int] = LEN_B):
        self.plateau = np.full(dim, fill_value=EMPTY_G, dtype=int)
        self.bateauxL = bateauxL

        self.bateaux: list[Bateau | None] = [None]*self.nbB
        self.coules: list[bool] = [False]*self.nbB
        self.end: bool = False

    @property
    def dim(self) -> Pos: # type: ignore
        return self.plateau.shape

    @property
    def nbB(self) -> int:
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

        return self.est_disponible(self.plateau, pos, size, direction)

    @staticmethod
    def est_disponible(plateau: np.ndarray, pos: Pos, length: int, direction: int, empty_valueL: list[int] = [EMPTY_G]) -> bool:
        """
        vérifie si la place que prendra un bateau dans le plateau est disponible
        """
        # HACK find a better way using numpy
        assert direction in DIR_L
        assert length >= MIN_LB

        if direction:
            return pos[1] + length <= plateau.shape[1] and \
                all(i in empty_valueL for i in plateau[pos[0],
                    pos[1]:pos[1]+length])

        return pos[0] + length <= plateau.shape[0] and \
            all(i in empty_valueL for i in plateau[pos[0]
                :pos[0]+length, pos[1]])

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
            logging.warning(
                f"Warning: bateau {type} pas placé sur {pos}, ce n'est pas libre"
            )
            return
        # sinon bateau déjà placé c'est bizarre
        if self.bateaux[type-1]:
            logging.warning("Warning : bateau déjà placé (?)")

        size: int = self.bateauxL[type-1]
        self.bateaux[type-1] = Bateau(length=size,
                                      direction=direction, pos=pos)

        if direction:
            self.plateau[pos[0], pos[1]:pos[1]+size] = type
            return

        self.plateau[pos[0]:pos[0]+size, pos[1]] = type

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
                logging.error(
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
            logging.warning(
                "Warning: le jeu est terminé, mais ça joue encore ?")
            return END_F, None
        y, x = pos
        type: int = self.plateau[y, x]
        if type == 0:
            return RATE_F, None

        if self.bateaux[type-1] is None:
            logging.critical(
                "Error : self.bateaux{} is None <!>".format(type-1))
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
