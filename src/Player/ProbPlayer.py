import numpy as np
import numpy.ma as ma
from random import randrange

from Game.EngineStats import EngineStats
from utils.constants import COULE_F, GEN_MC, MAX_GEN, MAX_IT
from utils.types import Pos, PosList
from .AbstractPlayer import AbstractPlayer


class ProbPlayer(AbstractPlayer):
    pass