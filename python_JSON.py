#1. Python JSON
"""
-> JSON is a syntax for storing and exchanging data.
-> JSON is text, written with JavaScript Object Notation.
-> Python has a built-in package called "json", which can be used to work with JSON data.
"""



#2. Parse JSON -Covert From JSON To Python

"""
-> If we have a JSON string, we can parse it by using json.loads() method.
-> The result will be a Python dictionary.
"""
import json

# Some JSON
x =  '{ "name":"John", "age":30, "city":"New York"}'

# Parse x
y = json.loads(x)

# The result is a Python dictionary
print(y)
print(type(y))
print(y["age"])





#3. Convert From Python To JSON
"""
-> If we have a Python object, we can convert it into a JSON string by using the json.dumps() method.
"""



import json

# A Python Object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# Convert Into JSON:
y = json.dumps(x)

# The result is a JSON string:
print(y)
print(type(y))







#4. Converting Python Different Types Into JSON Strings
"""
-> We can convert Python objects of the following types, into JSON strings.
   1. dict
   2. list
   3. tuple
   4. string
   5. int
   6. float
   7. True
   8. False
   9. None

   
-> When we convert from Python to JSON, Python objects are converted into JSON(JavaScript) equivalent.

  Python                          JSON
1. dict                           Object
2. list                           Array
3. tuple                          Array
4. str                            String
5. int                            Number
6. float                          Number
7. True                           true
8. False                          false
9. None                           null
"""
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))




x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
y=json.dumps(x)   #Converted To JSON Strings
print(type(x))

print(y)
print(type(y))








#5. Formatting The Result
"""
-> The example above prints a JSON string, but it is not very easy to read, with no indentations and line breaks.
-> The json.dumps() method has parameters to make it easier to read the result.
-> We can also define the seperators, default value is (", " , ": "), which means using a comma and a space to separate 
   each object, and a colon and a space to separate keys from values.
"""
y=json.dumps(x, indent=4)
print(y)


y=json.dumps(x, indent=4, separators=(". ", " = "))
print(y)





#6. Order The Result
"""
-> The json.dumps() method has a parameters to order the keys in the result.
"""

y=json.dumps(x, indent=4, sort_keys=True)
print(y)