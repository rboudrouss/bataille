"""
Projet 1 bataille navale
les bateaux sont :
1 : un porte-avions (5 cases)
2 : un croiseur (4 cases)
3 : un contre-torpilleurs (3 cases)
4 : un sous-marin (3 cases)
5 : un torpilleur (2 cases)
"""
import numpy as np

from constants import Pos, PosList
from constants import DIM_PLATEAU, LEN_B, MAX_IT
from Bataille import Bataille


def nb_placer(type: int) -> int:
    j = Bataille()
    ym, xm = j.dim
    nb: int = 0
    for y in range(ym):
        for x in range(xm):
            for dir in range(2):
                if j.peut_placer((y, x), type, dir):
                    nb += 1
    return nb


def nb_placerL(types: list[int]) -> int:
    j = Bataille()
    return _nb_placerL(j, j.plateau.copy(), types)


def _nb_placerL(jeu: Bataille, plateau: np.ndarray, types: list[int]) -> int:
    if not types:
        return 0

    jeu.plateau = plateau

    ym, xm = jeu.dim
    nb: int = 0
    for y in range(ym):
        for x in range(xm):
            for dir in range(2):
                if jeu.peut_placer((y, x), types[0], dir):
                    plateau = jeu.plateau.copy()
                    jeu.place((y, x), types[0], dir)
                    nb += _nb_placerL(jeu, jeu.plateau, types[1:])
                    jeu.plateau = plateau
                    if len(types) == 1:
                        nb += 1
    return nb


if __name__ == "__main__":
    print(nb_placerL(list(range(5))))
