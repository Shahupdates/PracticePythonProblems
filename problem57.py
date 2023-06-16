"""
Check if a String is an Anagram

Write a program that takes two strings as input and checks whether they are anagrams of each other. Anagrams are strings that have the same characters but in a different order.
"""

# Take input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the strings are anagrams
is_anagram = sorted(string1.lower()) == sorted(string2.lower())

# Print the result
if is_anagram:
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")
