from flask import Flask, render_template, request
import sqlite3
import os
from db_config import get_db_connection

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # Получаем соединение с базой данных
        conn = get_db_connection()
        cursor = conn.cursor()

        # Проверяем, существует ли пользователь в базе данных
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = cursor.fetchone()

        if user:
            # Если пользователь существует, обновляем его данные (например, пароль)
            cursor.execute("UPDATE users SET password = ? WHERE email = ?", (password, email))
            conn.commit()
            return "Пароль обновлен для пользователя: " + email
        else:
            # Если пользователя нет, добавляем нового
            cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (email, password))
            conn.commit()
            return f"Пользователь {email} успешно зарегистрирован!"

        # Закрываем соединение с базой
        cursor.close()
        conn.close()

    return render_template('index.html')

if __name__ == "__main__":
    # Перед запуском проверим, что таблица users существует в базе данных
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL)''')
    conn.commit()
    cursor.close()
    conn.close()

    app.run(debug=True)
