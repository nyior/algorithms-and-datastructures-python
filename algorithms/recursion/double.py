"""double each entry in a given array recursively"""


def double_entries(arr, index=0):
    if index >= len(arr):
        return arr

    else:
        arr[index] = arr[index]*2
        return(double_entries(arr, index+1))


if __name__ == '__main__':
    a = [1,2,3,4,5]
    print(double_entries(a))
    