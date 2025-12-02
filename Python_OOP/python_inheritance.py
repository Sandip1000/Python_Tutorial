#1. Python Inheritance
"""
-> Inheritance allows us to define a class that inherits all the methods and properties from another class.
-> Parent class is the class being inherited from, also called base class.
-> Child class is the class that inherits from another class, also called derived class.
"""




#2. Creating A Parent Class
"""
-> Any class can be a parent class, so the syntax is the same as creating a other class.
"""
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()





#3. Creating a Child Class
"""
-> To create a class that inherits the functionality from another class, we have to send the parent class as a parameter when creating a child class.
-> We can use the "pass" keyword when we do not want to add any other properties or methods to the class.
"""

class Student(Person):   #Student class inherits all the properties and methods from Person class
  pass


x = Student("Mike", "Olsen")  #Now, the Student class has the same properties and methods as the Person class
x.printname()




#4. Adding The __init__() Function In Chlild Class
"""
-> So far we have created a child class that inherits the properties and methods from its parent.
-> We want to add the __init__() function to the child class(instead of the pass keyword).
-> The __init__() function is called automatically everytime the class is being used to create a new object.
-> When we add the __init__() function, the child class will no longer inherit the parent's __init__() function.
-> The child's __init__() function overrides the inheritance of the parent's __init__() function.
-> To keep the inheritance of the parent's __init__() function, we should add a call to the parents's __init__() function.
-> Now we have sucessfully added the __init__() function, and kept the inheritance of the parent class, and we are ready to add functionality in the __init__() function.
"""
class Student(Person):
  def __init__(self, fname, lname):   #Overrides the parent's __init__() function
    self.fname=fname
    self.lname=lname



class Student(Person):
  def __init__(self, fname, lname):   #We can add additional properties in this __init__() function
    Person.__init__(self, fname, lname)    #Adds the properties and method of parent's class






#5. Use Of super() Function
"""
-> Python also has a super() function that will make the child class inherit all the methods and properties from its parent.
-> By using the super() function, we do not have to use the name of the parent element, it will automatically inherit the methods and properties from its parent.
"""
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)




#6. Adding Properties In Child Class
"""
-> We can add the new property in the child class using __init__() method of child class and inherit all the parent's class properties using super() function.
"""
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)





#7. Adding Methods In Child Class
"""
-> We can also add new methods in the child class.
-> If we add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overidden.
"""
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)



x = Student("Mike", "Olsen", 2019)
x.welcome()





#8. Examples of Inheritance

class Person:
    def __init__(self, name, age, address):
        self.name=name
        self.age=age
        self.address=address

    def display_info(self):
        print("I am displaying Personal Info.")
        print("Name:", self.name)
        print("Age: ", self.age)
        print("Address: ", self.address)

    def person_method(self):
        print("I am a person")

class Student(Person):

    def __init__(self, name, age, address, university):
        super().__init__(name, age, address)
        self.university=university

    #Person class has same method display_info(), so to inherit that method we use super() function
    #And if the parent class and child class has a same name of function then the function of the child class will override the function of parent class
    def display_info(self):
        super().display_info()
        print("I am displaying Student Info.")
        print("University: ", self.university)
    
    def student_method(self):
        print("I am a Student and I can Study")


#Creating object of subclass
student1=Student("Hari",25,"Lalitpur","Tribhuvan University")
student1.display_info()
student1.person_method()
student1.student_method()





import math
class Shape:
    def __init__(self):
       pass 
    def area(self):
        pass
    def perimeter(self):
        pass
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    
    def area(self):
        return self.length*self.breadth
    
    def perimeter(self):
        return 2*(self.length+self.breadth)
    
class Circle(Shape):
    def __init__(self, radius):
       self.radius=radius
    
    def area(self):
       return math.pi*self.radius*self.radius
    
    def perimeter(self):
       return 2*math.pi*self.radius
    

rec=Rectangle(10,20)
print(f"Area of a rectangle: {rec.area()}")
print(f"Perimeter of a rectangle: {rec.perimeter()}")
    
cir=Circle(7)
print(f"Area of a circle : {cir.area()}")
print(f"Circumference of a circle : {cir.perimeter()}")

