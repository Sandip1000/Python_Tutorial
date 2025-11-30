#1. Python Math
"""
-> Python has a set of built-in math functions, including an extensive math module, that allows 
   us to perform mathematical tasks on numbers.
"""


#2. Built-In Math Functions


#A. min() and max() Functions
"""
-> The min() and max() functions can be used to find the lowest or highest value in an iterable.
"""

x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)



#B. abs() Function
"""
-> The abs() function returns the absolute(positive) value of the specified number.
"""

x = abs(-7.25)

print(x)


#C. pow() Function
"""
-> The pow(x,y) function returns the value of x to the power of y.
"""
x = pow(4, 3)

print(x)







#3. The Math Module
"""
-> Python has also a built-in module called "math", which extends the list of mathematical functions.
-> To use it, we must import the "math" module.
-> When we have imported the "math" module, we can start using methods and constants of the module.
"""


#A. math.sqrt()
"""
-> It returns the square root of a number.
"""

import math

x = math.sqrt(64)

print(x)


#B. math.ceil() And math.floor()
"""
-> The math.ceil() method rounds a number upwards to its nearest integer, and returns the result.
-> The math.floor() method rounds a number downwards to its nearest integer, and returns the result.
"""

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1


#C. math.pi
"""
-> The math.pi constant, returns the value of PI(3.14...).
"""
import math

x = math.pi

print(x)