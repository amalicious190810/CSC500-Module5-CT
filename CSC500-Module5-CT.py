# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 11:13:27 2023

@author: pulik
"""

#%%

# Part 1: Average Rainfall Calculator

# Ask for user input for number of years
num_years = int(input("Enter the number of years:\n"))

# List of month names
months = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
    ]

# Init total rainfall variable
total_rainfall = 0

# Outer loop for each year
for year in range(1, num_years + 1):
    # Inner loop for each month of each year
    for month in range(12):
        # Ask for user input for inches of rainfall of each month
        inches = float(
            input(
                f"\nEnter inches of rainfall for {months[month]} of Year {year}:\n"))
        total_rainfall += inches
        
# Calculate the number of months
num_months = num_years * 12

# Calculate the average rainfall per month
average_rainfall = total_rainfall / num_months

# Print results
print(f"\nTotal Number of Months: {num_months} months")
print(f"\nTotal Inches of Rainfall: {total_rainfall} inches")
print(f"\nAverage Rainfall per Month: {average_rainfall} inches")

#%%

# Part 2: Book Club Points Calculator

# Ask for user input for number of books purchased
num_books = int(input("\nEnter the number of books you purchased this month:\n"))

# Conditionally calculate the awarded points based on the number of books purchased
if num_books <= 1:
    points = 0
elif num_books <= 3:
    points = 5
elif num_books <= 5:
    points = 15
elif num_books <= 7:
    points = 30
elif num_books >= 8:
    points = 60
else:
    points = 0  # No points for other values

# Display the points awarded
print(f"You have earned {points} points for purchasing {num_books} books this month.")

