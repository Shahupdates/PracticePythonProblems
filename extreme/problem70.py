"""
Find the Median of Two Sorted Arrays

Write a program that takes two sorted arrays as input and finds the median of the two arrays.
"""

def find_median_sorted_arrays(nums1, nums2):
    def find_kth_element(nums1, nums2, k):
        if not nums1:
            return nums2[k - 1]

        if not nums2:
            return nums1[k - 1]

        if k == 1:
            return min(nums1[0], nums2[0])

        mid1 = min(k // 2, len(nums1))
        mid2 = min(k // 2, len(nums2))

        if nums1[mid1 - 1] < nums2[mid2 - 1]:
            return find_kth_element(nums1[mid1:], nums2, k - mid1)
        else:
            return find_kth_element(nums1, nums2[mid2:], k - mid2)

    n = len(nums1) + len(nums2)
    if n % 2 == 1:
        return find_kth_element(nums1, nums2, (n + 1) // 2)
    else:
        return (find_kth_element(nums1, nums2, n // 2) + find_kth_element(nums1, nums2, n // 2 + 1)) / 2

# Take input from the user
nums1 = list(map(int, input("Enter the first sorted array (separated by spaces): ").split()))
nums2 = list(map(int, input("Enter the second sorted array (separated by spaces): ").split()))

# Find the median of the two arrays
median = find_median_sorted_arrays(nums1, nums2)

# Print the result
print("The median of the two sorted arrays is", median)
