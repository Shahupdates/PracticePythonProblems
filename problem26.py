"""
Find the Union of Two Lists

Write a program that takes two lists as input and finds the union of the two lists (i.e., all unique elements from both lists).
"""

# Take input from the user
list1 = input("Enter the first list of elements (separated by spaces): ").split()
list2 = input("Enter the second list of elements (separated by spaces): ").split()

# Find the union of the two lists
union = list(set(list1) | set(list2))

# Print the result
print("The union of the two lists is:", union)
