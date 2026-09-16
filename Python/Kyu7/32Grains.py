def square(number):
    resultado = 0
    for i in range(number+1):
        if i == 1:
            resultado = 1
        elif i > 1:
            resultado = resultado * 2
    return resultado

"""
Write a program that calculates the number of grains of wheat on a specific
square of chessboard given that the number on each square is double the
previous one.

There are 64 squares on a chessboard.

#Example: square(1) = 1 square(2) = 2 square(3) = 4 square(4) = 8 etc...

Write a program that shows how many grains were on each square.
"""
