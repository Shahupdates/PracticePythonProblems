"""
Find the GCD of Two Numbers

Write a program that takes two numbers as input and finds their greatest common divisor (GCD).
"""

# Function to calculate the GCD using Euclidean algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Take input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Find the GCD
gcd_result = gcd(num1, num2)

# Print the result
print("The GCD of", num1, "and", num2, "is", gcd_result)
