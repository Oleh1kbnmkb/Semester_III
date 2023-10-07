import sqlite3

def read_var_data():
  try:
    sqlite_connection = sqlite3.connect("sqlite_python.db")

    cursor = sqlite_connection.cursor()

    sqlite_select_query = """SELECT * FROM sqlitedb_developers"""


    cursor.execute(sqlite_select_query)

    record = cursor.fetchall()

    for row in record:
      print("ID", row[0])
      print("Name", row[1])
      print("e-email", row[2])
      print("data", row[3])
      print("salary", row[4], end="\n\n\n\n")

    

    cursor.close()


  except sqlite3.Error as error:
    print("Помилка підключення до", error)
  finally:
    if (sqlite_connection):
      sqlite_connection.close()
      print("Connection закрито")


read_var_data()