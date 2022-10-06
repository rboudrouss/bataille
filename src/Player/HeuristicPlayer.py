from Game.Engine import Engine
from Player.RandomPlayer import RandomPlayer
from utils.constants import Pos, PosList


class HeuristicPlayer(RandomPlayer):
    def __init__(self, game: Engine) -> None:
        super().__init__(game)

        self.huntMode = False
        self.lastfeedback = 0
        self.queueCoups: PosList = []

    def play_hunt(self) -> None:
        direction = -2

        self.add_adjacentCase(self.lastCoup)

        while self.queueCoups and self.lastfeedback != -1:
            y, x = self.queueCoups.pop()
            self.lastCoup = (y, x)
            self.available.discard((y, x))

            self.lastfeedback, coule = self.interact((y, x))
            self.handle_feedback(self.lastfeedback, coule, (x, y))

            if self.lastfeedback == 1:
                self.add_adjacentCase(self.lastCoup)

        self.huntMode = False
        print("Switch to random mode -------")

    def add_adjacentCase(self, pos: Pos):
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= pos[0]+dy < self.dim[0] and 0 <= pos[1]+dx < self.dim[1] and self.plateau[pos[0]+dy, pos[1]+dx] == 0:
                self.queueCoups.append((pos[0]+dy, pos[1]+dx))

    def play_random(self) -> None:
        while self.lastfeedback in [0, 2]:
            super().play()
        self.huntMode = True
        print("switch to hunt mode ---------")

    def main_loop(self) -> None:
        while self.lastfeedback != -1:
            if self.huntMode:
                self.play_hunt()
            else:
                self.play_random()
        print("le joueur heuristique a trouvé après {} coups".format(self.nbCoup))
