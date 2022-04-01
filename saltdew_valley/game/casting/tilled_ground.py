from game.casting.actor import Actor
from constants import TILLED_GROUND
from game.shared.tile import Tile
class Tilled_ground(Actor):

    def __init__(self,position):
        super().__init__()
        self._texture = TILLED_GROUND
        self._position = position

    def create_save(self):
        data_string = f'Tilled_ground,{self._position.get_tiled_x()},{self._position.get_tiled_y()}'
        return data_string

    def load_save(self, data):
        self._position = Tile(float(data[0]),float(data[1]))
        