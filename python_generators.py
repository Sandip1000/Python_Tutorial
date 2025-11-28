#1. Python Generators
"""
-> Generators are functions that can pause and resume their execution.
-> When a generator function is called, it returns a generator object, which is an iterator.
-> The code inside the function is not executed yet, it is only compiled. The function only executes when we 
   iterate over the generator.
-> Generator allow us to iterate over the data without storing the entire dataset in memory.
-> Instead of using "return", generators use the "yield" keyword.
"""
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)





def generator():
  for i in range(10):
    yield i

gen=generator()
for i in gen:
  print(i)





#2. The yield Keyword
"""
-> The "yield" keyword is what makes a function a generator.
-> When "yield" is encountered, the function's state is saved, and the value is returned. The next time
   the generator is called, it continues from where it left off.
-> Unlike "return", which terminates the function, "yield" pauses it and can be called multiple times. 
"""


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)





#3. Generators Saves Memory
"""
-> Generators are memory-efficient because they generate values on-the-fly instead of 
   storing everything in memory.
-> For large datasets, generators save memory.
"""
def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))     #Generates the value when generator function is called




#4. Using next() With Generators
"""
-> We can manually iterate through a generator using the next() function.
-> When there are no more values to yield, the generator raises a "StopIteration" exception.
"""
def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))




def simple_gen():
  yield 1
  yield 2

gen = simple_gen()
print(next(gen))
print(next(gen))
#print(next(gen)) # This will raise StopIteration exception



#5. Generator Expressions
"""
-> Similar to list comprehensions, we can create generators using generator expressions with
   parentheses instead of square brackets.
"""

# List comprehension - creates a list
list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))



# Calculate sum of squares without creating a list
total = sum(x * x for x in range(10))
print(total)





#6. Fibonacci Sequence Generator
"""
-> Generators can be used to create the Fibonacci sequence.
-> It can continue generating values indefinitely, without running out of memory.
"""

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))




#7. Generator Methods
"""
-> Generators have special methods for advanced control.
-> The send() method allows us to send a value to the generator.
-> The close() method stops the generator.
"""

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")




def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()