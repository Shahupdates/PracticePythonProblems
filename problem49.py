"""
Implement a Binary Search Algorithm

Write a program that takes a sorted list of numbers and a target number as input and implements the binary search algorithm to find the index of the target number in the list. If the target number is not found, return -1.
"""

# Function to implement binary search
def binary_search(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Take input from the user
numbers = input("Enter a sorted list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]
target = int(input("Enter the target number: "))

# Find the index of the target number using binary search
index = binary_search(numbers, target)

# Print the result
if index != -1:
    print("The target number", target, "is found at index", index)
else:
    print("The target number", target, "is not found in the list.")
