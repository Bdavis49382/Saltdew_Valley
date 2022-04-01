from game.items.item import Item

from constants import *
from game.casting.tilled_ground import Tilled_ground
from game.shared.tile import Tile
from game.casting.flower import Flower
from game.casting.placed_salt import Placed_salt

class Seed(Item):
    """An item that can be placed to create a plant
            
    """
    
    def __init__(self,type) -> None:
        super().__init__()
        self._type = type
        self._aging = 0
        self._cost = 0
        self._price = 0
        self._fertilized = False
        if type == "Rose":
            self._texture = ROSES[0]
            self._aging = NORMAL_AGING*(2/3)
            self._cost = 10
            self._price = 30

        elif type == "Lavender":
            self._texture = LAVENDER[0]
            self._aging = NORMAL_AGING
            self._cost = 90
            self._price = 200

        elif type == "Tulip":
            self._texture = TULIPS[0]
            self._aging = NORMAL_AGING * 1.5
            self._cost = 600
            self._price = 1500

        elif type == "Violet":
            self._texture = VIOLETS[0]
            self._aging = NORMAL_AGING * 2.25
            self._cost = 3600
            self._price = 9000

        elif type == "Poppy":
            self._texture = POPPY[0]
            self._aging = NORMAL_AGING *3.375
            self._cost = 21600
            self._price = 54000

    def get_type(self):
        return self._type

    def get_price(self):
        return self._price

    def get_aging(self):
        return self._aging

    
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
            if type(actor) == type(Flower(Tile(0,0),self)):
                output = False
            if type(actor) == type(Placed_salt(Tile(0,0))):
                self._fertilized = True

        return output


    def interact_with(self, cast, tile):
        self._player.spend(self._cost)
        new_flower = Flower(tile,self)
        if self._fertilized:
            new_flower.get_animation().half_rate()
        cast.add_actor(FLOWER_GROUP,new_flower)
    
    def get_description(self):
        return f"{self._type}: Costs: {self._cost}. Grows in {(self._aging/NORMAL_AGING):.1f} years. Sells for {self._price:.0f}."
        
        