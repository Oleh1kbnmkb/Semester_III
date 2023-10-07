import sqlite3

try:
  sqlite_connection = sqlite3.connect("sqlite_python.db")

  cursor = sqlite_connection.cursor()

  sqlite_select_query = "select sqlite version();"
  cursor.execute(sqlite_select_query)
  record = cursor.fetchall()
  print("Версія БД:", record)
  cursor.close()


except sqlite3.Error as error:
  print("Помилка підключення до", error)
finally:
  if (sqlite_connection):
    sqlite_connection.close()
    print("Connection закрито")