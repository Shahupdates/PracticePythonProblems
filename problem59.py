"""
Find the Kth Smallest Element in a List

Write a program that takes a list of numbers and an integer `k` as input, and finds the `k`th smallest element in the list.
"""

# Take input from the user
numbers = input("Enter a list of numbers (separated by spaces): ").split()
numbers = [int(num) for num in numbers]
k = int(input("Enter the value of k: "))

# Find the kth smallest element using quickselect algorithm
def quickselect(nums, k):
    pivot = nums[0]
    smaller = [num for num in nums if num < pivot]
    equal = [num for num in nums if num == pivot]
    larger = [num for num in nums if num > pivot]

    if k <= len(smaller):
        return quickselect(smaller, k)
    elif k <= len(smaller) + len(equal):
        return pivot
    else:
        return quickselect(larger, k - len(smaller) - len(equal))

kth_smallest = quickselect(numbers, k)

# Print the result
print("The", k, "th smallest element is", kth_smallest)
