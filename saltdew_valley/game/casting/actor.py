from game.shared.tile import Tile
class Actor():
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Actor is to keep track of its appearance, position and velocity in 2d 
    space.

    Attributes:
        _texture (texture2d): the key to the image/animation of the actor in the video_service's texture dictionary

        _position (Point): The screen coordinates.
        _velocity (Point): The speed and direction.
    """
    def __init__(self):
        self._texture = ""
        self._position = Tile(1,1)
        self._velocity = Tile(0,0)

    def move_next(self):
        self._position =self._position.add(self._velocity)
        

    def get_texture(self):
        return self._texture
    
    def get_position(self):
        return self._position
    
    def get_velocity(self):
        return self._velocity

    def set_velocity(self,velocity):
        self._velocity = velocity
    
    def create_save(self):
        """outputs a string with the necessary information for it to be reloaded the next time the game is played.
         Each child of actor will have their own implementation"""
        return ''

    def load_save(self,data):
        """takes a list of information and loads the information into the new actor"""
        pass