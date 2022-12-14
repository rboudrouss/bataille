import logging
from Game import Engine
from Player.RandomPlayer import RandomPlayer
from utils.constants import END_F, MAX_IT, NOINFO_P, TOUCHE_F
from utils.types import Pos, PosList


class HeuristicPlayer(RandomPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)

        self.huntMode = False
        self.queueCoups: PosList = []

    @property
    def name(self):
        return "Heuristic"

    def reset(self, game: Engine | None = None) -> None:
        super().reset(game)
        self.huntMode = False
        self.queueCoups = []

    def play_hunt(self) -> None:
        """
        code for hunt play of HeuristicPlayer
        pour chaque case touché ajoute les cases adjacentes directes à la
        queue self.queueCoups. Tant qu'il y a des cases dedans 

        TODO à optimiser pour éliminer les cases par zone. par ex si case dans le groupe 
        x,y (1,0) est un raté, retire toutes les cases qui était dans le groupe (1,0)
        """
        self.add_adjacentCase(self.lastCoup)

        while self.queueCoups and self.lastfeedback != END_F:
            y, x = self.queueCoups.pop()
            self.lastCoup = (y, x)
            self.available.discard((y, x))

            self.lastfeedback, coule = self.interact((y, x))
            self.handle_feedback(self.lastfeedback, coule, (x, y))

            if self.lastfeedback == TOUCHE_F:
                self.add_adjacentCase(self.lastCoup)

        self.huntMode = False
        logging.info("Heuristic player switching to RANDOM mode")

    def add_adjacentCase(self, pos: Pos):
        """
        add adjencent keys of pos in the queue self.queueCoups
        """
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= pos[0]+dy < self.dim[0] and 0 <= pos[1]+dx < self.dim[1] and \
                    self.plateau.mask[pos[0]+dy, pos[1]+dx]:
                self.queueCoups.append((pos[0]+dy, pos[1]+dx))

    def play_random(self) -> None:
        """
        Plays ramdomly if last feedback is raté or coulé

        TODO optimiser pour envoyer que dans des cases pairs
        (vu que la taille minimal d'un bateau est 2, il est donc impossible de poser
        un bateau sans avoir une case tel que x ou y divisble par 2)
        """
        while self.lastfeedback not in [TOUCHE_F, END_F]:
            super().play()
        self.huntMode = True
        logging.info("Heuristic player switching to HUNT mode")
    
    def play(self) -> None:
        if self.huntMode:
            self.play_hunt()
        else:
            self.play_random()
