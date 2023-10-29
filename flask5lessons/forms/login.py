from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class LoginForm(FlaskForm):
  nickname = StringField('Nickname1', [validators.DataRequired()],)
  password = PasswordField('Password1', [validators.DataRequired()],)
  submit = SubmitField("Log in")