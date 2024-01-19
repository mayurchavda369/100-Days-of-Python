# String datatype.
# string is used in characters. 
# Strings are fundamental to Python programming and are extensively used for text processing, manipulation, and representation. 
# string are immutable, Ordered,indexing and slicing possible. Duplicate character allowed.
# basic string is like a="hello"
# # [A-Z,a-z, 0-9, special symbols[~!@#$%^&*() ]]

# Syntzx : 
# """
# str_name  = 'this is a string'
# str_name  = "this is a string"
# str_name  = """this is a string"""
# str_name  = '''this is a string'''

# escape sequence in string 
# Ex: 
# a="Hello\nworld"
# print(a)
# if you want to print esacpe character use rstring "r".
# ex:
# a=r "Hello\nworld"
# print(a) o/p-> Hello\nworld
# Concatenating in string : Strings can be concatenated using the + operator.
# ex : 
# a="Hello"
# b="God"
# c=a+b
# print(c) o/p=> Hello God 
# Immutablity : you cant add and update in string.
# a="Hello" 
# b="Go"
# print(a + b) HelloGo
# print(a) Hello
# Accessing & Slicing  in string : you can access character through indexing.
# Ex:
# text1="My name is mayur"
# t2=text1[2:7] if i want "name" then i do it with slicing
# print(t2) o/p-> name
# note : we access string but we cant make changes in string. we make new string to apply the changes.
# Ex:
# s1="Mayur chavda"
# for i in s1:
#     print(i,end=" ")
# Ex: using enumerate function
# s1="Mayur"
# for i in enumerate(s1):
#     print(i,end=" ")
# o/p= (0, 'M') (1, 'a') (2, 'y') (3, 'u') (4, 'r') 

# String Formating :
# fname = "Mayur"
# lname = 'Chavda'
# age = 27
# price = 369.23
# print(fname + " " + lname)
# print(f"your name is {fname + ' ' + lname}")
# print(f"your name is {fname} {lname}")
# print("your name is {} {}".format(fname, lname))
# print("your name is {0} {1}".format(fname, lname))
# print("your name is %s %s your age is %d: price is : %.2f" % (fname, lname, age, price))
# Output
# Mayur Chavda
# your name is Mayur Chavda
# your name is Mayur Chavda
# your name is Mayur Chavda
# your name is Mayur Chavda
# your name is Mayur Chavda your age is 27: price is : 369.23

# String Mehods:
# print(dir(str)) if you want to see methods of any datatypes use dir() function.
# dir( ) means directory.
# methods:
# ['__add__', '__class__', '__contains__', '__delattr__',
#  '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
# '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', 
# '__hash__', '__init__', '__init_subclass__', '__iter__', 
# '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', 
# '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 
# 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 
# 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 
# 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 
# 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 
# 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 
# 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
# 'splitlines', 'startswith', 'strip', 
# 'swapcase', 'title', 'translate', 'upper', 'zfill']
# str1="mayur chavda"
# find length use len() function 
# print(len(str1)) o/p-> 12 
# Capitalize Converts the first character of a string to uppercase.
# str2=str1.capitalize() 
# print(str2) o/p-> Mayur chavda
# Upper method converts all lower case into upper case.
# str2=str1.upper()
# print(str2) o/p-> MAYUR CHAVDA
# Lower method converts all upper case into lower case.
# t="MAYUR CHAVDA"
# s=t.lower()
# print(s) o/p-> mayur chavda
# title():Converts the first character of each word to uppercase.
# text = "hello, world!"
# title_text = text.title()
# print(title_text)
# # Output: Hello, World!
# replace():Replaces a substring with another substring in the string.
# text = "hello, world!"
# new_text = text.replace("hello", "hi")
# print(new_text)
# # Output: hi, world!
# startswith() and endswith():
# Checks if the string starts or ends with a specific substring.

# text = "hello, world!"
# starts_with_hello = text.startswith("hello")
# ends_with_world = text.endswith("world")
# print(starts_with_hello)  # Output: True
# print(ends_with_world)    # Output: False
# casefold() This make forcefully character in lower case.
# he casefold() method, however, is considered more aggressive in 
# handling different Unicode characters, making it 
# suitable for case-insensitive comparisons in a broader range of situations.
# text = "heLlo, WorLd!"
# s=text.casefold()
# print(s) o/p-> hello, world!
# Split() the string into a list of substrings based on a specified delimiter.
# text = "apple, banana, cherry"
# fruits = text.split(", ")
# print(fruits)
# Output: ['apple', 'banana', 'cherry']
# rsplit() right side split
# text="ok,get,go"
# x=text.rsplit(',')
# print(x) o/p-> ['ok', 'get', 'go']
# center(int,str) make center of given words. take one argument as int.
# text = "apple"
# s=text.center(10,"*")
# print(s)
# optional second arguments.
# rjust(int) make alignment on right side. take one argument.
# second arg is optional.
# text = "apple"
# s=text.rjust(9,"+")
# print(s) o/p->++++apple
# ljust(int) make alignment on left side.take one argument.
# second arg is optional.
# text = "apple"
# s=text.ljust(9,"+")
# print(s)  
# o/p->apple++++
# zfill(int) fill zero on the right side. take exact one argument.
# text = "apple"
# s=text.zfill(8)
# print(s) o/p= 000apple
# Find(str,start,stop) method used to find words in the string. give index number.it follows left to right.
# start,stop is optional
# text="My name is Mayur"
# res=text.find("name")
# print(res) o/p-> 3 
# text="My name is Mayur"
# res=text.find("i",1,12)
# print(res)  o/p-> 8
# index(str,start,stop) method give index number of string. case sensetive method must 
# give words upper or lower.# start,stop is optional. it follows left to right.
# ext="My name is Mayur"
# res=ext.index("m")
# print(res)  o/p-> 5
# text="My name is Mayur"
# res=text.find("a",1,12)
# print(res) o/p->4
# swapcase() convert upper to lower and lower words to upper.
# text="Hello bOys"
# x=text.swapcase()
# print(x) o/p-> hELLO BoYS
# join()-> seperator.join(iterable) The join method is particularly useful
#  when you need to concatenate a large number of strings efficiently
# It takes an iterable (such as a list, tuple, or string) as 
# its argument and joins the elements of the iterable with the string on which it is called.
# words = ["Hello", "World", "Python"]
# joined_string = " ".join(words)
# print(joined_string) o/p-> Hello World Python
# numbers = ["1", "2", "3", "4", "5"]
# csv_string = ",".join(numbers)
# print(csv_string) o/p-> 1,2,3,4,5
# expandtab(int) -> expand the string with 2,4,6 tab range. we have to give tab range.
# If you want to see the effect of expandtabs(), you can use a string with tab characters:
# if you dont give tabs range its contain by default 8.
# a = "ms\tdhoni"
# b = a.expandtabs(4)
# print(b) o/p-> ms  dhoni
# parttition(str) The partition method searches for the first occurrence of 
# the specified separator and splits the string into three parts. it gives tuple output.
# if words are not in string then it gives only (" "," ","str") output.left to right.

