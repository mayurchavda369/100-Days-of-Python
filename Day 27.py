# Turnery operator in Python: shorthand of if else.
# there is no ternary operator in the traditional sense found in some other programming languages (e.g., C, Java).
# However, Python offers a ternary expression, which is a one-liner conditional expression often referred to as the "ternary operator" due to its similarity in behavior.
# The syntax for the ternary expression in Python is as follows:
# x if condition else y
# If condition evaluates to True, the expression returns x.
# If condition evaluates to False, the expression returns y.
# Syn: Value if True if Condition else Value if False.
# Ex:
# x = 5
# y = 10
# result = x if x > y else y
# print(result)  # Output: 10
# Ex : Max value
# x=int(input("Enter number one: "))
# y=int(input("Enter Number Two: "))
# Max= x if x>y else y
# print(Max)
# o/p-> input given is 11 and 23 so answer is 23 means y.
# Ex
# a = 330000
# b = 3303
# print("A") if a > b else print("=") if a == b else print("B")

# c = 9 if a>b else 0
# print(c)
# o/p-> A 9
# While Python's ternary expression syntax is concise and can be useful for simple conditional assignments,
#  it's important to maintain readability and clarity in your code. 

