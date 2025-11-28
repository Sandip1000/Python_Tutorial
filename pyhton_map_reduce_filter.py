#1. Python map(), reduce() and filter() Function
"""
-> Python's map(), filter(), and reduce() functions are tools from functional programming 
   that allow for powerful data manipulation using concise code.
-> They are also called as the higher order functions.
"""


#2. map() Function
"""
-> The map() function applies a specified function to every item in an iterable (like a list) and returns an iterator of the results. 
-> The main purpose of this function is to transform the every elements of the sequence.
-> Syntax:
    map(function,iterable)
"""

# Function to square a number
def square(n):
    return n * n

numbers = [1, 2, 3, 4, 5]

# Using map() and converting the result to a list
squared_numbers = list(map(square, numbers))

print(squared_numbers)
# Output: [1, 4, 9, 16, 25]



#We can also use lambda function for same purpose.
numbers = [1, 2, 3, 4, 5]
squared_numbers=list(map(lambda x:x*x, numbers))
print(squared_numbers)




#3. filter() Function
"""
-> The filter() function constructs an iterator from elements of an iterable for which
   the provided function returns True.
-> The main purpose of filter() function is to select a subset of elements based on a condition.
-> Syntax:
   filter(function, iterable)
"""

# Function to check if a number is even (must return True or False)
def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]

# Using filter() and converting the result to a list
even_numbers = list(filter(is_even, numbers))

print(even_numbers)
# Output: [2, 4, 6]




#Using Lambda Function 
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


#4. reduce() Function
"""
-> The reduce() function applies a rolling computation to sequential pairs of values in an iterable, ultimately returning a single value.
-> Unlike map() and filter(), reduce() is not a built-in function and must be imported from the 'functools' module.
-> The main purpose of reduce() functio is to accumulate elements into a single result (e.g., sum, product, max value).
-> Syntax:
    reduce(function, iterable,[initializer])
"""

from functools import reduce

# Function to add two numbers
def add(x, y):
    return x + y

numbers = [1, 2, 3, 4, 5]

# Using reduce() to sum all elements
sum_of_numbers = reduce(add, numbers)

print(sum_of_numbers)
# Output: 15



#Using Lambda Function
sum_of_numbers=reduce(lambda x, y: x+y ,numbers)
print(sum_of_numbers)