"""
Find the Largest Prime Factor of a Number

Write a program that takes a number as input and finds the largest prime factor of that number.
"""

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Take input from the user
number = int(input("Enter a number: "))

# Find the largest prime factor
largest_prime = 0
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0 and is_prime(i):
        largest_prime = i

# Print the result
if largest_prime != 0:
    print("The largest prime factor of", number, "is", largest_prime)
else:
    print(number, "is a prime number.")
