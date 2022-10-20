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
from Game import Engine, EngineStats
from Player import AbstractPlayer, HeuristicPlayer, HumanPlayer, MCPlayer, ProbPlayer, RandomPlayer
from utils.constants import NB_B

if __name__ == "__main__":

    print("On peut placer le bateau de taille 5 {} fois différentes sur la plateau".format(
        EngineStats.nb_placer(1)
    ))

    print("On peut placer tout les bateaux (sans exclure les collisions) de {} fois différentes".format(
        EngineStats.nb_placerL(list(range(1,NB_B)))
    ))

    print("On peut placer les deux bateaux de taille 5 & 4 de {} manière différente".format(
        EngineStats.nb_placerL_NC([1,2])
    ))


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
