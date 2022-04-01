from game.items.item import Item
class Tool(Item):
    """An item that can interact with something without placing anything"""
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