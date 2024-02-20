# Readline(),Readlines(),seek(),tell(),writable(),readable() functions in File handling:
# (1) readline():
# This method reads a single line from the file.
# If the end of the file (EOF) is reached, it returns an empty string.
# Syntax: line = file.readline()
# Ex:
# with open("mytxt.txt","r") as f:
    # x=f.readline()
    # print(x)
# o/p-> hello mayur
# (2) readlines(): 
# This method reads all lines from the file and returns them as a list.
# Each element in the list corresponds to a line from the file.
# Syntax: lines = file.readlines()
# it gives output in list format.
# # Ex:
# with open("mytxt.txt","r") as f:
#     x=f.readlines()
#     print(x)
# o/p-> ['hello mayur \n', ' python is great\n', ' python is great']
# (3) seek(offset, whence):
# change the location of cursor.
# This method changes the file's current position (file pointer).
# offset specifies the number of bytes to move the pointer.
# whence determines the reference point for the offset:
# 0 (default): Start of the file
# 1: Current position
# 2: End of the file
# Syntax: file.seek(offset, whence)
# with open("mytxt.txt","r") as f:
#     f.seek(10)
# (4) tell()-> return location of cursor
# Syntax: position = file.tell()
# with open("mytxt.txt","r") as f:
#     x=f.tell()
#     print(x)
# o/p-> 0
# (5) writable():
# This method checks if the file is writable.
# It returns True if the file was opened in a writable mode ("w", "w+", "a", "a+"), otherwise False.
# Syntax: is_writable = file.writable()
# with open("mytxt.txt","w") as f:
#     x=f.writable()
#     print(x)
# o/p-> True
# (6) readable():
# This method checks if the file is readable.
# if the file is open in a mode that allows reading ("r", "r+", "w+", "a+"), otherwise it returns False. 
# Syntax: is_readable = file.readable()
# with open("mytxt.txt","r") as f:
#     x=f.readable()
#     print(x)
# o/p-> True
# This method is particularly useful when you want to verify if a file can be read from before attempting to perform read operations.






