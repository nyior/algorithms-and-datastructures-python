"""
input: a valid roman numeral between 1, 3999
output return its integer equivalent
key words/phrases: every roman numeral contains the chars ('I', 'V', 'X', 'L', 'C', 'D', 'M')
example: iii -> 3


key operation: Given an input string, parse the string and return its integer equivalent

simplest version:
s = 'I' -> 1
s = 'II' -. 2
s = 'III' -> 3
s = 'IV'
s = 'vIII'
s = 'IX'

pseudocode:
roms = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

sum = 0
integer = 0

for elem in s:
    integer = roms.get(elem)
    
    if integer > sum and sum > 0:
        sum = integer  - sum
    else:
        sum += integer 
        
return sum
    
"MCMXCIV"    
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roms = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0


        for i in range(len(s)):
            elem = roms[s[i]]
            try:
                if elem < roms[s[i+1]]:
                    total -= elem
                else:
                    total += elem
            except:
                total += elem

        return total
        