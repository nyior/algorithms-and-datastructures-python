"""
    Construct an algorithm to check whether two words (or phrases) 
    are anagrams or not! 

    --An anagram is a word or phrase formed by rearranging the letters 
    of a different word or phrase, typically using all the original 
    letters exactly once.
"""


def is_anagram(str1, str2) :

    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True


if __name__ == "__main__":
    str1  = "fluster"
    str2 = "restfel"
    
    print(is_anagram(str1, str2))

