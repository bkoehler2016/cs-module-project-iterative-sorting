def linear_search(arr, target):
    for index, elem in enumerate(arr):
        if elem is target:
            return index

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        middle = (low + high) // 2
    
        if arr[middle] is target:
            return middle
        else:
            if arr[middle] > target:
                high = middle - 1
            else:
                low = middle + 1

    return -1  # not found
