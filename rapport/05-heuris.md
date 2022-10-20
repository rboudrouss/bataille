## Joueur Heuristique

Un peu de stratégie, nous jouons toujours aléatoirement dans la détections mais cette fois nous usons des informations que nous donnes le jeu.
Si une case est touché, vu que les cases des bateaux sont lié, il a très probablement une case à touché à coté.

### Étude probabilistique

Notre stratégie heuristique avec l'ajout simple du mode "hunt" au mode aléatoire, nous sommes réussi à passer de 95 coups en moyennes à 64 coups. Et c'est bien ce que l'on observe sur la *Figure 2*.

![Probabilité pour le joeur Heuristique de gagner avec précisément n coup](./rapport/img/Heuristic_win.png "non cumulative Heuristic chances"){width=60%}


### Implémentation

Notre stratégie heuristique est implémenté dans le fichier `Player/HeuristicPlayer.py`. Il contient 2 mode de jeu

1. Mode "Hunt"

    - Ajoutes les cases adjacentes du derniers à la queue queueCoups

    - tant qu'il y a des éléments dans cette queue et que le jeu n'est pas terminé :

        - Joue le dernier élément de la queue
        
        - si c'est touché, ajoute les cases adjacentes à la queue.

    -Si il n'y plus d'élément dans la queue, passe en mode Aléatoire.

2. Mode Aléatoire (hérité de RandomPlayer)

    - tant que le dernier coup n'est pas un touché:

        - joue aléatoirement un coup dans l'ensemble des coups disponible

