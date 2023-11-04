from flask import Flask, render_template, redirect, flash
from app import app
from forms import SignupForm, LoginForm
from models import Session, User
from flask_login import login_user
from  werkzeug.security import generate_password_hash, check_password_hash

@app.route("/singup/", methods=["GET", "POST"])
def singup():
    form = SignupForm()
    if form.validate_on_submit():
        session=Session()
        user = session.query(User).where(User.email == form.email.data).first()
        if user:
            flash("User currently exists")
            return redirect("login")

        pwd = generate_password_hash(form.password.data)
        user = User(
            nickname = form.email.data.split("@")[0],
            email = form.email.data,
            password = pwd,
        )
        session.add(user)
        session.commit()
        return redirect("login")

    return render_template("form_template.html", form=form)
