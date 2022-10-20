## Joueur Probabiliste Simple

Essayons cette fois-ci de prendre en compte de l'information "coulé" qui nous donne aussi les cases du bateau couclé.
Nous pouvons donc déduire des bateaux coulés et de ceux qui sont restant.

### Étude probabilistique

La stratégie probabilist simple prend environ 57 coups en moyenne pour réussir. Cependant on vois bien qu'elle prend beaucoup plus de temps à s'excécuter contrairement aux deux autres stratégies précédentes (en moyenne 1.7 secondes vs largement moins qu'une seconde) car elle nécessite beaucoup plus de calcul avant.


![Probabilité de gagner avec exactement n coup](./rapport/img/Probabilistic_winNC.png "cumulative probabilistic chances"){width=50%}
![Probabilité de gagner avec exactement n coup](./rapport/img/Probabilistic_time.png "cumulative probabilistic chances"){width=50%}

à gauche le probablité de gagner avec exactement n coup et à droite un historigrame du temps d'exécution en secondes.


### Implémentation

Notre stratégie probabiliste simple est implémenté dans le fichier `Player/HeuristicPlayer.py`. Avant chaque coup, pour chauque position que peut occuper un bateau et qui n'a pas déjà été joué, il ajoute 1
si le bateau peut être joué. Joue ensuite la case avec le nombre maximal.
