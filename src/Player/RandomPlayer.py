import numpy as np
from json import loads
from random import randrange, choice

from Game.Engine import Engine
from utils.constants import MAX_IT
from .AbstractPlayer import AbstractPlayer


class RandomPlayer(AbstractPlayer):
    def __init__(self, game: Engine) -> None:
        """
        TODO use self.plateau istead of self.available
        + find a way to not use self.lastCoup & self.lastfeedback
        like self.play returning the feedback ?
        """
        super().__init__(game)
        self.available = {(y, x) for y in range(self.dim[0])
                          for x in range(self.dim[1])}
        self.lastCoup = (0, 0)
        self.lastfeedback = 10

    @property
    def name(self):
        return "random"

    def reset(self, game: Engine | None = None) -> None:
        super().reset()
        self.available = {(y, x) for y in range(self.dim[0])
                          for x in range(self.dim[1])}
        self.lastCoup = (0, 0)
        self.lastfeedback = 10

    def play(self) -> None:
        y, x = choice(list(self.available))
        self.available.discard((y, x))
        self.lastfeedback, posL = self.interact((y, x))

        self.handle_feedback(self.lastfeedback, posL, (x, y))
        self.lastCoup = (y, x)
