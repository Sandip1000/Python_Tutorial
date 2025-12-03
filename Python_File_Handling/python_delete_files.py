#1. Python Delete File
"""
To delete a file, we must import the os module, and run its os.remove() function.
"""
path=fr"Python_File_Handling\datafiles\newfile.txt"
import os
os.remove(path)




#2. Checking If File Exists
"""
-> To avoid getting an error, we might want to check the file exists before we try to delete it.
"""
import os
if os.path.exists(path):
  os.remove(path)
else:
  print("The file does not exist")



#3. Deleting A Folder
"""
-> To delete an entire folder, we use the os.rmdir() function.
-> We can only remove empty folders.
"""
# import os
# os.rmdir("myfolder")