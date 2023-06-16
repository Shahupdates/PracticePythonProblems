"""
Find the Longest Word in a Sentence

Write a program that takes a sentence as input and finds the longest word in the sentence.
"""

# Take input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)

# Print the result
print("The longest word in the sentence is:", longest_word)
