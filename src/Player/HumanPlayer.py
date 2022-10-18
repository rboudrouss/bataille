import logging
from Game.Engine import Engine
from utils.constants import MAX_IT
from utils.helpers import convert_posinput, valid_posinput
from .AbstractPlayer import AbstractPlayer


class HumanPlayer(AbstractPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)
        print(self.messages["start"].format(str(self.dim)))

    @property
    def name(self):
        return "human"

    def play(self) -> None:
        print(self.messages["showState"])
        self.show_info()
        self.show_game_info()

        if self.end:
            print(self.messages["playFinished"])
            return

        inp: str = ""
        i: int = 0
        while not valid_posinput(inp) and i < MAX_IT:
            inp = input(self.messages["askInput"])

        if i >= MAX_IT:
            logging.error(
                "Error : User took too many retries ({}) to give a valid input".format(
                    i)
            )
            exit(1)

        x, y = convert_posinput(inp)

        self.interact_n_handle((y, x))
