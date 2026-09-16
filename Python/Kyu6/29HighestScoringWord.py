import string
def high(x):
    abc = list(string.ascii_lowercase)
    new_score = 0
    for y in x.split():
        old_score = 0
        for z in y.strip():
            old_score += abc.index(z)+1
        if old_score > new_score:
            new_score = old_score
            highscore = y
    return highscore

"""
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
