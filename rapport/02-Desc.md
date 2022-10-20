Description du code
====================

Le code de notre projet s'organise comme suit :

\dirtree{%
    .1 Bataille/.
    .2 rapport/.
    .2 src/.
        .3 data/.
        .3 Game/.
            .4 {Bateau.py}.
            .4 {Engine.py}.
            .4 {EngineStats.py}.
        .3 Player/.
            .4 {AbstractPlayer.py}.
            .4 {HeuristicPlayer.py}.
            .4 {HumanPlayer.py}.
            .4 {MCPlayer.py}.
            .4 {ProbPlayer.py}.
            .4 {RandomPlayer.py}.
        .3 utils/.
            .4 {constants.py}.
    .2 {main.py}.
    .2 {partie4.py}.
}

Le dossier `rapport/` est le dossier qui contient tous les fichiers qui constituent le présent rapport.

Le dossier `src/` contient l'essentiel du code et de nos différentes simulations. 

Le fichier `main.py` permet d'exécuter le code. Pour lancer le programe il faut se déplacer dans `src`avec `cd src/` et ensuite lancer `main.py` avec `python main.py`.

Le dossier `data/` contient différentes données telles que les résultats des joueurs, des images ou des ressources nécessaires à la bonne excécution du programme.

Le dossier `utils/` contient des fonctions utiles au projet. Il contient aussi, et surtout, le fichier `constants.py` qui possède toutes les configurations du jeu et les conventions de programmation. N'hésitez pas à y changer certains paramètres.

Le dossier `Game` contient le code de la partie logique du jeu. C'est une sorte de "game engine" (d'où le nom `Engine.py`).
`Engine.py` pour le jeu en lui même et `Bateau.py` pour le code de l'objet "Bateau" qui nous permet de simplifier et centraliser notre code pour le bateau.
`EngineStats.py` a  les mêmes caractéritiques que `Engine.py` mais avec quelques fonctions assez techniques en plus. C'est ici que vous trouverez certaines des fonctions requises dans le sujet.

Le fichier `partie4.py` contient le code nécessaire demandé pour la partie 4.

Nous avons fait le choix de connaître les bateaux en amont de leur placement, nous les avons alors indexés avec ce que nous appelons leur `type`.
C'est le numéro du bateau dans une liste triée par taille. Par défaux nous avons :

Bateau              | Taille    | Type
--------------------|-----------|----
Porte avion         | 5         | 1
Croiseur            | 4         | 2
Contre-torpilleurs  | 3         | 3
Sous-marin          | 3         | 4
Torpilleur          | 2         | 5
