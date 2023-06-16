"""
Find the Maximum Number in a List

Write a program that takes a list of numbers as input and finds the maximum number in the list.
"""

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Find the maximum number
maximum = max(numbers)

# Print the result
print("The maximum number in the list is", maximum)
