"""
    Harold is a kidnapper who wrote a ransom note, but now he is worried it will 
    be traced back to him through his handwriting. 
    He found a magazine and wants to know if he can cut out whole words from it 
    and use them to create an untraceable replica of his ransom note. 
    The words in his note are case-sensitive and he must use only whole words available in the magazine. 
    He cannot use substrings or concatenation to create the words he needs.

    Given the words in the magazine and the words in the ransom note, 
    print Yes if he can replicate his ransom note exactly using whole words from the magazine; 
    otherwise, print No.

    Example
    magazine = "attack at dawn"  note= "Attack at dawn"

    The magazine has all the right words, but there is a case mismatch. The answer is No.
"""
from collections import Counter

def check_magazine(magazine, note):
    mag = Counter(magazine) # This creates a dict containing elements in mag.. and the number of times they occur
    note = Counter(note)
    
    if note - mag == {}:
        print("Yes")
    else: 
        print("No")