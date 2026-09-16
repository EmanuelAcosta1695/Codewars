import math
def heron(a, b, c):
    s = (a + b + c)/2
    return round(math.sqrt(s * (s - a) * (s - b) * (s - c)),2)

"""
Write function heron which calculates the area of a triangle with sides a, b, and c.

Heron's formula: sqrt (s * (s - a) * (s - b) * (s - c)), where s = (a + b + c) / 2. Output should have 2 digits precision.
"""
