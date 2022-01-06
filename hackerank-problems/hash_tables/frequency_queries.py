"""
    You are given  queries. Each query is of the form two integers described below:
-  1 x: Insert x in your data structure.
-  2 y: Delete one occurence of y from your data structure, if present.
-  3 z: Check if any integer is present whose frequency is exactly z. If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size q where queries[i][0] contains the operation, 
and  queries[i][1] contains the data element.

Example
queries = [(1,1), (2,2), (3,2), (1,1), (1,1), (2,1), (3,2)]

The results of each operation are:

    Operation   Array   Output
    (1,1)       [1]
    (2,2)       [1]
    (3,2)                   0
    (1,1)       [1,1]
    (1,1)       [1,1,1]
    (2,1)       [1,1]
    (3,2)                   1

    Return an array with the output: [0, 1].
"""

from collections import Counter, defaultdict 

def freq_query(queries):
    """
        Approach: track how the number of times each data element increases or decreases
        as you traverse the list of queries.
        We do this by having the d_to_o data structure that stores each element and the number of times they occur
        o_to_d data structure stores the reverse of d_to_O

    """
    d_to_o = Counter()
    o_to_d = defaultdict(set)
    
    for k, v in queries:
        value = d_to_o[v]
        
        if k == 1:
            o_to_d[value].discard(v)
            o_to_d[value+1].add(v)
            
            d_to_o[v] = value+1
        
        if k == 2:
            if value:
                o_to_d[value].discard(v)
                o_to_d[value-1].add(v)
                
                d_to_o[v] = value-1
                
        if k == 3:
            yield 1 if o_to_d.get(v) else 0