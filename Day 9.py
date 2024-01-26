# List :ist is a versatile and commonly used data structure that represents an ordered collection of items.
#  Lists are mutable, which means you can change their contents by adding, removing, or modifying elements.
#  Lists are created using square brackets [ ] and can contain elements of different data types.
# empty list [].
# Mutuable,ordered,indexed,slicing possible,allow Duplicate elements.
# Any type of data can store in list.
# Create a List:
# ex:
# l1=[1,"ram",3.6,True]
# print(type(l1)) o/p-> <class 'list'>
# Accessing List : through indexing you can access the elements of list.
# l1=[1,2,3,True]
# x=l1[0]
# print(x) o/p-> 1
# minus indexing is also applicable on this.
# Slicing in List : 
# my_list = [1, 2, 3, 'apple', 'banana', True]
# x=my_list[2:5]
# print(x) o/p-> [3, 'apple', 'banana']
# Modifying in List :
# my_list = [1, 2, 3, 'apple', 'banana', True]
# my_list[2]="Mayur"
# print(my_list) o/p-> [1, 2, 'Mayur', 'apple', 'banana', True]
# List Operations: you can perform +,* operator for concatenation and repeating program.
# concating:
# l1=[1,2,3,"ok"]
# l2=[7,8,"lol"]
# l3=l1+l2
# print(l3) o/p-> [1, 2, 3, 'ok', 7, 8, 'lol'] 
# repeating :
# l1=[1,2,3,"ok"]
# l2=l1*2
# print(l2) o/p-> [1, 2, 3, 'ok', 1, 2, 3, 'ok']
# Nested Lists:
# Lists can contain other lists, forming nested structures.
# nested_list = [1, [2, 3], ['apple', 'banana']]
# List Comprehension : are a concise and expressive way to create lists in Python. 
# They allow you to generate a new list by specifying the elements you want to include based on an existing iterable (such as a list, tuple, or range) and applying an expression to each element
# Syntax: list = [expression for item in iterable if condition]
# expression: The operation to be performed on each item.
# item: The variable representing each element in the iterable.
# iterable: The existing iterable (e.g., a list or range).
# condition (optional): An optional condition that filters elements.
# Ex: Squring Names
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = [x**2 for x in numbers]
# print(squared_numbers)
# Output: [1, 4, 9, 16, 25]
# Ex: Filtering Even Numbers
# numbers = [1, 2, 3, 4, 5]
# even_numbers = [x for x in numbers if x % 2 == 0]
# print(even_numbers)
# # Output: [2, 4]
# Ex: Creating a list of pairs
# names = ['Alice', 'Bob', 'Charlie']
# pairs = [(name, len(name)) for name in names]
# print(pairs)
# Output: [('Alice', 5), ('Bob', 3), ('Charlie', 7)]
# Ex: Using a condition
# numbers = [1, 2, 3, 4, 5]
# squared_evens = [x**2 for x in numbers if x % 2 == 0]
# print(squared_evens)
# Output: [4, 16]
# Methods in List :
# len() : find length of list.
# l1=[1,2,3,4]
# print(len(l1))
# o/p=4
# print(dir(list))
# ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__','__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 
# 'pop', 'remove', 'reverse', 'sort']
# Append(arg) : use to add the element. but it add ends on the list. inline change.
# Ex:
# l1=[1,2,3,"ram"]
# l1.append("sita")
# print(l1) o/p-> [1, 2, 3, 'ram', 'sita']
# Extend(arg) add elents as well add multiple elemts in list. inline change.
# you can also add one list to another list. without using concatenation.
# l1=[1,7,"ok"]
# l2=["lol",9]
# l1.extend(l2)
# print(l1) o/p-> [1, 2, 3, 'ram', 'sita']
# l1=[1,7,"ok"]
# l1.extend("mayur")
# print(l1)
# o/p-> [1, 7, 'ok', 'm', 'a', 'y', 'u', 'r'] it can add one by one elements.
# clear() use to clear the list.
# l1=[1,2,"ok"]
# l1.clear()
# print(l1) o/p-> []
# copy() make copy of one list.
# l1=[1,2,"ok"]
# l2=l1.copy()
# print(l2) o/p-> [1, 2, 'ok']
# Count(element) -> count the element of list.
# l1=[1,2,"ok",3,"go","ok"]
# x=l1.count("ok")
# print(x) o/p-> 2 
# if element is not exist its give output as 0.
# index(element) give index position. follows left to right rule. if element does not exist it gives value error.
# l1=[1,2,"ok",3,"go","ok"]
# x=l1.index("ok")
# print(x) o/p-> 2
# insert(index number,element) it add new element to particular index number.
# l1 = ["hello", 8, "nice", 6]
# l1.insert(2, "mayur")
# print(l1) o/p-> ['hello', 8, 'mayur', 'nice', 6]
# pop(index number) delete last element. also display which element is deleted.
# l1 = ["hello", 8, "nice", 6]
# l1.pop(2) o/p-> 'nice'
# print(l1) o/p-> ['hello', 8, 6]
# remove(element) remove the element. does not show which element removed. Follow left to right rule.
# l1 = ["hello", 8, "nice", 6]
# l1.remove("hello")
# print(l1) o/p-> [8, 'nice', 6]
# reverse() it returns a list in reverse order. ascending to descending.
# l1 = ["hello", 8, "nice", 6]
# l1.reverse()
# print(l1) o/p-> [6, 'nice', 8, 'hello']
# sort() sorting the list. By default Asc to Dsc. 
# its not support "int" or "str" you have to make list only int or str. otherwise it gives error.
# l1 = [1,21,8,6]
# l1.sort()
# print(l1) o/p-> [1, 6, 8, 21]
# Ex: Follow a-z rule
# l1=["mayur","bhumi","lokesh","did"]
# l1.sort()
# print(l1) o/p-> ['bhumi', 'did', 'lokesh', 'mayur']
# if you put one upper letter then it consider first.
# l1=["mayur","bhumi","Lokesh","did"]
# l1.sort()
# print(l1) o/p-> ['Lokesh', 'bhumi', 'did', 'mayur']
# if you want DSC to ASC order so you have to write sort(reverse=True).
# ex:
# l1 = [1,21,8,6]
# l1.sort(reverse=True)
# print(l1) o/p-> [21, 8, 6, 1]





























