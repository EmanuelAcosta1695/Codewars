def count_positives_sum_negatives(arr):
    
    if len(arr) == 0:
        return []  

    count = 0
    sum = 0
    for x in arr:
        if x > 0:
            count += 1
        elif x <= 0:
            sum = sum + x
        elif x == []:
            return list
    return [count, sum]

"""
Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.

If the input array is empty or null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""