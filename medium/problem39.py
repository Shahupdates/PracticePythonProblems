"""
Find the Difference between Two Lists

Write a program that takes two lists as input and finds the elements that are present in the first list but not in the second list.
"""

# Take input from the user
list1 = input("Enter the first list of elements (separated by spaces): ").split()
list2 = input("Enter the second list of elements (separated by spaces): ").split()

# Find the difference between the two lists
difference = list(set(list1) - set(list2))

# Print the result
print("The elements present in the first list but not in the second list are:", difference)
