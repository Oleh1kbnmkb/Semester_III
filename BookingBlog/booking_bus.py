import flask
from flask import Flask, render_template, request
import flask_wtf
import wtforms
import random as r


app = Flask(__name__)


app.secret_key = 'Oleh'

def is_luggage_weight_valid(form, field):
  if field.data > 30:
    raise wtforms.validators.ValidationError("Вага дуже велика")


class LuggageForm(flask_wtf.FlaskForm):
  surname = wtforms.StringField("Surname", validators=[wtforms.validators.InputRequired()])
  name = wtforms.StringField("Name", validators=[wtforms.validators.InputRequired()])
  password = wtforms.IntegerField("Card_id", validators=[wtforms.validators.InputRequired()])
  luggage = wtforms.IntegerField("Weight", validators=[wtforms.validators.InputRequired(),
                                                              is_luggage_weight_valid])
  submit = wtforms.SubmitField("Send")


@app.route("/luggage/", methods=["GET", "POST",])
def luggage():
  form = LuggageForm()
  if flask.request.method == "GET":
    return render_template("luggage.html", form=form)
  if form.validate_on_submit():
    return "ok"
  else:
    return f"{form.errors}"
  return form.name.data



app.run(debug=True, port=40000)