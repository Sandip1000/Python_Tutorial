#1. Python Range
"""
-> The built-in range() function returns an immutable sequence of numbers, commonly used for looping
   a specific number of times. Immutable means that it cannot be modified after it is created.
-> The set of numbers has its own data type called range.
-> The range() function can be called with 1,2, or 3 arguments, using the syntax below:

    range(start, stop, stepsize)
"""



#2. Call range() With One Argument
"""
-> If the range function is called with only one argument, the argument represents the stop value.
-> The start argument is optional, and if not provided, it defaults to 0.
-> For example, range(10) returns a sequence of each number from 0 to 9.(The start argumemt, 0 is inclusive,
   and the stop argument, 10 is exclusive).
"""

x=range(10)
print(x)

for i in x:
    print(i)




#3. Call range() With Two Arguments
"""
-> If the range function is called with two arguments, the first argument represents the start value, and the
   second argument represents the stop value.
-> For example, range(3,10) returns a sequence of each number from 3 to 9.
"""

x=range(3,10)

for i in x:
    print(i)






#4. Call range() With Three Arguments
"""
-> If the range function is called with three arguments, the third argument represents the step value.
-> The step value means the difference between each number in the sequence. It is optional, and if not provided,
   it defaults to 1.
-> For example, range(3,10,2) returns a sequence of each number from 3 to 9, with a step of 2.
"""

x=range(3,10,2)

for i in x:
    print(i)






#5. Using Ranges
"""
-> Ranges are often used in for loops to iterate over a sequence of numbers.
"""


for i in range(10):
  print(i)




#6. Using List To Display Ranges
"""
-> The range object is a data type that represents an immutable sequence of numbers, and it is not directly displayable.
-> Therefore, ranges are often converted to lists for display.
"""
print(list(range(5)))
print(list(range(1, 6)))
print(list(range(5, 20, 3)))



#7. Slicing Ranges
"""
-> Like other sequences, ranges can be sliced to extract a subsequence.
"""
r=range(10)
print(r[2])   #Returns the value at index 2
print(r[:3])  #Returns a new range object, from index 0 to 3.





#8. Membership Testing
"""
-> Ranges support membership testing with the in operator.
-> The return value is True when the number is present in the range, and False when it is not.
"""

r = range(0, 10, 2)
print(6 in r)
print(7 in r)




#9. Length
"""
-> Ranges support the len() function to get the number of elements in the range.
"""
r=range(0,10,2)
print(len(r))