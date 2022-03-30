from constants import *
from game.casting.actor import Actor
class Text_bar(Actor):
    """A line of text that has a position somewhere on the screen
    
    Attributes:
        _text(String): the text to be displayed
        _color(Color): the color of the text
        _position(Point): the starting position of the text
    """

    """corner_displays(Money and Age) and commentators"""
    """A text message."""

    def __init__(self, text, position, fontfile = FONT_FILE, size = FONT_LARGE, alignment = ALIGN_LEFT):
        """Constructs a new Text."""
        super().__init__()
        self._text = text
        self._fontfile = fontfile
        self._size = size
        self._alignment = alignment
        self._position = position

    def get_position(self):
        return self._position

    def get_alignment(self):
        """Gets the alignment for the text.
        
        Returns:
            A number representing the text alignment.
        """
        return self._alignment

    def get_fontfile(self):
        """Gets the font file for the text.
        
        Returns:
            A string containing the font file.
        """
        return self._fontfile

    def get_size(self):
        """Gets the font size of the text.
        
        Returns:
            A number representing the font size.
        """
        return self._size

    def get_text(self):
        """Gets the text's text.
        
        Returns:
            A string containing the text's text.
        """
        return self._text

    def set_text(self, text):
        """Sets the text's text.
        
        Args:
            A string containing the text's text.
        """
        self._text = text