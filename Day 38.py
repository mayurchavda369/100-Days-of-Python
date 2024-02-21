# Iterators and Generators in Python:
# NOTE: all iterators are generator but not all generators are iterators.
# (1) Iterators:
# iterator is an object which contains a countable number of values and it is used to iterate over iterable objects like list, tuples, sets, etc. 
# Iterators are implemented using a class and a local variable for iterating is not required here,
# It follows lazy evaluation where the evaluation of the expression will be on hold and stored in the memory until the item is called specifically which helps us to avoid repeated evaluation. 
# Iterators can be created using iterables (objects that implement the __iter__() method), but they can also be created manually by implementing the __iter__() and __next__() methods in a class.
# An iterator is an object that represents a stream of data. It implements two methods: __iter__() and __next__().

# Using an iterator-
# iter() keyword is used to create an iterator containing an iterable object.
# next() keyword is used to call the next element in the iterable object.
# After the iterable object is completed, to use them again reassign them to the same object.
# Ex
# iter_list = iter(['Hello', 'For', 'Mayur']) 
# print(next(iter_list)) 
# print(next(iter_list)) 
# print(next(iter_list)) 
# o/p-> 
# Hello
# For
# Mayur
# Ex
# class MyIterator:
#     def __init__(self):
#         self.data = [1, 2, 3]
#         self.index = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = self.data[self.index]
#         self.index += 1
#         return value
# x=MyIterator()
# print(x.__next__())
# print(x.__next__())
# print(x.__next__())
# o/p->
# 1
# 2
# 3

# Generators:
# It is another way of creating iterators in a simple way where it uses the keyword “yield” instead of returning it in a defined function. 
# Generators are implemented using a function. Just as iterators, generators also follow lazy evaluation. 
# Here, the yield function returns the data without affecting or exiting the function.
# It will return a sequence of data in an iterable format where we need to iterate over the sequence to use the data as they won’t store the entire sequence in the memory.
# Generators are a special type of iterator that can be created using generator functions or generator expressions.
# Generator functions are defined using the def keyword, but they use the yield keyword to return values one at a time. When a generator function is called, it returns a generator object, which is an iterator.
# Generator expressions are similar to list comprehensions, but they use parentheses instead of square brackets. They produce values lazily, on-demand, as they are requested.
# Generators are memory efficient because they don't store all values in memory at once. Instead, they generate values on-the-fly and only keep track of the current state.
# Generators are often used to generate sequences of values that are too large to fit into memory, or to process data in a pipeline fashion.
# Ex
# def my_generator():
#     data = [1, 2, 3]
#     for item in data:
#         yield item
# gen=my_generator()
# # print(next(gen))
# # print(next(gen))
# # print(next(gen))
# # or
# for i in gen:
#     print(i)
# o/p-> 
# 1
# 2
# 3
# Ex:
# def sq_numbers(n): 
# 	for i in range(1, n+1): 
# 		yield i*i 
# a = sq_numbers(3) 

# print("The square of numbers 1,2,3 are : ") 
# print(next(a)) 
# print(next(a)) 
# print(next(a)) 
# o/p->
# The square of numbers 1,2,3 are : 
# 1
# 4
# 9
# NOTE:
# iterators and generators are both used to work with sequences of data, but generators provide a more concise and memory-efficient way to generate values lazily.







