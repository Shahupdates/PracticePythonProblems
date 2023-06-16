"""
Find the Prime Factors of a Number

Write a program that takes a number as input and finds all the prime factors of that number.
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

# Find the prime factors
prime_factors = []
for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0 and is_prime(i):
        prime_factors.append(i)

# Print the result
print("The prime factors of", number, "are:", prime_factors)
