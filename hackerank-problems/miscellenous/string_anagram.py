"""
Given 2 arrays of Strings check the total no of Anagrams found in the 
dictionary list for each String in query list.

 Eg Input : 
            dictionary -> ['heater', 'cold', 'clod', 'reheat', 'dolc']
            query -> ['codl', 'heatre', 'abcd']

Eg Output: 3 2 0

STEP-1: UNDERSTANDING THE PROBLEM
- inputs: two arrays each containing strings
- key operation: for each word in the query array, find all its anagrams in the dict array
- expected output: a list of numbers, with each number representing the number of anagrams
a query entry has.

STEP-2: MANUALLY SOLVING THE PROBLEM
- simplest version of the problem: checking if two words are anagrams
- how do I manually check if two words are anagrams? e.g came   maec
    - if they're of different lengths then they're not anagrams
    - Else:
        - pick each alphabet in the first word and see if it exists in the second word

- Scale simplest version to the given problem:
    - How do I manually check the number of anagrams that a word has in a given list
        - declare a counter
        - compare each word in the list with the given word, each time an anagram is found
        increment counter
        - how do i track for multiple words?
            - have an array of results push counter into the array at the end of every pass
            and reset counter

        - Is there a pattern? 
            - None spotted


STEP-4: PSEUDOCODE
Eg Input : 
        dictionary -> ['heater', 'cold', 'clod', 'reheat', 'dolc']
        query -> ['codl', 'heatre', 'abcd']

    - set counter to 0
    - declare empty list result
    - while i < len(query)
        for j in dictionory
            if j is_anagram_of query[i]
                counter + = 1

            result.append(counter)
            counter = 0

time complexity = m * n * 

"""
from collections import Counter
    
def string_anagram(dic, query):
    dic = [sorted(i) for i in dic]
    print(f"dic list: {dic}")
    dic = Counter(dic)

    query = [sorted(i) for i in query]

    ans = []

    for i in query:
        ocr = dic.get(i, 0)
        ans.append(ocr)

    return ans


if __name__ == '__main__':
    d = ['heater', 'cold', 'clod', 'reheat', 'dolc']
    q = ['codl', 'heatre', 'abcd']

    print(string_anagram(d, q))

# Need to revisit this problem