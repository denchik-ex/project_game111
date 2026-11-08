# настройки игры

WIDTH = 900
HEIGHT = 500
FPS = 60

TITLE = "Geometry Dash — моя версия"

BACKGROUND_COLOR = (35, 10, 65)
GROUND_COLOR = (25, 10, 45)        # цвет земли
PLAYER_COLOR = (110, 255, 60)        # цвет игрока
OBSTACLE_COLOR = (255, 80, 80)      # цвет препятствий
TEXT_COLOR = (255, 255, 255)        # цвет текста

PLAYER_SIZE = 40                    # размер кубика игрока
PLAYER_X = 150                      # игрок стоит на одном месте по X
PLAYER_START_Y = 300                # начальная высота игрока

PLAYER_GRAVITY = 0.8                # сила притяжения
PLAYER_JUMP_POWER = -14             # сила прыжка; минус — вверх
PLAYER_MAX_FALL_SPEED = 20          # максимальная скорость падения

GROUND_HEIGHT = 80                              # толщина земли
GROUND_Y = HEIGHT - GROUND_HEIGHT               # верхняя граница земли

OBSTACLE_SIZE = 40
OBSTACLE_SPEED = 5
OBSTACLE_SPAWN_DELAY = 90

# Интерфейс
MENU_TITLE_SIZE = 56
MENU_TEXT_SIZE = 30
MENU_LINE_GAP = 48

# Уровень
LEVEL_LENGTH = 12000

# Интерфейс
FONT_SIZE = 30
HUD_MARGIN = 20

# Сохранение рекорда
SAVE_FILENAME = "save.json"

# Разновидности препятствий
SPIKE_WIDTH = 30
SPIKE_HEIGHT = 35

BLOCK_WIDTH = 45
BLOCK_HEIGHT = 50

OBSTACLE_OUTLINE_COLOR = (255, 255, 255)
OBSTACLE_OUTLINE_WIDTH = 2

# Узор фона
BACKGROUND_PATTERN_COLOR = (48, 15, 82)
BACKGROUND_PATTERN_BORDER = (65, 22, 105)
BACKGROUND_TILE_SIZE = 160
BACKGROUND_TILE_GAP = 12
BACKGROUND_BORDER_WIDTH = 3

# Оформление земли
GROUND_GRID_COLOR = (75, 30, 110)
GROUND_LINE_COLOR = (205, 140, 255)
GROUND_GRID_SIZE = 30
GROUND_LINE_WIDTH = 3

# Оформление кубика
PLAYER_BORDER_COLOR = (15, 10, 25)
PLAYER_INNER_COLOR = (30, 10, 55)
PLAYER_CENTER_COLOR = (0, 225, 255)
PLAYER_BORDER_WIDTH = 3