import flask
from flask import Flask, render_template, request
import random as r

app = Flask(__name__)


@app.route("/search/")
def flask_search():
  return render_template("search.html")


@app.route("/search2/")
def flask_search2():
  return render_template("mail_search.html")


@app.route("/getsearch/")
def get_search():
    mail = flask.request.args.get("mail")
    return f"Сторінка пошуку через гет, пошук по {mail}"


@app.route("/postsearch/", methods=["GET", "POST"])
def post_search():
  mail = flask.request.args.get("mail")
  return f"Сторінка пошуку через пост, пошук по {mail}"


@app.route("/dosearch/")
def flask_do():
  s = flask.request.args.get("s")
  return f"Це сторінка пошуку. Пошук по {s}"



@app.route("/calculate/")
def flask_form_calculate():
  a = flask.request.args.get("a")
  b = flask.request.args.get("b")
  s = int(a) + int(b)
  d = flask.request.args.get("d")
  return f"Це сторінка пошуку. Пошук по {s}"


app.run(debug=True, port=87500)