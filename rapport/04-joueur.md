Modélisation probabiliste du jeu
===========

Nous allons maintenant modéliser différentes stratégies de jeu que nous analyserons. 

## Implémentation des Joueurs

Tous les joueurs doivent hériter de la classe `AbstractPlayer` et override les fonctions `play`, `reset`, et `name` pour être considérés comme Joueur.
La classe `AbstractPlayer` s'occupe de plusieurs chose, telles que les interactions avec le game engine, détecter si le jeu est fini, gérer le plateau qui récapitule toute la vision qu'a le joueur à l'instant T et surtout la boucle principale.
En clair elle regroupe tout le code centrale et nécessaire à un joueur.


## Joueur Aléatoire

Le joueur aléatoire est sans doute la stratégie la plus naïve et la plus simple, mais jusqu'à quel point est-elle mauvaise ?

### Étude probabilistique

Soit notre grille contenant $N=100$ cases, $m=17$ le nombre de cases occupées. La probabilité que le jeu se termine en $n$ actions est alors :

$$
P(n) = \frac{C^{N-m}_{n-m}}{C^n_100}
$$

avec $17 \leq n \leq 100$. Ce qui nous donne comme espérence $\approx 95.4$. C'est bien ce que l'on observe sur la *Figure 1*.

![Probabilité pour le joueur aléatoire de gagner avec au plus n coup](./rapport/img/Random_win.png "cumulative random chances"){width=60%}

### Implémentation

Notre stratégie aléatoire est implémentée dans le fichier `Player/RandomPlayer.py` avec une fonction `play` qui contient l'algorithme suivant :

- choisir aléatoirement une position dans l'ensemble des coups non-joués
- jouer cette position et la retirer de l'ensemble

