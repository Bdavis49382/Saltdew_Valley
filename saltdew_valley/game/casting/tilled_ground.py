from game.casting.actor import Actor
from constants import TILLED_GROUND
class Tilled_ground(Actor):

    def __init__(self,position):
        super().__init__()
        self._texture = TILLED_GROUND
        self._position = position