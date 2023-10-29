from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class SignupForms(FlaskForm):
  email = StringField('Email', [validators.DataRequired(), validators.Email(),],)
  password = PasswordField('Password', [validators.DataRequired()], )
  submit = SubmitField("Sign up")