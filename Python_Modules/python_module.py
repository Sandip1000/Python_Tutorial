#1. Module
"""
-> A file containing a set of functions that we want to include in our application is known as module.
"""



#2. Creating A Module
"""
-> To create a module we just have to save the code we want in a file with the file extension '.py'.
"""

#3. Using A Module
"""
-> We can use the module we just created , by using "import" statement.
-> When using a function from a module, we should use following syntax:
      module_name.function_name()
"""

import mymodule
mymodule.greeting("John")


#4. Variable In A Module
"""
-> The module can contain functions, as already described, but also variables of all types(arrays, dictionaries, objects etc).
"""


import mymodule
a = mymodule.person1["age"]
print(a)



#5. Naming A Module
"""
-> We can name the module file whatever we like, but it must have the file extension '.py'.
"""





#6. Re-naming A Module
"""
-> We can create an alias when we import a module, by using the 'as' keyword.
"""


import mymodule as mm
a=mm.person1["name"]
print(a)






#7. Built-In Modules
"""
-> There are several built-in modules in Python, which we can import whenever we like.
"""

import platform
x=platform.system()
print(x)





#8. Using The dir() Function
"""
-> There is a bulit-in function that is dir() to list all the function names(or variable names) in a module.
-> The dir() function can be used on all modules, also the ones we create ourself.
"""
import platform

x = dir(platform)
print(x)


y=dir(mm)
print(y)




#9. Import From Module
"""
-> We can choose to import only parts from a module, by using the "from" keyword.
-> When importing using the from keyword, we do not use the module name when referring to elements in the module.
   Example: person1['age'], not mymodule.person1['age']
"""

from mymodule import person1

print (person1["age"])