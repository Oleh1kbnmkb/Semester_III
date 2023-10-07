import sqlite3

def insert_var_data(name, email, joining_date, salary):
  try:
    sqlite_connection = sqlite3.connect("sqlite_python.db")

    cursor = sqlite_connection.cursor()

    sqlite_insert_query = """INSERT INTO sqlitedb_developers (name, email, joining_date, salary)
                          VALUES (?, ?, ?, ?);
                          """


    data_tuple = (name, email, joining_date, salary)


    cursor.execute(sqlite_insert_query, data_tuple)

    sqlite_connection.commit()
    cursor.close()


  except sqlite3.Error as error:
    print("Помилка підключення до", error)
  finally:
    if (sqlite_connection):
      sqlite_connection.close()
      print("Connection закрито")


insert_var_data("Ivan", "ivan5645@gmail.com", "2023-10-30", 5000)
insert_var_data("Petro", "petro56822@gmail.com", "2023-11-21", 9000)