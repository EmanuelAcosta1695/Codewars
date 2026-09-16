def order(sentence):
    list1 = []
    list2 = []
    for x in sentence.split():
        list1.append(x)
        list2.append(1)
    for x in list1:
        for y in x:
            if y.isdigit():
                list2[int(y)-1] = x
    return ' '.join(word for word in list2)

"""
Your task is to sort a given string. Each word in the string will contain a single number.
This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""
