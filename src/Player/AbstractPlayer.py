from abc import ABC, abstractclassmethod
import numpy as np
from json import loads

from Game.Engine import Engine
from utils.constants import DEBUG, MessDict, Pos, PosList
from utils.helpers import orderl, str_PosL


class AbstractPlayer(ABC):
    """
    Object abstrait auquel tout les joeurs devrons hérité pour être considéré comme fonctionnel

    Ici se passe toutes les intéractions avec le gameEngine et 
    se rappelle des résultats des anciens coups
    """

    def __init__(self, game: Engine) -> None:
        """
        game must be initialized

        pour le self.plateau :
        0 : Pas d'information
        1 : touché
        -1 : raté
        """

        if not game.isPlayable():
            print("Error : Game is not playable")
            return

        self.game = game
        self.dim = self.game.dim
        self.plateau = np.zeros(self.dim, dtype=int)
        self.end: bool = False
        self.nbCoup = 0

        with open("data/messages.json", 'r') as f:
            self.messages: MessDict = loads(f.read())

    def interact(self, pos: Pos) -> tuple[int, PosList | None]:
        """
        retourne 0 si raté, 1 si touché, 2 si coulé et -1 si le jeu est terminé
        si coulé retourne aussi les positions du bateau
        """
        self.nbCoup += 1
        return self.game.joue(pos)

    def handle_feedback(self, feedback: int, posL: PosList | None, pos: Pos) -> None:
        """
        affiche ce qu'il faut afficher à l'utilisateur selon le feedback de son action
        """
        x, y = pos

        # no switch
        if feedback == -1:
            if self.end:
                print(self.messages["playFinished"])
            else:
                assert posL
                self.end = True
                print(self.messages["couleCase"].format(str_PosL(posL)))
                print(self.messages["win"])

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

    def show_game_info(self) -> None:
        """
        Affiche le plateau du jeu
        <!> seulement en mode débug <!>
        """
        if DEBUG:
            print(self.game.plateau)

    @abstractclassmethod
    def main_loop(self) -> None:
        """
        loop principale du jeu
        """
        raise NotImplementedError
