from game.scripting.action import Action
from constants import *
class Draw_mouse_box_action(Action):
    def __init__(self,video_service,mouse_service,cast) -> None:
        self._video_service = video_service
        self._mouse_service = mouse_service
        self._player = cast.get_first_actor("players")
    
    def execute(self, cast, script):
        tile = self._mouse_service.get_tiled_coordinates()
        player_tile = self._player.get_position()
        dif_x = abs(tile.get_tiled_x() - player_tile.get_tiled_x())
        dif_y = abs(tile.get_tiled_y() - player_tile.get_tiled_y())
        if dif_x <= REACH and dif_y <= REACH:
            self._video_service.draw_mouse_box(tile)
        