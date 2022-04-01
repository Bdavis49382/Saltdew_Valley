from game.casting.actor import Actor
from game.casting.animation import Animation
from constants import *
from game.shared.tile import Tile
class Flower(Actor):

    def __init__(self,position,seed):
        super().__init__()
        self._type = seed.get_type()
        self._aging = seed.get_aging()
        self._price = seed.get_price()
        
        if self._type == "Rose":
            self._animation = Animation(ROSES,self._aging,0)
            

        elif self._type == "Lavender":
            self._animation = Animation(LAVENDER,self._aging,0)
            

        elif self._type == "Tulip":
            self._animation = Animation(TULIPS,self._aging,0)
            

        elif self._type == "Violet":
            self._animation = Animation(VIOLETS,self._aging,0)
            

        elif self._type == "Poppy":
            self._animation = Animation(POPPY,self._aging,0)
        
        

        self._position = position

    def get_price(self):
        return self._price
    
    def get_animation(self):
        return self._animation
    
    def grow(self):
        self._animation.add_frames(100)
    
    

    def create_save(self):
        data_string = f'{self._type},{self._position.get_tiled_x()},{self._position.get_tiled_y()},{self._animation.get_index()}'
        return data_string
    
    def load_save(self, data):
        self._position = Tile(float(data[0]),float(data[1]))
        self._animation.set_index(int(data[2]))