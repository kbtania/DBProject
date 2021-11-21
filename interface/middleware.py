import sqlite3


def get_all_teachers():
    try:
        sqlite_connection = sqlite3.connect('../backend/data.db')
        cursor = sqlite_connection.cursor()
        print("Успішно підключено до бази даних SQLite.")

        sqlite_select_query = "SELECT teacher_name FROM teachers"
        all_teachers = []
        for row in cursor.execute(sqlite_select_query):
            all_teachers.append(row[0])
        cursor.close()

    except sqlite3.Error as error:
        print("Помилка при підключенні до SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("З'єднання з SQLite закрито.")
    return all_teachers



