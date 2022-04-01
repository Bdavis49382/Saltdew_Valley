
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
        hotbar = cast.get_first_actor("hotbar")

        if self._keyboard_service.is_key_down('1'):
            hotbar.set_index(0)
        if self._keyboard_service.is_key_down('2'):
            hotbar.set_index(1)
        if self._keyboard_service.is_key_down('3'):
            hotbar.set_index(2)
        if self._keyboard_service.is_key_down('4'):
            hotbar.set_index(3)
        if self._keyboard_service.is_key_down('5'):
            hotbar.set_index(4)
        if self._keyboard_service.is_key_down('6'):
            hotbar.set_index(5)
        if self._keyboard_service.is_key_down('7'):
            hotbar.set_index(6)
        if self._keyboard_service.is_key_down('8'):
            hotbar.set_index(7)
        if self._keyboard_service.is_key_down('9'):
            hotbar.set_index(8)
        

        max_speed = player.calculate_max_speed()

            # left
        if self._keyboard_service.is_key_down('a'):
            player.set_velocity(Tile(-max_speed, 0))
        
            # right
        elif self._keyboard_service.is_key_down('d'):
            player.set_velocity(Tile(max_speed, 0))

            # up
        elif self._keyboard_service.is_key_down('w'):
            player.set_velocity(Tile(0, -max_speed))

            # down
        elif self._keyboard_service.is_key_down('s'):
            player.set_velocity(Tile(0,max_speed))

        else:
            player.set_velocity(Tile(0,0))



