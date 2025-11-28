#1. Python *args and *kwargs
"""
-> By default, a function must be called with the correct number of arguments.
-> However, sometimes we may not know how many arguments that will be passed in our function.
-> *args and *kwargs allow functions to accept a unknown number of arguments.
"""



#2. Arbitary Arguments - *args
"""
-> If we don't know how many arguments will be passed into our function, we should add a '*' before the parameter name.
-> In this way, function will receive a tuple of arguments and can access the items accordingly.
-> The "*args" parameter allows a function to accept any number of positional arguments.
-> Inside the function, args becomes a tuple containing all the passed arguments.
"""


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")




def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")



#3. Using *args with Regular Arguments
"""
-> We can combine regular parameters with *args.
-> Regular parameters must come before *args.
"""


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")



#4. Practical Example Of *args
"""
-> *args is useful when we want to create a flexible function.
"""
def my_function(*numbers):    #A function that calculates the sum of any number of values.
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))




def my_function(*numbers):   #Finding the maximum number
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))




#5. Arbitary Keyword Arguments - **kwargs
"""
-> If we don't know how many keyword arguments will be passed into our function, we should add two astericks "**" 
   before the parameter name.
-> In this way, the function will receive a dictionary of arguments and can access the items accordingly.
-> The "**kwargs" parameter allows a function to accept any number of keyword arguments.
-> Inside the function, kwargs becomes a dictionary containing all the keyword arguments.
"""
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")



#6. Using **kwargs With Regular Arguments
"""
-> We can combine regular parameters with **kwargs.
-> Regular parameters must come before **kwargs.
"""

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")



#7. Combining *args And **kwargs 
"""
-> We can use both *args and **kwargs in the same function.
-> The order must be:
   1. Regualr Parameters
   2. *args
   3. **kwargs
"""
def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")






#8. Unpacking Arguments
"""
-> The '*' and '**' operators can also be used when calling functions to unpack(expand) a list or dictionary into sequence arguments.
"""



#9. Unpacking Lists With *
"""
-> If we have values stored in a list, we can use '*' unpack them into individual arguments.
"""

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)



#10. Unpacking Dictionaries With **
"""
-> If we have keyword arguments stored in a dictionary, we can use '**' to unpack them.
"""
def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")




#Note:
#Use '*' and '**' in function definations to collect arguments, and use them in function calls to unpack arguments.