#NO PUDE SOLO pero simplifique el codigo
def take(arr, n):
    return arr[:n] #recorre el array. forma mas facil. desde vacio(0) hasta n, indicado en argumento

"""
Create a method take that accepts a list/array and a number n, and returns a list/array array of the first n elements from the list/array.
"""

take=lambda a,n:a[:n]



def take(arr, n):
    return arr[range(0,n)]  #MAL. px el indice de la lista no puede ser un rango, tiene q ser un entero
