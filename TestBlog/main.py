from flask import Flask, render_template
import random as r


app = Flask(__name__)


nearby_galaxies = {
  1:{'galaxy':'Canis Major Dwarf Galaxy', 'distance_trillionkm':236000000.56626, 'distance_ly':25000, 'description':'satellite of Milky Way'},
  2: {'galaxy':'Milky Way', 'distance_trillionkm': 223000000.5755156, 'distance_ly': 20000, 'description': 'home galaxy of Earth'},
  3: {'galaxy': 'Large Magellanic Cloud', 'distance_trillionkm': 250000000.5455455, 'distance_ly': 160000, 'description': 'home galaxy of Earth'},
}





@app.route("/")
def main():
  name = "user"
  randor = r.random()


  return render_template("test.html", data=name, mode=randor)




@app.route("/shop")
def shopping():
  restourant = {
    "pizza":["margarita", "giorgia", "tonna", "suprema"],
    "coffee":["rastretto", "latte", "ice - coffee", "espresso", "capuchino"]
  }

  return render_template("shop.html", data=nearby_galaxies)







app.run(port=59664, debug=True)