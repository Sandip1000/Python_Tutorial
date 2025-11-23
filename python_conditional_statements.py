#1. If Statement
"""
-> An if statement is written by using "if" keyword.
-> The if statement evaluates a condtion(an expression that results in True or False). If the condition is True, the code 
   block inside the if statement is executed. If the condtion is False, the code block is skipped.
"""

a = 33
b = 200
if b > a:
  print("b is greater than a")


number = 15
if number > 0:     #Checking If A Number Is Positive
  print("The number is positive")


#2. Multiple Statements In If Block
"""
-> We can have multiple statements inside an if block.
-> All statements must be identated at the same level.
"""

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")


#3. Using Variables In Conditions
"""
-> Boolean variables can be used directly in if statements without comparison operators.
"""
is_logged_in = True
if is_logged_in:
  print("Welcome back!")