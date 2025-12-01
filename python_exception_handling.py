#1. Python Try Except
"""
-> The "try" block lets us to test a block of code for errors.
-> The "except" block lets us to handle the error.
-> The "else" block lets us to execute code when there is no error.
-> The "finally" block lets us to execute code, regardless of the result of the try and except blocks.
"""



#2. Exception Handling
"""
-> When an error occurs, or exception as we call it, Python will normally stop and generate an error message.
-> These exceptions can be handled using the "try" statement.
"""
# try:
#   print(x)     #The try block will generate error, because x is not defined.
# except:
#   print("An exception occurred")  #Since try block raises an error, the except block will be executed.
def square_root(x):
    if x<10:
        raise
    return x**0.5

try:
    number=-10
    square_root_of_number=square_root(number)
    print(f"Square of {number} is {square_root_of_number}")

except Exception:   #Here, Exception is a base class for all types of exceptions
    print("Exception occured.")





#3. Many Exceptions
"""
-> We can define as many exceptions blocks as we want, eg if we want to execute a special block of code 
   for a special kind of error.
-> There are many built-in exceptions we can use.
"""

# try:
#   print(x)
# except NameError:    #NameError is an built-in exceptions
#   print("Variable x is not defined")
# except:
#   print("Something else went wrong")




#4. Else Block
"""
-> We can use the "else" keyword to define a block of code to be executed if no errors were raised.
"""
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")






#5. Finally Block
"""
-> The finally block, if specified , will be executed regardless if the try block raises an error or not.
-> This can be useful to close objects and clean up resources.
"""

# try:
#   print(x)
# except:
#   print("Something went wrong")
# finally:
#   print("The 'try except' is finished")




try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")










#6. Raise An Exception
"""
-> As a Python developer we can choose to throw an exception if a condition occurs.
-> To throw(or raise) an exception, we can use "raise" keyword.
-> The "raise" keyword is used to raise an exception.
-> We can define what kind of error to raise, and the text to print to the user.
"""
# x = -1

# if x < 0:
#   raise Exception("Sorry, no numbers below zero")





# x = "hello"

# if not type(x) is int:
#   raise TypeError("Only integers are allowed")







#7. Custom Exception Handling

class SquareofOddError(Exception):     #Exception is an base class for all exceptions
    def __init__(self,number):
        self.number=number
        self.message=f"{number} is an even number"

        super().__init__(self.message)

number=int(input("Enter the number: "))

if __name__=="__main__":
    try:
        if number%2!=0:
            result=number**2
            print(result)
        else:
            raise SquareofOddError(number)
    except SquareofOddError as e:
        print(e.message)
        print("Sqaure of even number is not possible in our program")

print("end of program")