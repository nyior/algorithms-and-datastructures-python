"""
input: an array of positive and negative numbers
expected output: return the sum of the sub-array with the largest sum
key things: a sub-array is a contiguous part of the array, each sub-array is one containing at least one element.

sample inputs: [1, 2, 4, 5, -9, 0, 4] result = 13


key operation: finding sub-array with maximum sum

simplest version: [2] return arr[0]
[1, 4] -> 1, 4, 1+4 return 5
[1, 4, 3] -> 1, 4, 1+4, 3, 3+4, 3+4+1
[1, 4, 3, 5]

[-2,-1]
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]
        
        current_max_sum = float('-inf')
        main_max_sum  = float('-inf')
        
        
        for i in nums:
            current_max_sum = max(i, i+current_max_sum)
            main_max_sum = max(current_max_sum, main_max_sum)
            
        return main_max_sum