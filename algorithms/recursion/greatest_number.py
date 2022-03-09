"""
    Find the greatest number in an array recursively
    arr = [1, 2, 3, 4, 5]

"""

def highest_num(arr):
    if len(arr) == 1:
        return arr[0]

    biggest = highest_num(arr[1:])
    if arr[0] > biggest:
        return arr[0]
    else:
        return biggest
