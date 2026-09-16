def reverse_words(s):
    res=[]
    for word in s.split(" "):
        res.append(word)
        
    return " ".join(res[::-1])

"""
Explanation:

1.declare an empty list 'res'
2.split 's' using split("  ")
3.append each word to list 'res'
4.reverse the list 'res'
5.join res using join(" ") by adding spaces

1.declarar una lista vacía 'res' 
2.dividir 's' usando dividir ("") 
3.añada cada palabra a la lista 'res' 
4.revierte la lista 'res' 
5.unir res usando join ("") agregando espacios

"The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

"""