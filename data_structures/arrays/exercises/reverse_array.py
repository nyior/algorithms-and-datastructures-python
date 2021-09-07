"""
    The problem is that we want to reverse a T[] array in O(N) 
    linear time complexity and we want the algorithm to be in-place 
    as well - so no additional memory can be used!

    For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]
"""

def reverse_array(array):
    """ runtime complexity of this algorithm is O(n) """

    # Starting index
    start_index = 0

    # Ending index
    last_index = len(array) - 1

    while last_index > start_index:
        # Swap items
        array[start_index], array[last_index] = \
            array[last_index],  array[start_index]

        # Increment first index and decrement last index
        start_index += 1
        last_index -= 1


if __name__ == "__main__":
    numbers = [-3,0,3]
    name = "nyior"
    # reverse_array(name)
    name[0] = "M"
    print(name)