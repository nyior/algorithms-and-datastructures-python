"""
  The core principle in Bubble sort is to compare all adjacent elements in 
  an array and then move the biggest element to the end of the list with each iteration.
  The Bubble sort algorithm is stable

  The number of elements to be parsed decreases with each iteration.

  For example given an array, [1,5,2,7,0,11]
  For iteration one we will consider elements from index 0 to the last index. The biggest, element
  11 will be left at the end of the list since it's already there.

  For iteration 2, since we already know that the last item is the biggest element, we will only
  compare elements from index 0 to the last index - 1 =(5-1=4)

  We will repeat the circle until we are only left with the first index to look at.

  Assumption: sorting in ascending order

  Run time complexity: O(n^2)
"""

class BubbleSort():

    def __init__(self, nums) -> None:
        self.nums = nums

    def sort(self) -> None:
        for i in range(len(self.nums)-1):
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]:
                    self._swap(j, j+1)

    def _swap(self, i, j) -> None:
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]