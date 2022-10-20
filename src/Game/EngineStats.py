import logging
import numpy as np
import numpy.ma as ma
from utils.constants import HOR_D, MIN_LB, VER_D

from utils.types import PosList
from .Engine import Engine


class EngineStats(Engine):
    """
    La même chose que Engine mais avec des fonctions techniques poussées
    """

    def get_plateau(self) -> np.ndarray:
        return self.plateau.copy()

    def get_bateau_place(self) -> list[int]:
        return [i+1 for i in range(self.nbB) if self.bateaux[i]]

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
            logging.error("Error : no boat of len {} in list self.bateauL {}".format(
                length, str(self.bateauxL)))
            exit(1)

        while type <= self.nbB and self.bateauxL[type-1] == length and self.bateaux[type-1]:
            type += 1

        if self.bateauxL[type-1] != length or type > self.nbB:
            type -= 1
            logging.warning("Warning : Les bateaux de la taille {} (type : {}) ont déjà été placés ??".format(
                length, type))

        pos = min(map(lambda x: x[0], posL)), min(map(lambda x: x[1], posL))
        assert pos in posL

        direction = HOR_D if posL[0][1] - posL[1][1] else VER_D

        self.place(pos, type, direction)


    def set_plateau(self, bateauPosL: list[PosList] = []) -> None:
        """
        met le jeu dans l'état donné en paramètre
        """
        self.reset()
        for posL in bateauPosL:
            self.place_posL(posL)

    def fill_random(self):
        """
        Place les bateaux non placés aléatoirement
        """
        typeL = [i+1 for i in range(self.nbB) if not self.bateaux[i]]

        for type in typeL:
            self.place_alea(type)

    def verify_from_mask(self, mask: ma.MaskedArray) -> bool:
        if mask.mask.all():
            return True
        plateau_temp = self.plateau.copy()
        mask_temp = mask.copy()
        plateau_temp[plateau_temp > 1] = 1
        mask_temp[mask_temp > 1] = 1
        return (mask_temp == plateau_temp).all()
    
    """
    Ici se trouve les fonctions demandés dans la partie 2 du projet

    c.a.d toutes les fonctions liés au combinatoire du jeu, elles sont
    moches et surtout absolument pas optimisés . Mais même optimisé 
    on sait qu'il sera compliqué (en python en tout cas) de pouvoir
    déterminer le nombre de plateau possible dans le jeu avec les conditions
    fixé au départ
    """
    # TODO améliorer les fonctions au moins visuellement

    @staticmethod
    def nb_placer(type:int)->int:
        """
        retourne le nombre de fois que l'ont peut placer un bateau sur la grille
        """
        j = EngineStats()
        ym, xm = j.dim
        nb = 0

        for y in range(ym):
            for x in range(xm):
                for dir in range(2):
                    if j.peut_placer((y, x), type, dir):
                        nb += 1
        return nb
    
    @staticmethod
    def nb_placerL(types: list[int])->int:
        """
        pour une liste de type de bateau retourne le nombre de position possible
        de ces bateaux sur cette grille.
        <!> avec cette fonctions les bateaux peuvent se supperposer.
        """
        nb = 1
        for type in types:
            nb *= EngineStats.nb_placer(type)
        return nb
    
    @staticmethod
    def nb_placerL_brute(types:list[int], jeu = None, plateau : np.ndarray | None = None) -> int:
        """
        Pour une liste de type de bateau retourne le nimbre de position possible
        de ces bateaux sur cette grille.
        <!> cette fonction les positions sont uniques
        cependant elle est relativement lente et absolument pas optimisé
        """
        if not types:
            return 0

        if not jeu:
            j = EngineStats()
            return EngineStats.nb_placerL_brute(types,j,j.get_plateau())

        ym, xm = jeu.dim
        nb: int = 0
        for y in range(ym):
            for x in range(xm):
                for dir in range(2):
                    if jeu.peut_placer((y, x), types[0], dir):
                        plateau = jeu.get_plateau()
                        jeu.place((y, x), types[0], dir)
                        nb += EngineStats.nb_placerL_brute(types[1:],jeu, jeu.get_plateau())
                        jeu.reset()
                        jeu.plateau = plateau
                        if len(types) == 1:
                            nb += 1
        return nb





