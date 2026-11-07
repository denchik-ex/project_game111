import pygame

from src.settings import (
    OBSTACLE_SPEED,
    OBSTACLE_COLOR,
    OBSTACLE_OUTLINE_COLOR,
    OBSTACLE_OUTLINE_WIDTH,
    SPIKE_WIDTH,
    SPIKE_HEIGHT,
    BLOCK_WIDTH,
    BLOCK_HEIGHT,
    GROUND_Y,
)


class Obstacle:
    """Шип, пара шипов или блок, которые нужно перепрыгнуть."""

    def __init__(self, x, kind):
        self.kind = kind

        if kind == "spike":
            width = SPIKE_WIDTH
            height = SPIKE_HEIGHT

        elif kind == "double_spike":
            width = SPIKE_WIDTH * 2
            height = SPIKE_HEIGHT

        elif kind == "block":
            width = BLOCK_WIDTH
            height = BLOCK_HEIGHT

        else:
            raise ValueError(f"Неизвестное препятствие: {kind}")

        self.rect = pygame.Rect(
            x,
            GROUND_Y - height,
            width,
            height,
        )

    def update(self):
        self.rect.x -= OBSTACLE_SPEED

    def is_off_screen(self):
        return self.rect.right < 0

    def draw_spike(self, screen, x):
        """Рисует один треугольный шип."""
        points = [
            (x, self.rect.bottom),
            (x + SPIKE_WIDTH // 2, self.rect.top),
            (x + SPIKE_WIDTH, self.rect.bottom),
        ]

        pygame.draw.polygon(screen, OBSTACLE_COLOR, points)
        pygame.draw.polygon(
            screen,
            OBSTACLE_OUTLINE_COLOR,
            points,
            OBSTACLE_OUTLINE_WIDTH,
        )

    def draw(self, screen):
        if self.kind == "block":
            pygame.draw.rect(screen, OBSTACLE_COLOR, self.rect)
            pygame.draw.rect(
                screen,
                OBSTACLE_OUTLINE_COLOR,
                self.rect,
                OBSTACLE_OUTLINE_WIDTH,
            )

        else:
            self.draw_spike(screen, self.rect.x)

            if self.kind == "double_spike":
                self.draw_spike(
                    screen,
                    self.rect.x + SPIKE_WIDTH,
                )