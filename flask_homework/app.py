from flask import Flask, render_template, request, abort, redirect, url_for, flash
import sqlite3
import requests
import random

app = Flask(__name__)

app.config['SECRET_KEY'] = "Your secret key"


API_KEY = 'bddebc304257efa7289dcdb93bebeee5'

def get_current_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

pizza1 = ['Пепероні', 'Маргариту', 'Мексиканську', 'Фреш салямі']
pizza2 = ['Гавайську', 'Піца з морепродуктами', 'Капоне з цибулею', '	Піца Далі', 'Чізі-бум']


def recommend_food(temperature):
    if temperature < 15:
        return f'Зараз холодно! Спробуйте щось гостіше, наприклад {random.sample(pizza1, k=1)[0]}'
    elif temperature > 15:
        return f'Температура досить висока! Спробуйте нову нашу піцу з морепродуктами {random.sample(pizza2, k=1)[0]}'
    else:
        return 'Також можете спробувати інші наші страви з меню'


@app.route('/')
def index():
    city = 'Київ'
    current_weather = get_current_weather(city)
    if current_weather:
        temperature = current_weather['main']['temp']
        food_recommendation = recommend_food(temperature)
    else:
        food_recommendation = None

    return render_template('index.html', current_weather=current_weather, title1="PizzaMondo", food_recommendation=food_recommendation)



@app.route("/menu/")
def menu():
    connection = sqlite3.connect('menu.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu")
    menu_data = cursor.fetchall()
    connection.close()

    return render_template('menu.html', title1="Меню", data=menu_data)


@app.route('/pizza_details/<pizza_name>')
def pizza_details(pizza_name):
    pizza = get_name(pizza_name)

    if pizza:
        pizza_details = {
            'name': pizza['name'],
            'description': pizza['description'],
            'price': pizza['price']
        }
        return render_template('pizza_details.html', pizza_details=pizza_details)
    else:
        abort(404)



@app.route("/add_pizza/", methods=["GET", "POST"])
def add_pizza():
    current_weather = get_current_weather(city="Київ")
    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']

        with sqlite3.connect("menu.db") as pizza:
            cursor = pizza.cursor()
            cursor.execute("INSERT INTO menu\
                           (name, description, price) VALUES (?, ?, ?)", (name, description, price))
            pizza.commit()
            return render_template('index.html', current_weather=current_weather)
    else:
        return render_template('join.html')




@app.route("/<pizza_name>/delete/", methods=("GET", "POST"))
def delete(pizza_name):
    if request.method == "POST":
        if pizza_name:
            connection = get_db_connection()
            connection.execute("DELETE FROM menu WHERE name = ?", (pizza_name,))
            connection.commit()
            connection.close()

        return redirect(url_for("menu"))


@app.route("/<pizza_name>/edit/", methods=("GET", "POST"))
def edit(pizza_name):
    connection = get_db_connection()
    pizza_details = connection.execute("SELECT * FROM menu WHERE name = ?", (pizza_name,)).fetchone()
    connection.close()

    if request.method == "POST":
        name = request.form['name']
        description = request.form['description']
        price= request.form['price']

        if not name:
            flash("Name is required")
            return redirect(url_for("edit", pizza_name=pizza_name))
        else:
            connection = get_db_connection()
            connection.execute("UPDATE menu SET name=?, description=?, price=? WHERE name=?", (name, description, price, pizza_name,))
            connection.commit()
            connection.close()

            flash("Pizza updated successfully")
            return redirect(url_for("index"))

    return render_template("edit.html", pizza_details=pizza_details or {})



@app.route("/<pizza_name>/order/", methods=("GET", "POST"))
def order(pizza_name):
    return render_template("order.html", pizza_name=pizza_name)

def get_db_connection():
  conn = sqlite3.connect("menu.db")
  conn.row_factory = sqlite3.Row
  return conn



def get_name(post_name):
  conn = get_db_connection()
  post = conn.execute("SELECT * FROM menu WHERE NAME = ?", (post_name,)).fetchone()
  conn.close()
  if post is None:
    abort(404)
  return post



if __name__ == '__main__':
    app.run(debug=False)