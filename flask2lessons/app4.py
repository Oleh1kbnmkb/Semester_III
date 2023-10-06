import sqlite3

try:
  sqlite_connection = sqlite3.connect("sqlite_python.db")

  cursor = sqlite_connection.cursor()

  sqlite_insert_query = """INSERT INTO sqlitedb_developers(id, name, email, joining_date, salary)
                        VALUES (1, "Oleh", "op663246@gmail.com", "2023-01-29", 8100);
                        """


  cursor.execute(sqlite_insert_query)
  sqlite_connection.commit()
  cursor.close()


except sqlite3.Error as error:
  print("Помилка підключення до", error)
finally:
  if (sqlite_connection):
    sqlite_connection.close()
    print("Connection закрито")