"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""

def remove_exclamation_marks(s):
    return s.replace("!", "") 

print(remove_exclamation_marks("!!hola!"))

#primera solucion q se me habia ocurrido
"""
def remove_exclamation_marks(s):
    letra = s.replace("!", "")
    return letra
    """