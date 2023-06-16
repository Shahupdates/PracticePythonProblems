"""
Check if a Number is a Perfect Square

Write a program that takes a number as input and checks whether it is a perfect square or not.
"""

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is a perfect square
is_perfect_square = number >= 0 and int(number ** 0.5) ** 2 == number

# Print the result
if is_perfect_square:
    print(number, "is a perfect square.")
else:
    print(number, "is not a perfect square.")
