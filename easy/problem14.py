"""
Check if a String is a Pangram

Write a program that takes a string as input and checks whether it is a pangram (contains all the letters of the alphabet).
"""

import string

# Take input from the user
string = input("Enter a string: ")

# Convert the string to lowercase and remove spaces
string = string.lower().replace(" ", "")

# Check if it is a pangram
is_pangram = all(letter in string for letter in string.ascii_lowercase)

# Print the result
if is_pangram:
    print(string, "is a pangram")
else:
    print(string, "is not a pangram")
