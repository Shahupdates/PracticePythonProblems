"""
Remove Duplicates from a List

Write a program that takes a list of elements as input and removes any duplicate elements from the list.
"""

# Take input from the user
elements = input("Enter a list of elements (separated by spaces): ").split()

# Remove duplicates from the list
unique_elements = list(set(elements))

# Print the result
print("The list with duplicates removed is:", unique_elements)
