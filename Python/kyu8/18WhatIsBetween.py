"""
Description:
Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

For example:

a = 1
b = 4
--> [1, 2, 3, 4]
"""


#SEGUNDO SOLUCION QUE SE ME OCURRIO SIMPLIFICADA
def between(a,b):
  return list(i + 1 for i in range(a-1, b))  #Itero con el range
#lo que hago es iterar a traves de un range, los valores en a-1 (asi incluye el valor de a) hasta alcanzar el valor de b y eso hace q por tieracion, i sume 1. i arranca teniendo el valor de a-1

#PRIMER SOLUCION QUE SE ME OCURRIOR
def between(a,b):
    list1 = []
    i = a
    list1.append(i)
    while i < b:
        i += 1
        list1.append(i)
    return list1