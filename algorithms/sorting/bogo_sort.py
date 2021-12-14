"""
    This sorting algorithm keeps generating all the possible permutations
    of the list it is passed until it finds the sorted version of that list.

    it has a running time complexity of O(n!). It is the most inefficient
    sorting algorithm. But when executed on a quantum computer, it has one of the 
    run time.
"""
import random


class BogoSort():

    def __init__(self, nums) -> None:
        self.nums = nums

    def sort(self) -> None:
        while not self._is_sorted:
            self._shufle() # keep generating permutations until it's sorted

    # Fisher Yates Shuffle Algorithm
    def _shufle(self):
        for i in range(len(self.num)-2, 0, -1): # Start from the end
            j = random.randint(0, i+1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i] # Swap

    def _is_sorted(self) -> bool:
        for i in range(len(self.nums)-1):
            if self.nums[i] > self.nums[i+1]:
                return False
        return True