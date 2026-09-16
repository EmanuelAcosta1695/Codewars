def multiplication_table(size):
    list2 = []
    for x in range(1,size+1):
        list1 = []
        for z in range(1, size+1):
            list1.append(x*z)
        list2.append(list1)
    return list2

"""
Your task, is to create NxN multiplication table, of size provided in parameter.

for example, when given size is 3:

1 2 3
2 4 6
3 6 9
for given example, the return value should be: [[1,2,3],[2,4,6],[3,6,9]]
"""
