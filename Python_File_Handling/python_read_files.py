#1. Python File Opening
"""
-> To open the file, we use the built-in open() function.
-> The open() function returns the file object, which has a read() method for reading the content of the file
"""
path=fr"Python_File_Handling\datafiles\example.txt"

f = open(path,"rt")
print(f.read())






#2. Using The with Statement
"""
-> We can also use the "with" statement when opening a file.
-> We do not have to worry about closing our files, the "with" statement takes care of that.
"""
with open(path) as f:
  print(f.read())





#3. Closing Files
"""
-> It is a good practice to always close the file when we are done with it.
-> If we are not using "with" statement, we must write a close statement in order to close the file.
-> We should always close the files. In some cases, due to buffering, changes made to a file may not show until we close the file.
-> We use close() method to close a file.
"""
f = open(path)
print(f.readline())
f.close()





#4. Read Only The Parts Of The File
"""
-> By default the read() method returns the whole text, but we can also specify how many characters we want to return.
"""
with open(path) as f:
  print(f.read(5))   #Returns the 5 first characters of the file





#5. Reeading Lines
"""
-> We can return one line by using the readline() method.
-> By calling readline() two times, we can read the two first lines.
-> By looping through the lines of the file, we can read the whole file line by line.
"""
with open(path) as f:
  print(f.readline())    # Read first line



with open(path) as f:
  print(f.readline())    # Read first line
  print(f.readline())    # Read second line




with open(path) as f:
  for x in f:            # Looping through the lines of file
    print(x)