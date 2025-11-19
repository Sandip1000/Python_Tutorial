#1. Python Sets
"""
-> Sets are used to store mutiple items in a single variable.
-> A set is a collection which is unordered, unchangeable and unindexed.
-> Set items are unchangeable, but we can remove items and add new items. Once a set is created, we cannot change
   its items.
-> Set items are unordered, so we cannot be sure in which order the items will appear. Items in a set
   do not have a defined order. Set items can appear in a different order every time we use them, and cannot be referred to by
   index or key
-> Duplicates are not allowed in the sets. Sets cannot have two items with the same value. Duplicate values will be ignored.
-> Sets are written with curly brackets.
"""

thisset={}       # But This Is Not An Empty Set, This Is An Empty Dictionary
print(thisset)
print(type(thisset))

thisset=set()   #Creating An Empty Set
print(thisset)

thisset = {"apple", "banana", "cherry"}  #This Is A Set
print(thisset)
print(type(thisset))

thisset = {"apple", "banana", "cherry", "apple"}  #Duplicates Are Not Allowed And Gets Ignored In Sets
print(thisset)


thisset = {"apple", "banana", "cherry", True, 1, 2} #The Values 'True' And '1' Are Considered The Same Value In Sets, And Are Treated As Duplicates
print(thisset)

thisset = {"apple", "banana", "cherry", False, True, 0} #The Values 'False' And '0' Are Considered The Same Value In Sets, And Are Treated As Duplicates
print(thisset)


#2. Length Of A Set
"""
-> To determine how many items a set has, we can use len() function.
"""
thisset = {"apple", "banana", "cherry"}
print(len(thisset))


#3. Set Items-Data Types
"""
-> Set items can be of any data type.
-> A set can contain different data types.
"""

set1 = {"apple", "banana", "cherry"}    #String
set2 = {1, 5, 7, 9, 3}                  #Integer
set3 = {True, False, False}             #Boolean
set4 = {"abc", 34, True, 40, "male"}    #Set With Multiple Data Type


#4. Set Type
"""
-> From Python's perspective, sets are defined as objects with the data type 'set'.
"""
myset = {"apple", "banana", "cherry"}
print(type(myset))


#5. The set() Constructor
"""
-> It is also possible to use the set() constructor to make a set.
"""
thisset = set(("apple", "banana", "cherry"))   # Note The Double Round-Brackets
print(thisset)

#6. Access Set Items
"""
-> We cannot access items in a set by referring to an index or a key.
-> But we can loop through the set items using for loop, or ask if a specified value is present
   in a set, by using the 'in' keyword.
-> Once a set is created, we cannot change its items, but we can add items.
"""
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)


if "banana" in thisset:    #Check If Item Exists
  print("Yes,'banana' exits in the set")


if "mango" not in thisset:  #Check If Item Does Not Exist
  print("No, 'mango' does not exist in the set")


#7. Add Set Items
"""
-> Once set is created, we cannot change its items, but we can add items.
-> To add one item to a set, we can use add() function.
"""
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


#8. Add Sets
"""
-> To add items from another set into the current set, we can use update() method.
"""
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


#9. Add Any Iterable
"""
-> The object in the update() method does not have to be a set, it can be any iterable objects(tuples, lists, dictionaries etc).
"""
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
print(type(thisset))



#10. Remove Set Items
"""
-> To remove an item in a set, we can use remove(), or the discard() method.
-> If the item to remove does not exist, remove() will raise an error.
-> If the item to remove does not exist, discard() will not raise an error.
"""

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)



#11. Removing Item Using pop() Method
"""
-> We can also use pop() method to remove an item from set, but this method will remove a random item, so we cannot be sure
   what item that gets removed. It is because the sets are unordered.
-> The return value of the pop() method is the removed item.
"""
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


#12. Clearing And Deleting Set
"""
-> The clear() method empties the set.
-> The 'del' keyword will delete the set completely.
"""
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)



thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset)   #This Will Raise An Error




#13. Loop Through Set Items
"""
-> We can loop through the set items by using a for loop.
"""

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)




#14. Set Union
"""
-> The union() method returns a new set with all items from both sets.
-> We can also use the '|' operator instead of the union() method, and we will get the same result.
"""

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)


#15.Joining Multiple Sets
"""
-> All the joining methods and operators can be used to join multiple sets.
-> When using a union() method, just add more sets in the parentheses, separated by commas.
-> When using '|' operator, separate the set with more '|' operators.
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)



set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 |set4
print(myset)



#16. Join A Set And A Tuple
"""
-> The union() method allows us to join a set with other data types, like lists or tuples.
-> The result of the operation will also be a set.
-> The '|' operator only allows us to join sets with sets, and not with other data types like we can with the
   union() method.
"""
x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)


#17. Join Using update() Method
"""
-> The update() method inserts all items from one set into another.
-> The update() changes the original set, and does not return a new set.
-> Both union() and update() will exclude any duplicate items.
"""

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)


#18. Set Intersection
"""
-> The intersection() method will return a new set, that only contains the items that are present in both sets.
-> We can use the '&' operator instead of the intersection() method and we will get the same result.
-> The '&' operator only allows us to join sets with sets, and not with other data types like we can with the
   intersection() method.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}
set3 = set1.intersection(set2)  #The Values 'True' and '1' Are Considered The Same Value. The Same Goes For 'False' And '0'.
print(set3)


#19. The intersection_update() Method
"""
-> The intersection_update() method will also keep only the duplicates, but it will change the original set instead of 
returning a new set.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)


#20. Set Difference
"""
-> The difference() method will return a new set that will contain only the items from the first set that are not present in
   the other set.
-> We can also use '-' operator instead of the difference() method, and we will get the same result.
-> The '-' operator only allows us to join sets with sets, and not with other data types like we can with the difference() method.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)




#21. The difference_update() Method
"""
-> The difference_update() method will also keep the items from the first set that are not in the other set, but it will change the 
   original set instead of returning a new set.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)


#22. Symmetric Difference
"""
-> The symmetric_difference() method will keep only the elements that are not present in both sets.
-> We can also use '^' operator instead of the symmetric_difference() method, and we will get the same result.
-> The '^' operator only allows us to join sets with sets, and not with other data types like  we can with the 
   symmetric_difference() method.
"""

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)


#23. The symmetric_difference_update() Method
"""
-> The symmetric_difference_update() method will also keep all but the duplicates, but it will change the original set 
   instead of returning a new set.
"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)



#24. FrozenSet
"""
-> Frozenset is an immutable version of a set.
-> Like sets, it contains unique, unordered, and unchangeable elements.
-> Unlike sets, elements cannot be added or removed from a frozenset.
-> We have to use frozenset() constructor to create a frozenset from any iterable.
-> Being immutable means we cannot add or remove elements in frozenset. However, frozensets support all non-mutating
   operations of sets like intersection, union, difference etc.
"""

x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))