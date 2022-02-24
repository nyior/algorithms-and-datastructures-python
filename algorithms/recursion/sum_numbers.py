"""
    write a recursive function that sums up all the numbers in an array.
    E.g  [1, 2, 3, 4, 5]  = 15
"""


def sum_numbers(arr):
    if len(arr) == 1:
        return
    else:
        return arr[0] + sum(arr[1:len(arr)])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(sum_numbers(arr))
