#1. Python File Write
"""
-> To write to an existing file, we must add a parameter to the open() function.
    1. "a"  : Append - Appends the content to the end of the file
    2. "w"  : Write - Overwrites the existing content
-> We use the write() method to write the content in file.
"""


#2. Writing To An Existing File Using "a" Parameter

path=fr"Python_File_Handling\datafiles\example.txt"

with open(path, "a") as f:
  f.write("Now the file has more content!")

#open and read the file after the appending:
with open(path) as f:
  print(f.read())



#3. Overwriting Existing Content Using "w" Parameter

with open(path, "w") as f:
  f.write("Woops! I have deleted the content!")

#open and read the file after the overwriting:
with open(path) as f:
  print(f.read())





#4. Creating A New File
"""
-> To create a new file in Python, we use the open() method, with one of the following parameters:

   1. "x" : Create - It will create a new file and returns an error if the file exists.
   2. "a" : Append - It will create a file if the specified file does not exist.
   3. "w" : Write - It will create a file if the specified file does not exist.
"""
path=fr"Python_File_Handling\datafiles\newfile.txt"
#f = open(path, "x")     #Creates a new empty file
f = open(path, "w")
f.write("A New File Is Created...")
f.close()