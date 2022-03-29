from constants import *

from game.casting.actor import Actor
from game.shared.tile import Tile

class Player(Actor):
    """The farmer which can move around, farm, trade, and attempt to escape the inevitable snail
    
        The player's responsibility is to show where the player is on the screen, and allow the player to interact with the world

        Attributes:
            _position(Point): the coordinates on the map where the player is
            _velocity(Point): the speed and direction of the player
            _texture(String): the key to the image/animation of the player in the video_service's texture dictionary
            
    """
    def __init__(self):
        super().__init__()
        self._texture = FARMER
        self._position = Tile(FARMER_STARTING_X,FARMER_STARTING_Y)
        self._velocity = Tile(.5,0)