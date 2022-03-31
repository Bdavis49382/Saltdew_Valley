from game.items.tool import Tool
from constants import HOE
from game.casting.tilled_ground import Tilled_ground
class Hoe(Tool):

    def __init__(self) -> None:
        super().__init__()
        self._texture = HOE
    
    def interact_with(self, cast, tile):
        cast.add_actor("tilled_ground",Tilled_ground(tile))
