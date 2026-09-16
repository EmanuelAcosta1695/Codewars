def solution(number):
    return sum([x for x in range(1, number) if x%3 == 0 or x%5 == 0])

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.

------------------------

Si enumeramos todos los números naturales debajo de 10 que son múltiplos de 3 o 5, obtenemos 3, 5, 6 y 9.
La suma de estos múltiplos es 23.

Termina la solución para que devuelva la suma de todos los múltiplos de 3 o 5 por debajo del número pasado.
Además, si el número es negativo, devuelve 0 (para los idiomas que los tienen).

Nota: si el número es un múltiplo de 3 y 5, solo cuéntelo una vez.

-------------------------
¿Cómo saber si un número es múltiplo de 3? Para saber si un número es múltiplo de 3, la mejor manera es dividir el número entre 3
y si el modulo es 0 entonces el número es divisible entre 3. Dividimos 9/3, esto nos da 3, por lo tanto el 27 es Múltiplo de 3.

Un número es múltiplo de otro si lo contiene varias veces exactamente.
Un número a es múltiplo de otro b cuando es el resultado de multiplicar éste último por otro número c.

"""
