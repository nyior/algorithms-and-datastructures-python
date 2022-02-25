"""
    write a function called count_x
    that returns the number of “x’s” in a given string. If our function is passed
    the string, "axbxcxd", it’ll return 3, since there are three instances of the character
"""

def count_x(string):
    if len(string) == 0:
        return 0

    if string[0] == 'x':
        return 1 + count_x(string[1:])
    else:
        return count_x(string[1:])


if __name__ == '__main__':
    print(count_x("axbxcxd"))
