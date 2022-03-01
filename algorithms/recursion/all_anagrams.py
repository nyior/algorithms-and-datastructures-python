"""
    write a function that returns an array of all anagrams of a
    given string. An anagram is a reordering of all the characters within a string.
    For example, the anagrams of "abc" are:

    ["abc", "acb", "bac", "bca", "cab", "cba"]

    input: a string
    Key ops:
        - Generate all the possible anagrams/re-orderings of the given string
    output:
        - A list of all the generated anagrams

    simplest version of the problem:
        - re-order a given string
             - swap the elements at any two indexes
        - bigger problem solution: generate all the possible pairs of indexes, and swap
        the elements at the indexes.
            - generate all the possible pairs of numbers between 0..n
            - Get only the unique pairs
            - swap the indexes represented by each pair
"""