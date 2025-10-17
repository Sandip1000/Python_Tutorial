#1. Checking The Version of the Python installed in this System
import sys

print(sys.version)

#2. Python Quickstart

print('Hello, World!')

#3. Python Identation

"""
-> Identation refers to the spaces at the beginning of the code line.
-> Python uses indentation to indicate a block of code.
-> Where in other programming languages the indentation in the code is for readability only, the identation in python is very important.
"""
#With Identation
if 5>2:
    print("Five is greater than two.")

#Without Identation(Error)

"""
if 5>2:
print("Five is greater than two.")
"""


#4.Python Comments

"""
-> Comments can be used to explain Python code.
-> Comments can be used to make the code more readable.
-> Comments can be used to prevent execution when testing code.
"""

#Single Line Comment
"""
-> Single Line Comments starts with '#'.
"""
#This is single line comment


#Multi Line Comment
""" 
-> Python does not really have a syntax for multiline comments.
-> To add a multiline comment we can insert a '#' for each line.
"""

#This is a 
#multiline
#comment

"""
-> We can also use multiline string as a multiline comments. Since Python ignores string literals that are
not assigned to a variable, we can add a multiline string(triple quotes) in our code and place
our comment inside it.
"""

"""
This is a comment
written in more than just on line.
"""

#5. Python Statements

"""
-> A computer program is a list of instructions to be executed by a computer.
-> In programming languages, these programming instructions are called statements
-> In Python , a statement usually ends when the line ends. You do not need to use a semicolon (;)
like in many other programming languages(for example , Java or C)
-> Most Python programs contains many statements. The statements are executed one by one, in the same order in which they are
written.
-> Semicolons are optional in Python. However, we can write multiple statements on one line by separating them with semicolon (;), but
this is rarely used because it makes the code hard to read and understand.
-> However , if we put two statements on the same line  without a semicolon, Pyhtom will give an error.
"""

print("This is the first python statement.")
print("This is the second python statement.")