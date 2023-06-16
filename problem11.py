"""
Generate Fibonacci Series

Write a program that takes a number as input and generates the Fibonacci series up to that number.
"""

# Take input from the user
n = int(input("Enter the number of terms: "))

# Generate Fibonacci series
fibonacci = [0, 1]
for i in range(2, n):
    next_term = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_term)

# Print the result
print("The Fibonacci series is:", fibonacci)
