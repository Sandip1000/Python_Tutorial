#1. Property Method
"""
-> The @property decorator in Python is built-in tool that provides a Pythonic way to create managed
   attributes in classes. It allows us to use methods that behave exactly like attributes, enabling encapsulation, data
   validation, and dynamically computed values without changing the class's public interface.
-> The primary purpose of @property is to give us control over attribute access(getting, setting, or deleting) while maintaining clean, readable code.
-> It helps encapsulate data by using "private" variables(by convention, prefixed with an underscore, e.g., _attribute_name) and providing controlled access through public properties.
-> The setter method allows us to add validation or transformation logic before a value is stored, ensuring data integrity.
-> We can create attributes whose values are computed dynamically from other attributes, rather than being stored directly.
-> It allows us to refactor our internal implementaion(e.g., changing how data is stored) without breaking the code of users who interact with our class's public API.
"""

#Example 1
#Public
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age


person1=Person("Hari",10)

print(person1.name)
print(person1.age)



#Protected 
class Person:
    def __init__(self,name,age):
        self._name=name
        self._age=age

    def get_name(self):
        return self._name
    
    def get_age(self):
        return self._age
    
    def set_name(self,name):
        self._name=name
        
    def set_age(self,age):
        self._age=age

person1=Person("Hari",10)

print(person1.get_name())
print(person1.get_age())

person1.set_name("Ram")
person1.set_age(30)

print(person1.get_name())
print(person1.get_age())




#Using @property decorator for getter and setter methods

class Student:

    def __init__(self,name,age):
        self._name=name
        self._age=age


    @property
    def name(self):
        #Getter method for name
        print("Inside getter method for name")
        return self._name
    
    @property
    def age(self):
        #Getter method for age
        print("Inside getter method for age")
        return self._age

    @name.setter
    def name(self,name):
        print("Inside Setter method of name")
        self._name=name
    
    @age.setter
    def age(self,age):
        print("Inside Setter method of age")
        self._age=age


student1=Student("ram",33)
print(student1.name)
print(student1.age)

student1.name="Hari"
student1.age=30

print(student1.name)
print(student1.age)




#Example 2
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius # This calls the setter method

    @property
    def celsius(self):
        """The temperature in Celsius.""" # Docstring goes in the getter
        print("Getting value...")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        print("Setting value...")
        if value < -273.15: # Absolute zero validation
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value
    
    # Optional: Define a deleter
    @celsius.deleter
    def celsius(self):
        print("Deleting value...")
        del self._celsius

# Usage
temp_obj = Temperature(25) # Calls the setter
print(f"Current temp: {temp_obj.celsius}") # Calls the getter

temp_obj.celsius = 30 # Calls the setter
print(f"New temp: {temp_obj.celsius}")

# del temp_obj.celsius # Calls the deleter





#2. Static Method
"""
-> The @staticmethod decorator in Python defines a method that belongs to a class but does not 
   operate on an instance or the class itself. It is essentially a regular function that is
   logically grouped within the class's namespace. 
-> Static methods do not receive an implicit first argument like self(for instance methods) or cls(for class methods).
-> They cannot access or modify instance attributes or class attributes directly within the method's code unless explicitly passed as an argument.
-> They can be called both on the class itself(ClassName.method()) and on an instance of the class(instance.method()).
-> They are primarily used for utility of helper functions that have a logical relationship to the class but are self-contained and
   don't need any class-specific data.
"""


#Example 1
class Book:
    # Attribute or properties section
    # In this section we will define the state/properties of the object
    # title= ""
    # author=""
    # price=0.0
    # discount=0.0
    class_variable="I am a class variable"
    #Constructor
    def __init__(self, title, author_name, price, discount_rate):
        #Usage: Constructor is used for the initialization of object Properties
         self.title=title
         self.author=author_name
         self.price=price
         self.discount=discount_rate
         self.sp=None
         print("I am constructor of Book Class",self)
        

    # Behavior or methods section

    # def calculate_sp(self,price,discount):
    #    sp=price-(price*discount/100)
    #    return sp

    @staticmethod
    def add_two_numbers(num1,num2):
         return num1+num2

    def calculate_sp(self):
         self.sp=self.price-(self.price*self.discount/100)



#Calling static method

sum=Book.add_two_numbers(10,20)
print(f"Sum: {sum}")

   




#Example 2
class DateUtils:
    @staticmethod
    def is_leap_year(year):
        """Check if a year is a leap year."""
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        return False

# You can call it directly on the class
year = 2024
if DateUtils.is_leap_year(year):
    print(f"{year} is a leap year.")

# You could also technically call it on an instance, but it makes no difference
# utils = DateUtils()
# utils.is_leap_year(year) 








#3. Class Method
"""
-> The @classmethod decorator in Python defines a method that is bound to the class and not a
   specific instance of the class. It takes the class itself as its first argument, coventionally named "cls".
-> The method operates on the class's state, which is shared by all instances, rather than the unique state of a particular instance.
-> When the method is called, Python automatically passes the class object as the first argument(cls).
-> Class methods can access and modify class-level attributes using the "cls" parameter.
-> They cannot directly access or modify instance-specific attributes(those defined with self).
-> A class method can be invoked using either the ClassName.method() or instance.method() syntax, but in both cases, the "cls" parameter will refer to the class itself.
"""



#Example 1
class Book:
    # Attribute or properties section
    # In this section we will define the state/properties of the object
    # title= ""
    # author=""
    # price=0.0
    # discount=0.0
    class_variable="I am a class variable"
    # Constructor
    def __init__(self,title,author_name,price,discount_rate):
        #Usage: Constructor is used for the initialization of object Properties
         self.title= title
         self.author=author_name
         self.price=price
         self.discount=discount_rate
         self.sp=None
         print("I am constructor of Book Class",self)
        

    # Behavior or methods section

    # def calculate_sp(self,price,discount):
    #    sp=price-(price*discount/100)
    #    return sp
    @classmethod
    def create_object(cls, title, author_name, price, discount_rate):
         #This method is used to create object
         print("Inside class method: ",cls.class_variable)
         return cls(title,author_name,price,discount_rate)

    def calculate_sp(self):
         self.sp=self.price-(self.price*self.discount/100)



#calling class method
book1=Book.create_object("Python","Rossum",1000,10)
print(book1.title)




#Example 2
from datetime import date

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        # 'cls' refers to the Person class (or a subclass)
        age = date.today().year - birth_year
        return cls(name, age) # Creates a new instance of the class

    def display(self):
        print(f"{self.name}'s age is: {self.age}")

# Use the standard constructor
person1 = Person('Adam', 19)
person1.display()

# Use the alternative class method constructor
person2 = Person.from_birth_year('John', 1985)
person2.display()
