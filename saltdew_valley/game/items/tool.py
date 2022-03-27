import imp
from item import Item
class Tool(Item):
    """An item that can interact with something without placing anything"""
    def can_interact(self,tile):
        """Checks if the tool can interact with the tile
            Args:
                tile: a tile of the map
            
            Returns Boolean, True if it can interact, False if not
        """
        pass
    
    def interact_with(self,tile):
        """Uses the tool on the tile
            Args:
                tile: a tile of the map

            Returns nothing
        """
        pass