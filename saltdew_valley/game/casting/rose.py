from game.casting.actor import Actor
from game.casting.animation import Animation
from constants import *
from game.shared.tile import Tile

class Rose(Actor):

    def __init__(self):
        super().__init__()
        self._animation = Animation(ROSES,NORMAL_AGING,0)
        self._growth_stage = 0
        self._position = (Tile(10,10))
    
    def get_animation(self):
        return self._animation

