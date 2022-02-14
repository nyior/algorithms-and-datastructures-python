"""
    This is a simple utility for getting all the substrings in a string
"""
from itertools import combinations, combinations_with_replacement

test_str = 'nyior'
res = [test_str[x:y] for x, y in combinations(
            range(len(test_str) + 1), r = 2)]