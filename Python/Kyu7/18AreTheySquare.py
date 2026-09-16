import math
def is_square(arr:list):
    x = 0
    if arr == []:
        return None
    else:
        for i in arr:
            if math.sqrt(i) == round(math.sqrt(i), 1):
                x += 1
        if x == len(arr):
            return True
        else:
            return False

"""
Description:
Write a function that checks whether all elements in an array are square numbers. The function should be able to take any number of array elements.

Your function should return true if all elements in the array are square numbers and false if not.

An empty array should return undefined / None / nil /false (for C). You can assume that all array elements will be positive integers.

Examples:

is_square([1, 4, 9, 16]) --> True

is_square([3, 4, 7, 9]) --> False

is_square([]) --> None
"""
