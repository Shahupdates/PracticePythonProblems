"""
Generate the nth Fibonacci Number

Write a program that takes a number `n` as input and generates the `n`th Fibonacci number.
"""

# Take input from the user
n = int(input("Enter a number: "))

# Generate the nth Fibonacci number
fibonacci = [0, 1]
for i in range(2, n + 1):
    next_term = fibonacci[i - 1] + fibonacci[i - 2]
    fibonacci.append(next_term)

# Print the result
print("The", n, "th Fibonacci number is:", fibonacci[n])
