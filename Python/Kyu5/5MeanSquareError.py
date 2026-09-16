import re

def solution(array_a, array_b):
    list_num = []

    for x, y in zip(array_a, array_b):
        list_num.append(abs((x)-(y))**2)

    string = str(sum(list_num)/len(array_a))
  
    if bool(re.compile(r'^[0-9]+(\.[0]{1})$').search(string)) == True:
        return int(float(string))

    return float(string)


a1 = [1,2,3] # 9
a2 = [4,5,6]

# 853573.28125
# a1 = [-768, -17, 143, 201, 98, -462, -890, -585, -356, -129, 299, 773, -996, 505, 384, 561, -221, -926, -836, -659, 880, -425, 425, 154, -71, -493, -752, 762, 125, 158, 51, -914]
# a2 = [366, 23, -426, -302, -436, 672, 110, 863, -965, -355, -875, -914, -462, -126, 907, -52, 454, 916, 990, -729, 67, 190, 81, 324, 397, -85, 798, 881, 561, 846, 932, 565]

solution(a1, a2) 

# b1 = [10, 20, 10, 2]
# b2 = [10, 25, 5, -2]

# solution(b1, b2)# 1.5 #16.5?  

# c1 = [0, -1]
# c2 = [-1, 0]

# solution(c1, c2)# 1

# d1 = [10, 10]
# d2 = [10, 10]

# solution(d1, d2)# 0

"""
Complete the function that

accepts two integer arrays of equal length
compares the value each member in one array to the corresponding member in the other
squares the absolute value difference between those two values
and returns the average of those squared absolute value difference between each member pair.

Examples
[1, 2, 3], [4, 5, 6]              -->   9   because (9 + 9 + 9) / 3
[10, 20, 10, 2], [10, 25, 5, -2]  -->  16.5 because (0 + 25 + 25 + 16) / 4
[-1, 0], [0, -1]                  -->   1   because (1 + 1) / 2
"""