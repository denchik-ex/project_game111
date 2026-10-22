import pygame

from src.settings import FPS
from src.window import Window


class Game:
    """Главный класс игры: запускает цикл и управляет состояниями."""

    def __init__(self):
        pygame.init()
        self.window = Window()
        self.clock = pygame.time.Clock()
        self.running = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        """Пока здесь будет логика игрока, препятствий и счёта."""
        pass

    def draw(self):
        self.window.clear()

        # Позже здесь будут земля, игрок и препятствия.
        pygame.draw.rect(
            self.window.screen,
            (0, 200, 255),
            (100, 300, 50, 50)
        )

        self.window.update()

    def run(self):
        """Главный игровой цикл."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()