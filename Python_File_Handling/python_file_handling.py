#1. Python File Handling
"""
-> File handling is an important part of any web application.
-> Python has several functions for creating, reading, updating, and deleting files.
"""



#2. open() Function In File Handling
"""
-> The key function for working with files in Python is the open() function.
-> The open() function takes two parameters; filename, and mode.
-> There are four different methods(modes) for opening a file:
     
    1. "r"   : Read - Default value. Opens a file for reading, error if the file does not exist.
    2. "a"   : Append - Opens a file for appending, creates the file if it does not exist.
    3. "w"   : Write - Opens a file for writing, creates the file if it does not exist.
    4. "x"   : Create - Creates the specified file, returns an error if the file exists.


-> In addition we can specify if the file should be handled as binary or text mode
    
    1. "t"   : Text - Default value. Text mode
    2. "b"   : Binary - Binary mode(e.g., images)


Syntax:
 
open(file_name, mode)
"""


path = "Python_File_Handling\datafiles\example.txt"


f = open(path,"xt")
f = open(path,"rt")  #Here "r" for read, and "t" for text are the default values, we do not need to specify them
