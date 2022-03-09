"""
from itertools import combinations, combinations_with_replacement

test_str = 'nyior'
res = [test_str[x:y] for x, y in combinations(
            range(len(test_str) + 1), r = 2)]


Define a function that returns all the substrings of a string

INPUT: a string e.g 'ab'
OUTPUT: returns a list containing all the substrings of the input string: ['ab', 'a', 'b']


KEY OPERATION: Fiding all the possible combinations of the characters in a string
SIMPLEST VERSION: string of length 2

SOLVING THE SIMPLEST VERSION MANUALLY
str = 'ab'
str[0]
str[0-1]
str[1]

str = 'abc'
str[0]
str[0-1]
str[0-2]
str[1]
str[1-2]
str[2]

str = 'abcd'
str[0]
str[0-1]
str[0-2]
str[0-3]
str[1]
str[1-2]
str[1-3]
str[2]
str[2-3]
str[3]

PSEUDOCODE
subs = ['a', 'ab', 'abc ]

str = 'abc'

- for i in str.length:
    subs << arr[i]

    - for j in str.length
        if i != j:
            subs << arr[i:j+1]

"""
def all_subs(string):
    subs = []
    n = len(string)

    for i in range(n):
        for j in range(i, n):
            print(i, j+1)
            subs.append(string[i:j+1])


    return subs

from itertools import combinations
def all_subs_alternative(string):
    # Generate all pairs of indexes
    subs = []
    indexes = combinations(range(len(string)+1), r=2)

    for x, y in indexes:
        subs.append(string[x:y])

    return subs


def all_subs_recursive(string):
    """
        sub-problem: 
        all_subs_recursive([string[1:]])
    """
    if len(string) == 1:
        return string[0]

    new_subs = []
    subs = all_subs_recursive(string[1:])

    new_subs.append(string[0])
    for sub in subs:
        new_subs.append(string[0] + sub)

    return new_subs


if __name__ == '__main__':
    print(all_subs_recursive('dabc'))
