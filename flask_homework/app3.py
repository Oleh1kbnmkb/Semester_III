import sqlite3

def insert_var_data(name, description, price):
  try:
    sqlite_connection = sqlite3.connect("menu.db")

    cursor = sqlite_connection.cursor()

    sqlite_insert_query = """INSERT INTO menu (name, description, price)
                          VALUES (?, ?, ?);
                          """


    data_tuple = (name, description, price)


    cursor.execute(sqlite_insert_query, data_tuple)
    sqlite_connection.commit()
    cursor.close()


  except sqlite3.Error as error:
    print("Помилка підключення до", error)
  finally:
    if (sqlite_connection):
      sqlite_connection.close()
      print("Connection закрито")


# insert_var_data("Маргарита", "Томатний соус, моцарела, базилік", 10.99)
# insert_var_data("Пепероні", "Томатний соус, пепероні, моцарела", 12.99)
# insert_var_data("Гавайська", "Томатний соус, шинка, ананаси, моцарела", 11.99)
# insert_var_data("BBQ Цезар", "BBQ соус, куряче філе, салат, моцарела", 13.99)
# insert_var_data("Мексиканська", "Томатний соус, ковбаски, паперчі, моцарела", 14.99)
# insert_var_data("Вегетаріанська", "Томатний соус, броколі, гриби, моцарела", 11.99)
# insert_var_data("Фреш салямі", "Томатний соус, салямі, моцарела", 12.99)
# insert_var_data("Піца з морепродуктами", "Томатний соус, морські гребінці, креветки, моцарела", 15.99)
# insert_var_data("Чотири сири", "Томатний соус, моцарела, дор-блю, пармезан, фета", 12.99)
# insert_var_data("Піца Одерман", "Томатний соус, пепероні, гриби, моцарела, оливки, салат, помідори", 14.99)