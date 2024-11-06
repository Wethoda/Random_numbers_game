import random
from config import DIFFICULTY_LEVELS

class Game:
    def __init__(self):
        self.target_number = None
        self.count = 0
        self.min_range, self.max_range = DIFFICULTY_LEVELS["легкий"]  # Начальный уровень

    def check_guess(self, guess):
        """Проверка, угадал ли пользователь число"""
        self.count += 1
        if guess == self.target_number:
            print(f"Вы угадали число за {self.count} попыток")
        elif guess < self.target_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

    def reset_game(self, difficulty="легкий"):
        """Перезапуск игры с новым уровнем сложности"""
        self.min_range, self.max_range = DIFFICULTY_LEVELS[difficulty]
        self.target_number = random.randint(self.min_range, self.max_range)
        self.count = 0