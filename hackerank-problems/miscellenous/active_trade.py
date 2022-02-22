"""
    Given a list of String representing the trades of customers, 
    return a list of customers who made at least 5% of the total sales in a sorted order.

    e.g ['alpha', 'beta', 'omega', 'omega', 'alpha' ]

    key op: find entries that constitute more than 5% of the total sales

    input: a list of names. With each name repsenting a sale made by the name owner
    output: a list of names of traders that had made at least 5% of the total sales


    step 2: Simplest version of the problem
    - what is the simplest version of the key op: compute the % of sales of each entry
    - How can I manually find the % of sales of each list entry?
        - find the total number of times each entry occurs
            - declare an empty dictionary
            -
        - percentage sales = num of occurences/total num of entries * 100
"""
from collections import Counter

def active_trade(arr):
    counter = Counter(arr)
    print(counter)
    result = []
    n = len(arr)

    # Compute percentage sales
    for key, value in counter.items():
        perc = (value/n) * 100
        if perc >= 5:
            print(f"{key}: {perc}")
            result.append(key)

    return sorted(result)


if __name__ == '__main__':
    arr = ['alpha', 'beta', 'omega', 'omega', 'alpha' ]
    print(active_trade(arr))