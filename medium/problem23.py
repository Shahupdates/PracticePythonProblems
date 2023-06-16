"""
Find Common Elements in Lists

Write a program that takes two lists as input and finds the common elements between them.
"""

# Take input from the user
list1 = input("Enter the first list of elements (separated by spaces): ").split()
list2 = input("Enter the second list of elements (separated by spaces): ").split()

# Find the common elements
common_elements = list(set(list1) & set(list2))

# Print the result
if common_elements:
    print("The common elements between the lists are:", common_elements)
else:
    print("There are no common elements between the lists.")
