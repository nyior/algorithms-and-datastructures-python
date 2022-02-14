"""
    A string is said to be a special string if either of two conditions is met:
    - All of the characters are the same, e.g. aaa.
    - All characters except the middle one are the same, e.g. aadaa.
    A special substring is any substring of a string which meets one of those criteria. 
    Given a string, determine how many special substrings can be formed from it.

    Example

    s = mnonopoo
    s contains the following 12 special substrings: {m, n, o, n, o, p, o, o, non, ono, opo, oo}

    Code a function that returns the number of special substrings in a string.
"""

def substr_count(s):
    """copied from hackerank"""
    
    tot = 0
    count_sequence = 0
    prev = ''

    for i,v in enumerate(s):
        count_sequence += 1
        
        if i and (prev != v):
            j = 1
            
            while ((i-j) >= 0) and ((i+j) < len(s)) and j <= count_sequence:
                if s[i-j] == prev == s[i+j]:
                    tot += 1
                    j += 1
                else:
                    break
        
            count_sequence = 1  

        tot += count_sequence            
        prev = v

    return tot  

