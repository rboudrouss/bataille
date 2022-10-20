## Joueur Heuristique

### Étude probabilistique

<!-- TODO -->
![Probabilité de gagner avec au plus n coup](./rapport/img/Heuristic_win.png "cumulative Heuristic chances"){width=60%}


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

