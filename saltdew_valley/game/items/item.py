class Item():
    """An item is anything that can be held by the player in the hotbar

        It's responsibility is to do something when used

        Attributes:
            _texture(texture2d): the visible image for use in the hotbar
            _name(String): the name of the item
    """
    def __init__(self) -> None:
        self._texture = ''
    
    def get_texture(self):
        return self._texture
    
    def get_description(self):
        return ""
        
    def can_interact(self,cast,tile):
        """Checks if the tool can interact with the tile
            Args:
                tile: a tile of the map
            
            Returns Boolean, True if it can interact, False if not
        """
        return True
    
    def interact_with(self,cast, tile):
        """Uses the tool on the tile
            Args:
                tile: a tile of the map

            Returns nothing
        """
        pass
    