from flask import Flask, render_template, request
import sqlite3
import requests

app = Flask(__name__)


API_KEY = 'bddebc304257efa7289dcdb93bebeee5'

def get_current_weather(city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None
@app.route('/')
def index():
    city = 'Київ'
    current_weather = get_current_weather(city)
    return render_template('index.html', current_weather=current_weather, title1="Oderman - Піцерія", title2="PizzaMondo")



@app.route("/menu/")
def menu():
    connection = sqlite3.connect('menu.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu")
    menu_data = cursor.fetchall()
    connection.close()

    return render_template('menu.html', title1="Меню", data=menu_data)



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





if __name__ == '__main__':
    app.run(debug=False)