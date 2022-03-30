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
        """This function moves the snail object toward the point passed in."""
        
        target = self._player.get_position()
        # my_x = self._position.get_tiled_x()
        # that_x = target.get_tiled_x()
        # my_y = self._position.get_tiled_y()
        # that_y = target.get_tiled_y()

        # print(that_x > my_x)
        change = self._position < target
        self._position += change * SNAIL_MOVEMENT_RATE
        # my_x += .05 if that_x > my_x else -.05
        # my_y += .05 if that_y > my_y else -.05
        # self._position = Tile((my_x),(my_y))

