"""
Check if a String is a Valid Parenthesis Expression

Write a program that takes a string as input and checks whether it is a valid parenthesis expression. A valid expression should have matching opening and closing parentheses.
"""

# Take input from the user
expression = input("Enter a string: ")

# Check if the string is a valid parenthesis expression
stack = []
opening = '([{'
closing = ')]}'

for char in expression:
    if char in opening:
        stack.append(char)
    elif char in closing:
        if len(stack) == 0:
            is_valid = False
            break
        elif opening.index(stack[-1]) == closing.index(char):
            stack.pop()
        else:
            is_valid = False
            break
else:
    is_valid = len(stack) == 0

# Print the result
if is_valid:
    print(expression, "is a valid parenthesis expression.")
else:
    print(expression, "is not a valid parenthesis expression.")
