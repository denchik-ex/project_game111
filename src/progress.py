import json
from pathlib import Path

from src.settings import SAVE_FILENAME


class Progress:
    """Загружает и сохраняет лучший процент прохождения."""

    def __init__(self):
        self.path = (
            Path(__file__).resolve().parent.parent / SAVE_FILENAME
        )
        self.best = self.load()

    def load(self):
        """Возвращает рекорд или 0, если сохранения ещё нет."""
        try:
            with self.path.open("r", encoding="utf-8") as file:
                data = json.load(file)

            best = data["best_progress"]

            if type(best) is int and 0 <= best <= 100:
                return best

        except (
            OSError,
            ValueError,
            KeyError,
            TypeError,
        ):
            pass

        return 0

    def save(self, result):
        """Записывает только новый рекорд."""
        if result <= self.best:
            return

        self.best = result

        try:
            with self.path.open("w", encoding="utf-8") as file:
                json.dump(
                    {"best_progress": self.best},
                    file,
                    indent=4,
                )
        except OSError:
            pass