#1. Python None
"""
-> "None" is a special constant in Python that represents the absence of a value.
-> Its data type is "NoneType", and "None" is the only instance of a "NoneType" object.
"""

#2. None Type
"""
-> Variables can de assigned "None" to indicate "no value" or "not set".
-> We can use type() to see the type of "None" value.
"""
x = None     #None is a constant value that represents the absence of value
print(x)
print(type(x))   #Type is NoneType




#3. Comparing To None
"""
-> To compare a value to "None", we can use identity operator "is" or "is not".
"""
result = None
if result is None:
  print("No result yet")
else:
  print("Result is ready")



result = None
if result is not None:
  print("Result is ready")
else:
  print("No result yet")




#4. True or False
"""
-> "None" evaluates to "False" in a boolean context.
"""
print(bool(None))



#5. Functions Returning None
"""
-> Functions that do not explicitly return a value, returns "None" by default.
"""
def myfunc():
  print("Hello")

x = myfunc()
print(x)
print(type(x))
