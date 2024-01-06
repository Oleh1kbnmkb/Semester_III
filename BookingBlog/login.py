import flask
from flask import Flask, render_template, request
import flask_wtf
import wtforms
import random as r

app = Flask(__name__)


app.secret_key = 'Oleh'



class RegistrationForm(flask_wtf.FlaskForm):
  email = wtforms.StringField('Пошта')
  password = wtforms.PasswordField('Пароль')
  submit = wtforms.SubmitField('Відправити')
  remember = wtforms.BooleanField("Запам'ятати мене")



@app.route('/register/', methods=['GET','POST',])
def register():
  form = RegistrationForm()
  if flask.request.method == 'GET':
    return flask.render_template('registration.html', form=form)
  return form.email.data





app.run(debug=True, port=55000)