# Tuple : is a collection of ordered and immutable elements. 
# ordered,indexed,slicing possible,Immutable,allow duplicate values.
# you cant add or remove from the original tuple.
# tuple show it with () bracket.
# (1) its not tuple.
# (1,) this is tuple.
# Use Cases:
# Tuples are often used to represent fixed collections of items.
# They can be used as keys in dictionaries due to their immutability.
# Tuples are commonly used in functions to return multiple values.

# create tuple:
# t1=(1,2,0.9,True,"mayur")
# print(t1)
# o/p->(1, 2, 0.9, True, 'mayur')
# support all type value as well as aloow duplicate value.
# Accessing Tuple: you can accessing tuple throw indexing.
# t1=(1,2,0.9,True,"mayur")
# t2=t1[2]
# print(t2) o/p-> 0.9
# Slicing Tuples:
# Just like lists, you can use slicing to extract sub-tuples from a tuple.
# t1=(1,2,0.9,True,"mayur","ho")
# t2=t1[:5:1]
# print(t2)
# o/p-> (1, 2, 0.9, True, 'mayur')
# Immutable Nature:
# Tuples are immutable, meaning you cannot change their elements or size after creation.


# my_tuple[0] = 100  # This will raise an error 
# (TypeError: 'tuple' object does not support item assignment)
# Tuple Methods:
# Tuples have a few methods, but they are limited compared to lists due to their immutability.
# count_2 = my_tuple.count(2)  # Count occurrences of the element 2
# index_apple = my_tuple.index('apple')  # Get the index of the first occurrence of 'apple'
# Tuple Packing and Unpacking:
# Tuple packing is the process of putting values into a tuple, 
# and tuple unpacking is extracting values from a tuple.

# Tuple Packing:
# Tuple packing is the process of creating a tuple by assigning values to it. 
# The values are automatically packed into a tuple.

# Tuple packing
# packed_tuple = 1, 'two', 3.0
# print(packed_tuple)
# # Output: (1, 'two', 3.0)
# In this example, the values 1, 'two', and 3.0 are automatically packed into a tuple named packed_tuple. 
# This is a convenient way to create tuples without explicitly using parentheses.

# Tuple Unpacking:
# Tuple unpacking is the process of extracting values from a tuple and assigning them to variables.

# # Tuple unpacking
# a, b, c = packed_tuple
# print(a, b, c)
# # Output: 1 two 3.0
# In this example, the values from the packed_tuple are unpacked and assigned to variables a, b, and c. 
# The order of assignment is based on the order of elements in the tuple.

# Using Tuple Packing and Unpacking in Functions:
# Tuple packing and unpacking are often used in functions to return multiple values.


# # Function returning multiple values as a tuple
# def get_coordinates():
#     x = 10
#     y = 20
#     z = 30
#     return x, y, z

# # Tuple unpacking when calling the function
# x_coord, y_coord, z_coord = get_coordinates()
# print(x_coord, y_coord, z_coord)
# # Output: 10 20 30
