from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)




@app.route("/")
def index():
    return render_template('index.html', title1="Oderman - Піцерія", title2="PizzaMondo", title3="Меню")



@app.route("/menu/")
def menu():
    connection = sqlite3.connect('menu.db')
    cursor = connection.cursor()
    cursor.execute("SELECT name, description, price FROM menu")
    menu_data = cursor.fetchall()
    connection.close()

    return render_template('menu.html', title1="Меню", menu=menu_data)



@app.route("/add_pizza/")
def add_foods():
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        with sqlite3.connect("menu.db") as pizza:
            cursor = pizza.cursor()
            cursor.execute("INSERT INTO PARTICIPANTS\
                           (name, description, price) VALUES (?, ?, ?)"), (name, description, price)
            pizza.commit()
    return render_template('add_pizza.html')


@app.route("/participants")
def participants():
    connect = sqlite3.connect ('menu.db')
    cursor = connect.cursor()
    cursor.execute("SELECT * FROM PARTICIPANTS")
    data = cursor.fetchall()
    return render_template ("menu.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)
