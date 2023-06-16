"""
Find the Longest Palindromic Substring

Write a program that takes a string as input and finds the longest palindromic substring within the string.
"""

def longest_palindromic_substring(string):
    n = len(string)
    dp = [[False] * n for _ in range(n)]

    start = 0
    max_length = 1

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if length == 2:
                dp[i][j] = string[i] == string[j]
            else:
                dp[i][j] = string[i] == string[j] and dp[i + 1][j - 1]

            if dp[i][j] and length > max_length:
                start = i
                max_length = length

    return string[start:start + max_length]

# Take input from the user
string = input("Enter a string: ")

# Find the longest palindromic substring
substring = longest_palindromic_substring(string)

# Print the result
print("The longest palindromic substring is", substring)
