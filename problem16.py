"""
Find the Smallest Number in a List

Write a program that takes a list of numbers as input and finds the smallest number in the list.
"""

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Find the smallest number
smallest = min(numbers)

# Print the result
print("The smallest number in the list is", smallest)
