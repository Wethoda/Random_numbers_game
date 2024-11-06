import random
from config import DIFFICULTY_LEVELS

class Game:
    def __init__(self):
        super().__init__()

        self.target_number = None
        self.count = 0

    def check_guess(self, guess):
        self.count += 1
        if guess == self.target_number:
            print(f"Вы угадали число за {self.count} попыток")
        elif guess < self.target_number:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

    def reset_game(self, difficalty=None):
        if difficalty:
            self.difficalty = difficalty
        self.min_range, self.max_range = DIFFICULTY_LEVELS[self.difficalty]
        self.target_number = random.randint(self.min_range, self.max_range)
        self.count = 0