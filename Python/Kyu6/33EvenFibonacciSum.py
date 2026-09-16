def even_fib(m):
    fn1 = 0
    fn2 = 1
    sum = 0
    if m == 0:
        return sum
    for x in range(m+1):
        fn = fn1 + fn2
        if fn >= m: return sum
        if fn % 2 == 0: sum += fn
        fn1, fn2 = fn, fn1

"""
Proporcione la suma de todos los números pares en una secuencia de Fibonacci hasta el número pasado a su función, pero sin incluirlo.

O, en otras palabras, suma todos los números pares de Fibonacci que son menores que el número n dado (n no es el elemento n de la secuencia de Fibonacci) sin incluir n.

La secuencia de Fibonacci es una serie de números donde el siguiente valor es la suma de los dos valores anteriores.

La serie comienza con 0 y 1: 0 1 1 2 3 5 8 13 21...

Por ejemplo:
eve_fib(0)==0
Eva_fib(33)==10
eve_fib(25997544)==19544084
"""
