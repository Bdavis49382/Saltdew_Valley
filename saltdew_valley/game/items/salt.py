from game.items.item import Item
from constants import SALT
from game.casting.placed_salt import Placed_salt
class Salt(Item):

    def __init__(self) -> None:
        super().__init__()
        self._texture = SALT
    
    def can_interact(self, cast, tile):
        for actor in cast.get_all_actors():
            if actor.get_position().equals(tile) and type(actor) == type(Placed_salt(tile)):
                return False
        return True

    def interact_with(self, cast, tile):
        cost = 200
        enough_money = cast.get_first_actor("players").get_salt()>=cost 
        if enough_money:
            cast.get_first_actor("players").spend(cost)
            cast.add_actor("salt",Placed_salt(tile))

    def get_description(self):
        return "Salt: Cost: 200. Place on the ground to deter snails or speed plant growth by 2x"