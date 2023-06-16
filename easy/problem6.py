"""
Problem 6: Check if a String is Palindrome

Write a program that takes a string as input and checks whether it is a palindrome.
"""

# Take input from the user
string = input("Enter a string: ")

# Check if the string is a palindrome
reverse = string[::-1]
if string == reverse:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")
