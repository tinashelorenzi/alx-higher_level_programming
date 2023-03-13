#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replaces an element in a list at a specific position without modifying the original list.

    Args:
    my_list: A list of elements
    idx: An integer representing the position of the element to replace
    element: The new element to insert at the specified position

    Returns:
    A new list with the specified element replaced at the specified position, or a copy of the original list if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list[:] # return a copy of the original list

    new_list = my_list[:] # create a copy of the original list
    new_list[idx] = element # replace the element at the specified position
    return new_list
