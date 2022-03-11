"""
input: an array of strings
output: return an array of arrays with each sub-array containing words that are anagrams of
each other

keywords: each entry consist of english letters only
- an entry can be an empty string

example: s = ['ab', 'bc', 'ba', 'cb'] -> [['ab', 'ba'], ['bc', 'cb']]


key operation: parse a list of strings, for each string find other entries 
that are anagrams of the given string

simplest version:
- given a list three strings, find all the anagrams of the first entry

example:  arr = ['ab','ba', 'bc' ba']
{'ab': []}

pseudocode


"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = {}
        all_groups = []
        
        for s in strs:
            key = ''.join(sorted(s))
            
            if key in groups.keys():
                groups[key].append(s)
            else:
                groups[key] = [s]
                
        
        for key, value in groups.items():
            all_groups.append(value)
            
            
        return all_groups
        