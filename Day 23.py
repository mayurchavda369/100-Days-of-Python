# Exception Handling in Python :
# Its also called as Error handling.
# Try-Except block.
# Try: if you think you face error in code you can write that part in Try block.
# Except: executable code write in Except block.
# Code that might raise an exception is placed inside the try block, and code to handle the exception is placed inside the except block.
# If an exception occurs in the try block, Python searches for an appropriate except block to handle it.
# NOTE: Error Name must be write in Pascal Case. Ex: ZeroDivisionError,NameError.
# Ex 1:
# try:
#     # Code that might raise an exception
#     result = 10 / 0  # Division by zero
# except ZeroDivisionError:
#     # Code to handle the exception
#     print("Error: Division by zero occurred")
# NOTE : 0 is not divide with any number so it gives error so we write that code in try block.
# Generic Except block: you dont have to write any ERROR Name.
# Ex:2 
# try:
#     u=1
#     print(ok)
# except:
#     print("ok is not defined")
# # ok is not defined in try block so it gives output as except block.
# Multiple Except block: we face multiple error in program so we can use multiple except block.
# Ex:
# try:
#     # Code that might raise an exception
#     result = int("abc")  # ValueError
# except ValueError:
#     print("Error: Invalid value provided")
# except ZeroDivisionError:
#     print("Error: Division by zero occurred")
# # Here we give string as value so we face the value error.
# Else block: you can also write else with try-except block.
# You can use the else block to execute code if no exceptions occur in the try block.
# if no error in try block then else block execute.
# Ex:
# try:
#     # Code that might raise an exception
#     result = 10 / 2
# except ZeroDivisionError:
#     print("Error: Division by zero occurred")
# else:
#     print("Result:", result)
# o/p-> Result:5.0
# Ex: Multiple Errors program
# try:
#     num=int(input()) -> here we face ValueError
#     x=10//num -> ZeroDivisionError
#     list1=[]
#     for i in range(num):
#         list1.append(i)
#         print(list1[x]) ->IndexError
# except ValueError:
#     num=int(input("Please enter integer number"))
#     x=10//num
#     list2=[]
#     for i in range(num):
#         list2.append(i)
#         print(list2[x])
# except ZeroDivisionError:
#     num=int(input("Please dont write zero"))
#     x=10//num 
#     list2=[]
#     for i in range(num):
#         list2.append(i)
#         print(list2[x])
# except: 
#         # (by default)
#     print("ok")
# o/p->6


















