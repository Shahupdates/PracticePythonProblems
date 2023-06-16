"""
Find the Duplicate Number

Write a program that takes a list of integers as input, where the list contains integers in the range 1 to n, and finds the duplicate number in the list.
"""

def find_duplicate(nums):
    slow = fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

# Take input from the user
nums = list(map(int, input("Enter a list of integers (separated by spaces): ").split()))

# Find the duplicate number
duplicate = find_duplicate(nums)

# Print the result
print("The duplicate number is", duplicate)
