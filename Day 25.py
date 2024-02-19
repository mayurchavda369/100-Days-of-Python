# Custom Exception in Exception Handling:you can create custom exceptions by defining new exception classes. 
# This allows you to create more specific exception types that can be raised and caught in your code. 
# Syntax: Class GoodError(Exception):
# GoodError->custom class (Exception)-> Any message
# Ex:
# class CustomError(Exception):
#     def __init__(self, message="An error occurred"):
#         self.message = message
#         super().__init__(self.message)

# # # Raise the custom exception
# # raise CustomError("This is a custom error message")
# # Ex: use try-except block.
# try:
#     # Code that might raise a custom exception
#     raise CustomError("This is a custom error message")
# except CustomError as e:
#     # Handle the custom exception
#     print("Custom error:", e.message)
# Custom exceptions are useful for signaling and handling specific error conditions in your code. They provide a way to encapsulate error logic and make your code more readable and maintainable.
# Assertion : if value is True then do nothing but if value is False the Assertion error is raised.
# he assert statement is used to test whether a given condition is true or false.
# It's primarily used for debugging purposes and to catch programming errors early in the development process. 
# When an assert statement is encountered, if the condition is true, the program continues execution as normal. However, if the condition is false, an AssertionError exception is raised, halting the program's execution.
# Syn: assert condition, error_message
# error_message is an optional argument that allows you to provide additional information about the assertion failure. 
# It's typically a string that describes the reason for the assertion failure.
# Ex:
# assert 67>100,"value is not proper"
# o/p-> AssertionError: value is not proper
# Ex
# x = 5
# assert x == 10, "x should be equal to 10"
# o/p-> AssertionError: x should be equal to 10

