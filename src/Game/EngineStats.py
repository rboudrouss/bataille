import numpy as np
import numpy.ma as ma

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

    def set_plateau(self, bateauPosL : list[PosList] = []) -> None:
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
        typeL = [i for i in range(self.nbB) if not self.bateaux[i]]

        for type in typeL:
            self.place_alea(type)
    
    def verify_from_mask(self, mask:ma.MaskedArray) -> bool:
        plateau_temp = self.plateau.copy()
        mask_temp = mask.copy()
        plateau_temp[plateau_temp > 1] = 1
        mask_temp[mask_temp > 1] = 1
        return  (mask_temp == plateau_temp).all()