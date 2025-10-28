#Python Operators
"""
-> Operators are used to perform operations on variables and values.
-> Python divides the operators in the following groups:
    1. Arithmetic Operators
    2. Assignment Operators
    3. Comparison Operators
    4. Logical Operators
    5. Identity Operators
    6. Membership Operators
    7. Bitwise Operators
"""

#1. Arithmetic Operators
"""
-> Arithmetic Operators are used with numeric values to perform common mathematical operations.
   1. Addition (+)
   2. Subtraction (-)
   3. Multiplication (*)
   4. Division (/) -> It always returns a float value.
   5. Modulus (%)
   6. Exponentiation (**) 
   7. Floor Division (//) ->It always returns an integer.
"""
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)  #It rounds down to the nearest integer.




#2. Assignment Operators

"""
-> Assignment Operators are used to assign values to variables.

"""
x=5
print(x)

x+=3   #x = x + 3
print(x)

x-=3   #x = x - 3
print(x)

x*=3   #x = x * 3
print(x)

x/=3   #x = x / 3
print(x)

x%=3   #x = x % 3
print(x)

x=7
x//=3  #x = x // 3
print(x)


x**=3  #x= x ** 3
print(x)

x=2
x&=3   #x= x & 3 AND operator
print(x)

x|=5  #x= x | 3  OR operator
print(x)

x=5
x^=3  #x= x ^ 3  XOR operator
print(x)

x>>=2  #x= x >> 6
print(x)

x<<=2 #x= x << 6
print(x)

print(x:=3)  # x=3  print(x)


"""
-> The Walrus Operator(:=)
-> It assigns values to variables as a part of larger expression.
"""

numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")



#3. Comparison Operator

"""
-> They are used to compare two values.
   1. Equal (==)
   2. Not Equal (!=)
   3. Greater Than (>)
   4. Less Than (<)
   5. Greater Than or Equal To (>=)
   6. Less Than or Equal To (<=)

-> Comparison Operators returns True or False based on comparison.
"""

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

"""
Chaining Comparison Operators
-> Python allows us to chain comparison operators.
"""

x = 5

print(1 < x < 10)

print(1 < x and x < 10)





#4. Logical Operators
"""
-> Logical operators are used to combine conditional statements.
    1. and -> Returns True if both statements are True.
    2. or  -> Returns True if one of the statements is True.
    3. not -> Reverse the result, returns False if the statement is True. 
"""
x = 5

print(x > 0 and x < 10)

print(x < 5 or x > 10)

print(not(x > 3 and x < 10))


#5. Identity Operators

"""
-> Identity Operators are used to compare objects, not if they are equal, but if they are actually the same object, with the
   same memory location.
    1. is     -> Returns True if both variables are the same object.
    2. is not -> Returns True if both variables are not the same object.
"""

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)
print(x is not y)

"""
-> Difference between is and ==
    1. is -> Checks if both variables point to the same object in memory.
    2. == -> Checks if the values of both variables are equal.
"""

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#6. Membership Operators
"""
-> Membership operators are used to test if a sequence is presented in an object.
    1. in     -> Returns True if a sequence with the specified value is present in the object
    2. not in -> Returns True if a sequence with the specified value is not present in the object
"""

fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"  # Membership operator can also be used in strings.

print("H" in text)
print("hello" in text)
print("z" not in text)

#7. Bitwise Operators
"""
-> Bitwise operators are used to compare binary numbers.
   1. AND (&)                    ->  Sets each bit to 1 if both bits are 1
   2. OR  (|)                    ->  Sets each bit to 1 if one of two bits is 1
   3. XOR (^)                    ->  Sets each bit to 1 if only one of two bits is 1
   4. NOT (~)                    ->  Inverts all the bits
   5. Zero Fill Left Shift  (<<) ->  Shift left by pushing zeros in from the right and let the leftmost bits fall off
   6. Zero Fill Right Shift (>>) ->  Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
"""


"""
-> Example 1
    The binary representation of 6 is 0110
    The binary representation of 3 is 0011
    Then the & operator compares the bits and returns 0010, which is 2 in decimal.
"""
print(6 & 3)


"""
-> Example 2
    The binary representation of 6 is 0110
    The binary representation of 3 is 0011
    Then the | operator compares the bits and returns 0111, which is 7 in decimal.
"""
print(6 | 3)

"""
-> Example 3
    The binary representation of 6 is 0110
    The binary representation of 3 is 0011
    Then the ^ operator compares the bits and returns 0101, which is 5 in decimal.
"""
print(6 ^ 3)



#8. Operator Precedance
"""
-> Operator precedance describes the order in which  operations are performed.
     1.  Parentheses                                           ->  ()      (Higher Precedance)
     2.  Exponentation                                         ->  **
     3.  Unary plus, unary minus, and bitwise NOT              ->  +x, -x, ~x
     4.  Multiplication, division, floor division, and modulus ->  *, /, //, %
     5.  Addition and subtraction                              ->  +, -
     6.  Bitwise left and right shifts                         ->  <<, >>
     7.  Bitwise AND                                           ->  &
     8.  Bitwise XOR                                           ->  ^
     9.  Bitwise OR                                            ->  |
     10. Comparison,identity and membership operators          ->  ==, !=, >, >=, <, <=, is, is not, in, not in
     11. Logical NOT                                           ->  not
     12. Logical AND                                           ->  and
     13. Logical OR                                            ->  or       (Lower Precedance)
"""

print((6 + 3) - (6 + 3))  # Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first.
print(100 + 5 * 3)        # Multiplication * has higher precedence than addition +, and therefore multiplications are evaluated before additions.

"""
-> Left to Right Evaluation
       If two operators have the same precedence, the expression is evaluated from left to right.
"""
print(5 + 4 - 7 + 3)     # Addition + and subtraction - has the same precedence, and therefore we evaluate the expression from left to right.