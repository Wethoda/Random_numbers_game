import sqlite3
from config import DATABASE_NAME

def init_db():

    connect = sqlite3.connect(DATABASE_NAME)
    cursor = connect.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   login VARCHAR(50) NOT NULL,
                   password VARCHAR(50) NOT NULL)""")
    connect.commit()
    connect.close()

def get_db_connection():
    return sqlite3.connect(DATABASE_NAME)