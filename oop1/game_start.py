from gameRPG import Archer,Warior


print("Welcome to the game!")
name = input("Enter your name> ")
answer = 0

while answer not in [1, 2]:
  answer = int(input("Chose you role\n1: Archer 2: Warior "))
  if answer == 1:
    hero = Archer(1)
  elif answer == 2:
    hero = Warior(1)

  else:
    print("Error! Try again")

print(hero)
enewy1 = Warior(1)
print(enewy1.hp)

enewy1.hp -= hero.attack_func()
enewy1.hp -= hero.attack_func()
enewy1.hp -= hero.attack_func()

print(enewy1.hp)