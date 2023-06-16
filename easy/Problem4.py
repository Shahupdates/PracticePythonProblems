"""
Problem 4: Check if a Number is Even or Odd

Write a program that takes a number as input and checks whether it is even or odd.
"""

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
