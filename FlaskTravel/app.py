from flask import Flask, render_template, abort
import os
import data


app = Flask(__name__)


@app.route("/")
def index():
  return render_template("index.html",
                         departures=data.departures,
                         title=data.title,
                         subtitle=data.subtitle,
                         description=data.description,
                         tours=data.tours)



@app.route("/departures/<departure>/")
def departure(departure):
  tours2 = dict(filter(lambda tour: tour[1]["departure"] == departure, data.tours.items()))
  print(tours2)
  if tours2:
    return render_template("departure.html",
                           departure=departure,
                           title=data.title,
                           departures=data.departures,
                           tours=tours2)
  abort(404)



@app.route("/tours/")
def list_tours():
  return render_template("tour.html")



@app.route("/departures/")
def zero_departure():
  return render_template("index.html")


@app.route("/tours/<int:id>/")
def tours(id):
  return render_template("tour.html",
                         tour=data.tours[id],
                         title=data.title,
                         departures=data.departures)


app.run(port=25000, debug=True)