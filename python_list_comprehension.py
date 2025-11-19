#1. List Comprehension

"""
-> List comprehension offers a shorter syntax when we want to create a new list based on the values 
   of an existing list.

   Syntax:
   newlist=[expression for item in iterable if condition == True]

-> The return value is a new list, leaving the old list unchanged.

-> The condition is like a filter that only accepts the items that evaluate to True. The condition is optional and 
   can be omitted.

-> The iterable can be any iterable object, like a list,tuple, set etc.

-> The expression is the current item in the iteration, but it is also the outcome, which we can manipulate before it ends up 
   like a list item in the new list.
"""

#Using For Loop

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#Using List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

#Some Examples Related To List Comprehension

newlist = [x for x in range(10) if x < 5]
print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]    #Coverted to Upper Case Before Inserting To New List
print(newlist)



list_of_num=[1,2,3,4]
list_of_square_of_num=[num**2 for num in list_of_num]    #Calculating The Square Of The Numbers Of The List And Inserting Into New List
print(list_of_square_of_num)

list_of_square_of_even_numbers=[num**2 for num in list_of_num if num%2==0]   #Calculating The Square Of The Numbers If The Numbers Are Even
print(list_of_square_of_even_numbers)



#2. Set Comprehension
"""
Syntax:
    new_set={expression for item in sequence if condition }

"""

set_of_num={1,2,3,4,5}
set_of_square_of_num=set()

#Without Using Set Comprehension
for num in set_of_num:
    square=num**2
    set_of_square_of_num.add(square)
print(set_of_square_of_num)

#Using Set Comprehension
set_of_square_of_num={num**2 for num in set_of_num}
print(set_of_square_of_num)



#3. Dictionary Comprehension
"""
Syntax:
    new_dict={key:expression for key ,value in dict.items() if condition}
"""

#Without Using Dictionary Comprehension 

ori_dict={"a":1,"b":2,"c":3}
swapped_dict={}

for key,value in ori_dict.items():
    swapped_dict[value]=key
print(swapped_dict)    


#Using Dictionary Comprehension

ori_dict={"a":1,"b":2,"c":3}
swapped_dict={value:key for key,value in ori_dict.items()}
print(swapped_dict)


#Create A New Dictionary In Which Only Even Values From Original Dictionary Are Stored After Squaring It
ori_dict={"a":1,"b":2,"c":3}
new_dict={key:value**2 for key,value in ori_dict.items() if value%2==0}

print(new_dict)