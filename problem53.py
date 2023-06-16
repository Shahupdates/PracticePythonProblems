"""
Calculate the Area of a Polygon

Write a program that takes the coordinates of the vertices of a polygon as input and calculates its area.
"""

# Function to calculate the area of a polygon
def polygon_area(x, y):
    n = len(x)
    area = 0
    j = n - 1

    for i in range(n):
        area += (x[j] + x[i]) * (y[j] - y[i])
        j = i

    return abs(area / 2)

# Take input from the user
n = int(input("Enter the number of vertices: "))
x_coords = []
y_coords = []

for i in range(n):
    x = float(input("Enter the x-coordinate of vertex " + str(i+1) + ": "))
    y = float(input("Enter the y-coordinate of vertex " + str(i+1) + ": "))
    x_coords.append(x)
    y_coords.append(y)

# Calculate the area of the polygon
area = polygon_area(x_coords, y_coords)

# Print the result
print("The area of the polygon is", area)
