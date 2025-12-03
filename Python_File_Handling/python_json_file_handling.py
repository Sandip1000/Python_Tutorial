#1. Python "json" File Handling
"""
-> json stands for Javascript Object Notation.
-> Python provides a built-in module json for working with JSON files.
"""




#2. Writing To A JSON File

import json
path=fr"Python_File_handling\datafiles\example.json"
data=[
    {
        "name":"Alice",
        "age":25,
        "city":"London"
    }
]
with open(path,"w") as file:
    json.dump(data, file, indent=4)


#3. Reading A JSON File


with open(path,"r") as file:
    data=json.load(file)

print(data)





#4. Appending To A JSON File
"""
-> JSON files do not support direct append like CSV/text files.
-> Instead, we must:
    1. Read the file
    2. Modify the data
    3. Write it back
"""

with open(path,"r") as file:
    data=json.load(file)

new_data={ 
        "name":"Bob",
        "age":20,
        "city": "Manchester"
    }
data.append(new_data)

with open(path,"w") as file:
    json.dump(data,file,indent=4)


with open(path,"r") as file:
    data=json.load(file)

