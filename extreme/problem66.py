"""
Find the Number of Islands II

Write a program that takes a grid of 0's and 1's as input and a list of positions where the value changes to 1. For each position, find the number of islands after the change. An island is a group of connected 1's, where connectivity is defined by horizontally or vertically adjacent 1's.
"""

def num_islands(grid, positions):
    rows = len(grid)
    cols = len(grid[0])
    count = 0
    result = []
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    roots = [-1] * (rows * cols)

    def find(x):
        if roots[x] == -1:
            return x

        roots[x] = find(roots[x])
        return roots[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x != root_y:
            roots[root_x] = root_y
            nonlocal count
            count -= 1

    def get_index(i, j):
        return i * cols + j

    for position in positions:
        i, j = position[0], position[1]

        if grid[i][j] == 0:
            grid[i][j] = 1
            count += 1

            for dx, dy in directions:
                x = i + dx
                y = j + dy

                if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                    union(get_index(i, j), get_index(x, y))

        result.append(count)

    return result

# Take input from the user
grid = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for _ in range(rows):
    row = list(map(int, input("Enter the row (0's and 1's): ").split()))
    grid.append(row)

n = int(input("Enter the number of positions: "))
positions = []

for _ in range(n):
    position = list(map(int, input("Enter the position (row and column): ").split()))
    positions.append(position)

# Find the number of islands after the changes
islands = num_islands(grid, positions)

# Print the result
print("The number of islands after the changes are:", islands)
