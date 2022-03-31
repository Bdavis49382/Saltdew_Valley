from game.scripting.action import Action
from game.services.mouse_service import MouseService
class Handle_clicks_action(Action):

    def __init__(self,mouse_service) -> None:
        self._mouse_service = mouse_service

    def execute(self, cast, script):
        mouse = self._mouse_service.get_tiled_coordinates()
        viable = True
        