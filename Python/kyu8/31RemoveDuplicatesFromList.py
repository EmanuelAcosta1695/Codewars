#no pude simplificarlo y lo hice con ayuda. no terminaba de descifrar la logica
def distinct(seq):
    myList = []
    for i in seq:
        if i not in myList:
            myList.append(i)
    return myList

"""
Define a function that removes duplicates from an array of numbers and returns it as a result.

The order of the sequence has to stay the same.
"""