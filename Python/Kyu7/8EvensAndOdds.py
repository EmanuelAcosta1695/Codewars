def evens_and_odds(n):
    if n % 2 == 0:
        return bin(n)[2:]
    else:
        return hex(n)[2:]

"""
This kata is about converting numbers to their binary or hexadecimal representation:

If a number is even, convert it to binary.
If a number is odd, convert it to hex.
"""
