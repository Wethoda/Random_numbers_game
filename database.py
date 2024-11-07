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
    cursor.execute("SELECT * FROM users WHERE login = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    connect.close()
    return user is not None

def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)