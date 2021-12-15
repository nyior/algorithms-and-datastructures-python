"""
  Insertion sort always out performs the bubble sort and selection sort
  Insertion sort is adaptive and stable. This means if we pass it an array with
  an already sorted part, it takes that into account too.

  In this sorting algorithm, an element is compared the elements preceeding it.
  Swapping is done where necessary


  For example given an array, [1,5,2,7,0,11]
  For iteration one, we will consider 1, has no preceeding elements so we proceed to the second
  element.

  For iteration 2, we compare 5 with 1. since 5 isn't smaller, we then proceed to the next element

  For iteration 3, we compare 2 with 5 and 1. We'd end up swapping 2 with 5 and this yields, 
  [1,2,5,7,0,11]. We repeat this process until we've reached the last item


  Assumption: sort in ascending order

  Run time complexity: O(n^2)
"""


class InsertionSort():

    def __init__(self, nums) -> None:
        self.nums = nums

    def sort(self) -> None:
        for i in range(len(self.nums)):

            j=i

            while j>0 and self.nums[j-1] > self.nums[j]:
                self._swap(j-1, j)
                j -= 1

    def _swap(self, i, j) -> None:
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]



""""
    We have seen how to implement insertion sort with integers. 
    Let's use insertion sort with custom objects. Create a Person class with 2 instance 
    variables: name and age. Let's sort a list of Person objects in ascending order based on their ages.
"""

class Person:
 
    # we have 2 instance variables - name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    # we have to define the 'less than' function to let Python know how to interpret the < and > operators
    # when we use < then Python calls this function to decide what object is smaller and what is greater
    def __lt__(self, other):
        return self.age < other.age
 
    # string representation of the object (when we use the print() function then this function is called)
    def __repr__(self):
        return str(self.name)
 
 
# we can use the exact same insertion sort algorithm we have implemented
def insertion_sort(people):
 
    for i in range(len(people)):
 
        j = i
 
        while j > 0 and people[j - 1] > people[j]:
            people[j], people[j-1] = people[j-1], people[j]
            j = j - 1
 
 
if __name__ == '__main__':
 
    n = [Person('Adam', 23), Person('Ana', 17), Person('Kevin', 32), Person('Daniel', 37)]
    insertion_sort(n)
    print(n)