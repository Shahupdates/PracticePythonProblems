"""
Implement Bubble Sort

Write a program that takes a list of numbers as input and implements the bubble sort algorithm to sort the list in ascending order.
"""

# Function to implement bubble sort
def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Sort the list using bubble sort
bubble_sort(numbers)

# Print the result
print("The sorted list is:", numbers)
