def count_inversions(data): 
    if len(data) == 1:
        return

    midpoint = len(data)//2
    left_subarray = data[:midpoint]
    right_subarray = data[midpoint:]

    # Recursively split the array to smaller arrays
    countInversions(left_subarray)
    countInversions(right_subarray)

    i, j, k, count = 0, 0, 0, 0
    
    left_length = len(left_subarray)
    right_length = len(right_subarray)
    
    while i < left_length and j < right_length:
        item_1 = left_subarray[i]
        item_2 = right_subarray[j]
        
        if item_1 <= item_2:
            data[k] = item_1
            i += 1

        else:
            data[k] = item_2
            j += 1
            count += (left_length - i)
        k += 1

    # If there are still items in the left subarray
    while i < left_length:
        data[k] = left_subarray[i]
        i += 1
        k += 1

    # If there are still items in the rightt subarray
    while j < right_length:
        data[k] = right_subarray[j]
        j += 1
        k += 1

    return count

# Test cases on hackerrank not passing