# string = "Python is fun!"
# result = string.partition(" is ")
# print(result)
# Output: ('Python', ' is ', 'fun!')
# rpartition(str) same as partition. it follows right to left.
# if words are not in string then it gives only (" "," ","str") output.
# string = "Python is fun! Python is versatile!"
# result = string.rpartition(" is ")
# print(result) o/p-> 'Python is fun! Python', ' is ', 'versatile!')
# strip() The strip method removes leading and trailing characters from a string.
#  By default, it removes whitespace characters (spaces, tabs, and newlines),
#  but you can also specify a custom set of characters to be removed.
# ex:
# string = "+++Hello, World!+++"
# custom = string.strip("+")
# print(custom) o/p-> Hello, World!
# by default it strip whitespaces.
# string = "   Hello, World!   "
# stripped_string = string.strip()
# print(stripped_string) o/p-> Hello, World!
# rstrip() follows right to left strip.
# string = "   Hello, World!   "
# right_stripped_string = string.rstrip()
# print(right_stripped_string) o/p->    Hello, World!
# splitness() The splitlines method in Python is a string method used to split a string into a list of lines. 
# It recognizes different newline characters such as '\n', '\r', or '\r\n', and 
# it handles them appropriately.
# This method does not include the newline characters in the resulting list.
# arguments are optional.
# ex:
# multi_line_string = "Line 1\nLine 2\r\nLine 3"
# lines = multi_line_string.splitlines()
# print(lines) o/p-> ['Line 1', 'Line 2', 'Line 3']  it neglet escape seq charcter.
# ex:
# multi_line_string = "Line 1\n hello\n Line 2\r\nLine 3"
# lines = multi_line_string.splitlines(2)
# print(lines) o/p-> ['Line 1\n', ' hello\n', ' Line 2\r\n', 'Line 3']
# # if you give arguments number more then 0 then cant ignore escape seq char.

# Note : this all methods give answer in boolean form (True or False)
# isalnum() check the string is alphanumeric (a-z and 1-100)
# *&@! character cant contain in alnum. so it will give output False.
# str="Mayur123"
# x=str.isalnum()
# print(x) o/p-> True
# isalpha() in string all characters are alphabets. (a-z or A-Z)
# str="Mayur"
# x=str.isalpha()
# print(x) o/p-> True
# isascii() ASCII characters include the English alphabet, digits, and various symbols.
#  keyboards all characters in the string so it will give True else False.
# str="Mayur$#@12"
# x=str.isascii()
# print(x) o/p-> True
# isidentifier() method is used to check if a given string is a valid identifier. 
# An identifier is a name given to entities like variables, functions, classes, etc. 
# The rules for a valid identifier in Python include:

# It must start with a letter (a-z, A-Z) or an underscore _.
# The remaining characters can be letters, digits (0-9), or underscores _.
# x="Hello1"
# s=x.isidentifier()
# print(s) o/p-> True
# isupper() in string all character are in uppercase so True else False.
# islower() in string all character are in lowercase so True else False.
# istitle() in string First character are in uppercase so True else False.
# isprintable() if charcter are show in terminal that type characters are printable so its True else False.
# Escape sequence charcter are not printable. so its always show False.\n,\,\b,\t.
# ex:
# x="Hello\nmayur"
# s=x.isprintable()
# print(s) o/p-> False
# isspace() in string check space if any space see it will give True else False.
# isdecimal()method returns True if all characters in a string are decimal characters (0-9), and False otherwise. 
# It does not consider other numeric characters.
# numeric_text = "12345"
# result = numeric_text.isdecimal()
# print(result)  # True
# isdigit() method returns True if all characters in a string are digits (0-9), and False otherwise.
#  It also returns True for superscript and subscript digits.

# digit_text = "12345"
# result = digit_text.isdigit()
# print(result)  # True
# isnumeric() method returns True if all characters in a string are numeric characters,
#  including digits, superscript, and subscript digits, and other numeric characters.
#  but 12.5 is not numeric because its contain "." as character.
# numeric_text = "12345"
# result = numeric_text.isnumeric()
# print(result)  # True
# x="12.56"
# s=x.isnumeric()
# # print(s) o/p-> False



























