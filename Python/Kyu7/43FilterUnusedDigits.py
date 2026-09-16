def unused_digits(*a):
    return ("".join(str(x) for x in range(0, 10) if str(x) not in "".join(str(x) for x in a)))

"""
Given a varying number of integer arguments, return the digits that are not present in any of them.

Example:

[12, 34, 56, 78]  =>  "09"
[2015, 8, 26]     =>  "3479"
Note: the digits in the resulting string should be sorted.
"""
