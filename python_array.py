#1. Python Arrays
"""
-> Python does not have built-in support for arrays, but Python Lists can be used instead.
-> We can also import Numpy(Numerical Python) to work with arrays.
-> Arrays are used to store multiple values in one single variable.
-> There are four collections(arrays) data types in the Python programming langauge:
   1. List      : It is a collection which is ordered and changeable. It also allows duplicate members.
   2. Tuple     : It is a collection which is ordered and unchangeable. It also allows duplicate members.
   3. Set       : It is a collection which is unordered, unchangeable and unindexed. It does not allow duplicate members. 
                  Set items are unchangeable, but can remove and/or add items whenever we like.
   4. Dictionary: It is a collection which is ordered and changeable. It does not allow duplicate members.
"""




#2. Mutable and Immutable Objects
"""
-> In Python, mutable objects can be changed after they are created, while immutable objects cannot. The mutuability 
   of an object is determined by its type and impacts how data is stored, refrenced, and passed to functions.

   1. Mutable Objects: Mutable objects allow in-place modification of their value or data without changing the object's
                       unique identity(memory address).

                       Characteristics:
                       1. Can be modified after creation(eg., adding, removing, or changing elements).
                       2. More memory-efficient for dynamic data that requires frequent changes, as new 
                          objects are not constantly created.
                       3. When multiple variables refrence the same mutable object, changes made through 
                          one variable are reflected in all other variables(known as aliasing).
                       4. Cannot be used as keys in a dictionary(because their hash value can change) or as 
                          elements in a set.
                        
                        Examples:
                        1. list
                        2. dict(dictionary)
                        3. set
                        4. bytearray
                        5. User-defined classes are generally mutable by default.

   2. Immutable Objects: Immutable objects cannot be altered after they are created. Any operation that appears 
                         to modify an immutable object actually results in the creation of new objects with the new
                         value, and the variable is then reassigned to this new object.


                        Characteristics:
                        1. Cannot be changed after creation (eg., we cannot change a single character in a string).
                        2. When a "modification" is made, a new object is generated in a memory, leading to a new unique 
                           identity.
                        3. They are inherently thread-safe because their state is fixed.
                        4. It can be used as keys in a dictionary or elements in a set because
                           their hash value is constant and reliable.

                        Examples:
                        1. int(integers)
                        2. float(floating-point numbers)
                        3. str(strings)
                        4. tuple
                        5. frozenset(an immutable version of a set)
                        6. bool(boolean values)
                        7. bytes
"""

#Mutable Objects
list1=[1,2,3,4,5]
list2=list1
list1.append(6)
print(list2)    #change made in list 1 automatically appears in list2
list3=[]
list3=list1.copy()
print(list3)
list1.append(7)
print(list1)
print(list3)

list1[3]="Hello"   #This is possible in mutable objects
print(list1)



#Immutable Objects

string1="Hello World"
print(string1)

#string1[5]="e"    #This is not possible in immutable objects
string2=string1
print(string2)
string1="I am changed"
print(string1)
print(string2)



#3. Iterable and Non-Iterable Objects
"""
-> In Python, an iterable is an object that we can loop over(eg. in a for loop), while a non-iterable
   object cannot be iterated through. The core difference lies in whether the object implements the iterator
   protocal (__iter__ or __getitem__ methods).

   1. Iterable Objects : An iterable is any object capable of returning its memebers one at a time. When a for loop
                         is used on an iterable, Python automatically calls the built-in iter() function on it to 
                         get an iterator.


                         Characteristics:
                         1. It can be looped over using a "for...in" loop.
                         2. It implements the __iter__() method(which returns an iterator object) or a __getitem__() method
                            with sequential indices starting from 0.
                         3. It can be iterated over multiple times because they do not maintain the iteration state themselves.


                         Examples:
                         1. list(lists)
                         2. tuple(tuples)
                         3. str(strings)
                         4. dict(dictionaries)
                         5. set(sets)
                         6. range objects
                         7. File objects

   2. Non-Iterable Objects : A non-iterable objects treats its content as a single unit and cannot be traversed element by element 
                             in a standard for loop. Attempting to iterate over a non-iterable will raise TypeError.


                        Characteristics:
                        1. It does not implement __iter__() or __getitem__() with sequential indicies.
                        2. It cannot be used in a for loop, as the iter() function call on it will fail.


                        Examples:
                        1. int(integers)
                        2. float(floating-point numbers)
                        3. bool(booleans)
                        4. None Type
"""

#Iterable Objects

list1=[1,2,3,4,5]
for i in list1:
    print(i)




#Non-Iterable Objects
int1=10
# for i in int1:      #This generates TypeError
#     print(i)