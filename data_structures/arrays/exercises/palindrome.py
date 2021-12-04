"""
    A palindrome is a string that reads the same forward and backward.

    For example: radar or madam.

    Our task is to design an optimal algorithm for checking whether
    a given string is palindrome or not! 
"""
from .reverse_string import reverse


def is_palindrome(string):
    """ runtime complexity of this algorithm is O(n) """
    
    reversed_string = reverse(string)

    if string == reversed_string:
        return True
    return False


def palindrome_pythonic(string):

    if string == string[::-1]:
        return True
    return False


if __name__ == "__main__":
    
    print(is_palindrome("racar"))