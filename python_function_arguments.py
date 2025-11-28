#1. Function Arguments
"""
-> Information can be passed into functions as arguments.
-> Arguments are specified after the function name, inside the parentheses. We can add as many arguments as we want, just we have to 
   separate them with a comma.
-> When the function is called, we pass the arguments which is used by the function.
"""


#A function with one argument
def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")




#2. Parameters Vs Arguments
"""
-> The terms parameter and argument can be used for the same thing: information that are passed into a function.
-> From a function's perspective:
    A parameter is the variable listed inside the parentheses in the function defination.
    An argument is the actual value that is sent to the function when it is called.
"""
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument




#3. Number of Arguments

"""
-> By default, a function must be called with the correct number of arguments.
-> If our function expects 2 arguments, we must call it with exactly 2 arguments.
-> If we try to call the function with the wrong arguments, we will get an error.
"""
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")





#4. Default Paramater Values 
"""
-> We can assign default values to the parameters. If the function is called without an argument, it uses the 
   default value.
"""
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()          #Uses Default Value
my_function("Linus")


def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()         #Uses Default Value
my_function("Brazil")





#5. Keyword Arguments
"""
-> We can send arguments with the key = value syntax.
-> In keyword arguments, the order of the arguments does not matter. Without keyword arguments, the arguments must follow the order 
   in which parameters are defined in the function.
"""

def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")






#6. Positional Arguments
"""
-> When we call a function with arguments without using a keyword, then they are called positional arguments.
-> Positional arguments must be in the correct order.
-> The order matters with positional arguments.
-> Changing the order either sometimes change the result or generate an error.
"""
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


#Switching the order changes the result.
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")



#7. Mixing Positional And Keyword Arguments
"""
-> We can mix positional and keyword arguments in a function call.
-> However, positional arguments must come before keyword arguments.
"""
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)




#8. Arguments Data Types
"""
-> We can send any data type as an argument to a function(string, number, list, dictionary, etc).
-> The data type will be preserved inside the function.
"""

#Sending a list as an argument
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Sending a dictionary as an argument
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)




#9. ReTurn Values Of A Function
"""
-> Functions can return values using the return satatement.
-> Functions can return any data type, including lists, tuples, dictionaries and more.
"""
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


#Function returning a list
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


#Function returning a tuple
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)



#10. Positional-Only Arguments
"""
-> We can specify that a function can have only positional arguments.
-> To specify positional-only arguments, we should add ",/" after the arguments.
-> Without the ",/" we are actually allowed to use keyword arguments even if the function expects
   positional arguments.
-> With ",/", we will get an error if we try to use keyword arguments.
"""


def my_function(name, /): #postional-only arguments
  print("Hello", name)

my_function("Emil")

def my_function(name):   #Can use keyword arguments here
  print("Hello", name)

my_function(name = "Emil")


#This will produce error as the function expects positional-only arguments

# def my_function(name, /):
#   print("Hello", name)
# my_function(name = "Emil")



#11. Keyword-Only Arguments

"""
-> To specify that a function can have only keyword arguments, we should add "*,", before the arguments.
-> Without "*,", we are allowed to use positional arguments even if the function expects keyword arguments.
-> With "*,", we will get an error if we try to use positional arguments.
"""
def my_function(*, name):   #Keyword-only arguments
  print("Hello", name)

my_function(name = "Emil")



def my_function(name):    #Can use positional arguments here
  print("Hello", name)

my_function("Emil")


#This will produce an error as the function expects keyword-only arguemnts

# def my_function(*, name):
#   print("Hello", name)
# my_function("Emil")





#12. Combining Positional-Only And Keyword-Only Arguments
"""
-> We can combine both argument types in the same function.
-> Arguments before "/" are positional-only, and arguments after "*" are keyword-only.
"""

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c= 15, d = 20)
print(result)