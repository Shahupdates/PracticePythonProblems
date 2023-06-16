"""
Check if a Year is a Leap Year

Write a program that takes a year as input and checks whether it is a leap year.
"""

# Take input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
