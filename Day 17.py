# User define Function:
# Use "def" keyward.
# basic two parts in function: (1) Define and (2) Calling.
# Without Parameter passing:
# def xyz(): -> function defination
#     print("Hello Mayur")
# xyz() ->function calling
# o/p-> Hello Mayur
# With Parameter:
# def sum(a,b): function with parameter 
#     sum=a+b
#     return sum (return to function defination)
# sum(10,20) calling the function with argument
# Find factorial using Function:
# def facto(x):
#     fac=1
#     for i in range(1,n+1):
#         fac=fac*i
#     print(fac)
#     return facto
# n=int(input())
# facto(n)
# o/p-> 120
# Example of functions:
# def sum(num1, num2):
#     total = num1 + num2
#     z = 50
#     # print(total)
#     return total, z

# print(sum(10,20)) # None
# print(type(sum(10,20)[0]))
# print(sum(10,20)[0])
# o/p-> 
# (30, 50)
# <class 'int'>
# (30, 50)
# Nested Function:
# def outer():
#     def inner1():
#         return "inner1"
    
#     def inner2():
#         return "inner2"
    
#     return inner1,inner2

# print(outer()[0]()) Tuple indexing then call the inner function
# print(outer()[1]())
# o/p-> 
# inner1
# inner2
# Functions can also be designed to accept default parameter values, accept variable numbers of arguments, or return multiple values using tuples. 
# They are a fundamental concept in Python and are widely used for organizing code and promoting code reuse.

# Function define rules:
# In Python, functions are defined using the def keyword followed by the function name and parentheses containing any parameters the function takes. 
# The function body is then indented below the function definition. Here are the key rules for defining functions in Python:

# Function Definition: To define a function, use the def keyword followed by the function name and parentheses containing any parameters the function accepts.
# For example:

# def my_function(parameter1, parameter2):
#     # Function body
#     # Code goes here
# Function Name: The function name should be a valid identifier in Python. It should follow the same naming conventions as variables.

# Parameters: Parameters are the inputs that a function receives. They are declared inside the parentheses in the function definition. 
# If a function doesn't take any parameters, the parentheses are left empty. For example:

# def greet(name):
#     print("Hello, " + name + "!")
# Function Body: The function body consists of one or more statements that are executed when the function is called.
# It must be indented relative to the function definition. For example:

# def square(x):
#     return x * x
# Return Statement: Functions can return values using the return statement. This statement exits the function and optionally returns a value back to the caller. 
# For example:

# def add(a, b):
#     return a + b
# Function Call: To call a function, use the function name followed by parentheses containing any arguments (if required). For example:
# result = add(3, 5)
# Docstrings: It's a good practice to include a docstring (documentation string) at the beginning of the function body to describe what the function does. 
# This helps other programmers (and yourself) understand the purpose of the function. For example:

# def greet(name):
#     """Print a greeting message."""
#     print("Hello, " + name + "!")
# These are the fundamental rules for defining functions in Python. Understanding and following these rules will help you write clean, readable, and maintainable code.


