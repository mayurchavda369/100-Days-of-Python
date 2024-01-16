# Data Structure :
# LIST,TUPLE,SET,DICTIONARY.
# Mutable datatypes : you can add remove and make any changes in datatypes. ex : list,set,Dict.
# Immutuable datatypes : you cant add remove and update means you cant make changes. ex: Tuple,string,int,float,bool.
# Mutable Data Types:
List:
Lists are ordered and mutable sequences.
You can add, remove, or modify elements in a list after its creation.

my_list = [1, 2, 3]
my_list.append(4)
my_list[1] = 5
Dictionary:

Dictionaries are mutable collections of key-value pairs.
You can add, remove, or modify key-value pairs in a dictionary.
my_dict={} that is also called dictionary.
my_dict = {'a': 1, 'b': 2}
my_dict['c'] = 3
del my_dict['a']
Set:

Sets are unordered and mutable collections of unique elements.
You can add or remove elements from a set.

my_set={1,} that is also called set.
my_set = {1, 2, 3}
my_set.add(4)
my_set.remove(2)
Immutable Data Types:
Tuple:

Tuples are ordered and immutable sequences.
Once a tuple is created, you cannot change its elements.

my_tuple = (1, 2, 3)
my_tuple=(1,) that is also called tuple.
String:

Strings are sequences of characters and are immutable.
You cannot modify the characters in a string directly.

my_string = "Hello"

Integer, Float, Boolean:
These are immutable numeric and boolean types.
Once assigned, their values cannot be changed.

my_int = 5
my_float = 3.14
my_bool = True
Immutable data types are safer to use in certain situations, such as when you want to ensure that the data remains unchanged. 
Mutable types, on the other hand, offer more flexibility for dynamic changes.