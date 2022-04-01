from game.items.tool import Tool
from constants import SCYTHE
from game.casting.rose import Rose
from game.shared.tile import Tile

class Scythe(Tool):

    def __init__(self) -> None:
        super().__init__()
        self._texture = SCYTHE
        self._target = Rose(Tile(0,0))
    
    def can_interact(self, cast, tile):
        for actor in cast.get_all_actors():
            if actor.get_position().equals(tile) and type(actor) == type(Rose(Tile(0,0))):
                if actor.get_animation().get_index() == 5:
                    self._target = actor
                    return True

    def interact_with(self, cast, tile):
        cast.remove_actor("flowers",self._target)
        cast.get_first_actor("players").earn(self._target.get_price())