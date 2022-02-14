"""
    There aren't real arrays natively built into Python.
    The closest data structure to arrays in Python are called lists.
    Python lists could store items of different types.

    Generally, each item in an array is associated with an index. 
    it has a random access feature(
        just specify an index, and you get the element at that index
    ).

    Arrays are perfect for operations that usually involve adding or removing
    an item from the end of the array. it's also good for retrieving items
    from an index. these operations have 0(1) runtime complexity.

    It's not so good for operations that require removing or inserting items
    at arbitrary locations in the array. These types of operations have 0(n)
    time complexity.

    resizing arrays too is a costly operation. This is because array sizes are
    not dynamic. When an array is declared it is being assigned a specific size
    implicitly if not explicitly done. Once that size is exceeded, the system 
    resizes the array by creating a new array that's double the size of the existing 
    array and it then pushes all the items into the new array.
"""
# Initializing an array
numbers = [1, 2, 3, 4, 5]

# Retrieving the first item
first_item = numbers[0]

# Retrieving the last item
last_item = numbers[-1]  # numbers[4]

# Retrieve items within a range
second_to_fourth_items = numbers[1:4] # Last item excluded
all_items = numbers[:]  # Or numbers[0:]

# Update the item at a specified index
numbers[0] = "Nyior"
