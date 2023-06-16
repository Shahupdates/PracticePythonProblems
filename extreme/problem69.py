"""
Find the Kth Largest Element in an Array

Write a program that takes an array of integers and an integer `k` as input, and finds the `k`th largest element in the array.
"""

import heapq

def find_kth_largest(nums, k):
    min_heap = []

    for num in nums:
        heapq.heappush(min_heap, num)

        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return min_heap[0]

# Take input from the user
nums = list(map(int, input("Enter the array of integers (separated by spaces): ").split()))
k = int(input("Enter the value of k: "))

# Find the kth largest element
kth_largest = find_kth_largest(nums, k)

# Print the result
print("The", k, "th largest element is", kth_largest)
