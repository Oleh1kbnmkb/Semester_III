from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'remarks.db'


def create_table():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS remarks(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      content TEXT NOT NULL
    )
  """)
  conn.commit()
  conn.close()


create_table()


@app.route("/")
def index():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM remarks ORDER BY id DESC")
  remarks = cursor.fetchall()
  conn.close()
  return render_template('index.html', remarks=remarks)


@app.route("/add/", methods=['POST'])
def add_remark():
    title = request.form.get('title')
    content = request.form.get('content')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO remarks (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))





@app.route("/notes")
def notes():
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM remarks")
    data = cursor.fetchall()
    connection.close()

    return render_template('notes.html', data=data)


@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    new_title = request.form.get('new_title')
    new_content = request.form.get('new_content')

    if new_title is not None and new_title.strip() != "":
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('UPDATE remarks SET title = ?, content = ? WHERE id = ?', (new_title, new_content, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    else:
        return redirect(url_for('error_page'))



@app.route('/delete/<int:id>')
def delete(id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM remarks WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



if __name__ == "__main__":
  app.run(debug=True)