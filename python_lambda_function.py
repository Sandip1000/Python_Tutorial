#1. Python Lambda Functions
"""
-> A lambda function is a small anonymous function.
-> A lambda function can take any number of arguments, but can only have one expression.
-> Syntax:
   lambda argumments: expression
    
-> The expression is evaluated and the result is returned.
-> We generally use lambda function with the higher order functions like map(), reduce() and filter().
"""

x = lambda a : a+10
print(x(5))


x = lambda a, b : a * b   #Can take any number of arguments
print(x(5, 6))


x = lambda a, b, c : a + b + c
print(x(5, 6, 2))







#2. Why To Use Lambda Functions?
"""
-> The power of lambda is better shown when we use them as an anonymous function inside another function.
-> So we have a function defination that takes one argument, and that argument will be multiplied with an unknown number.
-> We can use that function defination to make a function that always doubles the number we send in.
-> Or, we can use that function defination to make a function that always triples the number we send in.
-> Or, we can use the same function to make both functions, in the same program.
-> Basically, we can use lambda functions when an anonymous function is required for a short peroid of time.
"""
def myfunc(n):
  return lambda a : a * n

mydoubler=myfunc(2)
print(mydoubler(11))


def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))







def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mytripler(11))










#3. Lambda Functions With Built-In Functions
"""
-> Lambda functions are commonly used with built-in functions like map(), filter(), and sorted().
"""




#4. Using Lambda With map()
"""
-> The map() function applies to a function to every item in an iterable.
"""

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))   #Doubles all numbers in a list
print(doubled)



#5. Using Lambda  With filter()
"""
-> The filter() function creates a list of items for which a function returns True.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))  #Filter out odd numbers in a list
print(odd_numbers)




#6. Using Lambda With sorted()
"""
-> The sorted() function can use a lambda as a key for custom sorting.
"""
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)



words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))   #Sort strings by length
print(sorted_words)

