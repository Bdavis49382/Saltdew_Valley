from game.casting.actor import Actor
from constants import *
from game.shared.point import Point
from game.shared.tile import Tile

class Snail(Actor):
    """A small, evil actor that follows the player around for the entire game"""
    def __init__(self,player):
        super().__init__()
        self._texture = SNAIL
        self._position = Point(SNAIL_STARTING_X,SNAIL_STARTING_Y)
        self._velocity = Tile(0,0)
        self._player = player
   
    def move_next(self):
        """This function moves the snail object toward the point passed in."""
        point = self._player.get_position()
        my_x = self._position.get_x()
        that_x = point.get_x()*CELL_SIZE
        my_y = self._position.get_y()
        that_y = point.get_y()*CELL_SIZE
        my_y += .25 if that_x > my_x else -.25
        my_y += .25 if that_y > my_y else -.25
        self._position = Point((my_x),(my_y))

