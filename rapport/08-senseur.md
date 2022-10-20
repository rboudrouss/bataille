Senseur Imparfait
=================

## Introduction

Nous essayons d'implémenter un algorithme d'approche bayésienne pour la recherche d'un objet perdu en mer avec un senseur de fiabilité $p_s < 1$. 

## Étude

Introduisont 4 variables :

- $y_i \in {0,1}$ : est la varialbe aléatoire qui vaut 1 pour la case i qui contient l'objet qu'on cherche et 0 dans les autres.

- $z_i \in {0,1}$ : est la variable aléatoire qui vaut 1 en cas de detection et 0 sinon

- $\pi_i \in [0,1]$ : la probabilité à priori de la contenance de l'objet recherché

- $p_s \in [0,1]$ : la probabilité que le senseur détecte l'objet.


Nous avons alors :
$$
p(z_i = 1 | y_i = 1) = ps 
$$$$
p(z_i = 0 | y_i = 0) = 1
$$$$
p(z_i = 0 | y_i = 1) = 1 - ps
$$$$
p(z_i = 1 | y_i = 0) = 0 
$$

Nous pouvons donc déduire que les deux événement sont indépendant l'un de l'autre. Alors la probabilité de l'événement où le senseur ne détecte pas l'objet présent dans une case $k$ est $\pi_k (1 - p_s)$.

Dans ce cas il suffie de changer la valeur de $\pi_k$, nous proposons alors l'algorithme suivant :

- On choisi la cellule avec la plus grande valeur de $\pi_i$

- En cas de detection, le programme se termine.

- Sinon, la valeur de $\pi_i$ devient $\pi_i (1-p_s)$ et on reprends le programme de l'étape 1.

Le résultat de l'exécution de notre algorithme se trouve dans la *Figure 3*. Pour le code, il se trouve dans le fichier `src/partie4.py`


![probabilité de détection avec exactement n étapes](./rapport/img/SS_prop.jpg "chances of detection"){width=50%}