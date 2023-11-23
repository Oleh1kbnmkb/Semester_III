import sqlite3

try:
  sqlite_connection = sqlite3.connect("menu.db")
  sqlite_create_table_query = """CREATE TABLE menu (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL,
                            description TEXT,
                            price REAL NOT NULL);"""


  cursor = sqlite_connection.cursor()
  cursor.execute(sqlite_create_table_query)
  # sqlite_connection.commit()
  print("Таблиця створена")
  cursor.close()



except sqlite3.Error as error:
  print("Помилка підключення до", error)
finally:
  if (sqlite_connection):
    sqlite_connection.close()
    print("Connection закрито")