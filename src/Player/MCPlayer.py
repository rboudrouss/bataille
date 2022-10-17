import numpy as np

from Game import Engine
from Game.EngineStats import EngineStats
from utils.constants import GEN_MC
from utils.types import Pos, PosList
from .AbstractPlayer import AbstractPlayer


class MCPlayer(AbstractPlayer):
    def __init__(self, game: Engine, nbGen : int = GEN_MC) -> None:
        """
        """
        super().__init__(game)
        self.name = "monte carlo"
        self.local_game = EngineStats()
        self.bateauPosL : list[PosList] = []
        self.nbGen = nbGen
    
    def play(self) -> None:
        temp_p = np.zeros(self.dim, dtype=int)
        for i in range(self.nbGen):
            while not self.local_game.verify_from_mask(self.plateau):
                self.local_game.set_plateau(self.bateauPosL)
                self.local_game.fill_random()
            
            self.local_game.set_plateau(self.bateauPosL)
            
    
