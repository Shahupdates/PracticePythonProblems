"""
Find the Longest Common Subsequence

Write a program that takes two strings as input and finds the length of the longest common subsequence between the two strings.
"""

def longest_common_subsequence(str1, str2):
    m = len(str1)
    n = len(str2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Take input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Find the length of the longest common subsequence
length = longest_common_subsequence(string1, string2)

# Print the result
print("The length of the longest common subsequence is", length)
