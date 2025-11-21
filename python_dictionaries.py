#1. Python Dictionary
"""
-> Dictionaries are used to store data values in key:value pairs.
-> A dictionary is a collection which is ordered, changeable and do not allow duplicates.
-> Dictionaries are written with curly brackets, and have keys and values.
-> Dictionary items are ordered, changeable and do not allow duplicates.
-> Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
-> When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
-> Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
-> Dictionaries does not allow duplicates that means it cannot have two items with the same key.
"""

thisdict={}            #Empty Dictionary
print(thisdict)
print(type(thisdict))



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
print(thisdict["brand"])   #Accessing Dictionary Value Using Key



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)       #Duplicate Values Will Overwrite Existing Values




#2. Dictionary Length
"""
-> To determine how many items a dictionary has, we can use len() function.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(len(thisdict))




#3. Dictionary Items-Data Types
"""
-> The values in dictionary items can be of any data type.
"""

thisdict = {
  "brand": "Ford",                         #String
  "electric": False,                       #Boolean
  "year": 1964,                            #Integer
  "colors": ["red", "white", "blue"]       #List
}
print(thisdict)




#4. Dictionary Type
"""
-> From Python's perspective, dictionaries are defined as objects with data type 'dict'.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))



#5. The dict() Constructor
"""
-> It is also possible to use the dict() constructor to make a dictionary.
"""
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)



#6. Accessing Dictionary Items
"""
-> We can access the items of a dictionary by referring to its key name, inside square brackets.
-> There is also a method called get() that will give the same result.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
y=thisdict.get("brand")   #Using get() Method
print(y)



#7. Get Dictionary Keys
"""
-> The keys() method will return a list of all keys in the dictionary.
-> The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be 
   reflected in the keys list.
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x)                     #Before The Change

car["color"] = "white"

print(x)                     #After The Change


#8. Get Dictionary Values
"""
-> The values() method will return a list of all values in the dictionary.
-> The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected 
   in the values list.
"""
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)                #Before The Change

car["year"] = 2020

print(x)                #After The Change




car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()

print(x)                  #Before The Change

car["color"] = "red"

print(x)                  #After The Change



#9. Get Dictionary Items
"""
-> The items() method will return each item in a dictionary, as tuples in a list.
-> The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will
   be reflected in the items list.
"""


car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x)               #Before The Change

car["year"] = 2020

print(x)               #After The Change




car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.items()

print(x)                 #Before The Change

car["color"] = "red"

print(x)                 #After The Change




#10. Check If Key Exists
"""
-> To determine is a specified key is present in a dictionary, we can use the 'in' keyword.
"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")





#11. Changing Dictionary Values
"""
-> We can change the value of a specified item by referring its key name.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict["year"])





#12. Updating Dictionary Items

"""
-> We can use update() method to update the dictionary with the items from the given argument.
-> The argument must be a dictionary, or an iterable object with key:value pairs.
"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020, "model":"Tesla"})
print(thisdict["year"])
print(thisdict["model"])




#13. Adding Dictionary Items
"""
-> Adding an item to the dictionary is done by using a new index key and assigning a value to it.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)





#14. Adding Dictionary Items Using update() Method
"""
-> The update() method will update the dictionary with the items from a given argument. If the item does not exist, the 
   item will be added.
-> The argument must be a dictionary, or an iterable objectwith key:value pairs.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)



#15. Removing Dictionary Items
"""
-> The pop() method removes the item with the specified key name.
-> The popitem() method removes the last inserted item.
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)





thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)




#16. Removing Items Using 'del' Keyword
"""
-> The 'del' keyword removes the item with the specified key name.
-> The 'del' keyword can also delete the dictionary completely.
"""


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)



thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
#print(thisdict)         #This Will Cause An Error Because "thisdict" No Longer Exists




#17. Clearing All Dictionary Items
"""
-> The clear() method empties the dictionary.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)




#18. Looping Through A Dictionary

"""
-> We can loop through a dictionary by using a for loop.
-> When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


for x in thisdict:
  print(x)                  #Print All Keys




for x in thisdict.keys():
  print(x)                  #Print All Keys Using keys() method



for x in thisdict:
  print(thisdict[x])        #Print All Values



for x in thisdict.values():
  print(x)                 #Print All Values Using values() Method




for x, y in thisdict.items():
  print(x, y)             #Loop Through Both Using keys and values Using items() Method





#19. Copying A Dictionary
"""
-> We cannot copy a dictionary simply by typing dict2 = dict1, because dict2 will only be a refrence to dict1, and 
   changes made in dict1 will automatically also be made in dict2.
-> There are several ways to make a copy of dictionary like using copy() and dict() method.
"""

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()                       #Using copy() Method
print(mydict)

thisdict.update({"color": "red"})
print(thisdict)

print(mydict)       #Changes Made In thisdict Does Not Affect mydict




thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)     #Using dict() Method
print(mydict)






#20. Nested Dictionaries
"""
-> A dictionary can contain dictionaries, this is called nested dictionaries.
"""


#Method 1
myfamily = {                           
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)





#Method 2
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}






#21. Accessing Items In Nested Dictionaries
"""
-> To access items from a nested dictionary, we can use the name of the dictionaries, starting with 
   the outer dictionary.
"""
print(myfamily["child2"]["name"])









#22. Looping Through Nested Dictionaries
"""
-> We can loop through a dictionary by using the items() method.
"""
for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])