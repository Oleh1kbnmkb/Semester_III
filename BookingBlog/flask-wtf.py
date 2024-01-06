import flask
from flask import Flask, render_template, request
import flask_wtf
import wtforms
import random as r

app = Flask(__name__)


app.secret_key = 'Oleh'

class SubscriptionForm(flask_wtf.FlaskForm):
  name = wtforms.StringField("Name")
  email = wtforms.StringField("Email")
  submit = wtforms.SubmitField("Subscribe")



class IcecreamForm(flask_wtf.FlaskForm):
  tastes = wtforms.StringField("Смак")
  topping = wtforms.SelectMultipleField("Топінг")
  cup_size = wtforms.RadioField("Стаканчик")
  submit = wtforms.SubmitField("Відправити")



class MonetForm(flask_wtf.FlaskForm):
  monet_name = wtforms.StringField("Назва")
  monet_year = wtforms.StringField("Рік")
  monet_price = wtforms.StringField("Ціна")
  monet_size = wtforms.RadioField("Розмір")
  submit = wtforms.SubmitField("Відправити")


@app.route("/subscribe/", methods=["GET", "POST",])
def subscribe():
  form = SubscriptionForm()
  if flask.request.method == "GET":
    return render_template("subscribe.html", form=form)
  return form.email.data



@app.route("/ice", methods=["GET", "POST",])
def ice():
  form = IcecreamForm()
  form.tastes.choices = [("vanila", "vanila"), ("choko", "choko"), ("mango", "mango")]
  form.topping.choices = [("coffe", "coffe"), ("strawberry", "strawberry"), ("kiwi", "kivi")]
  form.cup_size.choices = [("small", "small"), ("middle", "middle"), ("big", "big")]
  if request.method == "GET":
    return render_template("icecream.html", form=form)
  return form.tastes.data


@app.route("/ice_vegan", methods=["GET", "POST",])
def ice_vegan():
  form = IcecreamForm()
  form.tastes.choices = [("vanila", "vanila"), ("grass", "grass"), ("tomato", "tomato")]
  form.topping.choices = [("coffe", "coffe"), ("strawberry", "strawberry"), ("lemon", "lemon")]
  form.cup_size.choices = [("small", "small"), ("middle", "middle"), ("big", "big")]
  if request.method == "GET":
    return render_template("icecream_vegan.html", form=form)
  return form.tastes.data



@app.route("/monet/", methods=["GET", "POST",])
def monet():
  form = MonetForm()
  form.monet_size.choices = [("small", "small"), ("middle", "middle"), ("big", "big")]
  if request.method == "GET":
    return render_template("monet.html", form=form)
  return form.monet_name.data


app.run(debug=True, port=95000)