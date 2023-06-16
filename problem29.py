"""
Find the Common Characters in Strings

Write a program that takes two strings as input and finds the common characters between them.
"""

# Take input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find the common characters
common_chars = ''.join(set(string1) & set(string2))

# Print the result
if common_chars:
    print("The common characters between the strings are:", common_chars)
else:
    print("There are no common characters between the strings.")
