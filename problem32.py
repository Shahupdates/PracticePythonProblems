"""
Reverse the Order of Words in a Sentence

Write a program that takes a sentence as input and reverses the order of the words while preserving the order of the characters in each word.
"""

# Take input from the user
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Reverse the order of the words and join them
reversed_sentence = ' '.join(words[::-1])

# Print the result
print("The sentence with reversed word order is:", reversed_sentence)
