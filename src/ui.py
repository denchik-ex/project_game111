import pygame

from src.settings import (
    WIDTH,
    HEIGHT,
    TEXT_COLOR,
    MENU_TITLE_SIZE,
    MENU_TEXT_SIZE,
    MENU_LINE_GAP,
)


class UI:
    """Рисует меню и экран поражения."""

    def __init__(self):
        # Шрифты создаём один раз, а не каждый кадр.
        self.title_font = pygame.font.SysFont(
            "arial", MENU_TITLE_SIZE
        )
        self.text_font = pygame.font.SysFont(
            "arial", MENU_TEXT_SIZE
        )

    def draw_centered_text(self, screen, text, font, y):
        """Рисует строку по центру окна."""
        image = font.render(text, True, TEXT_COLOR)
        rect = image.get_rect(center=(WIDTH // 2, y))
        screen.blit(image, rect)

    def draw_menu(self, screen):
        center_y = HEIGHT // 2

        self.draw_centered_text(
            screen,
            "Geometry Dash",
            self.title_font,
            center_y - MENU_LINE_GAP * 2,
        )
        self.draw_centered_text(
            screen,
            "Enter — начать игру",
            self.text_font,
            center_y,
        )
        self.draw_centered_text(
            screen,
            "Пробел / ↑ — прыжок",
            self.text_font,
            center_y + MENU_LINE_GAP,
        )
        self.draw_centered_text(
            screen,
            "Esc — выход",
            self.text_font,
            center_y + MENU_LINE_GAP * 2,
        )

    def draw_game_over(self, screen):
        center_y = HEIGHT // 2

        self.draw_centered_text(
            screen,
            "Поражение!",
            self.title_font,
            center_y - MENU_LINE_GAP,
        )
        self.draw_centered_text(
            screen,
            "R — попробовать снова",
            self.text_font,
            center_y + MENU_LINE_GAP,
        )
        self.draw_centered_text(
            screen,
            "Esc — главное меню",
            self.text_font,
            center_y + MENU_LINE_GAP * 2,
        )