#1. Object Oriented Programming
"""
-> OOP stands for Object-Oriented Programming.
-> Python is an object-oriented language, allowing us to structure our code using classes and objects for better organization and reusability.
-> The advantages of OOP are given below:
   1. Provides a clear structure to programs.
   2. Makes code easier to maintain, reuse and debug.
   3. Helps keep our code DRY(Don't Repeat Yourself). The DRY priciple means we should avoid writing same code more than once. Move repeated code into functions or classes and reuse it.
   4. Allows us to build reusable applications with less code.
"""



#2. Classes and Objects
"""
-> Classes and Objects are the two core concepts in object-oriented programming.
-> A class defines what an object should look like, and an object is created based on that class.
-> A class is like an object constructor, or a "blueprint" for creating objects.
-> An object is an instance of a class.
   For Example:

   Class                 Objects
   Fruit                 Apple, Banana, Mango
   Car                   Volvo, Audi, Toyota

-> When we create an object from a class, it inherits all the variables and functions defined inside that class.
"""




#3. Creating A Class
"""
-> To create a class, we should use the the keyword "class".
"""

class MyClass:
    x=5


#4. Creating An Object
"""
-> Now, we can use the class name to create objects.
"""
obj=MyClass()
print(obj.x)





#5. Deleting An Object
"""
-> We can delete objects by using the "del" keyword.
"""
del obj
#print(obj.x)    #This will generate an error





#6. Creating Multiple Objects
"""
-> We can create multiple objects from the same class.
-> Each object is independent and has its own copy of the class properties.
"""
obj1=MyClass()
obj2=MyClass()
obj3=MyClass()

print(obj1.x)
print(obj2.x)
print(obj3.x)




#7. The pass Statement
"""
-> Class defination cannot be empty, but if we for a some reason have a class defination with no content, we should
   put in "pass" statement to avoid getting an error.
"""
class Person:
  pass





#8. Example Of Classes and Objects

class Book:
    # Attribute or properties section
    # In this section we will define the state/properties of the object
    # title= ""
    # author=""
    # price=0.0
    # discount=0.0
    class_variable="I am a class variable"


    # Constructor
    def __init__(self, title, author_name, price, discount_rate):
        # Usage: Constructor is used for the initialization of object Properties
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
    

    def calculate_sp(self):
         self.sp=self.price-(self.price*self.discount/100)
         

# Instantiating the class or creating an object of the class
book1=Book(title="A Breif History of Time",author_name="Stphen Hawking",price=1000,discount_rate=15)
book2=Book("Theory of Everything","Stephen Hawking",1500,15)


# Acessing object Attributes
# We can acess object attributes and methods using dot(.) operator
print(book1.title)
print(book1.author)
print(book1.price)
print(book1.discount)
print(book1.class_variable)


print(book2.title)
print(book2.class_variable)

# sp_of_book1=book1.calculate_sp(book1.price,book1.discount)
# sp_of_book1=book1.calculate_sp()
# print(f"Selling Price of {book1.title}: {sp_of_book1}")

book1.calculate_sp()
print(f"Selling Price of {book1.title}: {book1.sp}")
book2.calculate_sp()
print(f"Selling price of {book2.title}: {book2.sp}")