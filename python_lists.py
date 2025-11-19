#1. Python Lists
"""
-> Lists are used to store multiple items in a single variable.
-> Lists are created using square brackets.
-> List items are ordered, changeable, and allow duplicates.
-> List items are indexed, the first item has index [0], the second item has index [1] etc.
-> When we say that lists are ordered, it means that the items have a defined order, and that order 
   will not change. If you add new items to a list, the new items will be placed at the end of the list. But, there are some list 
   methods that will change order, but in general the order of the items will not change.
-> The list is changeable, meaning that we can change, add, and remove items in a list after 
   it has been created.
-> Since lists are indexed, lists can have items with the same value, that means it allows duplicate values.
"""
this_list=["apple","banana","cherry"]

print(this_list)

this_list.append("mango")               #List is ordered and changeable
this_list.append("apple")               #List allow duplicates
print(this_list)
print(this_list[0])                     #First list item
print(this_list[len(this_list)-1])      #Last list item


#2. List Length
"""
-> To determine how many items a list has, we can use len() function.
"""
list1=[1,2,3,4,5]
print(len(list1))


#3. List are Mutable Objects
"""
-> Mutable objects are those whose value or state can be modified after they are created, without creating a new 
   object in memory.
-> Changes made to a mutable object are reflected in all references pointing to that object.
-> They are generally not hashable, meaning they cannot be used as keys in dictionaries or elements in sets(unless they
   are specifically designed to be immutable, like frozenset).
"""
my_list = [1, 2, 3]
another_list = my_list  # another_list refers to the same object as my_list
my_list.append(4)
print(my_list)      # Output: [1, 2, 3, 4]
print(another_list) # Output: [1, 2, 3, 4] - another_list also changed


#4. List Items - Data Types
"""
-> List items can be of any data type.
-> A list can contain different data types.
"""

list1 = ["apple", "banana", "cherry"]   #String Data Type
list2 = [1, 5, 7, 9, 3]                 #Integer Data Type
list3 = [True, False, False]            #Boolean Data Type
list4 = ["abc", 34, True, 40, "male"]   #List with Multiple Data Types
print(list1)
print(list2)
print(list3)
print(list4)


#5. List Type
"""
-> From Python's Perspective, lists are defined as objects with the data type 'list'.
"""

mylist=["apple","banana","cherry"]
print(type(mylist))

#6. The list() constructor
"""
-> It is also possible to use the list() constructor when creating a new list.
"""
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#7. Access List Items
"""
-> List items are indexed and we can access them by reffering to the index number.
-> The first item of list is indexed as zero.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist[1])


#8. Negative Indexing In List
"""
-> Negative indexing means start from the end, -1 refers to the last item and -2 refers to the second last item etc.
"""
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])       #Print last item


#9. Range of Indexes In List
"""
-> We can specify a range of indexes by specifying where to start and where to end the range.
-> When specifying a range, the return value will be a new list with the specified items.
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])     #The search will start at index 2(included) and end at the index 5(not included).
print(thislist[:4])      #By leaving out the start value, the range will start at the first item.
print(thislist[2:])      #By leaving out the end value, the range will go on to the end of the list.
print(thislist[-4:-1])   #The search will start at index -4(included) and end at the index -1(not included).
print(thislist[::-1])    #Reverse the list item



#10. Check If The Item Exists in List
"""
-> To determine if a specified item is present in a list, we can use the 'in' keyword.
"""
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:            #Checks if apple exits
  print("Yes, 'apple' is in the fruits list")


#11. Changing List Item
"""
-> To change the value of a specific item, we can use indexing.
"""
thislist = ["apple", "banana", "cherry"]
print(this_list)
thislist[1] = "mango"              #Changing second item
print(thislist)


#12. Changing Range of List Items
"""
-> To change the value of items within a specific range, define a list with new values, and
   refer to the range of index numbers where we want to insert new values.
-> If we insert more items than we replace, the new items will be inserted where we specified, and
   the remaining items will move accordingly. The length of the list will change when the number of 
   items inserted does not match the number of items replaced.
-> If we insert less items than we replace, the new items will be inserted where we specified, and the remaining 
   items  will move accordingly.
"""

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(len(thislist))
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
print(len(thislist))

