"""
    You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] 
    without any duplicates. You are allowed to swap any two elements. 
    Find the minimum number of swaps required to sort the array in ascending order.

    Example
    arr = [7, 1, 3, 2, 4, 5, 6]
"""

def minimum_swaps(arr):
    a = dict(enumerate(arr,1))
    b = dict(
                zip(
                    list(a.values()),
                    range(1,len(a)+1)
                )
        )
    swaps = 0
    
    for i in a:
        
        x = a[i]
        index = b[i]
        
        if x!=i:
            a[i], a[index] = a[index], a[i]
            b[x], b[i] = b[i], b[x] # Update second dict too
            swaps+=1

    return swaps