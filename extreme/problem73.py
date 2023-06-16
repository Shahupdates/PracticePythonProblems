"""
Find the K Closest Points to the Origin

Write a program that takes a list of points (coordinates) in a 2D plane and an integer `k` as input, and finds the `k` closest points to the origin. The distance between two points `(x1, y1)` and `(x2, y2)` is given by the formula: `distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)`.
"""

import heapq
from math import sqrt

def find_k_closest(points, k):
    max_heap = []

    for point in points:
        distance = sqrt(point[0] ** 2 + point[1] ** 2)
        heapq.heappush(max_heap, (-distance, point))

        if len(max_heap) > k:
            heapq.heappop(max_heap)

    return [point for _, point in max_heap]

# Take input from the user
points = []
n = int(input("Enter the number of points: "))

for _ in range(n):
    point = list(map(int, input("Enter the coordinates (x and y): ").split()))
    points.append(point)

k = int(input("Enter the value of k: "))

# Find the k closest points to the origin
k_closest = find_k_closest(points, k)

# Print the result
print("The", k, "closest points to the origin are:", k_closest)
