"""
    The problem is that we want to find duplicates in a one-dimensional 
    array of integers in O(N) running time where the integer values 
    are smaller than the length of the array!

    For example: if we have a list [1, 2, 3, 1, 5] then the algorithm 
    can detect that there are a duplicate with value 1.

    Note: the array can not contain items smaller than 0 and items with 
    values greater than the size of the list. 
    This is how we can achieve O(N) linear running time complexity!
"""


def find_repetition(array):

    for item in array:
        if array[abs(item)] >= 0:
            array[abs(item)] = -array[abs(item)]
        else:
            print(f"{abs(item)} is repeated")


if __name__ == "__main__":
    arr = [2, 1, 3, 1, 4, 3, 2]

    find_repetition(arr)