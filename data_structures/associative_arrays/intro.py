"""
    The problem we've noticed with arrays and Linked list is the fact that
    if we want to access items at arbitrary location(lookup), the operation has an O(n)
    running time complexity.

    In BST, AVL, and Red Black Trees we've reduced the running time of finding
    items at arbitrary locations to O(LogN). This is great improvement, but can
    we even reduce this to O(1) ?

    Yes. Enter Associative Arrays(Maps or Dictionaries). Here, items are stored
    as key-value pairs. Associative arrays are ADT usually built on top of a 
    one-dimensional array(hash table) or a binary search tree. The idea is to 
    combine the random access feature of BST with hash functions and reduce the
    running time of accessing items at arbitrary locations to O(1). Most operations(
        adding items, removing items, lookups
    ) could be completed in O(1) running time with associative arrays.

    However, associative arrays are usually unordered and do not support sorting

    In Python, hash tables come built in as dictionaries
"""