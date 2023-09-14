class BankAcount:
  def __init__(self, name, balance, password):
    self.__name = name
    self.__balance = balance
    self.__password = password

  def __str__(self):
    return f"User {self.__name} have {self.__balance}"


  def getBalance(self):
    return self.__balance

  def setBalance(self, new_balance):
    if new_balance > 100:
      self.__balance = new_balance
    else:
      print("Error")




acount1 = BankAcount("Sergiy Ivanov", 5000, "MPSL56256DK5W4D")


print(acount1)

acount1.setBalance(10000)
print(acount1.getBalance())


