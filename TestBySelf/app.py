from flask import Flask, render_template, request
import os


app = Flask(__name__)

filename = "data.txt"


poll_data = {
  "question": "Which framework do you use?",
  "fields": ["Flask", "Django"],
  "correct": "Flask"
}


@app.route("/")
def root():
  return render_template("poll.html", data=poll_data)



@app.route("/poll")
def poll():
  vote = request.args.get('fields')
  out = open(filename, 'a')
  out.write(vote + '\n')
  out.close()
  if vote == poll_data.get("correct"):
    return render_template("thankyou.html", data=poll_data, votes=vote)
  else:
    return render_template("nothankyou.html", data=poll_data, votes=vote)





app.run(port=56995, debug=True)