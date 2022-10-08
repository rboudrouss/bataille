import numpy as np
from json import loads
from random import randrange, choice

from Game.Engine import Engine
from utils.helpers import convert_posinput, orderl, str_PosL, valid_posinput
from utils.types import MessDict, Pos, PosList
from .AbstractPlayer import AbstractPlayer


class RandomPlayer(AbstractPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)
        self.available = {(y, x) for y in range(self.dim[0])
                          for x in range(self.dim[1])}
        self.lastCoup = (0, 0)
        self.lastfeedback = 0

    def play(self) -> None:
        y, x = choice(list(self.available))
        self.available.discard((y, x))
        self.lastfeedback, posL = self.interact((y, x))

        self.handle_feedback(self.lastfeedback, posL, (x, y))
        self.lastCoup = (y, x)

    def main_loop(self) -> None:
        while not self.end:
            # self.show_game_info()
            self.play()
        print(self.messages['RandomNbWin'].format(self.nbCoup))
