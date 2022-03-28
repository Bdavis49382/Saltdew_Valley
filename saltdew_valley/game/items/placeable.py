from item import Item
class Placeable(Item):
    """A specific kind of Item, placeables are able to be placed in the world

    """
    def can_be_placed_on(self,tile):
        """Checks if the item can be placed on the tile
            Args:
                tile: a tile of the map
            
            Returns Boolean, True if it can be placed, False if not
        """
        pass
    def place(self,tile):
        """Places the item on the tile
            Args:
                tile: a tile of the map

            Returns nothing
        """
        pass
    pass