def camelize(str_):
    words = ""
    list1 = []
    str_ += " "
    for x in str_:
        if x.isalnum():
            words += "".join(x.lower())
        else:
            neword = ""
            for x, y in enumerate(words):
                    if x == 0:
                        neword += y.upper()
                    else:
                        neword += y
            if neword not in list1:
                list1.append(neword)
                words = ""
    return ("".join(x for x in list1))

"""
You must create a method that can convert a string from any format into PascalCase. This must support symbols too.

Don't presume the separators too much or you could be surprised.

For example: (Input --> Output)

"example name" --> "ExampleName"
"your-NaMe-here" --> "YourNameHere"
"testing ABC" --> "TestingAbc"
"""
