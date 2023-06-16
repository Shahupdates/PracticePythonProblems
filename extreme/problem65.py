"""
Find the Longest Increasing Path in a Matrix

Write a program that takes a matrix of numbers as input and finds the length of the longest increasing path within the matrix. A path is considered increasing if each number along the path is strictly greater than the previous number.
"""

def longest_increasing_path(matrix):
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    dp = [[0] * cols for _ in range(rows)]

    def dfs(i, j):
        if dp[i][j] != 0:
            return dp[i][j]

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        length = 1

        for dx, dy in directions:
            x = i + dx
            y = j + dy

            if 0 <= x < rows and 0 <= y < cols and matrix[x][y] > matrix[i][j]:
                length = max(length, 1 + dfs(x, y))

        dp[i][j] = length
        return length

    longest = 0

    for i in range(rows):
        for j in range(cols):
            longest = max(longest, dfs(i, j))

    return longest

# Take input from the user
matrix = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for _ in range(rows):
    row = list(map(int, input("Enter the row (separated by spaces): ").split()))
    matrix.append(row)

# Find the length of the longest increasing path
length = longest_increasing_path(matrix)

# Print the result
print("The length of the longest increasing path in the matrix is", length)
