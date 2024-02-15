# Recursion function in python: Function calling him self.
# Recursion in Python refers to the process in which a function calls itself directly 
# or indirectly to solve a problem. 
# is a powerful programming technique that allows solving complex problems by breaking them down into smaller, more manageable subproblems.
# in function defination function calling himself.
# Ex : factorial using recursion
# def fact(n):
#     if (n==0) or (n==1):
#         return 1
#     else:
#         return n * fact(n-1) function calling himself in the function defination.

# fact(5)
# o/p-> 120
# PROCESS OF RECURSION :
# fact(5) is like 5*fact(5-1) is 5 * fact(4)= 5 * 4*3*2*1 = 120 is answer.
# Ex 2: The fibonacci() function takes an integer n as input and returns the nth Fibonacci number.
# The base cases are when n is 0 or 1, in which case the function returns n.
# For n greater than 1, the function recursively calls itself with n-1 and n-2,
#  and returns the sum of the results.
# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# # Test the function
# for i in range(11):
#     print(fibonacci(i))
# fibonacci(10)
# o/p->
#  55 
#  55
# Process : f0=0 f1=1 ex: 5 of fibonacci is = 0 1 1 2 3 like 0+1+1+2+3
