from game.casting.actor import Actor
from game.casting.animation import Animation
from constants import *
from game.shared.tile import Tile

class Rose(Actor):

    def __init__(self):
        super().__init__()
        self._animation = Animation(ROSES,NORMAL_AGING,NORMAL_AGING*6)
        self._growth_stage = 0
        self._position = (Tile(1,1))
