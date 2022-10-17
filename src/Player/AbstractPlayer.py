from abc import ABC, abstractclassmethod
import numpy as np
import numpy.ma as ma
from json import loads

from Game.Engine import Engine
from utils.constants import COULE_F, COULE_P, DEBUG, END_F, FEEDBACK_L, INFOP_L, MAX_IT, NOINFO_P, RATE_F, RATE_P, TOUCHE_F, TOUCHE_P
from utils.types import Pos, PosList, MessDict
from utils.helpers import orderl, str_PosL


class InfoP(ma.MaskedArray):
    """
    initialise une liste numpy selon les dimensions données mais
    ne peux accépter que les valeurs qui sont dans la liste INFOP_L
    """
    def __new__(cls, dim: Pos):
        data = np.full(dim, NOINFO_P, dtype=int)
        mask = ma.array(data, mask=True, fill_value=NOINFO_P)
        
        obj = ma.asarray(mask).view(cls)
        return obj

    def __setitem__(self, key, value):
        assert value in INFOP_L
        return super().__setitem__(key, value)


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
        2 : coulé
        -1 : raté
        """

        if not game.isPlayable():
            print("Error : Game is not playable")
            return

        self.game = game
        self.dim = self.game.dim
        self.plateau = InfoP(self.dim)
        self.end: bool = False
        self.nbCoup = 0
        self.name = "abstract"

        with open("data/messages.json", 'r') as f:
            self.messages: MessDict = loads(f.read())

    def interact(self, pos: Pos) -> tuple[int, PosList | None]:
        """
        retourne 0 si raté, 1 si touché, 2 si coulé et -1 si le jeu est terminé
        si coulé retourne aussi les positions du bateau
        """
        self.nbCoup += 1
        feedback, posL = self.game.joue(pos)

        assert feedback in FEEDBACK_L
        assert posL if feedback == COULE_F else True

        return feedback, posL

    def handle_feedback(self, feedback: int, posL: PosList | None, pos: Pos) -> None:
        """
        FIXME pos en x,y <!>

        affiche ce qu'il faut afficher à l'utilisateur selon le feedback de son actioe
        et modifie la liste des informations donné par le jeu & la variable self.end
        """
        assert feedback in FEEDBACK_L
        assert posL if feedback == COULE_F else True

        x, y = pos

        # no switch
        if feedback == END_F:
            if self.end:
                print(self.messages["playFinished"])
            else:
                assert posL
                self.end = True
                print(self.messages["couleCase"].format(str_PosL(posL)))
                print(self.messages["win"])

        elif feedback == RATE_F:
            print(self.messages["rate"].format(str((x, y))))
            self.plateau[y, x] = RATE_P

        elif feedback == TOUCHE_F:
            print(self.messages["touche"].format(str((x, y))))
            self.plateau[y, x] = TOUCHE_P

        elif feedback == COULE_F:
            if posL is None:
                print("Error: posL is None ??")
                exit()
            print(self.messages["couleCase"].format(str_PosL(posL)))

            xmin, xmax = orderl(posL[0][1], posL[-1][1])
            ymin, ymax = orderl(posL[0][0], posL[-1][0])

            self.plateau[ymin:ymax+1, xmin:xmax+1] = COULE_P

    def interact_n_handle(self, pos: Pos) -> tuple[int, PosList | None]:
        """
        interact and handle feedbake
        litteraly just excecute both self.interact & self.handle_feedback
        and returns the feedback

        pos en y,x
        """
        r = self.interact(pos)
        self.handle_feedback(*r, (pos[1], pos[0]))
        return r

    def show_game_info(self) -> None:
        """
        Affiche le plateau du jeu
        <!> seulement en mode débug <!>
        """
        if DEBUG:
            print(self.game.plateau)

    def show_info(self) -> None:
        """
        Affiche le plateau des informations donnés par le jeu
        """
        print(self.plateau)

    @abstractclassmethod
    def play(self, pos: Pos) -> None:
        # TODO maybe centralize play and make max int verification in this mainloop ?
        raise NotImplementedError

    def main_loop(self) -> None:
        """
        loop principale du jeu
        """
        i = 0
        while not self.end:
            # self.show_game_info()
            self.play()
            i += 1
            if i > MAX_IT:
                print("Error : i : {} > MAXIT {} in Player {}".format(
                    i, MAX_IT, self.name))
                exit(1)
        print(self.messages['NbWin'].format(self.name, self.nbCoup))

# TODO fonctions qui retourne les stats du joueur
