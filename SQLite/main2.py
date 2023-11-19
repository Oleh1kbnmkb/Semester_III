from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'users.db'


def create_table():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
      user_id INTEGER PRIMARY KEY AUTOINCREMENT,
      user_name TEXT NOT NULL,
      user_email TEXT NOT NULL
    )
  """)
  conn.commit()
  conn.close()


create_table()


@app.route("/")
def index():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM users ORDER BY user_id DESC")
  users = cursor.fetchall()
  conn.close()
  return render_template('index.html', users=users)


@app.route("/add", methods=['POST'])
def add():
    user_name = request.form.get('user_name')
    user_email = request.form.get('user_email')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (user_name, user_email) VALUES (?, ?)", (user_name, user_email))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))



@app.route('/update/<int:user_id>', methods=['POST'])
def update(user_id):
    new_user_name = request.form.get('new_user_name')
    new_user_email = request.form.get('new_user_email')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET user_name = ?, user_email = ? WHERE user_id = ?', (new_user_name, new_user_email, user_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



@app.route('/delete/<int:user_id>')
def delete(user_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM users WHERE user_id = ?', (user_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



if __name__ == "__main__":
  app.run(debug=True)