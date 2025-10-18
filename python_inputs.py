#Python User Input


"""
-> Python allows for user input using input() function. That means we are able to ask user for input.
-> Python stops executing when it comes to the input() function, and continues when the user has given some input.
-> Input function always returns the string object.
Syntax:

variable_name=input(prompt)

where:
prompt is the string written to standard output(usually screen) without newline which acts a message for user input. 

"""

name=input("Enter your name: ")
print(f"Hello {name}")
print(type(name))   #Always returns the string object


#Taking number as input

num=int(input("Enter any number: "))
print(num)
print(type(num))