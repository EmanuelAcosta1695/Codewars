def multiply(n):
    if n > 0:
        return 5 ** (len(str(n))) * n
    else:
        return 5 ** (len(str(n)) - 1) * n 

def multiply(n):
    return 5 ** (len(str(n))) * n if n > 0 else 5 ** (len(str(n)) - 1) * n

"""
Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of digits of each numbers, so, for example:

multiply(3)==15
multiply(10)==250
multiply(200)==25000
multiply(0)==0
multiply(-3)==-15
"""