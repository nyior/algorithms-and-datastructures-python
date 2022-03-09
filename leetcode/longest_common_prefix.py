"""
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".

    Example 1:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"
"""
from typing import List


def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        shortest = min(strs, key=len)
        n = len(shortest)
        
        
        if len(strs) == 1:
            return strs[0]
        
        for i in range(n):
    
            for entry in strs:
                if shortest[i] != entry[i]:
                    return prefix

            prefix += shortest[i]
            
        return prefix