from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.plant import Plant
from game.casting.player import Player
from game.casting.snail import Snail
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import Move_actors_action
from game.scripting.handle_collisions_action import Handle_collisions_action
from game.scripting.draw_actors_action import DrawActorsAction
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService



class Director:
    
    def __init__(self):
        self._cast = Cast()

        self._cast.add_actor("players",Player())

        self.keyboard_service = KeyboardService()
        self.video_service = VideoService()


        self._script = Script()
        self._script.add_action("input", ControlActorsAction(self.keyboard_service))
        self._script.add_action("update", Move_actors_action())
        self._script.add_action("update", Handle_collisions_action())
        self._script.add_action("output", DrawActorsAction(self.video_service))


        
        

    def run_game(self):

        self.video_service.open_window()
        while self.video_service.is_window_open():
            self._execute_actions("input", self._cast, self._script)
            self._execute_actions("update", self._cast, self._script)
            self._execute_actions("output", self._cast, self._script)
        self.video_service.close_window()
    
    def _execute_actions(self, group, cast, script):
        """Calls execute for each action in the given group.
        
        Args:
            group (string): The action group name.
            cast (Cast): The cast of actors.
            script (Script): The script of actions.
        """
        actions = script.get_actions(group)    
        for action in actions:
            action.execute(cast, script)   