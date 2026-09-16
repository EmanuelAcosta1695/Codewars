def abbrev_name(name):
    firstLetter = name[0].upper()
    secondLetter = name[name.find(' ')+1].upper()
    return firstLetter + "." + secondLetter

print(abbrev_name("Sam Harris"))


"""
ejercicio:

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F



"""