"""
    Our task is to design an efficient algorithm to reverse 
    a given integer.

    For example if the input of the algorithm is 1234 then the 
    output should be 4321
"""


def reverse_integer(integer):
    """ runtime complexity of this algorithm is O(n) """

    reversed = 0

    # Pop the last digit of the integer after each iteration
    # Then update the value of the integer
    while integer > 0 :
        remainder = integer % 10
        reversed = reversed*10 + remainder

        integer = integer // 10

    return reversed


if __name__ == "__main__":
    print(reverse_integer(12345))
