from pathlib import Path

import pygame

from src.level import LEVEL_OBSTACLES
from src.obstacles import Obstacle
from src.player import Player
from src.progress import Progress
from src.settings import (
    FONT_SIZE,
    FPS,
    HEIGHT,
    HUD_MARGIN,
    LEVEL_LENGTH,
    OBSTACLE_SPEED,
    SOUND_VOLUME,
    TEXT_COLOR,
    WIDTH,
    MUSIC_VOLUME
)
from src.window import Window


class Game:
    def __init__(self):
        pygame.init()

        self.sounds = {}
        self.load_sounds()
        self.music_loaded = False
        self.music_started = False
        self.load_music()

        self.window = Window()
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("arial", FONT_SIZE)
        self.progress = Progress()

        self.player = Player()
        self.obstacles = []
        self.distance = 0

        self.state = "menu"
        self.running = True

    def load_sounds(self):
        if not pygame.mixer.get_init():
            return

        sounds_path = (
            Path(__file__).resolve().parent.parent
            / "sounds"
        )

        for name in ("jump", "fail", "victory"):
            try:
                sound = pygame.mixer.Sound(
                    str(sounds_path / f"{name}.mp3")
                )
                sound.set_volume(SOUND_VOLUME)
                self.sounds[name] = sound

            except (pygame.error, OSError)  :
                pass

    def load_music(self):
        if not pygame.mixer.get_init():
            return

        music_path = (
            Path(__file__).resolve().parent.parent
            / "sounds"
            / "music1.mp3"
        )

        try:
            pygame.mixer.music.load(str(music_path))
            pygame.mixer.music.set_volume(MUSIC_VOLUME)
            self.music_loaded = True

        except (pygame.error, OSError):
            pass

    def play_sound(self, name):
        sound = self.sounds.get(name)

        if sound is not None:
            sound.play()

    def get_percent(self):
        return min(
            100,
            self.distance * 100 // LEVEL_LENGTH,
        )

    def restart(self):
        self.player = Player()

        self.obstacles = [
            Obstacle(x, kind)
            for x, kind in LEVEL_OBSTACLES
        ]

        self.distance = 0
        self.state = "playing"

        if self.music_loaded:
                pygame.mixer.music.stop()
                pygame.mixer.music.play(-1)
                self.music_started = True

    def finish_attempt(self, state):
        self.progress.save(self.get_percent())
        self.state = state

        if self.music_loaded:
            pygame.mixer.music.stop()

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
                        
                        if self.music_loaded:
                            pygame.mixer.music.pause()

                elif self.state == "paused":
                    if event.key == pygame.K_p:
                        self.state = "playing"

                        if self.music_loaded:
                            if pygame.mixer.music.get_busy:
                                pygame.mixer.music.unpause()
                            else:
                                pygame.mixer.music.play(-1)

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
        line_height = self.font.get_linesize()
        start_y = HEIGHT // 2 - len(lines) * line_height // 2

        for index, line in enumerate(lines):
            image = self.font.render(line, True, TEXT_COLOR)
            rect = image.get_rect(
                midtop=(
                    WIDTH // 2,
                    start_y + index * line_height,
                )
            )

            self.window.screen.blit(image, rect)

    def draw_world(self):
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
                "Neon Dash",
                f"Рекорд: {self.progress.best}%",
                "",
                "Enter — начать игру",
                "Пробел / стрелка вверх — прыжок",
                "P — пауза",
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