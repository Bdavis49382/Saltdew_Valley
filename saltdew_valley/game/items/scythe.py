from game.items.item import Item
from constants import SCYTHE
from game.casting.flower import Flower
from game.shared.tile import Tile
from game.items.seed import Seed

class Scythe(Item):

    def __init__(self) -> None:
        super().__init__()
        self._texture = SCYTHE
        self._target = Flower(Tile(0,0),Seed("Blank"))
    
    def can_interact(self, cast, tile):
        for actor in cast.get_all_actors():
            
            if actor.get_position().equals(tile) and type(actor) == type(self._target):
                
                if actor.get_animation().get_index() == 5:
                    self._target = actor
                    return True

    def interact_with(self, cast, tile):
        
        cast.remove_actor("flowers",self._target)
        cast.get_first_actor("players").earn(self._target.get_price())
    
    def get_description(self):
        return "Scythe: Harvests fully cultivated plants"