from game.casting.actor import Actor

class Plant(Actor):
    """A plant is something that once planted, grows regularly, and can be harvested to recieve an item once finished growing
    
        Attributes:
            _growth_level(int): the stage of growth it is on
            _position(Point): the point on the map where the plant is placed
            _growth_rate(float): the rate at which the plant is growing, dependant on how close it is to water
            _type(String): the type of plant. ex: wheat, potato, carrot, etc.
    """
    def __init__(self,position,type):
        super().__init__()
        self._growth_level = 0
        self._position = position
        self._growth_rate = 1
        self._type = type
        self._texture = ""
    
    def grow(self):
        self._growth_level +=1

    