from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')


status = 'В обробці'

post = [
  {"status": 'В обробці'},
  {"status": 'В обробці'},
  {"status": 'В обробці'},
  {"status": 'В обробці'},
  {"status": 'Відправлено'},
  {"status": 'Відправлено'},
  {"status": 'Відправлено'}
]



products = [
  {'name': 'Cucember', 'price': 100, 'description': 'Green vegetable'},
  {'name': 'Tomato', 'price': 40, 'description': 'Red vegetable'},
  {'name': 'Milk', 'price': 2, 'description': 'White product'},
  {'name': 'Banana', 'price': 75, 'description': 'Yellow product'}
]

context = {
  'post': products
}
@app.route("/results/")
def hello_world():
  return render_template("results.html", **context)


app.run(host="0.0.0.0", port=9009, debug=True)