#1. Python Iterators
"""
-> An iterator is an object that contains a countable number of values.
-> An iterator is an object that can be iterated upon, meaning that we can traverse through all the values.
-> Technically, in Python, an iterator is an object which implements the iterator protocal, which consists of the 
   methods __iter__() and __next()__().
"""



#2. Iterator vs Iterable
"""
-> Lists, tuples, dictionaries and sets are all iterable objects. They are iterable containers which can get an iterator from.
-> All these objects have a iter() method which is used to get an iterator.
"""

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)   #Returing an iterator from an object using iter() method

print(next(myit))
print(next(myit))
print(next(myit))



mystr = "banana"    #Strings are also iterable objects, containing a sequence of characters.
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))



#3. Looping Through An Iterator
"""
-> We can also use a for loop to iterate through an iterable object.
-> The for loop actually creates an iterator object and executes the next() method for each loop.
"""
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)






mystr = "banana"

for x in mystr:
  print(x)





#4. Creating An Iterator
"""
-> To create an object/class as an iterator we have to implement the methods __iter__() and __next__() to our object.
-> All classes have a function called __init__(), which allows us to do some initializing when the object is being created.
   The __iter__() method acts similar, we can do operations(initializing etc.), but must always return the iterator object itself.
-> The __next__() method also allows us to do operations, and must return the next item in a sequence.
"""

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))



#5. StopIteration Exception
"""
-> The example above would continue forever if we had enough next() statements, or if it was used in a for loop.
-> To prevent the iteration from going on forever, we can use StopIteration statement.
-> In the __next__() method , we can add terminating condition to raise an error if the iteration is done a specified number of times.
"""
class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)