# Looping in Python
# If you want to do some repeated task you can using loop.
# Three types of loop in python : (1) For (2) While. (3) Nested loop.
# For Loop : its use when you have sequence data like list set tuple. one by one get and you know condition.
# using in iterable datatypes like str + collection datatypes[list,set,tup,dict]
# While Loop : its use when you as much as then condition will be true. 
# Nested Loop : loop in loop thats we use this.
# For Loop examples:
# fruits = ["apple", "banana", "cherry"]
# for fruit in fruits:
#     print(fruit,end=' ')
# o/p : 
    # apple banana cherry
# how for work exactly?
# l = range(1, 6)
# l1 = iter(l)
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# print(next(l1))
# ex : 
    # for i in "good":
    #     print(i,end=" ")
# o/p= good 
# here i is variable in is operator and good is iterable.
# Range function : given range of the variable
# range(int,int,int)
# range(start,stop,step)
# range(start,stop) by default step is 1.
# range(stop) by default start is 0.
# stop is exclusive.
# ex: 
# for i in range (1,10,2):
#     print(i,end=" ")
# o/p=1 3 5 7 9 
# you can also give negative range.
# M.IMP : for loop stops when (1) loop is over and (2) loop is break.
# While loop stops when (1) condition is false and (2) loop is break.
# Printing example using Foor loop :

# for i in range (1,6):
#     print("*"*i)
# o/p =
# *
# **
# ***
# ****
# *****
# find factorial using for loop 
# n=5
# fac=1
# for i in range(1,n+1):
#     fac=fac * i
#     print(fac,end=" ")
# O/p= 1 2 6 24 120
# for pos in range(len(name)):
#     # print(name[pos])

#     if name[pos] == 't':
#         continue
#     elif pos == 3:
#         pass
#     elif pos == 4:
#         break
    
#     print(name[pos])

# print("hello")


# product = {
#     'tomato':20,
#     'potato':50,
#     'pen':54
# }

# print(product.items())

# for k, v in product.items():
#     print(k, v)

# nums = [(1,2,3), (2,3,4), (3,4,5)]

# for a,b,c in nums:
#     print(a,b,c)

# for a,b in nums:
#     print(a,b)
    
# While loop :
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# o/p= 
# 0
# 1
# 2
# 3
# 4
# while(1):
#     age = int(input("Enter your age : "))
#     if (age >= 18):
#         weight = int(input("Enter your weight : "))
#         if(weight >= 50):
#             print("You can donate")
#         else:
#             print("You can not donate")
#     else:
#         print("You can not donate")
# while (1) means condition is true.
# you have to use break statement to stop the loop.
# ex : find fibonacci series using while loop.
# n=10
# a=0
# b=1
# c=0
# while c<n:
#     print(a,end=" ")
#     sum=a+b
#     a=b
#     b=sum
#     c+=1
# o/p= 0 1 1 2 3 5 8 13 21 34 

# Nested loop : loops under loops
# example of nested loops:
num = 11

# for r in range(1, num):
#     for c in range(1, num):
#         print("*", end=" ")
# #     print("")

# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *
# * * * * * * * * * *


# for r in range(1, num):
#     for c in range(1, r+1):
#         print("*", end=" ")
#     print("")

# *
# * *
# * * *
# * * * *
# * * * * *
# * * * * * *
# * * * * * * *
# * * * * * * * *
# * * * * * * * * *
# * * * * * * * * * *


# for r in range(1, num):
#     for c in range(1, num-r):
#         print("*", end=" ")
#     print("")

# * * * * * * * * *
# * * * * * * * *
# * * * * * * *
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for r in range(1, num):
#     for c in range(1, r+1):
#         print(" ", end=" ")
#     for c in range(1, num-r):
#         print("*", end=" ")
#     print("")

#   * * * * * * * * *
#     * * * * * * * *
#       * * * * * * *
#         * * * * * *
#           * * * * *
#             * * * *
#               * * *
#                 * *
#                   *

# for r in range(1, num):
#     for c in range(1, num-r):
#         print(" ", end=" ")
#     for c in range(1, r+1):
#         print("*", end=" ")
#     print("")

#                   *
#                 * *
#               * * *
#             * * * *
#           * * * * *
#         * * * * * *
#       * * * * * * *
#     * * * * * * * *
#   * * * * * * * * *
# * * * * * * * * * *

# for r in range(1, num):
#     for c in range(1, num-r):
#         print(" ", end=" ")
#     for c in range(1, r+1):
#         print("*", end=" ")
#     for c in range(1, r):
#         print("*", end=" ")
#     print("")

#                   *
#                 * * *
#               * * * * *
#             * * * * * * *
#           * * * * * * * * *
#         * * * * * * * * * * *
#       * * * * * * * * * * * * *
#     * * * * * * * * * * * * * * *
#   * * * * * * * * * * * * * * * * *
# * * * * * * * * * * * * * * * * * * *

# use of Controll statements : Break,continue and Pass.
# Break : use for stop the loop. terminate the loop.
Example with break:
python
Copy code
# Using break to exit the loop when a condition is met
for number in range(10):
    if number == 5:
        print("Breaking the loop at number 5")
        break
    print(number)
Output:
0
1
2
3
4
Breaking the loop at number 5
Example with continue:

# Using continue to skip printing when a condition is met
for number in range(6):
    if number == 3:
        print("Skipping number 3")
        continue
    print(number)
Output:
0
1
2
Skipping number 3
4
5
Example with pass:

# Using pass as a placeholder when a condition is met
for number in range(4):
    if number == 2:
        print("Encountered number 2 but doing nothing with pass")
        pass
    else:
        print(number)
Output:
0
1
Encountered number 2 but doing nothing with pass
3
In these examples, break is used to exit the loop when a condition is met,
continue is used to skip the rest of the code inside the loop 
for a specific iteration, and 
pass is used as a placeholder when a condition is met but 
no specific action is needed.

    

    
    
