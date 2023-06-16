"""
Calculate the Minimum Window Substring

Write a program that takes two strings as input, a larger string and a smaller string, and finds the minimum window substring of the larger string that contains all the characters of the smaller string.
"""

from collections import Counter

def min_window(s, t):
    target_counts = Counter(t)
    required = len(target_counts)
    formed = 0
    window_counts = {}
    ans = float('inf'), None, None
    l = r = 0

    while r < len(s):
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1

        if char in target_counts and window_counts[char] == target_counts[char]:
            formed += 1

        while l <= r and formed == required:
            char = s[l]

            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)

            window_counts[char] -= 1

            if char in target_counts and window_counts[char] < target_counts[char]:
                formed -= 1

            l += 1

        r += 1

    return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]

# Take input from the user
s = input("Enter the larger string: ")
t = input("Enter the smaller string: ")

# Find the minimum window substring
substring = min_window(s, t)

# Print the result
print("The minimum window substring is", substring)
