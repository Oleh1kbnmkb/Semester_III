from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
class LoginForm(FlaskForm):
    nickname = StringField('Nickname', [validators.DataRequired()],)
    password = PasswordField('Nickname', [validators.DataRequired()],)
    submit = SubmitField("Log in")