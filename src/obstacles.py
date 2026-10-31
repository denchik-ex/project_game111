# src/obstacles.py
import pygame

from src.settings import (
    OBSTACLE_SIZE,
    OBSTACLE_SPEED,
    OBSTACLE_COLOR,
    GROUND_Y,
)


class Obstacle:
    """Препятствие, которое движется влево."""

    def __init__(self, x):
        self.rect = pygame.Rect(
            x,
            GROUND_Y - OBSTACLE_SIZE,
            OBSTACLE_SIZE,
            OBSTACLE_SIZE
        )

    def update(self):
        self.rect.x -= OBSTACLE_SPEED

    def is_off_screen(self):
        return self.rect.right < 0

    def draw(self, screen):
        pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)