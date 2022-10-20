## Joueur Heuristique

Un peu de stratégie, nous jouons toujours aléatoirement dans la phase de détections mais cette fois nous usons des informations que nous donnes le jeu.
Si une case est touchée, les cases des bateaux étant liées, il y a très probablement une case occupée adjacente.

### Étude probabiliste

Grâce à notre stratégie heuristique, avec l'ajout simple du mode "hunt" au mode aléatoire, nous avons réussi à passer de 95 coups en moyennes à 64 coups. C'est bien ce que l'on observe sur la *Figure 2*.

![Probabilité pour le joeur Heuristique de gagner avec précisément n coup](./rapport/img/Heuristic_win.png "non cumulative Heuristic chances"){width=60%}


### Implémentation

Notre stratégie heuristique est implémentée dans le fichier `Player/HeuristicPlayer.py`. Il contient 2 mode de jeu

1. Mode "Hunt"

    - ajoute les cases adjacentes de la dernière case touchée à la queue queueCoups

    - tant qu'il y a des éléments dans cette queue et que le jeu n'est pas terminé :

        - joue le dernier élément de la queue
        
        - si un bateau est touché, ajoute les cases adjacentes à la queue.

    - si il n'y plus d'élément dans la queue, passe en mode Aléatoire.

2. Mode Aléatoire (hérité de RandomPlayer)

    - tant que le dernier coup n'a pas touché:

        - joue aléatoirement un coup dans l'ensemble des coups disponibles

