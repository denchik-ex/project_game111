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

        self.speed_y = 0          # вертикальная скорость
        self.on_ground = False    # стоит ли игрок на земле

    def jump(self):
        """Заставляет игрока прыгнуть, если он стоит на земле."""
        if self.on_ground:
            self.speed_y = PLAYER_JUMP_POWER
            self.on_ground = False

    def update(self):
        """Обновляет физику игрока: гравитацию и падение."""
        self.speed_y += PLAYER_GRAVITY

        # Не даём игроку разгоняться вниз бесконечно
        if self.speed_y > PLAYER_MAX_FALL_SPEED:
            self.speed_y = PLAYER_MAX_FALL_SPEED

        self.rect.y += self.speed_y

        # Если игрок достиг земли — останавливаем падение
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.speed_y = 0
            self.on_ground = True

    def draw(self, screen):
        """Рисует игрока на экране."""
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)