# Python first program 
# Ex 1:
print("Hello World ")
print("mayur",1,1.7,True)
print("mayur","chavda",369, sep="~")
print("mayur","chavda",369, end="36\n")
print("ram")
print(object())
print()
with open('output.txt', 'w') as file:
    print("Hello, World!", file=file)


# Print is a Built in Function to dispaly anything.
# you can give any type of value in print function.
# you can using "sep"keyward for seperation in print.
# you can using "end" keyward for write anything in end of words in print.
# When you call print(object()), it essentially creates an instance of the object class (which is a generic, built-in class in Python), and 
# then the print function attempts to convert this object to its string representation and display it. 
# The string representation of an instance of the object class typically includes information about the memory location of the object.
# In the output, 0xXXXXXXXX represents the memory address where the object is stored. The exact address will vary each time you run the program.
# print() use for new line.
# we can using print function we write in file also.

# comments : some info provide to team member or some info hide to code thats why we use comment
# comment symbol is "#" and multiline comments use with ''' comments '''.

#Escape squence character :
# In Python, escape sequences are special characters that are used to represent non-printable or special characters within string literals. 
#  using in strings.
# They are represented by a backslash "\" followed by a specific character. Here are some common escape sequences in Python:

# Newline (\n): Represents a newline character.

print("Hello\nWorld")
# Tab (\t): Represents a tab character.

print("Hello\tWorld")
# Backslash (\\): Represents a literal backslash character.


print("This is a backslash: \\")
# Single Quote (\'): Represents a single quote character in a single-quoted string.


print('This is a single quote: \'')
# Double Quote (\"): Represents a double quote character in a double-quoted string.


print("This is a double quote: \"")
# Backspace (\b): Represents a backspace character.


print("Hello\bWorld")
# Carriage Return (\r): Represents a carriage return character.

print("Hello\rWorld")
# Octal Escape (\ooo): Represents a character based on its octal value (e.g., \012).


print("\012")  # Prints a newline character using octal value
# Unicode Escape (\uXXXX or \UXXXXXXXX): Represents a Unicode character based on its hexadecimal value.

print("\u03A3")  # Prints the Greek letter Sigma (Σ)
