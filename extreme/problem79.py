"""
Find the First Missing Positive

Write a program that takes a list of integers as input and finds the first missing positive integer. The missing integer should be in the range of 1 to n+1, where n is the length of the list.
"""

def find_first_missing_positive(nums):
    n = len(nums)

    # Step 1: Transform negative numbers and numbers greater than n into a special number (n+1)
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2: Mark the presence of each number in the array
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    # Step 3: Find the index of the first positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # Step 4: If all numbers from 1 to n are present, return n+1
    return n + 1

# Take input from the user
nums = list(map(int, input("Enter a list of integers (separated by spaces): ").split()))

# Find the first missing positive integer
missing_positive = find_first_missing_positive(nums)

# Print the result
print("The first missing positive integer is", missing_positive)
