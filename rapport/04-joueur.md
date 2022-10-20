Modélisation probabiliste du jeu
===========

Nous allons maintenant modéliser différentes stratégies de jeu que nous analyserons. 

## Implémentation des Joueurs

Tout les joueurs doivent hériter de la classe `AbstractPlayer` et override les fonctions `play`, `reset`, et `name` pour être considiré comme Joueur.
La class `AbstractPlayer` s'occupe d'énormement de chose, tel que les intéractions avec le game engine, détecter si le jeu et fini ou pas, gérer le plateau qui récapitule toute la vision qu'à le joueur pour l'instant et surtout la boucle principale.
En clair elle regroupe tout le code centrale et nécessaire à un joueur.


## Joueur Aléatoire

### Étude probabilistique

Soit notre grille contenant $N=100$ cases, $m=17$ le nombre de cases occupé paré. La probabilité que le jeu se termine en n action est alors :

$$
P(n) = \frac{C^{N-m}_{n-m}}{C^n_100}
$$

avec $17 \leq n \leq 100$. Ce qui nous donne comme espérence $\approx 95.4$. Et c'est bien ce que l'on observe :

![Probabilité de gagner avec au plus n coup](./rapport/img/Random_win.png "cumulative random chances"){width=60%}

### Implémentation

Notre stratégie aléatoire est implémenté dans le fichier `Player/RandomPlayer.py` avec une fonction `play` qui contient l'algorithme suivant :

- choisi aléatoirement une position dans l'ensemble des coups non-joué
- Joue cette position et la retire de l'ensemble

