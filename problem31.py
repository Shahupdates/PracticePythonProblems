"""
Find the Mode of a List

Write a program that takes a list of elements as input and finds the mode (most frequently occurring element) of the list.
"""

# Take input from the user
elements = input("Enter a list of elements (separated by spaces): ").split()

# Find the mode of the list
element_count = {}
for element in elements:
    element_count[element] = element_count.get(element, 0) + 1

modes = []
max_count = max(element_count.values())
for element, count in element_count.items():
    if count == max_count:
        modes.append(element)

# Print the result
if len(modes) > 1:
    print("The modes of the list are:", ', '.join(modes))
else:
    print("The mode of the list is:", modes[0])
