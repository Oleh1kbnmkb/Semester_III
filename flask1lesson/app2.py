from flask import Flask, render_template

works = [
    {"working": "Telegram-bot", "year": 2023},
    {"working": "Game", "year": 2022},
    {"working": "Сайт", "year": 2023}
]



app = Flask(__name__, template_folder='templates', static_folder='static')
@app.route('/')
def index():
  context = {
    "title": "Portfolio",
    "portfolio": works
  }
  return render_template('index.html', **context)



app.run(host="0.0.0.0", port=8000, debug=True)