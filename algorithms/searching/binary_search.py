ordered_list = [3, 4, 5, 6, 10, 30, 50, 100, 200, 250, 500, 10000, 200000]

def binary_search(array, value):
    lower_bound = 0
    upper_bound = len(array)-1
    steps = 1

    while lower_bound <= upper_bound:
        midpoint = (lower_bound+upper_bound)//2
        mid_elem = array[midpoint]

        if value == mid_elem:
            print(f"steps: {steps}\n index: {midpoint}")
            return mid_elem

        if value < mid_elem:
            steps += 1
            upper_bound = midpoint-1

        if value > mid_elem:
            steps += 1
            lower_bound = midpoint+1



unorderable_list = [100, 2, 50, 0, 5, 1, 11, 10, 3, 4, 60, 20]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        index = i

        while index>0 and arr[index]<arr[index-1]:
            arr[index], arr[index-1] = arr[index-1], arr[index]
            index -= 1
    print(arr)


if __name__ == '__main__':
    # binary_search(ordered_list, 100)
    insertion_sort(unorderable_list)