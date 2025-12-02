#1. The self Parameter
"""
-> The "self" parameter is a reference to the current instance of the class.
-> It is used to access the properties and method that belong to the class.
-> The "self" parameter must be the first parameter of any method in the class.
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)
    print("I am ", self.age ," years old.")

p1 = Person("Emil", 25)
p1.greet()



#2. Why To Use self?
"""
-> Without "self", Python would not know which object's properties we want to access.
-> The "self" parameter links the method to the specific object.
"""
class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()



#3. self Does Not Have To Be Named "self"
"""
-> It does not have to be named "self", we can call it whatever we like, but it has to be the first parameter of any method in the class.
-> While we can use a different name, it is strongly recommended to use "self" as it is the convention in Python and makes our code more readable to others.
"""

class Person:
  def __init__(myobject, name, age):   #Using word myobject instead of self
    myobject.name = name
    myobject.age = age

  def greet(abc): #Using word abc instead of self
    print("Hello, my name is " + abc.name)

p1 = Person("Emil", 36)
p1.greet()





#4. Accessing Properties With self
"""
-> We can access any property of the class using "self".
"""
class Car:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year

  def display_info(self):
    print(f"{self.year} {self.brand} {self.model}")

car1 = Car("Toyota", "Corolla", 2020)
car1.display_info()






#5. Calling Methods With self
"""
-> We can also call other methods within the class using "self".
"""
class Person:
  def __init__(self, name):
    self.name = name

  def greet(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet()
    print(message + "! Welcome to our website.")

p1 = Person("Tobias")
p1.welcome()