def flatten_and_sort(array:list):
    lista = []
    for i in sorted(array):
        for x in i:
            lista.append(x)
    return sorted(lista)

"""
itertools — Funciones que crean iteradores para bucles eficientes
Este módulo implementa un número de piezas básicas iterator inspiradas en constructs de APL,
Haskell y SML. Cada pieza ha sido reconvertida a una forma apropiada para Python.

El módulo estandariza un conjunto base de herramientas rápidas y eficientes en memoria,
útiles por sí mismas o en combinación con otras. Juntas, forman un «álgebra de iteradores»,
haciendo posible la construcción de herramientas especializadas, sucintas y eficientes, en Python puro.

chain() -> p, q, …   ->  p0, p1, … plast, q0, q1, …  -> chain('ABC', 'DEF') --> A B C D E F
"""
