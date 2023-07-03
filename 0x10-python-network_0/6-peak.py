#!/usr/bin/python3
"""
   this function finds a peak in a list of unsorted integers
"""

def find_peak(list_of_integers):
    """
    Finds the peak in a list of list_of_integers using an optimized binary search approach.
    """
    length = len(list_of_integers)
    if length == 0:
        return None

    low = 0
    high = length - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid

    return list_of_integers[low]
