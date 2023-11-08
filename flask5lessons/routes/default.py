from flask import render_template
from app import app
from datetime import date, timedelta
import random as r
import requests
from models import Session, User, Event

@app.route("/")
def main():
    mock = {}
    for item in range(5):
        events = [
            requests.get("https://www.boredapi.com/api/activity/"),
            requests.get("https://www.boredapi.com/api/activity/"),
        ]
        event_date = date.today() + timedelta(days=item)
        date_str = event_date.strftime("%d %B")
        r1 = "event " + str(r.randint(1, 100))
        r2 = "event " + str(r.randint(100, 500))
        mock[date_str] = [event.json().get("activity") for event in events]

        session = Session()
        event1 = Event()
        event1.date = event_date
        event1.header = events[0].json().get("activity")
        event1.describe = events[1].json().get("activity")
        session.add(event1)
        session.commit()

    return render_template("main.html", iterable=mock)
