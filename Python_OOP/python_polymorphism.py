#1. Python Polymorphism
"""
-> The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
   with the same name that can be executed on many objects or classes. 
"""




#2. Function Polymorphism
"""
-> An example of a Python function that can be used in different objects is the len() function.
"""

#String
x = "Hello World!"

print(len(x))           #For strings len() function returns the number of characters in string



#Tuple
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))     #For tuples len() function returns the number of items in tuple



#Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))    #For dictionaries len() function returns the number of key/value pairs in the dictionary






#3. Class Polymorphism
"""
-> Polymorphism is often used in class methods, where we can have multiple classes with the same method name.
-> For example, say we have three classes: Car, Boat, and Plane, and they all have a method called move().
"""
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()






#4. Inheritance Class Polymorphism
"""
-> Child classes inherits the properties and methods from the parent class.
-> In the example below we can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.
-> The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but both overide the move() method.
-> Because of polymorphism we can execute the same method for all classes.
"""
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()




