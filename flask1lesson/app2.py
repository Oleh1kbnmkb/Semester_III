from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')



max_score = 100
test_name = "Python Challenge"
students = [
  {"name": 'Vlad', "score": 100},
  {"name": 'Svyt', "score": 70},
  {"name": 'Alex', "score": 98},
  {"name": 'Rimma', "score": 50},
  {"name": 'Oleh', "score": 99},
  {"name": 'Yaroslav', "score": 80},
  {"name": 'Tim', "score": 71}
]
@app.route("/")
def hello_world():
  return render_template("base.html", title="Jinja2")

@app.route("/results/")
def results():
  context = {
    "title": "Results",
    "students": students,
    "test_name": test_name,
    "max_score": max_score
  }
  return render_template("results.html", **context)



app.run(host="0.0.0.0", port=9008, debug=True)