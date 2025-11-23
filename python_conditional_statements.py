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




#4. Elif Statement
"""
-> The "elif" keyword in Python's way of saying"if the previous conditions were not true, then
   try this condition."
-> The "elif" keyword allows us to check multiple expressions for True and execute a block of code as
   soon as one of the condtions evaluates to True.
-> We can have as many "elif" statements as we need. Python will check each condition in order and execute the first one that is
   true.
-> When we use "elif", Python evaluates the conditions from top to botttom. As soon as it finds a condition
   that is true, it executes that block and skips all remaining conditions. Only the first true condition will be executed.
   Even if multiple conditions are true, Python stops after executing the first matching block.
-> We can use "elif" when we have multiple mutually exclusive conditions to check. This is more efficient than using multiple separate
   "if" statements because Python stops checking once it finds a true condition.
"""
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


#Testing Multiple Conditions
score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")



age = 25

if age < 13:
  print("You are a child")
elif age < 20:
  print("You are a teenager")
elif age < 65:
  print("You are an adult")
elif age >= 65:
  print("You are a senior")




#Mutually Exclusive = Two or more events that cannot occur at same time.
day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")





#5. Else Statement
"""
-> The "else" keyword catches anything which isn't caught by the preceding conditions.
-> The "else" statement is executed when "if" condition (and any "elif" conditions) evaluate to False.
->  We can use "else" without "elif" , where the decision should be made based on two conditoins.
-> The "else" statements provides a default action when none of the previous condtions are true. Think of
   it as a "catch-all" for any scenario covered by if and else statements.
-> The "else" statement must come last. We cannot have an "elif" after an "else".
-> We can combine "if", "elif" and "else" to create a comprehensive decision making structure.
-> The "else" statements acts as a fallback that executes when none of the preceding conditions are true.
   This makes it useful for error handling, validation, and providing default values.
"""

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



#Else Without Elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



#Checking Even or Odd Number
number = 7

if number % 2 == 0:                 
  print("The number is even")
else:
  print("The number is odd")




#Complete If-Elif-Else Chain
temperature = 22

if temperature > 30:
  print("It's hot outside!")
elif temperature > 20:
  print("It's warm outside")
elif temperature > 10:
  print("It's cool outside")
else:
  print("It's cold outside!")



#Else As Fallback
username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")




#6. Short Hand If Statement
"""
-> If we have only one statement to execute, we can put it on the same line as the "if" statement.
-> But we still need the colon(:) after the condition. 
"""
a = 5
b = 2
if a > b: print("a is greater than b")



#7. Short Hand If ... Else (Ternary Operator)
"""
-> If we have one statement for "if" and one for "else", we can put them on same line using a conditional expression.
-> This is called a conditional expression or sometimes known as ternary operator.
-> We can also use a one-line if/else to choose a value and assign it to a variable.
   Syntax:
     variable = value_if_true if condtion else value_if_false
-> Ternary operators are particularly useful for simple assignments and return statements.
-> Shorthand if statements and ternary operators should be used when:
      1. The conditions and actions are simple.
      2. It improves code readability.
      3. If we want to make a quick assignment based on a condition.
-> While shorthand if statements can make code more concise, avoid overusing them for complex conditions.
"""
a = 2
b = 330
print("A") if a > b else print("B")


#Assign a Value With If ... Else

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)


#Multiple Conditions On One Line(Chaining Conditional Expressions)
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#Finding Maximum Of Two Numbers
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)



#Setting A Default Value
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)




#8. If Else Statement With Logical Operators
"""
-> Logical Operators(and, or, not) are used to combine condtional statements.
-> We combine multiple logical operators in a single expression. Python evaluates "not" first, then "and", then "or".
-> When combining multiple logical operators, we can use parentheses to make our intentions clear and control the order of evaluation.
"""

#and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")



#or Operator

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")


#not Operator
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")



#Combining Multiple Operators

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")


#Using Parentheses For Complex Conditions
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")


#User Authentication Check
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")



#Range Checking
score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")







#9. Nested If Statements
"""
-> If statements inside an if statements is known as nested if statements.
-> Each level of nesting creates a deeper level of decision-making. The code evaluates from the outermost condition to inward.
-> We can nest as many levels deep as needed, but should keep in mind that too many levels can make code harder to read.
"""

# In the example below, the inner if statement only runs if the outer condtion(x>10) is true.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")



#Checking Multiple Conditions With Nesting
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")



#Three Levels Of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")






#10. Pass Statement

"""
-> If statements cannot be empty, but if we for some reason have an if statement with no content, we can put in the 
   "pass" statement to avoid getting an error.
-> The "pass" statement is a null operation - nothing happens when it executes. It serves as an placeholder.
-> The "pass" statement is useful in several situations like:
    1. When we're creating a code structure but haven't implemented the logic yet.
    2. When a statement is required syntactically but no action is needed.
    3. As a placeholder for future code during development.
    4. In empty functions or classes that are planned to implemented later.
-> During development, we might want to sketch out our program structure before implementing the details. The "pass" statement allows us to do this 
   without syntax errors.
-> A comment is ignored by Python, but "pass" is an actual statement that gets executed(though it does nothing). We need "pass" where Python
   expects a statement, not just a comment.
-> We can use "pass" in any branch of an if-elif-else statement.
-> While we focus on "pass" with if statements here, it's also commonly used with loops, functions, and classes.
"""


#pass In Development
age = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")



#pass Vs Comments
"""
This will cause error:
score = 85

if score > 90:
  # This is excellent
# This will raise an IndentationError
"""

score = 85

if score > 90:
  pass # This is excellent
print("Score processed")



#pass With Multiple Conditions

value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")


#pass In Other Contexts
# Function exists but doesn't do anything yet
def calculate_discount(price):
  pass # TODO: Implement discount logic