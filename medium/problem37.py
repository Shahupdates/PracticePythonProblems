"""
Count the Occurrences of Each Element in a List

Write a program that takes a list of elements as input and counts the number of occurrences of each element in the list.
"""

# Take input from the user
elements = input("Enter a list of elements (separated by spaces): ").split()

# Count the occurrences of each element
element_count = {}
for element in elements:
    element_count[element] = element_count.get(element, 0) + 1

# Print the result
print("Element Count:")
for element, count in element_count.items():
    print(element, "-", count)
