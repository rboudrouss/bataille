from utils.constants import DIR_L, HOR_D, MIN_LB, VER_D
from utils.types import Pos, PosList
from utils.helpers import str_PosL


class Bateau:

    def __init__(
        self,
        posL: PosList | None = None,
        length: int | None = None,
        direction: int | None = None,
        pos: Pos | None = None,
        name: str | None = None
    ):
        """
        si un posL est attribué, on force les valeurs à travers les listes de coordonées
        sinon on calcul les listes des coordonnées à partir des valeurs renseignés

        pos c'est (y,x)
        direction : 0 verical, 1 horizontal
        """
        self.damage: PosList = []

        if not posL:
            assert length and length >= MIN_LB and direction in DIR_L and pos

            self.length: int = length
            self.direction = direction
            self.origine = pos
            self.name = name if name else str(length) + " " + str(pos)

            self.poss: PosList = self.generate_posL(pos, length, direction)

    def touche(self, pos: Pos) -> None:
        assert pos in self.poss

        self.damage.append(pos)

    def est_coule(self) -> bool:
        return set(self.poss) == set(self.damage)

    def get_pos(self) -> PosList | None:
        if self.est_coule():
            return self.poss
        return None

    @staticmethod
    def generate_posL(pos: Pos, length: int, direction: int) -> PosList:
        posl: PosList = []
        for i in range(length):
            if direction:
                posl.append((pos[0], pos[1]+i))
            else:
                posl.append((pos[0]+i, pos[1]))
        return posl
