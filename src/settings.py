# настройки игры

WIDTH = 900
HEIGHT = 500
FPS = 60

TITLE = "Geometry Dash — моя версия"

BACKGROUND_COLOR = (30, 30, 46)
GROUND_COLOR = (70, 70, 100)        # цвет земли
PLAYER_COLOR = (0, 200, 255)        # цвет игрока
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