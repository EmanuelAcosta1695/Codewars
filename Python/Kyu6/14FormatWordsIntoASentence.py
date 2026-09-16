def format_words(words):
    string = ""
    if words == None or words == [] or words == [""]:
        return ""
    for x in words[:]:
        if x == "":
            words.remove(x)
    if len(words) == 1:
        return "".join(words[0])
    elif len(words) == 2:
        return "{} and {}".format(words[0], words[1])
    elif len(words) > 2:
        for y, x in enumerate(words):
            if y == 0:
                string += x
            elif y > 0 and y < len(words)-1:
                string += ", " + x
            elif y == len(words)-1:
                string += " and " + x
        return string

"""
Complete the method so that it formats the words into a single comma separated value.
The last word should be separated by the word 'and' instead of a comma. The method takes
in an array of strings and returns a single formatted string.

Note:
-Empty string values should be ignored.

-Empty arrays or null/nil/None values being passed into the method should result in an
empty string being returned.

Example: (Input --> output)

['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
['ninja', '', 'ronin'] --> "ninja and ronin"
[] -->""


"""
