"""
Calculate the Minimum Cost Path in a Matrix

Write a program that takes a matrix of numbers and finds the minimum cost path from the top-left corner to the bottom-right corner. The cost of a path is the sum of the numbers along the path.
"""

def min_cost_path(matrix):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    dp[0][0] = matrix[0][0]

    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = matrix[i][j] + min(dp[i - 1][j], dp[i][j - 1])

    return dp[m - 1][n - 1]

# Take input from the user
matrix = []
m = int(input("Enter the number of rows: "))
n = int(input("Enter the number of columns: "))

for _ in range(m):
    row = list(map(int, input("Enter the row (separated by spaces): ").split()))
    matrix.append(row)

# Find the minimum cost path
cost = min_cost_path(matrix)

# Print the result
print("The minimum cost path in the matrix is", cost)
