"""
    There is a new mobile game that starts with consecutively numbered clouds. 
    Some of the clouds are thunderheads and others are cumulus. 
    The player can jump on any cumulus cloud having a number that is equal to the number 
    of the current cloud plus 1 or 2 . 
    The player must avoid the thunderheads. 
    Determine the minimum number of jumps it will take to jump from the starting postion to the last cloud. 
    It is always possible to win the game.

    For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided.

    Example
    c = [0, 1, 0, 0, 0, 1, 0]

    Index the array from 0...6 
    The number on each cloud is its index in the list so the player must avoid the clouds at indices 1 and 5 . 
    They could follow these two paths: 0-> 2 ->4 -> 6 or 0-> 2 -> 3->4 -> 6  . 
    The first path takes 3 jumps while the second takes 4 . Return 3.
"""

def jumping_on_clouds(c):
    jumps = 0
    i = 0
    
    while i < (len(c)-1): 
        if c[i]==0:       
            if i < len(c)-2 and c[i+2] ==0:
                jumps += 1
                i += 2
                continue
                    
            if i < len(c)-2 and c[i+1] ==0 and c[i+2] !=0:
                jumps += 1
                i += 1
                
            if i == len(c)-2 and c[i+1] ==0 and c[i-1] !=0:
                    jumps += 1 
                    i += 1    
    return jumps


def jumping_on_clouds_recursive(c):
    """copied this solution directly from the discussion section on Hackerrank"""
    if len(c) == 1 : return 0
    if len(c) == 2: return 0 if c[1]==1 else 1
    if c[2]==1: 
        return 1 + jumping_on_clouds_recursive(c[1:])
    if c[2]==0:
        return 1 + jumping_on_clouds_recursive(c[2:])