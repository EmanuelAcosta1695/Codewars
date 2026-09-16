#codigo de otro. nunca use re
def sp_eng(sentence: str) -> bool:
    result = re.search(r'english', sentence, re.IGNORECASE)
    return True if result else False

#1era simplificacion q hice
import re
def sp_eng(sentence: str) -> bool:
    return True if re.search(r'english', sentence, re.IGNORECASE) else False

#2da simplificacion que hice
import re
def sp_eng(sentence):
    return True if re.search(r'english', sentence, re.IGNORECASE) else False

"""
Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".

The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.

Upper or lower case letter does not matter -- "eNglisH" is also correct.

Return value as boolean values, true for the string to contains "English", false for it does not.
"""