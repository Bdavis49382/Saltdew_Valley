from constants import *
from game.shared.point import Point
class Tile(Point):
    def __init__(self, x, y):
        super().__init__(x*CELL_SIZE, y*CELL_SIZE)
        self.tiled_x = x
        self.tiled_y = y
    
    def get_tiled_x(self):
        return self.tiled_x
    
    def get_tiled_y(self):
        return self.tiled_y

    
    
