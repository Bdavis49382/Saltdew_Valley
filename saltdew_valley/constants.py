import pyray
from game.shared.color import Color

# -------------------------------------------------------------------------------------------------- 
# GENERAL GAME CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# Game
CAPTION = "Saltdew Valley"
FRAME_RATE = 15

FAST_AGING = 10
NORMAL_AGING = 100

SNAIL_MOVEMENT_RATE = .25

SAVE_FILE = "saltdew_valley/assets/save_file.txt"

# Screen

MAP_MAX_X = 1185
MAP_MAX_Y = 455

pyray.init_window(0,0,"title")
# print(pyray.get_screen_width())
SCALE = pyray.get_screen_width()/1185

pyray.close_window()

MAX_X = MAP_MAX_X * SCALE
MAX_Y = MAP_MAX_Y * SCALE

NO_TINT = pyray.Color(255,255,255,255)
BLACK_TINT = pyray.Color(0,0,0,255)


CELL_SIZE = 16 * SCALE
FONT_SIZE = 15
COLUMNS = 40
ROWS = 20

# Text
FONT_FILE = "saltdew_valley/assets/Quicksand-Bold.otf"
FONT_LARGE = 48
ALIGN_LEFT = 1



# Sprites
FARMER_GROUP = "players"
FARMER = "saltdew_valley/assets/Farmer_001.png"
FARMER_STARTING_X = 6
FARMER_STARTING_Y = 9

SNAIL = "saltdew_valley/assets/Snail_001.png"
SNAIL_STARTING_X = 20
SNAIL_STARTING_Y = 9

MAP = "saltdew_valley/assets/TestMap.png"

FLOWER_GROUP = "flowers"
ROSES = [f"saltdew_valley/assets/roses{n}.png" for n in range(1, 7)]