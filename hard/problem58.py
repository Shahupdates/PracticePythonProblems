"""
Calculate the Maximum Subarray Sum

Write a program that takes a list of integers as input and calculates the maximum sum of a subarray within the list.
"""

# Take input from the user
numbers = input("Enter a list of integers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Calculate the maximum subarray sum
max_sum = float('-inf')
current_sum = 0

for num in numbers:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

# Print the result
print("The maximum subarray sum is", max_sum)
