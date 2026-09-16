def fibonacci(n):
    list = []
    for x in range(n):
        if x == 0:
            list.append(x)
        elif x == 1:
            list.append(x)
        else:
            z = list[-1] + list[-2]
            list.append(z)
    return list

"""
Description:
The function 'fibonacci' should return an array of fibonacci numbers. The function takes a number
as an argument to decide how many no. of elements to produce. If the argument is less than or equal
to 0 then return empty array

Example:

fibonacci(4) # should return  [0,1,1,2]
fibonacci(-1) # should return []
"""
