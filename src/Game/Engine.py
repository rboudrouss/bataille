import numpy as np # type: ignore
from random import randint
import matplotlib.pyplot as plt # type: ignore

from utils.constants import DIM_PLATEAU, LEN_B, MAX_IT
from utils.constants import Pos, PosList
from Game.Bateau import Bateau


class Engine:
    def __init__(self):
        self.plateau = np.zeros(DIM_PLATEAU, dtype=int)
        self.bateauxL = LEN_B
        self.nbB: int = len(self.bateauxL)

        self.bateaux: list[Bateau | None] = [None]*self.nbB
        self.coules: list[bool] = [False]*self.nbB
        self.end: bool = False

    @property
    def dim(self) -> Pos:
        return self.plateau.shape

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
        assert type <= self.nbB
        assert 0 <= direction <= 1

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
        if not self.peut_placer(pos, type, direction):
            print("bateau {type} pas placé sur {pos}, ce n'est pas libre")
            return
        # sinon bateau déjà placé c'est bizarre
        if self.bateaux[type-1]:
            print("warning : bateau déjà placé (?)")

        size: int = self.bateauxL[type-1]
        self.bateaux[type-1] = Bateau(size, direction, pos)

        if direction:
            self.plateau[pos[0], pos[1]:pos[1]+size] = type
            return

        self.plateau[pos[0]:pos[0]+size, pos[1]] = type

    def place_alea(self, type: int) -> None:
        """
        Place aléatoirement le bateau de type type
        """

        size: int = self.bateauxL[type-1]

        pos = (randint(0, self.dim[0]-1), randint(0, self.dim[1]-1))
        direction = randint(0, 1)

        i: int = 0

        while not self.peut_placer(pos, type, direction):
            i += 1

            pos = (randint(0, self.dim[0]-1), randint(0, self.dim[1]-1))
            direction = randint(0, 1)

            if i > MAX_IT:
                print(
                    f"Plus de {MAX_IT} itération dans place_alea avec type {type}")
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

    def reset(self) -> None:
        """
        réinitialise à 0 l'objet
        """
        self.plateau = np.zeros(DIM_PLATEAU)

        for bateau in self.bateaux:  # on libère la mémoire sur python lol
            del bateau

        self.bateaux = [None]*self.nbB
        self.coules = [False]*self.nbB
        self.end = False

    def joue(self, pos: Pos) -> int:
        """
        retourne 0 si raté, 1 si touché, 2 si coulé et -1 si le jeu est terminé
        """
        if self.end:
            print("le jeu est terminé")
            return -1
        y, x = pos
        type: int = self.plateau[y, x]
        if type == 0:
            print("raté")
            return 0

        if self.bateaux[type-1] is None:
            print("Error : self.bateaux{} is None <!>".format(type-1))
            exit()

        bateau : Bateau = self.bateaux[type-1] # type: ignore

        bateau.touche(pos)
        if bateau.est_coule():
            self.coules[type-1] = True
            print("coulé")
            print("le bateau se trouvait aux cases", bateau.poss)
            self.victoire()
            return 2

        print("touché")
        return 1

    def victoire(self) -> bool:
        if all(self.coules):
            print("victoire \\o/")
            print(self.plateau)
            self.end = True
            return True
        return False

    @staticmethod
    def eq(grilleA: np.ndarray, grilleB: np.ndarray):
        """
        vérifie que deux grilles sont égales
        """
        return np.array_equal(grilleA, grilleB)
