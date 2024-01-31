# Dictionary : s a mutable and unordered collection of key-value pairs. 
# Each key must be unique within a dictionary, and the keys are used to access their corresponding values.
# Dictionaries are created using curly braces {} and a colon : to separate keys and values.
# mutable,unordered,unindexing,no slicing possible,no duplicate values allowed.
# Use Cases:
# Dictionaries are widely used for representing structured data.
# They are efficient for fast lookups using keys.
# JSON data is often represented as dictionaries in Python.
# Create Dictionary:
# D1={"one":1,"two":2,"two":4} key value pair dict
# print(D1)
# o/p-> {'one': 1, 'two': 4} Duplicate key not allowed. give output latest duplicate key.
# d1={} Empty Dictionary.
# Accessing Values:
# Values in a dictionary are accessed using their corresponding keys.
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# print(my_dict['name'])  # Output: John
# print(my_dict['age'])   # Output: 25
# Modifying Values:
# Dictionaries are mutable, so you can add, modify, or remove key-value pairs.
# my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# my_dict['age']=36
# print(my_dict)
# o/p-> {'name': 'John', 'age': 36, 'city': 'New York'}
# del my_dict['city']
# print(my_dict)
# o/p-> {'name': 'John', 'age': 36}
# Nested Dictionary:
# Short example :
# d1={"emp1":{"name":"mayur"},"emp2": {"age": 29}}
# print("employee name : ",d1["emp1"]["name"])
# Multiple employees example:
# employees = {
#     'employee1': {
#         'name': 'Alice',
#         'age': 28,
#         'position': 'Software Engineer',
#         'projects': ['Project A', 'Project B']
#     },
#     'employee2': {
#         'name': 'Bob',
#         'age': 35,
#         'position': 'Data Scientist',
#         'projects': ['Project B', 'Project C']
#     },
#     'employee3': {
#         'name': 'Charlie',
#         'age': 32,
#         'position': 'UX Designer',
#         'projects': ['Project A', 'Project C']
#     }
# }

# # Accessing nested information
# print("Employee 1 Name:", employees['employee1']['name'])
# print("Employee 2 Projects:", employees['employee2']['projects'])
# # o/p-> Employee 1 Name: Alice
# # Employee 2 Projects: ['Project B', 'Project C']

# # Adding a new employee
# employees['employee4'] = {
#     'name': 'David',
#     'age': 29,
#     'position': 'QA Engineer',
#     'projects': ['Project A', 'Project C']
# }

# # Modifying information
# employees['employee3']['age'] = 33

# # Displaying the updated dictionary
# print("\nUpdated Employees Dictionary:")
# print(employees)
# # o/p->
# Updated Employees Dictionary:
# {'employee1': {'name': 'Alice', 'age': 28, 'position': 'Software Engineer', 'projects': ['Project A', 'Project B']}, 
#  'employee2': {'name': 'Bob', 'age': 35, 'position': 'Data Scientist', 'projects': ['Project B', 'Project C']}, 
#  'employee3': {'name': 'Charlie', 'age': 33, 'position': 'UX Designer', 'projects': ['Project A', 'Project C']}, 
#  'employee4': {'name': 'David', 'age': 29, 'position': 'QA Engineer', 'projects': ['Project A', 'Project C']}}

# Dictionary Methods:
# x=dir(dict)
# print(x)
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', 
#  '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', 
#  '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', 
#  '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__',
#   'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']

# clear() : clear the dictionary.
# d1={"name": "mayur","age":27}
# d1.clear()
# print(d1) o/p-> {} Empty dictionary.
# copy() : one dict to make another copy dict.
# d1={"name": "mayur","age":27}
# d2=d1.copy()
# print(d2)
# o/p-> {'name': 'mayur', 'age': 27}
# keys() Method:
# The keys() method returns a view of the dictionary's keys. give output in tuple.
# my_dict = {'name': 'Charlie', 'age': 28, 'city': 'Paris'}
# all_keys = my_dict.keys()
# print(all_keys)
# # Output: dict_keys(['name', 'age', 'city'])
# fromkeys() Method:
# The fromkeys(keys,deault_value) method creates a new dictionary with specified keys and a default value.
# NOTE : you have to make keys in LIST. so you can perform fromkeys method. otherwise it will give erroe.
# d1 = ['name', 'age', 'city'] in LIST you can write keys.
# default_value = 'N/A'
# new_dict = dict.fromkeys(d1, default_value)
# print(new_dict)
# # Output: {'name': 'N/A', 'age': 'N/A', 'city': 'N/A'}
# Ex
# d1 = ["name", "age", "mob"]
# x = "msd", 29, 9090
# d2 = dict.fromkeys(d1, x)
# print(d2)
# o/p-> {'name': ('msd', 29, 9090), 'age': ('msd', 29, 9090), 'mob': ('msd', 29, 9090)}
# values() Method:
# The values() method returns a view of the dictionary's values.
# my_dict = {'name': 'Henry', 'age': 22, 'city': 'Toronto'}
# all_values = my_dict.values()
# print(all_values)
# Output: dict_values(['Henry', 22, 'Toronto'])
# get() Method:
# The get(key_name) method retrieves the value for a given key. 
# If the key is not found, it returns a default value (or None if not specified).
# my_dict = {'name': 'Alice', 'age': 30}
# age = my_dict.get('age')
# print(age)
# Output: 30
# items() Method:
# The items() method returns a view of the dictionary's key-value pairs as tuples.
# my_dict = {'name': 'Bob', 'age': 25, 'city': 'London'}
# all_items = my_dict.items()
# print(all_items)
# Output: dict_items([('name', 'Bob'), ('age', 25), ('city', 'London')])
# update("key": value) Method:
# The update() method updates the dictionary with key-value pairs from another dictionary or iterable.
# dict1 = {'name': 'Grace', 'age': 40}
# dict2 = {'city': 'Sydney', 'gender': 'Female'}
# dict1.update(dict2)
# print(dict1)
# # Output: {'name': 'Grace', 'age': 40, 'city': 'Sydney', 'gender': 'Female'}
# Ex :
# dict1 = {'name': 'Grace', 'age': 40}
# dict1.update({"city":"surat"})
# # print(dict1)
# setdefault(key_name,default_value) : The setdefault() method returns the value for a given key. 
# If the key is not found, it inserts the key with a specified default value. it always add into end.
# is useful when you want to ensure that a key is present in the dictionary, 
# and if it's not, you can set a default value for that key.
# my_dict = {'name': 'Frank', 'city': 'Tokyo'}
# age = my_dict.setdefault('age', 35)
# print(age) Output: 35
# print(my_dict) {'name': 'Frank', 'city': 'Tokyo', 'age': 35}
# pop() Method:
# The pop(key_name) method removes the specified key and returns its corresponding value. 
# If the key is not found, it raises a KeyError or returns a default value if provided.
# my_dict = {'name': 'David', 'age': 32, 'city': 'Berlin'}
# removed_age = my_dict.pop('age')
# print(removed_age)
# # Output: 32
# popitem() Method:
# The popitem() method removes and returns the last key-value pair from the dictionary.
# my_dict = {'name': 'Eva', 'age': 27, 'city': 'New York'}
# removed_item = my_dict.popitem()
# print(removed_item)
# # Output: ('city', 'New York')
# NOTE : if you want to remove particular key or value use "pop" method or removed last item use method "popitem".

















