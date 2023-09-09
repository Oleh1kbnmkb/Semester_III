# first_name1 = 'Oleh'
# last_name1 = 'Pavlov'
# age1 = 14

# first_name2 = 'Ivan'
# last_name2 = 'Ivanov'
# age2 = 25

# def print_user(first_name, last_name, age):
#   print(f"User {first_name}, {last_name}, {age}")
  
  
# print_user(first_name1, last_name1, age1)
# print_user(first_name2, last_name2, age2)


user1 = {
  "first_name":"Oleh",
  "last_name":"Pavlov",
  "age1": 14
}



user2 = {
  "first_name":"Ivan",
  "last_name":"Ivanov",
  "age": 25
}


def print_user(user):
  print(f"User {user['first_name']}")