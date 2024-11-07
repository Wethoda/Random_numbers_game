from PySide6.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QComboBox

class UiMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Угадай число")
        self.setFixedSize(300, 200)

        self.instruction_label = QLabel("Введите ваше число:", self)
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Число")

        self.result_label = QLabel("", self)
        self.check_button = QPushButton("Проверить", self)
        self.reset_button = QPushButton("Начать заново", self)

        self.difficulty_label = QLabel("Выберите сложность:", self)
        self.difficulty_combo = QComboBox(self)
        self.difficulty_combo.addItems(["Легкий", "Средний", "Сложный"])

        layout = QVBoxLayout()
        layout.addWidget(self.difficulty_label)
        layout.addWidget(self.difficulty_combo)
        layout.addWidget(self.instruction_label)
        layout.addWidget(self.input_field)
        layout.addWidget(self.result_label)
        layout.addWidget(self.check_button)
        layout.addWidget(self.reset_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
