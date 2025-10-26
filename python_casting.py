# Type Casting In Python

"""
-> We can specify the variable type using casting in Python.
-> Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.
-> Casting in python is therefore done using constructor functions which is also known as Explicit Typecasting:
    1. int()   : constructs an integer number from an integer literal, a float literal (by removing all decimals), 
                  or a string literal (providing the string represents a whole number).
    2. float() : constructs a float number from an integer literal, a float literal or 
                  a string literal (providing the string represents a float or an integer).
    3. str(): constructs a string from a wide variety of data types, including strings, integer literals and float literals.
-> If one data type is converted to another data type by the python interpreter itself automatically, then it called as 
   Implicit Typecasting.
"""

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print(w)
print(type(w))


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))

# Implict Type Casting

a=7    # Integer
b=5.5  # Float
c=a+b
print(c)
print(type(c))

