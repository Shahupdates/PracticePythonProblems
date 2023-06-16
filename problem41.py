"""
Check if a Number is a Strong Number

Write a program that takes a number as input and checks whether it is a strong number or not.
"""

# Function to calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Take input from the user
number = int(input("Enter a number: "))

# Calculate the sum of the factorial of its digits
temp = number
sum_of_factorial = 0
while temp > 0:
    digit = temp % 10
    sum_of_factorial += factorial(digit)
    temp //= 10

# Check if it is a strong number
is_strong = sum_of_factorial == number

# Print the result
if is_strong:
    print(number, "is a strong number.")
else:
    print(number, "is not a strong number.")
