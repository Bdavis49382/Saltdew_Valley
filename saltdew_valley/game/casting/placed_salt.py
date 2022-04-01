from game.casting.actor import Actor
from game.shared.tile import Tile
from constants import PLACED_SALT
class Placed_salt(Actor):
    """A piece of salt on the ground, it's there to fight off snails, and goes away when a player walks over it

    
    """
    def __init__(self,position):
        super().__init__()
        self._position = position
        self._texture = PLACED_SALT
        
    def create_save(self):
        data_string = f'Salt,{self._position.get_tiled_x()},{self._position.get_tiled_y()}'
        return data_string

    def load_save(self, data):
        self._position = Tile(float(data[0]),float(data[1]))