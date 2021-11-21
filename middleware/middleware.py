import sqlite3

try:
    sqlite_connection = sqlite3.connect('../backend/data.db')
    cursor = sqlite_connection.cursor()
    print("Успішно підключено до бази даних SQLite.")

    sqlite_select_query = "SELECT teacher_name FROM teachers"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()[0][0]
    print(record)
    cursor.close()

except sqlite3.Error as error:
    print("Помилка при підключенні до SQLite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("З'єднання з SQLite закрито.")
