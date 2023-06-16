"""
Sort a List of Strings by Length

Write a program that takes a list of strings as input and sorts the list in ascending order based on the length of the strings.
"""

# Take input from the user
strings = input("Enter a list of strings (separated by spaces): ").split()

# Sort the list by length of strings
strings.sort(key=len)

# Print the result
print("The sorted list of strings by length is:", strings)
