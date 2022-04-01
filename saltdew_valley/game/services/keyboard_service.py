import pyray

class KeyboardService():
    """Detects player input. 
    
    The responsibility of a KeyboardService is to indicate whether or not a key is up or down.

    Attributes:
        _keys (Dict[string, int]): The letter to key mapping.
    """

    def __init__(self):
        """Constructs a new KeyboardService."""
        self._keys = {}
        
        self._keys['w'] = pyray.KEY_W
        self._keys['a'] = pyray.KEY_A
        self._keys['s'] = pyray.KEY_S
        self._keys['d'] = pyray.KEY_D
        self._keys['1'] = pyray.KEY_ONE
        self._keys['2'] = pyray.KEY_TWO
        self._keys['3'] = pyray.KEY_THREE
        self._keys['4'] = pyray.KEY_FOUR
        self._keys['5'] = pyray.KEY_FIVE
        self._keys['6'] = pyray.KEY_SIX
        self._keys['7'] = pyray.KEY_SEVEN
        self._keys['8'] = pyray.KEY_EIGHT
        self._keys['9'] = pyray.KEY_NINE

    def is_key_up(self, key):
        """Checks if the given key is currently up.
        
        Args:
            key (string): The given key (w, a, s, d)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_up(pyray_key)

    def is_key_down(self, key):
        """Checks if the given key is currently down.
        
        Args:
            key (string): The given key (w, a, s, d)
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_down(pyray_key)