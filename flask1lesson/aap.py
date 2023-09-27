from flask import Flask, url_for, request, send_file, abort
import random as r


app = Flask(__name__)

@app.route("/")
def hello_world():
    c = 25 ** 2
    return f"Hello World! {c}"


@app.route("/horoscope/")
def hello_world2():
    list = ["Сьогодні у вас гарний день", "Вас чекають неприємності", "Вас чекає гарна звістка"]
    return r.choice(list)

@app.route("/login/")
def send_login():
  return send_file("C:/Python_1y_15_22/flask1lesson/tamplates/login.html")


@app.route("/login/", methods = ["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return "Request method POST - user name = %s" %user
    else:
        user = request.args.get("nane")
        return "Request method GET - user name = %s" %user

# @app.route("/url_for_test/")
# def url_for_test():
#     return url_for("hello")

# @app.route('/redirect-to-login-page')
# def redirected():
#     if user_name == "Admin":
#         abort(401)
#         return redirect(url_for('admin'))
#     else:
#         return redirect(url_for('login'))



def this_is_never_execute():
    pass

@app.route("/aborted-page/")
def aborted_page():
    abort(401)
    this_is_never_execute()

@app.errorhandler(404)
def page_not_found(error):
    return "такої сторінки немає", 404

@app.errorhandler(401)
def page_not_found(error):
     return "ДОСТУП ЗАБОРОНЕНО",



with app.test_request_context():
    print(url_for("send_login"))
    print(url_for("url_for_test"))
    print(url_for("hello_world2"))
    print(url_for("redirected"))
app.run(host="0.0.0.0", port=8080, debug=True)