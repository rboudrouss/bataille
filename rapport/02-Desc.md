Description du code
====================

Le code de notre proje s'organise comme suit :
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
}

Le dossier `rapport/` est le dossier qui contient tout les fichiers qui ont été nécessaires à la création du présent rapport.

Le dossier `src/` contient l'essentiel du code et de no différentes simulation. 

Le fichier `main.py` est le fichier qui permet d'executer le code. Pour lancer le programe il faut `cd src/` et ensuite `python main.py`.

Le dossier `data/` contient toutes sortes d'informations sur les différences de données telque les résultats des joueurs, des images ou des données nécessaire à la bonne excécution du programme.

Le dossier `utils/` contient toutes sorte de fonctions qui ont été utiles au projet. Mais il contient aussi et surtout le fichier `constants.py` qui possède toutes les configurations du jeu et le convention de programmation. Hésitez pas à changer des paramètres dessus.

Le dossier `Game` contient les codes de la partie logique du jeu. C'est un sorte de "game engine" (d'où le nom `Engine.py`).
`Engine.py` pour le jeu en lui même et `Bateau.py` pour le code de l'objet "Bateau" qui nous permet de facilité et centralisé notre code pour le bateau.
`EngineStats.py` a  les mêmes caractéritiques que `Engine.py` mais avec quelques fonctions assez techniques en plus. C'est ici que vous trouverais quelques une des fonctions demandés dans le sujet.