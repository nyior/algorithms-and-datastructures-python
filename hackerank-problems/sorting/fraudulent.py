"""
HackerLand National Bank has a simple policy for warning clients about possible fraudulent account activity. 
If the amount spent by a client on a particular day is 2X greater than or equal to  
the client's median spending for a trailing number of days, they send the client 
a notification about potential fraud. The bank doesn't send the client any notifications 
until they have at least that trailing number of prior days' transaction data.

Given the number of trailing days  d and a client's total daily expenditures for a period of n days, 
determine the number of times the client will receive a notification over all n days.
"""
from bisect import insort, bisect_left

# Solution 1: copied from hackerrank
def activityNotifications(arr, d):
    noti = 0
    n = len(arr)

    lastd = sorted(arr[:d])
    def med():
        return lastd[d//2] if d % 2 == 1 else ((lastd[d//2] + lastd[d//2-1])/2)

    for i in range(d, n):
        if arr[i] >= 2*med():
            noti += 1
        del lastd[bisect_left(lastd, arr[i-d])]
        insort_left(lastd, arr[i])
    return noti

# TODO: How to find the running median using bisectleft and insortleft in Python
# How to find running median using heaps
# How to find median with counting sort
# The running median is the median in a list after each iteration