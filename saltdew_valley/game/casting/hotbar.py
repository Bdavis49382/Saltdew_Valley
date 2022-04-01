from game.casting.actor import Actor
from constants import *
from game.shared.point import Point
from game.items.hoe import Hoe
from game.items.scythe import Scythe
from game.items.seed import Seed
from game.shared.tile import Tile
from game.items.watering_can import Watering_can
class Hotbar(Actor):
    """The only inventory the player has, it goes on the bottom of the screen and has slots with items in them
    
        Attributes:
        _slots(Slot[]): A list of slots with or without items in them
    """
    def __init__(self) -> None:
        super().__init__()
        self._texture = HOTBAR
        self._position = Point(HOTBAR_X,HOTBAR_Y)
        self._index = 0
        self._slots = [Hoe(),Scythe(),Watering_can(),Seed("Rose")]

    def get_slots(self):
        return self._slots

    def get_index(self):
        return self._index
    
    def set_index(self, index):
        self._index = index

    def create_save(self):
        data_string = f'Hotbar,{self._position.get_tiled_x()},{self._position.get_tiled_y()}'
        return data_string

    def load_save(self, data):
        self._position = Tile(float(data[0]),float(data[1]))
        