#1. Python Inner Class
"""
-> An inner class is a class defined inside another class.
-> The inner class can access the properties and methods of the outer class.
-> Inner classes are useful for grouping classes that are only used in one place, making code more organized.
"""
class Outer:
  def __init__(self):
    self.name = "Outer Class"

  class Inner:
    def __init__(self):
      self.name = "Inner Class"

    def display(self):
      print("This is the inner class")

outer = Outer()
print(outer.name)




#2. Accessing Inner Class From The Outside
"""
-> To access the inner class, we should create an object of the outer class, and then create an object of the inner class.
"""

class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()



#3. Accessing Outer Class From Inner Class
"""
-> Inner classes in Python do not automatically have access to the outer class instance.
-> If we want the inner class to access the outer class, we need to pass the outer class instance as a parameter.
"""
class Outer:
  def __init__(self):
    self.name = "Emil"

  class Inner:
    def __init__(self, outer):
      self.outer = outer

    def display(self):
      print(f"Outer class name: {self.outer.name}")

outer = Outer()
inner = outer.Inner(outer)
inner.display()






#4. Practical Example Of Using Inner Class
"""
-> Inner classes are useful for creating helper classes that are only used within the context of the outer class.
"""
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model
    self.engine = self.Engine() 

  class Engine:
    def __init__(self):
      self.status = "Off"

    def start(self):
      self.status = "Running"
      print("Engine started")

    def stop(self):
      self.status = "Off"
      print("Engine stopped")

  def drive(self):
    if self.engine.status == "Running":
      print(f"Driving the {self.brand} {self.model}")
    else:
      print("Start the engine first!")

car = Car("Toyota", "Corolla")
car.drive()
car.engine.start()
car.drive()




#5. Multiple Inner Classes
"""
-> A class can have multiple inner classes.
"""
class Computer:
  def __init__(self):
    self.cpu = self.CPU()
    self.ram = self.RAM()

  class CPU:
    def process(self):
      print("Processing data...")

  class RAM:
    def store(self):
      print("Storing data...")

computer = Computer()
computer.cpu.process()
computer.ram.store()