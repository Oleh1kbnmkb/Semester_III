from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DATABASE = 'task.db'

def create_table():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("""
    CREATE TABLE IF NOT EXISTS task(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      description TEXT NOT NULL,
      completed BOOLEAN NOT NULL
    )
  """)
  conn.commit()
  conn.close()

create_table()


@app.route("/")
def index():
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM task ORDER BY id DESC")
  tasks = cursor.fetchall()
  conn.close()
  return render_template('index.html', tasks=tasks)



@app.route("/add/", methods=['POST'])
def add():
  description = request.form.get('description')
  conn = sqlite3.connect(DATABASE)
  cursor = conn.cursor()
  cursor.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (description, False))
  conn.commit()
  conn.close()



  @app.route('/update/<int:task_id>', method=['POST'])
  def update(task_id):
    new_name = request.form.get('new_name')
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('UPDATE tasks SET user_name = ? WHERE id  = ?', (new_name, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))



  @app.route('/delete/<int:task_id>')
  def delete(task_id):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
