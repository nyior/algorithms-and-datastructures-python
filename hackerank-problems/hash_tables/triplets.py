"""
    You are given an array and you need to find number of tripets of indices  (i, j, k)
    such that the elements at those indices are in geometric progression for a given 
    common ratio r and  i < j < k.

    Example
    arr=[1,4,16,64] r=4

    There are  [1,4,16] and  [4,16,64] at indices (0,1,2) and (1,2,3) . Return 2.
"""

from collections import Counter

def count_triplets(arr, r):
    """
        For each elem in arr, find number of elements==elem*r and number of elements==elem/r

        We need to handle the edge case when r=1 though
    """
    items_count = Counter(arr)

    g_p = 0
    
    for i in arr:
        left_count = 0
        right_count = 0
        
        right_multiple = i * r
        left_factor = i/r
        
        right_count = items_count.get(right_multiple)
        left_count = items_count.get(left_factor)
        
        if right_count and left_count:  
            g_p += (left_count * right_count)
        
    return g_p