thislist = ["apple", "banana", "mango","orange","kiwi","cherry","guava"]
thislist[1:4] = ["watermelon","pear"]
print(thislist)


#13. Insert Items
"""
-> To insert a new list item, without replacing any of the existing values, we can use insert() method.
-> The insert() method inserts an item at the specified index.
"""

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
print(len(thislist))


#14. Add/Append List Items
"""
-> To add an item to the end of the list, we can use append() method.
"""
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)


#15. Extend List
"""
-> To append elements from the another list to the current list, we can use the extend() method.
-> The elements eill be added to the end of the list.
"""
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

#16. Add any Iterable
"""
-> The extend() method does not have to append lists, we can add any iterable objects(tuples, sets, dictionaries etc).
"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)


#17. Remove Specified Item
"""
-> The remove() method removes the specified item.
-> If there are more than one item with the specified value,the remove() method removes the first occurrence. 
"""
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")     # Removes the first occurrence of banana
print(thislist)


#18. Remove Specified Index
"""
-> The pop() method removes the specified index.
-> If we do not specify the index, the pop() method removes the last item.
"""
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop()      #Removes the last item of the list
print(thislist)    

#19. Del Keyword

"""
-> The del keyword also removes the specified index.
-> The del keyword can also delete the list completely.
"""

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist


#20. Clear The List 
"""
-> The clear() method empties the list. The list still remains, but it has no content.
"""
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


#21. Loop Through a List

"""
-> We can loop through the list items by using a for loop.
"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


#21. Loop Through The Index Numbers
"""
-> We can also loop through the list items by referring to their index number.
-> We can use range() and len() method to create a suitable iterable.
"""

thislist = ["apple", "banana","orange", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])


#22. Looping Using While Loop
"""
-> We can loop through the list items using while loop.
-> Use the len() function to determine the length of the list, the start at 0 and loop through the list items by refferring their indexes.
-> Then we have to update the index by 1 after each iteration.
"""
thislist = [1,2,3,4,5]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1




#23. Loop Using List Comprehension
"""
-> List comprehension offers the shortest syntax for looping through lists.
"""

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]




#24. Sort List Alphanumerically
"""
-> List objects have a sort() method that will sort the list alphanumerically, ascending, by default.
-> To sort descending, we can use the keyword argument reverse=True.
"""
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)    #Sort In Descending Order
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)   #Sort In Descending Order
print(thislist)


#25. Customize Sort Function
"""
-> We can also customize our own function by using the keyword argument key = function.
-> The function will return a number that will be used to sort the list(the lowest number first).
"""
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)    #Sort the list based on how close the number is to 50.
print(thislist)


#25. Case Incensitive Sort
"""
-> By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters.
-> If we want a case-insensitive sort function, use str.lower as a key function.
"""

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()   #Case Sensitive Sorting
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)  #Case Insensitive Sorting
print(thislist)


#26. Reverse The order of List
"""
-> We can reverse the order of a list, regardless of the alphabet by using reverse() method.
-> The reverse() method reverses the current sorting order of the elements.
"""
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)


#27.Copy Lists
"""
-> We cannot copy a list simply by typing list2=list1, because list2 will only be a reference to list1, and
   changes made in list1 will automatically also be made in list2.
-> We can copy list by using copy() method, list() method and slice operator(:).
"""

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()    #Using Copy Method
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)     #Using List Method
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]        #Using Slice Operator
print(mylist)


#28. Join Lists
"""
-> There are the several ways to join, or concatenate, two or more lists in Python.
-> The most useful ways are + operator, for loop with append() method, and extend() method.
"""

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2   #Using + Operator
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)     #Using For Loop And append() Method

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)  #Using extend() method
print(list1)

#29. Nested List
"""
-> Nested List is khown as list inside a list.
"""
nestedList=[[1,2,3,4],["a","b","c","d"]]
print(f"First Element of Nested List: {nestedList[0]}")
print(f"Second Element of Nested List: {nestedList[1]}")
print(f"First Element of First List of Nested List: {nestedList[0][0]}")
print(f"First Element of Second List of Nested List: {nestedList[1][0]}")