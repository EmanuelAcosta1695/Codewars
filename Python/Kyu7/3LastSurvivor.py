def last_survivor(letters, coords):
    new_letters = list(letters)
    for pos in coords:
        new_letters.pop(pos)
    return ''.join(new_letters)

"""
You are given a string of letters and an array of numbers.
The numbers indicate positions of letters that must be removed, in order, starting from the beginning of the array.
After each removal the size of the string decreases (there is no empty space).
Return the only letter left.

Example:

let str = "zbk", arr = [0, 1]
    str = "bk", arr = [1]
    str = "b", arr = []
    return 'b'
"""
