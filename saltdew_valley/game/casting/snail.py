from game.casting.actor import Actor
from constants import *

from game.shared.tile import Tile

class Snail(Actor):
    """A small, evil actor that follows the player around for the entire game"""
    def __init__(self,player):
        super().__init__()
        self._texture = SNAIL
        self._position = Tile(SNAIL_STARTING_X,SNAIL_STARTING_Y)
        self._velocity = Tile(0,0)
        self._player = player
   
    def move_next(self):
        """This function moves the snail object toward the position of it's player."""
        
        target = self._player.get_position()
        # print("running snail.move_next()")
        # my_x = self._position.get_tiled_x()
        # that_x = target.get_tiled_x()
        # my_y = self._position.get_tiled_y()
        # that_y = target.get_tiled_y()

        # # print(that_x > my_x)
        change = self._position.compare_to(target) * SNAIL_MOVEMENT_RATE
        self._position += change
        # my_x += .05 if that_x > my_x else -.05
        # my_y += .05 if that_y > my_y else -.05
        #self._position = Tile((my_x),(my_y))

    def get_tiled_coordinates(self):
        position = self.get_position()
        x = position.get_x()-(position.get_x()%CELL_SIZE)
        y = position.get_y() - (position.get_y()%CELL_SIZE)
        return Tile(x/CELL_SIZE,y/CELL_SIZE)

    def set_position(self,tile):
        self._position = tile

    def create_save(self):
        data_string = f'Snail,{self._position.get_tiled_x()},{self._position.get_tiled_y()}'
        return data_string
    
    def load_save(self, data):
        self._position = Tile(float(data[0]),float(data[1]))

