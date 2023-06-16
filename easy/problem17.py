"""
Check if a String is a Palindrome Number

Write a program that takes a string as input and checks whether it is a palindrome number.
"""

# Take input from the user
string = input("Enter a string: ")

# Remove non-digit characters from the string
digits = ''.join(char for char in string if char.isdigit())

# Check if the string is a palindrome number
reverse = digits[::-1]
if digits == reverse:
    print(string, "is a palindrome number")
else:
    print(string, "is not a palindrome number")
