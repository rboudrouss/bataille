import numpy as np
import numpy.ma as ma
from random import randrange

from Game import Engine
from Game.EngineStats import EngineStats
from utils.constants import COULE_F, GEN_MC, MAX_IT
from utils.types import Pos, PosList
from .AbstractPlayer import AbstractPlayer


class MCPlayer(AbstractPlayer):
    def __init__(self, game: Engine, nbGen: int = GEN_MC) -> None:
        """
        """
        super().__init__(game)
        self.name = "monte carlo"
        self.local_game = EngineStats()
        self.bateauCPosL: list[PosList] = []
        self.nbGen = nbGen

    def play(self) -> None:
        temp_p: ma.MaskedArray = ma.array(
            np.zeros(self.dim, dtype=int),
            mask=self.plateau.mask == False,
            hard_mask=True,
            fill_value=-1
        )

        for j in range(self.nbGen):
            i = 0
            self.local_game.fill_random()
            while not self.local_game.verify_from_mask(self.plateau) and i < (MAX_IT*10):
                self.local_game.set_plateau(self.bateauCPosL)
                self.local_game.fill_random()
                i += 1

            if i >= MAX_IT*10:
                print(
                    "Warning : could not generate a valid plateau avec {} attempts. attempt n°{}".format(i, j))
                continue

            temp = self.local_game.get_plateau()
            temp[temp > 1] = 1
            temp_p += temp

            self.local_game.set_plateau(self.bateauCPosL)

        if (temp_p == 0).all():
            print(
                "Warning : Toutes les générations étaient des echecs, on joue une case aléatoire")
            y = randrange(0, self.dim[0])
            x = randrange(0, self.dim[1])
            while self.plateau.mask[y, x]:
                y = randrange(0, self.dim[0])
                x = randrange(0, self.dim[1])
        else:
            y, x = np.unravel_index(temp_p.argmax(), temp_p.shape)

        feedback, posL = self.interact_n_handle((y, x))

        if feedback == COULE_F:
            assert posL
            self.bateauCPosL.append(posL)
