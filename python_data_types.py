#Python Built-In Data Types

"""
Text Type      : str
Numeric Types  : int, float, complex
Sequence Types : list, tuple, range
MappinG Type   : dict
Set Types      : set, frozenset
Boolean Type   : bool
Binary Types   : bytes, bytearray, memoryview
None Type      : NoneType

"""

#Getting The Data Type

""" 
-> We can get the data type of any object by using the type() function.
"""

x=20
print(type(x))


#Setting The Data Type

"""
-> In Python, the data type is set when you assign a vlaue to a variable
"""

#String
x="Hello, World!"
print(type(x))



#Integer
x=20
print(type(x))



#Float
x=20.5
print(type(x))



#Complex
x=1j
print(type(x))



#List
x=["apple", "banana", "cherry"]
print(type(x))



#Tuple
x=("apple", "banana", "cherry")
print(type(x))



#Range
x=range(6)
print(type(x))



#Dictionary
x={
    "name":"John",
    "age":36
   }
print(type(x))



#Set
x={"apple", "banana", "cherry"}
print(type(x))




#Frozenset
x=frozenset({"apple", "banana", "cherry"})
print(type(x))




#Boolean
x=True
print(type(x))


#Bytes
x=b"Hello" 
print(x)
print(type(x))



#Bytearray
x=bytearray(5)
print(x)
print(type(x))



#Memoryview
x=memoryview(bytes(5))
print(x)
print(type(x))


#NoneType
x=None
print(type(x))


#Setting The Specific Data Type

"""
-> If we want to specify the data type, we can use the following constuctor functions.
"""
#String
x=str("Hello World!")
print(x)
print(type(x))


#Integer
x=int(20)
print(x)
print(type(x))


#Float
x=float(20.5)
print(x)
print(type(x))


#Complex
x=complex(1j)
print(x)
print(type(x))



#List
x=list(("apple","banana","cheery"))
print(x)
print(type(x))



#Tuple
x=tuple(("apple","banana","cheery"))
print(x)
print(type(x))



#Range
x=range(6)
print(x)
print(type(x))



#Dictionary
x=dict(name="John",age=36)
print(x)
print(type(x))



#Set
x=set(("apple","banana","cheery"))
print(x)
print(type(x))



#Frozenset
x=frozenset(("apple","banana","cheery"))
print(x)
print(type(x))



#Boolean
x=bool(True)
print(x)
print(type(x))



#Bytes
x=bytes(5)
print(x)
print(type(x))



#Bytearray
x=bytearray(5)
print(x)
print(type(x))



#Memoryview
x=memoryview(bytes(5))
print(x)
print(type(x))
