def double_every_other(lst):
    i = 0
    list = []
    for x in lst:
        if i%2 == 0:
            list.append(x)
        else:
            list.append(x*2)
        i += 1
    return list

"""
Write a function that doubles every second integer in a list starting from the left.

Example:

  double_every_other([1,2,3,4]) # -> [1, 4, 3, 8]
"""
