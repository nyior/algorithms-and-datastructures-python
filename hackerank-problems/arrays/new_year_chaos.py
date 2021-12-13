"""
    It is New Year's Day and people are in line for the Wonderland rollercoaster ride. 
    Each person wears a sticker indicating their initial position in the queue from 1 to n. 
    Any person can bribe the person directly in front of them to swap positions, 
    but they still wear their original sticker. One person can bribe at most two others.

    Determine the minimum number of bribes that took place to get to a given queue order. 
    Print the number of bribes, or, if anyone has bribed more than two people, print Too chaotic.

    Example
    q = [1,2,3,5,4,6,7,8]

    If person 5 bribes person 4, the queue will look like this: 1,2,3,5,4,6,7,8. Only 1 bribe is required. 
    Print 1.

    q = [4,1,2,3]
    Person 4 had to bribe 3 people to get to the current position. Print Too chaotic.
"""

def minimum_bribes(q): # This solution is grossly inefficient O(n**2)
    bribes = 0

    for i in range(len(q)-1):
        if (q[i] - (i+1)) > 2:
            print("Too chaotic")
            return
        
    for i in range(len(q)-1):
        for j in range(len(q)-1):
            if q[j] > q[j+1]:
                q[j], q[j+1]  = q[j+1], q[j]
                bribes += 1
                
    print(bribes)


# saw this optimal solution on hackerrank. O(n)
def minimumBribes(q):
    totalBribes = 0
    
    expectedFirst = 1
    expectedSecond = 2
    expectedThird = 3
    
    for i in range(len(q)-1):
        if q[i] == expectedFirst:
            expectedFirst = expectedSecond
            expectedSecond = expectedThird
            expectedThird += 1
        elif q[i] == expectedSecond:
            totalBribes += 1
            expectedSecond = expectedThird
            expectedThird += 1
        elif q[i] == expectedThird:
            totalBribes += 2
            expectedThird += 1
        else:
            print("Too chaotic")
            return
    
    print(totalBribes)