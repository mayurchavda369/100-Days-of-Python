# Finally block in Python:
# its always executed if try-except block executed or not.
# The finally block is executed whether an exception occurs or not. 
# its use to utility purpose.
# It's typically used to perform cleanup actions, such as closing files or releasing 
# Ex 1:
# try:
#     n=int(input())
#     x=n//0
# except:
#     print("please enter valid number")
# finally:
#     print("Hi i am finally block")
# o/p->
# input is given 10. so 10 is not divide with zero so its give error.
# please enter valid number
# Hi i am finally block
# its use in file handling program.
# Ex 2:
# try:
#     # Code that might raise an exception
#     file = open("example.txt", "r")
#     data = file.read()
#     print(data)
# except FileNotFoundError:
#     print("Error: File not found")
# finally:
#     # Code that always runs, regardless of whether an exception occurred
#     file.close()
# so basically finally block is always executable.

# Raise in Exception Handling: raise Error name("message") 
# Basically you can give name of the error with message.
# raise statement is used to raise exceptions programmatically. 
# You can use the raise statement to interrupt the normal flow of the program and signal that an error or exceptional condition has occurred.
# This allows you to handle exceptional situations in a controlled manner.
# Ex:
# num=int(input("Enter number"))
# if num>10:
#     raise ValueError("Number is High")
# else:
#     print(num)

# o/p-> input given is 123.
# ---------------------------------------------------------------------------
# ValueError                                Traceback (most recent call last)
# c:\MY FILE\100 Days of Python\Day 24.py in line 40
#      38 num=int(input("Enter number"))
#      39 if num>10:
# ---> 40     raise ValueError("Number is High")
#      41 else:
#      42     print(num)

# ValueError: Number is High

# Reraising Exceptions: You can use the raise statement within an except block to re-raise an exception after handling it. This is useful when you want to catch an exception, perform some additional processing, and then propagate the exception to a higher level of the program.

# try:
#     # Some code that might raise an exception
#     result = 10 / 0
# except ZeroDivisionError:
#     # Handle the exception
#     print("Error: Division by zero occurred")
#     # Reraise the exception
#     raise
# In this example, the ZeroDivisionError exception is caught, and a message is printed. Then, the raise statement is used without specifying an exception type, which reraises the caught exception, propagating it to the next level of the program.

# When you raise an exception, you can provide an optional error message or additional information that helps identify the cause of the exception. This information is included as part of the exception object and can be accessed when handling the exception.

# Overall, the raise statement is a powerful tool in Python's exception handling mechanism, allowing you to effectively signal and handle errors in your code.





