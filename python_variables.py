#1. Python Variables

"""
-> Variables are the containers for storing data values.
-> Python has no command for declaring a variable. A variable is created when we assign value to it.
-> Variables do not need to be declared with any particular type, and can even change type after they have been set.
-> If we want to specify the data type of the variable, this can be done using casting.
"""

x=5 #Here x is an integer variable.
y="Nepal" # Here y is a string variable.
print(x,y)

x=int(10) # Specifying the variable type using casting
y=str("Hello, World!")
print(x,y)

#2. Variable Names

"""
-> A variable can have a short name(like x and y) or more desciptive name(age,car_name,total_volume)
-> Rules for Python Variables:
    1. A variable name must start with a letter or the underscore character.
    2. A variable name cannot start with a number.
    3. A variable name can only contain alphanumeric characters and underscores(A-Z, a-z, 0-9 and _).
    4. Vaiable names are case-sensitive(age, Age, AGE are three different types of variables).
    5. A variable name cannot be any Python Keywords.
"""

#3. Multi Words Variables Names

"""
-> Variable names with more than one word ca be difficult to read.
-> There are several techniques that can be used to make them more readable.

    1. Camel Case  : Each word, except the first ,starts with a capital letter.
    2. Pascal Case : Each word starts with a capital letter.
    3. Snake Case  : Each word is separated by an underscore character.
"""

myVariableName="camelCaseVariable"
print(myVariableName)
MyVariableName="PascalCaseVariable"
print(MyVariableName)
my_variable_name="snake_case_variable"
print(my_variable_name)

#4. Assign Multiple Values

"""
-> Python allows us to assign multiple values to a multiple variables in one line. We have to make sure that the number of variables
matches the number of values, or else we will get an error.
-> Python also allows us to assign the same value to multiple variables in one line.
"""
x, y, z="variable1", "variable2", "variable3"
print(x)
print(y)
print(z)


x=y=z="variable"
print(x)
print(y)
print(z)

#5. Output Variables

""" 
-> The print() function is often used to output variables.
-> In print() function we can output multiple variables, seperated by commas. We can also use + operator to output multiple variables
of same data type.
-> The best way to output multiple variables in print() function is to seperate them with commas, which even supports different data 
types.
""" 

x="Python is awesome"
print(x)

x="Python "
y="is "
z="awesome "
print(x,y,z)
print(x+y+z)

x=5
y=10
print(x+y)

x="Ram is"
y=10
z="years old."
print(x,y,z)

#6. Global Variables

"""
-> Variables that are created outside of the function are known as global variables.
-> Global variables can be used by everyone, both inside and outside the function.
"""

x="awesome" #Global Variable

def my_func():
    print("Python is "+x)

my_func()




"""
-> If we create a variable with the same name inside a function, this variable will be local, and can only be used 
inside the function. The global variable with the same name will remain as it was, global and with the original value.
"""

x="awesome"#Global Variable

def myFunc():
    x="fantastic" #Local Variable
    print("Python is "+ x)

myFunc()
print("Python is "+ x)



"""
-> To create a global variable inside a function we can use global keyword.
-> If we use global keyword, the variable belongs to a global scope.
-> Also, we can use global keyword, if we want to change the global variable inside
a function.
"""

def myfunc():
    global x 
    x="fantastic"
    print("Python is "+ x)

myfunc()
print("Python is "+ x)


x="awesome"

def MyFunc():
    global x
    x="fantastic"
    print("Python is "+x)
MyFunc()

