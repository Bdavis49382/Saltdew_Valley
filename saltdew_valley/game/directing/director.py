from pyray import Image
from constants import *
from game.casting.cast import Cast
from game.casting.actor import Actor
from game.casting.player import Player
from game.casting.snail import Snail
from game.casting.text_bar import Text_bar
from game.casting.tilled_ground import Tilled_ground
from game.casting.flower import Flower
from game.items.seed import Seed
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import Move_actors_action
from game.scripting.handle_collisions_action import Handle_collisions_action
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.draw_flowers_action import DrawFlowersAction
from game.scripting.start_drawing_action import StartDrawingAction
from game.scripting.end_drawing_action import EndDrawingAction
from game.scripting.draw_mouse_box_action import Draw_mouse_box_action
from game.scripting.play_sound_action import PlaySoundAction
from game.casting.hotbar import Hotbar
from game.services.audio_service import AudioService
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.services.mouse_service import MouseService
from game.shared.tile import Tile
from game.casting.sound import Sound


import raylib

from game.scripting.handle_clicks_action import Handle_clicks_action

from game.casting.placed_salt import Placed_salt









class Director:
    
    def __init__(self):
        self._cast = Cast()

        self.load_game()
        
        
        self._is_game_over = False

        self.keyboard_service = KeyboardService()
        self.video_service = VideoService()
        self.mouse_service = MouseService()
        self.audio_service = AudioService()
        
        self._script = Script()
        self._script.add_action("input", ControlActorsAction(self.keyboard_service,self.mouse_service))
        self._script.add_action("update", Move_actors_action())
        self._script.add_action("update", Handle_collisions_action(self))
        self._script.add_action("update",Handle_clicks_action(self.mouse_service))
        self._script.add_action("output", StartDrawingAction(self.video_service))
        self._script.add_action("output", DrawActorsAction(self.video_service))
        self._script.add_action("output",Draw_mouse_box_action(self.video_service,self.mouse_service,self._cast))
        self._script.add_action("output", DrawFlowersAction(self.video_service))
        self._script.add_action("output", EndDrawingAction(self.video_service))
        #self._script.add_action("output",PlaySoundAction(self.audio_service,BACKGROUND_MUSIC))


        
        

    def run_game(self):

        self.video_service.open_window()
        self.video_service.load_textures()
        self.video_service.load_fonts()

        self.audio_service.load_sounds()
        PlaySoundAction(self.audio_service, BACKGROUND_MUSIC).execute(self._cast,self._script)

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
        
            with open(SAVE_FILE,'r') as save_file:
                actors = save_file.readlines()
                if len(actors)>4 and SAVE_GAME_MODE:
                    
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
                                instance = Flower(Tile(0,0),Seed("Rose"))
                                self._cast.add_actor("flowers",instance)
                            
                            if data[0] == "Lavender":
                                instance = Flower(Tile(0,0),Seed("Lavender"))
                                self._cast.add_actor("flowers",instance)
                            
                            if data[0] == "Tulip":
                                instance = Flower(Tile(0,0),Seed("Tulip"))
                                self._cast.add_actor("flowers",instance)
                            
                            if data[0] == "Violet":
                                instance = Flower(Tile(0,0),Seed("Violet"))
                                self._cast.add_actor("flowers",instance)
                                
                            if data[0] == "Poppy":
                                instance = Flower(Tile(0,0),Seed("Poppy"))
                                self._cast.add_actor("flowers",instance)

                            if data[0] == 'Text_bar':
                                instance = Text_bar()
                                self._cast.add_actor("text_bars",instance)
                                
                            if data[0] == 'Hotbar':
                                instance = Hotbar()
                                self._cast.add_actor(HOTBAR_GROUP,instance)

                            if data[0] == 'Salt':
                                instance = Placed_salt(Tile(0,0))
                                self._cast.add_actor("salt",instance)

                            if data[0] == "Tilled_ground":
                                instance = Tilled_ground(Tile(0,0))
                                self._cast.add_actor("tilled_ground",instance)
                            data.pop(0)
                            instance.load_save(data)
                else:
                    self._cast.add_actor("players",Player())
                    self._cast.add_actor("snails",Snail(self._cast.get_first_actor("players")))

                    self._cast.add_actor("text_bars",Text_bar("Age:",Tile(1,0)))
                    self._cast.add_actor("text_bars",Text_bar("Salt: ",Tile(1,2)))

                    
                    self._cast.add_actor(HOTBAR_GROUP, Hotbar())
                    

                    

        
            
            