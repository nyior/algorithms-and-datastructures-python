"""
    write a reverse function that reverses
    a string. So, if the function accepts the argument "abcde", it’ll return "edcba".

    - what is the sub-problem: arr[-1] + reverse(arr[0, -1])
"""

def reverse_string(string):
    if len(string) == 1:
        return string[-1]
    else:
        return string[-1] + reverse_string(string[0:-1])


if __name__ == '__main__':
    print(reverse_string("clement"))