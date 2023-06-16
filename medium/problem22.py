"""
Find the Second Largest Number in a List

Write a program that takes a list of numbers as input and finds the second largest number in the list.
"""

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Find the second largest number
largest = float('-inf')
second_largest = float('-inf')

for num in numbers:
    if num > largest:
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

# Print the result
if second_largest != float('-inf'):
    print("The second largest number in the list is", second_largest)
else:
    print("There is no second largest number in the list.")
