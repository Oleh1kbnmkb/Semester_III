class Animal:
  def walk(self):
    print("I can walk and I can run")

  def eat(self):
    print("I can eat")

  def makeSound(self):
    print("Animal make sound")

class Dog(Animal):
  def bite(self):
    print("Woof-woof, I bite you")

  def makeSound(self):
    print("Woof-woof")


class Cat(Animal):
  def play(self):
    print("A am cat. A play with tail")


  def makeSound(self):
    print("Mayu-myau")


murka = Cat()
haski = Dog()

murka.walk()
haski.eat()
haski.makeSound()
murka.makeSound()