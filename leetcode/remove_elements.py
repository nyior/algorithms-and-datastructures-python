"""
input: array of integers, and val
output: returns the lengrh of array after removing k elems, and the newly modified array

keyword: This has to be done inplace

sample input: [0,1,2,2,3,0,4,2]

{0:0, 1:1, 2:2, 3:2, 4:3, 5:0, 6:4, 7:2}
2
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0

        while index <= len(nums)-1:
            if val == nums[index]:
                del nums[index]
            else:
                index += 1

            if index == len(nums):
                index += 1 
            
        return (len(nums))