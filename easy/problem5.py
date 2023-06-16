"""
Problem 5: Calculate the Factorial of a Number

Write a program that takes a number as input and calculates its factorial.
"""

# Take input from the user
number = int(input("Enter a number: "))

# Calculate the factorial
factorial = 1
for i in range(1, number + 1):
    factorial *= i

# Print the result
print("The factorial of", number, "is", factorial)
