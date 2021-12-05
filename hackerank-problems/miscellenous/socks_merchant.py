"""
    There is a large pile of socks that must be paired by color. 
    Given an array of integers representing the color of each sock, 
    determine how many pairs of socks with matching colors there are.

    Example
    n = 7
    ar = [1, 2, 1, 2, 1, 2, 3]

    There is one pair of color 1 and one of color 2 . 
    There are three odd socks left, one of each color. The number of pairs is 2.
"""

def sock_merchant(n, ar):
    # Write your code here
    socks = {}
    pairs = 0
    
    for i in ar:
        if socks.get(i):
            pairs += 1
            socks.pop(i)
        else: 
            socks.update({i: i})
    return pairs