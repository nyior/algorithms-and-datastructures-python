"""
Given 2 arrays of Strings check the total no of Anagrams found in the 
dictionary list for each String in query list.

 Eg Input : 
            dictionary -> ['heater', 'cold', 'clod', 'reheat', 'dolc']
            query -> ['codl', 'heatre', 'abcd']

Eg Output: 3 2 0

STEP 1: UNDERSTANDING THE PROBLEM
- Input: two lists: dictionary list, and a query list
- Key Operation: finding the number of anagrams each word in the query string has in the dict list
- Expected Output: a list of the number of anagrams each query entry has

STEP 2: HOW CAN I MANUALLY CARRY OUT THE KEY OPERATION
    - what is the simplest version of the problem: find the first anagram of a query entry in the 
    dictionary entry
    - How can I manually solve the simplest version above:
        - Pick each item in the query list, compare it against each item in the dict list to
        see if the item in the dict list is it's anagram
        - how do i manually find out if two words are anagrams of each other
            - do they have thesame length?
                - sort them
                - comapare each alphabet
"""

def anagrams(word1, word2):
    if len(word1) != len(word2):
        return False

    word1 = sorted(word1)
    word2 = sorted(word2)

    for i in range(len(word1)-1):
        if word1[i] != word2[i]:
            return False

    return True


def string_anagram(dic, query):
    n = len(query)
    ocr = [0 for _ in range(n)]

    counter = 0

    while counter < n:
        for i in dic:
            if anagrams(query[counter], i):
                ocr[counter] += 1

        counter += 1

    return ocr



if __name__ == '__main__':
    d = ['heater', 'cold', 'clod', 'reheat', 'dolc']
    q = ['codl', 'heatre', 'abcd']

    print(string_anagram(d, q))

# Need to revisit this problem