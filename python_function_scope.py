#1. Python Scope
"""
-> A variable is only available from inside the region it is created. This is called scope.
"""


#2. Local Scope 
"""
-> A variable created inside a function belongs to the local scope of that function, and can only
   be used inside that function.
"""

def myfunc():
  x = 300     #x is an local variable and can be used only inside myfunc().
  print(x)

myfunc()




#3. Function Inside Function
"""
-> As explained in the example above, the variable 'x' is not available outside the function, but it is 
   available for any function inside the function.
-> The local variable can be accessed from a function within the function.
"""
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)   # x can be accessed inside the function
  myinnerfunc()

myfunc()





#4. Global Scope
"""
-> A variable created in the main body of the Python code is a global variable and belongs to the global scope.
-> Global variables are available from within any scope, global and local.
-> A variable created outside of a function is global and can be used by anyone.
"""

x = 300

def myfunc():
  print("Inside Function x:",x)

myfunc()

print("Outside Function x:",x)




#5. Naming Variables
"""
-> If we operate with the same variable name inside and outside of a function, Python will treat them as two separate variables,
   one available in the global scope(outside the function) and one available in the local scope(inside the function).
"""
x = 300

def myfunc():
  x = 200
  print("Local x:",x)

myfunc()

print("Global x:",x)





#6.Global Keyword
"""
-> If we need to create a global variable, but are stuck in the local scope, we can use "global" keyword.
-> The "global" keyword makes the variable global.
-> Also, we can use "global" keyword if we want to make a change to a global variable inside a function.
"""


def myfunc():
  global x
  x = 300

myfunc()

print(x)       #Can be Accesed Outside The Function


x = 300

def myfunc():
  global x
  x = 200      #Changing The Vlaue Of Global Variable x

myfunc()

print(x)



#7. Nonlocal Keyword
"""
-> The "nonlocal" keyword is used to work with variables inside the nested functions.
-> The "nonlocal" keyword makes the variable belong to outer function.
"""

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())




#8. The LEGB Rule
"""
-> Python follows the LEGB rule when looking up variable names, and searches for them in this order:
    1. Local - Inside the current function
    2. Enclosing - Inside enclosing functions(from inner to outer)
    3. Global - At the top level of the module
    4. Built-In - In Python's built-in namespace
"""
x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)