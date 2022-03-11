"""
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are 
(i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, 
such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.
"""
from typing import List


# Brute Force
def maxArea(height: List[int]) -> int:
    max_area = 0

    for i in range(len(height)):
        for j in range(i, len(height)):
            if i!= j:
                area = (j -i) * min(height[i], height[j])
                max_area = max(max_area, area)
                
    return max_area


# Optimal solution
def maxArea(self, height: List[int]) -> int:
    start = 0
    end = len(height)-1
    max_area = 0

    while end > start:
        area = (end -start) * min(height[start], height[end])
            
        if area > max_area:
            max_area = area
            
        if height[start] > height[end]:
            end -= 1
        else:
            start += 1
                
    return max_area