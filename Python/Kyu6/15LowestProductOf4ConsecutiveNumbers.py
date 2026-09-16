def lowest_product(input):
    listM = []
    listR = []
    for x in input:
        listM.append(int(x))
        if len(listM) == 4:
            listR.append(listM[0] * listM[1] * listM[2] * listM[3])
            listM.pop(0)
    return min(listR) if listR else "Number is too small"

"""
Cree una función que devuelva el producto más bajo de 4 dígitos consecutivos en un
número dado como una cadena.

Esto solo debería funcionar si el número tiene 4 dígitos o más. Si no, devuelve
"El número es demasiado pequeño".
"""
