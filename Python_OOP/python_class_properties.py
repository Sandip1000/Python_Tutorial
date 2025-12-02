#1. Class Properties
"""
-> Properties are the variables that belong to a class. 
-> They store data for each object created from the class.
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Emil", 36)

print(p1.name)
print(p1.age)





#2. Accessing Properties
"""
-> We can access object properties using dot(.) notation.
"""
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

car1 = Car("Toyota", "Corolla")

print(car1.brand)
print(car1.model)




#3. Modify Properties
"""
-> We can modify the value of properties on objects.
"""
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print(p1.age)




#4. Delete Properties
"""
-> We can delete properties from objects using the "del" keyword.
"""

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Linus", 30)

del p1.age

print(p1.name) # This works
#print(p1.age) # This would cause an error





#5. Class Properties Vs Object Properties
"""
-> Properties defined inside __init__() belong to each object(instance properties).
-> Properties defined outside methods belong to class itself(class properties) and are shared by all objects.
"""
class Person:
  species = "Human" # Class property

  def __init__(self, name):
    self.name = name # Instance property

p1 = Person("Emil")
p2 = Person("Tobias")

print(p1.name)
print(p2.name)
print(p1.species)
print(p2.species)






#6. Modifying Class Properties
"""
-> When we modify a class property, it affects all objects.
"""
class Person:
  lastname = ""

  def __init__(self, name):
    self.name = name

p1 = Person("Linus")
p2 = Person("Emil")

Person.lastname = "Refsnes"

print(p1.lastname)
print(p2.lastname)





#7. Adding New Properties
"""
-> We can add new property to an object.
-> Adding properties this way only adds them to that specific object, not to all objects of the class.
"""

class Person:
  def __init__(self, name):
    self.name = name

p1 = Person("Tobias")

p1.age = 25
p1.city = "Oslo"

print(p1.name)
print(p1.age)
print(p1.city)
