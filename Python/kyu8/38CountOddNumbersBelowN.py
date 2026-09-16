import numpy as np
def odd_count(n):
    return len(np.array([x for x in range(1,n,2)]))

#TARDA MUCHO CON MATRICES

#MEJOR
def odd_count(n):
    return n//2


odd_count(7) #3
#odd_count(15)#7
#odd_count(15023)#7511

"""
Given a number n, return the number of positive odd numbers below n, EASY!

oddCount(7) //=> 3, i.e [1, 3, 5]
oddCount(15) //=> 7, i.e [1, 3, 5, 7, 9, 11, 13]
"""

