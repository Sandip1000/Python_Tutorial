#1. Python Tuple
"""
-> Tuples are used to store multiple items in a single variable.
-> A tuple is a collection which is ordered and unchangeable.
-> Tuples are written with round brackets.
-> Tuples items are ordered, unchangeable, and allow duplicate values.
-> Tuples items are indexed, the first item has index [0], the second item has index [1] etc.
-> When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
-> Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
-> Since tuples are indexed, they can have items with the same value.
"""
this_tuple=()
print(this_tuple)   #Empty Tuple
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#2. Tuple Length
"""
-> To determine how many items a tuple has, we can use len() function.
"""
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#3. Creating Tuple With One Item
"""
-> To create a tuple with only one item, we have to add a comma after the item, otherwise Python will not recognize it as a tuple.
"""

thistuple = ("apple",)
print(type(thistuple))

thistuple = ("apple")  #Not A Tuple
print(type(thistuple))


#4.Tuple Items- Data Types
"""
-> Tuple items can be of any data type.
-> A tuple can contain different data types.
"""

tuple1 = ("apple", "banana", "cherry")    #String
tuple2 = (1, 5, 7, 9, 3)                  #Integer
tuple3 = (True, False, False)             #Boolean
tuple4= ("abc", 34, True, 40, "male")    #A Tuple With Strings, Integers And Boolean Values


#5. Tuple Type
"""
-> From Python's perspective, tuples are defined as objects with the data type 'tuple'.
"""
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#6. The tuple() Constructor
"""
-> It is also possible to use the tuple() constructor to make a tuple.
"""
thistuple = tuple(("apple", "banana", "cherry")) # Note The Double Round-Brackets
print(thistuple)


#7. Accessing Tuple Items
"""
-> We can access multiple tuple items by referring to the index number, inside square brackets.
-> The first item has index 0, second item has index 1 and so on.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

#8. Negative Indexing In Tuple
"""
-> Negative indexing means starting from the end that means -1 refers to last item, -2 refers to the second last item and so on.
"""
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


#9. Range Of Indexes In Tuple
"""
-> We can specify a range of indexes by specifying where to start and where to end the range.
-> When specifying a range, the return value will be a new tuple with the specified items.
-> We can also specify the negative indexes, if we want to start the search from the end of the tuple.
"""

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])       #The Search Will Start At Index 2(Included) And End At Index 5(Not Included)
print(thistuple[:4])        #By Leaving Out The Start Value, The Range Will Start At The First Item
print(thistuple[2:])        #By Leaving Out The End Value, The Range Will Go On To The End Of The Tuple
print(thistuple[-4:-1])     #The Search Will Start At Index -4(Included) And End At Index -1(Not Included)


#10. Check If Item Exists
"""
-> To determine if a specified item is present in a tuple we can use 'in' keyword.
"""
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")



#11. Changing/Updating Tuple Values
"""
-> Tuples are unchangeable, meaning that we cannot change ,add, or remove items once the tuple is created.
-> Once a tuple is created, we cannot change its values. Tuples are unchangeable, or immutable as it also is called.
-> Since tuples are immutable, they do not have a built-in append() method, but there are some workarounds to add items to a tuple.
    1. Convert Into List    : We can convert the tuple into a list, add items and convert back into a list.
    2. Add Tuple To A Tuple : We are allowed to add tuples to tuples, so if we want to add one or more item, create a new tuple with the 
                              item(s), and add it to a existing tuple. 
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
y = ("papaya",)       # Remember To Include A Comma After The Item, When Creating A Tuple With Only One Item
thistuple += y

print(thistuple)

#12. Removing Tuple Items
"""
-> Tuples are unchangeable, so we cannot remove items from it, but we can convert the tuple into a list, remove items and convert back into tuple.
-> Or, we can delete the tuple completely using 'del' keyword.
"""
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)


thistuple = ("apple", "banana", "cherry")
del thistuple
#print(thistuple) #This Will Raise An Error Because The Tuple No Longer Exists



#13. Unpacking A Tuple
"""
-> When we create a tuple, we normally assign values to it. This is called "packing" a tuple.
-> But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking".
-> While unpacking, the number of variables must match the number of values in the tuple, if not, we must use an 
   asterick(*) to collect the remaining values as a list.
"""

fruits = ("apple", "banana", "cherry")     #Packing

(green, yellow, red) = fruits              #Unpacking

print(green)
print(yellow)
print(red)



#14. Unpacking Using Asterick(*)
"""
-> If the number of variables is less than the number of values, we can add (*) to the variable name and the values will be assigned 
   to a variable as a list.
-> If the asterick is added to another variable name than the last, Python will assign values to the variable until the number of values
   left matches the number of variables left.
"""
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)


fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)



#15. Looping Through A Tuple
"""
-> We can loop through the tuple items by using a for loop.
"""
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


#16. Loop Through The Index Numbers
"""
-> We can also loop through the tuple items by referring to their index numbers.
-> We can use range() and len() functions for this.
"""
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])


#17. Using A While Loop
"""
-> We can loop through the tuple items by using a while loop.
-> Use the len() function to determine the length of the tuple, then start at 0 and loop through the tuple items 
   by referring to their indexes. Then we have to increase the index by 1 after each iteration.
"""
thistuple = ("cat","dog","rabbit")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1


#18. Join Two Tuples
"""
-> To join two or more tuples we can use the '+' operator.
"""
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)




#19. Multiply Tuples
"""
-> If we want to multiply the content of a tuple a given number of times, we can use '*' operator.
"""

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)