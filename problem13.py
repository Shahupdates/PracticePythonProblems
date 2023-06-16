"""
Calculate the Power of a Number

Write a program that takes a base number and an exponent as input and calculates the power of the base number raised to the exponent.
"""

# Take input from the user
base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# Calculate the power
power = base ** exponent

# Print the result
print(base, "raised to the power of", exponent, "is", power)
