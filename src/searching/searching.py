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
def binary_search(arr, target):
    first = 0
    last = len(arr)-1
    found = -1
    while(first <= last and found == -1):
        mid = (first + last)//2
        if arr[mid] == target:
            found = mid
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found
