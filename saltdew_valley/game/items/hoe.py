from game.items.item import Item
from constants import HOE
from game.casting.tilled_ground import Tilled_ground
class Hoe(Item):

    def __init__(self) -> None:
        super().__init__()
        self._texture = HOE
    
    def can_interact(self, cast, tile):
        for actor in cast.get_all_actors():
            if actor.get_position().equals(tile) and type(actor) == type(Tilled_ground(tile)):
                return False
        return True

    def interact_with(self, cast, tile):
        cast.add_actor("tilled_ground",Tilled_ground(tile))

    def get_description(self):
        return "Hoe: Tills ground"
