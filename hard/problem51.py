"""
Find the Longest Increasing Subsequence

Write a program that takes a list of numbers as input and finds the length of the longest increasing subsequence in the list.
"""

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]

# Find the length of the longest increasing subsequence
n = len(numbers)
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            dp[i] = max(dp[i], dp[j] + 1)

longest_length = max(dp)

# Print the result
print("The length of the longest increasing subsequence is", longest_length)
