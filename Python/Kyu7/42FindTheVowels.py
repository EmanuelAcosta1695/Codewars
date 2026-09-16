def vowel_indices(word):
    vocals = ["a", "e", "i", "o", "u", "y"]
    pos = []
    for x, y in enumerate(word.lower()):
        if y in vocals:
            pos.append(x+1)
    return(pos)

"""
We want to know the index of the vowels in a given word, for example, there are two
vowels in the word super (the second and fourth letters).

So given a string "super", we should return a list of [2, 4].

Some examples:
Mmmm  => []
Super => [2,4]
Apple => [1,5]
YoMama -> [1,2,4,6]
NOTES
Vowels in this context refers to: a e i o u y (including upper case)
This is indexed from [1..n] (not zero indexed!)
"""
