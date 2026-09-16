def solution(s: str):
    lista = []
    x = 0
    if len(s) % 2 == 0:
        while x < len(s):
            for i in s[x]:
                for e in s[x+1]:
                    x = x + 2
                    lista.append(i+e)
        return lista
    else:
        s= s+"_"
        while x < len(s):
            for i in s[x]:
                for e in s[x+1]:
                    x = x + 2
                    lista.append(i+e)
        return lista

"""
Complete the solution so that it splits the string into pairs of two characters.
If the string contains an odd number of characters then it should replace the
missing second character of the final pair with an underscore ('_').

Examples:

solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']
"""
