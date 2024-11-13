import sqlite3
from config import DATABASE_NAME

def init_db():
    """Инициализация базы данных"""
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   login VARCHAR(50) NOT NULL,
                   password VARCHAR(50) NOT NULL)""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS game_logs(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       id_user INTEGER NOT NULL,
                       attempt_count INTEGER NOT NULL,
                       target_number INTEGER NOT NULL,
                       difficulty TEXT NOT NULL,
                       FOREIGN KEY (id_user) REFERENCES users(id))""")

    connect.commit()
    connect.close()

def add_user(username, password):
    """Добавление нового пользователя"""
    try:
        connect = sqlite3.connect(DATABASE_NAME)
        cursor = connect.cursor()
        cursor.execute("INSERT INTO users (login, password) VALUES(?, ?)", (username, password))
        connect.commit()
        connect.close()
        return True
    except sqlite3.IntegrityError:
        return False
def check_user(username, password):
    """Проверка есть ли такой пользователь в базе данных"""
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()
    cursor.execute("SELECT id FROM users WHERE login = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    connect.close()
    return user[0] if user else None

def log_game_result(user_id, attempt_count, target_number, difficulty):
    """Логируем результаты игры"""
    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()  # Вызов метода cursor() для создания курсора

    cursor.execute("""INSERT INTO game_logs (id_user, attempt_count, target_number, difficulty) 
                      VALUES(?, ?, ?, ?)""", (user_id, attempt_count, target_number, difficulty))

    connect.commit()
    connect.close()


def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)