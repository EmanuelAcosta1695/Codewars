def to_camel_case(text: str):
    newString = ""
    if text != '' and text != ' ':
        newString += text[0]
    for y, x in zip(text[:-1], text[1:]):
        if x == "_" or x == "-":
            pass
        elif y == "_" or y == "-":
            newString += x.upper()
        else:
            newString += x
    return newString

"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).
"""
