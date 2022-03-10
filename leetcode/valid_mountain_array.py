"""
    Given an array of integers arr, return true if and only if it is a valid mountain array.

    Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
    arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
    arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
"""

from typing import List


def validMountainArray(arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        
        peak_index = 0
        n = len(arr)

        for i in range(n-1):
            if arr[i] >= arr[i+1]:
                peak_index = i
                break
        
        if peak_index == 0:
            return False

        for i in range(peak_index, n-1):
            if arr[i] <= arr[i+1]:
                return False
        return True