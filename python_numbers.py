# 1.Python Numbers
"""
-> There are three numeric types in Python:
    1. int
    2. float
    3. complex
"""
x=1
print(x)
print(type(x))

y=2.8
print(y)
print(type(y))

z=1j+2
print(z)
print(type(z))


# 2.Integer
"""
-> Int, or integer is a whole number, positive or negative, without
decimals, of unlimited length.
"""

x=1
y=-786543435
z=11648849474639

print(type(x))
print(type(y))
print(type(z))

#3. Float
"""
-> Float, or "Floating point number" is a number, positive or negative,
containing one or more decimals.
"""

x=1.10
y=2.0
z=-3.3

print(type(x))
print(type(y))
print(type(z))

"""
-> Float can also be scientific numbers with an 'e' to indicate 
the power of 10.
"""

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))

#4. Complex
"""
-> Complex numbers are written with a 'j' as the imaginary part.
"""

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

#5. Type conversion 
"""
-> We can convert one type of python numbers to another using int(), float() and complex()
methods. But, we cannot convert complex numbers into another number type.
"""

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

#6. Random Number 
"""
-> Python does not have a random() function to make a random number, but Python has a 
built-in module called random that can be used to make random numbers.
"""

import random
print(random.randrange(1,10)) #Returns output number in between 1 to 10.