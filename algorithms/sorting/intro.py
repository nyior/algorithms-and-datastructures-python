"""
    O(n^2) running time sorting algorithms: bubble sort, insertion sort, and selection sort
    O(nlogn) running time sorting algorithms: Merge sort, Quick sort
    O(n) running time sorting algorithms: bucket sort and radix sort.. They are not comparison
    based sorting algorithms.

    Quick sort and Merge could recursively implemented. Quicksort is also an in place 
    sorting algorithm because it does not require extra memory for the sorting operation

    insertion sort and merge sort are stable sorting algorithms. This means that after the sorting has
    been done, the relative order of items with equal values is preserved. so if we have two items
    with values  10 in a list to be sorted(10 at index 0, and 10 at index 3), the 10 at index 0 will
    come before the 10 at index 3: The order is preserved. this might be a bad example when sorting
    integers of equal values the order inwhich they appear doesn't really matter.

    when sorting based on multiple criteria(e.g sort users based on their names and cities) then it
    is important that we use a stable sorting algorithm. However, when sorting based on a single criterion
    then even the unstable algorithms would work just fine.
"""