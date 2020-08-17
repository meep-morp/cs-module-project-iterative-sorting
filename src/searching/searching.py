from iterative_sorting import selection_sort


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Compare the item in the middle of the data set to the item we are searching for.
    # If it is the same, stop. We found it and are done!
    # Else, if the item we are searching for is LESS than the item in the middle:
    # Eliminate the RHS of list. Repeat step 1 with only the LHS of list.
    # Else, the item we are searching for is GREATER than the item in the middle:
    # Eliminate the LHS of list. Repeat step 1 with only the RHS of the list.


# Write an iterative implementation of Binary Search
def binary_search(arr, target, start=0, end=None):
    arr = selection_sort(arr)

    if end is None:
        end = len(arr) - 1

    if start > end:
        return -1

# Stack Overflow helped with this :D
    mid = (start + end) // 2
    if target == arr[mid]:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, start, mid-1)

    return binary_search(arr, target, mid+1, end)
