import pygame

from src.settings import (
    WIDTH,
    HEIGHT,
    TITLE,
    BACKGROUND_COLOR,
    BACKGROUND_PATTERN_COLOR,
    BACKGROUND_PATTERN_BORDER,
    BACKGROUND_TILE_SIZE,
    BACKGROUND_TILE_GAP,
    BACKGROUND_BORDER_WIDTH,
    GROUND_Y,
    GROUND_COLOR,
    GROUND_GRID_COLOR,
    GROUND_LINE_COLOR,
    GROUND_GRID_SIZE,
    GROUND_LINE_WIDTH,
)


class Window:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

    def clear(self):
        self.screen.fill(BACKGROUND_COLOR)

        tile_size = BACKGROUND_TILE_SIZE
        gap = BACKGROUND_TILE_GAP

        for row, y in enumerate(range(0, HEIGHT, tile_size)):
            # Соседние ряды смещены, чтобы узор не был однообразным.
            offset = tile_size // 2 if row % 2 else 0

            for x in range(-tile_size, WIDTH, tile_size):
                rect = pygame.Rect(
                    x + offset + gap // 2,
                    y + gap // 2,
                    tile_size - gap,
                    tile_size - gap,
                )

                pygame.draw.rect(
                    self.screen,
                    BACKGROUND_PATTERN_COLOR,
                    rect,
                )
                pygame.draw.rect(
                    self.screen,
                    BACKGROUND_PATTERN_BORDER,
                    rect,
                    BACKGROUND_BORDER_WIDTH,
                )

    def draw_ground(self):
        """Рисует землю с сеткой и ярким верхним краем."""
        pygame.draw.rect(
            self.screen,
            GROUND_COLOR,
            (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y),
        )

        # Вертикальные линии сетки
        for x in range(0, WIDTH, GROUND_GRID_SIZE):
            pygame.draw.line(
                self.screen,
                GROUND_GRID_COLOR,
                (x, GROUND_Y),
                (x, HEIGHT),
            )

        # Горизонтальные линии сетки
        for y in range(GROUND_Y, HEIGHT, GROUND_GRID_SIZE):
            pygame.draw.line(
                self.screen,
                GROUND_GRID_COLOR,
                (0, y),
                (WIDTH, y),
            )

        # Верхний край рисуем последним, поверх сетки.
        pygame.draw.line(
            self.screen,
            GROUND_LINE_COLOR,
            (0, GROUND_Y),
            (WIDTH, GROUND_Y),
            GROUND_LINE_WIDTH,
        )

    def update(self):
        pygame.display.flip()