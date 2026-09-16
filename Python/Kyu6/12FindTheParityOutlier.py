def find_outlier(integers):
    list1 = []
    list2 = []
    for x in integers:
        if x%2 == 0:
            list1.append(x)
        else:
            list2.append(x)
    return list1[0] if len(list1) == 1 else list2[0]

"""
You are given an array (which will have a length of at least 3, but could be very large) containing integers.
The array is either  entirely comprised of odd integers or entirely comprised of even integers except for a
single integer N. Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""
