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
from Player import AbstractPlayer, HeuristicPlayer, HumanPlayer, MCPlayer, ProbPlayer, RandomPlayer, show_diagram
from utils.constants import MAX_IT, NB_B

if __name__ == "__main__":

    game = Engine()
    game.genere_grille()
    game.affiche()

    if input("Voulez vous essayer de trouver le nombre de combinaisons possible ? y/[n]").strip().capitalize().startswith("Y"):
        for i in range(NB_B):
            logging.info("On peut placer le bateau de type {}, {} fois différentes sur la plateau".format(
                i, EngineStats.nb_placer(i)
            ))

        logging.info("On peut placer tout les bateaux (sans exclure les collisions) de {} fois différentes".format(
            EngineStats.nb_placerL(list(range(1, NB_B+1)))
        ))

        logging.info("Nombre d'itération pour tirer une grille aléatoire {}".format(
            EngineStats.nb_alea(game.plateau)
        ))

        bateaux : list = []
        for i in range(NB_B):
            bateaux.append(i+1)
            logging.info("on peut placer les bateaux {} de {} manières différentes".format(bateaux,EngineStats.nb_placerL_brute(bateaux)))

    if input("Voulez vous générer des données ? y/[n] ").strip().capitalize().startswith("Y"):
        i = 0
        while True:
            i+=1
            game.reset()
            game.genere_grille()

            player= RandomPlayer(game)
            player.main_loop()

            game.reset()
            game.genere_grille()

            player = HeuristicPlayer(game)
            player.main_loop()

            game.reset()
            game.genere_grille()

            player = ProbPlayer(game)
            player.main_loop()

            game.reset()
            game.genere_grille()

            player = MCPlayer(game)
            player.main_loop()

            print(i)

    if input("Voulez vous afficher les données enregistrés? y/[n] ").strip().capitalize().startswith("Y"):
        print("Attention les données doivent être généré au préalable")
        show_diagram("Random")
        show_diagram("Heuristic")
        show_diagram("Probabilistic")
        show_diagram("MC")



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
    