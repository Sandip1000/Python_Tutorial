#1. Python Decorators
"""
-> A decorator is also known as the higher order function.
-> Decorators let us to add extra behaviour to a function, without changing the function's code.
-> A decorator is a function that takes another function as input and returns a new function.
-> Basically, decorator accepts the function as input and return the modified version of that function.
-> A decorator is implemeted as a function that takes another function as an argument, defines an inner wrapper 
   function to contain enhanced logic, and returns that inner function.
"""



#2. Basic Decorator
"""
-> We have to define the decorator first, then apply it with "@decorator_name" above the function.
-> By placing '@changecase' directly above the function defination, the function 'myfunction' is being decorated with the 'changecase' function.
-> The function 'changecase' is the decorator.
-> The function 'myfunction' is the function that gets decorated.
"""

#A basic decorator that uppercases the return value of the decorated function
def changecase(func):
  def myinner():    #Here myinner() is a wrapper function
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

# It can also be written as:
# myfunction=changecase(myfunction)
#chagecase(myfunction)()

print(myfunction())





def greet(func):
  def modifiedhellofunction():
    print("Good Morning")
    func()
    print("Thanks for using this function.")
  return modifiedhellofunction

def hello():
  print("Hello World")

hello=greet(hello)    #This is same as writing @greet above the function

hello()




#3. Multiple Decorator Calls
"""
-> A decorator can be called multiple times. We have to place the decorator above the function we want to decorate.
"""


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())




#4. Arguments In The Decorated Function
"""
-> Functions that requires arguments can also be decorated, just we have to make sure to pass the arguments to the wrapper function.
"""
def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))



#5. *args And **kwargs In Decorator Function
"""
-> Sometimes, the decorator function has no control over the arguments passed from the decorated function. To solve this problem, we add (*args, **kwargs)
   to the wrapper function. In this way, the wrapper function can accept any number, and any type of arguments, and pass them to the decorated function.
"""

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))




#6. Decorator With Arguments
"""
-> Decorators can accept their own arguments by adding another wrapper level.
"""

def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

# @changecase(1)
def myfunction():
  return "Hello Linus"

myfunction=changecase(1)(myfunction)
print(myfunction())



#7. Multiple Decorators
"""
-> We can use multiple decorators on one function.
-> This is done by placing calls on the top of each other.
-> Decorators are called in the reverse order, starting with the one closest to the function.
"""

def changecase(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + " Have a good day!"
  return myinner

@changecase
@addgreeting    #First this decorator will run
def myfunction():
  return "Tobias"

print(myfunction())





#8. Preserving Function Metadata
"""
-> Functions in Python has metadata that can be accessed using the "__name__" and "__doc__" attributes.
-> Normally, a function's name can be returned with the "__name__" attribute.
-> But, when a function is decorated, the metadata of the original function is lost.
-> To fix this, Python has a buit-in function called "functools.wraps" that can be used to preserve the original function's name and docstring.
"""

def myfunction():
  """This is my function."""
  return "Have a great day!"

print(myfunction.__name__)
print(myfunction.__doc__)




def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)     #The name of the original function is lost







import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)    #Preserves the original name of the function