# TypeCasting In Python : 
# Basic Datatypes is int,str,float and bull.
# two types of Typecasting :  (1) Implicit. (2) Explicit
# (1) Implicit Type Conversion:
# Python automatically performs some type conversion during operations if 
# the types are compatible. 
# For example, in arithmetic operations between integers and floats, 
# the result is automatically converted to the more general type:

# Ex
# x = 10      # integer
# y = 5.5     # float

# result = x + y  # x is implicitly converted to float
# print(result)   # Output: 15.5
# 2. Explicit Type Conversion:
# You can explicitly convert variables from one type to another 
# using built-in functions like int(), float(), str(), etc.

# a. Integer to Float:

# integer_number = 42
# float_number = float(integer_number)
# print(float_number)
# # Output: 42.0
# b. Float to Integer:

# float_number = 3.14
# integer_number = int(float_number)
# print(integer_number)
# # Output: 3
# c. Integer to String:

# integer_number = 123
# string_number = str(integer_number)
# print(string_number)
# # Output: '123'
# d. String to Integer:

# string_number = "456"
# integer_number = int(string_number)
# print(integer_number)
# # Output: 456
# e. String to Float:

# string_float = "3.14"
# float_number = float(string_float)
# print(float_number)
# # Output: 3.14
# 3. Using bool() for Type Conversion:
# The bool() function can be used to convert other types to boolean values.

# number = 42
# boolean_value = bool(number)
# print(boolean_value)
# # Output: True
