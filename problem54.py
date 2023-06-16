"""
Find the Smallest Missing Positive Integer

Write a program that takes a list of integers as input and finds the smallest missing positive integer that does not appear in the list.
"""

# Take input from the user
numbers = input("Enter a list of integers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Find the smallest missing positive integer
n = len(numbers)

for i in range(n):
    while 1 <= numbers[i] <= n and numbers[numbers[i] - 1] != numbers[i]:
        numbers[numbers[i] - 1], numbers[i] = numbers[i], numbers[numbers[i] - 1]

for i in range(n):
    if numbers[i] != i + 1:
        smallest_missing = i + 1
        break
else:
    smallest_missing = n + 1

# Print the result
print("The smallest missing positive integer is", smallest_missing)
