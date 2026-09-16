def reverse_words(text:str):
    x = ""
    if "  " in text:
        for i in text.split():
            x += "  " + "".join(reversed(i))
        return x.strip()
    elif "   " in text:
        for i in text.split():
            x += "   " + "".join(reversed(i))
        return x.strip()
    else:
        for i in text.split():
            x += " " + "".join(reversed(i))
        return x.strip()

"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""
