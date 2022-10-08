from utils.constants import Pos, PosList


class Bateau:

    def __init__(self, length: int, direction: int, pos: Pos, name: str = ""):
        """
        pos c'est (y,x)
        """
        self.length: int = length
        self.damage: PosList = []
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
