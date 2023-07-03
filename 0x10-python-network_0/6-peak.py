def find_peak(numbers):
    """
    Finds the peak in a list of numbers using binary search.
    """
    length = len(numbers)
    if length == 0:
        return None
    if length == 1:
        return numbers[0]

    low = 0
    high = length - 1

    while low <= high:
        mid = (low + high) // 2
        current = numbers[mid]

        if (mid == 0 or numbers[mid - 1] <= current) and (mid == length - 1 or current >= numbers[mid + 1]):
            return current
        elif mid > 0 and numbers[mid - 1] > current:
            high = mid - 1
        else:
            low = mid + 1

    return None