def move_zeros(lst: list):

    pos = 0

    for x in lst:
        if x == 0:
            pos = lst.index(x)
            lst.pop(pos)
            lst.append(0)

    return lst


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])# [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
# move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]), # [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# move_zeros([0, 0]) # [0, 0]
# move_zeros([0]) # [0]
# move_zeros([]) # []

"""
Write an algorithm that takes an array and moves all of the zeros to the end, 
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""