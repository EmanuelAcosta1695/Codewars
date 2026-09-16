def get_middle(s:str):
    import math
    if len(s)<3:
        return s
    return s[int(len(s)/2-1):int(len(s)/2+1)] if len(s)%2 == 0 else s[math.ceil(len(s)/2)-1]

"""
You are going to be given a word. Your job is to return the middle character of the word.
If the word's length is odd, return the middle character. If the word's length is even,
return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
"""
