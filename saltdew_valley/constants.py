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

SAVE_GAME_MODE = False

SAVE_FILE = "saltdew_valley/assets/save_file.txt"
SAVE_FILE = "saltdew_valley/assets/data/save_file.txt"

REACH = 5

# Screen

MAP_MAX_X = 1801
MAP_MAX_Y = 809

pyray.init_window(0,0,"title")
# print(pyray.get_screen_width())
SCALE = pyray.get_screen_width()/MAP_MAX_X

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
FONT_FILE = "saltdew_valley/assets/fonts/Quicksand-Bold.otf"
FONT_LARGE = 48
ALIGN_LEFT = 1



# Sprites
FARMER_GROUP = "players"
FARMER = "saltdew_valley/assets/images/Farmer_001.png"
FARMER_STARTING_X = 6
FARMER_STARTING_Y = 9

SNAIL = "saltdew_valley/assets/images/Snail_001.png"
SNAIL_STARTING_X = 20
SNAIL_STARTING_Y = 9

# Map
MAP = "saltdew_valley/assets/images/finished map.png"

# Roses
FLOWER_GROUP = "flowers"
ROSES = [f"saltdew_valley/assets/images/roses{n}.png" for n in range(1, 7)]

#Tilled Ground
TILLED_GROUND = "saltdew_valley/assets/tilled_ground.png"

# Borderbox
BORDER_BOX = "saltdew_valley/assets/images/placebox.png"

# Watering Can
WATERING_CAN = "saltdew_valley/assets/images/bucket.png"

# Hoe
HOE = "saltdew_valley/assets/images/hoe.png"

# Scythe
SCYTHE = "saltdew_valley/assets/images/scythe.png"




# Hotbar
HOTBAR_GROUP = "hotbar"
<<<<<<< HEAD
HOTBAR = "saltdew_valley/assets/hotbar.png"
HOTBAR_X = (MAX_X // 2) - 250
HOTBAR_Y = MAX_Y - 80
=======
HOTBAR = "saltdew_valley/assets/images/hotbar.png"
HOTBAR_X = (MAP_MAX_X // 2) - 250
HOTBAR_Y = MAP_MAX_Y - 80
>>>>>>> 42f156a17cb36243b30f8a7f6c23ac383f101f01
