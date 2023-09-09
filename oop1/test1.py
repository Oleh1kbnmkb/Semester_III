from oop import User
import random as r
import math

user1 = User("Denis", "Bagrov", 66)
user2 = User("Kiril", "Danilov", 34)


user1.print_user()
print("--------------------------------------------")
user2.print_user()

user2.change_name("Ast")
print(user2.name)



print(user1.__dict__)

