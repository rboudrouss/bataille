## Joueur Probabiliste Simple

Essayons cette fois-ci de prendre en compte l'information "coulé" qui nous donne les cases du bateau coulé.
Nous pouvons donc déduire la liste des bateaux coulés et celle de ceux restants.

### Étude probabilistique

La stratégie probabilist simple prend environ 57 coups en moyenne pour terminer. Cependant on constate qu'elle prend beaucoup plus de temps à s'exécuter contrairement aux deux autres stratégies précédentes (en moyenne 1.7 secondes contre significativement moins qu'une seconde) car elle nécessite beaucoup plus de calculs en amont.


![Probabilité de gagner avec exactement n coup](./rapport/img/Probabilistic_winNC.png "cumulative probabilistic chances"){width=50%}
![Probabilité de gagner avec exactement n coup](./rapport/img/Probabilistic_time.png "cumulative probabilistic chances"){width=50%}

à gauche le probablité de gagner avec exactement n coups et à droite un historigramme du temps d'exécution en secondes.


### Implémentation

Notre stratégie probabiliste simple est implémentée dans le fichier `Player/HeuristicPlayer.py`. Avant chaque coup, pour chaque position que peut occuper un bateau et qui n'a pas déjà été jouée, il ajoute 1
si le bateau peut être joué. Joue ensuite la case avec le nombre maximal.
