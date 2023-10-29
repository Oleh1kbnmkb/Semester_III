from flask import render_template
from app import app
from forms import LoginForm, SignupForm

@app.route("/signup/", methods=["GET", "POST"])
def signup():
  form = SignupForm()
  return render_template("form_templates", form=form)


@app.route("/login/", methods=["GET", "POST"])
def login():
  form = LoginForm()
  return render_template("form_templates", form=form)