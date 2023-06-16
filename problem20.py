"""
Count the Occurrences of an Element in a List

Write a program that takes a list of elements and an element as input, and counts the number of occurrences of that element in the list.
"""

# Take input from the user
elements = input("Enter a list of elements (separated by spaces): ").split()
element = input("Enter the element to count: ")

# Count the occurrences of the element
count = elements.count(element)

# Print the result
print("The element", element, "occurs", count, "time(s) in the list.")
