from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from data import tours


app = Flask(__name__)
DATABASE = 'users.db'



def create_table():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
    )
  """)
  conn.commit()
  conn.close()

create_table()



# Login app_route
@app.route("/", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    else:
        return render_template("register.html")


@app.route("/login/", methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
      return redirect(url_for('index'))
    else:
      return "Incorrect username or password. Please try again."
  else:
    return render_template("login.html")


@app.route("/home/")
def index():
  return render_template("index.html", tours=tours)



@app.route('/house/<int:id>/')
def show_tour(id):
    tour = tours.get(id)
    if tour:
        return render_template('tours.html', tour=tour)
    else:
        return "Тур не знайдено", 404



@app.route("/tours_houses/")
def tours_houses():
  return render_template("tours_houses.html", tours=tours)


@app.route("/buy_houses/")
def buy_houses():
  return render_template("buy_houses.html")


@app.route("/about_us/")
def about_us():
  return render_template("aboutus.html")


@app.route("/our_contacts/")
def our_contacts():
  return render_template("our_contacts.html")


@app.route("/search/", methods=['POST'])
def search():
    country = request.form['country'].lower()
    matching_tours = [tour for tour in tours.values() if tour['country'].lower() == country]
    return render_template('search.html', tours=matching_tours)



app.run(port=50000, debug=True)