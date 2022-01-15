"""
  Selection sort always out performs the bubble sort. It is aunstable.
  Selection sort also does fewer swap operations, and by extension memory writes 
  than Bubble sort. In the  worst case, it does n-1 swap operations

  The core principle in selection is to devide the list to be sorted into the
  sorted and unsorted part. With each iteration the unsorted part is traversed and manipulated.
  This is repeated until there is no unsorted part left. How is this achieved?

  With each iteration the smallest item in the unsorted part is spoted and swapped with the
  leftmost item in the unsorted part. The smallest item put in place of the leftmost item then 
  becomes a part of the sorted part.

  The number of elements to be parsed decreases with each iteration.

  For example given an array, [1,5,2,7,0,11]
  For iteration one we will consider elements from index 0 to the last index. The smallest element
  is o so it will be swapped with 1 = [0,5,2,7,1,11]. Our sorted part is now [0] and the unsorted part is
  [5,2,7,1,11]

  For iteration 2, we again find the smallest item in the unsorted part and swap it with the leftmost item.
  This entials swapping 1 with 5. this then yields, [1,2,7,5,11]. Our sorted part is now [0, 1], and unsorted
  is [2,7,5,11]

  We will repeat the circle until we are only left with no unsorted part

  Assumption: sort in ascending order

  Run time complexity: O(n^2)
"""


class SelectionSort():

    def __init__(self, nums) -> None:
        self.nums = nums

    def sort(self) -> None:
        for i in range(len(self.nums)-1):

            index = i # index of the smallest item in the unsorted part

            for j in range(i, len(self.nums)):
                if self.nums[j] < self.nums[index]:
                    index = j

            if index != i: # To avoid swapping an element with itself
                self._swap(i, index)

    def _swap(self, i, j) -> None:
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]