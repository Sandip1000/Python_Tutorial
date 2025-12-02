#1. The __init__ Method
"""
-> All classes have a built-in method called __init__(), which is always executed when the class is being initiated.
-> The __init__() method is used to assign values to object properties, or to perform operations that are necessary 
   when the object is being created.
-> The __init__() method is called automatically every time the class is being used to create a new object.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)




#2. Why To Use __init__()?
"""
-> Without the __init__() method, we would need to set properties manually for each object.
-> Using __init__() method, makes it easier to create objects with initial vlaues.
"""


#Without Using __init__() Method
class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)




#With Using __init__() Method
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 28)

print(p1.name)
print(p1.age)





#3. Default Values In __init__() Method
"""
-> We can also set default values for parameters in the __init__() method.
"""
class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)




#4. Multiple Parameters
"""
-> The __init__() method can have as many parameters as we need.
"""
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
