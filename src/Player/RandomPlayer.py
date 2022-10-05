import numpy as np
from json import loads
from random import randrange

from Game.Engine import Engine
from utils.helpers import convert_posinput, orderl, str_PosL, valid_posinput
from utils.constants import MessDict, Pos, PosList
from .AbstractPlayer import AbstractPlayer


class RandomPlayer(AbstractPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)

    def main_loop(self) -> None:
        i = 0
        while not self.end:
            # self.show_game_info()
            x = randrange(self.dim[1])
            y = randrange(self.dim[0])
            self.handle_feedback(*self.interact((y,x)), (x,y))
            i+=1
        print("Le joueur aléatoire y est arrivé en {} coups".format(i))
        
        
