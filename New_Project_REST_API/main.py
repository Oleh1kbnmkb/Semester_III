from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class NutritionInfo(Resource):
  def __init__(self, proteins, carbs, fats):
    self.proteins = proteins
    self.carbs = carbs
    self.fats = fats

  def energy(self):
    return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)

  def to_dict(self):
    return {
      'proteins': self.proteins,
      'carbs': self.carbs,
      'fats': self.fats,
    }

  @staticmethod
  def bmi(weight, height):
    return weight / (height ** 2)

  @classmethod
  def calories(cls, gender, age, height, weight, activity_level):
    if gender.lower() == 'male':
      calories_result = 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
    elif gender.lower() == 'female':
      calories_result = 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
      return None


    activity_factors = {
      'sedentary': 1.2,
      'lightly_active': 1.375,
      'moderately_active': 1.55,
      'very_active': 1.725,
      'extra_active': 1.9
    }

    if activity_level.lower() in activity_factors:
      calories_result *= activity_factors[activity_level.lower()]
    else:
      return None

    return calories_result



@app.route("/sum", methods=["POST"])
def sum():
  nutrition_info_1 = request.json["nutrition_info_1"]
  nutrition_info_2 = request.json["nutrition_info_2"]

  nutrition_info_sum = NutritionInfo(
    int(nutrition_info_1['proteins']) + int(nutrition_info_2['proteins']),
    int(nutrition_info_1['carbs']) + int(nutrition_info_2['carbs']),
    int(nutrition_info_1['fats']) + int(nutrition_info_2['fats']),
  )

  return jsonify(nutrition_info_sum.to_dict())


@app.route("/bmi", methods=["POST"])
def bmi():
  weight = float(request.json["weight"])
  height = float(request.json["height"])
  bmi_result = NutritionInfo.bmi(weight, height)
  return jsonify({'bmi': bmi_result})


@app.route("/calories", methods=["POST"])
def calories():
  gender = request.json["gender"]
  age = int(request.json["age"])
  height = float(request.json["height"])
  weight = float(request.json["weight"])
  activity_level = request.json["activity_level"]

  calories_result = NutritionInfo.calories(gender, age, height, weight, activity_level)

  if calories_result is not None:
    return jsonify({'calories': calories_result})
  else:
    return jsonify({'error': 'Invalid input or gender not specified'}), 400


if __name__ == '__main__':
  app.run(debug=True, port=25000)
