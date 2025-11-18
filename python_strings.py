# Python Strings

"""
-> Strings in python are surrounded by either single quotation marks, or double quotation marks.
"""
print('Hello')
print("Hello")

#1. Quotes Inside Quotes
"""
-> We can use quotes inside quotes, as long as they don't match the quotes surrounding the string.
"""
print("It's alright.")
print("He is called 'Johhny'")
print('He is called "Johhny"')

#2. Assign String To a Variable

a="This is a string"
print(a)

#3. Multiline Strings
"""
-> We can assign a multiline string to a variable by using three quotes(single or double quotes).
"""
a="""This is a
multiline
strings.
"""
print(a)

#4. Strings Are Arrays of Characters
"""
-> Like many other popular programming languages, strings in Python are arrays of unicode characters.
-> However, Python does not have a character datatype, a single character is simply a string with lenght 1.
-> Square brackets can be used to access elements of the string.
-> The position of the first character in the string is zero.
"""
a="Hello"
print(a[0]) #Indexing starts from 0
print(a[1])


#5. Looping Through String
"""
-> Since strings are arrays, we can loop through the characters in a string, with a for loop.
"""
x="Hello! World"
for characters in x:
    print(characters)



#6. String Length
"""
-> To get the length of a string, use the len() function.
"""

x="Hello! World"
print(len(x))
print(x[len(x)-1])


#7. Check String

"""
-> To check if a certain phrase or character is present in a string, we can use a keyword 'in'.
-> To check if a certain phrase or character is not present in a string, we can use a keyword 'not in'.
"""

text="This is a string."

print("is" in text)
print("a" in text)
print("the" in text)


print("the" not in text)
print("This" not in text)



#8. Slicing Of String
"""
-> We can return a range of characters by using the slice syntax.
-> Specify the start index and the end index separated by colon, to return a part of the string.
-> By leaving out the start index, the range will start at the first character.
-> By leaving out the end index, the range will go to the end.
"""
a="Hello! World"
print(a[2:5])      # Get the characters from the position 2 to position 5(not included)
print(a[:5])       # Get the characters from the start to position 5(not included)
print(a[2:])       # Get the characters from position 2, and all the way to the end



#9. Negative Indexing
"""
-> We can use negative indexes to start the slice from the end of the string.
-> The postion of last character in the string is -1.
"""
b="Hello! World"
print(b[-5:-2])     # Get the characters from the postion -5 to the position -2(not included).


#10. Useful String Methods
"""
-> Python has set of built-in methods that we can use on strings.
-> All string methods return new values. They do not change the original string.
"""

a=" Hello, World!"

print(a.upper())                # The upper() method returns the string in upper case.
print(a.lower())                # The lower() method returns the string in lower case.
print(a.strip())                # The strip() method removes the whitespace from the beginning or end. Whitespace is the space before and/or after the actual text.
print(a.replace("H", "J"))      # The replace() method replaces a string with another string.
print(a.split(','))             # The split() method splits the string into substrings if it finds instances of the separator. It then returns list of substrings.





#11. String Concatenation
"""
-> To concatenate, or combine, two strings we can use '+' operator.
"""
a="Hello"
b="World"
c=a+b
d=a+" "+b
print(c)
print(d)



#12. String Formatting
"""
-> We can combine strings and numbers by using f-strings or the format method.
-> To specify a string as an f-string, simply put an 'f' in front of the string literal, and add 
   curly brackets {} as placeholders for variables and other operations.
"""

age=16
txt=f"My name is John, I am {age}."
print(txt)

# Placeholders and Modifiers
"""
-> A placeholder can contain variables, operations, functions, and modifiers to format the value.
-> A placeholder can include a modifier to format the value.
-> A modifier is included by adding colon(:) followed by a legal formatting type, like '.2f' which 
   means fixed point number with 2 decimals.
-> A placeholder can contain Python code, like math operations.  
"""
price=100
txt= f"The price is {price:.2f} dollars."
print(txt)

txt= f"The price is {20*10} dollars."
print(txt)


#13. Escape Characters

"""
-> To insert characters that are illegal in a string, we can use an escape character.
-> An escape character is a backlash (\) followed by the character that we want to insert.
-> The escape character allows us to use double quotes when we normally would not be allowed. 
"""

txt="We are the so-called \"Vikings\" from the north."
print(txt)

txt="This is the first line.\nThis is the second line."
print(txt)

# Some Escape Characters

#   """
#   \'   = Single Quote
#   \\   = Backslash
#   \n   = New Line
#   \r   = Carriage Return
#   \t   = Tab
#   \b   = Backspace
#   \f   = Form Feed
#   \ooo = Octal Value
#   \xhh = Hex Value
#   """