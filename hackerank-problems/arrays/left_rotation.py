""""
    A left rotation operation on an array shifts each of the arrays elements  unit to the left. 
    For example, if  2 left rotations are performed on array, [1,2,3,4,5] then the array would become [3,4,5,1,2]. 
    Note that the lowest index item moves to the highest index in a rotation. 
    This is called a circular array.

    Given an array a of n integers and a number, d, perform  left rotations on the array. 
    Return the updated array to be printed as a single line of space-separated integers.
"""

def rotLeft(a, d):
    return a[d:]+a[:d]

    # NB: x left rotations = len(a)-x right roations
    # e.g in a array with 5 elems, performing 2 left roations = performing 3 right rotations