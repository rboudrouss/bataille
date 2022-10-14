import numpy as np

from Game.Engine import Engine
from utils.helpers import convert_posinput, valid_posinput
from .AbstractPlayer import AbstractPlayer


class HumanPlayer(AbstractPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)

    def play(self) -> None:
        if self.end:
            print(self.messages["playFinished"])
            return

        inp: str = ""
        while not valid_posinput(inp):
            inp = input(self.messages["askInput"])

        x, y = convert_posinput(inp)

        self.handle_feedback(*self.interact((y, x)), (x, y))


    def main_loop(self):
        """
        loop princiaple du jeu
        """
        print(self.messages["start"].format(str(self.dim)))
        while not self.end:
            print(self.messages["showState"])
            self.show_info()
            self.show_game_info()
            self.play()
