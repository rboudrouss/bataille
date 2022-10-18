import logging
import numpy as np
import numpy.ma as ma
from random import randrange

from Game.Engine import Engine
from Game.EngineStats import EngineStats
from utils.constants import COULE_F, GEN_MC, MAX_GEN, MAX_IT
from utils.types import Pos, PosList
from .AbstractPlayer import AbstractPlayer


class MCPlayer(AbstractPlayer):
    def __init__(self, game: Engine, nbGen: int = GEN_MC, maxGen: int = MAX_GEN) -> None:
        super().__init__(game)
        self.local_game = EngineStats()
        self.bateauCPosL: list[PosList] = []
        self.nbGen = nbGen
        self.maxGen = maxGen

    @property
    def name(self):
        return "monte carlo"

    def reset(self, game: Engine | None = None, nbGen=GEN_MC, maxGen=MAX_GEN) -> None:
        super().reset()
        self.local_game.reset()
        self.bateauCPosL = []
        self.nbGen = nbGen
        self.maxGen = maxGen

    def play(self) -> None:
        temp_p: ma.MaskedArray = ma.array(
            np.zeros(self.dim, dtype=int),
            mask=self.plateau.mask == False,
            hard_mask=True,
            fill_value=-1
        )

        nbSuc = 0
        for j in range(self.nbGen):
            nbSuc += self.generate_plateau(j)

            temp = self.local_game.get_plateau()
            temp[temp > 1] = 1
            temp_p += temp

            self.local_game.set_plateau(self.bateauCPosL)

        logging.debug(
            f"Info : Playing with {nbSuc}/{self.nbGen} successful generations")
        if (temp_p == 0).all():
            logging.warning(
                "Warning : Toutes les générations étaient des echecs, on joue une case aléatoire")
            y = randrange(0, self.dim[0])
            x = randrange(0, self.dim[1])
            while not self.plateau.mask[y, x]:
                y = randrange(0, self.dim[0])
                x = randrange(0, self.dim[1])
        else:
            y, x = np.unravel_index(temp_p.argmax(), temp_p.shape)

        feedback, posL = self.interact_n_handle((y, x))

        if feedback == COULE_F:
            assert posL
            self.bateauCPosL.append(posL)

    def generate_plateau(self, num: int) -> int:
        """
        FIXME beaucoup trop de génération échoué, y aurait-il pas un meilleur moyen de générer ?

        genere un plateau aléatoire dans self.local_game
        respectant les contraintes de self.plateau
        Retourne 1 si réussi sinon 0
        """
        i = 0
        self.local_game.set_plateau(self.bateauCPosL)
        self.local_game.fill_random()
        while not self.local_game.verify_from_mask(self.plateau) and i < self.maxGen:
            self.local_game.set_plateau(self.bateauCPosL)
            self.local_game.fill_random()
            i += 1

        if i >= self.maxGen:
            logging.warning(
                "Warning : could not generate a valid plateau after {} attempts. attempt n°{}".format(i, num+1))
            self.local_game.set_plateau(self.bateauCPosL)
            return 0
        return 1
