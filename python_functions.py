#1. Python Functions

"""
-> A function is a block of code which only runs when it is called.
-> A function can return data as a result.
-> A function helps avoid code repetition.
-> In Python, a function is defined using the "def" keyword, followed by a function name and parentheses.
-> The code inside the function must be indented. Python uses identation to define code blocks.
-> To call a function, write its name followed by parentheses.
-> We can call the same function multiple times.
"""

#Creating A Function
def my_function():
  print("Hello from a function")   #This Creates A Function Named my_function() That Prints "Hello from a function" When It Is Called.



#Calling A Function
my_function()



#Calling A Function Multiple Times
my_function()
my_function()
my_function()



#2. Function Names
"""
-> Function names follow the same rules as variables names in Python.
-> A function name must start with a letter or underscore.
-> A function name can only contain letters, numbers, and underscores.
-> Function name are case-sensitive("myFunction" and "myfunction" are different).
-> It's good practice to use descriptive names that explain what the function does.
"""


#3. Use Of Function
"""
-> The main use of the function is code reusability. It helps to avoid rewriting of the code
   for the same kind of task. 
"""

#Without Using Functions
temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


#Using Functions
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))





#4. Function Return Values
"""
-> Functions can send data back to the code that called them using the "return" statement.
-> When a function raeches a "return" statement, it stops executing and sends the result back.
-> If a function doesn't have a return statement, it returns "None" by default.

"""
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)
 


#Use the return value directly
def get_greeting():
  return "Hello from a function"

print(get_greeting())





#5. The pass Statement

"""
-> Function definations cannot be empty. If we need to create a function placeholder without any code, use the 
   "pass" statement.
-> The "pass" statement is often used when developing, allowing us to define the structure first and implement details later.
"""
def my_function():
  pass