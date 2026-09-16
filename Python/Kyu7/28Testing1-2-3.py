def number(lines):
    num = 0
    list = []
    for i in lines:
        num = num + 1
        list.append("%s: %s" % (num, i))
    return list

"""
Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.

Write a function which takes a list of strings and returns each line prepended by the correct number.

The numbering starts at 1. The format is n: string. Notice the colon and space in between.

Examples:

number([]) # => []
number(["a", "b", "c"]) # => ["1: a", "2: b", "3: c"]

"""
