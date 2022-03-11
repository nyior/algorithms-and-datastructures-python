"""
    Have the function MathChallenge(num) take the num parameter 
    being passed and return the next number greater than num using the same digits. 
    For example: if num is 123 return 132, if it's 12453 return 12534. 
    If a number has no greater permutations, return -1 (ie. 999).
"""

"""
    input: an integer
    output: the next number greater than num. The number has to be 
    formed from the same integers in the original given num

    example:
    123 -> 132
    1234 -> 1243
    12345 -> 12354
    123456 -> 123465
    4321 ->  -1
    2222 - -1
    12453 -> 12534

    KEY operation:
    - Given an integer, how can it be re-arranged to the
    next biggest integer?

    SIMPLEST VERSION:
    1 -> 1
    12 -> 21
    21
    123 - 132
    412 
"""

def PermutationsStep(num):
    string = str(num)
    n = len(string)

    if n == 1:
        return -1

    for i in range(n-2, -1, -1):
        if string[i] < string[i+1]:
            return int(string[:i] + string[i+1: ] + string[i])

    return -1


print(PermutationsStep(11121))