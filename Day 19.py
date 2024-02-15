# Lambda function: 
# a lambda function is a small anonymous function that can have any number of arguments but only one expression. 
# Lambda functions are often used as a shortcut for defining simple functions without the need to formally define a function using the def keyword.
# Syntax: lambda arguments: expression
# Ex:
# Here's a simple example of a lambda function that calculates the square of a number:

# square = lambda x: x * x
# In this example:

# lambda is the keyword for defining a lambda function.
# x is the argument.
# x * x is the expression that calculates the square of x.

# You can call this lambda function like a regular function:
# result = square(5)
# print(result) 
# Output will be 25
# Lambda functions are often used in situations where a small anonymous function is needed for a short period of time, such as in combination with functions like map(), filter(), and reduce(), or as arguments to higher-order functions. However, lambda functions are limited in complexity compared to named functions defined using def, as they can only contain a single expression.
# Ex 2:
# sum= lambda a,b:a+b
# r=sum(10,20)
# print(r)
# NOTE : you can lambda function store in any variable then you able to print.