

def reverse(string):
    """ runtime complexity of this algorithm is O(n) """

    # Starting index
    start_index = 0

    # Ending index
    array = list(string)
    last_index = len(array) - 1

    while last_index > start_index:
        # Swap items
        array[start_index], array[last_index] = \
            array[last_index],  array[start_index]

        # Increment first index and decrement last index
        start_index += 1
        last_index -= 1
    return ''.join(array)

