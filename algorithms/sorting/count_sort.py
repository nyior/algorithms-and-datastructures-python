"""
    The count sort is a non-comparison based sorting algorithm:
    In other words, it sorts items in a list without having to compare them.
    The counting sort algorithm only works with integers.
    It sorts the integers in an array by creating a second array based on the range of
    values in the original array(max-min). Initially it populates the second array with 0s.
    It then counts the number of occcurence of each item in the original array. It then updates
    that value in the second array.
"""

class CountSort(object):

    def __init__(self, data):
        self.data = data
        self.count_array = [0 for _ in range((max(data)-min(data))+1)]


    # First we count all the items in data and the number of times they occur
    # Indexes start from 0 + we have to consider negative indexes as well
    for i in range(len(self.data)):
        self.count_array[self.data[i]-min(self.data)] += 1

    # Now consider the counting array: see how many times an entry occurs
    z=0
    for i in range(min(self.data), max(self.data)+1):
        while self.count_array[i-min(self.data)] > 0:
            self.data[z] = i
            z += 1

            self.count_array[i-min(self.data)] -= 1