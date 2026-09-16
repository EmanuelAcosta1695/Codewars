def square_or_square_root(arr):
    list = []
    for x in arr:
        z = x**(0.5)
        if z == round(z, 1):
            list.append(int(z))
        else:
            list.append(pow(x, 2))

    return list
square_or_square_root([4, 3, 9, 7, 2, 1 ]) #[2, 9, 3, 49, 4, 1]

def square_or_square_root(arr):
    return [int(x**(0.5)) if x**(0.5) == round(x**(0.5), 1) else pow(x, 2) for x in arr]

square_or_square_root([4, 3, 9, 7, 2, 1 ]) #[2, 9, 3, 49, 4, 1]

"""
Write a method, that will get an integer array as parameter and will process every number from this array.

Return a new array with processing every number of the input-array like this:

If the number has an integer square root, take this, otherwise square the number.

Example
[4,3,9,7,2,1] -> [2,9,3,49,4,1]
Notes
The input array will always contain only positive numbers, and will never be empty or null.
"""

