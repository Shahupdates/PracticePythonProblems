"""
Find the Celebrity

Suppose you are at a party with n people labeled from 0 to n-1. You are given a 2D matrix called `knows`, where `knows[i][j]` is `True` if person i knows person j, and `False` otherwise. A celebrity is defined as someone who knows no one but is known by everyone else.
"""

def find_celebrity(n, knows):
    potential_celebrity = 0

    for i in range(1, n):
        if knows[potential_celebrity][i]:
            potential_celebrity = i

    for i in range(n):
        if i != potential_celebrity and (knows[potential_celebrity][i] or not knows[i][potential_celebrity]):
            return -1

    return potential_celebrity

# Take input from the user
n = int(input("Enter the number of people: "))
knows = []

print("Enter the 'knows' matrix (1 for True and 0 for False):")
for _ in range(n):
    row = list(map(int, input().split()))
    knows.append(row)

# Find the celebrity at the party
celebrity = find_celebrity(n, knows)

# Print the result
if celebrity == -1:
    print("No celebrity found.")
else:
    print("The celebrity at the party is person", celebrity)
