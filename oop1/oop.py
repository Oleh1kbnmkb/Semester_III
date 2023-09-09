class User:
  def __init__(self, name, last_name, age):
    self.name = name
    self.last_name = last_name
    self.age = age
    
  def print_user(self):
    print(f"User {self.name} {self.last_name} {self.age}")
    
  def change_name(self, name):
    if len(name) < 5:
      print("User name invalid")
    else:
      self.name = name
    
  
  
  
class Dog:
  def __init__(self, name, age, weight):
    self.name = name
    self.age = age
    self.weight = weight
    
  def bark(self):
    print("wof, wof")
    
    
dog1 = Dog('tuzic', 2, 5)

dog1.bark()