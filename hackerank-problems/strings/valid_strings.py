"""
    Sherlock considers a string to be valid if all characters of the string appear the same number of times. 
    It is also valid if he can remove just 1 character at 1 index in the string, 
    and the remaining characters will occur the same number of times. Given a string, 
    determine if it is valid. If so, return YES, otherwise return NO.
"""
from collections import Counter

# Copied this solution from Hackerrank
def is_valid(s):
    string=Counter(s)
    string=Counter(string.values())
    
    if len(string.keys())==1:
        return "YES"

    elif len(string.values())==2:
        key1,key2=string.keys()
        if string[key1]==1 and (key1-1==key2 or key1-1==0):
            return "YES"
        elif string[key2]==1 and (key2-1==key1 or key2-1==0):
            return "YES"
        else:
            return "NO"

    else:
        return "NO"