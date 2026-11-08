import pygame
from pathlib import Path

from src.settings import (
    FPS,
    WIDTH,
    HEIGHT,
    GROUND_Y,
    GROUND_COLOR,
    TEXT_COLOR,
    OBSTACLE_SPEED,
    LEVEL_LENGTH,
    FONT_SIZE,
    HUD_MARGIN,
    SOUND_VOLUME
)
from src.window import Window
from src.player import Player
from src.obstacles import Obstacle
from src.progress import Progress
from src.level import LEVEL_OBSTACLES


class Game:
    """Управляет игрой, меню и прохождением уровня."""

    def __init__(self):
        pygame.init()

        sounds_path = (
            Path(__file__).resolve().parent.parent
            / "sounds"
        )

        self.sounds = {}

        if pygame.mixer.get_init():
            for name in ("jump", "fail", "victory"):
                try:
                    sound = pygame.mixer.Sound(
                        str(sounds_path / f"{name}.mp3")
                    )
                    sound.set_volume(SOUND_VOLUME)
                    self.sounds[name] = sound

                except (pygame.error, OSError) as error:
                    print(
                        f"Не удалось загрузить звук {name}: {error}"
                    )
        else:
            print("Звук недоступен: игра запущена без аудио.")

        self.window = Window()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", FONT_SIZE)
        self.progress = Progress()

        self.player = Player()
        self.obstacles = []
        self.distance = 0

        self.state = "menu"
        self.running = True

    def get_percent(self):
        """Возвращает целый процент прохождения от 0 до 100."""
        return min(100, self.distance * 100 // LEVEL_LENGTH)

    def restart(self):
        self.player = Player()

        self.obstacles = [
            Obstacle(x, kind)
            for x, kind in LEVEL_OBSTACLES
        ]

        self.distance = 0
        self.state = "playing"

    def play_sound(self, name):
        sound = self.sounds.get(name)

        if sound is not None:
            sound.play()

    def finish_attempt(self, state):
        """Заканчивает попытку и сохраняет результат."""
        self.progress.save(self.get_percent())
        self.state = state

        if state == "game_over":
            self.play_sound("fail")

        elif state == "victory":
            self.play_sound("victory")

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.progress.save(self.get_percent())
                self.running = False
                return

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.state == "menu":
                        self.running = False
                    else:
                        self.finish_attempt("menu")

                elif self.state == "menu":
                    if event.key == pygame.K_RETURN:
                        self.restart()

                elif self.state == "playing":
                    if event.key in (pygame.K_SPACE, pygame.K_UP):
                        if self.player.on_ground:
                            self.player.jump()
                            self.play_sound("jump")

                    elif event.key == pygame.K_p:
                        self.state = "paused"

                elif self.state == "paused":
                    if event.key == pygame.K_p:
                        self.state = "playing"

                elif self.state in ("game_over", "victory"):
                    if event.key == pygame.K_r:
                        self.restart()

    def update(self):
        if self.state != "playing":
            return

        self.player.update()

        self.distance = min(
            self.distance + OBSTACLE_SPEED,
            LEVEL_LENGTH,
        )

        for obstacle in self.obstacles:
            obstacle.update()

            if self.player.rect.colliderect(obstacle.rect):
                self.finish_attempt("game_over")
                return

        self.obstacles = [
            obstacle
            for obstacle in self.obstacles
            if not obstacle.is_off_screen()
        ]

        if self.distance >= LEVEL_LENGTH:
            self.finish_attempt("victory")

    def draw_text(self, lines):
        """Рисует несколько строк по центру окна."""
        line_height = self.font.get_linesize()
        start_y = HEIGHT // 2 - len(lines) * line_height // 2

        for index, line in enumerate(lines):
            image = self.font.render(line, True, TEXT_COLOR)
            rect = image.get_rect(
                midtop=(WIDTH // 2, start_y + index * line_height)
            )
            self.window.screen.blit(image, rect)

    def draw_world(self):
        """Рисует землю, препятствия, игрока и прогресс."""
        self.window.draw_ground()
       

        for obstacle in self.obstacles:
            obstacle.draw(self.window.screen)

        self.player.draw(self.window.screen)

        current = self.get_percent()
        best = max(current, self.progress.best)

        image = self.font.render(
            f"Прогресс: {current}%   Рекорд: {best}%",
            True,
            TEXT_COLOR,
        )
        self.window.screen.blit(
            image,
            (HUD_MARGIN, HUD_MARGIN),
        )

    def draw(self):
        self.window.clear()

        if self.state == "menu":
            self.draw_text([
                "Geometry Dash",
                f"Рекорд: {self.progress.best}%",
                "",
                "Enter — начать игру",
                "Пробел / стрелка вверх — прыжок",
                "Esc — выход",
            ])

        elif self.state in ("game_over", "victory"):
            title = (
                "Уровень пройден!"
                if self.state == "victory"
                else "Поражение!"
            )

            self.draw_text([
                title,
                f"Пройдено: {self.get_percent()}%",
                f"Рекорд: {self.progress.best}%",
                "",
                "R — попробовать снова",
                "Esc — главное меню",
            ])

        else:
            self.draw_world()

            if self.state == "paused":
                self.draw_text([
                    "Пауза",
                    "",
                    "P — продолжить",
                    "Esc — главное меню",
                ])


        self.window.update()

    def run(self):
        while self.running:
            self.handle_events()

            if not self.running:
                break

            self.update()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()