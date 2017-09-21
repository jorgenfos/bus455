# BUS455 Applied Programming and Data Analysis for Business
# Assignment 1

## Problem 1

my_list = [45, 4, 1, 76, 3, 5, 8, 89, 21, 34, 55, 71] # add items to list called my_list

print("Pick a number:")
number = int(input()) # prompt user for number

for item in my_list:
    if item < number:
        print(item)
