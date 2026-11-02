import pygame

from src.settings import (
    FPS,
    WIDTH,
    HEIGHT,
    GROUND_Y,
    GROUND_COLOR,
    OBSTACLE_SPAWN_DELAY,
)
from src.window import Window
from src.player import Player
from src.obstacles import Obstacle


class Game:
    """Главный класс игры: игровой цикл, игрок и препятствия."""

    def __init__(self):
        pygame.init()
        self.window = Window()
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.obstacles = []

        self.spawn_timer = 0
        self.running = True

    def handle_events(self):
        """Обрабатывает закрытие окна и прыжок."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_SPACE, pygame.K_UP):
                    self.player.jump()

    def spawn_obstacle(self):
        """Создаёт новое препятствие справа за экраном."""
        self.obstacles.append(Obstacle(WIDTH + 50))

    def update(self):
        """Обновляет игрока, препятствия и проверяет столкновения."""
        self.player.update()

        # Создаём препятствия через равные промежутки времени
        self.spawn_timer += 1

        if self.spawn_timer >= OBSTACLE_SPAWN_DELAY:
            self.spawn_timer = 0
            self.spawn_obstacle()

        # Двигаем препятствия
        for obstacle in self.obstacles:
            obstacle.update()

        # Удаляем препятствия, которые уехали за экран
        self.obstacles = [
            obstacle
            for obstacle in self.obstacles
            if not obstacle.is_off_screen()
        ]

        # Проверяем столкновение игрока с препятствиями
        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                self.running = False

    def draw(self):
        """Рисует текущий кадр."""
        self.window.clear()

        # Земля
        pygame.draw.rect(
            self.window.screen,
            GROUND_COLOR,
            (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y)
        )

        # Препятствия
        for obstacle in self.obstacles:
            obstacle.draw(self.window.screen)

        # Игрок
        self.player.draw(self.window.screen)

        self.window.update()

    def run(self):
        """Главный игровой цикл."""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()