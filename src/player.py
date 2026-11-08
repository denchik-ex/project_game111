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
    PLAYER_BORDER_COLOR,
    PLAYER_INNER_COLOR,
    PLAYER_CENTER_COLOR,
    PLAYER_BORDER_WIDTH,
)


class Player:

    def __init__(self):
        self.rect = pygame.Rect(
            PLAYER_X,
            PLAYER_START_Y,
            PLAYER_SIZE,
            PLAYER_SIZE
        )

        self.y = float(self.rect.y)

        self.speed_y = 0          
        self.on_ground = False    # стоит ли игрок на земле

    def jump(self):
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
        pygame.draw.rect(screen,PLAYER_COLOR,self.rect,)
        pygame.draw.rect(
            screen,
            PLAYER_BORDER_COLOR,
            self.rect,
            PLAYER_BORDER_WIDTH,
        )

        x = self.rect.x
        y = self.rect.y
        size = self.rect.width

        # Тёмный квадрат внутри кубика
        pygame.draw.rect(
            screen,
            PLAYER_INNER_COLOR,
            (x + size // 4, y + size // 4, size // 2, size // 2),
        )

        # Голубой квадрат в центре
        pygame.draw.rect(
            screen,
            PLAYER_CENTER_COLOR,
            (x + size * 3 // 8, y + size * 3 // 8, size // 4, size // 4),
        )