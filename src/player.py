import pygame

from src.settings import (
    PLAYER_SIZE,
    PLAYER_X,
    PLAYER_START_Y,
    PLAYER_GRAVITY,
    PLAYER_JUMP_POWER,
    PLAYER_MAX_FALL_SPEED,
    PLAYER_COLOR,
    GROUND_Y,
)


class Player:
    """Игрок-кубик: умеет прыгать, падать и рисоваться."""

    def __init__(self):
        # Прямоугольник игрока: позиция и размер
        self.rect = pygame.Rect(
            PLAYER_X,
            PLAYER_START_Y,
            PLAYER_SIZE,
            PLAYER_SIZE
        )

        self.y = float(self.rect.y)

        self.speed_y = 0          # вертикальная скорость
        self.on_ground = False    # стоит ли игрок на земле

    def jump(self):
        """Заставляет игрока прыгнуть, если он стоит на земле."""
        if self.on_ground:
            self.speed_y = PLAYER_JUMP_POWER
            self.on_ground = False

    def update(self):
        self.speed_y = min(
            self.speed_y + PLAYER_GRAVITY,
            PLAYER_MAX_FALL_SPEED,
        )

        self.y += self.speed_y

        if self.y + self.rect.height >= GROUND_Y:
            self.y = float(GROUND_Y - self.rect.height)
            self.speed_y = 0
            self.on_ground = True

        self.rect.y = round(self.y)
        
    def draw(self, screen):
        """Рисует игрока на экране."""
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)