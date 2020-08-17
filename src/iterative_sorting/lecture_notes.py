my_list = [1, 2, 3, 4, 5]

# Linear time complexity -> depends on length
# O(n)
# n == length of input


def print_list(arr):
    for a in arr:
        print(a)

# O(n^2) -- 'steps' quadruple


def nested_loop(arr):
    for thing in arr:
        for other_thing in arr:
            print(thing, other_thing)


#  == == == SORT ALGORITHYM EXAMPLE == == == => #

arr = [99, 98, 4, 0, 5, 2, 3, 1]


def insertion_sort(arr):
    # Start looping at second element
    for i in range(1, len(arr)):
        # pick up current element and hold it
        current = arr[i]
        current_i = 1
        # while current element is less than its left sibling, swap
        while current < arr[i - 1]:
            arr[current_i], arr[current_i - 1] = arr[current_i - 1], arr[current_i]
            current_i -= 1
        # Put current element down
        arr[current_i] = current
    return arr


# Time complexity of insertion sort => O(n^2)
print(arr)
print(insertion_sort(arr))
