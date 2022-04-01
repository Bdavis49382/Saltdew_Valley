from game.casting.flower import Flower
from game.casting.animation import Animation
from constants import *
from game.shared.tile import Tile

class Rose(Flower):

    def __init__(self,position):
        super().__init__(position)
        self._animation = Animation(ROSES,NORMAL_AGING,0)

        self._type = "Rose"
        self._price = 30


