import flask
from flask import Flask, render_template, request
import flask_wtf
import wtforms
import random as r


app = Flask(__name__)


app.secret_key = 'Oleh'
import json



@app.route("/test")
def test():
  with open("users.json") as f:
    users = json.load(f)
    for user in users:
      print(user["name"])

  users.append({"name": "Ira", "email": "ira@gmail.com"})

  with open("users.json", "w") as f:
    json.dump(users, f, indent=4, ensure_ascii=False)
  return flask.jsonify(users)

app.run(debug=True, port=56822)