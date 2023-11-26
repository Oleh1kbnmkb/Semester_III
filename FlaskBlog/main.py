from flask import Flask, render_template, abort, request, flash, redirect, url_for
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = "Your secret key"



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



@app.route("/<int:post_id>")
def post(post_id):
  post = get_post(post_id)
  return render_template("post.html", post=post)




@app.route('/<int:post_id>/edit', methods=("GET", "POST"))
def edit(post_id):
    post = get_post(post_id)
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        if not title:
            flash("Title is required")
        else:
            connection = get_db_connection()
            connection.execute("UPDATE posts SET title=?, content=? WHERE id=?",
                               (title, content, post_id))
            connection.commit()
            connection.close()
            return redirect(url_for("index"))
    return render_template("edit.html", post=post)




@app.route("/create", methods=('GET', 'POST'))
def create():
  if request.method == "POST":
    title = request.form['title']
    content = request.form['content']
    if not title:
      flash("Title is needed")
    else:
      connection = get_db_connection()
      connection.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
      connection.commit()
      connection.close()
      return redirect(url_for("index"))
  return render_template('create.html')




@app.route('/<int:post_id>/delete', methods=("POST",))
def delete(post_id):
  post = get_post(post_id)
  connection = get_db_connection()
  connection.execute("DELETE FROM posts WHERE id = ?", (post_id,))
  connection.commit()
  connection.close()
  return redirect(url_for("index"))




def get_db_connection():
  conn = sqlite3.connect("database.db")
  conn.row_factory = sqlite3.Row
  return conn



def get_post(post_id):
  conn = get_db_connection()
  post = conn.execute("SELECT * FROM posts WHERE ID = ?", (post_id,)).fetchone()
  conn.close()
  if post is None:
    abort(404)
  return post


if __name__ == '__main__':
  app.run(port=53000, debug=True)