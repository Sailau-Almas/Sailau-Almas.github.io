import sqlite3

# Подключаемся к базе данных
conn = sqlite3.connect('fishing.db')  # Укажите путь к вашей базе данных
cursor = conn.cursor()

# Выполняем SQL-запрос для получения всех данных из таблицы users
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Выводим результат
for row in rows:
    print(row)

# Закрываем соединение с базой
conn.close()
