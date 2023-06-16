"""
Reverse a List

Write a program that takes a list of elements as input and reverses the order of the elements.
"""

# Take input from the user
elements = input("Enter a list of elements (separated by spaces): ").split()

# Reverse the list
reversed_list = elements[::-1]

# Print the result
print("The reversed list is:", reversed_list)
