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
        self._velocity = Tile(0,0)
        self._age = 20
        self._clock = 0
        self._salt = 200
    
    def move_next(self):
        super().move_next()
        self._clock+=1
        if(self._clock%FAST_AGING==0):
            self._age+=1
        
    def calculate_max_speed(self):
        if self._age<40:
            return .5
        elif self._age<50:
            return .4
        elif self._age<60:
            return .3
        return .25/(.2*(self._age-55))

    def get_age(self):
        return self._age
    
    def set_age(self,age):
        self._age = age
    
    def get_salt(self):
        return self._salt
    
    def set_salt(self,salt):
        self._salt = salt