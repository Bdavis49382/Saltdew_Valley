from game.scripting.action import Action
from game.services.mouse_service import MouseService
from constants import REACH
from constants import HOTBAR_GROUP
class Handle_clicks_action(Action):

    def __init__(self,mouse_service) -> None:
        self._mouse_service = mouse_service
        
        
        

    def execute(self, cast, script):
        tile = self._mouse_service.get_tiled_coordinates()
        
        player = cast.get_first_actor("players")
        hotbar = cast.get_first_actor(HOTBAR_GROUP)
        index = hotbar.get_index()
        actors = cast.get_all_actors()
        player_tile = player.get_position()
        dif_x = abs(tile.get_tiled_x() - player_tile.get_tiled_x())
        dif_y = abs(tile.get_tiled_y() - player_tile.get_tiled_y())
        
        if dif_x <= REACH and dif_y <= REACH and self._mouse_service.is_button_pressed("left"):
            item = hotbar.get_slots()[index]
            if item.can_interact(cast,tile):

                item.interact_with(cast,tile)
        
        