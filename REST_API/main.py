import random

from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
import random as r
from db_connection import get_db_connection, get_quote, limit, create, update, delete
from flask_cors import CORS
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
api = Api(app)
CORS(app)
SWAGGER_URL = "/swagger"
API_URL = "/FRONTEND/swagger.json"


swagger_ui_blueprint = get_swaggerui_blueprint(
   SWAGGER_URL,
   API_URL,
   config={
       'app_name': 'Access API'
   }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

def row_to_json(quote):
  data = {'id': quote["id"], "author": quote["author"], "quote": quote["quote"]}
  json_data = jsonify(data)
  json_data.status_code=200
  return json_data


class Quote(Resource):
  def get(self, id=0):
    if id == 0:
      count_of_records = limit()
      quote = get_quote(r.randint(1, count_of_records))
      quote_json = row_to_json(quote)
      return quote_json
    quote = get_quote(id)
    if quote:
      quote_json = row_to_json(quote)
      return quote_json
    return "Quote not found", 404


  def post(self):
    parser = reqparse.RequestParser()

    parser.add_argument('author')
    parser.add_argument('quote')

    params = parser.parse_args()
    answer = create(params['author'], params['quote'])
    json_data = jsonify(f'Records create with id {answer}')
    json_data.status_code = 201
    return json_data

  def put(self, id):
    parser = reqparse.RequestParser()

    parser.add_argument('author')
    parser.add_argument('quote')
    params = parser.parse_args()
    update(id, params['author'], params['quote'])
    json_data = jsonify(f'Records edit with id {id}')
    json_data.status_code = 201
    return json_data


  def delete(self, id):
    delete(id)
    json_data = jsonify(f'Records delete with id {id}')
    json_data.status_code = 202
    return json_data

api.add_resource(Quote, "/api/v1.0/quotes", "/api/v1.0/quotes/", "/api/v1.0/quotes/<int:id>")


app.run(port=32560, debug=True)
