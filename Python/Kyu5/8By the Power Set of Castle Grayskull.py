def power(a):
    new_list = [[]]

    for x in a:
        new_list += [y + [x] for y in new_list]

    return new_list

power([1, 2, 3]) # [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

"""
Write a function that returns all of the sublists of a list/array.

Example:
power([1,2,3]); => [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

"""

