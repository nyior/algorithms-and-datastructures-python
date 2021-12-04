def find_repetition(array):
    items = {}

    for item in array:

        try:

            if items[item]:
                print(f"{item} is repeated")
        except KeyError:
             items[item] = item

    return items


def find_unique_pairs(array):
    pairs = []

    for i in array:
        for j in array:
            pairs.append((i, j))
    print(pairs)

def boundedRatio(a, l, r):
    bool_arr = []
    
    for i in range(len(a)):
        num = a[i]
        x = num/(i + 1)
        print(x)
        if x%1<=0 and x >= l and x <= r:
            bool_arr.append(True)
        else:   
            bool_arr.append(False)

    print(bool_arr)

if __name__ == "__main__":
    a = [8, 5, 6, 16, 5] 
    l = 1
    r=3

    boundedRatio(a, l, r)