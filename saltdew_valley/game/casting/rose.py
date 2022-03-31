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
    
    def create_save(self):
        data_string = f'Rose,{self._position.get_tiled_x()},{self._position.get_tiled_y()},{self._animation.get_index()}'
        return data_string
    
    def load_save(self, data):
        self._position = Tile(float(data[0]),float(data[1]))
        self._animation.set_index(int(data[2]))

