from game.items.tool import Tool
from constants import WATERING_CAN
from game.casting.rose import Rose
from game.shared.tile import Tile

class Watering_can(Tool):

    def __init__(self) -> None:
        super().__init__()
        self._texture = WATERING_CAN
        
    
    def can_interact(self, cast, tile):
        for actor in cast.get_all_actors():
            if actor.get_position().equals(tile) and type(actor) == type(Rose(Tile(0,0))):
                if actor.get_animation().get_index() != 5:
                    self._target = actor
                    return True

    def interact_with(self, cast, tile):
        self._target.grow()
        