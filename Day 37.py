# zip,enumerate,eval,chr,ord,min,max,pow,round,slice,sum function in python :
# they all are built in function of python.
# This all method gives an object in the output so we convert into it.
# (1) zip(): combine parameter and arguments.
# The zip() function takes iterables (like lists) as input and returns an iterator that produces tuples where the i-th tuple contains the i-th element from each of the input iterables.
# Syntax: zip(iterable1, iterable2, ...)
# Ex:
# l1=[1,2,3]
# l2=["a","b","c"]
# l3=[4,5,6]
# x=list(zip(l1,l2,l3))
# print(x)
# o/p-> [(1, 'a', 4), (2, 'b', 5), (3, 'c', 6)]
# Ex : unziping list of tuples
# data = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
# names, ages = zip(*data)
# print(names)  # Output: ('Alice', 'Bob', 'Charlie')
# print(ages)   # Output: (30, 25, 35)
#(2) enumerate(): The enumerate() function adds a counter to an iterable and returns an enumerate object. Each element of the enumerate object is a tuple containing the index (starting from 0 by default) and the value from the iterable.
# Syntax: enumerate(iterable, start=0)
# Ex
# fruits = ['apple', 'banana', 'cherry']
# enumerated_fruits = enumerate(fruits, start=1)
# print(list(enumerated_fruits))  # Output: [(1, 'apple'), (2, 'banana'), (3, 'cherry')]
# (3) eval() : The eval() function parses and evaluates a Python expression represented as a string.
# Syntax: eval(expression, globals=None, locals=None)
# convert string number into int
# Ex:
# result = eval('3 + 4')
# print(result)  # Output: 7
# Ex:
# x="7+9*3"
# res=eval(x)
# print(res)
# o/p->34
# Ex
# x="mayur chavda"
# y=eval('x.capitalize()') you have to must convert methods into string.
# print(y)
# o/p->Mayur chavda
# chr() & ord() : 
# chr() : gives ascii character
# x=65
# y=chr(x)
# print(y) o/p-> A
# ord() : gives ascii number .
# x="m"
# y=ord(x)
# print(y)
# o/p-> 109
# min() : gives minimum value from the list,set,tuple or any values.
# x={1,2,3,4}
# y=min(x)
# print(y)
# o/p-> 1
# max() -> gives maximum value from the list,set,tuple or any values.
# x={1,2,3,4,5}
# y=max(x)
# print(y)
# o/p-> 5
# pow(): gives power of value.
# pow() function returns the value of x to the power of y.
# Syntax: pow(x, y)
# Example:
# result = pow(2, 3)
# print(result)  # Output: 8
# round():returns the floating point number rounded to the specified number of decimals.
# Syntax: round(number[, ndigits])
# Example:
# num = 3.14159
# rounded_num = round(num, 2)
# print(rounded_num)  # Output: 3.14
# slice():
# The slice() function creates a slice object representing the set of indices specified by start, stop, and step.
# Syntax: slice(start, stop, step)
# Example:
# s = slice(1, 5, 2)
# print(s)  # Output: slice(1, 5, 2)
# Using slice() Function:
# s = slice(1, 5, 2)
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# sliced_numbers = numbers[s]
# print(sliced_numbers)  # Output: [1, 3]
# Slicing Lists:
# numbers = [1, 2, 3, 4, 5]
# sliced_numbers = numbers[1:4]  # Get elements from index 1 to 3
# print(sliced_numbers)  # Output: [2, 3, 4]
# Slicing Strings:
# text = "Hello, World!"
# sliced_text = text[7:]  # Get elements from index 7 to the end
# print(sliced_text)  # Output: "World!"

# Slicing with Step:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sliced_numbers = numbers[::2]  # Get every second element
# print(sliced_numbers)  # Output: [1, 3, 5, 7, 9]

# Using Negative Indices:
# numbers = [1, 2, 3, 4, 5]
# sliced_numbers = numbers[-3:-1]  # Get elements from the third last to the second last
# print(sliced_numbers)  # Output: [3, 4]
# sum() function:
# The sum() function returns the sum of all elements in an iterable.
# Syntax: sum(iterable[, start])
# Example:
# numbers = [1, 2, 3, 4, 5]
# total = sum(numbers)
# print(total)  # Output: 15
# Ex:
# s={1,9,8,5}
# x=sum(s)
# print(x)
# o/p->23











