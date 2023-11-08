from flask import Flask, render_template, redirect, flash
from app import app
from forms import SignupForm, LoginForm
from models import Session, User
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        session = Session()
        user = session.query(User).where(User.email == form.email.data).first()
        if user:
            flash("User currently exists")
            return redirect("login")

        pwd = generate_password_hash(form.password.data)
        print("PASSWORD HASH=", pwd)
        user = User(
            nickname=form.email.data.split('@')[0],
            email=form.email.data,
            password=pwd,
        )
        session.add(user)
        session.commit()

        return redirect("login")
    return render_template("form_template.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        session = Session()
        print("form-data", form.nickname.data)
        user = session.query(User).where(User.nickname == form.nickname.data).first()
        print("user_before if=", user)
        if user:
            print("user_from if=", user)
            print("user.password=", user.password, "form.password=", form.password)
            if check_password_hash(user.password, form.password.data):
                print(check_password_hash(user.password, form.password.data))
                login_user(user)
                return redirect("/")
            flash("Wrong password")
            return redirect("login")
        flash("Wrong nickname")
        return redirect("login")
    return render_template("form_template.html", form=form)
