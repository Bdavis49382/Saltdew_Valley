
from constants import *
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.tile import Tile


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.
    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """Executes the control actors action.
        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        
        
        player = cast.get_first_actor("players")

            # left
        if self._keyboard_service.is_key_down('a'):
            player.set_velocity(Tile(-.5, 0))
        
            # right
        elif self._keyboard_service.is_key_down('d'):
            player.set_velocity(Tile(.5, 0))

            # up
        elif self._keyboard_service.is_key_down('w'):
            player.set_velocity(Tile(0, -.5))

            # down
        elif self._keyboard_service.is_key_down('s'):
            player.set_velocity(Tile(0,.5))

        else:
            player.set_velocity(Tile(0,0))



