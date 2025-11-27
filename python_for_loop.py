#1. For Loop
"""
-> A "for" loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
-> This is less like "for" keyword in other programming languages, and works more like an iterator method as found in other
   object-oriented programming langauges.
-> With the "for" loop we can execute a set of statements, once for each item in a list, tuple, set etc.
-> The "for" loop does not require an indexing variable to set beforehand.
"""


#Printing Each Item Of List
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)


#Looping Through A String

for x in "banana":
  print(x)




#2. The Break Statement
"""
-> With the "break" statement we can stop the loop before it has looped through all the items.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)      #Break Before Printing





#3. The Continue Statement
"""
-> With the "continue" statement we can stop the current iteration of the loop, and continue with the next.
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)      #Do Not Print "banana"





#4. The range() Function
"""
-> To loop through a set of code a specified number of times, we can use the range() function.
-> The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1(by default), and ends at a specified number.
-> The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding parameter like range(2,6), which
   means from 2 to 6(but not including 6).
-> The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter like range(2,30,3).
   Syntax:
      range(start, end, stepsize)
"""
for x in range(6):      #Note That range(6) Returns The Value From 0 To 5, NoT 0 To 6
  print(x)


for x in range(2, 6):
  print(x)


for x in range(2, 30, 3):
  print(x)





#5. Else In For Loop
"""
-> The "else" keyword in a for loop specifies a block of code to be executed when the loop is finished.
-> The "else" block will not be executed if the loop is stopped by a break statement.
"""

for x in range(6):
  print(x)
else:
  print("Finally finished!")



for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")






#6. Nested For Loops

"""
-> A nested loop is a loop inside a loop.
-> The inner loop will be executed one time for each iteration of the outer loop.
"""
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



#7. The pass Statement
"""
-> For loops can be empty, but if we for some reason have a for loop with no content, put in the "pass"
   statement to avoid getting an error.
"""