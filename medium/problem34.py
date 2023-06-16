"""
Find the Median of a List

Write a program that takes a list of numbers as input and finds the median of the list.
"""

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [float(num) for num in numbers]

# Sort the numbers
numbers.sort()

# Find the median
n = len(numbers)
if n % 2 == 0:
    median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2
else:
    median = numbers[n // 2]

# Print the result
print("The median of the list is", median)
