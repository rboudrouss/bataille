"""
Projet 1 battaile navale
les bateaux sont :
1 : un porte-avions (5 cases)
2 : un croiseur (4 cases)
3 : un contre-torpilleurs (3 cases)
4 : un sous-marin (3 cases)
5 : un torpilleur (2 cases)
"""

from Game.Engine import Engine
from Player.HumanPlayer import HumanPlayer
from Player.RandomPlayer import RandomPlayer
from utils.comb import nb_placer

if __name__ == "__main__":
    game = Engine()
    game.genere_grille()

    assert game.isPlayable()

    player = RandomPlayer(game)
    player.main_loop()

