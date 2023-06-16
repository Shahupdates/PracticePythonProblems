"""
Find the Intersection of Two Sets

Write a program that takes two sets as input and finds the intersection of the two sets, i.e., the elements that are common to both sets.
"""

# Take input from the user
set1 = set(input("Enter the first set of elements (separated by spaces): ").split())
set2 = set(input("Enter the second set of elements (separated by spaces): ").split())

# Find the intersection of the two sets
intersection = set1.intersection(set2)

# Print the result
print("The intersection of the two sets is:", intersection)
