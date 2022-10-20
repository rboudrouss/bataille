## Joueur Probabiliste Simple

### Étude probabilistique

<!-- TODO -->
![Probabilité de gagner avec exactement n coup](./rapport/img/Probabilistic_winNC.png "cumulative probabilistic chances"){width=50%}
![Probabilité de gagner avec exactement n coup](./rapport/img/Probabilistic_time.png "cumulative probabilistic chances"){width=50%}

à gauche le probablité de gagner avec exactement n coup et à droite un historigrame du temps d'exécution.


### Implémentation

Notre stratégie probabiliste simple est implémenté dans le fichier `Player/HeuristicPlayer.py`. Avant chaque coup, pour chauque position que peut occuper un bateau et qui n'a pas déjà été joué, il ajoute 1
si le bateau peut être joué. Joue ensuite la case avec le nombre maximal.
