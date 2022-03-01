"""
    Let’s say we have a staircase of N steps, and a person has the ability to climb
    one, two, or three steps at a time. How many different possible “paths” can
    someone take to reach the top? Write a function that will calculate this for N
    steps.

    Input: an integer n
    key operation: in what different ways can we count from 0 - n, provided we can skip
    1, 2, or three numbers at a time
    output: an integer representing the number of ways we can count from 0 to n

    how to manually perform the key operation
    - simplest version of the problem: when n = 2

    sub-problem:
"""

def staircase(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4

    return staircase(n-1) + staircase(n-2) + staircase(n-3)


if __name__ == '__main__':
    print(staircase(4))