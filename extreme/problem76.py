"""
Find the Longest Increasing Subsequence

Write a program that takes a list of integers as input and finds the length of the longest increasing subsequence within the list.
"""

def longest_increasing_subsequence(nums):
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

# Take input from the user
nums = list(map(int, input("Enter a list of integers (separated by spaces): ").split()))

# Find the length of the longest increasing subsequence
length = longest_increasing_subsequence(nums)

# Print the result
print("The length of the longest increasing subsequence is", length)
