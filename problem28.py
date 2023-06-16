"""
Convert Decimal to Binary

Write a program that takes a decimal number as input and converts it to binary representation.
"""

# Take input from the user
decimal = int(input("Enter a decimal number: "))

# Convert decimal to binary
binary = bin(decimal)[2:]

# Print the result
print("The binary representation of", decimal, "is", binary)
