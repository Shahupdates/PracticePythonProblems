"""
Reverse a Number

Write a program that takes a number as input and reverses the digits of the number.
"""

# Take input from the user
number = int(input("Enter a number: "))

# Reverse the digits of the number
reverse = 0
temp = number
while temp > 0:
    digit = temp % 10
    reverse = (reverse * 10) + digit
    temp //= 10

# Print the result
print("The reverse of", number, "is", reverse)
