from game.items.item import Item
from constants import WATERING_CAN
from game.casting.flower import Flower
from game.shared.tile import Tile
from game.items.seed import Seed

class Watering_can(Item):

    def __init__(self) -> None:
        super().__init__()
        self._texture = WATERING_CAN
        
    
    def can_interact(self, cast, tile):
        for actor in cast.get_all_actors():

            if actor.get_position().equals(tile) and type(actor) == type(Flower(Tile(0,0),Seed("Blank"))):
                
                if actor.get_animation().get_index() != 5:
                    self._target = actor
                    return True

    def interact_with(self, cast, tile):
        self._target.grow()
    
    def get_description(self):
        return "Watering Can: Speeds up growth"
        