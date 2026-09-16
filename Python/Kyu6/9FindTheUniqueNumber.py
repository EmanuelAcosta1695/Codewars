def find_uniq(arr):
    for x in range(len(arr)-1):
        if arr[x] != arr[x+1] and arr[x] != arr[x-1]:
            return arr[x]
        elif arr[x] != arr[x-1] and arr[x-2] in arr and arr[x] != arr[x-2]:
            return arr[x]
        elif arr[x] != arr[x+1] and arr[x+2] in arr and arr[x] != arr[x+2]:
            return x

"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""
