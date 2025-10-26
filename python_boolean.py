#1. Python Booleans

"""
-> Booleans represents one of two values: True or False.
-> When we evaluate an expression in Python, we often get either True or False.
"""

print(10 > 9)
print(10 == 9)
print(10 < 9)

"""
-> When we run a condition in an if statement, it returns either True or False.
"""

a=10
b=20

if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")



#2. Evaluate Values and Variables
"""
-> The bool() function allows us to evaluate any value, and returns either True or False.
"""
print(bool("Hello"))
print(bool(15))


#3. Most Values are True

"""
-> Almost any value is evaluated as True if it has some sort of content.
-> Any string is True, except empty strings.
-> Any number is True, except 0.
-> Any list, tuple, set and dictionary are True, except empty ones.
"""

print(bool("abc"))
print(bool(1))
print(bool(["apple","banana","orange"]))

#4. Some Values are False

"""
-> There are not many values that evaluate to False,except empty values,
such as (), [], {}, "", the number 0, and the value None. 
-> And, also the value False evaluates to False.
"""

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


"""
-> One more value, or object in this case, evaluates to False, and that 
is if we have an object that is made from a class with a __len__ functions 
that returns 0 or False.
"""
class myclass():
    def __len__(self):
        return 0

myobj=myclass()
print(bool(myobj))

#5. Function can Return a Boolean
"""
-> We can create functions that returns a Boolean Value.
"""
def MyFunction():
    return True

print(MyFunction())

"""
-> We can also execute code based on the Boolean answer 
of a function.
"""

def myFunction():
    return True

if myFunction():
    print("YES! ")
else: 
    print("NO! ")

"""
-> Python also has many built-in functions that return a Boolean value, like the
isinstance() function, which can be used to determine if an object is of a certian 
data type.
"""

x=200
print(isinstance(x,int))
print(isinstance(x,str))