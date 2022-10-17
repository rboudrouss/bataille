import numpy as np
from Game import Engine
from Game.EngineStats import EngineStats
from utils.constants import GEN_MC
from utils.types import Pos, PosList
from .AbstractPlayer import AbstractPlayer


class MCPlayer(AbstractPlayer):
    def __init__(self, game: Engine, nbGen : int = GEN_MC) -> None:
        """
        TODO Il est possible de récupérer les listes ci-dessous à partir de self.plateau.where() 
        bateauCPosL : la liste des PosList des bateaux coulé, cad la liste des listes de coordonnées
        touchCase : liste des cases coulées
        rateCase : liste des cases ratés
        """
        super().__init__(game)
        self.name = "monte carlo"
        self.local_game = EngineStats()
        self.bateauCPosL: list[PosList] = []
        self.touchCases: set[Pos] = {}
        self.rateCases: set[Pos] = {}
        self.nbGen = nbGen
    
    def play(self) -> None:
        temp_p = np.zeros(self.dim, dtype=int)
        for i in range(self.nbGen):
            plateau = self.local_game.get_plateau()
            self.local_game.fill_random()
    
