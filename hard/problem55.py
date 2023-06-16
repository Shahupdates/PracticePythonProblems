"""
Reverse Words in a Sentence

Write a program that takes a sentence as input and reverses the order of the words in the sentence.
"""

# Take input from the user
sentence = input("Enter a sentence: ")

# Reverse the order of the words in the sentence
words = sentence.split()
reversed_sentence = ' '.join(words[::-1])

# Print the result
print("The reversed sentence is:", reversed_sentence)
