def array_diff(a: list, b: list):
    copy_list = []
    if len(a) == 0:
        return a
    copy_list = a.copy()
    for x in a:
        for y in b:
            if x == y:
                if y in copy_list:
                    copy_list.remove(y)
    return copy_list

"""

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.

array_diff([1,2],[1]) == [2]
If a value is present in b, all of its occurrences must be removed from the other:

array_diff([1,2,2,2,3],[2]) == [1,3]
"""
