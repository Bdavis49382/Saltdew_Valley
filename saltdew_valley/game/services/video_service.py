import pyray
from constants import *
import time

class VideoService:
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    def __init__(self, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._textures = {}
        self._fonts = {}
        self._animations = {}

        self._debug = debug

    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    def draw_actor(self, actor, centered=False):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        texture = self._textures[actor.get_texture()]
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        
        position = pyray.Vector2(x,y)
        pyray.draw_texture_ex(texture,position,0,1,NO_TINT)
    
    def draw_flower(self, flower):
        animation = flower.get_animation()
        image = animation.next_image()
        texture = self._textures[image]
        x = flower.get_position().get_x()
        y = flower.get_position().get_y()
        
        position = pyray.Vector2(x,y)
        pyray.draw_texture_ex(texture,position,0,1,NO_TINT)
        
        
    def draw_actors(self, actors, centered=False):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        
        for actor in actors:
            self.draw_actor(actor, centered)

    def draw_text_bars(self,cast,text_bars):
        """Draws all the text from a list of text_bars"""

        for text_bar in text_bars:
            x = text_bar.get_position().get_x()
            y = text_bar.get_position().get_y()
            text = text_bar.get_text()
            if 'Age' in text:
                age = cast.get_first_actor("players").get_age()
                text_bar.set_text(f'Age: {age}')

            if 'Salt' in text:
                
                salt = cast.get_first_actor("players").get_salt()
                text_bar.set_text(f'Salt: {salt}')

            pyray.draw_text_ex(self._fonts[FONT_FILE], text_bar.get_text(), pyray.Vector2(x,y), FONT_LARGE, 0, BLACK_TINT)



    def draw_background(self):
        """Draws the background on the screen"""
        texture = self._textures[MAP]
        # texture = pyray.load_texture(MAP)
        position = pyray.Vector2(0,0)
        
        
        pyray.draw_texture_ex(texture,position,0,1,NO_TINT)
       
    
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        
        return not pyray.window_should_close()

    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        
        pyray.init_window( MAX_X,  MAX_Y,  CAPTION)
        pyray.set_target_fps( FRAME_RATE)

    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0,  MAX_Y,  CELL_SIZE):
            pyray.draw_line(0, y,  MAX_X, y, pyray.GRAY)
            
        for x in range(0,  MAX_X,  CELL_SIZE):
            pyray.draw_line(x, 0, x,  MAX_Y, pyray.GRAY)
    
    def load_fonts(self):
        self._fonts[FONT_FILE] = pyray.load_font(FONT_FILE)

    def load_textures(self):

        self._textures[MAP] = pyray.load_texture(MAP)
        self._textures[FARMER] = pyray.load_texture(FARMER)
        self._textures[SNAIL] = pyray.load_texture(SNAIL)
        for n in ROSES:
            self._textures[n] = pyray.load_texture(n)

    # def load_animations(self):
    #     self._animations["roses"] = []
    #     for n in ROSES:
    #         self._animations["roses"].append(pyray.load_texture(n))
        

    def unload_fonts(self):
        for font in self._fonts.values():
            pyray.unload_font(font)
        self._fonts.clear()



    def unload_textures(self):
        for texture in self._textures.values():
            
            pyray.unload_texture(texture)
        self._textures.clear()

    # def unload_animations(self):
    #     for animation in self._animations.values():
    #         for texture in animation:
    #             pyray.unload_texture(texture)
    #     self._animations.clear()


    def _get_x_offset(self, text, font_size):
        width = pyray.measure_text(text, font_size)
        return int(width / 2)
    