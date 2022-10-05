from Game.Engine import Engine
from Player.RandomPlayer import RandomPlayer
from utils.constants import Pos


class HeuristicPlayer(RandomPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)

        self.chaseMode = False
        self.lastfeedback = 0

    def play_chase(self) -> None:
        while self.lastfeedback != -1:
            pass

    def play_random(self) -> None:
        while self.lastfeedback in [0, -1]:
            super().play()
        self.chaseMode = True
