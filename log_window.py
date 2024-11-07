from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Вход")
        self.setFixedSize(300, 200)

        self.login_label = QLabel("Логин: ", self)
        self.login_input = QLineEdit(self)
        self.login_input.setPlaceholderText("Введите логин")

        self.password_label = QLabel("Пароль: ", self)
        self.password_input = QLineEdit(self)
        self.password_input.setPlaceholderText("Введите пароль")
        self.password_input.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Войти", self)
        self.register_button = QPushButton("Регистрация", self)

        layout = QVBoxLayout()
        layout.addWidget(self.login_label)
        layout.addWidget(self.login_input)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_input)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
