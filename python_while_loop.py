#1. Python While Loop

"""
-> With the "while" loop we can execute a set of statements as long as a condition is true.
-> The while loop requires relevant variables to be ready, in the example below we need to define an
   indexing variable, i which we set to 1.
"""


i = 1
while i < 6:
  print(i)
  i += 1       #Remember To Increment i, or Else The Loop Will Continue Forever.




#2. The Break Statement
"""
-> With the "break" statement we can stop the loop even if the while condition is true.
"""

i = 1
while i < 6:
  print(i)
  if i == 3:       #Exit The Loop When i Equals To 3
    break
  i += 1





#3. The Continue Statement
"""
-> With the "continue" statement we can stop the current iteration and continue with the next iteration.
"""

i = 0
while i < 6:
  i += 1
  if i == 3:   #Skip The 3rd Iteration
    continue
  print(i)




#4. The else Statement

"""
-> With the "else" statement we can run a block of code once when the condition no longer is true.
"""

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
