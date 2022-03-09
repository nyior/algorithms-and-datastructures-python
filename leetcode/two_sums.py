"""
    Given an array of integers nums and an integer target, 
    return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, 
    and you may not use the same element twice. You can return the answer in any order.
"""
from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        value_index = {}
        
        for index, value in enumerate(nums):
            diff = target - value
           
            if value_index.get(diff) is not None:
                return [index, value_index[diff]]
            else:    
                value_index[value] = index
                