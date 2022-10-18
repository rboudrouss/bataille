import logging
import numpy as np
import numpy.ma as ma
from utils.constants import HOR_D, MIN_LB, VER_D

from utils.types import PosList
from .Engine import Engine


class EngineStats(Engine):
    """
    TODO move les fonctions utils.comb ici & faire des trucs plus complet
    genre génération de statitique etc...
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
