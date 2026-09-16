"""
Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

"""

def fake_bin(x:str):
    my_str = [] 
    for num in x:
        if int(num) >= 5:
            num = 1
            my_str.append(num)
        else:
            num = 0
            my_str.append(num)
    return (''.join(map(str, my_str)))


def fake_bin(x):
    return ''.join('0' if c < '5' else '1' for c in x)