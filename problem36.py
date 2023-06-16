"""
Check if a Number is a Perfect Number

Write a program that takes a number as input and checks whether it is a perfect number or not.
"""

# Take input from the user
number = int(input("Enter a number: "))

# Find the proper divisors
divisors = []
for i in range(1, number):
    if number % i == 0:
        divisors.append(i)

# Check if the number is a perfect number
is_perfect = sum(divisors) == number

# Print the result
if is_perfect:
    print(number, "is a perfect number.")
else:
    print(number, "is not a perfect number.")
