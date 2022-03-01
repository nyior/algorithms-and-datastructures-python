"""
    Use recursion to write a function that accepts an array of strings and
    returns the total number of characters across all the strings. For example,
    if the input array is ["ab", "c", "def", "ghij"], the output should be 10 since there
    are 10 characters in total.

    sub-problem: arr[1:] 
    base case: when length of string is 1 then return 1. when length of string is 0 return 0
"""

def total_length(arr):
    if len(arr) == 1:
        return len(arr[0])
    
    elif len(arr) == 0:
        return 0

    else:
        return len(arr[0]) + total_length(arr[1:])


if __name__ == '__main__':
    print(total_length(['you', 'go', 'more', 'car']))

    