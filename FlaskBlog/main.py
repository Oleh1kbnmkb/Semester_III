from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


connection = sqlite3.connect("database.db")
with open("shema.sql") as f:
  connection.executescript(f.read())

cursor = connection.cursor()

cursor.execute("INSERT INTO posts (title, content) VALUES(?, ?)",
               ("First Post", "Content for the first post"))


cursor.execute("INSERT INTO posts (title, content) VALUES(?, ?)",
               ("Second Post", "Content for the second post"))


connection.commit()
connection.close()


@app.route("/")
def index():
  conn = get_db_connection()
  posts = conn.execute("SELECT * FROM posts").fetchall()
  conn.close()
  return render_template("index.html", posts=posts)



def get_db_connection():
  conn = sqlite3.connect("database.db")
  conn.row_factory = sqlite3.Row
  return conn


if __name__ == '__main__':
  app.run(port=53000, debug=True)