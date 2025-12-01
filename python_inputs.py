#1. Python User Input
"""
-> Python allows for user input using input() function. That means we are able to ask user for input.
-> Python stops executing when it comes to the input() function, and continues when the user has given some input.
-> Input function always returns the string object.
Syntax:

variable_name=input(prompt)

where:
prompt is the string written to standard output(usually screen) without newline which acts a message for user input. 

"""

name=input("Enter your name: ")
print(f"Hello {name}")
print(type(name))   #input() always returns the string object



#2. Taking Multiple Inputs
"""
-> We can add as many inputs as we want, Python will stop executing at each of them, waiting for user input.
"""

name = input("Enter your name:")
print(f"Hello {name}")
fav1 = input("What is your favorite animal:")
fav2 = input("What is your favorite color:")
fav3 = input("What is your favorite number:")
print(f"Do you want a {fav2} {fav1} with {fav3} legs?")






#3. Taking Number as Input
"""
-> The input from the user is treated as string. So, we have to convert the string to a number using int() or float() constructor.
"""

num=int(input("Enter any number: "))
print(num)
print(type(num))


import math
x = input("Enter a number:")

#find the square root of the number:
y = math.sqrt(float(x))

print(f"The square root of {x} is {y}")




#4. Validate Input
"""
-> It is good practice to validate any input from the user. It is useful to avoid the errors.
"""
y = True
while y == True:
  x = input("Enter a number:")
  try:
    x = float(x)
    y = False
  except:
    print("Wrong input, please try again.")

print("Thank you!")