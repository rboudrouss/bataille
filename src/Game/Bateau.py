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

            self.poss: PosList = []
            for i in range(length):
                if direction:
                    self.poss.append((self.origine[0], self.origine[1]+i))
                else:
                    self.poss.append((self.origine[0]+i, self.origine[1]))

    def touche(self, pos: Pos) -> None:
        assert pos in self.poss

        self.damage.append(pos)

    def est_coule(self) -> bool:
        return set(self.poss) == set(self.damage)

    def get_pos(self) -> PosList | None:
        if self.est_coule():
            return self.poss
        return None
