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
    