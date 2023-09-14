# Клас для представлення продукту харчування
class Product:
    def __init__(self, name, calories, protein, fat, carbs):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbs = carbs

class Meal:

    def __init__(self, name) -> None:
        self.name = name
        self.products = []


    def add_products(self, product, grams):
        self.products.append({"product": product, "grams":grams})



    def sum_calories(self):
        total_calories = 0
        for item in self.products:
            product = item["product"]
            grams = item["grams"]
            calories_100g = product.calories
            total_calories += (calories_100g / 100) * grams
        return total_calories




    def meal_composition(self):
        print(f"Склад страви '{self.name}':")
        for item in self.products:
            product = item["product"]
            grams = item["grams"]
            print(f"{product.name} - {grams} грамів")
        print(f"Загальна кількість калорій: {self.sum_calories()} ккал")







# Приклад використання
apple = Product("Яблуко", 52, 0.2, 0.2, 14)
sugar = Product("Цукор", 387, 0, 0, 99.8)
dough = Product("Тісто", 100, 0.2, 10, 15)

meal = Meal("cake")
meal.add_products(apple, 100)
meal.add_products(sugar, 10)
meal.add_products(dough, 500)


meal.meal_composition()