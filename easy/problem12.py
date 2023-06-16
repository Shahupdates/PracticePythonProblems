"""
Check if a Number is Prime

Write a program that takes a number as input and checks whether it is a prime number.
"""

# Take input from the user
number = int(input("Enter a number: "))

# Check if the number is prime
is_prime = True
for i in range(2, number):
    if number % i == 0:
        is_prime = False
        break

# Print the result
if is_prime:
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")
