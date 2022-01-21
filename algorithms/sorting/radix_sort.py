"""
Counting sort becomes really inefficient when the difference between
the minimum and maximum item in a list is significantly greater than
the mximum item in the list. In such situations we actually could
end up with a running time complexity that surpases the quadratic running time.

The radix sort algorithm exists to solve this problem. It is stable.
Using the Least significant data approach, we use the counting sort as subroutine
to sort the integer items in a least by first sorting the right-most item of each 
integer in the least and then moving to the left.
"""
ITEMS_IN_BUCKET = 10

class RadixSort:

    def __init__(self, data):
        self.data = data

    def get_digits(self):
        return len(str(max(self.data)))

    def sort(self):
        for digit in range(self.get_digits()):
            self.counting_sort(digit)

    def counting_sort(self, d):
        count_array = [[] for _ in range(ITEMS_IN_BUCKET) ]

        # Store the count of  each element in count array
        for num in self.data:
            # Calculate the index of the given bucket
            index = (num//(10**d)) % 10
            count_array[index].append(num)

        # We have to consider all the items in the count array
        z = 0
        for in in range(len(count_array)):
            while len(count_array[i]) > 0:
                # it takes 0(N) linear running time complexity. So we could use a dictionary here
                self.data[z] = count_array[i].pop(0)
                z += 1