# Conditional statement and controll statements.
# Conditional statements : if,else,elif,nested if-else.
# Controll staements : break,continue,pass.
# if Statement:
The if statement is used to check a condition and execute a block of code if the condition is true.
x = 10
if x > 5:
    print("x is greater than 5")

if-else Statement:
The if-else statement allows you to execute one block of code if the condition is true and another block if the condition is false.
x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

if-elif-else Statement:
The if-elif-else statement allows you to check multiple conditions and execute different blocks of code based on the first true condition.

x = 3
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

Nested if Statements:
You can also nest if statements inside each other to handle more complex conditions.

x = 10
if x > 5:
    print("x is greater than 5")
    if x == 10:
        print("x is equal to 10")
else:
    print("x is not greater than 5")

Ternary Conditional Expression:
Python also supports a concise form of conditional expression using the ternary operator.

x = 7
result = "x is greater than 5" if x > 5 else "x is not greater than 5"
print(result)
Conditional statements are fundamental for controlling the flow of your program based on different situations and conditions. 

Ex: Print table using if statement
n=int(input())
i=1
if n*1 <= n*10:
    print(n*i)
    i+=1
    print(n*i)
    i+=1
    print(n*i)
    i+=1
    print(n*i)
#  till perform 9 times then you get table of number.
    