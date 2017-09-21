# BUS455 Applied Programming and Data Analysis for Business
# Assignment 1

## Problem 2

def sort_and_check(list, number):
    boolean = True
    if number not in list:
        boolean = False
    list.sort()
    print("My ordered list: " + str(list))
    print(boolean)


a = [2.5, 10, 34.5, 1, 67.4, 21, 78, 0, 11]

sort_and_check(a, 5)
sort_and_check(a, 10)
sort_and_check(a, -1)
sort_and_check(a, 2.5)