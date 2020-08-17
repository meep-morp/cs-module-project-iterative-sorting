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
