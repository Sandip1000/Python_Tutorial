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
