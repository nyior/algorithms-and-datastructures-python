"""
    Two strings are anagrams of each other if the letters of one string can be 
    rearranged to form the other string. 
    Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

    Example
    s = 'mom'
    the list of all anagrammatic pairs is [m, m] and [mo, om]
"""
from itertools import combinations

def sherlock_anagrams1(s):
    """the approach i had in my head, but it doesn't work"""
    anagrams = {}
    count = 0
    subs = [s[x:y] for x, y in combinations(
            range(len(s) + 1), r = 2)] # Returns all the possible substrings

    for i in subs:
        if anagrams.get(str(sorted(i))):
            count += 1
        else:
            anagrams[str(sorted(i))] = i
            
    # print(f"substrings: \n {subs}")      
    return count


def sherlock_anagrams2(s):
    """copied this from hackerrank, and it works"""
    was = dict()

    n = len(s)
    for i in range(n):
        for j in range(i, n):
            cur = s[i:j + 1]
            cur = ''.join(sorted(cur))
            was[cur] = was.get(cur, 0) + 1

    ans = 0
    for x in was:
        v = was[x]
        ans += (v * (v - 1)) // 2

    return ans

if __name__ == "__main__":
    import timeit

    s = 'mom'
    print(timeit.timeit('sherlock_anagrams1(s)', globals=globals(), number=100000))
    print(timeit.timeit('sherlock_anagrams2(s)', globals=globals(), number=100000)) # More efficient

# generate all the pairs in an array
a = [1,2,3,43,4]
pairs = list(combinations(a, r=2))
pairs1 = [(i, j) for i in range(len(a)) \
                for j in range(i+1, len(a)+1)]

# generate all substrings
s = 'nyior'
subs = [s[x:y] for x, y in combinations(range(len(s)+1), r=2)]