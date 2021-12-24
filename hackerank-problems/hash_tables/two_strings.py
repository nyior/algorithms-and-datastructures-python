"""
    Given two strings, determine if they share a common substring. 
    A substring may be as small as one character.

    Example
    s1='and'
    s2='art'

    These share the common substring a.

    s1='cat'
    s2='be'

    These do not share a substring.
"""

def two_strings(s1, s2):

    if set(s1).intersection(set(s2)): # If it returns something, then the two strings have common element(s)
            return "YES"
    else:   
        return "NO"
