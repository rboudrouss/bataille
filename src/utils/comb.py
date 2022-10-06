"""
Ici se trouve les fonctions demandés dans la partie 2 du projet

c.a.d toutes les fonctions liés au combinatoire du jeu, elles sont
moches et surtout absolument pas optimisés . Mais même optimisé 
on sait qu'il sera compliqué (en python en tout cas) de pouvoir
déterminer le nombre de plateau possible dans le jeu avec les conditions
fixé au départ
"""
# TODO améliorer les fonctions au moins visuellement

import numpy as np
from Game.Engine import Engine


def nb_placer(type: int) -> int:
    j = Engine()
    ym, xm = j.dim
    nb: int = 0
    for y in range(ym):
        for x in range(xm):
            for dir in range(2):
                if j.peut_placer((y, x), type, dir):
                    nb += 1
    return nb


def nb_placerL(types: list[int]) -> int:
    j = Engine()
    return _nb_placerL(j, j.plateau.copy(), types)


def _nb_placerL(jeu: Engine, plateau: np.ndarray, types: list[int]) -> int:
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


# TODO estimation aléatoire tralala TME2
