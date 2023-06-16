"""
Calculate the Sum of Digits in a Number

Write a program that takes a number as input and calculates the sum of its digits.
"""

# Take input from the user
number = int(input("Enter a number: "))

# Calculate the sum of digits
sum_of_digits = sum(int(digit) for digit in str(number))

# Print the result
print("The sum of digits in", number, "is", sum_of_digits)
