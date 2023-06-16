"""
Count Words in a String

Write a program that takes a string as input and counts the number of words in it.
"""

# Take input from the user
string = input("Enter a string: ")

# Split the string into words
words = string.split()

# Count the number of words
word_count = len(words)

# Print the result
print("The number of words in the string is", word_count)
