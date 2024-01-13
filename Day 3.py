# Variable,keywards and Operators :
# variable is like container who store the data types and his value.
# Ex:
a=20
print(type(a))
# output is <class 'int'>
# so basically datatype is int and value is 20.
# Rules of Variable:
# (1) First character can be "_" or Alphabets (UPPER or lower)
# (2) can not take numbers first ex: 123A. you write like Ax23="hello".
# (3) You can not take any python keyword as variable.
# PYTHON KEYWORDS : total 35 keywards
# False, None, True, and, as, assert, async, await, break, class, continue,
# def, del, elif, else, except, False, finally, for, from, global, if, import,
# in, is, lambda, nonlocal, None, not, or, pass, raise, return, True, try, 
# while, with, yield

#Ex :
a=b=c=d=100
print(b)
# output=100
# Ex:
var1,var3,var5=20,11,23
print(var3)
# output=11
# Python Operators:
# Operators: who perform some works.
# operands: on whom the task is being performed.
# types of operators:
# (1) Arithmatic (2)Assignment (3)Comparision (4)logical (5)Membership
# (6) Identity (7) Bitwise.
Arithmetic Operators:

+ (Addition)
- (Subtraction)
* (Multiplication)
/ (Division)
% (Modulus)
// (Floor Division)
** (Exponentiation)

Comparison Operators:

== (Equal)
!= (Not Equal)
< (Less Than)
> (Greater Than)
<= (Less Than or Equal To)
>= (Greater Than or Equal To)

Logical Operators:

and (Logical AND)
or (Logical OR)
not (Logical NOT)

Bitwise Operators:

& (Bitwise AND)
| (Bitwise OR)
^ (Bitwise XOR)
~ (Bitwise NOT)
<< (Left Shift)
>> (Right Shift)

Assignment Operators:

= (Assignment)
+=, -=, *=, /=, %=, //=, **= (Compound Assignment)

Membership Operators:

in (True if value is found in the sequence)
not in (True if value is not found in the sequence)

Identity Operators:

is (True if both variables are the same object)
is not (True if both variables are not the same object)

# NOTE : = check both side value and 
# is check bothside id.
# Arithmetic operators [+,-,*,/,%,//,**]
# print(1/7)
# x = 2
# p = 4
# print(x ** p)


# Assignment operators [+=,-=,*=,/=,%=,//=,**=,<<=,>>=]
# x = 10

# x = x + 20
# x += 20
# print(x)


# Comparison operators [=,==,!=, <, >, <=, >=]
# x = 10
# y = 10
# z = x == y
# z = x != y
# z = x < y
# z = x > y
# z = x >= y
# z = x <= y
# print(z)

# Logical operators [and, or, not]

# A B C
# T T T T T
# T F F T F
# F T F T F
# F F F F F

# z = (10 > 20)
# # print(not z) # False
# print(not z) # True


# Identity operators [ is, is not]
# x = 10
# y = 10
# print(y is x)
# print(y is not x)


# Membership operators [ in, not in]
# name = "python"
# print('p' in name)
# print('py' in name)
# print('Py' in name)
# print('pth' not in name)


# Bitwise operators [&, |, ^]
# AB&|^
# 00000
# 01011
# 10011
# 11110

# <<, >>
