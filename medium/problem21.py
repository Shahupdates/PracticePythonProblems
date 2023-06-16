"""
Validate Email Address

Write a program that takes an email address as input and validates whether it is a valid email address format or not.
"""

import re

# Take input from the user
email = input("Enter an email address: ")

# Validate the email address format
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
is_valid = re.match(pattern, email)

# Print the result
if is_valid:
    print(email, "is a valid email address.")
else:
    print(email, "is not a valid email address.")
