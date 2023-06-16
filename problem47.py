"""
Count the Palindrome Substrings in a String

Write a program that takes a string as input and counts the number of palindrome substrings in the string.
"""

# Function to check if a string is palindrome
def is_palindrome(string):
    return string == string[::-1]

# Take input from the user
string = input("Enter a string: ")

# Count the palindrome substrings
count = 0
length = len(string)
for i in range(length):
    for j in range(i+1, length+1):
        substring = string[i:j]
        if is_palindrome(substring):
            count += 1

# Print the result
print("The number of palindrome substrings in the string is", count)
