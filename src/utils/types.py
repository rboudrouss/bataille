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
        "NbWin": str
    }
)
