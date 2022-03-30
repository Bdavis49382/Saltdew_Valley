from constants import *
from game.shared.point import Point
class Tile(Point):
    def __init__(self, x, y):
        super().__init__(x*CELL_SIZE, y*CELL_SIZE)
        self._tiled_x = x
        self._tiled_y = y
    
    def get_tiled_x(self):
        return self._tiled_x
    
    def get_tiled_y(self):
        return self._tiled_y
    
    def __add__(self, other):
        if type(other) == Tile:
            my_x = self._tiled_x + other._tiled_x
            my_y = self._tiled_y + other._tiled_y
            return Tile(my_x, my_y)
        elif type(other) == Point:
            my_x = self._x + other.get_x()
            my_y = self._y + other.get_y()
            return Tile(my_x, my_y)
        else:
            raise(ValueError)
    
    def __sub__(self, other):
        return self + (other * -1)

    def __mul__(self, other):
        if (type(other == int) or type(other)==float):
            return self.scale(other)
        else:
            raise(ValueError)

    def __rmul__(self, other) -> bool:
        return other * self

    def __gt__(self, other) -> bool:
        if type(other) == Tile:
            bool_x = self._tiled_x > other.get_tiled_x()
            bool_y = self._tiled_y > other.get_tiled_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)
        elif type(other) == Point:
            bool_x = self._x > other.get_x()
            bool_y = self._y > other.get_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)

    def __lt__(self, other) -> bool:
        if type(other) == Tile:
            bool_x = self._tiled_x < other.get_tiled_x()
            bool_y = self._tiled_y < other.get_tiled_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)
        elif type(other) == Point:
            bool_x = self._x < other.get_x()
            bool_y = self._y < other.get_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)
    
    def __eq__(self, other) -> bool:
        if type(other) == Tile:
            bool_x = self._tiled_x == other.get_tiled_x()
            bool_y = self._tiled_y == other.get_tiled_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)
        elif type(other) == Point:
            bool_x = self._x == other.get_x()
            bool_y = self._y == other.get_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)

    def __lte__(self, other) -> bool:
        if type(other) == Tile:
            bool_x = self._tiled_x == other.get_tiled_x() or self._tiled_x < other.get_tiled_x()
            bool_y = self._tiled_y == other.get_tiled_y() or self._tiled_y < other.get_tiled_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)
        elif type(other) == Point:
            bool_x = self._x == other.get_x() or self._x < other.get_x()
            bool_y = self._y == other.get_y() or self._x < other.get_x()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)

    def __gte__(self, other) -> bool:
        if type(other) == Tile:
            bool_x = self._tiled_x == other.get_tiled_x() or self._tiled_x > other.get_tiled_x()
            bool_y = self._tiled_y == other.get_tiled_y() or self._tiled_y > other.get_tiled_y()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)
        elif type(other) == Point:
            bool_x = self._x == other.get_x() or self._x > other.get_x()
            bool_y = self._y == other.get_y() or self._x > other.get_x()
            my_x = 1 if bool_x else -1
            my_y = 1 if bool_y else -1
            return Tile(my_x, my_y)
    def __str__(self):
        return f"({self._tiled_x}, {self._tiled_y})"