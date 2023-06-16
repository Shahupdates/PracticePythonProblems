# Problem 3: Count Vowels in a String
# Problem Description: Write a program that takes a string as input and counts the number of vowels (a, e, i, o, u) in it.

# Take input from the user
string = input("Enter a string: ")

# Initialize a counter variable
count = 0

# Count the vowels
for char in string:
    if char.lower() in "aeiou":
        count += 1

# Print the result
print("The number of vowels in", string, "is", count)
