from flask import Flask, render_template
import random as r

app = Flask(__name__)

# hero = ["Waerrior 1", "Mag 1", "Wizard 1", "Archer 1", "Orc 1"]


max_score = 100
test_name = "Python Challenge"
stundents = [
    {"name": "Vlad", "scorer": 90},
    {"name": "Svyt", "scorer": 56},
    {"name": "Alex", "scorer": 78},
    {"name": "Rimma", "scorer": 100},
    {"name": "Oleh", "scorer": 99},
    {"name": "Yaroslav", "scorer": 90},
    {"name": "Timofei", "scorer": 85}
]
@app.route("/")
def hello_world2():
    return render_template("base.html", title="All work fine")

@app.route("/index/")
def index():
    return render_template("base.html", title="All work fine")

@app.route("/results/")
def results():
    context= {
        "title": "Results",
        "students": stundents,
        "test_name": test_name,
        "max_score": max_score
    }
    return render_template("results.html", **context)


app.run(host="0.0.0.0", port=9000, debug=True)