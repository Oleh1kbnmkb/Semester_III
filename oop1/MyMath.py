class MyMath:
  @staticmethod
  def add(a, b):
    return a + b
  
  
  @staticmethod
  def multiply(a, b):
    return a * b
  
  
c = MyMath.add(5, 5)
d = MyMath.multiply(5, 5)

print(c, d)
  