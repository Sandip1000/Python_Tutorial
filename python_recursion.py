#1. Recursion In Python
"""
-> Recursion is when a function calls itself.
-> Recursion is a common mathematical and programming concept. It means that a function calls itself.
   This has the benefit of meaning that we can loop through data to reach a result.
-> The developer should be very careful with recursion as it can be quite easy to slip into writing a
   function which never terminates, or one that uses excess amounts of memory or processor power. However, when
   written correctly recursion can be a very efficient and mathematically elegant approach to programming.
"""

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1)

countdown(5)




#2. Base Case And Recursive Case
"""
-> Every recursive function must have a two parts.
   1. A base case      : A condition that stops the recursion.
   2. A recursive case : The function calling itself with a modified argument.

-> Without a base case, the function would call itself forever, causing a stack overflow error.
-> The base case is crucial. Always make sure that recursive function has a condition that will eventually be met.
"""

#Finding a factorial of a number
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))



#3. Fibonacci Sequence
"""
-> The Fibonacci sequence is a classic example where each number is the sum of the two preceding ones.
   The sequence starts with 0 and 1.
    0,1,1,2,3,5,8,13,....
-> The sequence continues indefinately, with each number being sum of the two preceding ones.
-> We can use recursion to find a specific number in a sequence.
"""


def fibonacci(n):
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n-1)+fibonacci(n-2)
  

print(fibonacci(7)) #Prints the 7th number of the sequence






#4. Recursion With Lists
"""
-> Recursion can be used to process lists by handling one element at a time.
"""


#Calculating the sum of all elements in a list
def sum_list(numbers):
  if len(numbers) == 0:
    return 0
  else:
    return numbers[0] + sum_list(numbers[1:])

my_list = [1, 2, 3, 4, 5]  
print(sum_list(my_list))



#Finding the maximum value in a list
def find_max(numbers):
  if len(numbers) == 1:
    return numbers[0]
  else:
    max_of_rest = find_max(numbers[1:])
    return numbers[0] if numbers[0] > max_of_rest else max_of_rest

my_list = [3, 7, 2, 9, 1]
print(find_max(my_list))





#5. Recursion DeptH Limit
"""
-> Python has a limit on how deep recursion can go. The default limit is usually around 1000 recursive calls.
-> If we need deeper recursion, we can increase the limit, but we should be careful as this can cause crashes.
-> Increasing the recursion limit should be done with caution. For very deep recursion, we should use iteration instead.
"""

import sys
print(sys.getrecursionlimit())


import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())