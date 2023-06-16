"""
Count the Number of Submatrices Summing to Target

Write a program that takes a matrix of numbers and an integer target as input, and counts the number of submatrices whose sum is equal to the target.
"""

from collections import Counter

def count_submatrices(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    count = 0

    for left in range(cols):
        row_sums = [0] * rows

        for right in range(left, cols):
            for i in range(rows):
                row_sums[i] += matrix[i][right]

            prefix_sum = Counter({0: 1})
            current_sum = 0

            for row_sum in row_sums:
                current_sum += row_sum
                count += prefix_sum[current_sum - target]
                prefix_sum[current_sum] += 1

    return count

# Take input from the user
matrix = []
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

for _ in range(rows):
    row = list(map(int, input("Enter the row (separated by spaces): ").split()))
    matrix.append(row)

target = int(input("Enter the target sum: "))

# Count the number of submatrices summing to target
count = count_submatrices(matrix, target)

# Print the result
print("The number of submatrices summing to", target, "is", count)
