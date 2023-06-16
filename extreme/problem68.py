"""
Count the Number of Valid Sudoku Boards

Write a program that takes a 9x9 Sudoku board as input and counts the number of valid Sudoku boards. A valid Sudoku board must satisfy the following rules:
- Each row contains the digits 1-9 without repetition.
- Each column contains the digits 1-9 without repetition.
- Each of the nine 3x3 sub-grids contains the digits 1-9 without repetition.
"""

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

def count_valid_sudoku(board):
    count = 0

    def backtrack(board, row, col):
        nonlocal count

        if row == 9:
            count += 1
            return

        if col == 9:
            backtrack(board, row + 1, 0)
            return

        if board[row][col] != 0:
            backtrack(board, row, col + 1)
            return

        for num in range(1, 10):
            if is_valid(board, row, col, num):
                board[row][col] = num
                backtrack(board, row, col + 1)
                board[row][col] = 0

    backtrack(board, 0, 0)
    return count

# Take input from the user
board = []
print("Enter the Sudoku board:")
for _ in range(9):
    row = list(map(int, input().split()))
    board.append(row)

# Count the number of valid Sudoku boards
count = count_valid_sudoku(board)

# Print the result
print("The number of valid Sudoku boards is", count)
