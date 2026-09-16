"""
You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.

Array can contain numbers or strings. X can be either.

Return true if the array contains the value, false if not.
"""

def check(seq, elem):
    list1 = list(seq)
    if elem in list1: 
        return True
    else:
        return False

#SOLUCION SIMPLIFICADA
def check(seq, elem):
    return True if elem in seq else False


"""
SOLUCION MAS SIMPLE

def check(seq, elem):
    return elem in seq 
"""