"""
Calculate the Power Set of a Set

Write a program that takes a set of elements as input and calculates its power set, which is the set of all possible subsets of the given set.
"""

from itertools import chain, combinations

# Take input from the user
elements = input("Enter a set of elements (separated by spaces): ").split()

# Calculate the power set
power_set = list(chain.from_iterable(combinations(elements, r) for r in range(len(elements) + 1)))

# Print the result
print("The power set of the given set is:")
for subset in power_set:
    print(subset)
