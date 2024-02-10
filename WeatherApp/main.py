from flask import Flask, render_template, jsonify, request
import requests
from secret import openweather_api_key
from service import extracted_weather_data
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route("/get_weather/")
def get_weather():
  location = request.args.get('location')
  if location:
    url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={openweather_api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
  else:
    return jsonify(error='Location not provided'), 400



@app.route("/get_weather_forecast/")
def get_weather_forcast():
  location = request.args.get('location')
  if location:
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={location}&appid={openweather_api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    forecast = []
    print(data)
    for entry in data["list"]:
      extracted_data = extracted_weather_data(entry)
      forecast.append(extracted_data)
    return jsonify(forecast)
  else:
    return jsonify(error='Location not provided'), 400




app.run(debug=True, port=5000)