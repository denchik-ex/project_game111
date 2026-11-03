from enum import Enum, auto

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
from src.ui import UI


class GameState(Enum):
    """Возможные состояния игры."""

    MENU = auto()
    PLAYING = auto()
    GAME_OVER = auto()


class Game:
    """Управляет игровым циклом и переключением экранов."""

    def __init__(self):
        pygame.init()

        self.window = Window()
        self.clock = pygame.time.Clock()
        self.ui = UI()

        self.player = Player()
        self.obstacles = []
        self.spawn_timer = 0

        self.state = GameState.MENU
        self.running = True

    def start_game(self):
        """Сбрасывает игровую попытку и начинает новую."""
        self.player = Player()
        self.obstacles.clear()
        self.spawn_timer = 0
        self.state = GameState.PLAYING

    def handle_events(self):
        """Обрабатывает события в зависимости от текущего экрана."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

            if event.type == pygame.KEYDOWN:
                self.handle_key(event.key)

    def handle_key(self, key):
        """Обрабатывает нажатие клавиши."""
        if self.state == GameState.MENU:
            if key == pygame.K_RETURN:
                self.start_game()
            elif key == pygame.K_ESCAPE:
                self.running = False

        elif self.state == GameState.PLAYING:
            if key in (pygame.K_SPACE, pygame.K_UP):
                self.player.jump()
            elif key == pygame.K_ESCAPE:
                self.state = GameState.MENU

        elif self.state == GameState.GAME_OVER:
            if key == pygame.K_r:
                self.start_game()
            elif key == pygame.K_ESCAPE:
                self.state = GameState.MENU

    def spawn_obstacle(self):
        """Создаёт препятствие сразу за правым краем окна."""
        self.obstacles.append(Obstacle(WIDTH))

    def update(self):
        """Обновляет мир только во время игры."""
        if self.state != GameState.PLAYING:
            return

        self.player.update()

        self.spawn_timer += 1

        if self.spawn_timer >= OBSTACLE_SPAWN_DELAY:
            self.spawn_timer = 0
            self.spawn_obstacle()

        for obstacle in self.obstacles:
            obstacle.update()

        self.obstacles = [
            obstacle
            for obstacle in self.obstacles
            if not obstacle.is_off_screen()
        ]

        for obstacle in self.obstacles:
            if self.player.rect.colliderect(obstacle.rect):
                # Заканчиваем попытку, но не закрываем окно.
                self.state = GameState.GAME_OVER
                break

    def draw_world(self):
        """Рисует землю, препятствия и игрока."""
        pygame.draw.rect(
            self.window.screen,
            GROUND_COLOR,
            (0, GROUND_Y, WIDTH, HEIGHT - GROUND_Y),
        )

        for obstacle in self.obstacles:
            obstacle.draw(self.window.screen)

        self.player.draw(self.window.screen)

    def draw(self):
        """Рисует экран текущего состояния."""
        self.window.clear()

        if self.state == GameState.MENU:
            self.ui.draw_menu(self.window.screen)
        else:
            self.draw_world()

            if self.state == GameState.GAME_OVER:
                self.ui.draw_game_over(self.window.screen)

        self.window.update()

    def run(self):
        """Главный игровой цикл."""
        while self.running:
            self.handle_events()

            # После команды выхода больше не обновляем игру.
            if not self.running:
                break

            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()