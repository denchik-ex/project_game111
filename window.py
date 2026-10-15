import pygame

from src.settings import WIDTH, HEIGHT, TITLE, BACKGROUND_COLOR


class Window:

    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(TITLE)

    def clear(self):
        self.screen.fill(BACKGROUND_COLOR)

    def update(self):
        pygame.display.flip()