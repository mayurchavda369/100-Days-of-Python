# Top 10 common Python Programs for beginners:
# ex: 1 Add two numbers
# n1=int(input("Enter First number : "))
# n2=int(input("Enter Second number : "))
# print("Your Sum is : ",n1+n2)
# # o/p-> Your Sum is :  40
# ex : 2 Even-Odd number 
# x=int(input("Enter Any number : "))
# if x%2==0:
#     print("Even")
# elif x==0:
#     print("please enter valid number ")
# else:
#     print("Odd")
# o/p-> 5 odd
# Ex 3: Reverse Number 
# n=int(input("Enter your number : "))
# reverse=0
# while n>0:
#     digit=n%10
#     reverse=(reverse*10)+digit
#     n=n//10
# print("reverse number is : ",reverse)
# Ex: 4 Armstrong number
# n=int(input("Enter your number : "))
# num=n
# sum=0
# order=len(str(n))
# while n>0:
#     d=n%10
#     sum=sum+d**order
#     n=n//10
# if(sum==num):
#     print("Armstrong number")
# else:
#     print("Not Armstrong number")
# o/p-> 153 Armstrong number
# Ex 5: Leap Year Program
# n = int(input("Enter Year: "))
# if (n % 4 == 0) and (n % 100 != 0) or (n % 400 == 0):
#     print("It's a leap year")
# else:
#     print("Not a leap year")
# o/p-> 2020 its a leap year.
# Ex 6:  Anagram Program (one string consider second string character)
# Input two strings from the user
# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")

# # Convert both strings to lowercase
# string1 = string1.lower()
# string2 = string2.lower()
# # Remove spaces from both strings
# string1 = string1.replace(" ", "")
# string2 = string2.replace(" ", "")
# # Sort the characters of both strings
# sorted_string1 = sorted(string1)
# sorted_string2 = sorted(string2)
# # Check if the sorted strings are equal
# if sorted_string1 == sorted_string2:
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")
# o/p-> listen and silent are anagram words.
# Ex:6 Prime number
# n=int(input("Enter Your Number : "))
# res="Prime"
# for i in range(2,n//2+1):
#     if n % i==0:
#         res="Non Prime"
#         break
# print(res)
# o/p-> 11 prime
# Ex: 7 swap the number
# a=int(input("enter value of A : "))
# b=int(input("enter value of B : "))
# print("A is : ",a,"B is : ",b)
# a,b=b,a
# print("A is : ",a,"B is : ",b)
# o/p->
# A is :  11 B is :  21
# A is :  21 B is :  11
# Ex 8: passed words is vowel or not 
# V1=str(input())
# if V1 in ("a,i,o,u,e") and ('A,I,O,U,E'):
#     print('vowel')
# else:
#     print('not vowel')
# o/p-> a is vowel
# Ex 9 : Find length of word without using function.
# name = input("write your name: ")
# length = 0
# for l in name:
#     length += 1
# print("Length of the string:", length)
# o/p-> mayur 5
# Ex 10: Write a Python program to check if a number is positive, negative or zero
# u=int(input())
# if u>0:
#     print("positive")
# elif u==0:
#     print("zero")
# else:
#     print("negative")













