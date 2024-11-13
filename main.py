import sys
from PySide6.QtWidgets import QApplication, QMessageBox
from ui_main_window import UiMainWindow
from game_logic import Game
from database import init_db, check_user, add_user, log_game_result
from log_window import LoginWindow

init_db()

class MainApp(UiMainWindow):
    def __init__(self, user_id, username):
        super().__init__()

        self.user_id = user_id
        self.username = username  # Сохраняем имя пользователя
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

        self.check_button.setEnabled(True)  # Разблокируем кнопку после начала новой игры.

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
            self.check_button.setEnabled(False)  # Блокируем кнопку после угадывания числа.

            difficulty = self.difficulty_combo.currentText()
            log_game_result(self.user_id, self.game.count, self.game.target_number, difficulty)
            self.input_field.clear()

        elif user_number < self.game.target_number:
            self.result_label.setText("Загаданное число больше.")
        else:
            self.result_label.setText("Загаданное число меньше.")


class Application:
    def __init__(self):
        self.app = QApplication(sys.argv)

        self.login_window = LoginWindow()
        self.login_window.login_button.clicked.connect(self.handle_login)
        self.login_window.register_button.clicked.connect(self.handle_register)
        self.login_window.show()

    def handle_login(self):
        """Обработчик входа"""
        username = self.login_window.login_input.text()
        password = self.login_window.password_input.text()

        if not username or not password:
            QMessageBox.warning(self.login_window, "Ошибка", "Поля логин и пароль не могут быть пустыми!")
            return

        user_id = check_user(username, password)  # Проверка в базе данных

        if user_id:  # Если пользователь найден
            self.login_window.close()
            self.main_game = MainApp(user_id, username)  # Передаем ID и имя пользователя
            self.main_game.show()
        else:
            QMessageBox.warning(self.login_window, "Ошибка", "Неверный логин или пароль.")

    def handle_register(self):
        """Обработчик регистрации"""
        username = self.login_window.login_input.text()
        password = self.login_window.password_input.text()

        if not username or not password:
            QMessageBox.warning(self.login_window, "Ошибка", "Поля логин и пароль не могут быть пустыми!")
            return

        if add_user(username, password):  # Добавляем нового пользователя в базу
            QMessageBox.information(self.login_window, "Успех", "Вы успешно зарегистрировались!")
        else:
            QMessageBox.warning(self.login_window, "Ошибка", "Пользователь с таким логином уже существует!")

    def run(self):
        sys.exit(self.app.exec())

if __name__ == "__main__":
    app = Application()
    app.run()
