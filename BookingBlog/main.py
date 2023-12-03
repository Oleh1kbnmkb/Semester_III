from flask import Flask, render_template


app = Flask(__name__)



@app.route("/")
def hello_world():
  return 'Hello World'



app.run(port=59664, debug=True)