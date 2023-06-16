"""
Find the Number of Islands

Write a program that takes a grid of 0's and 1's as input and finds the number of islands. An island is a group of connected 1's, where connectivity is defined by horizontally or vertically adjacent 1's.
"""

def num_islands(grid):
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(i, j):
        if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j] != "1":
            return

        grid[i][j] = "0"

        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == "1":
                dfs(i, j)
                count += 1

    return count

# Take input from the user
grid = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for _ in range(rows):
    row = list(input("Enter the row (0's and 1's): "))
    grid.append(row)

# Find the number of islands
num = num_islands(grid)

# Print the result
print("The number of islands in the grid is", num)
