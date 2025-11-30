#1. Python Dates
"""
-> A date in Python is not a data type of its own, but we can import a module named
   "datetime" to work with dates as date objects.
"""
import datetime
x=datetime.datetime.now()
print(x)



#2. Date Output
"""
-> When we execute the code from the example above the result will be:
   For Example: 2025-12-01 00:01:32.113177
-> The date contains year, month, day, hour, minute, second, and microsecond.
-> The "datetime" module has many methods to return information about the date object.
"""

import datetime

x = datetime.datetime.now()

print(x.year)    #Returns The Year
print(x.strftime("%A")) #Returns the Day



#3. Creating A Date Object
"""
-> To create a date, we can use the datetime() class(constructor) of the datetime module.
-> The datetime() class requires three parameters to create a date: year, month, day.
-> The datetime() class also takes parameters for time and timezone(hour, minute, second, microsecond, tzone),
   but they are optional, and has a default value of 0,(None for timezone).
"""
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)





#4. The strftime() Method
"""
-> The datetime object has a method for formatting date objects into readable strings.
-> The method is called strftime(), and takes one parameter, format, to specify the format of the returned string.
"""
import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))     #Returns Name Of The Month