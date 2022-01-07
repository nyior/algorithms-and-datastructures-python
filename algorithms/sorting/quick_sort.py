"""
    The quicksort is a comparison based sorting algorithm that's based 
    on the devide and conquer approach to problem solving.
    Given a list of items, the quicksort algorithm sorts it by first of all
    deviding the list into two sub-lists: left and right lists. It does this
    by generating a pivot value. All the items in the left sublist must be less
    than the pivot value, and all the other items will go the right sub-list. The pivot
    value will always be in its sorted position.

    The quicksort algorithm has an average runtime complexity of O(NlogN), and a worse case runtime
    complexity of O(n**2).
"""

class Quicksort(object):

    def __init__(self, data) -> None:
        self.data = data

    def sort(self):
        self._quick_sort(0, len(self.data)-1)

    # Low is the index of the first element
    # High is the index of the last item
    def _quick_sort(self, low, high):
        if low >= high:
            return

        pivot_index = self._partion(low, high)

        # Call the function recursively on the left sub-array
        self._quick_sort(low, pivot_index-1) # Exclude the pivot element coz it's sorted
        # Call the function recursively on the right sub-array
        self._quick_sort(pivot_index+1, high)

    def _partition(self, low, high):
        pivot_index = (low + high)//2

        # Swap pivot with last item
        self.data[pivot_index], self.data[high] = self.data[high], self.data[pivot_index]

        for j in range(low, high):
            if self.data[j] < self.data[high]:
                self.data[j], self.data[low] = self.data[low], self.data[j]
                low += 1
        self.data[low], self.data[high] = self.data[high], self.data[low]

        # Return index of the pivot
        return low