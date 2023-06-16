"""
Calculate the Edit Distance between Two Strings

Write a program that takes two strings as input and calculates the edit distance between the two strings. The edit distance is the minimum number of operations (insertion, deletion, or substitution) required to transform one string into another.
"""

# Take input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Calculate the edit distance using dynamic programming
m = len(string1)
n = len(string2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(m + 1):
    dp[i][0] = i

for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):
        if string1[i - 1] == string2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

edit_distance = dp[m][n]

# Print the result
print("The edit distance between the two strings is", edit_distance)
