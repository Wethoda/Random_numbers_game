import sys
import random
from PySide6.QtWidgets import QApplication
from ui_main_window import UiMainWindow
import config

class MainApp(UiMainWindow):
    def __init__(self):
        super().__init__()

        self.target_number = None
        self.count = 0
        self.min_range = 1
        self.max_range = 10

        self.check_button.clicked.connect(self.check_guess)
        self.reset_button.clicked.connect(self.start_new_game)

        self.start_new_game()

    def start_new_game(self):
        """Начинаем новую игру"""
        difficulty = self.difficulty_combo.currentText()

        self.min_range, self.max_range = config.DIFFICULTY_LEVELS[difficulty]

        self.target_number = random.randint(self.min_range, self.max_range)
        self.count = 0
        self.result_label.setText(f"Загадано число от {self.min_range} до {self.max_range}. Начинайте угадывать!")
        self.input_field.clear()

    def check_guess(self):
        """Проверка введённого числа"""
        try:
            user_number = int(self.input_field.text())
            self.count += 1
        except ValueError:
            self.result_label.setText(f"Пожалуйста, введите число от {self.min_range} до {self.max_range}.")
            return

        if user_number < self.min_range or user_number > self.max_range:
            self.result_label.setText(f"Число должно быть в диапазоне от {self.min_range} до {self.max_range}.")
            return

        if user_number == self.target_number:
            self.result_label.setText(f"Поздравляю! Вы угадали число {self.target_number} за {self.count} попыток!")
        elif user_number < self.target_number:
            self.result_label.setText("Загаданное число больше.")
        else:
            self.result_label.setText("Загаданное число меньше.")

        self.input_field.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())