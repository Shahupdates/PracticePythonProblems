"""
Calculate the Average of a List of Numbers

Write a program that takes a list of numbers as input and calculates their average.
"""

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [float(num) for num in numbers]

# Calculate the average
average = sum(numbers) / len(numbers)

# Print the result
print("The average of the numbers is", average)
