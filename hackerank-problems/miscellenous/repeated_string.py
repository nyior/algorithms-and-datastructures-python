"""
There is a string, s, of lowercase English letters that is repeated infinitely many times. 
Given an integer, n , find and print the number of letter a's in the first  
letters of the infinite string.

Example
s =  'abcac'
n=10

The substring we consider is 'abcacabcac', 
the first  characters of the infinite string. 
There are 4 occurrences of a in the substring.
"""

def repeatedString(s, n):
    
    return (s.count('a')*(n//len(s))) + (s[:n % len(s)].count('a'))