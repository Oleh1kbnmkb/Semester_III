from flask import Flask
from flask import render_template, request
from sqlalc import Session, Base, engine, create_db, drop_db
from group import Group
from sqlalchemy import select


app = Flask(__name__)

create_db()

@app.route("/")
def main():
    return render_template("main.html")

@app.route('/groups', methods=["GET", "POST"])
def group_management():
    with Session() as session:
        if request.method == "POST":
            session.add(Group(name=request.form.get('name')))
            session.commit()
        data = session.query(Group).all()

    return render_template('group/management.html', iterable=data,)


@app.route("/groups/<int:id>", methods=["GET"])
def group_get(id):
    with Session() as sesion:
        data = sesion.scalars(select(Group).where(Group.id == id)).first()
        print(data)

    return render_template("index.html", content=data)


if __name__ == '__main__':
    app.run()


