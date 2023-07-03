#!/usr/bin/python3
"""
   this function finds a peak in a list of unsorted integers
"""

def find_peak(numbers):
    """
    Finds the peak in a list of numbers using an optimized binary search approach.
    """
    length = len(numbers)
    if length == 0:
        return None

    low = 0
    high = length - 1

    while low < high:
        mid = (low + high) // 2

        if numbers[mid] < numbers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return numbers[low]
