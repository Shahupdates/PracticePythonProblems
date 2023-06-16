"""
Generate Random Password

Write a program that generates a random password of a specified length. The password should contain a mix of uppercase letters, lowercase letters, digits, and special characters.
"""

import random
import string

# Take input from the user
length = int(input("Enter the length of the password: "))

# Define the characters to choose from
characters = string.ascii_letters + string.digits + string.punctuation

# Generate the random password
password = ''.join(random.choice(characters) for _ in range(length))

# Print the result
print("Random Password:", password)
