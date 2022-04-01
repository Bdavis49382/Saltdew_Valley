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
        self._salt = 20
        self._clock = 0
    
    def move_next(self):
        super().move_next()
        self._clock+=1
        if(self._clock%NORMAL_AGING==0):
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

    def earn(self,salt):
        self._salt += salt
    
    def spend(self,salt):
        self._salt -= salt
        
    def create_save(self):
        data_string = f'Player,{self._position.get_tiled_x()},{self._position.get_tiled_y()},{self._age},{self._salt},{self._clock}'
        return data_string

    def load_save(self, data):
        self._position = Tile(float(data[0]),float(data[1]))
        self._age = int(data[2])
        self._salt = int(data[3])
        self._clock = float(data[4])