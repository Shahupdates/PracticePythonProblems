"""
Count Words in a Text File

Write a program that takes the path to a text file as input and counts the number of words in the file.
"""

# Take input from the user
file_path = input("Enter the path to the text file: ")

# Count the number of words in the file
word_count = 0

with open(file_path, 'r') as file:
    for line in file:
        words = line.split()
        word_count += len(words)

# Print the result
print("The number of words in the file is", word_count)
