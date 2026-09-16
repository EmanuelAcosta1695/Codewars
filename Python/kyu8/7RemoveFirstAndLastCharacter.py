def remove_char(s):
    word = s
    count = 0
    for x in s:
        if x == '':
            count+1
    cutWord = ""
    cutWord = str(word[1:count-1])
    return cutWord

print(remove_char('eloquent'))

#simplificado (YO)
"""
def remove_char(s):
    word = s
    count = 0
    for x in s:
        if x == '':
            count+1

    return word[1:count-1]
"""

#mas simplificado aun (YO) (La que envie)
"""
def remove_char(s):
    num = len(s)
    return s[1:num-1]
"""