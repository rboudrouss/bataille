from .types import Pos, PosList


def valid_posinput(inp: str) -> bool:
    """
    Vérifie que l'input de la position émie par l'humain est bien valide
    sous la force x,y ou (x,y)
    """
    inp = inp.replace(" ", "").replace("(", "").replace(")", "")
    return inp.count(",") == 1 and inp[:inp.index(",")].isdigit() and inp[inp.index(",")+1:].isdigit()


def convert_posinput(inp: str) -> Pos:
    """
    Converti un string sous la forme "x,y" ou "(x,y)" en un tuple (x,y) avec x et y des int
    """
    assert valid_posinput(inp)
    inp = inp.replace(" ", "").replace("(", "").replace(")", "")
    x, y = map(int, inp.split(","))
    return x, y


def str_PosL(posL: PosList) -> str:
    """
    convertie une liste de position en str
    """
    return ", ".join(map(lambda x: str((x[1], x[0])), posL))


def orderl(*l: int) -> list[int]:
    """
    returne une liste ordonnée des paramètres données
    """
    return list(sorted(list(l)))
