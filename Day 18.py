# Diffrent Arguments in Python:
# (1) Positional Arguments : Position oriented (1,2)
# (2) Keyword Arguments : Keyword oriented like i=1,j=2.
# (3) Arbitary Arguments : *args -> parameter < Argument o/p-> Tuple
# (4) Arbitary Keyword Arguments : **kwargs -> Parameter < keyword Argument o/p-> Dictinary.
# (5) Default Arguments: giving diffrent value. Argument < parameter.

# (1) Positional Arguments: These are arguments passed to a function in the order they are defined. 
# The function receives them in the same order. 

# Ex 1:
# def greet(name, message):
#     print(f"{message}, {name}!")
# greet("Alice", "Hello")  
# # Positional arguments: "Alice" and "Hello"

# # Ex 2:
# def fun1(a,b,c):
#     return b
# fun1(1,2,3)
# # o/p-> 2
# (2) Keyword Arguments: These are arguments preceded by an identifier (keyword) and an equal sign (=). 
# The function receives them as keyword arguments, and their order doesn't matter.
# Ex 1: 
# def greet(name, message):
#     print(f"{message}, {name}!")

# greet(message="Hello", name="Alice")  
# # Keyword arguments: "name" and "message"
# Ex 2:
# def fun1(a,b,c):
#     return c
# fun1(a=1,b=2,c=3)
# # o/p-> 3
# (3)Default Arguments: These are arguments that have default values specified in the function definition. 
# If the caller doesn't provide a value for these arguments, the default value is used.
# Note: it always reserved one value. Less arguments then parameter.

# Ex 1:
# def greet(name, message="Hello"):
#     print(f"{message}, {name}!")
# greet("Alice") 
 # Default argument for "message" is used
# Ex 2:
# def fun1(a,b,t=0,j=90):
#     return t
# fun1(44,55,77)
# o/p-> 77 t is 77. parameter > arguments
# (4) Variable length Arguments:Functions can accept a variable number of arguments using two special symbols:

# *args (Non-keyword Variable-length Arguments): This allows the function to accept any number of positional arguments as a tuple.
# **kwargs (Keyword Variable-length Arguments): This allows the function to accept any number of keyword arguments as a dictionary.

# (i) *args: parameter < arguments . Take the rest of positional Arguments in a Tuple.
# it gives output in tuple.
# NOTE: its write wit "*" args its optional. you can write any name with **. Ex: *xyz
# def fun1(e,*args):
#     return args
# fun1(1,2,3,4,5)
# o/p-> (2, 3, 4, 5) in this e=1.
# (ii) **kwargs: parameter < Keyward Arguments (i=0,a=1..etc)
# # rest of kwyward argument in a dictionary. (key-value pair)
# NOTE: its write wit "**" kwargs its optional. you can write any name with **.Ex: **hero
# def fun1(x,**mayur):
#     return mayur
# fun1(1,j=8,k=9)
# o/p-> {'j': 8, 'k': 9}
# Mix example of *args and **kwargs :
# def print_info(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# print_info(1, 2, 3, name="Alice", age=30)
# o/p-> Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}

# (5) Unpacking Arguments: You can unpack a list or tuple and pass its elements as separate arguments to a function using the * operator. 
# Similarly, you can unpack a dictionary and pass its key-value pairs as keyword arguments using the ** operator. 

# Ex: 
# def greet(name, message):
#     print(f"{message}, {name}!")

# args = ("Alice", "Hello")
# kwargs = {"message": "Hello", "name": "Alice"}
# greet(*args)       # Unpacking positional arguments
# greet(**kwargs)   # Unpacking keyword arguments
# o/p->
# Hello, Alice!
# Hello, Alice!






