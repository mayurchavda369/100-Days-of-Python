# Match case in python :
# However, starting from Python 3.10, the language introduced the match statement as part of PEP 634. 
# The match statement allows for more flexible and readable pattern matching.
# Must use this in python version 3.10.
# its a substitute of if-elif-else.
# in c,c++,java has switch case statement its simillar like that.
# must use keyward "match" to perform this operation. for the default case use "_".
# NOTE: you can take as many as default case.
# ex:
# x=int(input())
# if we enter any number except then 5 so its go to default case.

# match x:

#     case 0:
#         print("its zero")
#     case 5:
#         print("its right")
#     case _: by default case
#         print("its default case ")   
# o/p-> its right (bcz we enter 5)
# ex: using Function 
# def check_value(value):
#     match value:
#         case 1:
#             print("Value is 1")
#         case 2:
#             print("Value is 2")
#         case _:
#             print("Value is something else")

# # Example usage
# check_value(2)
# # output: value is 2.
# ex: you can take as many as default cases.
# x = int(input("Enter the value of x: "))
# # x is the variable to match
# match x:
#     # if x is 0
#     case 0:
#         print("x is zero")
#     # case with if-condition
#     case 4:
#         print("case is 4")

#     case _ if x!=90:
#         print(x, "is not 90")
#     case _ if x!=80:
#         print(x, "is not 80")
#     case _:
#         print(x)



