from pyray import Image
from constants import *
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.plant import Plant
from game.casting.player import Player
from game.casting.snail import Snail
from game.casting.text_bar import Text_bar
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import Move_actors_action
from game.scripting.handle_collisions_action import Handle_collisions_action
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.draw_flowers_action import DrawFlowersAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.end_drawing_action import EndDrawingAction

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.tile import Tile
from game.casting.rose import Rose

import raylib








class Director:
    
    def __init__(self):
        self._cast = Cast()

        self.load_game()
        
        self._is_game_over = False

        self.keyboard_service = KeyboardService()
        self.video_service = VideoService()
        
        
        self._script = Script()
        self._script.add_action("input", ControlActorsAction(self.keyboard_service))
        self._script.add_action("update", Move_actors_action())
        self._script.add_action("update", Handle_collisions_action(self))
        self._script.add_action("output", StartDrawingAction(self.video_service))
        self._script.add_action("output", DrawActorsAction(self.video_service))
        self._script.add_action("output", DrawFlowersAction(self.video_service))
        self._script.add_action("output", EndDrawingAction(self.video_service))


        
        

    def run_game(self):

        self.video_service.open_window()
        self.video_service.load_textures()
        self.video_service.load_fonts()


        while self.video_service.is_window_open():
            
            self._execute_actions("input", self._cast, self._script)
            self._execute_actions("update", self._cast, self._script)
            self._execute_actions("output", self._cast, self._script)

        self.video_service.unload_fonts()
        self.video_service.unload_textures()

        
        self.save_game()

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

    def game_over(self):
        self._is_game_over = True

    def save_game(self):
        with open(SAVE_FILE,'w') as save_file:
            if not self._is_game_over:
                actors = self._cast.get_all_actors()
                for actor in actors:
                    
                    save_file.write(actor.create_save()+'\n')
    
    def load_game(self):
        try:
            with open(SAVE_FILE,'r') as save_file:
                actors = save_file.readlines()
                if len(actors) >2:
                    for actor in actors:
                        if len(actor) >1:
                            data = actor.split(',')
                            if data[0] == 'Player':
                                instance = Player()
                                self._cast.add_actor("players",instance)

                            if data[0] == 'Snail':
                                instance = Snail(self._cast.get_first_actor("players"))
                                self._cast.add_actor("snails",instance)
                                
                            if data[0] == 'Rose':
                                instance = Rose()
                                self._cast.add_actor("flowers",instance)
                                
                            if data[0] == 'Text_bar':
                                instance = Text_bar()
                                self._cast.add_actor("text_bars",instance)
                                pass
                            data.pop(0)
                            instance.load_save(data)
                else:
                    self._cast.add_actor("players",Player())
                    self._cast.add_actor("snails",Snail(self._cast.get_first_actor("players")))

                    self._cast.add_actor("text_bars",Text_bar("Age:",Tile(1,0)))
                    self._cast.add_actor("text_bars",Text_bar("Salt: ",Tile(1,2)))

                    self._cast.add_actor(FLOWER_GROUP,Rose())
        except:
            print("something is wrong with the save file!")
            
            