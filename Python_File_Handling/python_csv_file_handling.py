#1. Python "csv" File Handling
"""
-> csv stands for Comma Separated Values
-> Python has built-in csv module for handling csv files.
-> Python's csv module is great for lightweight and fast csv handling.
"""



#2. Writing A CSV File


#Using csv.writer
import csv

path1=fr"Python_File_handling\datafiles\example1.csv"

with open(path1,"w",newline='') as file:
    writer=csv.writer(file)
    writer.writerow(["name","age"])
    writer.writerow(["Alice",25])



#Using csv.DictWriter

path2=fr"Python_File_handling\datafiles\example2.csv"

with open(path2,"w",newline='')as file:
    fieldnames=["name","age"]
    writer=csv.DictWriter(file,fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name":"Bob","age":25})



#3. Reading A CSV File

#Using csv.reader

with open(path1,"r") as file:
    reader=csv.reader(file)
    for row in reader:  
        print(row)


#Using csv.DictReader

with open(path2,"r") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row["name"],row["age"])




#4. Appending To A CSV File

with open(path1,"a",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["Charlie",28])





#5. Reading CSV Into A List

rows=[]
with open(path1) as file:
    reader=csv.reader(file)
    for row in reader:
        rows.append(row)
    
print(rows)