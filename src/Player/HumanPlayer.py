import numpy as np
from json import loads

from Game.Engine import Engine
from utils.helpers import convert_posinput, orderl, str_PosL, valid_posinput
from utils.constants import MessDict, Pos, PosList
from .AbstractPlayer import AbstractPlayer


class HumanPlayer(AbstractPlayer):
    def __init__(self, game: Engine) -> None:
        """
        game must be initialized

        pour le self.plateau :
        0 : Pas d'information
        1 : touché
        -1 : raté
        """
        super().__init__()

        if not game.isPlayable():
            print("Error : Game is not playable")
            return

        self.game = game
        self.plateau = np.zeros(game.dim, dtype=int)
        self.end: bool = False
        with open("data/messages.json", 'r') as f:
            self.messages: MessDict = loads(f.read())

    def play(self) -> None:
        if self.end:
            print(self.messages["playFinished"])
            return

        inp: str = ""
        while not valid_posinput(inp):
            inp = input(self.messages["askInput"])

        x, y = convert_posinput(inp)

        self.handle_feedback(*self.interact((y, x)), (x, y))

    def handle_feedback(self, feedback: int, posL: PosList | None, pos: Pos) -> None:
        """
        affiche ce qu'il faut afficher à l'utilisateur selon le feedback de son action
        """
        x, y = pos

        # no switch
        if feedback == -1:
            self.end = True
            if posL:
                print(self.messages["couleCase"].format(str_PosL(posL)))
                print(self.messages["win"])
            else:
                print(self.messages["playFinished"])

        elif feedback == 0:
            print(self.messages["rate"].format(str((x, y))))
            self.plateau[y, x] = -1

        elif feedback == 1:
            print(self.messages["touche"].format(str((x, y))))
            self.plateau[y, x] = 1

        elif feedback == 2:
            if posL is None:
                print("Error: posL is None ??")
                exit()
            print(self.messages["couleCase"].format(str_PosL(posL)))

            xmin, xmax = orderl(posL[0][1], posL[-1][1])
            ymin, ymax = orderl(posL[0][0], posL[-1][0])

            self.plateau[ymin:ymax+1, xmin:xmax+1] = 2

    def interact(self, pos: Pos) -> tuple[int, PosList | None]:
        """
        retourne 0 si raté, 1 si touché, 2 si coulé et -1 si le jeu est terminé
        si coulé retourne aussi les positions du bateau
        """
        return self.game.joue(pos)

    def show_info(self) -> None:
        print(self.plateau)

    def mainLoop(self):
        """
        loop princiaple du jeu
        """
        print(self.messages["start"].format(str(self.game.dim)))
        while not self.end:
            print(self.messages["showState"])
            self.show_info()
            print(self.game.plateau)
            self.play()
        
