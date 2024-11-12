import sqlite3
import os

def get_db_connection():
    # Создаем или открываем файл базы данных SQLite в той же папке, где проект
    db_path = os.path.join(os.path.dirname(__file__), 'fishing.db')
    connection = sqlite3.connect(db_path)
    return connection
