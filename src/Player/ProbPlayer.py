import numpy as np
import numpy.ma as ma
from Game.Bateau import Bateau

from Game import Engine
from utils.constants import COULE_F, DIR_L, NOINFO_P, TOUCHE_P
from .AbstractPlayer import AbstractPlayer


class ProbPlayer(AbstractPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)
        self.notCBateaux = self.get_bateaux()

    def reset(self, game: Engine | None = None):
        super().reset()
        self.notCBateaux = self.get_bateaux()

    @property
    def name(self):
        return "Probabilistique"

    def play(self):
        temp_plateau = self.plateau.copy()
        temp_plateau.mask = False

        temp_p: ma.MaskedArray = ma.array(
            np.zeros(self.dim, dtype=int),
            mask=self.plateau.mask == False,
            hard_mask=True,
            fill_value=-1
        )

        for y in range(self.dim[0]):
            for x in range(self.dim[1]):
                for length in self.notCBateaux:
                    for dir in DIR_L:
                        if Engine.est_disponible(temp_plateau, (y, x), length, dir, [NOINFO_P, TOUCHE_P]):
                            for pos in Bateau.generate_posL((y, x), length, dir):
                                temp_p[pos] += 1
        # HACK les quadruples boucle for j'aime pas, trouver un meilleur moyen

        y, x = np.unravel_index(temp_p.argmax(), temp_p.shape)

        feedback, posL = self.interact_n_handle((y, x))  # type: ignore

        if feedback == COULE_F:
            assert posL
            self.notCBateaux.pop(self.notCBateaux.index(len(posL)))
