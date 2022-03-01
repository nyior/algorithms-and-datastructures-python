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
        string = 'ab'
    - how do I move from ab to the output 2?
        - every string has one anagram by default-- itself
        - swap the two elements to get the second anagram
        - 'abc'

    pseudocode

        - def all_anagrams(string)
                all_anagrams = []
                anagrams = all_anagrams(string[1:])

                if len(string) == 0:
                    return

                if len(string) == 1:
                    return string[0]

                for a in anagrams
                    for index in len(a)
                        new_anagram = insert_string[0]_at_index
                        all_anagrams.append(new_anagram)

                return all_anagrams


"""

def all_anagrams(string):
    if len(string) == 0:
        return

    if len(string) == 1:
        return string[0]

    words = []
    anagrams = all_anagrams(string[1:])

    for a in anagrams:
        for index in range(len(a)):
            a_copy = a
            new_anagram = a[:index] + string[0] + a[index:]
            words.append(new_anagram)

    return words


if __name__ == '__main__':
    print(all_anagrams('nyior'))