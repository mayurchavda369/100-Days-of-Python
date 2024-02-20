# map(),filter(),reduce() function in Python :
# all are higher order function means he need one function to perform task.
# all are works with iterable.
# most of use lambda function in them.
# (1) map function: each element same function apply.
# syntax: map(function,iterable)
# map() function applies a given function to each item of an iterable (e.g., a list) and returns a new iterable containing the results.
# ex:
# numbers = [1, 2, 3, 4, 5]
# squared = map(lambda x: x**2, numbers)
# print(list(squared))  
# Output: [1, 4, 9, 16, 25]
# ex : you can also write with "def" function
# def squre(x):
#     return x*x
# l1=[4,8,9]
# squred=list(map(squre,l1))
# print(squred)
# o/p-> [16, 64, 81]
# Ex : make the int into string
# i=[1,2,3,4]
# x=list(map(str,i))
# print(x)
# o/p-> ['1', '2', '3', '4']
# s = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# x = list(map(sum, s))
# print(x)
# o/p-> [6, 15, 24]
# (2) Filter function: same as map but it works only specific function.
# The filter() function constructs an iterator from elements of an iterable for which a given function returns True.
# Syntax: filter(function, iterable)
# Ex
# numbers = [1, 2, 3, 4, 5]
# evens = filter(lambda x: x % 2 == 0, numbers)
# print(list(evens))  # Output: [2, 4]
# Ex:
# l=[1.2,9.8,8.8,7.5,2,3,4]
# f=list(filter(lambda y: type(y)==float,l))
# print(f)
# o/p-> [1.2, 9.8, 8.8, 7.5]
# reduce function :  you have to import functools module
# The reduce() function applies a rolling computation to sequential pairs of values from an iterable, ultimately reducing them to a single value.
# Before Python 3, reduce() was a built-in function, but in Python 3, it was moved to the functools module.
# Syntax: reduce(function, iterable[, initializer])

# ex:
# from functools import reduce
# numbers = [1, 2, 3, 4, 5]
# total = reduce(lambda x, y: x + y, numbers)
# print(total)  # Output: 15

# Ex:
# from functools import reduce
# words = ["Hello", "World", "!"]
# joined_string = reduce(lambda x, y: x + " " + y, words)
# print(joined_string)  # Output: "Hello World !"
# Ex: Finding the Maximum Value in a List
# from functools import reduce
# x=[11,2,33,4,55]
# m=reduce(lambda f,y:f if f>y else y,x)
# print(m)
# o/p->55
















