"""
Projet 1 battaile navale
les bateaux sont :
1 : un porte-avions (5 cases)
2 : un croiseur (4 cases)
3 : un contre-torpilleurs (3 cases)
4 : un sous-marin (3 cases)
5 : un torpilleur (2 cases)
"""

import logging
from Game.Engine import Engine
from Player import AbstractPlayer, HeuristicPlayer, HumanPlayer, MCPlayer, ProbPlayer, RandomPlayer

if __name__ == "__main__":
    game = Engine()
    game.genere_grille()

    player: AbstractPlayer = RandomPlayer(game)
    player.main_loop()

    logging.info("-"*60)

    game.reset()
    game.genere_grille()

    player = HeuristicPlayer(game)
    player.main_loop()

    logging.info("-"*60)

    game.reset()
    game.genere_grille()

    player = ProbPlayer(game)
    player.main_loop()

    logging.info("-"*60)

    game.reset()
    game.genere_grille()

    player = MCPlayer(game)
    player.main_loop()

    logging.info("-"*60)

    if input("Voulez vous jouer au jeu vous même ? y/[n] ").strip().capitalize().startswith("Y"):
        game.reset()
        game.genere_grille()

        player = HumanPlayer(game)
        player.main_loop()
