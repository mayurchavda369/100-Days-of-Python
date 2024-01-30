# Set : is an unordered and mutable collection of unique elements. 
# Sets are defined using curly braces {} or by using the set() constructor.
# Sets do not allow duplicate elements, 
# and the order of elements is not guaranteed.
# gives random values as output.
# Use cases:
#Sets are useful for scenarios where you need to work with unique and unordered collections of elements. 
# They are commonly used for membership testing, removing duplicates,
#and performing set operations like union and intersection.
# create a set : 
# single set: set1=set()
# values with set: set1={1,2,3}
# ex:
# s1={1,3,4,4,5,9,"nice",True,0.9} all type value accepted
# print(s1)
# o/p-> {0.9, 1, 'nice', 3, 4, 5, 9} Dont print duplicate value.
# Note : here 1 consider as True. bcz 1 is True and 0 is False.
# set with loop:
# x={1,9,8,7,"mayur",False}
# for i in x:
#     print(i,end=" ") give random output.
# o/p-> False 1 7 8 9 mayur 
# Set Methods : 
# x=dir(set)
# print(x)
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', 
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', 
#  '__gt__', '__hash__', '__iand__', '__init__', '__init_subclass__', '__ior__', 
#  '__isub__', '__iter__', '__ixor__', '__le__', '__len__', '__lt__', '__ne__',
#    '__new__', '__or__', '__rand__', '__reduce__', '__reduce_ex__', '__repr__', 
#    '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__', '__str__',
#      '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
#        'difference_update', 'discard', 'intersection', 'intersection_update', 
#        'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 
#  'symmetric_difference', 'symmetric_difference_update', 'union', 'update']
# Add(element) : you can add element in sets. but it adds end of the set.
# x={1,2,3,"milli"}
# x.add("mayur")
# print(x) o/p-> {1, 2, 3, 'milli', 'mayur'}
# Clear() clear the set.
# x={1,2,"lol"}
# x.clear()
# print(x)
# o/p-> set() means empty set.
# Copy() copy one set to another set.
# x={3,4,5,"popo"}
# y=x.copy()
# print(y)
# o/p-> {'popo', 3, 4, 5} copy of x.
# Update(set_name or elements) one set to add many elements or add another set.
# x={1,2,3,"ko"}
# y={"mike","mayur",9}
# x.update(y)
# print(x)
# o/p-> {1, 2, 3, 'ko', 'mike', 9, 'mayur'} set x update throw set y.
# x={1,2,3,"ko"}
# x.update({9,"lol"})
# print(x)
# o/p-> {1, 2, 3, 'ko', 'lol', 9} set x update throw elements.
# pop() its randomly remove any element. if set is empty it will raise Key error.
# x={1,11,2,3}
# x.pop()
# print(x)
# o/p->{1,2,3}
# Remove(element) removes particular element. if element is not exist it will raise Key Error.
# x={1,3,4,5}
# x.remove(8)
# print(x)
# o/p-> {1, 3, 5}
# Discard(element) removes a specified element from the set. 
# If the element is not present, it does nothing without raising an error.
# my_set = {1, 2, 3, 4}
# my_set.discard(3)
# print(my_set)
# # Output: {1, 2, 4}
# Note : below all methods perform with two sets.
# union(set_name) : returns a new set containing all unique elements from both sets.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# union_set = set1.union(set2)
# print(union_set)
# Output: {1, 2, 3, 4, 5}
# diffrence(set_name) returns a new set containing elements that are present in the first set but not in the second set. 
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# difference_set = set1.difference(set2)
# print(difference_set)
# Output: {1, 2}
# symmetric_difference(set_name) method returns a new set containing elements that are present in either of the sets, but not in both.
# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5}
# symmetric_difference_set = set1.symmetric_difference(set2)
# print(symmetric_difference_set)
# # Output: {1, 2, 5}

# difference_update(set_name) : method in a set is used to remove all elements of another set from the current set. 
# This method modifies the set in place, updating it with the result of the difference operation.
# It's important to note that difference_update modifies the set it is called on and does not create a new set.
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# set1.difference_update(set2)
# print(set1)
# intersection(set_name) : The intersection method returns a new set containing common elements from both sets.
# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# intersection_set = set1.intersection(set2)
# print(intersection_set)
# Output: {3}
# intersection_update(set_name) : method in a set is used to update the set with the intersection of itself and another iterable (such as a set or any other iterable).
#  This method modifies the set in place.
# intersection_update modifies the set it is called on and does not create a new set.
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# # Update set1 with the intersection of set1 and set2
# set1.intersection_update(set2)
# print(set1)
# o/p-> {3,4,5}
# Note : Below all methods give output in boolean value. as True or False. need two sets to perform operation.
# These methods are useful for checking relationships between sets and are commonly used in various scenarios,
#  such as checking for common elements, verifying if one set is a subset or superset of another, 
# and determining if sets have any common elements.
# 'isdisjoint', 'issubset', 'issuperset',
# isdisjoint(set_name) : method checks whether two sets are disjoint, meaning they have no common elements.
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}

# result = set1.isdisjoint(set2)
# print(result)
# # Output: True (Sets are disjoint; no common elements)
# In this example, isdisjoint() returns True because set1 and set2 have no common elements.

# issubset() Method:
# The issubset() method checks whether one set is a subset of another set.
# set1 = {1, 2, 3, 4}
# set2 = {2, 3}

# result = set2.issubset(set1)

# print(result)
# # Output: True (set2 is a subset of set1)
# In this example, issubset() returns True because all elements of set2 are also present in set1.

# issuperset() Method:
# The issuperset() method checks whether one set is a superset of another set.
# set1 = {1, 2, 3, 4}
# set2 = {2, 3}

# result = set1.issuperset(set2)

# print(result)
# # Output: True (set1 is a superset of set2)
# In this example, issuperset() returns True because all elements of set2 are contained in set1.
# 











