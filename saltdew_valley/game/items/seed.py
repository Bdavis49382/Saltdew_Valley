from game.items.tool import Tool
from game.casting.rose import Rose
from constants import *
from game.casting.tilled_ground import Tilled_ground
from game.shared.tile import Tile
from game.casting.flower import Flower
class Seed(Tool):
    """An item that can be placed to create a plant
            
    """
    
    def __init__(self,type) -> None:
        super().__init__()
        self._type = type
        if type == "Rose":
            self._texture = ROSES[0]
            self._cost = 10

        
    
    def can_interact(self, cast, tile):
        self._player = cast.get_first_actor("players")
        output = False
        sharers = []
        for actor in cast.get_all_actors():
            same_position = actor.get_position().equals(tile)
            ground_is_tilled = type(actor) == type(Tilled_ground(Tile(0,0)))
            enough_money = self._player.get_salt()>=self._cost
            if  same_position and ground_is_tilled and enough_money:
                output = True
            
            if same_position:
                sharers.append(actor)

        for actor in sharers:
            if type(actor) == type[Flower]:
                output = False

        return output


    def interact_with(self, cast, tile):
        self._player.spend(self._cost)
        if self._type == "Rose":
            cast.add_actor(FLOWER_GROUP,Rose(tile))
        