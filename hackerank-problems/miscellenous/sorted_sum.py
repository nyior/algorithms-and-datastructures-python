"""
input: array of integers

key operation on array: 
    - find all the consecutive sequences
    - sort the numbers in the sequence in ascending order
    - find the product of each number in the sequence by its index
    - sum up the products

Expected output: return the sum of sums % (10**9 *7)
sample input: [2, 1, 3]
sequence 1: 2, sum =2
sequence 2: 1, 2. sum = 1*1 + 2* 2 = 5
sequence 3: 1, 2, 3. sum = 1*1 + 2*2 + 3*3 = 14

answer = 21

How can I manually solve this problem:
- what is the simplest version of the problem
    - how do I find all the sequences in an array
        - for i in arr: sequence = sorted(arr[0: i+1]). store sequence in an array of sequences
    - for seq in sequences:
        sum = 0
        for i in seq:
            sum += (index*i)
        add sum to total_sum

    toal_sum%(number)
"""

def sorted_sum(arr):
    total_sum = 0
    seq = None

    for i in range(len(arr)):
        seq = arr[0:i+1] # Index out of range will be thrown here

        if len(seq) > 1:
            seq = sorted(seq)
        
        sum = 0
        for i in range(len(seq)):
            sum += ((i+1) * seq[i])
            
        total_sum += sum

    return total_sum % (10**9 * 7)


if __name__ == '__main__':
    print(sorted_sum([4, 3, 2, 1]))