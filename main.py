import sys
from PySide6.QtWidgets import QApplication
from ui_main_window import UiMainWindow
from game_logic import Game

class MainApp(UiMainWindow):
    def __init__(self):
        super().__init__()

        self.game = Game()
        self.check_button.clicked.connect(self.check_guess)
        self.reset_button.clicked.connect(self.start_new_game)

        self.start_new_game()

    def start_new_game(self):
        """Начинаем новую игру"""
        difficulty = self.difficulty_combo.currentText()

        self.game.reset_game(difficulty)
        self.result_label.setText(f"Загадано число от {self.game.min_range} до {self.game.max_range}. Начинайте угадывать!")
        self.input_field.clear()

        self.check_button.setEnabled(True) # Разблокируем кнопку после начала новой игры.

    def check_guess(self):
        """Проверка введённого числа"""
        try:
            user_number = int(self.input_field.text())
        except ValueError:
            self.result_label.setText(f"Пожалуйста, введите число от {self.game.min_range} до {self.game.max_range}.")
            return

        if user_number < self.game.min_range or user_number > self.game.max_range:
            self.result_label.setText(f"Число должно быть в диапазоне от {self.game.min_range} до {self.game.max_range}.")
            return

        self.game.check_guess(user_number)

        if user_number == self.game.target_number:
            self.result_label.setText(f"Поздравляю! Вы угадали число {self.game.target_number} за {self.game.count} попыток!")
            self.check_button.setEnabled(False) # Блокируем кнопку после угадывания числа.
        elif user_number < self.game.target_number:
            self.result_label.setText("Загаданное число больше.")
        else:
            self.result_label.setText("Загаданное число меньше.")

        self.input_field.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())