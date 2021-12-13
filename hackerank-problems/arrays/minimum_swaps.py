"""
    You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
    without any duplicates. You are allowed to swap any two elements. 
    Find the minimum number of swaps required to sort the array in ascending order.

    Example
    arr = [7, 1, 3, 2, 4, 5, 6]
"""

def minimum_swaps(arr):
    swaps = 0
    
    for i in range(len(arr)):
        for j in range(len(arr)):
            if (arr[i] > (i+1)) and (arr[j] == (i+1)):
                arr[i], arr[j] = arr[j], arr[i]
                swaps += 1
    return swaps