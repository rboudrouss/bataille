from typing import TypedDict


Pos = tuple[int, int]  # | list[int]
PosList = list[Pos]
MessDict = TypedDict(
    "MessDict",
    {
        "win": str,
        "couleCase": str,
        "touche": str,
        "askInput": str,
        "rate": str,
        "playFinished": str,
        "start": str,
        "showState": str,
        "RandomNbWin": str
    }
)


DIM_PLATEAU = (10, 10)
LEN_B = [5, 4, 3, 3, 2]
MAX_IT = 100
DEBUG = True
